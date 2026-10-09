> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Enterprise Best Practices Overview

Guides for adopting AI coding at an enterprise scale: security, compliance, team workflows, CI/CD automation, and measuring adoption.

## Practice Areas

<Columns cols={2}>
  <Card title="AI Coding Foundations" href="/learn/enterprise-best-practices/ai-coding-foundations">
    Explain the mechanics of LLM copilots, reduce hallucinations, and anchor teams on mental models that keep agents productive and safe.
  </Card>

  <Card title="Security, Compliance & Deployment" href="/learn/enterprise-best-practices/enterprise-security-compliance-deployment">
    Learn how Zencoder meets SOC 2/ISO requirements, configure SSO + RBAC, and monitor usage with BYOK controls for regulated environments.
  </Card>

  <Card title="Team Collaboration & Zen Agents" href="/learn/enterprise-best-practices/team-collaboration-zen-agents">
    Design, share, and govern reusable Zen Agents so squads can encode tribal knowledge and spread expert workflows across the org.
  </Card>

  <Card title="Integration Ecosystem" href="/learn/enterprise-best-practices/integration-ecosystem">
    Connect Jira, MCP tools, and partner systems so Zencoder can reason over external data sources and trigger actions in your toolchain.
  </Card>

  <Card title="CI/CD Automation" href="/learn/enterprise-best-practices/ci-cd-automation">
    Automate pull requests, releases, and multi-repo workflows with GitHub/Jira-triggered agents that keep delivery pipelines moving.
  </Card>

  <Card title="Measuring Success" href="/learn/enterprise-best-practices/measuring-success">
    Define adoption metrics, use the analytics dashboard + API, and report ROI to stakeholders.
  </Card>
</Columns>

## Share the Playbooks

<ul className="space-y-6">
  <li>
    <p>
      <strong>Use the “Share card via email” buttons</strong> on any practice area to pre-fill an email with the exact card link and slug so stakeholders can jump
      straight to the relevant tactics.
    </p>

    <div className="mt-3" data-copy-exclude="true">
      <a
        className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition"
        href="#"
        onClick={(event) => {
      event.preventDefault();
      if (typeof window !== 'undefined') window.alert('This is just an example!');
    }}
      >
        <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
          <rect x="2" y="4" width="20" height="16" rx="2" />

          <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
        </svg>

        <span>Share card via email</span>
      </a>
    </div>
  </li>

  <li>
    <p>
      <strong>Click “Download card as image”</strong> when you need an executive-ready JPG—perfect for slide decks, onboarding docs, or quick Slack updates.
    </p>

    <div className="mt-3" data-copy-exclude="true">
      <button
        type="button"
        className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition"
        onClick={() => {
      if (typeof window !== 'undefined') window.alert('This is just an example!');
    }}
      >
        <svg className="h-4 w-4 text-[#F24A07]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
          <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />

          <circle cx="9" cy="9" r="2" />

          <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
        </svg>

        <span>Download card as image</span>
      </button>
    </div>
  </li>
</ul>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.