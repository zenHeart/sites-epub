> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# SSO

> Configure Single Sign-On for your Zencoder organization.

Single Sign-On (SSO) allows your team to authenticate through your organization's identity provider instead of individual Zencoder credentials.

<img src="https://mintcdn.com/forgoodaiinc/Y_SEC3iavYl5Qnon/images/admin/admin-sso.jpg?fit=max&auto=format&n=Y_SEC3iavYl5Qnon&q=85&s=82da7eb9b25a6df8778ffe6e9b7d9cab" alt="SSO Connection page showing the Set up SSO button" style={{ borderRadius: '12px', marginTop: '8px', marginBottom: '16px' }} width="1260" height="720" data-path="images/admin/admin-sso.jpg" />

## Setting Up SSO

Click **Set up SSO** to configure your identity provider. The setup wizard walks you through connecting your IdP (e.g., Okta, Azure AD, Google Workspace) with Zencoder.

## Benefits

| Benefit | Description |
| - | - |
| **Centralized authentication** | Users sign in through your existing IdP — no separate Zencoder passwords |
| **Automatic provisioning** | New team members get access when added to the appropriate IdP group |
| **Security compliance** | Enforce your organization's authentication policies (MFA, session length, IP restrictions) |
| **Simplified offboarding** | Removing a user from your IdP automatically revokes Zencoder access |

<Note>
  SSO is available on Team and Enterprise plans. Contact support if you need help with your IdP configuration.
</Note>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.