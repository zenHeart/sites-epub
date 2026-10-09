> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub Integration

> Connect Zenflow to GitHub for repository management and pull requests.

<span className="set-page-badge-native" />

<Note>
  This native integration requires a Zencoder account.
</Note>

## Overview

Zenflow integrates with GitHub to streamline your development workflow. Connect your repositories, create pull requests directly from tasks, and sync status across platforms.

## Connecting to GitHub

There are two ways to connect to Github - OAuth flow and Personal Access Token flow

<Tabs>
  <Tab title="OAuth">
    <Steps>
      <Step title="Open Settings & Integrations">
        Navigate to **Settings → Integrations** in the Zenflow sidebar.
      </Step>

      <Step title="Find GitHub">
        Locate **GitHub** in the Integrations Catalog.
      </Step>

      <Step title="Click Connect">
        Click the **Connect** or **\[+]** button on the GitHub card, and select **Connect with OAuth**.

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/device-flow/connection-method-selection-df.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=5402b1ab7cba1bc13523d739584698af" alt="github method selection" width="1836" height="870" data-path="images/integrations/github/device-flow/connection-method-selection-df.png" />

        Click the link shown in the modal or [click here](https://github.com/login/device)
        Select the account you want to connect if you have multiple

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/device-flow/device-activation-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=143186b01b39f39952d0f9435154410d" alt="github method selection" width="1844" height="1164" data-path="images/integrations/github/device-flow/device-activation-screen.png" />

        Enter code shown in Zenflow and click **Continue**

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/device-flow/code-entered.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=4e22e5f30f9f6ec595dfa58d7a9e3f87" alt="github code entry" width="1848" height="1253" data-path="images/integrations/github/device-flow/code-entered.png" />

        Click **Authorize zencoderai**

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/device-flow/authorization-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=c38e617dcd8c3e4ba67c03a0fe0d72f0" alt="github scope screen" width="1820" height="1920" data-path="images/integrations/github/device-flow/authorization-screen.png" />

        You should see confirmation page

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/device-flow/all-set-github.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=d782c04f3ff38ead32fcb533ada95510" alt="github confirmation screen" width="1830" height="994" data-path="images/integrations/github/device-flow/all-set-github.png" />
      </Step>

      <Step title="Integration enabled">
        It can take a few seconds for the connection to get updated in Zenflow

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/device-flow/connected-integration-zenflow.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=543328ac24e6421e68d2a621824297d3" alt="github integration connected" width="1698" height="183" data-path="images/integrations/github/device-flow/connected-integration-zenflow.png" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Personal Access Token">
    <Steps>
      <Step title="Open Settings & Integrations">
        Navigate to **Settings → Integrations** in the Zenflow sidebar.
      </Step>

      <Step title="Find GitHub">
        Locate **GitHub** in the Integrations Catalog.
      </Step>

      <Step title="Click Connect">
        Click the **Connect** or **\[+]** button on the GitHub card, and select **Use Personal Access Token**.

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/pat-flow/connection-method-selection-pat.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=a984a3b178ec4cba6ce901c2c714d2e6" alt="github method selection" width="1868" height="873" data-path="images/integrations/github/pat-flow/connection-method-selection-pat.png" />

        Click the link shown in the modal or [click here](https://github.com/settings/tokens/new?description=Zenflow\&scopes=repo,user:email)
        After confirming your identity, you should land on **New Personal Access Token (Classic)** page

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/pat-flow/new-pat-page.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=68bab29a5e4296dcb4af4e157477f553" alt="github new token creation page" width="3392" height="1238" data-path="images/integrations/github/pat-flow/new-pat-page.png" />

        Set token expiration date to your desired expiration date

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/pat-flow/expiration-dropdown.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=8c79459960d362ed6b407dc3c6a8b6f6" alt="github expiration date" width="499" height="588" data-path="images/integrations/github/pat-flow/expiration-dropdown.png" />

        Make sure the scopes selected as shown on the screenshot - whole `repo` section  and `user:email` in `user` section

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/pat-flow/scopes.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=44a4741839ced649abd92ce231909188" alt="github token scopes" width="1572" height="2142" data-path="images/integrations/github/pat-flow/scopes.png" />

        Click **Generate token** at the bottom of the page. You'll be redirected to the page with all your token and shown the newly generated token

        <Warning>
          The token is only shown once. Store it securely before leaving the page.
        </Warning>

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/pat-flow/token-created.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=dc351c277a30ed75a7b8fa9e0273c84b" alt="github generated token" width="1594" height="457" data-path="images/integrations/github/pat-flow/token-created.png" />

        Paste token in Zenflow and click **Done**

        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/pat-flow/pasted-token.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=a7b750ed1525786ac607b9e7ac9915b5" alt="github token entry" width="1820" height="856" data-path="images/integrations/github/pat-flow/pasted-token.png" />
      </Step>

      <Step title="Integration enabled">
        <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/github/pat-flow/connected-integration-zenflow.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=29ad82caffe4deb913c8783f911cc4b7" alt="github integration connected" width="1698" height="183" data-path="images/integrations/github/pat-flow/connected-integration-zenflow.png" />
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Features

### Clone from GitHub

When creating a new project, you can clone directly from GitHub:

1. Click **New Project → Clone from GitHub**
2. Select the repository
3. Choose the local directory
4. Zenflow clones and sets up the project

### Create Pull Requests

When a task is complete:

1. Open the task's context menu (⋯)
2. Click **Create PR**
3. Review the PR title and description (pre-filled from task)
4. Select target branch
5. Create the pull request

Zenflow pushes the task branch and opens the PR on GitHub.

### PR Status Sync

Zenflow syncs PR status back to tasks:

| GitHub Status | Task Status |
| - | - |
| PR Open | Review |
| PR Merged | Completed |
| PR Closed | Archived (optional) |

### Automated Workflows

Trigger Zenflow tasks from GitHub events:

* **Issue created**: Auto-create a Fix Bug task
* **PR comment**: Re-run agents with new instructions
* **Review requested**: Notify in Zenflow inbox

## Authentication Options

### OAuth (Recommended)

Standard GitHub OAuth flow—sign in with your GitHub account and authorize Zenflow.

### Personal Access Token

For fine-grained control or organizations with OAuth restrictions:

1. Generate a token at **GitHub → Settings → Developer settings → Personal access tokens**
2. Required scopes: `repo`, `workflow`
3. Enter the token in **Project → Settings → GitHub**

### GitHub App (Enterprise)

Organizations can install the Zenflow GitHub App for centralized access control:

* Admin manages permissions
* No individual tokens needed
* Audit logging for compliance

## Repository Settings

Configure per-repository behavior:

| Setting | Description |
| - | - |
| **Default branch** | Base for new tasks (usually `main`) |
| **Branch prefix** | Naming pattern for task branches |
| **Auto-push** | Push branches automatically |
| **PR template** | Default description template |

## Troubleshooting

<AccordionGroup>
  <Accordion title="Can't see my repository" icon="eye-slash">
    Verify that your GitHub connection has access to the repository. For organization repos, an admin may need to grant access.
  </Accordion>

  <Accordion title="PR creation fails" icon="xmark">
    Check that:

    * The task branch has commits
    * You have write access to the repository
    * The target branch exists
    * There are no GitHub branch protection conflicts
  </Accordion>

  <Accordion title="Webhook not triggering" icon="bell-slash">
    Zenflow webhooks may be blocked by:

    * Firewall rules
    * GitHub organization settings
    * Network connectivity issues

    Check **Project → Settings → Integrations** for webhook status.
  </Accordion>
</AccordionGroup>

## Next Steps

<CardGroup cols={2}>
  <Card title="MCPs" icon="plug" href="/zenflow/mcps">
    Connect additional tools via MCP
  </Card>

  <Card title="Repository Configuration" icon="gear" href="/zenflow/project-configuration">
    Configure automation settings
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.