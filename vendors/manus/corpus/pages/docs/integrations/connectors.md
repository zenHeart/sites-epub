> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectors

> Browse every connector available in Manus and learn how to connect apps, MCP servers, and APIs to your tasks.

## What it is

Connectors give Manus access to the apps and services you already use. When you enable a connector, Manus can read data from that service and take actions in it during a task. For example, Manus can search your [Gmail](https://manus.im/connectors/gmail), update a [Notion](https://manus.im/connectors/notion) page, or check a [Vercel](https://manus.im/connectors/vercel) deployment.

For an overview of what connectors can do, see the [Connectors feature page](https://manus.im/features/connectors).

Manus currently offers **416 connectors** in its catalog. Each connector uses one of three connection types:

| Type | How it connects | What you provide |
| :- | :- | :- |
| App | A built-in integration that Manus maintains | You sign in to your account |
| MCP | A Model Context Protocol (MCP) server for the service | You sign in or add a key, depending on the server |
| API key | A direct connection to the service's API | You paste an API key or token |

The catalog has 13 App connectors, 369 MCP connectors, and 34 API key connectors.

> [!NOTE]
>
> This page was last updated on November 2, 2026. Manus adds new connectors regularly, and this page updates when the catalog changes.

## How to use it

**1. Open Connectors**

In Manus, open **Connectors**. You can also go directly to [Explore connectors](https://manus.im/app?openConnectors=true).

**2. Find a connector**

Search for the app or service by name, or browse the catalog. Use the directory below to see what each connector does.

**3. Connect your account**

Select the connector and follow the prompts. For most App and MCP connectors, you sign in to the service and approve access. For API key connectors, you enter the key or token from that service.

**4. Use it in a task**

Mention the app in your prompt. For example: "Check my unread Gmail messages from today and summarize what needs attention." Manus uses the enabled connector to complete the task.

If your task needs a connector that you have not enabled, Manus recommends it in the conversation. Manus enables it only after you approve. If the connector needs a sign-in, you must complete that step yourself.

To connect a service that is not in the catalog, see [Custom MCP Servers](https://manus.im/docs/integrations/custom-mcp.md).

## Connector directory

Select a category to see its connectors. The **Type** column shows how each connector connects.

> [accordion] Productivity and documents (41)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [Airtable](https://manus.im/connectors/airtable) | MCP | Search, read, and update records or manage database tables |
> | [Box](https://manus.im/features/connectors) | MCP | Search files, preview documents, extract data, and automate content workflows |
> | [CalendarBridge](https://manus.im/features/connectors) | MCP | Manage calendars, schedule events, create links, and configure calendar syncing |
> | [Calendly](https://manus.im/connectors/calendly) | MCP | Manage event types, availability, meetings, invitees, and scheduling links |
> | [Circleback](https://manus.im/features/connectors) | MCP | Search meeting transcripts, action items, calendar events, emails, and contacts |
> | [Coda](https://manus.im/features/connectors) | MCP | Create and update documents, pages, tables, and comments |
> | [Craft](https://manus.im/features/connectors) | MCP | Search and edit documents, organize tasks, and manage workspace collections |
> | [Dropbox](https://manus.im/connectors/dropbox) | MCP | Search, create, and organize files, extract text, and generate shared links |
> | [Dropbox API](https://manus.im/connectors/dropbox) | API key | Upload, download, organize, and share files programmatically |
> | [Egnyte](https://manus.im/features/connectors) | MCP | Search files, summarize content, manage folders, and access project documents |
> | [Evernote](https://manus.im/features/connectors) | MCP | Find, create, and organize notes, notebooks, tasks, and attachments |
> | [Falconer](https://manus.im/features/connectors) | MCP | Search, create, and update documents, comments, folders, and permissions |
> | [Fathom](https://manus.im/features/connectors) | MCP | Search meeting recordings, retrieve transcripts, find action items, and review event details |
> | [Fellow](https://manus.im/features/connectors) | MCP | Search meeting summaries, transcripts, action items, and participant details |
> | [Fireflies](https://manus.im/features/connectors) | MCP | Transcribe and summarize meetings to support follow-ups |
> | [Gamma](https://manus.im/features/connectors) | MCP | Create presentations, documents, webpages, and social posts; browse and export projects |
> | [GitBook](https://manus.im/features/connectors) | MCP | Create documentation sites, edit content, and reorganize pages |
> | [Google Calendar](https://manus.im/connectors/google-calendar) | App | Organize calendar events, set reminders, and automate scheduling |
> | [Google Workspace](https://manus.im/connectors/google-drive) | App | Find files, analyze content, and organize workspace information |
> | [Granola](https://manus.im/features/connectors) | MCP | Search meeting transcripts, summarize them, and surface insights |
> | [Guru](https://manus.im/features/connectors) | MCP | Search verified knowledge, ask questions, and draft or update documents |
> | [Heptabase](https://manus.im/features/connectors) | MCP | Search notes and PDFs, read content, and save notes or journal entries |
> | [Jotform](https://manus.im/connectors/jotform) | MCP | Create forms, manage submissions, and connect data collection to workflows |
> | [Lucid](https://manus.im/connectors/lucid) | MCP | Search documents, edit diagrams, manage sharing, and export files |
> | [Lumin PDF](https://manus.im/features/connectors) | MCP | Send signature requests, manage files, and generate PDFs from Markdown |
> | [Mem](https://manus.im/features/connectors) | MCP | Search, read, create, and organize notes in your knowledge base |
> | [Mintlify](https://manus.im/features/connectors) | MCP | Search, edit, and publish documentation, update navigation, and review changes |
> | [Notion](https://manus.im/connectors/notion) | MCP | Create, edit, search, and organize workspace pages, databases, and content |
> | [Outlook Calendar](https://manus.im/connectors/outlook) | App | Schedule events, set reminders, and organize your calendar |
> | [PandaDoc](https://manus.im/features/connectors) | MCP | Create documents, send them for eSignature, track status, and analyze activity |
> | [Plaud](https://manus.im/features/connectors) | MCP | Search recordings and retrieve transcripts, summaries, and action items |
> | [Read AI](https://manus.im/features/connectors) | MCP | Search meeting transcripts, summaries, action items, and recordings |
> | [Readwise](https://manus.im/features/connectors) | MCP | Search highlights and reading documents, and ask questions about your reading history |
> | [Responsive](https://manus.im/features/connectors) | MCP | Find approved content and draft grounded responses for RFPs and questionnaires |
> | [Revise](https://manus.im/features/connectors) | MCP | Create, edit, search, export, and collaborate on documents |
> | [SignNow](https://manus.im/features/connectors) | MCP | Send signing invitations, manage documents, and download completed files |
> | [Tally](https://manus.im/features/connectors) | MCP | Create and update forms, manage settings, and review submissions |
> | [Tana](https://manus.im/features/connectors) | MCP | Search, review, and update workspace content, documents, tables, and calendars |
> | [Tana Outliner](https://manus.im/features/connectors) | MCP | Search and update structured notes, tasks, tags, and workspace content |
> | [Typeform](https://manus.im/connectors/typeform) | API key | Create surveys, retrieve responses, and automate workflows with webhooks |
> | [Typeform](https://manus.im/connectors/typeform) | MCP | Read forms and manage respondent contacts |

> [accordion] Communication and email (16)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [AgentMail](https://manus.im/features/connectors) | MCP | Create inboxes and send, schedule, search, and manage email messages |
> | [Demodesk](https://manus.im/features/connectors) | MCP | Search meeting recordings, transcripts, summaries, and coaching scorecards |
> | [Fastmail](https://manus.im/features/connectors) | MCP | Search and manage email, contacts, and calendar events |
> | [Gmail](https://manus.im/connectors/gmail) | App | Search, organize, and reply to emails |
> | [Krisp](https://manus.im/features/connectors) | MCP | Search meeting conversations, read transcripts, and manage action items |
> | [LINE](https://manus.im/features/connectors) | MCP | Send messages, broadcast announcements, retrieve profiles, and manage rich menus |
> | [Otter.ai](https://manus.im/features/connectors) | MCP | Search meeting history, retrieve transcripts, and view profile information |
> | [Outlook Mail](https://manus.im/connectors/outlook) | App | Search, organize, and reply to emails |
> | [Resend](https://manus.im/features/connectors) | MCP | Send transactional emails and campaigns, manage contacts, and configure webhooks |
> | [Roam](https://manus.im/features/connectors) | MCP | Search meeting transcripts, post chat messages, and create calendar events |
> | [SendMux](https://manus.im/features/connectors) | MCP | Manage mailboxes, send emails, and monitor delivery infrastructure |
> | [Slack](https://manus.im/connectors/slack) | MCP | Search, read, and write conversations to support team workflows |
> | [Superhuman Mail](https://manus.im/features/connectors) | MCP | Search email, draft replies, manage attachments, and update calendar events |
> | [tl;dv](https://manus.im/features/connectors) | MCP | Retrieve meeting details, transcribe conversations, and extract highlights |
> | [Wispr Flow](https://manus.im/features/connectors) | MCP | Search meeting transcripts, summaries, notes, and recordings |
> | [Zoom](https://manus.im/features/connectors) | MCP | Find meeting recordings and create documents from Markdown |

> [accordion] Project and work management (20)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [Asana](https://manus.im/connectors/asana) | MCP | Manage tasks, projects, and goals |
> | [Atlassian](https://manus.im/connectors/atlassian) | MCP | Search, summarize, create, and update issues, pages, and documentation |
> | [ClickUp](https://manus.im/connectors/clickup) | MCP | Create, update, and search tasks across projects |
> | [DevRev](https://manus.im/features/connectors) | MCP | Manage issues, tickets, work items, sprints, and team workflows |
> | [Fibery](https://manus.im/features/connectors) | MCP | Query databases, manage workflows, create entities, and update schemas |
> | [Ketryx](https://manus.im/features/connectors) | MCP | Search projects, configuration items, versions, and documentation |
> | [Linear](https://manus.im/connectors/linear) | MCP | Create and update issues, plan projects, and track team workflows |
> | [Make](https://manus.im/connectors/make) | MCP | Discover and run automations that connect apps and perform tasks |
> | [Miro](https://manus.im/connectors/miro) | MCP | Create collaborative boards, diagrams, tables, and documents, and resolve comments |
> | [monday.com](https://manus.im/connectors/monday) | MCP | Manage board items, assign owners, set timelines, and post updates |
> | [Podio](https://manus.im/features/connectors) | MCP | Manage workspaces, records, comments, and tasks |
> | [Productboard](https://manus.im/features/connectors) | MCP | Search and edit product specs, comment with owners, and update statuses |
> | [Rhythm](https://manus.im/features/connectors) | MCP | Track goals, manage tasks, prepare meetings, and draft weekly check-ins |
> | [Smartsheet](https://manus.im/connectors/smartsheet) | MCP | Manage sheets, rows, workspaces, discussions, reports, and dashboards |
> | [Taskade](https://manus.im/features/connectors) | MCP | Manage projects and tasks, deploy agents, and automate workflows |
> | [Todoist](https://manus.im/connectors/todoist) | MCP | Organize tasks, manage projects, and keep to-do details in sync |
> | [Trello](https://manus.im/connectors/trello) | MCP | Manage boards, lists, cards, checklists, and calendar events |
> | [Wrike](https://manus.im/features/connectors) | MCP | Track projects, manage tasks, organize folders, and customize workflows |
> | [Zapier](https://manus.im/connectors/zapier) | MCP | Search app data and automate actions such as sending emails and scheduling meetings |
> | [Zoho](https://manus.im/connectors/zoho) | MCP | Manage deals, invoices, tickets, and projects across business apps |

> [accordion] Developer tools and infrastructure (62)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [Anthropic](https://manus.im/features/connectors) | API key | Generate content and handle complex tasks with AI assistant services |
> | [Antimetal](https://manus.im/features/connectors) | MCP | Investigate infrastructure issues, inspect root causes, and retrieve remediation plans |
> | [AWS Knowledge](https://manus.im/features/connectors) | MCP | Find AWS documentation, best practices, and service workflow guidance |
> | [Blockscout](https://manus.im/features/connectors) | MCP | Explore blockchain data, inspect contracts, and query tokens, NFTs, and transactions |
> | [Braintrust](https://manus.im/features/connectors) | MCP | Analyze production traces, experiments, and datasets, and run evaluations |
> | [Buildkite](https://manus.im/features/connectors) | MCP | Manage build pipelines, inspect jobs and logs, and analyze test failures |
> | [Checkmarx](https://manus.im/features/connectors) | MCP | Find security vulnerabilities and get remediation guidance for code and infrastructure |
> | [Clerk](https://manus.im/features/connectors) | MCP | Find SDK code snippets, implementation guides, and framework-specific patterns |
> | [Cloudflare](https://manus.im/connectors/cloudflare) | MCP | Manage Cloudflare services and search developer documentation |
> | [Cloudflare API](https://manus.im/connectors/cloudflare) | API key | Automate website deployment, DNS, security, and integrations |
> | [Cloudflare Worker Bindings](https://manus.im/connectors/cloudflare) | MCP | Create, deploy, and manage Workers and associated resources |
> | [Cohere](https://manus.im/features/connectors) | API key | Build applications for text understanding, generation, and classification |
> | [Context7](https://manus.im/connectors/context7) | MCP | Find current technical documentation and implementation examples for software libraries |
> | [Coralogix](https://manus.im/features/connectors) | MCP | Query logs, metrics, and traces, investigate incidents, and manage observability resources |
> | [Datadog](https://manus.im/connectors/datadog) | MCP | Investigate logs, metrics, traces, monitors, incidents, and platform resources |
> | [Dify](https://manus.im/features/connectors) | MCP | Trigger workflows, query data, and manage tasks through Dify apps |
> | [FireHydrant](https://manus.im/features/connectors) | MCP | Manage incidents, search monitoring alerts, and create retrospectives |
> | [GitHits](https://manus.im/features/connectors) | MCP | Explore open-source code, dependencies, vulnerabilities, documentation, and implementation examples |
> | [GitHub](https://manus.im/connectors/github) | App | Search and organize repositories, manage issues and pull requests, and automate workflows |
> | [Google Gemini](https://manus.im/features/connectors) | API key | Analyze text, images, and code |
> | [Harness](https://manus.im/features/connectors) | MCP | Manage and diagnose CI/CD, cloud, security, and developer resources |
> | [Honeycomb](https://manus.im/features/connectors) | MCP | Query observability data, investigate anomalies, and manage service objectives |
> | [IcePanel](https://manus.im/features/connectors) | MCP | Explore and update architecture models, diagrams, flows, and decision records |
> | [ilert](https://manus.im/features/connectors) | MCP | Inspect incidents, correlate alerts with deployments, and review on-call schedules |
> | [incident.io](https://manus.im/features/connectors) | MCP | Analyze incidents, manage escalations, and review on-call schedules and telemetry |
> | [Jam](https://manus.im/features/connectors) | MCP | Analyze bug recordings with video, user events, logs, errors, and network requests |
> | [Jentic](https://manus.im/features/connectors) | MCP | Find APIs, execute operations and workflows, and inspect stored credentials |
> | [JSONBin.io](https://manus.im/features/connectors) | API key | Store and retrieve JSON data through an API |
> | [LaunchDarkly](https://manus.im/features/connectors) | MCP | Manage feature flags and experiments, and query observability data |
> | [LiveKit Docs](https://manus.im/features/connectors) | MCP | Search official documentation, changelogs, code repositories, and pricing information |
> | [Mapbox](https://manus.im/features/connectors) | MCP | Search locations, geocode addresses, calculate routes, and generate map images |
> | [Meticulous](https://manus.im/features/connectors) | MCP | Review test results, investigate regressions, inspect coverage, and trigger test runs |
> | [n8n](https://manus.im/connectors/n8n) | MCP | Build and run workflows, manage credentials, and query data tables |
> | [n8n API](https://manus.im/connectors/n8n) | API key | Create workflows that connect apps and automate repetitive tasks |
> | [Nango](https://manus.im/features/connectors) | MCP | Run integration actions while managing API credentials, retries, and logging |
> | [Netlify](https://manus.im/connectors/netlify) | MCP | Deploy projects, inspect logs, and manage environment settings and access controls |
> | [OpenAI](https://manus.im/features/connectors) | API key | Generate text, hold conversations, and create content with language models |
> | [OpenRouter](https://manus.im/features/connectors) | MCP | Compare AI models, check pricing and benchmarks, test prompts, and search documentation |
> | [OpenRouter API](https://manus.im/features/connectors) | API key | Access multiple AI model services through a unified API |
> | [Opsera](https://manus.im/features/connectors) | MCP | Manage pipelines and projects, monitor executions, and retrieve analytics and logs |
> | [PagerDuty](https://manus.im/connectors/pagerduty) | MCP | Manage incidents and on-call schedules, analyze service performance, and trigger workflows |
> | [Playwright](https://manus.im/features/connectors) | MCP | Automate browser interactions, fill forms, upload files, and capture screenshots |
> | [Postman](https://manus.im/connectors/postman) | MCP | Create and manage API workspaces, collections, specifications, and monitors |
> | [Red Sift](https://manus.im/features/connectors) | MCP | Manage email security compliance, domain monitoring, certificates, accounts, and users |
> | [Render](https://manus.im/features/connectors) | MCP | Manage services, inspect deploys and logs, analyze metrics, and query Postgres |
> | [Replicate](https://manus.im/features/connectors) | MCP | Find AI models, compare capabilities and pricing, run predictions, and manage deployments |
> | [Resolve](https://manus.im/features/connectors) | MCP | Investigate incidents, analyze telemetry, explore causes, and coordinate resolutions |
> | [Roboflow](https://manus.im/features/connectors) | MCP | Explore computer-vision projects, run inference, and manage models and deployments |
> | [Rootly](https://manus.im/features/connectors) | MCP | Manage incidents, alerts, on-call schedules, and response handoffs |
> | [Sentry](https://manus.im/connectors/sentry) | MCP | Review application issues, manage projects, and identify error causes |
> | [Serena](https://manus.im/features/connectors) | MCP | Search code semantically, edit symbols, and manage projects |
> | [SmartSpectra](https://manus.im/features/connectors) | MCP | Manage developer accounts, app registrations, API keys, and SDK settings |
> | [Sonatype Guide](https://manus.im/features/connectors) | MCP | Review software components, licenses, vulnerabilities, dependencies, and upgrades |
> | [Sourcegraph](https://manus.im/features/connectors) | MCP | Search code, inspect repositories, navigate symbols, and investigate history |
> | [Statsig](https://manus.im/features/connectors) | MCP | Create and analyze feature gates, experiments, configurations, and metrics |
> | [Stytch](https://manus.im/features/connectors) | MCP | Manage authentication projects, credentials, templates, and SDK configurations |
> | [Tailscale](https://manus.im/features/connectors) | App | Connect private network services and devices to your workflow |
> | [TierZero](https://manus.im/features/connectors) | MCP | Investigate logs, metrics, traces, code, and deployment workflows |
> | [Tines](https://manus.im/features/connectors) | MCP | Trigger workflow actions, query data, and orchestrate security and business processes |
> | [Twilio Documentation](https://manus.im/features/connectors) | MCP | Search API endpoint documentation across messaging, voice, verification, and other products |
> | [Vercel](https://manus.im/connectors/vercel) | MCP | Manage deployments, inspect build logs, check domains, and search documentation |
> | [WorkOS](https://manus.im/features/connectors) | MCP | Configure organizations, users, roles, SSO connections, and audit log streams |

> [accordion] Data, analytics and databases (40)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [Amplitude](https://manus.im/connectors/amplitude) | MCP | Query and create charts, dashboards, experiments, and audience cohorts |
> | [Amplitude EU](https://manus.im/connectors/amplitude) | MCP | Query product data and create charts, dashboards, experiments, and cohorts |
> | [Atlan](https://manus.im/features/connectors) | MCP | Search governed data assets, trace lineage, run SQL, and propose metadata updates |
> | [ChartMogul](https://manus.im/features/connectors) | MCP | Analyze subscription revenue, churn, retention, customer histories, and forecasts |
> | [ClickHouse](https://manus.im/features/connectors) | MCP | Inspect ClickHouse Cloud resources and run read-only queries |
> | [CockroachDB Cloud](https://manus.im/features/connectors) | MCP | Explore clusters, schemas, query results, and running queries |
> | [Contentsquare](https://manus.im/features/connectors) | MCP | Analyze user behavior, funnels, journeys, page performance, and errors |
> | [Databricks](https://manus.im/connectors/databricks) | MCP | Ask data questions, search indexes, run SQL, and call catalog functions |
> | [DataFast](https://manus.im/features/connectors) | MCP | Analyze website traffic, revenue, conversion funnels, and visitor segments |
> | [Deepnote](https://manus.im/features/connectors) | MCP | Create and run notebooks, manage projects, and explore workspace resources |
> | [Dovetail](https://manus.im/features/connectors) | MCP | Search research projects and retrieve insights, entries, and extracted document text |
> | [Enterpret](https://manus.im/features/connectors) | MCP | Analyze customer feedback themes, sentiment, evidence, and attributed quotes |
> | [FactSet](https://manus.im/features/connectors) | MCP | Access financial, company, market, ownership, and supply chain data |
> | [Grafana](https://manus.im/features/connectors) | MCP | Search dashboards, query data sources, and retrieve incidents and alerts |
> | [Hex](https://manus.im/features/connectors) | MCP | Search workspace projects and explore data through natural language |
> | [MarcoPolo](https://manus.im/features/connectors) | MCP | Query connected systems, profile datasets, and investigate issues across data stores |
> | [Metabase](https://manus.im/features/connectors) | MCP | Search, retrieve, and export analytics data from Metabase |
> | [Microsoft Clarity](https://manus.im/features/connectors) | MCP | Query traffic dashboards and review session recordings to understand site performance |
> | [Mixpanel](https://manus.im/features/connectors) | MCP | Analyze user behavior, build dashboards, and manage experiments and data quality |
> | [Monte Carlo](https://manus.im/features/connectors) | MCP | Investigate data quality alerts, inspect lineage, and manage monitors |
> | [MotherDuck](https://manus.im/features/connectors) | MCP | Run DuckDB queries, inspect schemas, and create interactive visualizations |
> | [Neon](https://manus.im/connectors/neon) | MCP | Create database projects, run queries, and change Postgres schemas |
> | [NocoDB](https://manus.im/features/connectors) | MCP | Query, update, and organize database records, tables, and attachments |
> | [Omni Analytics](https://manus.im/features/connectors) | MCP | Query data models, search documentation, and perform iterative data analysis |
> | [Orion](https://manus.im/features/connectors) | MCP | Ask data questions, monitor metrics, review dashboards, and run workflows |
> | [Pendo](https://manus.im/features/connectors) | MCP | Query product analytics, feature adoption, guide performance, NPS, and session replays |
> | [PlanetScale](https://manus.im/features/connectors) | MCP | Explore databases and schemas, run SQL queries, and review performance |
> | [Polar Analytics](https://manus.im/features/connectors) | MCP | Generate reports and explore ecommerce metrics and dashboards |
> | [PopHIVE](https://manus.im/features/connectors) | MCP | Explore public health datasets on immunization, disease, and hospital trends |
> | [PostHog](https://manus.im/connectors/posthog) | MCP | Analyze product data, manage feature flags, and run experiments |
> | [Prisma Postgres](https://manus.im/features/connectors) | MCP | Explore a Postgres database, run queries, manage backups, and oversee migrations |
> | [S\&P Global](https://manus.im/features/connectors) | MCP | Query company financials, transactions, indices, transcripts, and market data |
> | [SandboxAQ](https://manus.im/features/connectors) | MCP | Calculate catalyst adsorption energy and predict protein-ligand activity |
> | [Sigma](https://manus.im/features/connectors) | MCP | Find data assets, explore schemas, and query live data |
> | [Snowflake](https://manus.im/connectors/snowflake) | MCP | Retrieve and query governed data using natural-language tools and SQL |
> | [Supabase](https://manus.im/connectors/supabase) | MCP | Manage database tables, run queries, deploy functions, and update project settings |
> | [Supabase API](https://manus.im/connectors/supabase) | API key | Build backends with databases, authentication, file storage, and real-time subscriptions |
> | [Synthesize Bio](https://manus.im/features/connectors) | MCP | Analyze gene expression data and retrieve differential-expression reports and raw counts |
> | [Tableau](https://manus.im/connectors/tableau) | MCP | Explore business data sources, query views, and retrieve metrics and insights |
> | [Windsor.ai](https://manus.im/features/connectors) | MCP | Query and analyze live data from advertising, sales, and commerce sources |

> [accordion] Sales and CRM (28)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [ActiveCampaign](https://manus.im/features/connectors) | MCP | Manage contacts, campaigns, automation workflows, and sales pipelines |
> | [Amplemarket](https://manus.im/features/connectors) | MCP | Find prospects, manage outreach, and analyze sales engagement performance |
> | [Apollo](https://manus.im/features/connectors) | MCP | Find prospects, enrich contacts, manage outreach, and review sales analytics |
> | [Apollo API](https://manus.im/features/connectors) | API key | Search for prospects and enrich contact and company data for sales workflows |
> | [Attio](https://manus.im/connectors/attio) | MCP | Manage CRM records, pipelines, tasks, communications, and reports |
> | [Carta CRM](https://manus.im/features/connectors) | MCP | Manage CRM contacts, deals, fundraising opportunities, campaigns, and pipeline reports |
> | [Clarify](https://manus.im/features/connectors) | MCP | Manage CRM records, analyze pipelines, run email campaigns, and find leads |
> | [Clay](https://manus.im/connectors/clay) | MCP | Find and enrich contacts and companies with professional and business data |
> | [Close](https://manus.im/features/connectors) | MCP | Manage leads, track opportunities, and prepare email templates |
> | [Common Room](https://manus.im/features/connectors) | MCP | Research accounts, prepare call briefs, find prospects, and draft outreach |
> | [Crossbeam](https://manus.im/features/connectors) | MCP | Find partner account overlaps, identify co-selling opportunities, and rank deal recommendations |
> | [Day AI](https://manus.im/features/connectors) | MCP | Manage CRM contacts and opportunities, draft emails, and analyze pipeline metrics |
> | [Dex](https://manus.im/features/connectors) | MCP | Manage contacts, log interactions, set reminders, and organize relationships |
> | [Explorium](https://manus.im/features/connectors) | MCP | Research companies and professionals, and monitor business events |
> | [FullEnrich](https://manus.im/features/connectors) | MCP | Find people and companies, enrich contacts, and export verified contact details |
> | [Grain](https://manus.im/features/connectors) | MCP | Search meeting transcripts, review notes, and find sales coaching insights |
> | [Harmonic](https://manus.im/features/connectors) | MCP | Research company, people, and investor data and manage lists |
> | [HighLevel LeadConnector](https://manus.im/features/connectors) | MCP | Manage contacts, conversations, calendars, content, and sales pipelines |
> | [HubSpot](https://manus.im/connectors/hubspot) | MCP | Search and retrieve CRM information about contacts, deals, companies, and tickets |
> | [Hunter](https://manus.im/features/connectors) | MCP | Find and verify email addresses, enrich leads, and save contacts |
> | [Lightfield](https://manus.im/features/connectors) | MCP | Read and update CRM records, including accounts, contacts, opportunities, and tasks |
> | [Phoenix](https://manus.im/features/connectors) | MCP | Research company data and qualify sales accounts |
> | [Regal](https://manus.im/features/connectors) | MCP | Review contact histories, calls, customer journeys, AI agents, and routing tasks |
> | [Salesloft](https://manus.im/features/connectors) | MCP | Review sales accounts, opportunities, calls, forecasts, and engagement metrics |
> | [Sumble](https://manus.im/features/connectors) | MCP | Search and enrich sales data about organizations, people, and job postings |
> | [Sybill](https://manus.im/features/connectors) | MCP | Review sales conversations, summaries, transcripts, deals, and accounts |
> | [Vibe Prospecting](https://manus.im/features/connectors) | MCP | Find decision-makers, enrich company profiles, and build targeted lead lists |
> | [Zocks](https://manus.im/features/connectors) | MCP | Search advisor records and transcripts to identify planning gaps and prepare reports |

> [accordion] Marketing, SEO and advertising (39)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [Adjust API](https://manus.im/features/connectors) | API key | Retrieve mobile campaign installs, revenue, sessions, and retention data |
> | [Adzviser](https://manus.im/features/connectors) | MCP | Analyze marketing spend, conversions, and campaign returns across platforms |
> | [Ahrefs](https://manus.im/connectors/ahrefs) | MCP | Research keywords, analyze competitors, track rankings, and audit websites |
> | [Ahrefs API](https://manus.im/connectors/ahrefs) | API key | Analyze keyword rankings, backlinks, and competitor SEO performance |
> | [AirOps](https://manus.im/features/connectors) | MCP | Track brand visibility in AI search and find citation opportunities |
> | [AWeber](https://manus.im/features/connectors) | MCP | Manage subscribers, schedule email broadcasts, and review campaign performance |
> | [beehiiv](https://manus.im/features/connectors) | MCP | Create newsletter posts, manage subscribers, automate workflows, and review analytics |
> | [Bitly](https://manus.im/features/connectors) | MCP | Create and track short links and QR codes |
> | [Braze](https://manus.im/connectors/braze) | MCP | Analyze marketing campaigns and manage content blocks and media assets |
> | [Customer.io](https://manus.im/features/connectors) | MCP | Manage campaigns, newsletters, segments, and customer data pipelines |
> | [DataForSEO](https://manus.im/features/connectors) | MCP | Research keywords, analyze search results and backlinks, and audit websites |
> | [Elastic Email](https://manus.im/features/connectors) | MCP | Send emails, manage campaigns and contacts, and retrieve templates |
> | [Google Ads](https://manus.im/connectors/google-ads) | App | Query advertising accounts, campaign metrics, and performance data |
> | [Helium 10](https://manus.im/features/connectors) | MCP | Research keywords, analyze Amazon listings, and review advertising data |
> | [Instagram Creator Marketplace](https://manus.im/features/connectors) | App | Discover creators by audience reach, topics, and content style |
> | [Instantly](https://manus.im/features/connectors) | MCP | Manage email campaigns and leads, reply to messages, and review performance |
> | [Iterable](https://manus.im/features/connectors) | MCP | Review marketing campaigns, metrics, templates, journeys, and experiments |
> | [Klaviyo](https://manus.im/connectors/klaviyo) | MCP | Manage customer profiles and campaigns, and analyze marketing performance |
> | [Linkly](https://manus.im/features/connectors) | MCP | Create short links, manage domains, and analyze click performance |
> | [Listen Labs](https://manus.im/features/connectors) | MCP | Run research studies, review respondent transcripts, and retrieve analysis reports |
> | [Local Falcon](https://manus.im/features/connectors) | MCP | Run local search scans, track rankings, monitor profiles, and analyze visibility |
> | [Mailchimp Marketing](https://manus.im/connectors/mailchimp) | API key | Build email campaigns, manage segmented subscriber lists, and analyze performance |
> | [MailerLite](https://manus.im/features/connectors) | MCP | Manage subscribers, schedule email campaigns, organize groups, and analyze results |
> | [Meta Ads Manager](https://manus.im/features/connectors) | App | Analyze ad performance, get optimization recommendations, and automate reports |
> | [OneSignal](https://manus.im/features/connectors) | MCP | Manage messaging apps, audiences, subscriptions, campaigns, and outcome analytics |
> | [Particl](https://manus.im/features/connectors) | MCP | Track competitor products, pricing, sales trends, campaigns, and retail market leaders |
> | [Peec AI](https://manus.im/features/connectors) | MCP | Track brand visibility and sentiment across AI search engines and analyze competitors |
> | [Profound](https://manus.im/features/connectors) | MCP | Analyze AI visibility, citations, sentiment, and traffic, and run marketing agents |
> | [Sanity](https://manus.im/features/connectors) | MCP | Query, create, and update content, schemas, and scheduled releases |
> | [Semrush](https://manus.im/features/connectors) | MCP | Research keywords, analyze competitors, audit backlinks, and optimize content |
> | [Serpstat](https://manus.im/features/connectors) | MCP | Analyze keywords, research competitors, inspect backlinks, and audit websites |
> | [Similarweb](https://manus.im/features/connectors) | MCP | Analyze website traffic, compare competitors, and explore audience demographics |
> | [Similarweb API](https://manus.im/features/connectors) | API key | Analyze traffic, marketing data, competitors, and audience behavior |
> | [Supermetrics](https://manus.im/features/connectors) | MCP | Query marketing data and create or update advertising campaigns |
> | [TikTok for Business](https://manus.im/connectors/tiktok-ads) | MCP | Manage ad campaigns, audiences, product catalogs, creative assets, and performance reports |
> | [Trendtrack](https://manus.im/features/connectors) | MCP | Research ecommerce stores, search ad libraries, and track competitor brands |
> | [Ubersuggest](https://manus.im/features/connectors) | MCP | Research keywords, analyze competitors, review backlinks, and audit websites |
> | [vidIQ](https://manus.im/features/connectors) | MCP | Research channels, analyze videos, identify trends, and review creator analytics |
> | [Webflow](https://manus.im/connectors/webflow) | MCP | Manage site content, update pages, and publish changes |

> [accordion] Social media and content publishing (15)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [AdaptlyPost](https://manus.im/features/connectors) | MCP | Create and schedule social posts, then review platform analytics |
> | [Ayrshare](https://manus.im/features/connectors) | MCP | Publish and schedule social posts, review analytics, and manage comments and messages |
> | [Blotato](https://manus.im/features/connectors) | MCP | Schedule posts, manage content calendars, and create media from templates |
> | [Brand24](https://manus.im/features/connectors) | MCP | Track brand mentions, analyze sentiment, and identify influential voices across the web |
> | [Buffer](https://manus.im/connectors/buffer) | MCP | Create, schedule, and manage social posts and publishing queues |
> | [Instagram](https://manus.im/connectors/instagram) | App | Plan and publish Instagram posts, stories, and reels |
> | [LunarCrush](https://manus.im/features/connectors) | MCP | Analyze social sentiment, track trends and influencers, and retrieve popular posts |
> | [Metricool](https://manus.im/features/connectors) | MCP | Schedule and edit social posts, review analytics, and monitor competitors |
> | [Postiz](https://manus.im/features/connectors) | MCP | Draft, schedule, and publish social media posts and review analytics |
> | [Publer API](https://manus.im/features/connectors) | API key | Schedule and publish social posts, manage media, and retrieve workspace accounts |
> | [Publora](https://manus.im/features/connectors) | MCP | Create and manage social content, accounts, and engagement analytics |
> | [Restream](https://manus.im/features/connectors) | MCP | Manage broadcast channels, schedule events, organize recordings, and review viewer analytics |
> | [Taplio](https://manus.im/features/connectors) | MCP | Draft, schedule, and publish LinkedIn posts, then review analytics |
> | [WordPress](https://manus.im/connectors/wordpress) | MCP | Create and update posts and pages, manage media, and configure site settings |
> | [Zernio](https://manus.im/features/connectors) | MCP | Schedule posts, manage social inboxes, run campaigns, and track analytics |

> [accordion] Design, images, video and audio (34)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [Agent Opus](https://manus.im/features/connectors) | MCP | Generate videos from prompts, scripts, articles, images, or audio |
> | [Canva](https://manus.im/connectors/canva) | MCP | Search, organize, import, autofill, and export creative projects |
> | [Cloudinary Asset](https://manus.im/features/connectors) | MCP | Upload, organize, search, and transform media assets |
> | [Comfy Cloud](https://manus.im/features/connectors) | MCP | Run cloud workflows to create images, videos, audio, and 3D assets |
> | [Descript](https://manus.im/features/connectors) | MCP | Create, edit, organize, and publish media projects |
> | [ElevenLabs](https://manus.im/connectors/elevenlabs) | MCP | Generate speech, transcribe audio, create sounds, and build conversational agents |
> | [ElevenLabs API](https://manus.im/connectors/elevenlabs) | API key | Generate multilingual speech and create cloned or personalized voices |
> | [Eraser](https://manus.im/features/connectors) | MCP | Create and edit technical diagrams, export images, and manage workspace files |
> | [Excalidraw](https://manus.im/features/connectors) | MCP | Create, find, and edit whiteboard scenes and manage workspace settings |
> | [fal.ai](https://manus.im/features/connectors) | MCP | Generate and edit images, videos, audio, and 3D assets |
> | [Flux](https://manus.im/features/connectors) | MCP | Generate, edit, browse, and create variations of images |
> | [Flux API](https://manus.im/features/connectors) | API key | Generate images in varied artistic styles from creative concepts |
> | [HeyGen](https://manus.im/connectors/heygen) | MCP | Generate avatar videos with realistic voices and facial gestures |
> | [HeyGen API](https://manus.im/connectors/heygen) | API key | Create avatar videos with realistic voices and facial gestures |
> | [Higgsfield](https://manus.im/connectors/higgsfield) | MCP | Generate cinematic images, videos, and campaign-ready creative assets |
> | [Hume](https://manus.im/features/connectors) | MCP | Create natural-sounding speech audio using preset or custom voices |
> | [ImagineArt](https://manus.im/features/connectors) | MCP | Generate and edit images, videos, music, ads, and fashion photoshoots |
> | [Kling](https://manus.im/connectors/kling) | API key | Generate videos from text descriptions |
> | [Leonardo](https://manus.im/features/connectors) | MCP | Generate images from prompts with controls for style, dimensions, and rendering |
> | [Magic Patterns](https://manus.im/features/connectors) | MCP | Generate UI designs, edit code artifacts, manage versions, and publish prototypes |
> | [Magnific](https://manus.im/features/connectors) | MCP | Create and upscale media, train consistent styles, and reuse past creations |
> | [Mermaid Chart](https://manus.im/features/connectors) | MCP | Validate Mermaid syntax, render diagrams, and manage diagram projects |
> | [MiniMax](https://manus.im/features/connectors) | MCP | Generate audio, clone voices, and create images, videos, and music |
> | [Mobbin](https://manus.im/connectors/mobbin) | MCP | Find reference screens and user interface patterns from shipped apps |
> | [Picsart](https://manus.im/features/connectors) | MCP | Create and edit images, videos, and audio, and organize creative files |
> | [Pletor](https://manus.im/features/connectors) | MCP | Run creative workflows, inspect runs, and compare models and credit costs |
> | [QuiverAI](https://manus.im/features/connectors) | MCP | Generate editable SVGs, vectorize images, and retrieve completed artwork |
> | [Runway](https://manus.im/connectors/runway) | MCP | Generate and upscale videos, images, and text-to-speech audio |
> | [Splice](https://manus.im/features/connectors) | MCP | Find music samples, build layered sound stacks, and download audio |
> | [Suno](https://manus.im/features/connectors) | MCP | Create, remix, and save songs from ideas, lyrics, and audio |
> | [Tripo API](https://manus.im/connectors/tripo) | API key | Generate 3D models from text descriptions or 2D images |
> | [VEED Fabric](https://manus.im/features/connectors) | MCP | Generate talking-head videos from scripts using avatars and multilingual voices |
> | [Whimsical](https://manus.im/features/connectors) | MCP | Create and edit diagrams, wireframes, boards, and workspace documents |
> | [Wireflow](https://manus.im/features/connectors) | MCP | Run AI workflows that generate images, video, and audio |

> [accordion] Finance, payments and commerce (51)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [1inch](https://manus.im/features/connectors) | MCP | Explore token prices, swap quotes, portfolio data, and order drafts |
> | [Alpaca](https://manus.im/features/connectors) | MCP | Trade stocks, crypto, and options while tracking portfolios and prices |
> | [Alpha Vantage](https://manus.im/features/connectors) | MCP | Fetch market prices, economic data, and technical analysis |
> | [Bigdata.com](https://manus.im/features/connectors) | MCP | Search financial documents and news, retrieve market benchmarks, and analyze sentiment |
> | [Brex](https://manus.im/features/connectors) | MCP | Review card expenses, spending limits, budgets, and company spend analytics |
> | [Cafe24](https://manus.im/features/connectors) | MCP | Search online store products and review variants, prices, and stock |
> | [Clover API](https://manus.im/features/connectors) | API key | Manage merchant inventory, orders, payments, and customer records |
> | [Coinbase](https://manus.im/features/connectors) | MCP | View portfolio balances, market data, and orders; preview or place trades |
> | [Coinbase Wallet](https://manus.im/features/connectors) | MCP | Manage wallet assets, send and swap tokens, and review transactions |
> | [CoinDesk](https://manus.im/features/connectors) | MCP | Access cryptocurrency market data, on-chain activity, and news |
> | [CoinGecko](https://manus.im/connectors/coingecko) | MCP | Explore cryptocurrency prices, market data, and on-chain analytics |
> | [CoinMarketCap](https://manus.im/features/connectors) | MCP | Query cryptocurrency quotes, market metrics, sentiment, and news |
> | [Crypto.com](https://manus.im/features/connectors) | MCP | Access live cryptocurrency prices, trading data, and trending assets |
> | [Digits](https://manus.im/features/connectors) | MCP | Analyze transactions and generate financial statements and aging reports |
> | [Era Context](https://manus.im/features/connectors) | MCP | Review balances and transactions, analyze spending, and manage financial categories |
> | [eToro API](https://manus.im/features/connectors) | API key | Monitor portfolio performance, resolve instrument symbols, and retrieve watchlists |
> | [Etsy](https://manus.im/features/connectors) | MCP | Explore the API specification to build Etsy integrations |
> | [Financial Datasets](https://manus.im/features/connectors) | MCP | Retrieve market data, analyze financial statements, screen stocks, and track insider trades |
> | [Financial Modeling Prep](https://manus.im/features/connectors) | MCP | Access stock prices, financial statements, SEC filings, and market events |
> | [Fiscal](https://manus.im/features/connectors) | MCP | Retrieve and analyze company financials, filings, ownership, news, and market data |
> | [freee](https://manus.im/features/connectors) | MCP | Access and update accounting, invoicing, HR, and business data |
> | [GoCardless](https://manus.im/features/connectors) | MCP | Review payment operations and perform supported account actions |
> | [Interactive Brokers](https://manus.im/features/connectors) | MCP | Analyze account positions, cash, performance, risk, and market data |
> | [Kalshi API](https://manus.im/features/connectors) | API key | Browse prediction markets and order books, and retrieve portfolio details |
> | [Lovie](https://manus.im/features/connectors) | MCP | Manage accounting, transactions, cards, invoices, company documents, and formation |
> | [Mercury](https://manus.im/features/connectors) | MCP | Review bank accounts, view transactions, and manage banking workflows |
> | [Morningstar](https://manus.im/features/connectors) | MCP | Research securities, review investment ratings, and screen stocks, funds, and ETFs |
> | [Numeric](https://manus.im/features/connectors) | MCP | Manage close tasks, retrieve financial reports, and analyze ledger transactions and trends |
> | [PayPal for Business](https://manus.im/connectors/paypal) | MCP | Manage transactions, invoices, and business account operations |
> | [Pazy](https://manus.im/features/connectors) | MCP | Manage invoices, purchase orders, expenses, vendor payments, approvals, and tax data |
> | [Privacy.com](https://manus.im/features/connectors) | MCP | Issue virtual cards, set spending limits, and review transactions |
> | [Raisely](https://manus.im/features/connectors) | MCP | Review fundraising campaigns, donations, supporters, and performance |
> | [Ramp](https://manus.im/connectors/ramp) | MCP | Review balances, expenses, cards, reimbursements, and budgets |
> | [Razorpay](https://manus.im/features/connectors) | MCP | Create payment links, manage orders, process refunds, and track payouts |
> | [RevenueCat](https://manus.im/features/connectors) | MCP | Manage subscription projects, products, entitlements, offerings, and paywalls |
> | [Rillet](https://manus.im/features/connectors) | MCP | Query financial records and reports, and create or update accounting entries |
> | [Robinhood Trading](https://manus.im/features/connectors) | MCP | Review investment accounts, analyze market data, and place trades |
> | [Shopify](https://manus.im/features/connectors) | App | Manage products and orders, and analyze store performance |
> | [Square](https://manus.im/connectors/square) | MCP | Manage payments, orders, customers, inventory, invoices, and subscriptions |
> | [Stripe](https://manus.im/connectors/stripe) | MCP | Manage customers, billing, and payments, and access documentation |
> | [Stripe API](https://manus.im/connectors/stripe) | API key | Accept payments, manage subscriptions, automate billing, and review financial data |
> | [SubscriptionFlow](https://manus.im/features/connectors) | MCP | Manage subscriptions, invoices, payments, refunds, and revenue metrics |
> | [Toast API](https://manus.im/features/connectors) | API key | Retrieve restaurant menus, order and payment data, and employee labor records |
> | [Truthifi](https://manus.im/features/connectors) | MCP | Analyze investment account performance, asset composition, and risk |
> | [Unusual Whales](https://manus.im/features/connectors) | MCP | Query options flow, trades, holdings, earnings, screeners, and prediction markets |
> | [Vantage](https://manus.im/features/connectors) | MCP | Compare cloud costs, inspect budgets and anomalies, and review savings recommendations |
> | [Wave API](https://manus.im/features/connectors) | API key | Create invoices, manage customers and products, and query accounting data |
> | [Webull](https://manus.im/features/connectors) | MCP | View account balances, track market data, and manage watchlists |
> | [Whop](https://manus.im/features/connectors) | MCP | Manage products, memberships, payments, checkout settings, and analytics |
> | [Wix](https://manus.im/connectors/wix) | MCP | Search site documentation and manage contacts, orders, and products |
> | [Xero](https://manus.im/connectors/xero) | MCP | Query accounting records, invoices, payroll, and financial reports |

> [accordion] Search, research and web data (29)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [Anchor Browser](https://manus.im/features/connectors) | API key | Automate web tasks, extract page content, and manage cloud browser sessions |
> | [Apify](https://manus.im/connectors/apify) | MCP | Run web scrapers and crawlers to extract data from websites and online sources |
> | [Aurora](https://manus.im/features/connectors) | MCP | Search engagements and analyze documents to answer questions about legal matters |
> | [AWS Marketplace](https://manus.im/features/connectors) | MCP | Search product listings and compare marketplace solutions with cited research |
> | [Brandfetch](https://manus.im/features/connectors) | MCP | Find brand assets, company details, and merchant identities from transaction descriptions |
> | [Bright Data](https://manus.im/features/connectors) | MCP | Search and scrape webpages into clean text or structured data |
> | [Consensus](https://manus.im/features/connectors) | MCP | Find academic studies and extract key takeaways and citations |
> | [Dupe](https://manus.im/features/connectors) | MCP | Find affordable alternatives to furniture, fashion, and beauty products |
> | [Elicit](https://manus.im/features/connectors) | MCP | Search academic papers and generate literature reviews with summaries and citations |
> | [Exa](https://manus.im/features/connectors) | MCP | Search the web, retrieve webpage content, and filter results |
> | [Firecrawl](https://manus.im/connectors/firecrawl) | MCP | Search, crawl, and scrape websites to collect and extract information |
> | [GoDaddy](https://manus.im/features/connectors) | MCP | Find domain names and check their registration availability |
> | [Granted](https://manus.im/features/connectors) | MCP | Find grants, research funders, and analyze historical award data |
> | [Grok](https://manus.im/features/connectors) | API key | Retrieve current information and analyze complex questions |
> | [Hugging Face](https://manus.im/features/connectors) | MCP | Search AI models, datasets, research papers, and documentation |
> | [Microsoft Learn](https://manus.im/features/connectors) | MCP | Search official Microsoft documentation, retrieve articles, and find code snippets |
> | [My Browser](https://manus.im/features/connectors) | App | Browse websites through your local Chrome session, including sites requiring login |
> | [Neimo](https://manus.im/features/connectors) | MCP | Search regulatory knowledge bases and find updates or compliance workflows |
> | [Open Targets](https://manus.im/features/connectors) | MCP | Search genes, diseases, and drugs, and explore evidence for drug discovery |
> | [Parallel](https://manus.im/features/connectors) | MCP | Search the web and retrieve page content for research and fact-checking |
> | [Perplexity](https://manus.im/features/connectors) | API key | Search the web and get researched answers with citations |
> | [Raindrop](https://manus.im/features/connectors) | MCP | Search, save, and organize bookmarks, collections, tags, and highlights |
> | [Rally](https://manus.im/features/connectors) | MCP | Recruit participants, schedule interviews, review transcripts, and manage research studies |
> | [Rhizome AI](https://manus.im/features/connectors) | MCP | Research regulatory questions using health-authority sources and citations |
> | [Scite](https://manus.im/features/connectors) | MCP | Search scientific articles, evaluate citations, and check papers for corrections |
> | [Tango](https://manus.im/features/connectors) | MCP | Search and analyze federal contracts, grants, vendors, and procurement data |
> | [Tavily](https://manus.im/features/connectors) | MCP | Search the web and extract current information from URLs |
> | [Wolfram](https://manus.im/connectors/wolfram) | MCP | Evaluate code and retrieve computational results across scientific subjects |
> | [Yelp API](https://manus.im/features/connectors) | API key | Search local businesses and retrieve ratings, reviews, photos, and events |

> [accordion] HR and recruiting (8)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [Ashby](https://manus.im/connectors/ashby) | MCP | Search candidates, prepare interviews, and manage recruiting pipelines and applications |
> | [Deel](https://manus.im/features/connectors) | MCP | Manage workforce records, contracts, time off, onboarding, invoices, and payslips |
> | [Dice](https://manus.im/features/connectors) | MCP | Search technology jobs by location, workplace, employment type, and other filters |
> | [Gusto](https://manus.im/connectors/gusto) | MCP | Access payroll, employee, benefits, and time-off information |
> | [Metaview](https://manus.im/features/connectors) | MCP | Analyze interview records, compare candidates, build profiles, and review hiring funnels |
> | [Ribbon AI](https://manus.im/features/connectors) | MCP | Review candidates, applications, interviews, open roles, and offers |
> | [Shapes](https://manus.im/features/connectors) | MCP | Search employee records, review workforce data, and find workplace resources |
> | [Workable](https://manus.im/features/connectors) | MCP | Manage recruiting, applicants, offers, employee records, and performance reviews |

> [accordion] Customer support (7)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [Intercom](https://manus.im/connectors/intercom) | MCP | Search and manage customer conversations and contacts |
> | [Plain](https://manus.im/features/connectors) | MCP | Manage support threads, customer records, and help center articles |
> | [Pylon](https://manus.im/features/connectors) | MCP | Search and manage support issues, accounts, and contacts |
> | [Respond.io](https://manus.im/features/connectors) | MCP | Manage contacts, conversations, messages, workflows, and AI agents |
> | [Unthread](https://manus.im/features/connectors) | MCP | Explore support conversations and analytics, update conversations, and create approval requests |
> | [Unwrap](https://manus.im/features/connectors) | MCP | Analyze customer feedback, identify themes, and chart trends over time |
> | [Zendesk API](https://manus.im/features/connectors) | API key | Create, update, and resolve support tickets and manage help desk users |

> [accordion] Travel, lifestyle and other (26)
>
> | Connector | Type | What you can do |
> | :- | :- | :- |
> | [AllTrails](https://manus.im/features/connectors) | MCP | Find trails, review route details, and check trailhead weather |
> | [Alma Food](https://manus.im/features/connectors) | MCP | Review meals, track nutrition goals, and analyze weight history |
> | [Cal.com](https://manus.im/features/connectors) | MCP | Create and manage bookings, event types, availability, and routing forms |
> | [COROS](https://manus.im/features/connectors) | MCP | Review training, sleep, recovery, and other activity and health data |
> | [doola](https://manus.im/features/connectors) | MCP | Form Wyoming LLCs by submitting ownership details and completing checkout |
> | [Ferryhopper](https://manus.im/features/connectors) | MCP | Find ferry routes, schedules, prices, and booking links |
> | [Fever](https://manus.im/features/connectors) | MCP | Find events and venues by location, date, price, and other details |
> | [Fitbod](https://manus.im/features/connectors) | MCP | Generate workout plans based on fitness goals, equipment, and experience |
> | [Flightradar24](https://manus.im/features/connectors) | MCP | Track live and historical flights and look up aircraft, airline, and airport details |
> | [Google Maps](https://manus.im/connectors/google-maps) | MCP | Search places, check weather, compute routes, and find location IDs |
> | [Habitify](https://manus.im/features/connectors) | MCP | Manage habits, log progress, and track statistics and streaks |
> | [Instacart](https://manus.im/connectors/instacart) | MCP | Create recipe pages and grocery shopping lists |
> | [Jinko](https://manus.im/features/connectors) | MCP | Compare flights and hotels, plan trips, and create booking checkout links |
> | [Kiwi.com](https://manus.im/features/connectors) | MCP | Search flights, compare options, and generate booking links |
> | [KKday](https://manus.im/features/connectors) | MCP | Find tours, activities, transport, and travel packages and compare prices |
> | [Lambus](https://manus.im/features/connectors) | MCP | Plan trips, manage bookings, discover places, and split travel expenses |
> | [Learning Commons](https://manus.im/features/connectors) | MCP | Find academic standards, break them into learning components, and trace progressions |
> | [Mindbody API](https://manus.im/features/connectors) | API key | Manage class schedules, appointments, client records, and sales for wellness businesses |
> | [MyRealTrip](https://manus.im/features/connectors) | MCP | Find flights, hotels, tours, and activities with availability, pricing, and booking links |
> | [Navan](https://manus.im/features/connectors) | MCP | Analyze travel bookings, expenses, approval flows, policies, and card transactions |
> | [Oath](https://manus.im/features/connectors) | MCP | Find clinical calculators, inspect inputs, and calculate structured results with evidence |
> | [OpticOdds](https://manus.im/features/connectors) | MCP | Compare sportsbook odds, track results, find prices, and evaluate bets |
> | [Ticket Tailor](https://manus.im/features/connectors) | MCP | Manage event tickets, orders, memberships, check-ins, and sales reports |
> | [TomTom Maps](https://manus.im/features/connectors) | MCP | Geocode locations, search places, calculate routes, and check live traffic |
> | [Trivago](https://manus.im/features/connectors) | MCP | Search and compare accommodations by location, dates, guests, and amenities |
> | [Viator](https://manus.im/features/connectors) | MCP | Find experiences by destination and dates, compare details, and retrieve booking links |

## What you need to know

* **Availability can depend on your account.** Some connectors, and some [Google Workspace](https://manus.im/connectors/google-drive) services, may not appear for every account or plan.
* **Permissions come from your account.** A connector can only do what the connected account is allowed to do in that service.
* **Manus does not bypass permission controls.** Manus asks for your approval before it enables a recommended connector.
* **The MCP server defines the tools.** The maintainer of each MCP server decides which tools it offers. The tools can change when the maintainer updates the server.
* **API key connectors use your own credentials.** Usage can count against the quota or billing of your account with that service.
* **You can revoke access.** Disconnect a connector in Manus at any time. You can also remove access in the settings of the connected service.

## Tips

* **Enable only what the task needs.** Fewer enabled connectors make it easier for Manus to choose the right tool.
* **Name the app in your prompt.** "Find the Q4 plan in Google Drive" gives Manus a clearer target than "find the Q4 plan."
* **Combine connectors in one task.** For example, ask Manus to read notes in [Notion](https://manus.im/connectors/notion) and create events in [Google Calendar](https://manus.im/connectors/google-calendar).
* **Ask for a review step before changes.** Add "show me the changes before you apply them" when a task writes to an external app.
* **Set up connectors for a Project.** A Project can recommend connectors, so every task in the Project starts with the right tools. See [Projects](https://manus.im/docs/features/projects.md).

## FAQ

> [accordion] What is the difference between App, MCP, and API key connectors?
>
> App connectors are built-in integrations that Manus maintains. MCP connectors use an MCP server for that service. API key connectors call the service's API with a key that you supply. All three types work the same way in a task.

> [accordion] Why does a connector on this page not appear in my account?
>
> Some connectors depend on your account, plan, or region. If you cannot find a connector, search for it by name in **Connectors**. You can also add it yourself as a custom MCP server if the provider offers one.

> [accordion] Can Manus enable a connector without my approval?
>
> No. Manus can recommend a connector, but you must approve it. If the connector needs a sign-in, you must complete that step.

> [accordion] Can I connect a service that is not in the catalog?
>
> Yes. Open **Connectors**, select **Create**, and add an MCP server by URL, add a command-based Custom MCP, or save an API key as a Custom API. See [Custom MCP Servers](https://manus.im/docs/integrations/custom-mcp.md).

> [accordion] Can I use connectors with the Manus API?
>
> Yes. Connect the connector in the Manus web app first. Then pass its ID in the `connectors` array when you create a task. See the [Manus API connectors guide](https://open.manus.ai/docs/v2/connectors).

> [accordion] How often does this page update?
>
> A scheduled check compares this page with the Manus connector catalog. When connectors are added or removed, the page is updated.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.