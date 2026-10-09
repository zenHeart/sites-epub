> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# November 2025

> Custom model support, LoC metrics, ZenCLI milestone, and dynamic model switching

# November 2025 Product Updates

This month marks a significant infrastructure milestone with the complete ZenCLI rollout, enabling custom model support and bringing your privately deployed models into Zencoder. We've also introduced Lines of Code metrics for better usage tracking, dynamic model switching mid-conversation, and major improvements to both VS Code and JetBrains plugins.

## Custom Models in Zencoder Plugins

<Card title="Bring Your Own Models" icon="microchip" color="#F24A07">
  Use your privately deployed models or connect to providers not natively supported by Zencoder. Full flexibility to leverage custom LLMs while maintaining Zencoder's powerful development features.
</Card>

Zencoder now supports custom model configurations across plugins and CLI, giving you complete control over your AI infrastructure:

**Key capabilities:**

* **Private model deployments** let you connect Zencoder to your organization's internally hosted LLMs
* **Unsupported providers** can now be integrated, expanding beyond our native model catalog
* **Custom model configurations** preserve all Zencoder features including context awareness, tool usage, and multi-step reasoning
* **Enterprise flexibility** enables compliance with strict data governance and security policies

This feature is available through [ZenCLI and plugin configurations](/features/custom-models-configuration), making it accessible whether you're working in the IDE or command line.

[Learn more about Custom Models →](/features/custom-models-configuration)

## Lines of Code Metrics

<Card title="Track Generated and Accepted Code" icon="chart-line" color="#10B981">
  New LoC metrics in the usage analytics dashboard and API provide visibility into how much code Zencoder generates versus how much your team actually uses.
</Card>

We've introduced two new metrics to help you measure Zencoder's impact on your development workflow:

**New metrics:**

* **Lines of code generated** shows the total output from all AI agents across your organization
* **Lines of code accepted** tracks what developers actually keep and commit, giving you a true measure of AI contribution
* Both metrics are available in the **web admin panel** under usage analytics for visual tracking
* The **[Analytics API](/features/analytics-api)** now exposes LoC data for custom reporting and integration with your existing tools

These metrics help quantify developer productivity gains and justify AI tooling investments with concrete data.

[Explore Analytics API →](/features/analytics-api)

## Performance Enhancements

<Card title="Faster, More Reliable Experience" icon="bolt" color="#9333EA">
  Significant performance improvements across all Zencoder operations deliver faster agent responses, better resource usage, and enhanced stability during long sessions.
</Card>

This month brings substantial performance improvements throughout the platform:

**What you'll notice:**

* **Faster agent responses** with optimized request handling reducing latency across all operations
* **Better resource management** improving memory usage and system performance during extended sessions
* **Enhanced reliability** through improved error handling and session management
* **Smoother long-running sessions** with better stability when working on complex, multi-step tasks

These improvements create a noticeably faster and more stable experience, especially during intensive coding sessions.

## Dynamic Model Switching

<Card title="Switch Models Mid-Conversation" icon="arrows-rotate" color="#F59E0B">
  Change AI models between messages without losing context or starting a new chat session.
</Card>

You can now switch models dynamically during an active chat session:

**How it works:**

* Use the **model selector** at any point in your conversation
* **Context preservation** ensures the new model has full visibility into previous messages
* **Compare approaches** by trying different models on the same problem without context switching
* **Optimize costs** by starting with a faster model and upgrading only when needed

This flexibility lets you match model capabilities to specific subtasks within a larger workflow.

## Model Catalog Updates

We've expanded and refined our model offerings this month:

**New additions:**

* **GPT-5.1-Codex** - Updated variant with improved code generation and reasoning
* **Gemini Pro 3.0** - Google's latest model with enhanced multi-turn conversation capabilities

**Removed models:**

* **Sonnet 4 PT** - Replaced by newer Sonnet variants
* **GPT-5** - Superseded by GPT-5.1-Codex with better performance

[View all available models →](/features/models)

<Accordion title="Version History">
  <Tabs>
    <Tab title="VS Code">
      * **3.6** (November 26, 2025)
      * **3.4** (November 21, 2025)
      * **3.2** (November 17, 2025)
      * **3.0** (November 10, 2025)
      * **2.80.0** (November 5, 2025)
      * **2.78.0** (November 5, 2025)
      * **2.76.0** (November 4, 2025)
    </Tab>

    <Tab title="JetBrains">
      * **3.2.1** (November 27, 2025)
      * **3.2.0** (November 27, 2025)
      * **3.1.0** (November 24, 2025)
      * **3.0.0** (November 11, 2025)
      * **2.28.0** (November 6, 2025)
    </Tab>
  </Tabs>
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.