> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Agents

> Use prebuilt or create custom AI agents (we also call them Zen Agents) that can be called for selected code or entire files directly in your IDE

## Understanding AI Agents

AI Agents are customizable, sharable agents that can be invoked on selected code or entire files in your IDE. Use prebuilt agents or create your own with specific instructions, tools, and commands.

<Tip>
  **Agents vs Skills**: AI Agents are interactive — you select them explicitly and chat with them. [Skills](/features/skills) are passive instruction packages that the agent loads automatically based on task context. Use agents for recurring interactive tasks; use skills for domain knowledge and procedural workflows.
</Tip>

## Navigating Agent Categories

At the top of the AI Agents screen, you'll find tabs that help you filter and navigate between different types of agents:

<CardGroup cols={3}>
  <Card title="All" icon="list">
    Shows all available agents
  </Card>

  <Card title="Zencoder" icon="robot">
    Displays prebuilt agents created by Zencoder (with the number indicating how many are available)
  </Card>

  <Card title="Custom" icon="user-gear">
    Shows your custom agents (with the number indicating how many you've created)
  </Card>
</CardGroup>

<img src="https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/ai-agents-selection.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=98a2b8e1c225759b4e1962de54072930" alt="AI Agents Selection" width="1288" height="146" data-path="images/ai-agents-selection.png" />

This categorization makes it easy to distinguish between default agents and your own custom creations.

## Creating an Agent

<Tabs>
  <Tab title="From scratch">
    <Steps>
      <Step title="Adding a New Agent">
        1. Click the three dots menu (⋮) at the top right corner.
        2. Select **Agents**
        3. Click the **Add custom agent** button in the top right
                   <img src="https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/ai-agents-make-custom-agent.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=2902095c56dc01dc81c3dd28d9b73556" alt="Create a Custom Agent" width="1294" height="476" data-path="images/ai-agents-make-custom-agent.png" />
      </Step>

      <Step title="Configuring an Agent">
        When adding or editing an agent, you'll need to set these properties:

        **Basic Settings:**

        * **Name**: A descriptive name for your agent (required)
        * **Share**: Control who can see and use this agent
          * Personal: Visible only to you
          * Shared: Visible to your entire organization (all users within your organization can share agents with others)

        **Configuration:**

        * **Command/Alias**: The chat command to invoke your agent (required)
        * **Instructions**: Detailed prompt instructions that define your agent's behavior (required)
        * **Tools**: Enable specific tools your agent can access
                  <img src="https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/ai-agents-config.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=e7a163f88eae7aa5d8bc76f1e54b364b" alt="Configuring an Agent" width="884" height="1686" data-path="images/ai-agents-config.png" />
      </Step>

      <Step title="Instructions Format">
        Define clear instructions for your agent that explain its purpose and how it should operate. Here's an example of instructions for a Repository Analyzer agent:

        ```
        Consider the currently open project and repository. 
        Understand its structure, mutual relations between files, folders, dependencies, and more. 
        Please provide me with an in-depth structured understanding of this repo
        ```

        Your instructions should be specific enough to guide the agent's behavior, but also flexible enough to work across different contexts.
      </Step>

      <Step title="Tool Selection">
        Agents can access various tools to enhance their capabilities:

        * git
        * File Search
        * Full Text Search
        * Web Search
        * Fetch Webpage Content
        * Semantic Code Search
        * File Editor
        * Execute Shell Command
        * Gather Requirements
        * ...

        Simply click on the tools your agent should have access to in the **Tools** section.

        <img src="https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/ai-agents-tools.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=fe68f09f513342d4ee58bb03e2e60849" alt="Configuring Agent tools" width="1038" height="1190" data-path="images/ai-agents-tools.png" />
      </Step>

      <Step title="Sharing Agents">
        If you're an admin, you can share agents with your organization:

        1. When editing an agent, find the **Share** dropdown
        2. Choose between:
           * **Personal**: Visible only to you
           * **Shared**: Visible to the whole organization
                     <img src="https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/ai-agents-share.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=8663f5a53c14f14b930275953b5d43a8" alt="Sharing Agent" width="1054" height="516" data-path="images/ai-agents-share.png" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="From Marketplace">
    The [Agents Marketplace](https://zencoder.ai/marketplace) contains prebuilt agents for various development tasks (bug prevention, documentation generation, code review, etc.).

    <Steps>
      <Step title="Browse Agents">
        Visit our <a href="https://zencoder.ai/marketplace" target="_blank">Agents Marketplace</a> to explore available agents. Browse through the list and select the one that best suits your development needs.
      </Step>

      <Step title="View Agent Details">
        Click on the agent to view its details, including:

        * Name
        * Description
        * Instructions
        * Tools required
      </Step>

      <Step title="Create a Custom Agent">
        1. Open the Zencoder extension in your IDE.
        2. Click the three dots menu (⋮) at the top right corner.
        3. Select **Agents** to open the custom agent creation page.
        4. Click **Add Custom Agent**.
      </Step>

      <Step title="Configure the Agent">
        * **Name**: Give your agent a unique name.
        * **Instructions**: Copy the instructions from the agent's detail page on the Marketplace and paste them into the "Instructions" field.
        * **Tools**:
          * Open the **Tools** section in the extension.
          * Navigate to **Manage Tools**.
          * Search for the tools listed in the agent's details and install them if needed.

        <Note>
          Tool configuration is case-by-case. Follow the guidance provided in the agent's description. There are no standardized patterns yet.
        </Note>
      </Step>

      <Step title="Finalize and Test">
        * After configuring the agent with the name, command, instructions, and tools, save it.
        * You can now use this custom agent directly in your IDE for coding assistance.
      </Step>
    </Steps>
  </Tab>
</Tabs>

### Contributing Your Own Agents

You can submit custom agents to the marketplace via the [zenagents-library GitHub repo](https://github.com/zencoderai/zenagents-library).

## Using Agents in Your Workflow

Once configured, you can use agents by:

1. Selecting code in your editor or focusing on an entire file
2. Invoking the agent using its command (e.g., `/unittests`, `/review`)
3. The agent will perform its specialized task on the selected code

## Example Use Cases

<AccordionGroup>
  <Accordion title="Security Review Agent">
    Create an agent with instructions to scan for OWASP Top 10 vulnerabilities, check for hardcoded secrets, and verify authentication/authorization patterns. Give it access to **File Editor**, **Codebase Search**, and **Shell Commands** (to run static analysis tools).
  </Accordion>

  <Accordion title="Release Notes Generator">
    Build an agent that reads recent git commits and generates changelog entries. Give it **Git Operations** and **Web Search** (to link to related issues). Set the command to `/release-notes`.
  </Accordion>

  <Accordion title="API Documentation Agent">
    Create an agent with instructions to generate OpenAPI specs from your route files. Scope it with **Codebase Search** and **File Editor** to read route definitions and write `.yaml` docs.
  </Accordion>

  <Accordion title="Onboarding Assistant">
    Share an agent across your org that new team members can invoke to get explanations of project architecture, key modules, and development workflows. Give it read-only tools (**Codebase Search**, **File Search**) and reference your repo's README and architecture docs in its instructions.
  </Accordion>
</AccordionGroup>

## Tips for Custom Agents

<AccordionGroup>
  <Accordion title="Keep instructions focused">
    An agent should do one thing well. A "Security Scanner" is better than a "Security Scanner + Performance Optimizer + Docs Generator."
  </Accordion>

  <Accordion title="Limit tool access">
    Only enable the tools your agent actually needs. A read-only analysis agent shouldn't have **File Editor** or **Shell Commands**.
  </Accordion>

  <Accordion title="Use the command wisely">
    Pick short, memorable commands like `/review`, `/docs`, or `/migrate`. These become muscle memory.
  </Accordion>

  <Accordion title="Share across your team">
    Set agents to **Shared** visibility so your entire org benefits. This is especially powerful for standardized workflows like PR reviews or release processes.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Coding Agent" icon="code" href="/features/coding-agent">
    The primary development agent that your custom agents can complement
  </Card>

  <Card title="Skills" icon="wand-magic-sparkles" href="/features/skills">
    Reusable instruction packages that agents load automatically based on task context
  </Card>

  <Card title="Integrations & MCP" icon="plug" href="/features/integrations-and-mcp">
    Connect external tools via Model Context Protocol
  </Card>

  <Card title="Supported Models" icon="microchip" href="/features/models">
    Choose from 10+ models or bring your own API key
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.