> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Admin Dashboard

> Manage your Zencoder organization — agents, connections, repositories, quotas, billing, users, SSO, and API keys.

The Admin Dashboard is the central hub for managing your Zencoder organization. Access it at [auth.zencoder.ai](https://auth.zencoder.ai).

<img src="https://mintcdn.com/forgoodaiinc/Y_SEC3iavYl5Qnon/images/admin/admin-quota-management.jpg?fit=max&auto=format&n=Y_SEC3iavYl5Qnon&q=85&s=446a2f8b15537e398cacd4755dc88396" alt="Zencoder Admin Dashboard showing the sidebar with Personal, Organization, and Administration sections" style={{ borderRadius: '12px', marginTop: '8px', marginBottom: '16px' }} width="1260" height="720" data-path="images/admin/admin-quota-management.jpg" />

## Dashboard Structure

The sidebar is organized into three sections:

### Personal

Settings that apply to your individual account.

<CardGroup cols={2}>
  <Card title="Agents" icon="robot" href="/admin/agents">
    Create and manage AI agents that automate coding tasks across your repositories.
  </Card>

  <Card title="Privacy & Security" icon="shield-halved" href="/admin/privacy-security">
    Active sessions, device management, and multi-factor authentication.
  </Card>
</CardGroup>

### Organization

Settings shared across your team.

<CardGroup cols={2}>
  <Card title="Connections" icon="link" href="/admin/connections">
    Connect your version control system (GitHub, GitLab, Bitbucket) to enable repository access.
  </Card>

  <Card title="Repositories" icon="code-branch" href="/admin/repositories">
    Add repositories for indexing and autonomous agent runs.
  </Card>
</CardGroup>

### Administration

Organization-wide management for admins.

<CardGroup cols={2}>
  <Card title="Quota Management" icon="gauge" href="/admin/quota-management">
    Monitor credit usage, set per-user quota caps, and manage your billing period.
  </Card>

  <Card title="Billing" icon="credit-card" href="/admin/billing">
    View your current plan, payment method, and team seat allocation.
  </Card>

  <Card title="User Management" icon="users" href="/admin/user-management">
    Invite team members, assign roles (Member, Admin, Manager), and manage access.
  </Card>

  <Card title="SSO" icon="key" href="/admin/sso">
    Configure Single Sign-On for your organization.
  </Card>

  <Card title="API Keys" icon="code" href="/admin/api-keys">
    Create and manage API keys for programmatic access to Zencoder.
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.