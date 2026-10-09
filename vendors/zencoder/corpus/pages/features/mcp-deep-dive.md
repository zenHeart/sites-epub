> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Configuration Guide

> Advanced guide to configuring, building, and troubleshooting Model Context Protocol servers in Zencoder

## What is MCP?

Model Context Protocol (MCP) is an open standard for connecting LLMs to external data sources and tools. Zencoder acts as an **MCP client** — it connects to **MCP servers** that expose specific capabilities like database queries, API calls, or browser automation.

For basic setup, see [Integrations & MCP](/features/integrations-and-mcp). This page covers advanced configuration, custom server development, and troubleshooting.

## Configuration Reference

MCP servers are configured differently depending on your IDE:

<Tabs>
  <Tab title="VS Code">
    Add servers to your VS Code settings under `zencoder.mcpServers`:

    ```jsonc theme={"system"}
    // .vscode/settings.json or User Settings
    "zencoder.mcpServers": {
      "server-name": {
        "command": "executable",
        "args": ["arg1", "arg2"],
        "env": {
          "API_KEY": "your-key"
        }
      }
    }
    ```
  </Tab>

  <Tab title="JetBrains">
    Configure in **Settings → Tools → Zencoder → MCP Servers**:

    ```jsonc theme={"system"}
    {
      "server-name": {
        "command": "executable",
        "args": ["arg1", "arg2"],
        "env": {
          "API_KEY": "your-key"
        }
      }
    }
    ```
  </Tab>
</Tabs>

### Configuration Properties

| Property | Required | Description |
| - | - | - |
| `command` | Yes (stdio) | The executable to run (e.g., `npx`, `uvx`, `docker`) |
| `args` | No | Array of command-line arguments |
| `env` | No | Environment variables passed to the server process |
| `url` | Yes (HTTP) | URL for remote HTTP-based MCP servers |

## Connection Protocols

Zencoder supports three MCP connection protocols:

### stdio (Local Servers)

The server runs as a subprocess on your machine. Communication happens over stdin/stdout.

```jsonc theme={"system"}
"zencoder.mcpServers": {
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/dir"]
  }
}
```

### Streamable HTTP (Remote Servers)

For servers running on a remote host, use HTTP-based connections:

```jsonc theme={"system"}
"zencoder.mcpServers": {
  "remote-db": {
    "url": "https://mcp.example.com/db"
  }
}
```

### OAuth2 (Authenticated Remote Servers)

For third-party services requiring OAuth2 authentication:

```jsonc theme={"system"}
"zencoder.mcpServers": {
  "github-mcp": {
    "url": "https://mcp.github.com",
    "auth": "oauth2"
  }
}
```

<Note>
  **Platform Support:**

  * **JetBrains**: Full support for stdio, HTTP, and OAuth2
  * **VS Code**: Supports stdio. HTTP and OAuth2 support is being rolled out — check the [changelog](/changelog/home) for status.
</Note>

## Popular MCP Servers

These servers are available in the built-in **MCP Library** (Agent Tools → MCP Library):

| Server | What it does | Install |
| - | - | - |
| **GitHub** | Repos, PRs, issues, code search | `npx @modelcontextprotocol/server-github` |
| **PostgreSQL** | Query databases, inspect schemas | `npx @modelcontextprotocol/server-postgres` |
| **Filesystem** | Read/write files outside workspace | `npx @modelcontextprotocol/server-filesystem` |
| **Slack** | Read channels, send messages | `npx @modelcontextprotocol/server-slack` |
| **Figma** | Extract design data for code generation | Via MCP Library |
| **Sentry** | Pull error details and stack traces | Via MCP Library |
| **Linear** | Issues, projects, and workflows | Via MCP Library |
| **Brave Search** | Web search for documentation and APIs | `npx @modelcontextprotocol/server-brave-search` |

<Tip>
  Browse 100+ servers in the MCP Library — open **Agent Tools** from the menu and click **MCP Library**.
</Tip>

## Building a Custom MCP Server

If no existing server fits your needs, you can build your own. MCP servers are lightweight programs that expose tools via the MCP protocol.

### Quick Start with Python

```python theme={"system"}
# server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-tool")

@mcp.tool()
def get_deployment_status(service: str) -> str:
    """Check the deployment status of a service."""
    # Your logic here — query your deployment API
    return f"{service} is running v2.3.1 (healthy)"

if __name__ == "__main__":
    mcp.run()
```

Register it in your MCP configuration:

```jsonc theme={"system"}
"zencoder.mcpServers": {
  "deployments": {
    "command": "python",
    "args": ["path/to/server.py"]
  }
}
```

### Quick Start with TypeScript

```typescript theme={"system"}
// server.ts
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "my-tool", version: "1.0.0" });

server.tool("get_deployment_status",
  { service: z.string() },
  async ({ service }) => ({
    content: [{ type: "text", text: `${service} is running v2.3.1 (healthy)` }]
  })
);

const transport = new StdioServerTransport();
await server.connect(transport);
```

### Resources

* [MCP Specification](https://spec.modelcontextprotocol.io) — Full protocol documentation
* [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Tool Permissions

Agents request permission before invoking MCP tools. You control this through the permission prompt:

* **Allow once** — permit the tool call for this interaction
* **Always allow** — trust this tool for all future calls (configurable in settings)
* **Deny** — block the tool call

<Note>
  You can configure trusted tools in Zencoder settings to skip the permission prompt for tools you use frequently.
</Note>

## Troubleshooting

<AccordionGroup>
  <Accordion title="MCP server not appearing in agent tools">
    * Verify the configuration syntax in your settings
    * Check that the `command` executable is available in your PATH
    * Restart the IDE after adding a new server
    * Look at the Zencoder output panel for error messages
  </Accordion>

  <Accordion title="Server starts but tools don't work">
    * Ensure the server implements the MCP protocol correctly
    * Check that required environment variables are set in the `env` block
    * For Docker-based servers, verify Docker is running
    * Test the server independently: `echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | your-command`
  </Accordion>

  <Accordion title="Authentication failures with OAuth2">
    * OAuth2 is fully supported on JetBrains; VS Code support is being rolled out
    * Clear cached tokens and re-authenticate
    * Verify the OAuth2 redirect URL is configured correctly in the service provider
  </Accordion>

  <Accordion title="Server crashes or times out">
    * Check server logs for unhandled exceptions
    * Ensure the server handles malformed input gracefully
    * For remote servers, verify network connectivity and firewall rules
    * Increase timeout values if your server processes large datasets
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Integrations & MCP" icon="plug" href="/features/integrations-and-mcp">
    Basic MCP setup and the built-in MCP Library
  </Card>

  <Card title="Coding Agent" icon="code" href="/features/coding-agent">
    The primary agent that invokes MCP tools
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.