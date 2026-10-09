> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# CI/CD Automation and Autonomous Agents

<CardGroup cols={1}>
  <div id="multi-repo-setup-and-configuration">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Multi-Repo Setup and Configuration
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is a multi-repo project? What's the benefit?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            A multi-repo (polyrepo) project spreads the product across several Git repositories instead of a single monorepo,
            which gives each service, library, or infrastructure module its own pipelines and permissions. Enterprises lean
            on it for autonomy: teams ship on their own cadence, guard access per repo, and even share specific repos with
            vendors or customers without exposing the rest of the codebase.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/what-is-a-multi-repo-project-what-s-the-benefit.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=e0085d5d6fc97848a961b6dd1b6edd2f" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/what-is-a-multi-repo-project-what-s-the-benefit.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">Why do coding agents struggle to work with multiple repos?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            IDE copilots typically ingest only the repo that's open in the editor. Even multi-root workspaces inherit config
            (linters, auth, launch files) that assume a single repo, so agents end up blind to adjacent services. Without
            those sibling repos, they hallucinate APIs, miss cross-repo contracts, and ship brittle changes because they
            cannot inspect or test the surrounding code.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/why-do-coding-agents-struggle-to-work-with-multiple-repos.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=a7e145c776c09dfaad72396df8826e67" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/why-do-coding-agents-struggle-to-work-with-multiple-repos.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What's the Zencoder multi-repo tool?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            It's an indexing system in the dashboard that ingests any GitHub, GitLab, or Bitbucket repo you connect via a
            scoped token. Once indexed, Zencoder keeps a read-only snapshot plus metadata (owners, last index time, auto-
            reindex toggle), and agents with the multi-repo tool can list, open, and read those repos even if they're not
            the one currently open in the IDE.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/what-s-the-zencoder-multi-repo-tool.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=d954ba6d73c3d55eeef318547210875a" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/what-s-the-zencoder-multi-repo-tool.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to configure the Zencoder multi-repo tool?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            In the web dashboard, start on <em>Connections</em> to add GitHub/GitLab/Bitbucket access with a personal access
            token that scopes exactly which repos the agent should read. Then switch to <em>Repositories</em>, add repos one
            by one, decide whether they auto-reindex on changes, and assign which teammates can use each repo through the
            tool. The same page shows indexing status so you can trigger manual refreshes later.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/how-to-configure-the-zencoder-multi-repo-tool.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=346b092b03ec41032aaf75588b13a6c9" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/how-to-configure-the-zencoder-multi-repo-tool.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to use the multi-repo tool?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Enable the tool on any agent (built-in or custom) and run your normal chat in the IDE. When the agent needs extra
            context it calls <em>listRepos</em>, jumps into the indexed repo, reads files or docs, and returns to edit the open
            repo. It's read-only - changes still land in the workspace you're editing - but it gives the agent the architectural
            picture it needs. A quick sanity check is to ask, "What repos can you see through the Multi-Repo tool?" and make
            sure it lists everything you expect.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/how-to-use-the-multi-repo-tool.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=c4952ee223047408e1546328b6c20b30" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/multi-repo-setup-and-configuration/how-to-use-the-multi-repo-tool.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fci-cd-automation%23multi-repo-setup-and-configuration" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="multi-repo-setup-and-configuration" data-copy-default-label="Download card as image" data-copy-exclude="true">
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

  <div id="github-triggered-autonomous-agents">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          GitHub-Triggered Autonomous Agents
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What are autonomous agents?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            They are the same Zencoder agents you run inside the IDE, but deployed as headless workers that live in your
            CI/CD systems. A trigger from GitHub/GitLab/Bitbucket (or any webhook) wakes them up; they load the repo map,
            follow their instructions, plan edits, run tests, and publish output without a human steering every step.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/github-triggered-autonomous-agents/what-are-autonomous-agents.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=21fc614c9a07bc7b12a94f6514faa488" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/github-triggered-autonomous-agents/what-are-autonomous-agents.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How can autonomous agents be activated at Zencoder, as an addon?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            It's a paid addon (Pro Plus plan or higher). Contact sales via
            <span className="text-[#F24A07] underline">[https://meetings.hubspot.com/griffin-kurzius/zencoder-intro](https://meetings.hubspot.com/griffin-kurzius/zencoder-intro)</span>
            and the team will enable the feature for your org, unlocking the dashboard sections for <em>Connections</em>,
            <em>Repositories</em>, and <em>Autonomous Flows</em>.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/github-triggered-autonomous-agents/how-can-autonomous-agents-be-activated-at-zencoder-as-an-addon.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=6f13166309f3ac85300807c4c90c4eb6" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/github-triggered-autonomous-agents/how-can-autonomous-agents-be-activated-at-zencoder-as-an-addon.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How are autonomous agents configured in GitHub/GitLab/Bitbucket?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Each provider follows the same arc: drop our workflow file into the repo, generate a Zencoder client ID/secret
            plus a platform token with repo + workflow scopes, store them as CI secrets, and register the repo inside
            Zencoder so the agent can pull code. The workflow then calls your chosen agent whenever the CI event fires. Full
            checklists live in the configuration guide:
            <span className="text-[#F24A07] underline">Contact your Zencoder admin for the latest configuration steps</span>.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/github-triggered-autonomous-agents/how-are-autonomous-agents-configured-in-github-gitlab-bitbucket.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=1263e9ccfff41eba50b5ae3d5a92df22" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/github-triggered-autonomous-agents/how-are-autonomous-agents-configured-in-github-gitlab-bitbucket.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What are use cases of autonomous agents in GitHub?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            They become programmable teammates inside CI: auto-review every pull request, fix reviewer comments, enforce
            internationalization, keep dependencies fresh, or assemble release notes the moment a branch or tag appears.
            Because workflows can target any custom agent, all your org-specific prompts carry over from the IDE into
            GitHub Actions.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/github-triggered-autonomous-agents/what-are-use-cases-of-autonomous-agents-in-github.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=b1b56ea0d456b6bb4028d010bcc98fcb" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/github-triggered-autonomous-agents/what-are-use-cases-of-autonomous-agents-in-github.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fci-cd-automation%23github-triggered-autonomous-agents" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="github-triggered-autonomous-agents" data-copy-default-label="Download card as image" data-copy-exclude="true">
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

  <div id="jira-triggered-autonomous-agents">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Jira-Triggered Autonomous Agents
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is the additional configuration needed to trigger from Jira?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Jira triggers use the webhook flavor of autonomous flows. You place the webhook workflow file in your repo,
            create an autonomous flow in the dashboard (which generates a webhook URL + secret), and then author a Jira
            Automation rule that POSTs that payload with the secret. It's a few more steps than a pure CI trigger, so keep
            the configuration guide handy when wiring the Jira form:
            <span className="text-[#F24A07] underline">Contact your Zencoder admin for the latest configuration steps</span>.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/jira-triggered-autonomous-agents/what-is-the-additional-configuration-needed-to-trigger-from-jira.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=25938534d0c05c601b10ff78512a43e8" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/jira-triggered-autonomous-agents/what-is-the-additional-configuration-needed-to-trigger-from-jira.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to monitor the autonomous agents triggered from Jira?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Check three surfaces: the Jira Automation rule history (to confirm the webhook fired), your CI provider's run
            logs (GitHub/GitLab/Bitbucket show the workflow execution), and the Autonomous Flows list in Zencoder, which
            records each run's status and output. Together they confirm the webhook arrived, the workflow ran, and the
            agent wrapped up successfully.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/jira-triggered-autonomous-agents/how-to-monitor-the-autonomous-agents-triggered-from-jira.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=50c65bdf76a1459c756ce40417e69dc3" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/jira-triggered-autonomous-agents/how-to-monitor-the-autonomous-agents-triggered-from-jira.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">Where else can autonomous agents be triggered from?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Anywhere that can call a webhook or emit a CI event: Linear, Zendesk, custom internal tools, cron jobs, or other
            business systems can hit the Zencoder webhook endpoint, while GitHub, GitLab, and Bitbucket platform triggers
            fire on pushes, pull requests, or scheduled workflows. If a system can send HTTP, it can wake an autonomous
            agent.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/ci-cd-automation/jira-triggered-autonomous-agents/where-else-can-autonomous-agents-be-triggered-from.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=d425409ee41b8581ed2c6c53b0508cc9" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/ci-cd-automation/jira-triggered-autonomous-agents/where-else-can-autonomous-agents-be-triggered-from.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fci-cd-automation%23jira-triggered-autonomous-agents" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="jira-triggered-autonomous-agents" data-copy-default-label="Download card as image" data-copy-exclude="true">
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