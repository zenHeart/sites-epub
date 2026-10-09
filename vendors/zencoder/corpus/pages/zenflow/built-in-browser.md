> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Built-in Browser

> Preview live UI state, browse the web, and verify agent work—all without leaving Zenflow.

## Overview

Zenflow includes a built-in browser that shows live UI state directly inside your workflow. Check rendered output, browse reference material, or verify agent changes without switching windows.

<CardGroup cols={3}>
  <Card title="Live Preview" icon="eye">
    View your running application at localhost directly inside Zenflow—no window switching required.
  </Card>

  <Card title="Browse While Agents Work" icon="globe">
    Open YouTube, docs, or any website in a browser tab while agents continue executing tasks in the background.
  </Card>

  <Card title="Copy and Fix" icon="copy">
    Spot something off? Copy the element from the browser and ask the agent to fix it—all in the same workspace.
  </Card>
</CardGroup>

## How It Works

The built-in browser lives alongside your chat tabs, terminals, and task steps. Open it anytime to check your app's live state, browse reference material, or verify agent work without context-switching.

<Steps>
  <Step title="Open the browser">
    Click **New browser** in the top-right toolbar of any task view, next to New chat and New terminal.
  </Step>

  <Step title="Navigate to any URL">
    Type a URL in the address bar. Navigate to localhost to preview your running app, or visit any website.
  </Step>

  <Step title="Work in parallel">
    Switch between browser, chat, and terminal tabs freely. Agents keep running in the background while you browse.
  </Step>

  <Step title="Verify and iterate">
    Check the live UI, copy elements that need changes, and ask the agent to fix them—all without leaving Zenflow.
  </Step>
</Steps>

## Typical Workflow

<Steps>
  <Step title="Click 'New browser'">
    From any task view, look for the **New browser** button in the top-right toolbar—right next to New chat and New terminal. Clicking it opens a browser tab alongside your existing chat and terminal tabs.
  </Step>

  <Step title="A browser tab appears">
    A new Browser tab shows up in your tab bar with a full address bar, back/forward buttons, and a reload control. Type any URL to navigate—just like a regular browser.
  </Step>

  <Step title="Browse while agents work">
    Navigate to YouTube, documentation, or any other website while agents continue executing your task steps in the background. Your task progress, chat history, and terminal sessions remain accessible in their own tabs.
  </Step>

  <Step title="Start a dev server from the terminal">
    Switch to a terminal tab and run your dev server (e.g., `npm run dev`). Once it's up, the built-in browser can connect to localhost to show your running application.
  </Step>

  <Step title="Preview your live app">
    Navigate the browser tab to your local dev server URL (e.g., `http://localhost:3420`). The live UI renders directly inside Zenflow so you can verify that agent changes look correct—without switching windows.
  </Step>

  <Step title="Copy elements and request fixes">
    Spot something off in the preview? Copy the element or take note of what needs changing, switch to the chat tab, and tell the agent what to fix. The agent applies the change, and you can immediately verify it in the browser.
  </Step>
</Steps>

## Use Cases

<CardGroup cols={2}>
  <Card title="UI Verification" icon="check">
    After agents implement a frontend change, open the browser to confirm the result looks correct before approving or merging.
  </Card>

  <Card title="Reference Browsing" icon="book">
    Pull up API docs, design specs, or Stack Overflow without leaving your Zenflow workspace.
  </Card>

  <Card title="Visual Feedback Loop" icon="arrows-rotate">
    See something that needs tweaking? Copy the element from the browser, paste it into the chat, and ask the agent to adjust it.
  </Card>

  <Card title="End-to-End Testing" icon="vial">
    Manually verify user flows by interacting with the live app while reviewing agent-generated code changes side by side.
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.