> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Enterprise Security, Compliance, and Deployment

<CardGroup cols={1}>
  <div id="the-security-triple-crown-soc-2-type-ii-iso-27001-iso-42001">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Certifications
        </span>
      </h3>

      <div className="mt-3 flex flex-wrap items-center gap-6 text-lg font-semibold text-slate-900 dark:text-white">
        <div className="flex items-center gap-2">
          <span className="text-[#F24A07] text-xl" aria-hidden="true">✓</span>
          <span>SOC 2 Type II</span>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-[#F24A07] text-xl" aria-hidden="true">✓</span>
          <span>ISO/IEC 27001</span>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-[#F24A07] text-xl" aria-hidden="true">✓</span>
          <span>ISO/IEC 42001</span>
        </div>
      </div>

      <div className="space-y-4 mt-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What do these certifications mean for enterprise security?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            SOC 2 Type II confirms an external auditor monitored production controls over time and verified data protection measures.
            ISO/IEC 27001 covers the formal security management system — inventories, risk reviews, policies, and continual improvement.
            ISO/IEC 42001 extends that to AI, requiring documented responsible-AI practices, data governance, monitoring, and human oversight
            from model design through deployment.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/9R0HS7Q5uy7jtU5U/files/enterprise-best-practices/enterprise-security-compliance-deployment/the-security-triple-crown-soc-2-type-ii-iso-27001-iso-42001/what-do-these-certifications-mean-for-enterprise-security.mp4?fit=max&auto=format&n=9R0HS7Q5uy7jtU5U&q=85&s=966843dc208b1698c17c63fda1ce0190" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/the-security-triple-crown-soc-2-type-ii-iso-27001-iso-42001/what-do-these-certifications-mean-for-enterprise-security.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">ISO 42001 is AI-specific; what does it mean?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            ISO/IEC 42001 is the world’s first management standard written for AI systems. It forces vendors to document every AI use case,
            govern the datasets feeding their models, and keep humans in the loop for approvals, monitoring, and incident response. Achieving
            it means Zencoder treats model training and deployment with the same rigor as traditional security: risk assessments, policies,
            audit trails, and continuous improvement for the entire AI lifecycle.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/the-security-triple-crown-soc-2-type-ii-iso-27001-iso-42001/iso-42001-is-ai-specific-what-does-it-mean.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=0d27f4529325bd2d97920cd3bc2d8d9c" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/the-security-triple-crown-soc-2-type-ii-iso-27001-iso-42001/iso-42001-is-ai-specific-what-does-it-mean.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is Zencoder’s zero-storage data privacy architecture?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Every request flows through Zencoder’s proxy, but the code, prompts, and model outputs never land on persistent media—data is
            encrypted in transit, processed in memory, and discarded once the response is returned. Logs retain only high-level metadata so
            customers can audit usage without exposing source code, and admins can pin the pipeline to their own LLM tenancy or keys for
            additional control. The privacy policy, terms of service, and acceptable-use policy lock this in contractually: your content is
            not written to disk, not mined for training, and only the minimal telemetry required for billing and abuse prevention survives.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/9R0HS7Q5uy7jtU5U/files/enterprise-best-practices/enterprise-security-compliance-deployment/the-security-triple-crown-soc-2-type-ii-iso-27001-iso-42001/what-is-zencoder-s-zero-storage-data-privacy-architecture.mp4?fit=max&auto=format&n=9R0HS7Q5uy7jtU5U&q=85&s=c29050925130e23d8f29d4d54af3ff3b" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/the-security-triple-crown-soc-2-type-ii-iso-27001-iso-42001/what-is-zencoder-s-zero-storage-data-privacy-architecture.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fenterprise-security-compliance-deployment%23the-security-triple-crown-soc-2-type-ii-iso-27001-iso-42001" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="the-security-triple-crown-soc-2-type-ii-iso-27001-iso-42001" data-copy-default-label="Download card as image" data-copy-exclude="true">
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

  <div id="configuring-single-sign-on-and-team-access">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Configuring Single Sign-On and Team Access
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How does one setup SSO with Okta or Google Workspace?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Zencoder supports SAML-based single sign-on with Okta and Google Workspace on Pro Plus plans and above. Admins simply exchange the
            IdP metadata with the Zencoder team (or upload it in the SSO section of the dashboard), verify the ACS URL, and flip SSO to
            “required” for the workspace. From that point users click “Sign in with SSO,” enter the company domain, and are routed through
            the IdP—no separate Zencoder password to manage.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/configuring-single-sign-on-and-team-access/how-does-one-setup-sso-with-okta-or-google-workspace.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=a3a5dcda0359e2d187bf72fa52a4cee5" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/configuring-single-sign-on-and-team-access/how-does-one-setup-sso-with-okta-or-google-workspace.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to add team members?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Head to Settings → Users and use the “Invite” button to add teammates up to the number of seats on your contract. Each invite
            captures the user’s email, role, and optional profile info, and the system enforces seat availability automatically. Need to
            give one engineer extra model usage? Adjust the per-user quota multiplier (1×, 2×, or 5×) before sending the invite so their
            allowance scales without over-subscribing the workspace.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/configuring-single-sign-on-and-team-access/how-to-add-team-members.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=97a13fecaa8f33cbd2e137491b023604" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/configuring-single-sign-on-and-team-access/how-to-add-team-members.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to configure role-based access control?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Zencoder keeps RBAC simple: every user is an Owner, Manager, or Member. Owners can manage billing, plan changes, and SSO, while
            Managers can invite and remove users, adjust quotas, and view org-wide settings. Members are limited to product usage only.
            Choose the role during the invite flow so privileged accounts stay limited to the small group that actually needs them.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/configuring-single-sign-on-and-team-access/how-to-configure-role-based-access-control.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=bf3fbb542ea44885ad9022602b279570" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/configuring-single-sign-on-and-team-access/how-to-configure-role-based-access-control.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to manage permissions?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Review the Users page regularly—especially the list of Owners and Managers—so you know exactly who can spend budget or invite
            new teammates. If someone’s responsibilities change, reach out to Zencoder support to adjust their role (or remove the account
            and re-invite with the new role); the three-dot menu also lets you delete dormant users in a few clicks. Keeping that roster tidy
            ensures only the right people wield elevated privileges.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/configuring-single-sign-on-and-team-access/how-to-manage-permissions.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=c900bc313ddad6ac298fcedc7b340b9d" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/configuring-single-sign-on-and-team-access/how-to-manage-permissions.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fenterprise-security-compliance-deployment%23configuring-single-sign-on-and-team-access" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="configuring-single-sign-on-and-team-access" data-copy-default-label="Download card as image" data-copy-exclude="true">
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

  <div id="subscription-management-and-cost-control">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Subscription Management and Cost Control
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How does the per-seat licensing work in Zencoder?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Plans are sold per seat (one paid user). Buy however many seats your org needs, keep everyone on the same tier, and assign them from the Users page. Billing runs
            monthly; if you add seats mid-cycle you only pay the prorated remainder, then the new seat count appears on the next invoice.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/how-does-the-per-seat-licensing-work-in-zencoder.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=a76d0f834d79bf59e5bd8ec1fecb3383" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/how-does-the-per-seat-licensing-work-in-zencoder.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How are LLM calls consumed in Zencoder?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            We meter the real LLM calls instead of charging per “agent request.” Each chat run shows how many calls the agent spent and how many remain, factoring in the org plan
            plus any quota multiplier the user has. That keeps incentives aligned: agents can chain tools freely without silently inflating cost.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/how-are-llm-calls-consumed-in-zencoder.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=6af3fe8192f84486508357104ed27e16" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/how-are-llm-calls-consumed-in-zencoder.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to use BYOK (Bring Your Own Key)? Why use it?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Open the IDE extension’s three-dot menu → Custom API Keys, paste your OpenAI or Anthropic key, and flip the provider toggle. With the key + toggle active the session
            bills your cloud credits instead of Zencoder’s allotment, which is perfect when you already negotiated rates elsewhere. BYOK works on every plan, even free.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/how-to-use-byok-bring-your-own-key-why-use-it.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=8d360405d999294a24c87416c4595a37" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/how-to-use-byok-bring-your-own-key-why-use-it.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How can we monitor usage of Zencoder in the organization?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Head to the Analytics page in the web dashboard. Pick a 7/30/90-day window to refresh the entire view, check the top-line stats (active users, LOC accepted, LOC
            generated), and watch the active-users-per-day chart. The Members table breaks down usage per person and you can export it via “Download CSV,” or pull daily metrics from
            the Analytics API (<span className="text-[#F24A07] underline">[https://docs.zencoder.ai/features/analytics-api](https://docs.zencoder.ai/features/analytics-api)</span>).
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/how-can-we-monitor-usage-of-zencoder-in-the-organization.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=f6529cf5ba9eb02287851be27ebe38f0" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/how-can-we-monitor-usage-of-zencoder-in-the-organization.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What if one specific user (not all) needs more usage?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Use the Quota dropdown on the Users page to boost that member to 2× or 5× the base allowance—essentially lending them extra seats. You can change multipliers anytime
            as long as the extra quota stays within the seats you already purchased. We can also set an account to 0× quota manually so its seat flows to someone who will use it.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/what-if-one-specific-user-not-all-needs-more-usage.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=91a29e3e6caa97d5661e5c3a0be9e1dc" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/enterprise-security-compliance-deployment/subscription-management-and-cost-control/what-if-one-specific-user-not-all-needs-more-usage.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fenterprise-security-compliance-deployment%23subscription-management-and-cost-control" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="subscription-management-and-cost-control" data-copy-default-label="Download card as image" data-copy-exclude="true">
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