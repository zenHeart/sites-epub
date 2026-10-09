> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Saved Prompts

> Create reusable prompt shortcuts and insert them quickly in chat or task descriptions

Saved Prompts let you create reusable prompt shortcuts that you can quickly insert into any chat or task description by typing `/`. Instead of retyping common instructions, save them once and reuse them everywhere.

## Why Saved Prompts?

Developers often repeat the same types of requests: refactoring patterns, review checklists, commit message formats, or project-specific instructions. Saved Prompts eliminate this repetition by letting you:

* **Save frequently used prompts** as named shortcuts
* **Insert them instantly** by typing `/` followed by the prompt name
* **Maintain consistency** across your team's workflows
* **Speed up interactions** with the agent by reducing typing

## How to Use Saved Prompts

1. Go to **Settings → Prompts & Skills** and click **+ Create new prompt**
2. Give it a shortcut name (e.g., `/review`) and add the prompt content
3. In any chat or task description, type `/` to see your available prompts
4. Select the prompt to insert it into your current input

<div className="mt-4 flex justify-center">
  <img src="https://mintcdn.com/forgoodaiinc/wAfswEtqaOe9ICOy/images/zenflow/zenflow-settings-prompts-skills.png?fit=max&auto=format&n=wAfswEtqaOe9ICOy&q=85&s=12f448d790973a43e1e443ae438b6695" alt="Zenflow Settings showing Prompts & Skills page with saved prompts list including /confirm-first, /fix-ci, /pr-comments, /review, /update-branch, and /explain" style={{ width:"100%", maxWidth:"800px", borderRadius:"12px" }} width="1144" height="720" data-path="images/zenflow/zenflow-settings-prompts-skills.png" />
</div>

<Tip>
  Saved Prompts work in both **Zencoder IDE Agents** and **Zenflow** task descriptions, so you can standardize prompts across your entire workflow.
</Tip>

## Example Use Cases

| Prompt Name | Example Content |
| - | - |
| `/review` | "Review this code for security vulnerabilities, performance issues, and adherence to our coding standards" |
| `/refactor` | "Refactor this code to follow SOLID principles while maintaining backward compatibility" |
| `/test` | "Write unit tests for this function covering edge cases, error handling, and happy path scenarios" |
| `/commit` | "Generate a conventional commit message for these changes" |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.