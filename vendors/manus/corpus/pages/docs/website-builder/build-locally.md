> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build locally in Manus Studio

> Build websites, web apps, mobile apps, and games in a folder on your own computer with Manus Studio. Choose Manus-managed services or a plain local project.

## What it is

**Build locally** lets Manus build a website, web app, mobile app, or game in a folder on your own computer. You work in **Manus Studio**, the Manus desktop app for macOS (Apple Silicon) and Windows. Manus writes the code, runs the project, and shows a live preview. It uses the files, folders, and tools that are already on your computer. To learn what Manus Studio can do on your computer, see [Manus Studio](https://manus.im/docs/features/desktop.md).

Use this feature in these cases:

* Your project already lives on your computer.
* You want to keep your own Git workflow.
* You want to use your own tools next to Manus.

You can also use the same workflow on a [Cloud Computer](https://help.manus.im/en/articles/15392111-what-is-the-cloud-computer). In that case, the project folder is on the Cloud Computer instead of your own machine.

For each website or mobile app, you choose one of two project types:

| Term | What it means |
| :- | :- |
| **Manus-managed project** | The project connects to Manus services, such as hosting, a database, user login, AI features, version history, and publishing. You can also continue the project in Manus on the web. |
| **Plain local project** | An ordinary project on your computer. You use your own tools and services. Manus does not set up hosting, publishing, or other Manus services. |
| **Manus version history** | The list of saved versions that Manus keeps for a Manus-managed project. It is separate from your own Git repository. |

The table shows which choices apply to each type of project.

| Project type | Your choices | Where development runs |
| :- | :- | :- |
| **Website or web app** | Manus-managed or plain local | Your computer |
| **Mobile app** | Manus-managed or plain local | Manus-managed: Manus Cloud. Plain local: your computer. |
| **Game** | Always Manus-managed | Your computer |

***

## How to use it

### Set up Manus Studio

**1. Download Manus Studio**

Open [manus.im/desktop](https://manus.im/desktop). Select **macOS (Apple Silicon)** or **Windows**, then run the installer.

**2. Sign in**

Open Manus Studio and sign in with your Manus account. If Manus asks you to update before you use a local folder, install the latest version.

**3. Turn on Work locally and choose the folder**

In the chat box, turn on **Work locally**. Click **Choose a folder** and select the folder where your project lives, or where Manus should create it. See [Manus Studio](https://manus.im/docs/features/desktop.md) for permission modes and folder access.

### Start a new website on your computer

**1. Describe the website and its location**

Start a task in Manus Studio. Describe the website, and tell Manus where to build it on your computer.

**2. Choose a project type**

Manus asks how you want to set up the website. Select **Manus-managed** to use Manus hosting, a database, login, version history, and publishing. Select **plain local** to use only your own tools and services.

**3. Allow code storage if the folder is not empty**

For a Manus-managed project, Manus checks the folder. If it already contains files, Manus shows a **Project code storage** card. The card asks: "Allow Manus to sync your project's code?" Click **Allow and initialize** to continue. If you cancel, Manus does not set up the project.

**4. Review the plan**

Manus presents a plan for the website. Ask for changes before Manus starts to build.

**5. Preview and refine**

Manus runs the website on your computer and opens a live preview in Manus Studio. Describe the changes you want in the same task.

Example prompt:

```text theme={null}
Build a booking website for my yoga studio in a new folder called yoga-site
in my Documents folder. Include a class schedule, a booking form, and a contact page.
```

> [!NOTE]
>
> If you already chose a project type in your prompt, for example "keep this local, no Manus hosting", Manus does not ask again.

### Continue a website that is already on your computer

**1. Point Manus at the folder**

In Manus Studio, tell Manus which project to continue. Give the full folder path if you can.

**2. Confirm the right copy**

Manus looks for Manus websites in that folder and in nearby folders. If Manus finds more than one match, or the match is unclear, it asks which one you mean.

**3. Choose how to connect existing code**

The folder can contain code that is not yet linked to Manus. In that case, Manus asks you to choose Manus-managed or plain local. Manus keeps your existing files and does not apply a starter template over them.

### Add a website to a larger project

You can add a website to a project that is not a website, for example an official site for a game.

1. Tell Manus that you want a separate website inside the larger project. For example: "Add an official website for this game."
2. Manus creates the website in its own subfolder, for example `website/`.
3. Only that subfolder belongs to the website. Manus does not include the rest of the project in website versions.

### Build a mobile app

**1. Describe the app**

In Manus Studio, describe the mobile app that you want to build.

**2. Choose a project type**

Manus asks you to choose before it starts. **Manus-managed** gives you a backend, database, login, AI features, version history, and app builds. **Plain local** keeps development on your computer with your own backend and services.

**3. Confirm the move to Manus Cloud**

A Manus-managed mobile app currently runs in Manus Cloud. If you choose it, Manus moves the task from your computer to Manus Cloud before development starts. Manus tells you about this move before you choose.

> [!WARNING]
>
> Files in your local folder may not move with the task to Manus Cloud. If you have existing code, tell Manus before you choose so that it can plan how to bring the code across.

### Build a game

1. In Manus Studio, describe the game and tell Manus where to build it on your computer.
2. Manus sets up the game as a Manus-managed project. It does not ask you to choose a project type.
3. Continue with the normal Game Dev workflow. See [Game Developer](https://manus.im/docs/features/game-developer.md).

### Save versions and publish a Manus-managed project

**1. Ask Manus to save a version**

When you are happy with a change, ask Manus to save a version. Manus uploads a copy of the code in the website folder to a private, Manus-managed repository. Manus uses this copy only for version history and publishing.

**2. Publish when you are ready**

Ask Manus to publish, or publish as described in [Publishing](https://manus.im/docs/website-builder/publishing.md). Manus asks "Allow Manus to publish?" Choose **Allow once**, or **Always allow for this website** to skip this question next time. Only the project owner can publish a local project. Saving a version does not publish your website by itself, unless you turned on automatic publishing.

> [!NOTE]
>
> A commit in your own Git repository does not create a Manus version and does not publish your website.

### Test Stripe payments in a local project

1. Ask Manus to add payments. Manus sets up Stripe in test mode. See [Payments](https://manus.im/docs/website-builder/payments.md).
2. Test the checkout with the Stripe test card `4242 4242 4242 4242`.
3. For full payment testing, Stripe must send payment events (webhooks) to your app. A preview on your own computer cannot receive these events. Ask Manus to move the project to a temporary cloud sandbox for this test. Manus asks for your approval first.
4. Before you publish for the first time, ask Manus to connect the Stripe webhook from a cloud preview.

### Connect a plain local project to Manus later

1. Open the project folder in Manus Studio.
2. Ask Manus to connect the website to Manus.
3. Manus links the existing folder to a new Manus-managed project. It keeps your source files and does not rebuild the website.

This applies to websites and web apps. To move a plain local mobile app to Manus-managed, Manus moves the task to Manus Cloud and reviews how to bring your code across.

***

## What you need to know

### What runs where

* **The preview runs on your computer.** Manus Studio opens the preview from a local address on your machine. Other devices cannot open this address.
* **Share with others by publishing.** To let other people see the website, publish it, or continue the task in Manus Cloud.
* **Sync before you continue in the cloud.** A new cloud task starts from the latest synced version. Changes that exist only on your computer are not included. Ask Manus to sync first, then select **Continue in a new cloud task**.
* **Only the owner can use local files.** Local files, local publishing, and continuing in a new task are available only to the project owner.
* **Managed mobile apps run in Manus Cloud.** Websites, web apps, and games stay on your computer. Manus-managed mobile apps move to Manus Cloud.

### What Manus uploads

* **Manus-managed projects:** When you save or sync a version, Manus uploads the code in the website folder. It does not upload the rest of a larger project, such as the game around a companion website.
* **Setup alone does not upload code.** Connecting a folder or setting up a Manus-managed project does not upload your code by itself.
* **Choosing Manus-managed does not publish anything.** Your website goes public only when you publish it.
* **Plain local projects:** Manus does not set up Manus services and does not save versions to Manus. You can connect the project to Manus later.

### How Manus works with your Git repository

* **Two separate histories.** Manus keeps its own version history for a Manus-managed project. Your own Git repository and its history stay separate.
* **Your Git setup stays the same.** Manus does not change your remotes, branches, hooks, or credentials. It does not import your Git history.
* **Commits do not copy across.** Your commits do not appear in Manus version history, and Manus versions do not appear as commits in your repository.
* **Shared files.** Both histories track the same files in the folder. When Manus brings in changes from its own history, those changes appear in your Git repository as uncommitted changes.
* **Folders without their own Git repository.** If the website folder is not inside a Git repository, your Git tools show the Manus version history for that folder. To use a separate repository there, ask Manus to set it up. Do not run `git init` in that folder yourself.
* **Manus adds two items to the website folder.** A small project file links the folder to your Manus project. A hidden folder stores the Manus version history. Do not delete either one. Do not commit the hidden folder to your own repository.
* **Git worktrees and branches.** You can commit the small project file to your repository. A new branch or worktree then stays linked to the same Manus project.
* **Cloud projects and GitHub.** For projects that you build in Manus Cloud, see [GitHub Integration](https://manus.im/docs/website-builder/github-integration.md) and [Code Control](https://manus.im/docs/website-builder/code-control.md).

### Current limits

* **Rollback is not available yet for local projects.** You cannot roll back a Manus-managed local project to an earlier saved version. To undo changes, use your own Git history.
* **Full Stripe webhook testing needs a cloud sandbox.** Test-mode checkout works locally. Payment events need a temporary cloud sandbox.
* **Games are always Manus-managed.** A plain local option is not available for games.
* **Managed mobile apps need Manus Cloud.** You cannot develop a Manus-managed mobile app on your own computer.

### Tools on your computer

* **Manus uses the tools you have.** Manus uses the programming languages, package managers, and other tools that are installed on your computer.
* **Project packages install as part of the task.** Manus installs the packages your project needs, using the project's own settings.
* **System changes need your permission.** Before Manus installs or repairs a tool for your whole computer, it explains the change and asks for your permission. It does not use administrator rights without your approval.

### Moving or copying a project folder

* **Move the whole folder.** If you move or rename the whole website folder, the link to your Manus project and its version history stay intact.
* **Copying only the project file does not create a new website.** The copy points to the same Manus project. Ask Manus to set up a new project instead.

### Credits

Tasks that work with your computer use credits at the same rate as equivalent tasks in the cloud. The complexity of the task sets the cost, not the location of the files. See [Understanding Credit Consumption in the Manus Desktop App](https://help.manus.im/en/articles/14134826-understanding-credit-consumption-in-the-manus-desktop-app).

***

## Tips

* **Give Manus the full folder path.** A full path, such as `~/Documents/yoga-site`, helps Manus find the right project the first time.
* **Use a new, empty folder for a new website.** Manus then sets up the project without asking you to confirm code storage.
* **State your project type in the first prompt.** Say "Manus-managed" or "keep this local" to skip the setup question.
* **Choose Manus-managed if you plan to publish with Manus.** You get hosting, version history, and publishing without extra setup.
* **Keep a companion website in its own subfolder.** Version history and uploads then include only the website, not the whole project.
* **Commit your work to Git before large changes.** Rollback is not yet available for Manus-managed local projects, so your own Git history is your safety net.
* **Commit the small project file, not the hidden folder.** Your branches and worktrees then stay linked to the same Manus project.
* **Plan payment testing early.** Ask Manus to set up a temporary cloud sandbox when you are ready to test the full payment flow.
* **Publish to share.** A local preview works only on your computer. Publish the website to send a link to other people.

***

## FAQ

> [accordion] Do I need Manus Studio to build locally?
>
> Yes. Building on your own computer needs Manus Studio for macOS (Apple Silicon) or Windows. Download it from [manus.im/desktop](https://manus.im/desktop). You can also use the same workflow on a Cloud Computer.

> [accordion] What is the difference between a Manus-managed project and a plain local project?
>
> A Manus-managed project connects to Manus services such as hosting, a database, login, version history, and publishing. A plain local project is an ordinary project on your computer. You use your own tools and services, and Manus does not set up hosting or publishing.

> [accordion] Does Manus upload my code?
>
> For a Manus-managed project, Manus uploads the code in the website folder when you save or sync a version. Setting up the project does not upload code by itself. For a plain local project, Manus does not save versions to Manus.

> [accordion] Will Manus change my Git repository?
>
> No. Manus keeps its own version history, separate from your repository. It does not change your remotes, branches, hooks, or credentials. When Manus changes files, those changes appear in your repository as uncommitted changes.

> [accordion] Why did my mobile app task move to the cloud?
>
> A Manus-managed mobile app currently runs in Manus Cloud. Manus tells you this before you choose. To keep the app on your computer, choose plain local development instead.

> [accordion] Why does Manus not ask me to choose a project type for my game?
>
> Games built locally are always Manus-managed. Manus sets up the game with Manus services and continues to the next step.

> [accordion] Can I roll back a local project to an earlier version?
>
> Not yet. Rollback is not available for Manus-managed local projects in this release. Commit to your own Git repository before large changes so that you can restore files yourself.

> [accordion] Can I test Stripe payments on my computer?
>
> You can test the checkout in Stripe test mode. Full testing of payment events (webhooks) needs a temporary cloud sandbox. Ask Manus to set it up. Manus asks for your approval before it moves the project.

> [accordion] Can someone else open my local preview?
>
> No. The preview runs at a local address on your computer. To share the website, publish it or continue the task in Manus Cloud.

> [accordion] Can I connect a plain local website to Manus later?
>
> Yes. Ask Manus to connect the website. Manus links the existing folder to a Manus-managed project and keeps your source files.

> [accordion] Manus asked to install a tool on my computer. Why?
>
> Your project needs a tool that is missing, outdated, or not working on your computer. Manus explains the change and asks for your permission before it installs or repairs a tool for your whole computer.

> [accordion] Does building locally cost more credits?
>
> No. Tasks that work with your computer use credits at the same rate as equivalent tasks in the cloud. See [Plans and Pricing](https://manus.im/docs/introduction/plans.md).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.