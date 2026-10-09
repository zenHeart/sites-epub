> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Universal AI Platform

> Unifying the world's most popular AI coding CLIs with Zencoder directly in your IDE

# Universal AI Platform

Use your existing AI subscriptions (Claude, ChatGPT, Gemini) inside Zencoder's IDE interface. Switch between CLI runtimes without leaving your editor.

<Note>
  Available on all plans. See [pricing](https://zencoder.ai/pricing) for details.

  *Please note that frontier model providers govern pricing, access, and usage policies for their respective CLI tools which may change at any time.*
</Note>

## What It Does

Zencoder acts as a host for external AI coding CLIs, giving them IDE integration, multi-repo context, custom agents, and skills. You pick the runtime; Zencoder provides the surrounding infrastructure.

## Supported CLI Tools

Currently, Zencoder supports:

* **Zen CLI** - Zencoder's native runtime
* **Claude Code** from Anthropic - Terminal-based agentic coding tool powered by Claude's latest models
* **OpenAI Codex** - Command-line interface using OpenAI's Codex models

## Setup Instructions

<Info>
  **Feature Availability**: The Universal AI Platform is now available across all Zencoder supported IDEs. Available in VS Code with Zencoder extension version 2.38+ and JetBrains IDEs with version 2.16+. Please ensure you're running the latest version of Zencoder to access these features.
</Info>

Install Zencoder, install your preferred CLI tool, and select the runtime in Zencoder settings.

### Connect Your CLI Tool

<Tabs>
  <Tab title="Claude Code">
    Claude Code is Anthropic's terminal-based coding CLI. It uses Claude's latest models to edit files, run tests, and manage Git operations via natural language.

    <Tip>
      **Pricing:** Claude Code is included with several Anthropic plans. See [anthropic.com/claude-code](https://www.anthropic.com/claude-code) for details.
    </Tip>

    **Prerequisites:**

    * Node.js 18 or newer
    * Claude subscription with Code access

    <Steps>
      <Step title="Install Claude Code by Anthropic">
        Visit [Claude Code by Anthropic](https://www.anthropic.com/claude-code) to learn more and choose a plan that includes Claude Code access.
      </Step>

      <Step title="Install Claude Code CLI">
        Install the Claude Code command-line interface using npm:

        ```bash theme={"system"}
        npm install -g @anthropic-ai/claude-code
        ```
      </Step>

      <Step title="Authenticate Claude Code">
        Authenticate Claude Code by running the following command. You'll be prompted to log in with your Claude account:

        ```bash theme={"system"}
        claude
        ```
      </Step>

      <Step title="Select Claude Code as Your Runtime">
        Once authenticated locally, return to Zencoder and select Claude Code as your runtime. In the chat box, click on the settings icon. Under the `Agent CLI` category, click on it and select `Claude Code` from the list of available CLIs (Zen CLI, Claude Code, or OpenAI Codex).

        <img src="https://mintcdn.com/forgoodaiinc/NMq1QhlpSl14Gauf/images/cli-selector-cc.png?fit=max&auto=format&n=NMq1QhlpSl14Gauf&q=85&s=a6f5b380f890e922057e6d1a9fffec64" alt="Selecting Claude Code as runtime in Zencoder settings" width="1214" height="750" data-path="images/cli-selector-cc.png" />

        <Note>
          If you haven't authenticated before, you'll see the following screens:

          You'll be prompted to open terminal to login

          <img src="https://mintcdn.com/forgoodaiinc/8v1FWTiXZjxP2hz5/images/zen-cli-cc-login.png?fit=max&auto=format&n=8v1FWTiXZjxP2hz5&q=85&s=20f4ca5954eacd5caccf6434f434b343" alt="Open terminal to login prompt" width="992" height="1024" data-path="images/zen-cli-cc-login.png" />

          Select and authenticate with your Claude account that has an active subscription

          <img src="https://mintcdn.com/forgoodaiinc/8v1FWTiXZjxP2hz5/images/zen-cli-cc-login-method.png?fit=max&auto=format&n=8v1FWTiXZjxP2hz5&q=85&s=a5953cab138b10861d3497424a8c8be3" alt="Select authentication method with Claude account" width="1838" height="529" data-path="images/zen-cli-cc-login-method.png" />

          Follow the authorization instructions shown in the screens

          <img src="https://mintcdn.com/forgoodaiinc/8v1FWTiXZjxP2hz5/images/zen-cli-cc-login-authorize.png?fit=max&auto=format&n=8v1FWTiXZjxP2hz5&q=85&s=11ad5e7d0e153ae3c8e7282e6f9596d9" alt="Authorization screen" width="1200" height="1285" data-path="images/zen-cli-cc-login-authorize.png" />

          Once everything is done, you'll see "Login successful, press Enter to continue"

          <img src="https://mintcdn.com/forgoodaiinc/8v1FWTiXZjxP2hz5/images/zen-cli-cc-login-success.png?fit=max&auto=format&n=8v1FWTiXZjxP2hz5&q=85&s=7835582bad348465bbd799c9e63d3462" alt="Login successful message" width="907" height="98" data-path="images/zen-cli-cc-login-success.png" />

          Finally, you'll see the welcome screen confirming Claude Code is ready

          <img src="https://mintcdn.com/forgoodaiinc/8v1FWTiXZjxP2hz5/images/zen-cli-cc-ready-to-work.png?fit=max&auto=format&n=8v1FWTiXZjxP2hz5&q=85&s=bb4a59adddaedf257d0061f3ef84ecb8" alt="Welcome to Claude Code screen" width="1502" height="738" data-path="images/zen-cli-cc-ready-to-work.png" />
        </Note>
      </Step>
    </Steps>

    **Using Claude Code with Zencoder**

    Once setup is complete, you can use Claude Code just like any other Zencoder runtime. You can select the [coding agent](/features/coding-agent), or use [custom agents](/features/ai-agents) from the [model selector](/features/models).

    <Tip>
      **Example:** Using the Review Agent with Claude Code to review the current file (august-2025.mdx). The agent executes commands and provides feedback just as it would with any other runtime.

      <img src="https://mintcdn.com/forgoodaiinc/8v1FWTiXZjxP2hz5/images/zen-cli-cc-custom-agents.png?fit=max&auto=format&n=8v1FWTiXZjxP2hz5&q=85&s=444ba097a2e29908b8830feba9e93c7f" alt="Using Claude Code with custom agents - showing Review Agent reviewing august-2025.mdx file" width="1096" height="796" data-path="images/zen-cli-cc-custom-agents.png" />
    </Tip>

    All Zencoder features (custom agents, multi-repo context, skills) work with the Claude Code runtime.
  </Tab>

  <Tab title="OpenAI Codex">
    OpenAI Codex is OpenAI's coding CLI using Codex models for code generation, explanation, and refactoring.

    <Tip>
      **Pricing:** Codex access is included with ChatGPT Plus and Team subscriptions. See [OpenAI's Codex docs](https://developers.openai.com/codex/cli) for details.
    </Tip>

    **Prerequisites:**

    * Node.js 18 or newer
    * ChatGPT Plus, Team, or Enterprise subscription

    <Steps>
      <Step title="Install OpenAI Codex">
        Visit [OpenAI Codex documentation](https://developers.openai.com/codex/cli) to learn more and ensure your ChatGPT subscription includes Codex access.
      </Step>

      <Step title="Install Codex CLI">
        Install the Codex command-line interface using npm:

        ```bash theme={"system"}
        npm i -g @openai/codex
        ```
      </Step>

      <Step title="Authenticate OpenAI Codex">
        Authenticate OpenAI Codex by running the following command. You'll be prompted to sign in with your ChatGPT account or provide your own API key:

        ```bash theme={"system"}
        codex
        ```
      </Step>

      <Step title="Select OpenAI Codex as Your Runtime">
        Once authenticated locally, return to Zencoder and select OpenAI Codex as your runtime. In the chat box, click on the settings icon. Under the `Agent CLI` category, click on it and select `OpenAI Codex` from the list of available CLIs (Zen CLI, Claude Code, or OpenAI Codex).

        <img src="https://mintcdn.com/forgoodaiinc/NMq1QhlpSl14Gauf/images/cli-selector-codex.png?fit=max&auto=format&n=NMq1QhlpSl14Gauf&q=85&s=381f17938c09cd5240ba5ffac148efc0" alt="Selecting OpenAI Codex as runtime in Zencoder settings" width="1215" height="739" data-path="images/cli-selector-codex.png" />

        <Note>
          After you install Codex and run the `codex` command, you will be prompted to log in with the following screens:

          <img src="https://mintcdn.com/forgoodaiinc/8v1FWTiXZjxP2hz5/images/zen-cli-codex-login.png?fit=max&auto=format&n=8v1FWTiXZjxP2hz5&q=85&s=d10a130da4def44b7eef9213da930e3c" alt="Open terminal to login prompt" width="1238" height="1101" data-path="images/zen-cli-codex-login.png" />

          Sign in with your ChatGPT account or provide your own API key, then press Enter to continue

          After logging in, you will be presented with an option to sign into Codex with ChatGPT. Press Continue on this dialog:

          <img src="https://mintcdn.com/forgoodaiinc/8v1FWTiXZjxP2hz5/images/zen-cli-codex-signin-confirm.png?fit=max&auto=format&n=8v1FWTiXZjxP2hz5&q=85&s=35963483707ca613920f4c5bceb0ba66" alt="Sign-in confirmation screen with Continue button" width="973" height="965" data-path="images/zen-cli-codex-signin-confirm.png" />

          After completing the web authentication, you will be able to return to the terminal and see this green notification confirming you have been signed in with your ChatGPT account. Press Enter to continue and you should be all set up:

          <img src="https://mintcdn.com/forgoodaiinc/8v1FWTiXZjxP2hz5/images/zen-cli-codex-signed-in-terminal.png?fit=max&auto=format&n=8v1FWTiXZjxP2hz5&q=85&s=d3f34f61bc58f13b82d74677ca994540" alt="Terminal showing successful authentication" width="1019" height="434" data-path="images/zen-cli-codex-signed-in-terminal.png" />
        </Note>
      </Step>
    </Steps>

    **Using OpenAI Codex with Zencoder**

    Once setup is complete, you can use OpenAI Codex just like any other Zencoder runtime. You can select the [coding agent](/features/coding-agent), or use [custom agents](/features/ai-agents) from the [model selector](/features/models).

    All Zencoder features (custom agents, multi-repo context, skills) work with the Codex runtime.
  </Tab>

  <Tab title="Gemini CLI">
    Gemini CLI is available as an agent runtime in [Zenflow](/clis/gemini). IDE Agent support is being rolled out — check the [changelog](/changelog/home) for updates.
  </Tab>
</Tabs>

## What You Get

* **Use existing subscriptions** — no additional runtime cost; use your ChatGPT, Claude, or Gemini plan
* **IDE integration** — CLI tools run inside VS Code / JetBrains instead of a separate terminal
* **Switch runtimes** — change the underlying model provider per chat
* **Multi-repo context** — agents see indexed repositories beyond the current project
* **Custom agents and skills** — team-wide agent configurations and coding standards apply regardless of runtime
* **Analytics** — usage tracking across all runtimes

## FAQ

<AccordionGroup>
  <Accordion title="Do I need to pay for Zencoder if I already have a ChatGPT/Claude subscription?">
    No! You can use Zencoder's Universal CLI Platform for free with your existing subscription. You can check more about the plans and available features on our [pricing page](https://zencoder.ai/pricing).
  </Accordion>

  <Accordion title="Can I switch between different CLI tools?">
    Yes! You can switch between Claude Code, OpenAI Codex, and other supported runtimes at any time through the Agent CLI settings in the chat box. Simply click the settings icon and select a different CLI from the Agent CLI category.
  </Accordion>

  <Accordion title="Do I lose any features when using external CLIs?">
    No! You get all of Zencoder's features (custom agents, multi-repo intelligence, etc.) regardless of which runtime you choose.
  </Accordion>

  <Accordion title="Is my code sent to Zencoder when using external CLIs?">
    When using external CLIs, your code is processed by your chosen provider (Anthropic, Google, or OpenAI). Zencoder only manages the IDE integration and enterprise features layer.
  </Accordion>

  <Accordion title="Can I use this with on-premise deployments?">
    Yes! Enterprise customers can deploy the entire stack on-premise or in a hybrid configuration. Contact [enterprise@zencoder.ai](mailto:enterprise@zencoder.ai) for details.
  </Accordion>
</AccordionGroup>

## Troubleshooting

<Card title="Windows Installation Issues" icon="windows" href="/user-guides/troubleshooting/windows-cli-installation">
  If you encounter PowerShell execution policy errors while installing Claude Code or OpenAI Codex on Windows, check our troubleshooting guide for a quick fix.
</Card>

***

<Note>
  Zencoder is not affiliated with or endorsed by Anthropic, OpenAI, Google, or Microsoft. All product and company names herein may be trademarks of their respective owners.
</Note>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.