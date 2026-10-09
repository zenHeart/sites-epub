> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Module 6: Complex Use Cases

## Intro

Module 6 stress-tests agent workflows on tougher projects: crafting migration agents to modernize legacy Java and pairing with Figma’s MCP so designs flow straight into production-ready UI code.

## Video lesson

<div className="mb-4" data-copy-exclude="true">
  <a className="inline-flex items-center gap-2 rounded-xl border border-[#F24A07] bg-[#F24A07] text-white px-4 py-2.5 text-base font-semibold shadow-sm hover:bg-[#d13d05] transition" href="https://www.udemy.com/course/the-10x-engineer-professional-ai-certification/" target="_blank" rel="noreferrer">
    <span>Course on Udemy</span>
  </a>
</div>

Preview lesson. The full video is available on Udemy.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/qPpy6gMhjQI" title="Module 6 Complex Use Cases Preview" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Key takeaways

* Start complex efforts by validating agent understanding—have it profile the codebase/version and restate functionality before transformations.
* Let agents draft the playbook: generate migration instructions (Java 6→17) with structure for analysis, build config, code changes, testing, and reporting, then reuse them in a custom agent.
* Package the migration agent with clear inputs (repo path, target version) and required tools so repeated runs stay predictable; review its summary after each execution.
* Expect multiple passes: inspect branches, rerun tests, and iterate on errors until both code and specs compile cleanly on the new runtime.
* For design-to-code flows, install the Figma MCP, share the design URL, and confirm the agent pulls layout context via `getDesignContext`.
* Ask the agent to scaffold the project (React/Vite) and render the UI; provide precise feedback (colors, layout, assets) and let it re-query Figma to fetch exact imagery.
* Use MCP-enabled tools whenever external context is needed (Figma, etc.); richer context leads to fewer manual fixes and higher-fidelity outputs.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.