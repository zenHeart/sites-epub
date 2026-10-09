> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# SubAgents

> Run specialized agents as sub-processes with different contexts, models, and tools

SubAgents allow you to run a different agent as a sub-process of the current (master) agent. This enables powerful orchestration patterns where tasks are delegated to specialized agents with isolated contexts, different models, or even different CLIs.

## What is a SubAgent?

A SubAgent is technically an MCP tool call that returns its result back to the master agent. Each SubAgent can have:

* **Different context**: The master agent decides what information to pass downstream, keeping the SubAgent focused on its specific task
* **Different tools**: Tool availability can vary depending on task requirements (e.g., SubAgents don't have the Ask tool since UI interaction happens through the master agent)
* **Different model or CLI**: Run SubAgents with a different LLM model or even a completely different CLI runtime

## Why SubAgents?

<CardGroup cols={3}>
  <Card title="Specialization" icon="crosshairs">
    SubAgents don't carry the "garbage" from the current session, resulting in higher quality outputs for focused tasks
  </Card>

  <Card title="Cost Efficiency" icon="coins">
    SubAgents can run with simpler, cheaper models for tasks that don't require the full power of a frontier model
  </Card>

  <Card title="Orchestration" icon="sitemap">
    Run different models in parallel for "best of N" scenarios out of the box with ZenCLI
  </Card>
</CardGroup>

## How to Use SubAgents

SubAgents are available at three levels:

### 1. General SubAgent Tool

The SubAgent capability is always available with ZenCLI. You can invoke SubAgents directly in chat:

* `"Run /skillX as subagent"`
* `"Research Y with subagent using model Z"`

### 2. Automatic Usage via System Prompts and Skills

ZenCLI may automatically decide to use SubAgents for certain tasks, such as planning, exploration, or code review.

<Tip>
  Check out the `/comprehensive-review` skill for an example of SubAgent-powered code review that provides thorough, multi-perspective feedback.
</Tip>

### 3. Native UI Features

SubAgents power built-in plugin features like **Get Second Opinion**, which works similarly to Zenflow but uses SubAgents under the hood.

## Using Different CLIs for SubAgents

To enable different CLI runtimes for SubAgents, add the following to `~/.zencoder/settings.json`:

```json theme={"system"}
{
  "availableRuntimes": ["zencoder", "claude", "codex"]
}
```

When configured:

* Adding `claude` to available runtimes routes all SubAgents using Anthropic models through Claude Code
* Adding `codex` enables OpenAI Codex as a SubAgent runtime
* The root agent always uses the CLI selected in the UI

<Note>
  SubAgents are supported for all CLIs when used through the ZenCLI adapter. One limitation is that parallel SubAgents are not yet supported for Claude Code.
</Note>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.