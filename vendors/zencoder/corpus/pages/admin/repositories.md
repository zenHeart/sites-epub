> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Repositories

> Add repositories for code indexing and autonomous agent runs.

The Repositories page lets you add and manage repositories that Zencoder indexes for code search and uses for autonomous agent runs.

<img src="https://mintcdn.com/forgoodaiinc/Y_SEC3iavYl5Qnon/images/admin/admin-repositories.jpg?fit=max&auto=format&n=Y_SEC3iavYl5Qnon&q=85&s=994da4c21bea941287b7f74737bdf771" alt="Repositories page showing the two-step setup: connect VCS and add repositories" style={{ borderRadius: '12px', marginTop: '8px', marginBottom: '16px' }} width="1260" height="720" data-path="images/admin/admin-repositories.jpg" />

## Adding Repositories

<Steps>
  <Step title="Set up a connection">
    If you haven't already, [add a connection](/admin/connections) to your version control system.
  </Step>

  <Step title="Add repositories">
    Click the **Add** button in the top-right corner. Select the repositories you want to index from your connected VCS provider.
  </Step>
</Steps>

Selected repositories are indexed for code search and made available for autonomous agent runs across your organization.

## What Indexing Enables

| Capability | Description |
| - | - |
| **Code search** | Agents can search across your codebase for patterns, references, and context |
| **Autonomous runs** | Agents can clone, branch, and work on tasks within indexed repositories |
| **Context awareness** | Agents understand your project structure, dependencies, and conventions |

<Note>
  Repository indexing is required before agents can work autonomously. IDE Agent features (inline chat, autocomplete) work without indexing — they use the locally open project.
</Note>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.