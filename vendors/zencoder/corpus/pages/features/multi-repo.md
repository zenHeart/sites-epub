> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-Repository Search

> Index and search across multiple repositories to enable AI agents to understand and work with complex multi-repo architectures

## What is Multi-Repository Search?

If you work with multiple repositories, Multi-Repository Search allows you to add and index repositories through the web admin panel, enabling Zencoder agents to search across those indexed repositories when needed.

<Tip>
  Multi-Repository Search is available for users on Pro Plus and Pro Max plans. Repository and Connections management requires Owner or Manager role permissions.
</Tip>

## Getting Started

Setting up multi-repository search involves a few steps that will give your AI agents access to your organization's codebase.

### Prerequisites

Before setting up multi-repository search, ensure you have:

* **Active subscription** on Pro Plus or Pro Max plan
* **Owner or Manager role** in your organization

### Setup Process

#### 1. Access Web Admin Panel

Navigate to [auth.zencoder.ai](https://auth.zencoder.ai) and log in to your account. Users with Owner or Manager roles will see additional options for Connections and Repositories management.

<img src="https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/multi-repo-admin-panel.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=1af6bde7cbed25a72a611b9026f378e2" alt="Web admin panel showing connections and repositories options" width="652" height="1078" data-path="images/multi-repo-admin-panel.png" />

#### 2. Add a connection to your VCS provider

Create a connection to your version control system:

1. Click on `Connections` in the admin panel
2. Select `Add`
3. Choose your VCS provider: GitHub, Bitbucket, or GitLab
4. Add your access token. Note that for multi-repo search, the token scope requires at least repo read permissions.

<img src="https://mintcdn.com/forgoodaiinc/pRqEaM47Xe_-nh77/images/multi-repo-add-connection.png?fit=max&auto=format&n=pRqEaM47Xe_-nh77&q=85&s=a2972e36e1e315594fd353b1bfaa4f83" alt="Adding a new VCS connection in the admin panel" width="1552" height="832" data-path="images/multi-repo-add-connection.png" />

<Note>
  **VCS Support**: GitHub, Bitbucket, and GitLab are all fully supported for multi-repository indexing.
</Note>

#### 3. Add Repositories

Once your connection is established, add repositories to your multi-repo index:

1. Navigate to `Repositories` in the admin panel
2. Click `Add`
3. Select a connection and then a repo name from your connected VCS provider
4. **Important**: Enable the "Indexing" flag for each repository (`Automatically reindex repository` checkbox) to allow AI agents to search its contents

<img src="https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/multi-repo-add-repository.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=6eb4a4e2e38ec2c3a63ba603258f3d19" alt="Adding repositories with indexing enabled" width="3448" height="1284" data-path="images/multi-repo-add-repository.png" />

<Warning>
  **Indexing Flag Required**: Only repositories with the indexing flag enabled will be searchable by AI agents.

  Index updates at least once a day. If there were no changes in repo, it will not be re-indexed.
</Warning>

#### 4. Configure Access Permissions

Control which users can access each repository through the multi-repo search tool:

* **Default setting** allows all users within your organization to access the repository
* **Custom access** lets you restrict access to specific users by their email addresses as needed

<img src="https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/multi-repo-permissions.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=eddfdd76c23f889df98bae06e5c9daf5" alt="Configuring repository access permissions" width="1622" height="476" data-path="images/multi-repo-permissions.png" />

## Using Multi-Repository Search

### Automatic Agent Detection

Since Multi-Repository Search is implemented as an agent tool, by default it is available for the [coding agent](/features/coding-agent) and [custom agents](/features/ai-agents).

Once configured, multi-repository search tool works with your existing workflow:

* **No special commands** are needed as AI agents automatically detect when you reference other repositories
* **Zencoder context understanding** allows agents to use repository names, service names, or project references to trigger searches

### Example Interactions

```
User: "How is authentication handled in the user-service repository? 

Use the multi-repo search tool to find relevant code."

Agent: [Automatically searches user-service repository for 
authentication patterns]
Based on the user-service repository, authentication is 
handled using JWT tokens with...
```

```
User: "Use the multi-repo search tool to find and then implement 
the same error handling pattern used in the payment-api".

Agent: [Searches payment-api repository for error handling patterns]
I found the error handling pattern in payment-api. 
Here's how to implement it in your current project...
```

## Best Practices

To get the most out of Multi-Repository Search, follow these guidelines for optimal results:

### Be Specific with Repository References and Tool Usage

For optimal search behavior, avoid making vague requests as agents might use the search tool excessively.

Instead, be specific when referencing repositories or services. Use exact repository names like "user-service" rather than generic terms like "the user thing" or "that authentication repo."

Also, since the Multi-repo search is a tool, you can be explicit in asking the agent to use it. This helps agents target their searches more effectively and return more relevant results.

### Consider Repository Size and Scope

Very large repositories may take longer to index initially, so consider the scope of your searches to get the most relevant results. When working with extensive codebases, provide additional context about which parts of the repository are most relevant to your current task.

### Provide Clear Context

The more context you provide about what you're looking for across repositories, the better the search results will be. Instead of asking "How does authentication work?", try "How is JWT token validation implemented in the auth-service repository? Use repo search tool."
This specificity helps agents understand exactly what information to retrieve.

## Related Features

Multi-Repository Search works with other Zencoder capabilities:

<CardGroup cols={2}>
  <Card title="Coding Agent" icon="code" href="/features/coding-agent">
    Leverages multi-repo context for code generation across your entire codebase
  </Card>

  <Card title="AI Agents" icon="microchip-ai" href="/features/ai-agents">
    Build specialized agents that work with specific repository combinations or workflows
  </Card>
</CardGroup>

<Info>
  Need help with setup or have questions about multi-repository search? Reach out to our [community support](/get-started/community-support) for assistance.
</Info>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.