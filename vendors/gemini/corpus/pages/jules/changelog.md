---
title: Changelog
description: Full history of changes to Jules
---


# Changelog


## 2026-03-09: Gemini 3.1 Pro is now available in Jules

---
title: "Gemini 3.1 Pro is now available in Jules"
pubDate: "2026-03-09"
description: "Gemini 3.1 Pro is now available in Jules"
image: "gemini-3.1-pro.png"
---

![gemini-3.1-pro](../../../public/gemini-3.1-pro.png)

Gemini 3.1 Pro is now available in Jules for Google Pro plan users. 3.1 Pro is a smarter, more capable baseline for complex problem-solving.

![gemini-3.1-pro-web-app](../../../public/gemini-3.1-pro-web-app.png)

This replaces Gemini 3 Pro as the default model for Pro users. Give it a try and let us know what you think.

___

## 2026-02-19: Auto-Fixing CI Failures and configure Jules to commit as you

---
title: "Auto-Fixing CI Failures and configure Jules to commit as you"
pubDate: "2026-02-19"
description: "Jules now automatically fixes CI failures on your PRs and gives you control over commit authorship attribution."
---

import Video from "../../components/Video.astro";

<Video directory="JULESVC000_CI_FIXER" />

### CI Fixer

Jules now automatically detects and fixes CI failures on pull requests it creates. When a check fails in GitHub Actions, Jules receives the error, works through a fix, and resubmits the PR — all without manual intervention.

![ci-fixer](../../../public/ci-fixer.png)

Previously, a failed CI check on a Jules PR would stall your workflow. Resolving it required setting up REST API calls or manually copy-pasting error logs back to Jules. CI Fixer closes that gap. Jules now operates in a loop — fixing, committing, and resubmitting — so your PRs keep moving forward.

### Commit Authoring

You can now control how commits from Jules are attributed on GitHub. Three authorship modes are available:

* **Jules:** Jules is the sole author of all commits (default, existing behavior).
* **Co-authored (Jules + You or You + Jules):** Commits are co-authored by both you and Jules, crediting both contributors.
* **User only:** You are the sole author. Jules applies its changes under your identity.

![authorship](../../../public/authorship.png)

Previously, Jules authored every commit and PR, which meant your GitHub contribution graph didn't reflect the work you initiated. Setting the commit authorship in to co-authored to you or you + Jules, makes it clear to contributors and PR reviewers who is driving each change. 

It applies at the user level across all repositories and all task types — scheduled, suggested, and manually triggered tasks.

#### Setting commit authorship

1. Go to the Jules Settings page
1. Open the **Commit Authoring** section
1. Select your preferred authorship mode
1. All future sessions will use the selected attribution

___

## 2026-02-02: MCP support comes to Jules

---
title: "MCP support comes to Jules"
pubDate: "2026-02-02"
description: "We've added MCP Server support for Linear, Stitch, Neon, Tinybird, Context7, and Supabase"
image: "mcp-support.png"
---

![mcp-support](../../../public/mcp-support.png)

Today we're launching MCP Server support in Jules starting with: Linear, Stitch, Neon, Tinybird, Context7, and Supabase.

Add a service connection in the Settings page and will trigger the MCP server tools in a session when it detects the need for a tool call.

### Getting started

Our MCP server integration uses API key authentication. To get started:

1. Get the service's API key (such as Linear or Stitch)
1. Go to the Jules Settings page
1. Click on the MCP section
1. Plug in your API key for that specific service
1. Kick off a new session
1. Jules will trigger the MCP server tools when it detects the need for the call

![mcp-settings](../../../public/mcp-settings.png)

### Focus on Security
It might seem odd for us to limit which MCP servers Jules can connect to. However, we are wanted to start with a focus on security. Jules operates within a cloud development environment connected to your GitHub repositories, so we prioritize a **security-first** approach to third-party integrations.

By hand-selecting these initial servers, we can:

* **Validate Data Flow:** We ensure that each server adheres to strict data-handling standards, keeping your source code and API keys isolated.
* **Audit Tool Permissions:** We verify that each server only requests the specific permissions it needs to function, preventing "over-privileged" access to your environment.
* **Ensure Stability:** A vetted integration means fewer connection drops and a more predictable experience when Jules interacts with your external data.

We plan to expand this list as we work with more partners.

### Tell us what to add next
If you have an MCP server in mind, you can let us know in the settings panel what we should add next.

___

## 2026-01-30: Gemini 3 Flash is now the base model in Jules

---
title: "Gemini 3 Flash is now the base model in Jules"
pubDate: "2026-01-30"
description: "Gemini 3 Flash is now the base model in Jules"
image: "gemini-3-flash@2x.png"
---

![gemini-3-flash](../../../public/gemini-3-flash@2x.png)

Today we're launching Gemini 3 Flash in Jules for all users on all tiers.

It's our new base model that's faster and significantly more capable than our previous base model, Gemini 2.5 Pro. If it feels like Jules feels like it had a double espresso, you now know why.

![gemini-3-flash-web-app](../../../public/gemini-3-flash-web-app.png)

Give it a spin and let us know what you think.

___

## 2026-01-26: Introducing the Planning Critic for Auto-Approved Plans

---
title: "Introducing the Planning Critic for Auto-Approved Plans"
pubDate: "2026-01-26"
description: "Introducing the Planning Critic for Auto-Approved Plans"
image: "planning-critic.png"
---

![Planning Critic](../../../public/planning-critic.png)

We’ve introduced a secondary agent—the Planning Critic—to review all plans that do not require human intervention. Before Jules executes a single line of code, this agent rigorously critiques and refines the proposed plan. While this adds a small amount of time to the planning phase, the result is a 9.5% reduction in task failure rates and significantly higher quality execution paths.

___

## 2026-01-26: Auto-Solving Your Top Task

---
title: "Auto-Solving Your Top Task"
pubDate: "2026-01-26"
description: "Jules now proactively solves your highest-confidence suggested task."
image: "topsuggested.png"
private: true
---

![topsuggested](../../../public/topsuggested.png)

Jules is getting more proactive. Instead of just *suggesting* improvements, Jules now automatically identifies the highest-confidence task and solves it for you in the background.

You don't need to trigger anything—just check the sidebar. The code will be waiting there, ready for a one-click review.

*Note: This feature is currently available to paid users.*

___

## 2026-01-26: Jules now finds performance optimizations

---
title: "Jules now finds performance optimizations"
pubDate: "2026-01-26"
description: "Jules now finds performance optimizations"
image: "performance.png"
---

![performance](../../../public/performance.png)

Jules now surfaces Performance Optimizations Jules has expanded its detection capabilities.

In addition to standard TODOs, Jules now proactively identifies performance optimizations within your code. These suggestions appear alongside your existing TODOs in the Suggested Tasks view, helping you catch bottlenecks and inefficiencies just as easily as you catch unfinished code.

___

## 2026-01-26: REST API: Repoless, File Outputs, and Activity Filters

---
title: "REST API: Repoless, File Outputs, and Activity Filters"
pubDate: "2026-01-26"
description: "REST API: Repoless, File Outputs, and Activity Filters"
image: "api-changes-repoless.png"
---

```shell
PROMPT_CONTENT=$(jq -Rs . < my_prompt.md)

curl 'https://jules.googleapis.com/v1alpha/sessions' \
  -X POST \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $JULES_API_KEY" \
  -d "{
    \"prompt\": $PROMPT_CONTENT,
    \"
```

### Repoless support in the REST API

Repoless comes to the REST API and we think this has **massive potential**. A repoless session in a sense becomes serverless, because it creates an ephemeral cloud dev environment with Node, Python, Rust, Bun, and other runtimes preloaded on the image.

The massive potential is that this serverless environment comes with an AI coding agent.

With a single API call you can spawn a serverless dev environment with only the context in your prompt. When it's done you can download the file outputs from the session.

We can't wait to see what you all do with this one.

### Get the entire file outputs from a session

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  FILES CHANGED                                                               │
├──────────────────────────────────────────────────────────────────────────────┤
│  [M]  bun.lock                                            +567    -163       │
│  [A]  bunfig.toml                                           +2      -0       │
│  [M]  examples/simple/main.ts                               +2      -1       │
│  [M]  packages/core/src/client.ts                          +21      -6       │
│  [M]  packages/core/src/network/adapter.ts                 +46     -13       │
│  [A]  packages/core/src/retry-utils.ts                     +89      -0       │
│  [M]  packages/core/src/sources.ts                          +2      -0       │
│  [M]  packages/core/src/streaming.ts                       +15     -51       │
│  [M]  packages/core/src/types.ts                           +12      -0       │
│  [M]  packages/core/tests/automated_session.test.ts       +125      -0       │
│  [M]  packages/core/tests/network/adapter.test.ts         +109      -0       │
│  [A]  packages/core/tests/retry-utils.test.ts             +140      -0       │
│  [M]  packages/core/tests/sources.test.ts                  +21      -0       │
├──────────────────────────────────────────────────────────────────────────────┤
│  Summary: 13 files changed                        +1,151 insertions, -234    │
└──────────────────────────────────────────────────────────────────────────────┘
  Session finished: completed
```

Speaking of file outputs, we just made that a lot easier. When a session completes a task, you can now get the entire change set. 

This is stored in a git patch format for parsing changes such as additions, modifications, and deletions.

### Timestamp based filters for Session Activities

```bash
ENDPOINT="https://jules.googleapis.com/v1alpha/sessions/1234567/activities"
TIMESTAMP="2026-01-17T00:03:53.137240Z"

curl -H "x-goog-api-key: $JULES_API_KEY" \
     "$ENDPOINT?createTime=$TIMESTAMP"
```

Each Jules Session has a collection of activities that represent the steps Jules took to complete the task. These activities are immutable and can be used to reconstruct the session.

Activities follow the event source pattern, meaning once they occur they never change. They are a record in time of the steps Jules took to complete the task. Since they never change, you can cache them aggressively. 

We added a `createTime` filter that works like a range cursor and allows you to only fetch new activities over the network.

This may seem like a small optimization but stay tuned. We have some big news around this one.

___

## 2026-01-26: Update Scheduled Tasks

---
title: "Update Scheduled Tasks"
pubDate: "2026-01-26"
description: "Edit, pause, and resume your scheduled tasks."
image: "edit-scheduled-tasks.png"
---

![edit-scheduled-tasks](../../../public/edit-scheduled-tasks.png)

Quick quality-of-life update: You no longer need to delete and recreate a scheduled task just to fix a typo or change the timing.

You can now **Edit**, **Pause**, and **Resume** your tasks directly from the menu. It’s a small change that saves a lot of clicking.

___

## 2025-12-10: Enable suggested tasks to let Jules find issues proactively

---
title: "Enable suggested tasks to let Jules find issues proactively"
pubDate: "2025-12-10"
description: "Enable suggested tasks to automatically find and fix #TODOs"
image: "suggested.png"
---

![suggested](../../../public/suggested.png)


Jules can now work proactively in the background to improve your code. With Suggested Tasks, Jules scans your repository for potential improvements and presents them on your repo page.

To get started, enable the proactive suggestions toggle on the repo page.

- **Tackle the #TODOs**: In this initial release, Jules focuses on identifying `#TODO` comments in your code. It reads the context, formulates a plan, and presents it for your approval—turning idle comments into active solutions. More use cases coming soon. 

- **Continuous Improvement**: Once enabled, Jules continuously monitors your codebase. You don't have to ask; just check your dashboard for new suggestions and approve the ones you want.

This experimental feature is available today for Google AI Pro and Ultra subscribers on up to five repositories.

Read more at: [Suggested Tasks](https://jules.google/docs/suggested-tasks/).

___

## 2025-12-10: Put routine maintenance on autopilot with Scheduled Tasks

---
title: "Put routine maintenance on autopilot with Scheduled Tasks"
pubDate: "2025-12-10"
description: "Set recurring tasks for Jules to handle maintenance automatically"
image: "scheduled.png"
---

![scheduled](../../../public/scheduled.png)

You can now set recurring tasks for Jules. Whether it’s a weekly dependency check, a nightly lint fix, or a monthly cleanup, just define it once and Jules will handle the rest on your schedule.

To get started, navigate to the **Scheduled** tab on your repo page to configure your first task.

- **Set it and forget it**: Define your maintenance chores once. Jules will wake up, perform the task, and open a PR without you needing to lift a finger.

- **Never miss a beat**: No more manual prompts for the stuff that needs to happen every week. Ensure consistent code quality and dependency hygiene by automating your routine work.

This feature is available today for all Jules users. 

Read more at: [Scheduled Tasks](https://jules.google/docs/scheduled-tasks/).

___

## 2025-12-10: Automated fixes for Render deployments

---
title: "Automated fixes for Render deployments"
pubDate: "2025-12-10"
description: "Automatically fix Render deployments"
image: "changelog-render.png"
---

![Render](../../../public/changelog-render.png)

We’ve integrated with Render to handle the last mile of shipping code. Jules can now detect failed builds, analyze the logs, and push fixes to its PRs before you even know your build failed. 

To enable this, go to your Render Dashboard, open the Help menu (top-right), and click Coding Agents to provision your API Key. Paste this key into Settings > Integrations in Jules.

1. **Instant Recovery:** No more context switching to dig through console logs. Jules detects the failure immediately and identifies the root cause.
2. **Proactive Fixes:** Instead of just alerting you to an error, Jules writes the code to fix it. Review the solution as a standard commit on your PR, merge it, and get back to green.

This integration is available now. Check out the [docs](/integrations) for the full setup guide, including enabling PR previews.

**Note:** For now, Jules only fixes PRs it has created.

___

## 2025-11-20: Start from scratch—instantly

---
title: "Start from scratch—instantly"
pubDate: "2025-11-20"
description: "Launch Jules tasks without a repository"
image: "repoless.png"
---

![Repoless](../../../public/repoless.png)

You can now start a Jules task immediately without selecting a repository. We’ve removed the speed bump between your idea and your code, allowing you to capture that spark of inspiration without the overhead.

To trigger this, simply click the "X" next to the selected repo to start a fresh, repoless session.

- **Skip the Detour**: Previously, starting a fresh journey meant hopping over to GitHub to create an empty repo first. Now, you can bypass that context switch entirely and keep your momentum.

- **Instant Ideation**: Whether you are prototyping a new feature or writing a quick script, you can dive straight into the logic. Just describe what you want, and Jules gets to work.

This update is available now for all users starting a new task.

___

## 2025-11-19: Introducing Gemini 3 Pro

---
title: "Introducing Gemini 3 Pro"
pubDate: "2025-11-19"
description: "Gemini 3 is now in Jules"
image: "gemini3.png"
---

![Gemini 3](../../../public/gemini3.png)

Gemini 3 Pro is now available in Jules. This is the newest generation of the Gemini family, bringing clearer reasoning, stronger instruction following, and a meaningful lift in day-to-day reliability.

- **Coherent Planning**: Multi-step tasks hold together more naturally. The agent requires less management during transitions, meaning your work moves forward with fewer detours.

- **Visual Verification**: Leveraging the improved multimodal capabilities of Gemini 3 Pro, Jules renders and verifies web app outcomes with significantly higher precision.

- **Agentic Memories**: The new model utilizes context more effectively, helping Jules adapt to your coding preferences and project nuances more reliably over time.

Gemini 3 Pro is rolling out now to Google AI Ultra users and will be available to Pro users in the coming days.

___

## 2025-11-10: New Jules Tools CLI Updates: Side-by-Side Diffs, Repo Inference, and More

---
title: "New Jules Tools CLI Updates: Side-by-Side Diffs, Repo Inference, and More"
pubDate: "2025-11-10"
description: "A summary of recent updates to the Jules Tools CLI, including a side-by-side diff viewer, repository inference, WSL/Arch Linux fixes, and PNPM support."
image: "julestools2.png"
---

![Jules Tools](../../../public/julestools2.png)

We've been busy shipping a bunch of new updates to the Jules Tools CLI to make your experience smoother and more powerful. Here’s a rundown of what’s new:

#### Parallel Task Execution

You can now start multiple parallel tasks for the same prompt using the `--parallel` flag with `jules remote new`. This is useful for getting multiple suggestions from Jules at once (max of 5).

- **Added**: `--parallel` flag to `remote new` command.

#### v0.1.40 - WSL/Arch Linux Credential Fixes

We've refactored how we handle authentication to resolve credential issues for users on WSL and Arch Linux. This means broader platform support and no more login issues.


#### v0.1.39 - OAuth2 Error Handling Improvements

We've enhanced our OAuth2 flow to be more resilient with better error recovery, making the authentication process more reliable.


#### v0.1.38 - Repository Inference Feature

To shorten CLI commands and reduce configuration, we've added repository inference. Now, Jules can automatically detect the repository from your current directory, so you don't have to specify it manually.


#### v0.1.37 - PNPM Installation Fixes

We've added better support for the PNPM package manager, ensuring full compatibility for a wider range of JavaScript projects.


#### v0.1.36 - Side-by-Side Diff Viewer + Bug Fixes

Reviewing code is now faster and more readable with the new side-by-side diff viewer in the TUI. We've also added comprehensive test coverage and fixed bugs related to auto-approval and timeout validation.

___

## 2025-10-03: Introducing the Jules API

---
title: "Introducing the Jules API"
pubDate: "2025-10-03"
description: "Introducing the Jules API"
image: "api.png"
---
![API](../../../public/api.png)

You can now programmatically access Jules's capabilities to automate your work and build powerful integrations. The Jules API is designed to help you seamlessly integrate Jules into your existing development workflows, unlocking new ways to automate and enhance the entire software development lifecycle.

**With the API, you can:**

- Create custom integrations with tools like Slack for "ChatOps" workflows, allowing you to assign tasks directly from your chat client.
- Automate bug fixing and feature implementation by connecting Jules to your project management tools like Linear or Jira.
- Integrate Jules directly into your CI/CD pipelines in services like GitHub Actions.

Here’s a quick example of how to create a new task (a "Session") using a cURL command:


```
curl 'https://jules.googleapis.com/v1alpha/sessions' \
    -X POST \
    -H "Content-Type: application/json" \
    -H 'X-Goog-Api-Key: YOUR_API_KEY' \
    -d '{
      "prompt": "Create a boba app!",
      "sourceContext": {
        "source": "sources/github/bobalover/boba",
        "githubRepoContext": {
          "startingBranch": "main"
        }
      },
      "title": "Boba App"
    }'

```

For more examples see the [API documentation](https://developers.google.com/jules/api).

___

## 2025-10-02: Jules in the command line

---
title: "Jules in the command line"
pubDate: "2025-10-02"
description: "Jules in the command line"
image: "julestools.png"
---
![Jules Tools](../../../public/julestools.png)

We’re launching Jules Tools, a new command-line interface designed to give you direct control over your AI coding agent, making it scriptable, customizable, and easy to integrate into your existing workflows.

**Key Features:**

- **Direct Control:** Create tasks (jules remote new), list active sessions (jules remote list), and monitor Jules without leaving your command line.
- **Apply Patches Locally:** Instantly pull work-in-progress code from an active Jules session and apply it to your local machine. This lets you test changes immediately, without waiting for a commit to GitHub.
- **Scriptable & Composable:** Integrate Jules into your automations by piping in output from other tools like gh, jq, or cat.
- **Interactive Dashboard:** For a more guided experience, launch the built-in terminal user interface (TUI) to create and manage tasks step-by-step.


**How to Install:**

Install globally via npm:
```npm install -g @google/jules```

Or run directly without a permanent installation:
```npx @google/jules```

**Starter Commands to Try:**

See all available commands:
```jules help```

List all repos connected to Jules:
```jules remote list --repo```

Create a new task in a specific repo:
```jules remote new --repo torvalds/linux --session "write unit tests"```

<br></br>

If you run into any issues, please share your experience with us via in-app feedback or on our [Discord channel](https://discord.com/channels/1172568727942860810/1374062797519847505).

___

## 2025-10-01: Use Environment Variables In Jules

---
title: "Use Environment Variables In Jules"
pubDate: "2025-10-01"
description: "Use Environment Variables In Jules"
image: "envar.png"
---
![Environment Variables](../../../public/envar.png)

You can now provide Jules with environment variables at the repository level. This enables Jules to access the project-specific configurations it needs to complete tasks, like running builds, executing tests, or interacting with different services.

**How It Works**:
- **Add Variables in Repo Settings:** Navigate to your repository's settings page to add your environment variables. They will be associated directly with your project.
- **Enable for a Task:** When you start a new task with Jules, you'll have the option to make these environment variables available to it.
- **Task-Long Access:** Once enabled for a specific task, Jules will have access to the variables for the entire duration of that task. Please note that this setting cannot be changed after the task has begun.

We're excited to see how this unlocks new and more complex workflows for you and your team! Let us know if you have any feedback.

___

## 2025-09-30: Jules gains memory!

---
title: "Jules gains memory!"
pubDate: "2025-09-30"
description: "Jules gains memory"
image: "memory.png"
---
![Memory](../../../public/memory.png)

**Jules Memory for Repositories:** We're excited to introduce a new Memory feature! Jules now has the ability to learn from your interactions.

- **How it works:** During a task, Jules will save your preferences, nudges, and corrections.
- **The benefit:** The next time you run the same or a similar task in that specific repository, Jules will reference its memory to better anticipate your needs and follow your established patterns, leading to more accurate results with less guidance.
- **Settings:** You can toggle memory on or off for the repo in the repo settings page under “Knowledge”

___

## 2025-09-29: Tell Jules exactly what file to work on using file selector

---
title: "Tell Jules exactly what file to work on using file selector"
pubDate: "2025-09-29"
description: "Tell Jules exactly what file to work on using File Selector"
image: "fileselector.png"
---
![File Selector](../../../public/fileselector.png)

You can now tell Jules exactly which files to work with for any given task. Use the new file selector to easily and precisely reference specific files. 

This removes ambiguity and gives you more granular control over Jules's actions, helping to tighten the context for your task.

___

## 2025-09-23: Jules Acts on PR Feedback

---
title: "Jules Acts on PR Feedback"
pubDate: "2025-09-23"
description: "Jules will now actively participate in pull request reviews, responding to your comments and applying suggested changes."
image: "changelog-pr-comments.png"
---
![Jules responding to a PR comment](../../../public/changelog-pr-comments.png)

Jules is now able to read and respond to your comments on pull requests!

When you start a review, Jules will add a 👀 emoji to each comment to let you know it's been read. Based on your feedback, Jules will then push a commit with the requested changes.

For more control, you can switch to **Reactive Mode** in your [global Jules UI settings](https://jules.google.com/settings). In this mode, Jules will only act on comments where you specifically mention `@Jules`.

___

## 2025-09-19: All Hands on Deck!

---
title: "All Hands on Deck!"
pubDate: "2025-09-19"
description: "All Hands on Deck!"
image: "changelog-019.png"
---
![image upload](../../../public/changelog-019.png)

Ahoy, mateys! To celebrate International Talk Like a Pirate Day, we've given Jules a temporary map to the treasure.

- Jules Speaks Pirate: You'll find your AI agent's responses are a bit more... swashbuckling... for today only.

- Same Great Logic: Fear not! Beneath the eyepatch and Jolly Roger, it's the same powerful coding engine ready to help you plunder that backlog and send bugs to Davy Jones' locker.

___

## 2025-09-09: Image upload

---
title: "Image upload"
pubDate: "2025-09-09"
description: "Image upload"
image: "image-upload.png"
---
![image upload](../../../public/image-upload.png)

You can now upload images when creating a task in Jules. Use this to show frontend bugs, design inspiration, UI mocks, or any visual context you want Jules to consider while generating code. 

For now: 

- Only JPEG and PNG formats are supported.
- You can uplaod as many images as you want, as long as the total size is under 5MB.
- Image upload is only supported at task creation (we're working on enabling it for follow-up prompts soon).

Note: If your task involves using assets (e.g. logos) directly in code, those must still be committed to your GitHub repo. 

[Read more](https://jules.google/docs/running-tasks/) about Jules image support.

___

## 2025-09-04: Stacked Diff

---
title: "Stacked Diff"
pubDate: "2025-09-04"
description: "Stacked Diff"
image: "changelog-017-fade.png"
---
![Stacked Diff](../../../public/changelog-017-fade.png)

To improve the code review experience, we've introduced a new stacked layout for the diff viewer. This change displays diffs for multiple files vertically on a single screen. The stacked view makes it easier to see related changes across your codebase at a glance, providing better context and speeding up your review process.

Changes:

- The diff viewer now stacks file changes vertically by default
- You can also toggle back to the previous tabbed diff viewer

___

## 2025-09-03: Improved Jules Critic

---
title: "Improved Jules Critic"
pubDate: "2025-09-03"
description: "Improved Jules Critic"
image: "changelog-016.png"
---
![Improved Critic](../../../public/changelog-016.png)

We've shipped significant improvements to the Jules critic agent, making its feedback more insightful and reliable. To increase transparency and give you more insight into its evaluation process, you can now see the critic's real-time analysis as it works.

Changes:

- The critic's thought process is now visible in the UI, showing its step-by-step evaluation of the code in real-time.
- The critic's now incorporates more contextual information when making decisions, leading to more accurate and relevant feedback on potential bugs and logic flaws.

___

## 2025-09-02: Jules Sample Prompts

---
title: "Jules Sample Prompts"
pubDate: "2025-09-02"
description: "A collection of sample prompts"
image: "changelog-015.png"
---
![Sample Prompts](../../../public/changelog-015.png)

To help new users get started with Jules, we've added sample prompts to the home page. These static prompts provide examples of how to use Jules and can be added to the text box with a single click.

Changes:

- Sample prompts are now displayed on the home page for all users.
- Clicking on a sample prompt will add the text of the prompt to the input box.

___

## 2025-08-22: Render images in the diff viewer

---
title: "Render images in the diff viewer"
pubDate: "2025-08-22"
description: "Jules can now render images in the diff viewer"
image: "imagesdiffviewer.png"
---
![Images in diff viewer](../../../public/imagesdiffviewer.png)

Jules now intelligently renders images within the diff viewer, providing an immediate visual context for your modifications.

This means:

- Instant Visual Feedback: When Jules generates images (like charts, diagrams, or web UI screenshots), you'll see the actual image in the diff, not just its code representation.
- Streamlined Workflow: No need to switch between tools or download files to see the results. Jules keeps everything in one place.

Try it out! Ask Jules to render an output, like a graph based on data, and commit it to your repository. You'll be able to see the generated image seamlessly within your diff viewer.

___

## 2025-08-15: Export at any time

---
title: "Export at any time"
pubDate: "2025-08-15"
description: "Export at any time"
---
![Export](../../../public/exportatanytime.png)

You're now in full control of when your code gets to GitHub. No need to wait for a task to finish or ask Jules to do it for you. At any point during a task, just click the GitHub icon in the top right to publish the current work-in-progress as a new branch or open a pull request. This gives you more flexibility and control to review, test, or take over whenever you’re ready.

___

## 2025-08-15: Increasing the VM Size to 20GB

---
title: "Increasing the VM Size to 20GB"
pubDate: "2025-08-15"
description: "Increasing the VM Size"
---

We heard your feedback about running into disk space limits on larger projects. To address this, we've significantly increased the available disk space in the Jules VM to 20GB. This provides more room for large dependencies, build artifacts, and complex repositories, reducing disk-related failures so Jules can tackle bigger tasks. Happy Julesing!

___

## 2025-08-08: Jules can surf the web

---
title: "Jules can surf the web"
pubDate: "2025-08-08"
description: "Jules can surf the web"
image: "websearch.png"
---
![Post Beta](../../../public/websearch.png)

Jules can now proactively search the web for relevant content, documentation, or code snippets to help complete your tasks. This means Jules can get the information it needs, resulting in more accurate and successful task completion.

In Summary:
- Jules can find the latest documentation for dependencies/libraries you're using
- Jules can proactively find examples or code snippets that can help inform its implementation 

**Note**: web search works best when working on technical documentation. Queries like: "What is the latest news today?" are not supported.

___

## 2025-08-08: Interactive Plan

---
title: "Interactive Plan"
pubDate: "2025-08-08"
description: "Interactive Plan"
image: "interactiveplan.png"
---
![Post Beta](../../../public/interactiveplan.png)

Meet Interactive Plan. Instead of jumping straight to the solution, Jules will now read your codebase, ask clarifying questions, and work with you to refine the plan. This collaborative approach gives you more control and ensures you're on the same page, leading to higher-quality code and a more reliable solution.

In summary:
- Trigger the interactive plan from the dropdown when you start a task
- Jules will start a brainstorm with you and ask clarifying questions

___

## 2025-08-08: Critic Agent

---
title: "Critic Agent"
pubDate: "2025-08-08"
description: "Critic Agent"
image: "critic.png"
---
![Critic Agent](../../../public/critic.png)

Great developers don’t just write code, they question it. And now, so does Jules. We’ve built the Jules critic agent to ensure that every line of code isn't just functional, but robust, secure, and efficient. It acts as an internal peer reviewer, challenging every proposed change to elevate the quality of the final output.

Some high level notes:

- **Critic-augmented generation:** The Jules critic is integrated directly into the generation process. Every proposed change undergoes adversarial review before completion.
- **Improved code quality:** The critic flags subtle bugs, missed edge cases, and inefficient code. Jules then uses this feedback to improve the patch in real-time.

- **A new kind of review:** The critic is not just another linter or test. It understands the intent and context behind code, similar to a human peer reviewer.

- **Built on research:** This feature draws on research into multi-step, tool interactive critiquing and actor-critic reinforcement learning, where an "actor" generates and a "critic" evaluates.

___

## 2025-08-07: Jules can test web-apps and show you the results

---
title: "Jules can test web-apps and show you the results"
pubDate: "2025-08-07"
description: "Jules can test web-apps and show you the results"
image: "computeruse.png"
---
![Post Beta](../../../public/computeruse.png)

Next time you are working on a front end project with Jules, ask it to verify its work and it'll render the website and send you back a screenshot!

- Ask Jules to complete a web development task and to verify the front end
- Jules will send you a screenshot of the front end along with any code changes
- The default Jules base image now includes Playwright for front end testing 
- Users can also add images in the form of public URLs for Jules to use as input

___

## 2025-08-06: Jules is out of beta!

---
title: "Jules is out of beta!"
pubDate: "2025-08-06"
description: "Jules is out of beta and our partership with Google One AI Plans"
image: "post-beta.png"
---
![Post Beta](../../../public/post-beta.png)

Today we are thrilled to announce that Jules is no longer in beta! Since launch just two months ago, Jules has passed over 140k public commits. Thank you to our amazing beta users for all your support and feedback. 

In addition, we’re launching our pricing plans to unlock higher task limits, along with a bunch of quality improvements in the Jules app and agent. Here are the details:
- Get higher task limits through the Google AI Pro and Ultra plans. More details at [Limits and Plans](./../usage-limits).
- Jules now uses the power of Gemini 2.5 thinking when creating its plan, resulting in higher quality plans and more complete tasks 
- Numerous bug fixes so Jules gets stuck less, and is better at following your instructions in agents.md

___

## 2025-08-05: Environment snapshots for faster tasks

---
title: "Environment snapshots for faster tasks"
pubDate: "2025-08-05"
description: "Snapshot your complex environments for faster tasks"
image: "envsnapshot.png"
---
![Env Snapshot](../../../public/envsnapshot.png)

Jules now creates a snapshot of your environment when you add environment setup scripts. For complicated environment, users should see faster and more consistent task execution. 

In summary:
- Jules will now snapshot your environment when you provide an environment setup script
- Snapshots are loaded automatically next time you run a task
- This provides for faster task startups, especially for complex environments
- You can find environment configuration by clicking the “codebase” in the left hand panel, or by clicking the “configure environment” button in the task pane.

___

## 2025-08-04: Open A PR directly from Jules

---
title: "Open A PR directly from Jules"
pubDate: "2025-08-04"
description: "Closing the loop from task to merge 🤝"
image: "openapr.png"
---
![Open a PR](../../../public/openapr.png)

Closing the loop from task to merge 🤝

Jules can now open a pull request directly from the UI.
After a task completes, just use the new dropdown next to the ‘Publish Branch’ button to open a PR. Jules will request to merge the newly published branch into main, streamlining your entire workflow. Less context switching, faster merging.

___

## 2025-07-18: Added Bun runtime support

---
title: "Added Bun runtime support"
pubDate: "2025-07-18"
description: "Jules now supports Bun. You can run tasks using Bun out of the box, no extra setup required."
image: "jules<3bun.png"
---
![Bun](../../../public/jules<3bun.png)

Jules now supports [Bun](https://bun.sh/). You can run tasks using Bun out of the box, no extra setup required. This expands compatibility for projects that use Bun instead of Node.

[Read more](https://jules.google.com/docs/environment/) about the jules base image and what tooling works with Jules.

___

## 2025-07-03: Improved task controls and other 💅 UI delight

---
title: "Improved task controls and other 💅 UI delight"
pubDate: "2025-07-03"
description: "Pause, resume, and delete tasks—without losing your sense of place. Available from sidebar and repo view."
image: "polish-tasks-changelog.png"
---
![Task controls](../../../public/polish-tasks-changelog.png)

- Pause, resume, and delete tasks—without losing your sense of place. Available from sidebar and repo view. You can even quickly copy task urls!
- Non-urgent task icons are now more recessive
- Certain hover states—which did not look good—have been toned back.
- System messages have more consistent padding and borders

[Learn more about running a task.](https://jules.google.com/docs/running-tasks/)

___

## 2025-06-26: Jules now listens to GitHub issues

---
title: "Jules now listens to GitHub issues"
pubDate: "2025-06-26"
description: "Add the label 'jules' to any GitHub issue to start a task in Jules. That’s it—label on, task live."
image: "assign-to-jules.png"
---
![Assign to Jules](../../../public/assign-to-jules.png)

Add the label 'jules' to any GitHub issue to start a task in Jules. That’s it—label on, task live.

How to summon Jules:

- Open a GitHub issue.
- Click the gear next to “Labels”.
- Add the label 'jules.'

Make sure the Jules GitHub App has access to your repo. After that, Jules takes it from there. [Read more about running tasks in Jules](https://jules.google/docs/running-tasks/)!

___

## 2025-06-20: Jules Agent Update: Faster, Smarter, More Reliable

---
title: "Jules Agent Update: Faster, Smarter, More Reliable"
pubDate: "2025-06-20"
description: "We’ve shipped a big upgrade to the Jules agent under the hood."
image: "agents-md-support.png"
---
![Jules environment updates](../../../public/agents-md-support.png)

We’ve shipped a big upgrade to the Jules agent under the hood.

What’s new:

- **Smarter context.** Jules reads from AGENTS.md if it’s in your repo.
- **Improved performance.** Tasks now complete faster—no numbers to share just yet, but you’ll feel it.
- **Significantly reduced punting.** We tightened the loop to keep Jules moving forward.
- **More reliable setup.** If you’ve added an environment setup script, Jules now runs it consistently.
- **Better test habits.** Jules is more likely to write and run tests on its own.

Check out the [Getting Started](https://jules.google/docs/) guide to learn more about AGENTS.md support.

___

## 2025-06-18: Modernized base environment and updated toolchains

---
title: "Modernized base environment and updated toolchains"
pubDate: "2025-06-18"
description: "We've overhauled the Jules development environment to move beyond the default Ubuntu 24.04 LTS packages."
image: "changelog-env-update.png"
---
![Jules environment updates](../../../public/changelog-env-update.png)

We've overhauled the Jules development environment to move beyond the default Ubuntu 24.04 LTS packages. This includes:

- Explicitly installing newer versions of key toolchains like Rust, Node, and Python, addressing long-standing version issues.
- Adding finer-grained control over installation steps via custom scripts instead of relying solely on apt.
- Introducing support for multiple runtimes, improved isolation, and version pinning to reduce drift and better match developer expectations.

These changes unblock several issues developers encountered with outdated dependencies and improve alignment with modern project requirements.

[Read about the Jules environment setup to learn more about what’s pre-installed.](https://jules.google/docs/environment/)

___

## 2025-06-06: Customization and Efficiency Enhancements

---
title: "Customization and Efficiency Enhancements"
pubDate: "2025-06-06"
description: "Performance upgrades: Enjoy a smoother, faster Jules experience with recent under-the-hood improvements."
image: "jules-copy-paste-download.png"
---
![Jules code view](../../../public/jules-copy-paste-download.png)

**Performance upgrades:** Enjoy a smoother, faster Jules experience with recent under-the-hood improvements.

**Quickly copy and download code:** New copy and download buttons are now available in the code view pane, making it easier to grab your code directly from Jules.

**Stay focused with task modals:** Initiate multiple tasks seamlessly through a new modal option, allowing you to keep your context and workflow intact. [Learn more](https://jules.google/docs/tasks-repos/) about kicking off tasks.

**Adjustable code panel:** Customize your workspace by adjusting the width of the code panel to your preferred viewing experience.

[Check out the docs](https://jules.google/docs/code/) to learn more about how to download code that Jules writes.

___

## 2025-05-30: A faster, smoother and more reliable Jules

---
title: "A faster, smoother and more reliable Jules"
pubDate: "2025-05-30"
description: "This week, our focus has been on improving reliability, fixing our GitHub integration, and scaling capacity."
---
This week, our focus has been on improving reliability, fixing our GitHub integration, and scaling capacity.

**Here’s what’s we shipped:**

- Updated our limits to 60 tasks per day, 5 concurrent.
- We substantially improved the reliability of the GitHub sync. Export to GitHub should also be fixed on previously created tasks.
- We’ve decreased the number of failure cases by 2/3

Learn more [about usage limits.](./../usage-limits)

___

## 2025-05-22: Improving Stablity

---
title: "Improving Stablity"
pubDate: "2025-05-22"
description: "We’ve been heads down improving stability and fixing bugs—big and small—to make Jules faster, smoother, and more reliable for you."
---
We’ve been heads down improving stability and fixing bugs—big and small—to make Jules faster, smoother, and more reliable for you.

**Here’s what’s fixed:**

- Upgraded our queuing system and added more compute to reduce wait times during peak usage
- Publish Branch button is now part of the summary UI in the activity feed so it's easier to find
- Bug vixes for task status and mobile

[Learn more](https://jules.google.com/docs/code/#pushing-to-github) about how to publish a branch on GitHub.

___

## 2025-05-19: Jules is here

---
title: "Jules is here"
pubDate: "2025-05-19"
description: "Today, we're launching Jules, a new AI coding agent."
image: "jules-changelog-og-image.png"
---
![Jules dashboard](../../../public/jules-changelog-og-image.png)


Today, we're launching <a href="https://jules.google.com" target="_blank" rel="noopener">**Jules,**</a> a new AI coding agent.

Jules helps you move faster by working autonomously on tasks in your GitHub repo. It can fix bugs, update dependencies, migrate code, and add new features.

Once you give Jules a task, it spins up a fresh dev environment in a VM, installs dependencies, writes tests, makes the changes, runs the tests, and opens a pull request. Jules shows its work as it makes progress, so you never have to guess what code it's writing, or what it's thinking.

**What Jules can do today**
- Fix bugs with test verified patches
- Handle version bumps and dependency upgrades
- Perform scoped code transformations
- Migrate code across languages or frameworks
- Ship isolated, scoped, features
- Open PRs with runnable code and test results

[Get started with the Jules documentation](/), and visit <a href="https://jules.google.com" target="_blank" rel="noopener">jules.google.com</a> to run your first Jules task.