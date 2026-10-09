> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# January 2026

> Skills support, terminal mentions, chat navigation improvements, and context window visibility

# January 2026 Product Updates

January 2026 brings powerful new customization capabilities with Skills support, improved chat navigation, terminal mentions, and enhanced context visibility. This release focuses on giving you more control over how the AI agent works and better visibility into your conversations.

## New Features

### Skills Support

<Card title="Customize Agent Behavior with Skills" icon="wand-magic-sparkles" color="#F24A07">
  Create reusable prompt templates that modify how the agent responds to specific tasks.
</Card>

Introducing Skills - a powerful way to customize the agent's behavior for your specific workflows:

**Key capabilities:**

* **Local and global skills** can be placed in `.agents/skills` (project-specific) or `~/.agents/skills` (global)
* **Prompt-based customization** allows you to define specialized instructions for different types of tasks
* **Reusable templates** create once and use across multiple projects and conversations

Skills make it easy to ensure consistent agent behavior for your team's specific coding standards, review processes, or documentation requirements.

### Terminal Mentions

<Card title="Reference Terminal Output in Chat" icon="terminal" color="#10B981">
  Mention terminal content directly in your chat to provide the agent with command output context.
</Card>

You can now reference terminal content in your conversations:

* **Direct terminal references** include output from your terminal in chat messages
* **Better debugging context** share command results, error logs, and build output with the agent
* **Seamless workflow** no need to copy-paste terminal output manually

### Chat Navigation Dropdown

<Card title="Jump Between Chats Instantly" icon="messages" color="#9333EA">
  A new dropdown shows your current chat, lets you search history, and keeps important chats pinned.
</Card>

Navigate your chat history more efficiently:

* **Quick chat switching** jump between conversations without losing context
* **Search functionality** find past chats by searching their content
* **Pin important chats** keep frequently referenced conversations easily accessible

### Context Window Indicator

<Card title="See How Much Context You're Using" icon="chart-pie" color="#F59E0B">
  A new indicator shows the percentage of context window used during your conversation.
</Card>

Better visibility into your conversation context:

* **Real-time percentage display** see how much of the context window is being used
* **Optimize your prompts** understand when to start fresh conversations
* **Avoid context limits** proactively manage long-running sessions

## Improvements

### Enhanced Chat Experience

* **Click to open files** click on any file mentioned in chat responses to open it directly in your editor
* **Streaming indicators** visual feedback shows when the agent is actively generating responses
* **Action required indicators** clear signals when your input is needed
* **Global MCP labels** easily identify globally installed MCP servers in the interface

### User Experience Updates

* **Improved small screen UI** better layouts and usability on smaller displays
* **Better error recovery** user guidance and reload button when chat encounters issues
* **Updated upgrade plan links** streamlined access to subscription management

## Bug Fixes

### Chat and Interface

* **Fixed chat deletion redirect** properly navigates to new chat screen when deleting current chat
* **Fixed agent selection on edit** editing a message now correctly maintains the selected agent
* **Fixed mention popup cleanup** reference popups properly close when exiting
* **Fixed workflow card spacing** improved layout between workflow cards and chat input
* **Fixed table line breaks** line breaks now render correctly in markdown tables
* **Fixed chat input focus** new chats automatically focus on the input field

### Platform Stability

* **Windows compatibility fix** resolved an issue that prevented the plugin from running for some Windows users
* **Docker MCP improvements** better error messages when Docker MCP encounters issues

<Accordion title="Version History">
  <Tabs>
    <Tab title="VS Code">
      - **3.27.0** (January 31, 2026)
      - **3.26.0** (January 24, 2026)
      - **3.25.0** (January 17, 2026)
      - **3.24.0** (January 10, 2026)
    </Tab>

    <Tab title="JetBrains">
      * **3.11.0** (January 31, 2026)
      * **3.10.0** (January 24, 2026)
      * **3.9.0** (January 17, 2026)
      * **3.8.0** (January 10, 2026)
    </Tab>
  </Tabs>
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.