> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# April 2025

> Enhanced tooling capabilities, new Bash tool, Requirements tool, and significant UX improvements

## Enhanced Developer Experience with New Tools and Improved Workflows

<Info>
  **Important Update**: Zencoder now requires JetBrains IDE version 2024.2 or later to run.
</Info>

April brought significant improvements to Zencoder's functionality and user experience. We've focused on adding powerful new tools like the Bash/Shell tool and Requirements tool, enhancing UX, and making many under-the-hood improvements to make your development workflow more efficient.

Here's what we've been working on:

## New Tools and Features

### Bash/Shell Tool for Coding Agent

The Bash tool is now available to the coding agent with significant improvements:

* Improved UX for safe commands that can run without confirmation
* Management options including "Don't ask again" in both VS Code and JetBrains
* Works seamlessly with Coffee Mode for increased productivity and speed
* Enhanced MCP management of environment variables and npx, making it more stable

<Card title="Learn More About Coding Agent" icon="code" href="/features/coding-agent">
  Explore how the Coding Agent can now leverage shell commands to better assist your development workflow.
</Card>

### Requirements Tool

Our new Requirements tool helps the coding agent better understand your needs:

* Automatically asks for clarifications when needed
* Gives you greater control over your project and work
* Better understands prompts and delivers higher-quality results
* Reduces back-and-forth by getting requirements right the first time

### Enhanced Chat Experience

We've made several improvements to the chat interface:

* Added support and hints for using slash commands (`/`) and file mentions (`@`) in the chatbox
* New warning system when chats become too long, helping you optimize token usage across multiple chats
* Ability to attach files from outside of the project to provide better context

## Debugging and Support Improvements

We've made it easier to get help when you need it:

* Simplified access to Operation IDs and debug settings to help us troubleshoot issues more effectively

<Info>
  **Helping Us Help You**: Operation IDs help our team trace exactly what happened during your interaction with the system. Learn how to access and share these IDs in our [Debug Information Guide](/user-guides/troubleshooting/debug-information#helping-us-help-you).
</Info>

## Search and Review Enhancements

* Significant improvements to local (client-side) search functionality
* Enhanced `/review` command is now invoking a pre-built custom agent with the same name, providing more precise and valuable insights
* You can adjust this custom agent's details in the Custom Agent settings

<Card title="Learn More About Custom Agents" icon="brush" href="/features/custom-agents">
  Discover how to customize the review agent and other specialized agents for your workflow.
</Card>

## Documentation Updates

* New descriptions and updated GIFs for documentation on both JetBrains and VS Code marketplaces
* Added detailed [guides on how to collect debug information and Operation IDs](/user-guides/troubleshooting/debug-information) to help with troubleshooting
* Enhanced documentation to make it easier to get support when needed

## Bugs and Fixes

We've addressed several user-facing issues:

* Fixed an annoying bug where indexing sometimes gets stuck at "Updating index" after reopening the IDE
* Fixed a problem with cursor positioning above inserted code snippets
* Improvements to Jira authentication flow
* Fixed hanging errors between the bash/shell tool and our internal processing

*Note: We've also made many background improvements and fixes that aren't listed here but contribute to a more stable and reliable experience.*

<Accordion title="Version History">
  <Tabs>
    <Tab title="VS Code">
      * 1.28.0 (Apr 28, 2025)
      * 1.26.0 (Apr 17, 2025)
      * 1.24.0 (Apr 10, 2025)
      * 1.22.0 (Apr 2, 2025)
    </Tab>

    <Tab title="JetBrains">
      * 1.24.0 (Apr 30, 2025)
      * 1.23.1 (Apr 24, 2025)
      * 1.23.0 (Apr 22, 2025)
      * 1.22.0 (Apr 15, 2025)
      * 1.21.0 (Apr 4, 2025)
    </Tab>
  </Tabs>
</Accordion>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.