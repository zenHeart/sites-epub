> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting

> Diagnose and resolve issues with Zenflow Desktop — common fixes, log locations, debug mode, and how to file a great bug report.

## Get Help

<CardGroup cols={3}>
  <Card title="Discord Community" icon="discord" href="https://discord.com/invite/zencoder">
    Ask questions, share workflows, and get real-time help from the community and Zencoder team.
  </Card>

  <Card title="Email Support" icon="envelope" href="mailto:support@zencoder.ai">
    For account issues, billing, or anything sensitive — **[support@zencoder.ai](mailto:support@zencoder.ai)**
  </Card>

  <Card title="YouTube Tutorials" icon="youtube" href="https://www.youtube.com/@zencoderai">
    Video walkthroughs of Zenflow features, workflows, and setup guides.
  </Card>
</CardGroup>

<Note>
  If you're behind a VPN, proxy, or corporate firewall, mention that in your report — it often affects agent connectivity.
</Note>

***

## Common Issues

<AccordionGroup>
  <Accordion title="Agent not responding">
    **Causes:** Agent authentication expired, network interruption, or service unavailable.

    **Fix:** Sign out and sign back into the agent in **Settings → Saved presets**. Check your internet connection and retry. If the issue persists, restart Zenflow Desktop.
  </Accordion>

  <Accordion title="Task stuck in progress">
    **Causes:** Long-running verification step, network timeout, or workspace lock.

    **Fix:** Check task logs for the last completed step. If stuck for more than 10 minutes, cancel and retry the task. See the [Logs](#logs--debug-info) section below for how to inspect execution logs.
  </Accordion>

  <Accordion title="Installation failures">
    **Causes:** Insufficient permissions, conflicting software, or corrupted download.

    **Fix:** Run the installer as administrator (Windows) or with `sudo` (macOS). Temporarily disable antivirus if the download is being blocked. Re-download the installer from the official site if the file is corrupted.
  </Accordion>

  <Accordion title="Workspace or git errors">
    **Causes:** Git conflicts, permission issues, or insufficient disk space.

    **Fix:** Ensure you have write permissions and at least 2 GB free disk space in your workspace directory. Run `git status` in the worktree to check for conflicts. Zenflow uses [git worktrees](/zenflow/git-worktrees) — verify they aren't corrupted.
  </Accordion>

  <Accordion title="Blank / gray screen on launch">
    **Causes:** GPU acceleration conflict, stale cache, or corrupted app state.

    **Fix:** Quit Zenflow, then relaunch with GPU acceleration disabled. On macOS: `open -a Zenflow --args --disable-gpu`. On Windows: launch from a terminal with `zenflow.exe --disable-gpu`. If the issue persists, clear the app cache directory (see [Cache & App Data](#cache--app-data) below).
  </Accordion>

  <Accordion title="Updates not installing">
    **Causes:** Blocked download, installer permissions, or antivirus interference.

    **Fix:** In **Settings → About**, click **Check for updates**. If the installer silently fails, download the latest build manually from your account portal and reinstall.
  </Accordion>

  <Accordion title="Integration / MCP tool won't connect">
    **Causes:** OAuth flow closed prematurely, expired token, or missing scopes.

    **Fix:** Reconnect the integration from **Settings → Integrations**. If the OAuth tab closes before completing, disable popup blockers and retry. See [Integrations & MCP](/zenflow/integrations) for provider-specific guidance.
  </Accordion>

  <Accordion title="Built-in browser not loading pages">
    **Causes:** Missing system webview component, network restrictions, or a corrupt browser tab.

    **Fix:** Close and reopen the browser tab. If pages still fail, disable the built-in browser in **Settings → General** and use your system browser instead. See [Built-in Browser](/zenflow/built-in-browser) for details.
  </Accordion>
</AccordionGroup>

***

## Logs & Debug Info

When something goes wrong, the fastest path to a fix is a good log file. Logs capture what the app, agents, and integrations were doing at the moment the issue occurred. Logs are stored **locally** and are **never transmitted automatically**.

### Log File Locations

<Tabs>
  <Tab title="macOS">
    ```bash theme={"system"}
    ~/Library/Application Support/zenflow-desktop/logs/
    ```

    Open in Finder:

    ```bash theme={"system"}
    open ~/Library/Application\ Support/zenflow-desktop/logs/
    ```
  </Tab>

  <Tab title="Windows">
    ```
    C:\Users\<username>\AppData\Roaming\zenflow-desktop\logs\
    ```

    Open in Explorer:

    ```powershell theme={"system"}
    explorer "%APPDATA%\zenflow-desktop\logs"
    ```
  </Tab>

  <Tab title="Linux">
    ```bash theme={"system"}
    ~/.config/zenflow-desktop/logs/
    ```

    Open in your file manager:

    ```bash theme={"system"}
    xdg-open ~/.config/zenflow-desktop/logs/
    ```
  </Tab>
</Tabs>

The most recent log is `main.log`. Older rotations are numbered (`main.1.log`, `main.2.log`, …).

### Log Categories

| File | What it contains |
| - | - |
| `main.log` | App lifecycle, window state, updater events |
| `renderer.log` | UI events, chat interactions, panel state |
| `agent.log` | Agent execution, tool calls, model responses |
| `cli.log` | ZenCLI, Claude Code, Codex, Gemini invocations |
| `integrations.log` | OAuth flows, MCP tool activity, webhook events |
| `git.log` | Git worktree operations, commits, diffs |

### Enabling Debug (Verbose) Logging

<Steps>
  <Step title="Open Settings">
    Go to **Settings → Advanced**.
  </Step>

  <Step title="Enable Debug Mode">
    Toggle **Enable debug logging**.
  </Step>

  <Step title="Reproduce the issue">
    Trigger the problem right after enabling debug mode so the log captures it cleanly.
  </Step>

  <Step title="Disable when done">
    Turn debug logging back off after you've captured what you need — verbose logs grow quickly.
  </Step>
</Steps>

<Tip>
  You can also launch Zenflow with the `--verbose` flag from a terminal to enable debug logging for a single session without changing your settings.
</Tip>

### Viewing Logs in the App

* **View → Toggle Developer Tools** opens the built-in DevTools console (renderer logs).
* **Help → Show Logs** reveals the log directory in your file manager.
* **Help → Export Logs** creates a scrubbed, zipped bundle of the last 24 hours for support.
* Task-level execution logs live inside each task's **Logs** tab.

### Operation IDs

Every request to Zenflow's backend has a unique **Operation ID**. Sharing this ID with support lets us trace exactly what happened.

* Open any assistant message and click the **⋯** menu → **Copy Operation ID**.
* For ZenCLI, the Operation ID is printed in the response header and surfaced in the UI.

Include the Operation ID whenever you file a bug or reach out to support.

### Cache & App Data

If Zenflow won't start or behaves inconsistently, clearing the cache is often the fastest fix. **This does not delete your tasks** — those live in your workspace directory.

<Tabs>
  <Tab title="macOS">
    ```bash theme={"system"}
    rm -rf ~/Library/Application\ Support/zenflow-desktop/Cache/
    rm -rf ~/Library/Application\ Support/zenflow-desktop/GPUCache/
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={"system"}
    Remove-Item -Recurse -Force "$env:APPDATA\zenflow-desktop\Cache"
    Remove-Item -Recurse -Force "$env:APPDATA\zenflow-desktop\GPUCache"
    ```
  </Tab>

  <Tab title="Linux">
    ```bash theme={"system"}
    rm -rf ~/.config/zenflow-desktop/Cache/
    rm -rf ~/.config/zenflow-desktop/GPUCache/
    ```
  </Tab>
</Tabs>

<Warning>
  Deleting anything **outside** the `Cache` and `GPUCache` folders can wipe your Zenflow settings, saved presets, and integration connections. Only delete those two folders unless support asks otherwise.
</Warning>

### Sharing Logs Safely

* **Scrub secrets**: search for tokens, API keys, and email addresses. Redact anything sensitive.
* **Trim to the incident window**: attach only the minutes around the failure.
* **Prefer zipped uploads**: compress the `logs/` folder into a single archive.

***

## Reporting an Issue

### Before You Report

1. Check [Common Issues](#common-issues) above for a known fix.
2. Make sure you're on the latest build (**Settings → About → Check for updates**).
3. Try to reproduce the issue in a fresh task — sometimes it's task-state specific.

### What to Include

<Steps>
  <Step title="Gather basic info">
    * **App version**: Settings → About (e.g., `Zenflow Desktop v2.3.4 build 612`)
    * **OS**: Version and architecture (e.g., `macOS 14.4 - Apple Silicon M2`, `Windows 11 23H2`)
    * **Agent / model**: Which agent and model were active
  </Step>

  <Step title="Document the issue">
    * **Timestamps**: When did it happen? Include your timezone.
    * **Steps to reproduce**: What were you doing when the error occurred? Number the steps.
    * **Expected vs. actual behavior**: One sentence each.
    * **Screenshots or recordings**: Capture any error messages or unexpected UI state.
  </Step>

  <Step title="Attach logs and Operation ID">
    Grab the relevant log files (see [Logs & Debug Info](#logs--debug-info)) and include the **Operation ID** for the failing request.
  </Step>

  <Step title="Send it">
    Email **[support@zencoder.ai](mailto:support@zencoder.ai)** or post in **#support** on [Discord](https://discord.com/invite/zencoder).
  </Step>
</Steps>

### Bug Report Template

```markdown theme={"system"}
### Summary
<one-line description>

### Environment
- Zenflow version:
- OS + version:
- Agent + model:
- Integrations involved:

### Steps to Reproduce
1.
2.
3.

### Expected Behavior


### Actual Behavior


### Operation ID / Task ID


### Attachments
- logs.zip
- screenshot / recording
```

### Screen Recordings

For UI glitches or hard-to-describe issues, a short recording is worth a thousand words. Tools like [Loom](https://www.loom.com), the built-in macOS screenshot recorder (`Shift+Cmd+5`), or Windows Xbox Game Bar (`Win+G`) work well.

### Sensitive Data

* In public channels (Discord, Reddit), redact tokens, private repos, and customer data.
* For anything sensitive, use email — **[support@zencoder.ai](mailto:support@zencoder.ai)** — and mention "sensitive" in the subject line.
* Include the email address on your Zencoder account so we can locate your workspace quickly.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.