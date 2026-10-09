> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connections

> Connect your version control system to enable repository access and autonomous agent runs.

Connections link Zencoder to your version control system. You need at least one connection to add repositories and allow agents to run autonomously.

<img src="https://mintcdn.com/forgoodaiinc/Y_SEC3iavYl5Qnon/images/admin/admin-connections.jpg?fit=max&auto=format&n=Y_SEC3iavYl5Qnon&q=85&s=104136b1496d9e4f2cfdf3fd976c2aba" alt="Connections page showing the setup flow with Add connection button" style={{ borderRadius: '12px', marginTop: '8px', marginBottom: '16px' }} width="1260" height="720" data-path="images/admin/admin-connections.jpg" />

## Setting Up a Connection

<Steps>
  <Step title="Click Add connection">
    On the Connections page, click the **Add connection** button.
  </Step>

  <Step title="Select your provider">
    Choose your version control system (GitHub, GitLab, or Bitbucket).
  </Step>

  <Step title="Authorize access">
    Follow the OAuth flow to grant Zencoder access to your repositories. You can scope access to specific organizations or repositories.
  </Step>
</Steps>

<Note>
  Connections are organization-scoped. Once a connection is set up, all team members in your Zencoder organization can access the linked repositories.
</Note>

## After Connecting

Once connected, head to [Repositories](/admin/repositories) to select which repositories to add for indexing and agent runs.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.