> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit in New Task

> Open an existing website or app in a new task and keep editing the same project. Run several tasks on one website at the same time.

## What it is

**Edit in New Task** opens an existing website or app in a new Manus task. The new task edits the **same** project. It does not create a copy. All tasks that edit the project share one version history, one database, one set of secrets and one published site.

Use Edit in New Task in two situations:

* **Continue work in a clean task.** The original task has a long history, and you want to start the next round of changes with a short, focused context.
* **Edit one website in several tasks at the same time.** For example, one task updates styles, a second task updates page content and a third task adds a feature.

Edit in New Task is the website and app part of [Parallel Tasks](https://manus.im/docs/features/parallel-tasks.md). Parallel Tasks lets one main task start and direct several tasks. Edit in New Task lets those tasks work on the same website.

### How Edit in New Task differs from Make a Copy

| | Edit in New Task | [Make a Copy](https://manus.im/docs/website-builder/make-a-copy.md) |
| :- | :- | :- |
| **Project** | The same project | A new, independent project |
| **Source code** | Shared. Changes from each task go into one version history. | Copied once. Changes do not affect the original. |
| **Database** | Shared. All tasks read and write the same data. | Schema copied. The new database is empty. |
| **Secrets** | Shared | Copied |
| **Published site and domains** | Shared. Publishing from one task updates the live site. | Not copied. The copy starts unpublished. |
| **Chat history** | Not carried over | Not carried over |
| **Best for** | More work on the same website | Experiments, variations and templates |

## How to use it

### Open a website in a new task

You can start Edit in New Task from three places.

**From the website dashboard:**

1. Open the website dashboard.
2. Click **More** (the **...** icon) in the dashboard header.
3. Click **Edit in new task**.

Manus opens a new task with the website attached to the message box.

**From the Library:**

1. Go to your **Library**.
2. Find the website or app.
3. Open the three-dot menu on the item.
4. Click **Edit in new task**.

**From a Project:**

1. Open the Project that contains the website.
2. Find the website card.
3. Open the menu on the card and click **Edit in new task**.

Manus attaches the website to the message box of this Project. The new task inherits the Project instruction, files, skills and connectors.

### Describe the change and send

1. In the new task, describe the change that this task must make. Give a self-contained brief, because the new task does not see the chat history of the original task.
2. Send the message.

Manus opens the website for editing at once. It does not ask you to confirm again.

**Example message:**

```text theme={null}
Update the pricing page only.
Change the Pro plan to $24/month and add a yearly option at $240/year.
Do not change the header, the footer or other pages.
```

### Start a parallel task from a suggestion

After you build or edit a website, Manus can show the card **Want to build your website faster?** For apps, the card says **Want to build your app faster?**

* Click **Start in new task** to open the same project in a new task.
* Click **Not now** to continue in the current task.

### Get the latest changes from other tasks

When another task saves a new version, this task shows a message in the preview:

> You're viewing an older version. This site has new changes in \[task name] — sync to update this preview.

The publish panel can also show: "A new version is available — sync before making more changes."

1. Click **Sync** to load the latest version into this task.
2. To see which task made the change, click the task name in the message.
3. If you click **Dismiss**, you can sync later from **Version history**.

## What you need to know

* **All tasks edit one project.** Changes from every task go into one version history. Each saved version records the task that created it.
* **Code changes merge automatically.** Before each edit, Manus loads the latest code. Before each saved version, Manus places its changes on top of the newest version. If two tasks change the same lines, the agent resolves the conflict. Manus does not overwrite another task's work.
* **Changes from other tasks are intended.** The agent treats changes that it did not make as edits from another task. It does not undo them.
* **The database is shared and has no conflict protection.** Code conflicts are handled, but data is not. If two tasks change the same data or the same tables at the same time, one change can overwrite the other.
* **Publishing applies to the whole website.** If you publish from one task, the website is live for all tasks. You do not need to publish again from each task.
* **One task can edit one website.** If you attach more than one website to a task, only one opens for editing. The others open as read-only references, and Manus does not save changes to them.
* **Only the website owner can use Edit in New Task.** Project collaborators who are not the owner see the message "Only the project owner can edit."
* **The new task does not see the original chat history.** Put the context that the task needs in your message or in the Project.
* **Each task uses credits.** Several tasks on one website can use more credits than one task.

## Tips

* **Give each task a different goal.** For example, one task for styles, one for content and one for a single feature. Separate areas cause fewer conflicts in the same files.
* **Change the database from one task at a time.** Plan schema changes and data imports in one task. Tell the other tasks not to change the database.
* **Sync before you review.** Click **Sync** before you check the preview, so that you see the changes from all tasks.
* **Use a Project for shared rules.** Start Edit in New Task from the Project website card. Then every task follows the same brand, copy and code rules.
* **Use the main task to coordinate.** Ask the main task to check which tasks are finished and to review the combined result. For more information, see [Parallel Tasks](https://manus.im/docs/features/parallel-tasks.md).
* **Use Make a Copy for risky experiments.** If you do not want a change to reach the live website, make a copy instead.

## FAQ

> [accordion] Does Edit in New Task create a copy of my website?
>
> No. The new task edits the same project. To create an independent project, use [Make a Copy](https://manus.im/docs/website-builder/make-a-copy.md).

> [accordion] What happens if two tasks edit the same file?
>
> Manus combines the changes when it saves each version. If the changes conflict, the agent resolves the conflict and does not overwrite the other task's work.

> [accordion] Why does my preview show an older version?
>
> Another task saved a newer version. Click **Sync** in the preview message to load the latest version.

> [accordion] Do I need to publish from every task?
>
> No. The publish status belongs to the website, not to the task. If you publish from one task, the website is live everywhere.

> [accordion] Is my database data safe when several tasks run?
>
> All tasks use the same database, and Manus does not detect data conflicts. Change shared data or tables from one task at a time.

> [accordion] Can my collaborators use Edit in New Task on my website?
>
> No. Only the website owner can open the website in a new task.

> [accordion] Does Edit in New Task work for mobile apps?
>
> Yes. Edit in New Task works for websites and mobile apps that you build with Manus. Older versions of the Manus mobile app do not show the option. Update the app to see it.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.