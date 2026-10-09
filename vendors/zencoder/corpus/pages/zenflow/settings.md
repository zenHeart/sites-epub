> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Settings

> Configure preferences, repositories, and profile in Zenflow.

Zenflow settings are organized into sections accessible from the left sidebar. Open settings from the gear icon or **Settings** in the navigation.

## General

<div className="mt-4 flex justify-center">
  <img src="https://mintcdn.com/forgoodaiinc/wAfswEtqaOe9ICOy/images/zenflow/zenflow-settings-general.png?fit=max&auto=format&n=wAfswEtqaOe9ICOy&q=85&s=e07be4c2cffd3c23dc371c93649e0f07" alt="Zenflow General settings showing Code Editor, Tasks, and Notifications sections" style={{ width:"100%", maxWidth:"800px", borderRadius:"12px" }} width="1144" height="720" data-path="images/zenflow/zenflow-settings-general.png" />
</div>

| Setting | Description |
| - | - |
| **Language** | Language the AI agent will use to respond |
| **Default IDE** | Which IDE opens when you click "Open in IDE" (VS Code, Cursor, etc.) |
| **Auto-archive tasks after** | Automatically archive inactive tasks after a set period to save disk space |
| **Sound alerts** | Play a sound when subtasks complete (configurable chime) |
| **Desktop notifications** | System notifications for task events |

## Integrations

Connect Zenflow to external tools. See [Integrations](/zenflow/integrations) for the full list of supported apps (GitHub, Linear, Jira, Slack, Notion, and more).

## Git

Configure how Zenflow handles commits and pushes. See [Tracking Changes](/zenflow/tracking-changes#git-settings) for details.

<div className="mt-4 flex justify-center">
  <img src="https://mintcdn.com/forgoodaiinc/wAfswEtqaOe9ICOy/images/zenflow/zenflow-settings-git.png?fit=max&auto=format&n=wAfswEtqaOe9ICOy&q=85&s=72018b974a771f7a2d172b6519306866" alt="Git settings showing commit mode, auto-commit, and auto-push toggles" style={{ width:"100%", maxWidth:"800px", borderRadius:"12px" }} width="1144" height="720" data-path="images/zenflow/zenflow-settings-git.png" />
</div>

| Setting | Description |
| - | - |
| **Commit mode — Automatic** | Zenflow commits after each agent execution |
| **Commit mode — Instruct AI when to commit** | The agent decides when to commit based on your instructions |
| **Auto-commit changes from agents** | Automatically commit after coding agent executions |
| **Auto-update remote branch** | Automatically push to the remote branch after commits |

## Repositories

Manage connected repositories. Each repository has its own configuration page with:

* **Project Name** — Display label for the project picker
* **Git Repository Path** — Absolute path to the repo Zenflow clones into task worktrees
* **Scripts & Automation** — Setup, Dev Server, and Cleanup scripts
* **Copy Files** — Local-only files (e.g., `.env`) copied into each worktree
* **AI Rules** — Rule folders and always-include rule files agents follow

See [Repository Configuration](/zenflow/project-configuration) for the full reference.

## Prompts & Skills

Manage [Saved Prompts](/zenflow/saved-prompts) and [Skills](/zenflow/skills) from a single page.

<div className="mt-4 flex justify-center">
  <img src="https://mintcdn.com/forgoodaiinc/wAfswEtqaOe9ICOy/images/zenflow/zenflow-settings-prompts-skills.png?fit=max&auto=format&n=wAfswEtqaOe9ICOy&q=85&s=12f448d790973a43e1e443ae438b6695" alt="Prompts & Skills settings showing saved prompts list and skills section" style={{ width:"100%", maxWidth:"800px", borderRadius:"12px" }} width="1144" height="720" data-path="images/zenflow/zenflow-settings-prompts-skills.png" />
</div>

* **Saved Prompts** — Reusable text snippets accessible via `/` command
* **Skills** — Agent skills loaded from `SKILL.md` files in your project

## Experimental

Early-access features that may change. Enable or disable experimental capabilities here.

## Default Agents

<div className="mt-4 flex justify-center">
  <img src="https://mintcdn.com/forgoodaiinc/wAfswEtqaOe9ICOy/images/zenflow/zenflow-settings-default-agents.png?fit=max&auto=format&n=wAfswEtqaOe9ICOy&q=85&s=9a416e2db1e17c42b36071d7704dafb3" alt="Default agents settings showing task implementation agent, reviewer agent, and code task instructions" style={{ width:"100%", maxWidth:"800px", borderRadius:"12px" }} width="1144" height="720" data-path="images/zenflow/zenflow-settings-default-agents.png" />
</div>

| Setting | Description |
| - | - |
| **Default agent & config** | The preset used for new task implementation |
| **Reviewer agent & config** | The preset used for review steps |
| **Code task instructions** | Instructions injected into every code task prompt |

## Saved Presets

Create and manage named agent configurations. Each preset defines a coding agent, model, and permission mode.

<div className="mt-4 flex justify-center">
  <img src="https://mintcdn.com/forgoodaiinc/wAfswEtqaOe9ICOy/images/zenflow/zenflow-saved-presets.png?fit=max&auto=format&n=wAfswEtqaOe9ICOy&q=85&s=4bbb8637dd0f4e72228b17dbdc27a1c6" alt="New configuration preset dialog with preset name, coding agent, model, and permission mode fields" style={{ width:"100%", maxWidth:"700px", borderRadius:"12px" }} width="1144" height="720" data-path="images/zenflow/zenflow-saved-presets.png" />
</div>

See [Agent Presets](/zenflow/orchestration/agent-presets) for how to assign presets to workflow steps.

## MCP Servers

Configure Model Context Protocol servers for extended tool access. See [MCP Servers](/zenflow/mcps) for details.

## Profile

* Update your name, email, and authentication methods
* Review workspace membership and access levels


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.