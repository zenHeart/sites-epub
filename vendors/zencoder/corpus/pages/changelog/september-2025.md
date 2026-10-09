> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# September 2025

> Universal AI Platform, Sonnet 4.5 Parallel Thinking, Expanded CLI Support, and comprehensive troubleshooting improvements

# September 2025 Product Updates

This month brings transformative capabilities with the Universal AI Platform, allowing you to leverage your existing AI subscriptions directly within Zencoder. We've added day-zero support for Anthropic's Sonnet 4.5 Parallel Thinking, introduced our most cost-efficient model yet, and expanded our troubleshooting documentation to help you resolve issues faster.

## Universal AI Platform

<Card title="Unify Your AI Tools" icon="terminal" color="#F24A07">
  Connect your existing ChatGPT, Claude, or (soon) Gemini subscriptions to access Zencoder's enterprise features without additional AI costs. The Universal AI Platform breaks down barriers between CLI tools, IDEs, and enterprise development.
</Card>

The [Universal AI Platform](/features/universal-cli-platform) represents a fundamental shift in how developers interact with AI coding tools. Instead of choosing between powerful CLIs or convenient IDE integrations, you can now use both seamlessly.

**Key capabilities:**

* You can now **use existing subscriptions** from ChatGPT, Claude, or Gemini accounts directly within Zencoder
* **Native CLI support** now means full integration with Claude Code and OpenAI Codex platforms
* The platform provides seamless **IDE integration** that works in VS Code (2.38+) and JetBrains IDEs (2.16+)
* You can **instantly switch** between AI providers without leaving your IDE or disrupting your workflow
* Access all of Zencoder's **enterprise features** using your existing AI subscription without additional costs

[Learn more about Universal AI Platform →](/features/universal-cli-platform)

## Sonnet 4.5 Parallel Thinking

<Card title="Day-Zero Model Release" icon="sparkles" color="#9333EA">
  Available from September 29, 2025 - the same day Anthropic released it. The first model we've seen that feels purpose-built for spec-driven development with persistent state tracking.
</Card>

We've integrated Anthropic's latest [Sonnet 4.5 Parallel Thinking model](/features/models) within hours of its release, bringing unprecedented capabilities for complex coding tasks:

**What makes it special:**

* The model offers **parallel execution** that handles multiple related tasks simultaneously without losing context
* It maintains **persistent state** across complex operations, remembering what it's working on throughout the session
* Built-in **high verification bias** ensures accuracy in critical code sections where precision matters most
* While it uses a **1.5× multiplier**, you're getting premium performance at a reasonable cost for complex tasks
* The model is **available on Starter+ plans**, making this advanced capability accessible to most users

The model excels at spec-driven development, making it ideal for implementing features from detailed requirements or refactoring large codebases.

## Cost-Efficient Model Options

<Card title="Grok Code Fast 1" icon="bolt" color="#10B981">
  The most cost-efficient model in our lineup at 0.25× multiplier, making AI coding assistance 4x more affordable without sacrificing essential capabilities.
</Card>

We've expanded our model selection with options for every budget and use case:

**New models this month:**

* **Grok Code Fast 1** from xAI delivers efficient processing at just 0.25× multiplier, making it perfect for routine tasks that don't require premium models
* The new **GPT-5 Codex** is a specialized variant optimized specifically for code generation, operating at a standard 1× multiplier

These additions ensure you can balance performance and cost based on your specific needs.

## Comprehensive Troubleshooting

<Card title="Known Issues & Solutions" icon="wrench" color="#F59E0B">
  New troubleshooting guides for common issues including VS Code gray screen and Windows CLI installation problems, helping you resolve issues quickly.
</Card>

We've significantly expanded our [troubleshooting documentation](/user-guides/known-issues) with detailed solutions:

**New troubleshooting guides:**

* The **[VS Code Gray Screen (GSOD)](/user-guides/known-issues/vscode-gray-screen)** guide provides a complete workaround for unresponsive chat panels that some users encounter
* Our **[Windows CLI Installation](/user-guides/troubleshooting/windows-cli-installation)** guide walks you through PowerShell execution policy fixes and common installation blockers
* We've added **enhanced debug information** with better guidance for gathering logs and operation IDs when you need support

Each guide includes step-by-step instructions, visual aids, and platform-specific solutions.

## Additional Updates

### Zen Rules Enhancements

* The new **rule creation starter** simplifies the process of creating project-specific rules tailored to your codebase
* **Applied rules visibility** lets you see exactly which rules are active in your current context at any time

\[Zen Rules have been replaced by [Skills](/features/skills)]

### Integration Improvements

* **Expanded MCP support** now includes stdio, HTTP, and OAuth2 authentication protocols for broader compatibility
* We've improved **server compatibility** to work seamlessly with various MCP server implementations in the ecosystem

### UI/UX Enhancements

* The **model selector** has been updated with a new visual design
* We've added a dedicated **CLI selector interface** that makes it easy to choose between Zen CLI, Claude Code, and Codex platforms
* **Improved navigation** throughout the documentation provides better organization of known issues and troubleshooting sections

### Bug Fixes

* **Windows PowerShell execution policy errors** that blocked CLI installations have been resolved with proper permission handling
* Numerous **stability and performance improvements** across both VS Code and JetBrains extensions

## Documentation Updates

This month we've added and enhanced numerous documentation pages:

**New documentation:**

* [Universal AI Platform setup and usage](/features/universal-cli-platform)
* [VS Code gray screen troubleshooting](/user-guides/known-issues/vscode-gray-screen)
* [Windows CLI installation guide](/user-guides/troubleshooting/windows-cli-installation)

**Enhanced pages:**

* [Model selection](/features/models) - Added new models and multiplier information
* [MCP integrations](/features/integrations-and-mcp) - Expanded protocol documentation
* [Skills](/features/skills) (formerly Zen Rules) - Added configuration and creation guides
* [Known Issues](/user-guides/known-issues) - Reorganized for better navigation

<Accordion title="Version History">
  <Tabs>
    <Tab title="VS Code">
      - 2.42.0 (September 29, 2025)
      - 2.40.0 (September 23, 2025)
      - 2.38.0 (September 18, 2025)
      - 2.36.0 (September 17, 2025)
      - 2.32.0 (September 10, 2025)
      - 2.30.0 (September 2, 2025)
    </Tab>

    <Tab title="JetBrains">
      * 2.16.0 (September 18, 2025)
      * 2.15.1 (September 16, 2025)
      * 2.15.0 (September 16, 2025)
      * 2.14.0 (September 9, 2025)
    </Tab>
  </Tabs>
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.