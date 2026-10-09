> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Team Collaboration and Knowledge Sharing with Zen Agents

<CardGroup cols={1}>
  <div id="understanding-zen-agents-and-the-library">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Understanding Zen Agents and the Library
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What are Zen Agents? Why are they useful?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Zen Agents are user-defined agents created on the Agents page. Each gets a name, CLI alias, and a set of instructions (coding patterns,
            review rules, release conventions, etc.). You assign tools per agent — for example, an observability agent might use search and file
            edit, while an SRE agent uses custom MCP actions. Once created, they appear in the Custom Agents section of the selector for the
            whole team to reuse.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/OuvGW_xqNIUEo0Hy/files/enterprise-best-practices/team-collaboration-zen-agents/understanding-zen-agents-and-the-library/what-are-zen-agents-why-are-they-useful.mp4?fit=max&auto=format&n=OuvGW_xqNIUEo0Hy&q=85&s=596a24797fbba3cafef86748fe4014c6" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/team-collaboration-zen-agents/understanding-zen-agents-and-the-library/what-are-zen-agents-why-are-they-useful.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to browse the Agents Library?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            The Library tab on the Agents page lists pre-built agents you haven't installed yet. Open any card to view its instructions,
            tools, and sharing defaults. Installed agents are editable, so you can use them as starting points and customize for your team's
            specific needs.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/dzMoqE79sXZcvTdJ/files/enterprise-best-practices/team-collaboration-zen-agents/understanding-zen-agents-and-the-library/how-to-browse-the-agents-library.mp4?fit=max&auto=format&n=dzMoqE79sXZcvTdJ&q=85&s=dea0903b2a4a57000c774d516e8e12dd" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/team-collaboration-zen-agents/understanding-zen-agents-and-the-library/how-to-browse-the-agents-library.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to use an agent from the Library?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            When a Library agent looks promising, click through to its detail view and hit <em>Add</em>. The agent is copied into your Custom Agents list as if you authored it, so you
            can retune the instructions, swap tools, and decide whether to keep it personal or share it org-wide. From there it behaves like any other agent: select it in the agent
            picker when starting a conversation, gather feedback from the runs, and keep iterating on its instructions so the entire org benefits from each tweak.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/dzMoqE79sXZcvTdJ/files/enterprise-best-practices/team-collaboration-zen-agents/understanding-zen-agents-and-the-library/how-to-use-an-agent-from-the-library.mp4?fit=max&auto=format&n=dzMoqE79sXZcvTdJ&q=85&s=9f421a56397242a1156016202026bf53" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/team-collaboration-zen-agents/understanding-zen-agents-and-the-library/how-to-use-an-agent-from-the-library.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to identify use cases for new custom agents?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Agents shine when the work is repetitive, high-stakes, or steeped in tribal knowledge. Look for areas where senior engineers keep repeating the same instructions—code
            review checklists, secure-by-default patterns, release rituals—and translate those expectations into agent prompts instead of reinventing them every run. The more
            specific the mandate, the better: a deployment hardening agent or a “backend observability sweeper” will always outperform a single generalist. If a workflow is already
            documented in runbooks or captured in hallway conversations, it is mature enough to crystallize into a custom agent so the expertise scales beyond one person.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/OuvGW_xqNIUEo0Hy/files/enterprise-best-practices/team-collaboration-zen-agents/understanding-zen-agents-and-the-library/how-to-identify-use-cases-for-new-custom-agents.mp4?fit=max&auto=format&n=OuvGW_xqNIUEo0Hy&q=85&s=168a33b4b709f2201bd1e3c5c55ae756" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/team-collaboration-zen-agents/understanding-zen-agents-and-the-library/how-to-identify-use-cases-for-new-custom-agents.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fteam-collaboration-zen-agents%23understanding-zen-agents-and-the-library" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="understanding-zen-agents-and-the-library" data-copy-default-label="Download card as image" data-copy-exclude="true">
          <svg className="h-4 w-4 text-[#F24A07]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />

            <circle cx="9" cy="9" r="2" />

            <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
          </svg>

          <span data-copy-card-label>Download card as image</span>
        </button>
      </div>
    </Card>
  </div>

  <div id="building-your-first-custom-agent">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Building Your First Custom Agent
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to build a custom agent?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Start from the Agents page (three-dot menu → Agents) and hit <em>Create agent</em>. Give it a descriptive name for the UI, set an alias for CLI use, and then author the
            instructions: spell out the task scope, preferred coding patterns, review cadence, and reporting quirks so the agent knows exactly how to behave. The form preloads the
            core tools every coding agent needs—search files, read context, edit files—so once instructions feel right you can save and the agent will appear under Custom Agents in
            the selector.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/OuvGW_xqNIUEo0Hy/files/enterprise-best-practices/team-collaboration-zen-agents/building-your-first-custom-agent/how-to-build-a-custom-agent.mp4?fit=max&auto=format&n=OuvGW_xqNIUEo0Hy&q=85&s=2f2fd6733785c3939e9b180d66d17734" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/team-collaboration-zen-agents/building-your-first-custom-agent/how-to-build-a-custom-agent.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to add tools to custom agents?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Below the instructions lives the tool roster. The defaults stay in place unless you remove them, and you can expand the toolbox by clicking <em>Add tool</em>, which opens a
            picker listing every MCP or integration already installed. Need something new? Choose <em>Manage tools</em> from that picker, configure additional MCPs on the Tools page,
            and jump back to the agent editor—the fresh capabilities now appear in the selector. Pair each tool with guidance in the instructions (“Use the Terraform MCP before
            editing infra files”) so the agent knows when to call it.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/OuvGW_xqNIUEo0Hy/files/enterprise-best-practices/team-collaboration-zen-agents/building-your-first-custom-agent/how-to-add-tools-to-custom-agents.mp4?fit=max&auto=format&n=OuvGW_xqNIUEo0Hy&q=85&s=661d8017e232d3903efe333938e245ed" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/team-collaboration-zen-agents/building-your-first-custom-agent/how-to-add-tools-to-custom-agents.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fteam-collaboration-zen-agents%23building-your-first-custom-agent" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="building-your-first-custom-agent" data-copy-default-label="Download card as image" data-copy-exclude="true">
          <svg className="h-4 w-4 text-[#F24A07]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />

            <circle cx="9" cy="9" r="2" />

            <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
          </svg>

          <span data-copy-card-label>Download card as image</span>
        </button>
      </div>
    </Card>
  </div>

  <div id="scaling-expertise-across-teams">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Scaling Expertise Across Teams
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to share a custom agent with the organization?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Every agent has a sharing dropdown: Personal keeps it private, Org promotes it to everyone. Flip that toggle before saving (or anytime later), and the agent surfaces under
            Custom Agents for every teammate alongside the creator’s email so folks know whom to ping. The same roster is visible in the web dashboard, where you can review both
            personal and org-wide agents; you may edit anything you created yourself but shared agents remain locked to their authors so governance stays tight.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/dzMoqE79sXZcvTdJ/files/enterprise-best-practices/team-collaboration-zen-agents/scaling-expertise-across-teams/how-to-share-a-custom-agent-with-the-organization.mp4?fit=max&auto=format&n=dzMoqE79sXZcvTdJ&q=85&s=44ea4a822c96a2267689c37d6ba5ece8" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/team-collaboration-zen-agents/scaling-expertise-across-teams/how-to-share-a-custom-agent-with-the-organization.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to share a custom agent with the library?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            The Agents Library is open source at <a className="text-[#F24A07] underline" href="https://github.com/zencoderai/zenagents-library" target="_blank" rel="noreferrer">[https://github.com/zencoderai/zenagents-library](https://github.com/zencoderai/zenagents-library)</a> under the MIT License.
            Fork the repo, add your agent definition following the provided template, and submit a pull request describing what problem it solves. Zencoder reviews every
            submission for usefulness and security; once approved, the agent automatically appears in the IDE’s Library tab so any customer can install it with the same <em>Add</em>
            button. It is the easiest way to share a proven workflow with the broader developer community while letting us handle distribution.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/dzMoqE79sXZcvTdJ/files/enterprise-best-practices/team-collaboration-zen-agents/scaling-expertise-across-teams/how-to-share-a-custom-agent-with-the-library.mp4?fit=max&auto=format&n=dzMoqE79sXZcvTdJ&q=85&s=9a862bfd1606b02ca1e777b07af67b8d" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/team-collaboration-zen-agents/scaling-expertise-across-teams/how-to-share-a-custom-agent-with-the-library.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fteam-collaboration-zen-agents%23scaling-expertise-across-teams" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="scaling-expertise-across-teams" data-copy-default-label="Download card as image" data-copy-exclude="true">
          <svg className="h-4 w-4 text-[#F24A07]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />

            <circle cx="9" cy="9" r="2" />

            <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
          </svg>

          <span data-copy-card-label>Download card as image</span>
        </button>
      </div>
    </Card>
  </div>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.