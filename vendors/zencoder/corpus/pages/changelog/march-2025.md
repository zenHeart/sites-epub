> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# March 2025

> A month of building and refinement with new integrations, Coffee Mode, and enhanced coding and testing capabilities

## Coding Agent Out of Beta, Integrations and MCP Support Available

March was a busy month for our team as we focused on making our AI coding assistant more intuitive, powerful, and integrated with your development workflow.

Here's what we've been working on:

## New Integrations

* **Jira Integration**: You can now mention Jira tickets directly in your chat requests, making it easy to fix or implement tickets without context switching.

* **MCP Servers Configuration**: We've added seamless integration with Zencoder, opening the door to millions of community-built tools. This significant upgrade enables powerful new workflows across your development environment.

* **Google Chrome Extension**: Our new [browser extension](https://chromewebstore.google.com/detail/zencoder/obkkfjgjhdkjnkleopbljciifoefhnbp) enables connection with 20+ different developer tools, making it easier to work with your favorite resources without leaving your workflow. This creates a seamless experience across IDEs and web-based tools.

<Card title="Learn More About Integrations" icon="puzzle-piece" href="/features/integrations-and-mcp">
  Explore all our integration options in the Integrations and MCP documentation.
</Card>

## Introducing Coffee Mode ☕

Say goodbye to constant confirmations! Our new "Coffee Mode" lets your coding assistant work continuously without interrupting your flow.

This productivity booster was one of our most requested features and is now available across all supported environments.

## Coding Agent Enhancements

The Coding Agent is now out of beta and is generally available across all supported IDEs, bringing meaningful code quality improvements.

Additionaly, we've significantly improved our coding agent's capabilities:

* Better codebase understanding and more stable code generation
* Intelligent prompting to use the coding agent when it's the better tool for the job
* The `/fix` command now uses the coding agent instead of basic chat
* Custom AI instructions are now supported

<Card title="Learn More About Coding Agent" icon="code" href="/features/coding-agent">
  Explore how the Coding Agent generates multi-file, multi-language code with deep codebase understanding.
</Card>

## Unit Testing Agent Improvements

The unit tests agent got smarter:

* Now checks for syntax and compile errors in generated code
* Analyzes existing tests to avoid duplication
* Overall improved generation quality
* Thanks to the redesigned unit testing agent, you can now follow up in your chats more easily than before
* Unit test agent now has access to Bash tools and can execute safe commands directly for you from the chat
* The agent is aware of command outputs, making it easier for you to work more seamlessly

<Note>
  The Unit Testing Agent has been consolidated into the [Coding Agent](/features/coding-agent), which now handles all testing workflows.
</Note>

## Custom Agents

* You can now use custom agents in chat and see your custom agent name displayed in the chat interface.
* We've improved the UI for defining custom agents, making it simpler and better integrated in the settings pane.

<Card title="Learn More About Custom Agents" icon="brush" href="/features/custom-agents">
  Learn how to create specialized agents tailored to your specific development workflows.
</Card>

## UX & Quality of Life Improvements

Throughout March, we've been refining the user experience with UI, UX, and quality of life improvements — often overlooked but incredibly important changes that make your daily workflow smoother:

* Single-click application for multi-file changes
* Persistent coding agent state between chat sessions
* New chat button & UI for easier creation from any screen
* Ability to attach files from outside the project
* Enhanced colors in various themes
* Automatic saving of accepted changes to files
* Fixed undo/redo behavior in chat input

## Docstrings Generation

We've completely revamped our docstrings generation capability:

* Simplified UI for a more intuitive experience
* Dramatically improved speed and reliability
* Better understanding of the code context that's being documented

## Documentation Overhaul

We've made significant improvements to our documentation:

* Completely recategorized content for easier navigation
* Added a new [Concepts page](/get-started/basic-concepts) with a full product demo video
* Added a new [Community, Feedback and Support hub](/get-started/community-support) for better user engagement
* Started our changelog tracking (yes, you're reading it right now—how meta!)

<Accordion title="Version History">
  <Tabs>
    <Tab title="VS Code">
      - 1.13.0 (Mar 4)
      - 1.14.0 (Mar 6)
      - 1.15.0 (Mar 12)
      - 1.16.0 (Mar 12)
      - 1.17.0 / 1.18.0 (Mar 20)
      - 1.19.0 (Mar 25)
    </Tab>

    <Tab title="JetBrains">
      * 1.16.0 (Mar 3)
      * 1.17.0 (Mar 11)
      * 1.18.0 (Mar 12)
      * 1.19.0 (Mar 20)
      * 1.20.0 (Mar 27)
    </Tab>
  </Tabs>
</Accordion>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.