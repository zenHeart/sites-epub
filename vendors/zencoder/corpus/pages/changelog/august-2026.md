> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# August 2026

> Structured logs panel, MCP tool audit trail, expanded reasoning-effort support, and stability fixes across VS Code and JetBrains

## Better Debuggability, Broader Model Reach

August 2026 focuses on making the IDE Agent easier to inspect when something goes wrong — a new structured logs panel, an MCP tool audit trail, and expanded reasoning-effort support across additional models.

## New Features

### Structured Logs Panel

<Card title="Inspect Agent Runs Without Leaving the IDE" icon="file-lines" color="#F24A07">
  A new panel surfaces agent execution logs — tool calls, model responses, and errors — filtered by task.
</Card>

The IDE Agent now ships a **structured logs panel**. Filter by severity, tool, or time range and copy the whole trace with a single Operation ID so support can reproduce your session end-to-end.

***

### MCP Tool Audit Trail

<Card title="See Every External Tool Call" icon="shield-check" color="#10B981">
  Every MCP tool invocation is now logged with inputs, outputs, and duration.
</Card>

The plugin records every MCP call the agent makes, so you can audit exactly which external tools ran, what they returned, and how long they took — visible in the new logs panel.

***

### Expanded Reasoning-Effort Support

Reasoning-effort selection (introduced in July) now works with additional models, including Claude Sonnet 5 and GPT-5.6, giving you finer control over depth-vs-speed across more of your workflow.

***

### Zencoder Agent CLI Update

The bundled `zencli` build now includes the July/August model updates and a faster startup path — cold starts are noticeably quicker on JetBrains.

***

## Improvements

* **Copy Operation ID** now available directly from any assistant message's overflow menu
* **Debug logging toggle** exposed in plugin settings without editing config files
* **JetBrains log viewer** integration — Zencoder logs stream into the IDE's Log tool window
* **Faster indexing** for large monorepos on first open
* **Reduced memory footprint** during long chat sessions

***

## Bug Fixes

* Fixed occasional **duplicate messages** when sending rapidly on VS Code
* Fixed **OAuth reconnect** loop when a corporate proxy stripped cookies
* Fixed **MCP tool timeout** not surfacing in the UI
* Fixed **rare crash** when pasting extremely large files into chat
* Fixed **JetBrains gutter icon** not clearing after task completion
* Various stability improvements

***

<Accordion title="Version History">
  <Tabs>
    <Tab title="VS Code">
      * **3.72** (August 25, 2026)
      * **3.70** (August 12, 2026)
    </Tab>

    <Tab title="JetBrains">
      * **3.33.0** (August 25, 2026)
      * **3.32.0** (August 12, 2026)
    </Tab>
  </Tabs>
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.