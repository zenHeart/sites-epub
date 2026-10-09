> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Module 2: Deep Codebase Understanding

## Intro

Module 2 shows how to keep agents effective as projects scale: wiring up Multi Repo Search tool so they can browse related repositories and tuning model choices (plus custom API keys) to match each agent’s task.

## Video lesson

<div className="mb-4" data-copy-exclude="true">
  <a className="inline-flex items-center gap-2 rounded-xl border border-[#F24A07] bg-[#F24A07] text-white px-4 py-2.5 text-base font-semibold shadow-sm hover:bg-[#d13d05] transition" href="https://www.udemy.com/course/the-10x-engineer-professional-ai-certification/" target="_blank" rel="noreferrer">
    <span>Course on Udemy</span>
  </a>
</div>

Preview lesson. The full video is available on Udemy.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/0hZ0PXhawjw" title="Module 2 Deep Codebase Understanding Preview" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Key takeaways

* Use the Multi Repo Search tool when questions span multiple repositories, letting agents pull relationships and artifacts without disrupting the current VS Code workspace.
* Prepare Multi Repo Search tool access by creating a fine-grained GitHub personal access token, adding a connection in the Zencoder dashboard, and registering every repo that agents should consult.
* Remember that repositories must be indexed before agents can read them, and the dashboard’s indexing log confirms when each sync finishes.
* Remove linked repositories before deleting a connection; once the connection is gone, you can rebuild it from scratch with fresh credentials.
* Verify MultiRepoTool availability per agent in the dashboard so the correct tooling is enabled during chats.
* Set agent models explicitly when needed—Auto is a safe default, but tailoring model choice can optimize for cost, latency, or capability.
* Add custom API keys for providers like Anthropic or OpenAI when you want usage charged to your own account instead of the workspace allocation.
* Reference docs at docs.zencoder.ai for current model availability, pricing multipliers, and step-by-step instructions on configuring premium or BYO keys.
* Follow the module’s model guidance: Grok Code FAST1 for budget tasks, Gemini 2.5 Pro for huge context, Sonnet 4.5 Parallel Thinking for spec workflows, GPT-5 Codecs for specialized code gen, and OPUS for the hardest problems.
* Collect system/model cards from providers, feed them to an LLM (e.g., Gemini 2.5 Pro’s 1M-token window), and have the agent synthesize comparison tables so you pick the best model per scenario.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.