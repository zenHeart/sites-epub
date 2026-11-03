> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Parallel Tasks

> Ask Manus to split your work into separate tasks and manage them from one main task. Start in a Project so that every task shares the same context.

## What it is

With **Parallel Tasks**, Manus starts separate tasks for you. You describe a goal with several parts, and Manus creates one task for each part. All tasks run at the same time.

Manus does not put these tasks in a Project for you. The best practice is to create a **Project** first and start the work there. The Project holds the key context: instructions, files, skills, connectors and, if you have one, your website. Every task in the Project starts from that context, so each new task builds on the work before it.

The task where you make the request is the **main task**. It stays in charge of the work. From the main task, Manus can check progress, read each task's result and send changes to one task or to all of them.

![Diagram: your request goes to a main task inside a Project. The main task starts four separate tasks, each with its own chat and result, and reads their results.](https://mintcdn.com/docs-manus/H5Hp5UOG6qOCJV7q/images/parallel-tasks-overview.png?fit=max\&auto=format\&n=H5Hp5UOG6qOCJV7q\&q=85\&s=843d25c2a95c0f7e8db6e41fd1073ec0)

Each task has its own chat and its own result. Feedback that you give in one task stays in that task, so a change to one deliverable does not change the others.

**Example:** You ask for a launch kit with a blog post, an email, release notes and social posts. Manus starts four tasks in your launch Project, one for each asset. You review each draft in its own task. Then you return to the main task to check that all four drafts use the same facts.

Parallel Tasks works for any type of work, such as documents, research, slides and websites. To let several tasks edit the same website, see [Edit in New Task](https://manus.im/docs/website-builder/edit-in-new-task.md).

Parallel Tasks is for people who move several pieces of work forward at once, such as product managers, founders, content leads and agencies. If you ask one question at a time, one task is enough.

### When to use Parallel Tasks, Branch, Wide Research or one task

| | One task | Wide Research | Branch | Parallel Tasks |
| :- | :- | :- | :- | :- |
| **What you get** | One chat and one result | One combined result, such as a table or report | A new task that copies the chat up to one reply | Several new tasks, each with its own result |
| **What the new task starts with** | Not applicable | Not applicable | The full chat history and files up to that reply | A short brief from the main task, plus the Project context if you work in a Project |
| **Who starts it** | You | Manus, inside one task | You, from the branch icon below a reply | Manus, when you ask for separate tasks |
| **Best for** | One question or one deliverable | Many similar items in one output | Several outputs from the same conversation | Several deliverables that you review and edit one by one |

## How to use it

### Step 1: Create a Project that holds the shared context (recommended)

Parallel Tasks works without a Project, but each task then starts with only its brief. A Project gives every task the same starting point, and it keeps all tasks in one place in the sidebar.

1. In the sidebar, click the **+** icon next to **Projects**.
2. Enter a clear name, for example **Q3 launch kit**.
3. Write the **master instruction**. Include every rule that all tasks must follow, such as audience, tone, format and where to save results.
4. Upload the **knowledge base** files that every task needs, such as a product fact sheet or a style guide.
5. Add the **connectors** and **skills** that the tasks must use. Sign in to each connector first. Adding a connector to a Project does not sign in to it for you.
6. If the work involves a website, keep the website in the same Project. Build it in a task inside the Project, or move the task that built it into the Project.

For more information, see [Projects](https://manus.im/docs/features/projects.md).

### Step 2: Ask Manus to start separate tasks

1. Open a new task inside the Project. This task becomes your main task.
2. Ask Manus to start a **separate task in this Project** for each part of the work. Manus works in the current task by default, so you must ask for separate tasks.
3. Ask Manus to give each task a short brief. A new task does not see the chat history of the main task.
4. Ask Manus to return one link per task.

**Example request:**

```text theme={null}
Start a separate task in this Project for each of these four launch assets.
Give each task a self-contained brief with the goal, the audience and the key facts.
Do not write the drafts here.

1. Launch blog post
2. Announcement email
3. Release notes
4. Three LinkedIn posts

When the tasks have started, give me a list with one link per task.
```

If Manus needs API access in this chat, it shows the card **Allow these actions?** Click **Allow in this task**. Manus can renew this access in the same chat without asking again.

### Step 3: Review and edit each task on its own

1. Open a task from its link, or from the Project in the sidebar.
2. Review the result in that task.
3. Give feedback in that task only. For example, in the email task: "Shorten the subject line to six words."

Each task changes only its own result. You can work in several tasks at the same time.

### Step 4: Manage all tasks from the main task

Return to the main task to manage all tasks from one place.

| Goal | Request to the main task |
| :- | :- |
| Check progress | "Check the four tasks and tell me which ones are finished." |
| Check consistency | "Read all four drafts. Flag claims that conflict with each other or with the fact sheet." |
| Send one change to every task | "Send this message to all four tasks: use 'Start your free trial' as the CTA." |
| Change a rule for future work | "Update the Project instruction: do not use exclamation marks." |

### Run several tasks on one website

To let several tasks edit the same website or app, use **Edit in New Task**. Each task edits the same project, with one shared version history, database and published site.

1. Open the website dashboard, the Library item or the Project website card.
2. Click **Edit in new task**.
3. Describe the change that this task must make, then send the message.

You can also ask the main task to start the website tasks for you. For setup details, syncing, conflicts and limits, see [Edit in New Task](https://manus.im/docs/website-builder/edit-in-new-task.md).

### Example ways to split work

| Work type | How to split the work |
| :- | :- |
| **Websites and apps** | One task per area: styles, page content, a new feature, bug fixes. All tasks edit the same website through [Edit in New Task](https://manus.im/docs/website-builder/edit-in-new-task.md). |
| **Documents and content** | One task per deliverable: blog posts, PRD sections, release notes, emails. The Project keeps the voice and facts the same. |
| **Research** | One task per question or market. Each task saves its result to a shared place, such as Google Drive. The main task compares the results. |
| **Slides** | One task per deck or per audience version. The Project holds the brand guide and the source material. |
| **Agents and support desks** | One task per conversation, customer or review. The main task stays free to answer quick questions. |

## What you need to know

* **Manus starts separate tasks when you ask.** By default, Manus does the work in the current task. Ask for separate tasks in your request. For websites, Manus can also suggest a new task, and you choose whether to start it.
* **Manus does not create a Project for you.** If you do not set up a Project, the new tasks are not grouped together and do not share instructions, files or connectors. Start the main task inside a Project, and ask Manus to create the tasks in that Project.
* **New tasks do not see the chat history.** Each new task starts with the brief that it receives, plus the Project context if you work in a Project. Put rules that all tasks need in the Project, not only in the main task.
* **Project updates reach tasks at different times.** Instruction updates apply the next time you send a message in a task. File updates apply only to tasks that you create after the update.
* **Each task uses credits.** Several tasks can use more credits than one task. API usage in the main task can also use credits.
* **Action confirmations happen in each task.** If a task needs your approval, for example before it sends an email, open that task to approve it. The main task cannot approve actions for another task.
* **Tasks on the same computer can share files.** Tasks that run on the same device and in the same folder see the same files. Manus does not create separate copies automatically. Give each task its own file or folder.
* **Tasks on one website share its code, database and published site.** Code changes merge automatically, but database changes have no conflict protection. For details, see [Edit in New Task](https://manus.im/docs/website-builder/edit-in-new-task.md).
* **Tasks stay private.** Project collaborators see only the tasks that they created. To share a task, invite people to that task.

## Tips

* **Write shared rules once.** Put tone, format, facts and save locations in the Project instruction and files. Then each task follows them without extra setup.
* **Let each round of tasks build on the last.** Save finished results, such as a final fact sheet or approved copy, to the Project files. Tasks that you start after the update read those files, so the next round starts from the approved work.
* **Keep the website in the Project.** If several tasks change one website, keep the website and those tasks in the same Project. Each task then has the same context about the website.
* **Ask for a self-contained brief per task.** Each brief needs the goal, the audience, the key facts and the expected output. A brief must not refer to "the chat above."
* **Decide when to start a new task.**
  * Quick questions: stay in the main task.
  * Separate deliverables: start one task for each.
  * Long research (more than about 10 minutes): start a separate task so that the main task stays free.
  * Follow-ups on one deliverable: send them to that deliverable's task.
* **Split website work by area.** Give each task a different area, such as styles, content or one feature, and change the database from one task at a time.
* **Use the main task as the final check.** Ask the main task to verify key numbers and claims from each task before you share the results.
* **Keep shared notes in files.** Save notes, decisions and work in progress to Project files or a shared folder. Every task can read files. No task can read another task's chat unless the main task reads it for you.
* **Turn feedback into Project rules.** After a review, add the lessons to the Project instruction. The next set of tasks starts from better rules.

## FAQ

> [accordion] Does Manus start separate tasks on its own?
>
> No. Manus starts separate tasks when you ask for them. For websites, Manus can suggest starting a new task, and you click **Start in new task** or **Not now**.

> [accordion] Do I need a Project to use Parallel Tasks?
>
> No, but we recommend it. Without a Project, each new task starts with only its brief, and the tasks are not grouped in the sidebar. With a Project, every task shares the same instructions, files, connectors and website, and you find all tasks in one place.

> [accordion] How is Parallel Tasks different from Wide Research?
>
> Wide Research runs many agents inside one task and combines their work into one result, such as a table or a report. Parallel Tasks creates separate tasks that you can open, review and edit one at a time. Use Wide Research for many similar items in one output. Use Parallel Tasks for several deliverables that each need their own review.

> [accordion] How is Parallel Tasks different from Branch?
>
> [Branch](https://manus.im/docs/features/branch.md) copies a task's chat history and files up to one reply into a new task. You start each branch yourself. With Parallel Tasks, Manus starts several new tasks for you. Each new task gets only the Project settings and a short brief, not the chat history. Use Branch when the new work needs the full conversation. Use Parallel Tasks when each piece of work can start from a clear brief.

> [accordion] Can a new task see what I discussed in the main task?
>
> No. A new task starts with the Project settings and the brief from the main task. If you want the main task to use another task's results, ask the main task to read that task.

> [accordion] Can I send the same change to all tasks?
>
> Yes. In the main task, ask Manus to send the message to all tasks. To make a change permanent for future work, update the Project instruction.

> [accordion] Can several tasks edit the same website?
>
> Yes. Use [Edit in New Task](https://manus.im/docs/website-builder/edit-in-new-task.md). All tasks edit the same project and share one published site.

> [accordion] Does Parallel Tasks use more credits?
>
> Each task uses its own credits. Several tasks can use more credits than one task, but they run at the same time instead of one after another.

> [accordion] Can my collaborators see the tasks that Manus starts?
>
> Not by default. Project collaborators see the shared instruction and knowledge base, but they see only their own tasks. To share a task, invite them to that task.

> [accordion] Can I move an existing task into the Project?
>
> Yes. Projects work like folders, so you can move an existing task into a Project. For more information, see [Projects](https://manus.im/docs/features/projects.md).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.