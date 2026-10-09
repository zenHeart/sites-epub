> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# April 2026

> GPT 5.5 and Claude Opus 4.7 support, auto permission mode, image generation, new agent-browser skill, and improved model experience

## New Models, Smarter Agents, and Better Control

April 2026 brings major model updates, a new auto permission mode for faster workflows, image generation built in, and a smoother experience for managing agents and models in your IDE.

## New Features

### GPT 5.5 Support

The latest frontier model from OpenAI is now available in Zencoder. Use GPT 5.5 for your most complex tasks — planning, debugging, and research workflows.

***

### Claude Opus 4.7 with Streaming Thinking

Claude Opus 4.7 is now supported with **streaming thinking** — watch the model's reasoning process in real time as it works through your problem.

***

### Auto Permission Mode

<Card title="Hands-Free Agent Execution" icon="bolt" color="#F24A07">
  Let the agent run without pausing for approvals on every action.
</Card>

A new **Auto permission mode** for Claude Code lets agents execute without manual approval at each step. Ideal for trusted workflows where you want the agent to move fast.

***

### Image Generation

<Card title="Generate Images in Chat" icon="image" color="#10B981">
  Ask the agent to create images — logos, diagrams, mockups — right inside your IDE.
</Card>

Image generation is now enabled by default. Ask the agent to create visuals and see results rendered inline in chat.

***

### Agent-Browser Skill

A new **agent-browser** skill replaces the previous Playwright skill, giving agents improved browser automation capabilities for testing and web interaction tasks.

***

### Frontend Design Skill

A new **built-in frontend-design skill** helps agents generate production-quality UI designs and HTML mockups directly from your descriptions.

***

### MCP Tool Permissions

<Card title="Control Which Tools Agents Can Use" icon="shield-check" color="#9333EA">
  Review and approve MCP tool access before agents use them.
</Card>

Agents now request permission before using MCP tools, giving you visibility and control over which external tools are invoked during a task. You can also configure **"Always allow"** for trusted tools in settings.

***

### Delete Rules from UI

You can now **delete skills** directly from the VS Code and JetBrains UI — no need to manually remove files.

***

## Improvements

### Model and Agent Experience

* **Improved model selector** — clearer display of the current engine and model
* **Optimized system prompts** for Claude 4.6 and GPT 5.4 model families
* **Updated comprehensive review** skill for better multi-model feedback
* **Updated cross-review** skill with improved output quality

### Agent Reliability

* Fixed agent reporting it edited a file when it didn't actually make changes
* Fixed Anthropic models stopping prematurely due to output token limits with adaptive thinking
* Fixed long-running agent sessions failing with MCP tools
* Fixed file edits now written atomically to prevent corruption

### User Experience

* Fixed empty `.zencoder/workflows` folders being created in every project
* Fixed session data corruption in VS Code
* Fixed sound notifications in JetBrains checking project window focus instead of app focus
* Fixed Ask Questions tool working correctly in Codex CLI for both VS Code and JetBrains

***

<Accordion title="Version History">
  <Tabs>
    <Tab title="VS Code">
      * **3.48.0** (April 14, 2026)
    </Tab>

    <Tab title="JetBrains">
      * **3.21.0** (April 14, 2026)
    </Tab>
  </Tabs>
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.