> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Module 4: Automations with Remote Agents

## Intro

Module 4 turns agent best practices into hands-free automation: wiring Jira, GitHub, and Zencoder’s autonomous flows so labeled tickets trigger agents that implement fixes and queue peer reviews without manual intervention.

## Video lesson

<div className="mb-4" data-copy-exclude="true">
  <a className="inline-flex items-center gap-2 rounded-xl border border-[#F24A07] bg-[#F24A07] text-white px-4 py-2.5 text-base font-semibold shadow-sm hover:bg-[#d13d05] transition" href="https://www.udemy.com/course/the-10x-engineer-professional-ai-certification/" target="_blank" rel="noreferrer">
    <span>Course on Udemy</span>
  </a>
</div>

The full video is available on Udemy.

## Key takeaways

* Pilot autonomy with a scoped task (e.g., adding docstrings) so you can verify the agent’s output before scaling to broader work.
* In the Zencoder dashboard, create a GitHub connection, register target repos, and spin up an Autonomous Flow (select agent + repo) while copying the webhook URL/secret plus issuing a personal access token (client ID/secret).
* Build a Jira automation that fires on specific labels (such as `zenagents-github`), posts to the Zencoder webhook, and forwards issue summary/description while signing with the stored secret.
* Store the Zencoder client ID/secret and needed GitHub token as encrypted repo secrets so GitHub Actions can authenticate the Zencoder CLI.
* Author GitHub workflows that download the Zencoder CLI, invoke the chosen agent with Jira payload details, and optionally chain a second flow for automated PR review once the implementation agent opens a PR.
* Monitor Actions logs to track agent runs, inspect generated branches/PRs, and confirm that review agents leave feedback before you merge.
* Remember similar setups work for GitLab or Bitbucket; adapt the same webhook/token flow to their automation hooks.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.