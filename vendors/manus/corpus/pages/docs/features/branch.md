> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Branch

> Branch lets you take any task in a new direction from any Manus reply. The new task keeps everything up to that point, and your original task stays unchanged.

## What it is

**Branch** creates a new task from a point in an existing task. This new task is called a **branch**. It starts with the conversation, files, and instructions from the original task, up to the reply you choose. You do not need to upload files again or repeat your instructions.

Your original task does not change. You can keep working in it while you work in the branch. Each branch has its own copy of the context, so work in one branch does not affect the original task or other branches.

[YouTube video player](https://www.youtube.com/embed/zTgRUw85b9c)

Use Branch when one piece of work leads to several outputs. For example, Manus writes up your meeting notes. From that one reply, you can create three branches: a to-do list for the team, an update for your manager, and a slide outline for next week's review. Each branch focuses on one output, and all three start from the same notes.

## How to use it

### Create a branch

**1. Find the reply**

Open the task that you want to branch. Find the Manus reply that you want to continue from.

**2. Click the branch icon**

Click the **branch icon** in the row below that reply. When a task is complete, the icon also shows next to **Task completed**. The tooltip says **Continue in new task**.

**3. Confirm the first time**

The first time you use Branch, a card titled **Want a different direction?** opens. Click **Continue in new task**. After the first time, one click on the branch icon creates the branch.

**4. Continue in the branch**

Wait for the **New task created** message. Manus opens the new task for you. Send your next message in the branch.

On the Manus iOS and Android apps, tap the branch icon below a reply and confirm. The app opens the new task when it is ready.

### Branch a task that runs on your computer

If the task works with files on your own computer, Manus asks where the branch should work. Select one option:

| Option | What it does | When to use it |
| :- | :- | :- |
| **Continue in this workspace** | The branch uses the same folder and files as the original task. | You want both tasks to work on the same files. |
| **Continue in a new worktree** | Manus creates a separate copy of your Git repository from the latest commit. Uncommitted changes are not copied. | You want the branch to change code without touching the original folder. |

The **new worktree** option is available only when the folder is a Git repository. Your computer must also be connected to Manus and running an up-to-date version of the app.

### Go back to the original task

Each branch shows a **Branched from** divider at the point where the branch starts. The divider includes the name of the original task. Click that name to open the original task.

The branch gets the original task name with **(branch)** at the end. For example, "Q3 market research" becomes "Q3 market research (branch)".

> [!NOTE]
>
> Tip: It helps to rename each branch as soon as they are created

### Create more branches

You can create as many branches as you need:

* **From the same reply:** Repeat the steps above. Each branch is a separate task.
* **From a different reply:** Click the branch icon below any other Manus reply.
* **From a branch:** Branches can have their own branches. Each one keeps the full history before it.

***

## What you need to know

### What the branch keeps

| The branch keeps | The branch does not keep |
| :- | :- |
| The conversation up to and including the reply you selected | Messages that came after the selected reply |
| Files as they were at that reply, including the latest version of each file at that time | Files and file versions created after the selected reply |
| The task's project, instructions, connectors, and model settings | Sharing settings and collaborators |
| | Permissions you approved for Manus to work on your computer |
| | Work that was still in progress at the selected reply |

Edits in a branch apply only to that branch. If you change a file in the branch, the file in the original task stays the same.

### Who can create a branch

Only the owner of a task can create a branch from it. In these cases, the branch icon is gray and you cannot click it:

* **You are a viewer or collaborator on someone else's task.** The tooltip says "Only the task owner can continue from here in a new task."
* **The task is a subtask.** Manus sometimes splits a large job into subtasks. You cannot branch these subtasks. Branch the main task instead.

### Tasks that include a website

Branch cannot copy a website project. If the part of the task you select includes a website, Manus shows **Copy this website instead**. Click **Open settings**, and then use [Make a copy](https://manus.im/docs/website-builder/make-a-copy.md) in the Website settings.

You can still branch from a reply that came before Manus created the website.

### Branching while Manus is working

You can create a branch from an earlier reply while Manus is still working on the task. The original task keeps running. The branch starts in a stopped state and waits for your next message.

If Manus had started a background job that was not finished at the selected reply, the branch does not include that job. Manus can start the job again in the branch if needed.

### Sharing a branch also shares its history

> [!WARNING]
>
> A branch contains the full history from before the branch point. If you share a branch, people with access can see that history and its files. This is true even if you never shared the original task. Check the history before you share a branch.

### Limits

* The task must have at least one message before the reply you select.
* You can create up to 10 branches per minute. If you reach this limit, wait a moment and try again.

### Availability

Branch is available to all users on the Manus web app, the desktop app, and the iOS and Android apps.

***

## Tips

* **Branch at a stable point.** Pick the reply where the shared foundation is complete, such as final meeting notes or a finished research summary. Every branch then starts from good material.
* **Give each branch one job.** One branch per output keeps Manus focused and the results accurate.
* **Compare two approaches.** Create two branches from the same reply and give each one a different instruction. Keep the result you like.
* **Keep a main task as a running log.** Add notes and research to one main task over time. When you need a deliverable, such as a plan, a summary, or a deck, create a branch for it. The main task keeps growing.
* **Rename your branches.** All branches get "(branch)" at the end of the name. Give each branch a clear name so you can find it in your task list.
* **Branch before the website.** If a task later built a website, branch from a reply that came before the website. Use [Make a copy](https://manus.im/docs/website-builder/make-a-copy.md) to duplicate the website itself.

***

## FAQ

> [accordion] Does creating a branch change my original task?
>
> No. The original task stays exactly as it was. The branch is a separate task.

> [accordion] Do I need to upload my files again?
>
> No. The branch includes the files from the original task as they were at the reply you selected.

> [accordion] If I edit a file in the branch, does the original file change?
>
> No. The branch has its own copies of the files. Changes in one task do not affect the other.

> [accordion] Can I create more than one branch from the same reply?
>
> Yes. Each branch is a separate task, so you can try several directions from one point.

> [accordion] Can I branch a branch?
>
> Yes. A branch of a branch keeps the full history from all earlier tasks.

> [accordion] Why is the branch icon gray?
>
> You may not be the task owner, or the task may be a subtask. Hover over the icon to see the reason.

> [accordion] Can I branch a task that built a website?
>
> You can branch from a reply that came before the website. To copy the website itself, use [Make a copy](https://manus.im/docs/website-builder/make-a-copy.md) in the Website settings.

> [accordion] Can I branch a scheduled task or a meeting notes task?
>
> Yes. You can branch these tasks the same way as any other task.

> [accordion] What happens to my branch if I delete the original task?
>
> Your branch keeps its full history and files.

> [accordion] Who can see my branch?
>
> A new branch is private to you, even if the original task was shared. If you share the branch, people with access can also see the history from before the branch point.

To learn more about how teams use Branch, read [Introducing Branch: One Context, Many Parallel Directions](https://manus.im/blog/manus-branch).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.