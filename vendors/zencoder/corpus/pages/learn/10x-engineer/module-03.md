> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Module 3: Custom Workflows

## Intro

Module 3 covers creating reusable instructions and rules, building custom agents (or installing from the library), and connecting MCP tools to match your team's policies and integrations.

## Video lesson

<div className="mb-4" data-copy-exclude="true">
  <a className="inline-flex items-center gap-2 rounded-xl border border-[#F24A07] bg-[#F24A07] text-white px-4 py-2.5 text-base font-semibold shadow-sm hover:bg-[#d13d05] transition" href="https://www.udemy.com/course/the-10x-engineer-professional-ai-certification/" target="_blank" rel="noreferrer">
    <span>Course on Udemy</span>
  </a>
</div>

Preview lesson. The full video is available on Udemy.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/IgkNbh740f8" title="Module 3 Custom Workflows Preview" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Key takeaways

* Use global Instructions for always-on guidance, and store reusable Zencoder Rules in `.zencoder/rules/*.md` so the whole project inherits consistent behaviours.
* Tweak each rule’s `always_apply` flag or mention it ad hoc; leverage `globs` to target file types (e.g., Markdown style guides) and keep shared rules in version control.
* Remember that repo-info output (`repo.md`) is itself an auto-applied rule, giving downstream agents immediate architectural context.
* Build custom agents by setting name, alias, instructions, and tool access; and save them in the custom tab.
* Browse the agent library for prebuilt roles (architecture reviews, etc.), clone them with one click, and adapt tooling or prompts as needed.
* Share vetted custom agents with your org by switching scope from personal to org; manage shared catalog entries through the web dashboard.
* Expand agent capabilities by installing MCP tools: some are one-click (Playwright E2E, Context7 docs) while others require OAuth or API tokens (InstantDB, GitHub).
* After installation, confirm new tools appear for the right agents and prune unused ones to avoid overwhelming default agent menus.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.