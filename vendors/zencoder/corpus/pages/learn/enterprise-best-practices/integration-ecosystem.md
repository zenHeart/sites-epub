> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integration Ecosystem - Connecting Your Development Workflow

<CardGroup cols={1}>
  <div id="how-mcp-works-from-a-theoretical-standpoint">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          How MCP Works from a Theoretical Standpoint
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">Who created MCP?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Anthropic launched MCP as an open-source specification and reference server, but it is intentionally
            vendor-neutral so other model providers, IDE makers, and tool vendors can extend it. Anthropic seeded
            the common language for exposing tools, prompts, and resources to agents, then invited the ecosystem to
            harden and expand the protocol together so every agent can discover and call those capabilities in the
            same way.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/integration-ecosystem/how-mcp-works-from-a-theoretical-standpoint/who-created-mcp.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=aa9894c95033c84dfa511257937a5908" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/integration-ecosystem/how-mcp-works-from-a-theoretical-standpoint/who-created-mcp.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is an MCP? What does it look like?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            An MCP server is a lightweight process—usually a local CLI or a remote service—that exposes a manifest of
            capabilities over a websocket. The manifest lists tools (actions with parameters), resources (read-only data
            the agent can fetch), and prompts (starter templates). When Zencoder connects it introspects that manifest,
            so “what it looks like” to the agent is a structured JSON schema describing each capability plus the live
            stream of responses the server returns whenever the agent calls a tool.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/integration-ecosystem/how-mcp-works-from-a-theoretical-standpoint/what-is-an-mcp-what-does-it-look-like.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=d732e1f43f9f0007df47407bbd48e203" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/integration-ecosystem/how-mcp-works-from-a-theoretical-standpoint/what-is-an-mcp-what-does-it-look-like.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is the difference between Local MCP and Remote MCP?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            A local MCP runs on your own machine, so the agent connects to `localhost` and any underlying APIs are called
            with the credentials stored on your laptop. That’s perfect for personal scripts but it means every teammate
            needs to install the MCP and keep secrets on their device. A remote MCP lives on a shared server: the server
            holds the credentials (e.g., AWS keys), enforces auth via tokens or SSO, and executes the tools centrally, so
            teammates simply connect over HTTPS and never handle the secrets directly.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/integration-ecosystem/how-mcp-works-from-a-theoretical-standpoint/what-is-the-difference-between-local-mcp-and-remote-mcp.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=b982e9eba5db1f3f26bbcf86daffa4cd" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/integration-ecosystem/how-mcp-works-from-a-theoretical-standpoint/what-is-the-difference-between-local-mcp-and-remote-mcp.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fintegration-ecosystem%23how-mcp-works-from-a-theoretical-standpoint" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="how-mcp-works-from-a-theoretical-standpoint" data-copy-default-label="Download card as image" data-copy-exclude="true">
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

  <div id="using-mcp-in-zencoder">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Using MCP in Zencoder
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What is the easiest way to add an MCP in Zencoder, from the library?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Open the three-dot menu → Tools → MCP Library, search the curated list, and pick a server that does not
            require credentials (like Context7). The detail pane shows the official repo plus the server command, and
            clicking <em>Install</em> adds it to your workspace instantly. Every built-in Zencoder agent (Code, Unit Test,
            etc.) inherits that MCP by default, so you can call its tools without configuring tokens or custom settings.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/integration-ecosystem/using-mcp-in-zencoder/what-is-the-easiest-way-to-add-an-mcp-in-zencoder-from-the-library.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=f548f856b787f621c29e3b30048b515c" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/integration-ecosystem/using-mcp-in-zencoder/what-is-the-easiest-way-to-add-an-mcp-in-zencoder-from-the-library.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How to add a custom MCP in Zencoder?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Go to Tools → Add custom MCP, give the integration a recognizable name, and paste the MCP server config—the
            same JSON/command snippet the maintainer documents (e.g., the GitHub or Context7 examples). Click
            <em>Install</em> and it joins your custom tools list. Zencoder’s built-in agents automatically inherit it,
            while custom Zen agents still need you to toggle it on (during creation or afterward) so you can control
            exactly which bespoke agents get access.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/integration-ecosystem/using-mcp-in-zencoder/how-to-add-a-custom-mcp-in-zencoder.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=99315394b7e15299cc788e67340a8c7f" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/integration-ecosystem/using-mcp-in-zencoder/how-to-add-a-custom-mcp-in-zencoder.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What types of MCP authentication can we find?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Local MCPs simply inherit whatever secrets you have on your machine (env vars, CLI logins, keychains), but
            remote MCPs put an extra door in front of the server. Some are open (no auth), others expect a static API key
            or bearer token, and increasingly you will see OAuth/device-code flows where the MCP shows a login link and
            you sign in before it issues a short-lived token. Enterprise deployments may go further with company SSO,
            mutual TLS certificates, or signed requests so only managed devices can connect; after that check passes, the
            MCP uses its own stored credentials (e.g., GitHub or AWS keys) to run the tools.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/OuvGW_xqNIUEo0Hy/files/enterprise-best-practices/integration-ecosystem/using-mcp-in-zencoder/what-types-of-mcp-authentication-can-we-find.mp4?fit=max&auto=format&n=OuvGW_xqNIUEo0Hy&q=85&s=09dc1b64b8c7669db330bf9e0c326a7c" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/integration-ecosystem/using-mcp-in-zencoder/what-types-of-mcp-authentication-can-we-find.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How are MCPs added differently to Zencoder agents vs. custom agents?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Every MCP you install in Tools flows automatically into the built-in Zencoder agents (Code, Unit Test, etc.)
            and cannot be removed there—Ask is the lone exception because it stays intentionally lightweight. Custom Zen
            agents, on the other hand, start with no extra MCPs; you add or remove them one by one in each agent’s tool
            configuration. Because the defaults inherit everything, it is worth pruning unused MCPs in Tools periodically
            so those core agents do not become bloated.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/integration-ecosystem/using-mcp-in-zencoder/how-are-mcps-added-differently-to-zencoder-agents-vs-custom-agents.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=6c052d5848902eda240ff721f601b5d2" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/integration-ecosystem/using-mcp-in-zencoder/how-are-mcps-added-differently-to-zencoder-agents-vs-custom-agents.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fintegration-ecosystem%23using-mcp-in-zencoder" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="using-mcp-in-zencoder" data-copy-default-label="Download card as image" data-copy-exclude="true">
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

  <div id="jira-integration-for-ticket-to-code-workflow">
    <Card title="" className="bg-[#F24A07]/5 dark:bg-[#F24A07]/10 border border-[#F24A07]/20">
      <h3 className="text-xl font-semibold text-slate-900 dark:text-white mb-3">
        <span className="bg-[#F24A07]/15 dark:bg-[#F24A07]/25 text-[#F24A07] px-3 py-1 rounded">
          Jira Integration for Ticket-to-Code Workflow
        </span>
      </h3>

      <div className="space-y-4">
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">How can we connect Jira to Zencoder?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            Jira ships as a native integration, so no MCP is required. From any chat, open the attach-context menu (click
            or type @) and pick <em>Jira</em>; the first time, you will be prompted to connect. Click <em>Connect</em> to
            jump to the Integrations page, hit <em>Connect</em> next to Jira, and approve the browser flow where you choose
            which Jira project to authorize. Once approved, the toggle flips to <em>Disconnect</em> (and you can swap
            projects later), and the @ menu now lists your Jira issues so you can attach any ticket as context in a single
            click.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video" defaultOpen>
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/9R0HS7Q5uy7jtU5U/files/enterprise-best-practices/integration-ecosystem/jira-integration-for-ticket-to-code-workflow/how-can-we-connect-jira-to-zencoder.mp4?fit=max&auto=format&n=9R0HS7Q5uy7jtU5U&q=85&s=6febfdebd5987765623975ebe7b45a45" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/integration-ecosystem/jira-integration-for-ticket-to-code-workflow/how-can-we-connect-jira-to-zencoder.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/60 px-4 py-3 shadow-sm">
          <p className="text-base font-semibold text-slate-900 dark:text-white">What’s the benefit?</p>

          <p className="text-base text-slate-600 dark:text-slate-300 mt-1">
            The integration removes copy/paste. Select a Jira issue from the @ menu and Zencoder injects the ticket’s
            title, description, and links straight into the conversation, so you can either add follow-up instructions or
            just send the ticket reference and let the agent run with it. Because the Integrations page exposes a quick
            <em>Disconnect</em> button plus a project selector, it is easy to revoke or re-scope access whenever priorities
            change.
          </p>

          <div className="mt-2 video-accordion">
            <AccordionGroup>
              <Accordion title="Watch video">
                <video className="w-full rounded-xl mt-1 border border-slate-200 dark:border-slate-800" src="https://mintcdn.com/forgoodaiinc/3DaobxETF8pO9d_v/files/enterprise-best-practices/integration-ecosystem/jira-integration-for-ticket-to-code-workflow/what-s-the-benefit.mp4?fit=max&auto=format&n=3DaobxETF8pO9d_v&q=85&s=9571bc1a17e2fb7196035db924ce8edc" controls playsInline preload="metadata" data-copy-exclude="true" data-path="files/enterprise-best-practices/integration-ecosystem/jira-integration-for-ticket-to-code-workflow/what-s-the-benefit.mp4" />
              </Accordion>
            </AccordionGroup>
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-3 justify-center">
        <a className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] bg-[#F24A07] text-white px-3 py-1.5 text-sm font-semibold hover:bg-[#d13d05] transition" href="mailto:?subject=Check%20out%20with%20AI%20coding%20best%20practice&body=I%20though%20you%20would%20appreciate%20reading%20about%20this%20AI%20coding%20best%20practices%20for%20enterprise%2C%20via%20Zencoder.ai%0A%0Ahttps%3A%2F%2Fdocs.zencoder.ai%2Flearn%2Fenterprise-best-practices%2Fintegration-ecosystem%23jira-integration-for-ticket-to-code-workflow" rel="noreferrer" data-copy-exclude="true">
          <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />

            <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" />
          </svg>

          Share card via email
        </a>

        <button type="button" className="inline-flex items-center gap-2 rounded-lg border border-[#F24A07] text-[#F24A07] px-3 py-1.5 text-sm font-semibold hover:bg-[#F24A07]/10 transition disabled:opacity-60 disabled:cursor-not-allowed" data-copy-target="jira-integration-for-ticket-to-code-workflow" data-copy-default-label="Download card as image" data-copy-exclude="true">
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