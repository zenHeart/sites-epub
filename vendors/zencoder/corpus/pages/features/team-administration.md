> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Team Administration

> Manage your organization — seats, SSO, audit logs, credit controls, and repository access

## Admin Panel

Organization settings are managed through the web admin panel at [auth.zencoder.ai](https://auth.zencoder.ai). Owners and Managers can access all administration features.

## Roles & Permissions

| Role | Users & Seats | Billing | Repositories | Analytics | Settings |
| - | :-: | :-: | :-: | :-: | :-: |
| **Owner** | ✔ | ✔ | ✔ | ✔ | ✔ |
| **Manager** | ✔ | ✘ | ✔ | ✔ | ✔ |
| **Member** | ✘ | ✘ | ✘ | ✘ | Personal only |

## Seat Management

### Adding Users

1. Go to [auth.zencoder.ai](https://auth.zencoder.ai)
2. Navigate to **Members** in the sidebar
3. Click **Invite** and enter the user's email address
4. The user receives an invitation to join your organization

### Removing Users

1. Go to **Members**
2. Find the user and click **Remove**
3. The seat is freed immediately and can be reassigned

<Tip>
  Monitor seat utilization through the [Analytics Dashboard](/features/analytics) — identify inactive seats and reallocate them to active team members.
</Tip>

## Credit Controls

Zencoder uses a [usage-based credit model](/faq/pricing). Admins have controls to manage how credits are consumed across the team:

### Per-User Credit Caps

Set a maximum percentage of the org credit pool that any single user can consume:

* **Default**: Credits split equally across seats
* **Custom**: Per-user overrides for power users or restricted accounts
* A user hitting their cap is blocked until the admin re-allocates or buys a top-up

### Re-Allocation

Admins can rebalance credit caps mid-cycle. Re-allocation shifts the cap — it doesn't create or destroy credits.

### Top-Ups

When the org runs out of credits:

1. Go to your billing settings at [auth.zencoder.ai](https://auth.zencoder.ai)
2. Purchase a top-up (minimum \$20)
3. Top-up credits go into the shared pool and follow per-user cap rules

<Note>
  Top-up credits are non-refundable. Plan credits expire at the end of each monthly billing period — no rollover.
</Note>

## SSO (Single Sign-On)

Available on **Pro Plus, Pro Max, and Enterprise** plans.

### Supported Protocols

* **SAML 2.0**
* **OIDC (OpenID Connect)**

### Configuration

1. Go to [auth.zencoder.ai](https://auth.zencoder.ai)
2. Navigate to **Settings → SSO**
3. Select your identity provider (Okta, Azure AD, Google Workspace, etc.)
4. Enter the required metadata (Entity ID, SSO URL, certificate)
5. Test the connection before enforcing SSO-only login

### Enforcement

Once configured, you can enforce SSO-only login — users must authenticate through your identity provider. Direct email/password login is blocked for enforced organizations.

## Audit Logs

Available on **Pro Plus, Pro Max, and Enterprise** plans.

Track actions across your organization:

| Event Type | Examples |
| - | - |
| **Authentication** | Login, logout, SSO events |
| **User management** | Invitations, role changes, removals |
| **Configuration** | Settings changes, MCP server updates |
| **Usage** | Agent interactions, model usage, credit consumption |

### Accessing Logs

1. Go to [auth.zencoder.ai](https://auth.zencoder.ai)
2. Navigate to **Settings → Audit Logs**
3. Filter by date range, user, or event type
4. Export as CSV for compliance reviews

## Repository Management

For teams using [Multi-Repository Search](/features/multi-repo):

### Connections

Connect to your version control system:

1. Go to **Connections** in the admin panel
2. Click **Add** and select GitHub, Bitbucket, or GitLab
3. Provide an access token with repo read permissions

### Repository Indexing

1. Go to **Repositories** in the admin panel
2. Click **Add** and select repositories from your connected VCS
3. Enable the **Indexing** flag for each repository you want agents to search
4. Configure access permissions — all users by default, or restrict to specific emails

<Warning>
  Only repositories with the indexing flag enabled are searchable by agents. Indexes update at least once daily.
</Warning>

## Analytics Dashboard

Available on **Pro Plus** and above. The [Analytics Dashboard](/features/analytics) provides:

* **Daily active users** — track adoption trends
* **Member activity** — per-user usage with last-active timestamps
* **IDE breakdown** — VS Code vs JetBrains usage
* **Language analytics** — which programming languages your team uses with Zencoder
* **CSV export** — download data for BI tools and compliance

Access it at [auth.zencoder.ai/analytics](https://auth.zencoder.ai/analytics).

## Plan Comparison for Teams

| Feature | Pro | Pro Plus | Pro Max | Enterprise |
| - | :-: | :-: | :-: | :-: |
| Shared credit pool | ✘ | ✔ | ✔ | ✔ |
| Per-user credit caps | ✘ | ✔ | ✔ | ✔ |
| Multi-repo indexing | ✘ | ✔ | ✔ | Unlimited |
| Analytics dashboard | ✘ | ✔ | ✔ | ✔ |
| SSO & audit logs | ✘ | ✔ | ✔ | ✔ |
| Priority support | ✘ | ✘ | ✔ | ✔ |
| Private deployment | ✘ | ✘ | ✘ | ✔ |
| Dedicated CSM | ✘ | ✘ | ✘ | ✔ |

## Related

<CardGroup cols={2}>
  <Card title="Pricing & Plans" icon="credit-card" href="/faq/pricing">
    Credit model, top-ups, and plan details
  </Card>

  <Card title="Analytics" icon="chart-line" href="/features/analytics">
    Usage tracking and team insights
  </Card>

  <Card title="Multi-Repository Search" icon="magnifying-glass" href="/features/multi-repo">
    Set up cross-repository indexing
  </Card>

  <Card title="Security & Privacy" icon="shield-halved" href="/features/security">
    Data handling, compliance, and enterprise controls
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.