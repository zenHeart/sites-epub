> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Coding Foundations

<CardGroup cols={1}>
  <div id="how-ai-coding-assistants-actually-work">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          How AI Coding Assistants Actually Work
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is an LLM, in simple terms?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            A large language model is software that ingests a prompt, reasons over its training data and recent context, and then emits the next best piece of text.
            In coding workflows that text can be a code change, a bug explanation, or a code review comment—so the LLM acts like a teammate that can draft or critique
            work as soon as you describe what you need.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/how-ai-coding-assistants-actually-work/what-is-an-llm-in-simple-terms.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=f561339f7951db271101bbc97a4ae4b1" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/how-ai-coding-assistants-actually-work/what-is-an-llm-in-simple-terms.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is the context window, and how does it affect AI coding?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            The context window is the model’s short-term memory: it can only keep a limited number of tokens from the current conversation in focus at once.
            Zencoder summarizes older turns before the limit overflows, but the best practice is still to feed only the files or snippets that matter for this task so
            the assistant never wastes precious window space on irrelevant code.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/how-ai-coding-assistants-actually-work/what-is-the-context-window-and-how-does-it-affect-ai-coding.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=15b29b43ce596785d4159999927ddf6b" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/how-ai-coding-assistants-actually-work/what-is-the-context-window-and-how-does-it-affect-ai-coding.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What are hallucinations, and is there a way to reduce them?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            A hallucination happens when the LLM confidently returns an incorrect answer—like fabricating an API or returning broken code.
            Mitigate this by giving the model precise, well-scoped instructions, supplying the source files it should anchor on, and turning on the Zencoder
            Requirements Clarification tool so the agent pauses to ask follow-up questions instead of guessing.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/how-ai-coding-assistants-actually-work/what-are-hallucinations-and-is-there-a-way-to-reduce-them.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=fc9ce1a39f1511a8b9997c1451f73346" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/how-ai-coding-assistants-actually-work/what-are-hallucinations-and-is-there-a-way-to-reduce-them.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What’s the proper way to use AI coding assistants?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Most teams blend two modes: lightweight autocomplete that offers the next few lines in the IDE (accept with Tab) and deeper natural-language sessions in
            the side panel where an agent can open files, edit code, or create new artifacts. The key is staying in control—hover close when precision matters, review
            every diff the agent prepares, and let it run longer only when the surface area and risk are well understood.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/how-ai-coding-assistants-actually-work/what-s-the-proper-way-to-use-ai-coding-assistants.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=90500f935c1c50efd5c597e5ca14bf8d" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/how-ai-coding-assistants-actually-work/what-s-the-proper-way-to-use-ai-coding-assistants.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fai-coding-foundations%23how-ai-coding-assistants-actually-work" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="how-ai-coding-assistants-actually-work" data-copy-default-label="Download card as image" data-copy-exclude="true">
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

  <div id="zencoders-integration-approach-and-ide-flexibility">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Zencoder’s Integration Approach and IDE Flexibility
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How is Zencoder different as an IDE Agent?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Some AI tools force you into their custom IDE, but Zencoder ships as a native extension in both VS Code and JetBrains, so you stay in the editor you already know.
            We maintain feature parity and top-tier performance across those marketplaces, so there’s no “secondary” experience—you get the same agent capabilities no matter which IDE you prefer.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/zencoders-integration-approach-and-ide-flexibility/how-is-zencoder-different-by-being-an-ide-plugin.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=a8b8c63b03fce7b5e217b0602dfc4426" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/zencoders-integration-approach-and-ide-flexibility/how-is-zencoder-different-by-being-an-ide-plugin.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">In Zencoder you can choose the LLM provider?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Yes—every chat starts with a model selector. Pick a heavier model when you anticipate complex reasoning, or drop to a lighter model for quick, inexpensive edits.
            We expose a cost multiplier next to each option (1×, 0.5×, 3×, etc.) so you always know how your usage is tracked, and we keep the catalog refreshed as new providers launch.
            You can even BYOK (bring your own key) for Anthropic or OpenAI and have Zen CLI call those APIs directly under your own subscription.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/zencoders-integration-approach-and-ide-flexibility/in-zencoder-you-can-choose-the-llm-provider.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=5e8f43b4cd8831772c8193e0c089ee3f" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/zencoders-integration-approach-and-ide-flexibility/in-zencoder-you-can-choose-the-llm-provider.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What’s an agent CLI?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Think of the agent CLI as the execution engine behind the chat UI. Zen CLI is our default engine and it can drive any model in the dropdown, but you can swap in
            first-party engines like Anthropic’s Claude Code or OpenAI’s Codex agent if you already pay for those services. When you do, usage comes out of your Anthropic/OpenAI plan
            while you still benefit from Zencoder’s workflow UI.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/zencoders-integration-approach-and-ide-flexibility/what-s-an-agent-cli.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=bea5adc12e177542a7a9c7b0b1e06e72" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/zencoders-integration-approach-and-ide-flexibility/what-s-an-agent-cli.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What are the agents that you can select in Zencoder?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Above the engine choice sits the agent selector—the “driving mode” for the conversation. Choose Code to have the assistant edit and write files, Ask for read-only Q\&A,
            Unit Test or E2E Test to draft and even execute tests (E2E can launch a browser, click through flows, and capture screenshots). You can also build custom agents: name them,
            attach instructions and MCP tools, and then share them with your whole org so everyone can summon that specialized helper from the same dropdown.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/zencoders-integration-approach-and-ide-flexibility/what-are-the-agents-that-you-can-select-in-zencoder.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=4592616056303155a736311fcb59cc91" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/zencoders-integration-approach-and-ide-flexibility/what-are-the-agents-that-you-can-select-in-zencoder.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fai-coding-foundations%23zencoders-integration-approach-and-ide-flexibility" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="zencoders-integration-approach-and-ide-flexibility" data-copy-default-label="Download card as image" data-copy-exclude="true">
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

  <div id="mental-models-for-effective-ai-collaboration">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Mental Models for Effective AI Collaboration
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What does it mean to treat AI as a “pair programmer”?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            A pair programmer works alongside you, not in place of you. AI shows the same pattern: if you give it high-quality inputs, review its work, and course-correct along
            the way, you get great output. If you lob vague GPT prompts and hope for magic, you won’t. Treat it like a teammate you guide, not a vending machine.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/what-does-it-mean-to-treat-ai-as-a-pair-programmer.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=5717315352e8dadc56756ade710dc61b" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/what-does-it-mean-to-treat-ai-as-a-pair-programmer.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What do we mean when we say that AI is “literal-minded”?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            The model takes your words at face value. It rarely stops to infer hidden context or push back on fuzzy asks, so it delivers the most direct interpretation of what you typed.
            Adapt by spelling out the constraints, edge cases, and architectural intent explicitly—think of it as over-communicating so the assistant never has to guess.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/what-do-we-mean-when-we-say-that-ai-is-literal-minded.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=604825d058240ab041081240118de6f9" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/what-do-we-mean-when-we-say-that-ai-is-literal-minded.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is Spec Driven Development, and what is it good for?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Spec Driven Development (SDD) front-loads the conversation with a full plan: describe the end state, outline the architecture, and detail the steps before the agent starts coding.
            Instead of spoon-feeding requests one snippet at a time, you hand the AI the entire map so it understands how today’s change fits into the bigger build.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/what-is-spec-driven-development-and-what-is-it-good-for.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=fdba2678ad410cd18cca1205b0b07650" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/what-is-spec-driven-development-and-what-is-it-good-for.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is Test Driven Development, and how does it fit with SDD?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            TDD slots neatly into that SDD plan. For each increment, have the agent sketch the tests first, watch them fail, write the implementation, and rerun the tests to confirm.
            Those tight red/green loops give the AI a built-in way to self-verify and keep the project on track, especially when you’re breaking a build into multiple SDD steps.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/what-is-test-driven-development-and-how-does-it-fit-with-sdd.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=82d1b3583afdd66b387339f780b99f83" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/what-is-test-driven-development-and-how-does-it-fit-with-sdd.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">When should one still use manual coding instead of AI?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            For tiny tweaks where you already know the exact file and change, typing it yourself can be quicker—and autocomplete can still fill in a few lines when you hit Tab.
            Save the full agent workflows for larger refactors, multi-file features, or cases where the AI’s ability to reason across the repo unlocks more leverage than manual edits.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/when-should-one-still-use-manual-coding-instead-of-ai.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=e9943609489df26aa15b8580095fae28" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ai-coding-foundations/mental-models-for-effective-ai-collaboration/when-should-one-still-use-manual-coding-instead-of-ai.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fai-coding-foundations%23mental-models-for-effective-ai-collaboration" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="mental-models-for-effective-ai-collaboration" data-copy-default-label="Download card as image" data-copy-exclude="true">
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