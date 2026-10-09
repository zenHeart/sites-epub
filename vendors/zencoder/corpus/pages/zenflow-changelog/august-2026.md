> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# August 2026

> Dedicated troubleshooting UI, log export, task automations for on-call, and reliability improvements

# August 2026 — Zenflow Updates

August shipped Zenflow Desktop 2.3.0 through 2.3.4, focused on **operability**: a redesigned troubleshooting surface, one-click log export, and new task automations aimed at on-call and platform teams.

## New Features

### Redesigned Troubleshooting Surface

<Card title="Find Fixes Faster" icon="triangle-exclamation" color="#F24A07">
  A dedicated Troubleshooting section brings common issues, logs, and reporting into one place.
</Card>

Zenflow Desktop now has a **Troubleshooting** section reachable from Settings and the Help menu, with dedicated pages for common issues, log locations, and how to file a report.

***

### One-Click Log Export

<Card title="Attach Logs Without the File-System Hunt" icon="download" color="#10B981">
  Export a scrubbed, zipped log bundle for support in a single click.
</Card>

**Help → Export Logs** produces a zip of the last 24 hours of logs with common secret patterns redacted — ready to attach to a support ticket.

***

### On-Call Automation Template

A new **On-Call Assistant** automation ships out of the box — connects to PagerDuty and Sentry to triage incoming alerts, summarize stack traces, and draft an initial response.

***

### Task Automations: Custom Cron

Scheduled automations now accept **custom cron expressions** in addition to the preset intervals, unlocking finer control over when jobs run.

***

### Slack Threaded Replies

The Slack integration can now **reply in-thread** to the message that triggered an action, keeping conversations clean when Zenflow is invoked from a busy channel.

***

### Multi-Model: Reviewer Model Override

In the **Multi-model workflow**, you can now assign a different model specifically to the review phase without changing your planning or implementation models.

***

## Improvements

### Performance

* **Log streaming latency** reduced under sustained agent activity
* **Faster cold start** on macOS via lazy-loaded panels
* **Lower memory usage** for long-running orchestrated tasks

### UI and UX

* **Troubleshooting entry point** in the Help menu and Settings sidebar
* **Copy Operation ID** action on every assistant message
* **Task Logs tab** now supports search and severity filters
* **Integration health indicators** in Settings → Integrations show last-successful-call timestamp
* **Compact chat density** setting for smaller screens
* **Reveal in Folder** now works for git-worktree paths as well as workspace files

### Reliability

* **Auto-recovery** for stuck task executions after network drops
* **Safer update installer** with rollback on partial failures
* **OAuth flow** hardened against premature tab closes across all providers
* **Retry with agent** now available on more failure classes, not just Git hook errors

***

## Bug Fixes

* Fixed **task history not scrolling** to newest entry after long runs
* Fixed **MCP tool permissions** dialog appearing behind main window on Windows
* Fixed **notification sound** playing after task cancellation
* Fixed **duplicate integration entries** appearing after reconnect
* Fixed **built-in browser** losing session cookies on tab reload
* Fixed **prompt editor** losing selection when switching between drafts
* Fixed **Pipedream** connector timing out silently on cold invocations
* Fixed **rare data race** when two subagents wrote to the same worktree file

***

<Accordion title="Version History">
  * **v2.3.4** (August 26, 2026)
  * **v2.3.3** (August 19, 2026)
  * **v2.3.2** (August 12, 2026)
  * **v2.3.1** (August 8, 2026)
  * **v2.3.0** (August 4, 2026)
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.