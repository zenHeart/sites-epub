> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Remote Hosts

> Install Zenflow on a remote Ubuntu VM and connect securely from the desktop app over SSH.

Run Zenflow on a remote VM so tasks and agents keep working after you close your laptop. In Zenflow 2.5.1 or later, the desktop app can connect to a remote Zenflow host over SSH. From the app you can create projects and tasks, chat with agents, inspect Git diffs, and use terminals on that host.

In private mode, Zenflow listens on the VM's `127.0.0.1:3000`; the desktop app connects through SSH. You don't need to expose Zenflow over HTTP or HTTPS. If you need browser access through a public URL instead, see [Public HTTPS VPS setup](/zenflow/vps-setup).

For a VM you can already SSH into, follow [Connect an existing Ubuntu VM](#connect-an-existing-ubuntu-vm). For a VM without a public IP, see the [Google Cloud IAP example](#example-create-a-private-google-cloud-vm) first.

## Connect an existing Ubuntu VM

1. [Install Zenflow on your laptop](https://zencoder.ai/download/all) and update it to version 2.5.1 or later.

2. Confirm that SSH works from your laptop to the VM. You need an Ubuntu VM, a non-root account with `sudo`, and an SSH destination such as `user@host` (or an alias in `~/.ssh/config`).

3. SSH into the VM as the account that will run Zenflow, then install Zenflow in private mode:

   ```bash theme={"system"}
   ssh user@host
   curl -fsSL https://download.zencoder.ai/releases/vps_setup.sh | sudo bash -s stable -- --access=private --non-interactive
   ```

   `stable` chooses the release channel (`beta` is also available). `--access=private` keeps the service on loopback without setting up Caddy or opening ports 80/443. `--non-interactive` skips the optional API key prompt; sign in from the desktop app instead. The services run as the account that invoked `sudo`, with application data under that account's `~/.zenflow`. Do not run the installer from a root login.

4. Check that the services and health endpoint are available **on the VM**:

   ```bash theme={"system"}
   sudo systemctl --no-pager status zenflow zenflow-bridge zenflow-update.timer
   curl -fsS http://127.0.0.1:3000/api/health
   /opt/zenflow/bin/server --version
   ```

5. In the desktop app on your laptop, open **Settings → Experimental**, enable **Remote hosts**, and save.

   <img src="https://mintcdn.com/forgoodaiinc/UskliqihHubfKTd-/images/zenflow/remote-hosts-setting.png?fit=max&auto=format&n=UskliqihHubfKTd-&q=85&s=54b373b6cbef04160fbb66eb2a20c719" alt="Enable remote hosts in Zenflow's Experimental settings" width="1540" height="295" data-path="images/zenflow/remote-hosts-setting.png" />

6. Under **Add host**, enter the VM's **SSH destination** (`user@host`, or `user@your-ssh-alias`) and **SSH port** (`22` unless you configured another port). Select the VM from the host switcher in the title bar.

   <img src="https://mintcdn.com/forgoodaiinc/UskliqihHubfKTd-/images/zenflow/remote-host-selector.png?fit=max&auto=format&n=UskliqihHubfKTd-&q=85&s=378bcb8939b242bbaa4d2019f1bb2dbf" alt="Connected remote VM in the Zenflow title-bar host selector" width="485" height="115" data-path="images/zenflow/remote-host-selector.png" />

7. Once connected, sign in, connect GitHub if needed, and create a project and task on the remote host. Install and authenticate Claude Code, Codex, and any other agents you want to run **on the VM** separately; local agent installations and subscriptions do not transfer to it. Zenflow can run tasks without choosing a workflow: enter a task description or paste a task link and select an executor.

<Note>
  Private mode does not require opening port 3000 in the VM's firewall. SSH is the only route from the laptop to the service, including when SSH uses a bastion or an IAP tunnel.
</Note>

## Example: Create a private Google Cloud VM

This optional example uses a GCP Ubuntu 24.04 VM with **no public IP**. Replace `YOUR_PROJECT_ID`, `YOUR_SUBNET`, `YOUR_ZONE`, `jdoe`, the VM name, and the SSH key path with your own values. IAP tunneling requires the appropriate GCP permissions and a firewall rule allowing IAP TCP forwarding to the VM on port 22; arrange those prerequisites before connecting. These commands assume metadata-based SSH keys; if your project enforces OS Login, configure access through OS Login instead.

1. Create the VM (from a terminal with `gcloud` authenticated):

   ```bash theme={"system"}
   gcloud compute instances create jdoe-dev-vm \
     --project YOUR_PROJECT_ID \
     --zone YOUR_ZONE \
     --machine-type e2-highmem-4 \
     --image-family ubuntu-2404-lts-amd64 \
     --image-project ubuntu-os-cloud \
     --boot-disk-size 200GB \
     --subnet YOUR_SUBNET \
     --no-address \
     --shielded-secure-boot \
     --shielded-vtpm \
     --shielded-integrity-monitoring
   ```

2. Add your laptop's public SSH key for the Linux account:

   ```bash theme={"system"}
   gcloud compute instances add-metadata jdoe-dev-vm \
     --zone YOUR_ZONE --project YOUR_PROJECT_ID \
     --metadata ssh-keys="jdoe:$(cat ~/.ssh/id_ed25519.pub)"
   ```

3. Add an SSH alias to `~/.ssh/config` on your laptop, replacing the project and zone with the same values as above:

   ```sshconfig theme={"system"}
   Host gcp-jdoe-dev
     HostName jdoe-dev-vm
     User jdoe
     IdentityFile ~/.ssh/id_ed25519
     IdentitiesOnly yes
     AddKeysToAgent yes
     ProxyCommand gcloud compute start-iap-tunnel %h 22 --listen-on-stdin --zone YOUR_ZONE --project YOUR_PROJECT_ID --verbosity=warning
     ServerAliveInterval 30
   ```

   On macOS, you can also add `UseKeychain yes`. Verify the connection from your laptop:

   ```bash theme={"system"}
   ssh gcp-jdoe-dev true
   ```

   If SSH returns `4003: failed to connect to backend`, check that the VM has finished starting:

   ```bash theme={"system"}
   gcloud compute instances describe jdoe-dev-vm --zone YOUR_ZONE --project YOUR_PROJECT_ID --format='value(status)'
   ```

4. Follow [Connect an existing Ubuntu VM](#connect-an-existing-ubuntu-vm), using `ssh gcp-jdoe-dev` to log in to the VM as `jdoe`. In the desktop app, enter `jdoe@gcp-jdoe-dev` as the SSH destination and `22` as the port. The app uses your SSH configuration, including the IAP `ProxyCommand`. Keep port 3000 closed in the GCP firewall.

## Updates and limitations

The `zenflow-update.timer` service checks for updates about every 30 minutes and installs them when no task is running. On the VM, inspect its logs with `sudo journalctl -u zenflow-update`.

To change the update channel of an existing install, set `UPDATE_CHANNEL=stable` or `UPDATE_CHANNEL=beta` in `/etc/zenflow/env`. **Do not rerun the installer just to switch channels:** it installs the requested release immediately, even if that release is older than the installed version. An older server might not be able to open a database migrated by a newer version.

Remote hosts are generally available but still marked experimental in Settings. Some in-app links may not be clickable, and **Open in local IDE/Finder** cannot open a remote project folder on your laptop.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.