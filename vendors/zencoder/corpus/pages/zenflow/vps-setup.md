> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# VPS Setup

> Set up Zenflow on a public VPS for browser-based access.

For private desktop access over SSH without exposing Zenflow to the internet, see [Remote Hosts](/zenflow/remote-hosts).

## Public HTTPS VPS (browser access)

To set up a publicly reachable VPS instead, follow the instructions below or watch the DigitalOcean walkthrough.

<iframe src="https://www.youtube.com/embed/Tn7A7LGHlEE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style={{ width: '100%', height: '405px', borderRadius: '0.5rem' }} />

<Card title="Public VPS requirements" icon="server">
  For this browser-access setup, allow HTTP and HTTPS traffic to the instance. The private SSH setup above does not need either port open.
</Card>

<Tabs>
  <Tab title="Digital Ocean">
    1. Log into [DigitalOcean](https://www.digitalocean.com)
    2. Click **Create** dropdown and select **Droplets**
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/create.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=a9dbc910ee28ba5c4e45c21b618b6c83" alt="create menu dropdown" width="3808" height="430" data-path="images/vps/do/create.png" />
    3. Choose the region based on your requirements
    4. Choose **Ubuntu 24.04** for the OS (the default image)
    5. Droplet size depends on your needs - if you expect Zenflow to execute heavy tasks (e.g. compiling code), you might want to create larger droplet. Or you can start with the default
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/droplet.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=82dd3ce56ef5bc52647cddb47721eaad" alt="droplet OS and size settings" width="2830" height="2228" data-path="images/vps/do/droplet.png" />
    6. Choose and set up your authentication method
    7. Optionally rename the droplet to something meaningful, like `Zenflow`
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/hostname.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=0ec6e23c1d606b62a74f6d3aada00072" alt="hostname set to Zenflow" width="2486" height="798" data-path="images/vps/do/hostname.png" />
    8. Click **Create Droplet** button
    9. After droplet gets created, connect to it either using terminal or through Digital Ocean's **Access console**
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/access-console.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=afc25fd397447201a31ade69862b7fe6" alt="menu with access console option" width="2502" height="868" data-path="images/vps/do/access-console.png" />
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/launch-console.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=92fa0b9f54d6ab0838fe13c4bf388b90" alt="button to launch droplet console" width="2484" height="970" data-path="images/vps/do/launch-console.png" />
  </Tab>

  <Tab title="Google Cloud">
    1. Log into [Google Cloud console](https://console.cloud.google.com/)
    2. Search for **compute engine** in a search bar
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/gcp/search.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=76796375e7c4acb7d3e8443f061ea619" alt="gcp search bar with compute engine" width="2786" height="271" data-path="images/vps/gcp/search.png" />
    3. Select **Compute Engine** from search results and click **Create instance** button
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/gcp/create-instance-button.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=89019b25ae46b7e3e34fcc657857f215" alt="gcp create instance button" width="981" height="206" data-path="images/vps/gcp/create-instance-button.png" />
    4. At **Machine configuration** step set **Name**, **Region**, **Zone** and **Machine type** based on your needs (if you expect Zenflow to execute heavy tasks (e.g. compiling code), you might want to create larger instance. Or you can start with the default)
    5. At **OS and storage** step set the image to Ubuntu 24.04. Optionally also adjust boot disk type and size or attach extra disks as per your needs
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/gcp/os.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=e2af3e72ec637ff968a718af90571d6b" alt="gcp os image settings" width="3840" height="1323" data-path="images/vps/gcp/os.png" />
    6. At **Networking** step in **Firewall** section make sure to check **Allow HTTP traffic** and **Allow HTTPS traffic** checkboxes
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/gcp/network.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=9c55abc5be816c36e6a812be6a1e2b5d" alt="gcp network firewall allow https traffic" width="1120" height="716" data-path="images/vps/gcp/network.png" />
    7. Set the rest of the settings according to your needs. Once all is set, click **Create** button
    8. After instance gets created, connect to it either using terminal or through Google Cloud's in-browser connection tool
           <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/gcp/in-browser-connection.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=03d04670533f3f63a2fa99bf665d917f" alt="button to launch gcp's in-browser console" width="775" height="478" data-path="images/vps/gcp/in-browser-connection.png" />
  </Tab>
</Tabs>

Once you are connected to the VPS:

1. Create non-root user with desired name (for example, `zenflow`), give it sudo rights and switch to the user:

```bash theme={"system"}
adduser zenflow
usermod -aG sudo zenflow
su - zenflow
```

2. Run the following command to download and execute set up script:

```
curl -fsSL https://download.zencoder.ai/releases/vps_setup.sh | sudo bash
```

3. After initial setup the script will ask you to create API key at [https://auth.zencoder.ai/api-keys](https://auth.zencoder.ai/api-keys)
   <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/api-key-request.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=bf11f2932fc180df4575efeb04a89cf0" alt="api key request" width="1470" height="503" data-path="images/vps/do/api-key-request.png" />
4. On that page click **Add**, give the API key a name and click **Create**. You will be shown the API key, store it in a secure place, it is only shown **once**
   <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/api-key-creation.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=b3a262a7585cd0e82eb6c0d1473e62db" alt="api key creation menu" width="3840" height="1446" data-path="images/vps/do/api-key-creation.png" />
5. Go back to your VPS and paste the API key
6. You will then be shown the URL at which you can access Zenflow and credentials (username/password)
   <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/credentials.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=aac379cc41f2c5aa8a7de8891c04cfde" alt="url and credentials" width="832" height="410" data-path="images/vps/do/credentials.png" />
7. When you visit the URL, you'll be prompted for Username/Password from the previous step
   <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/cred-menu.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=93098010624c5255b99367795458fda7" alt="credentials request modal" width="748" height="548" data-path="images/vps/do/cred-menu.png" />
8. Once logged in, you'll see the onboarding screen of Zenflow and now can work with it through browser remotely
   <img src="https://mintcdn.com/forgoodaiinc/WhjbItcZWqNCzwRt/images/vps/do/onboarding-screen.png?fit=max&auto=format&n=WhjbItcZWqNCzwRt&q=85&s=b3c16212aab305fd2b686d30e3e5e15e" alt="onboarding first screen" width="2320" height="1562" data-path="images/vps/do/onboarding-screen.png" />


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.