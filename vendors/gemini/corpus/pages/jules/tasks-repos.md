---
title: "Managing tasks and repos"
description: "How to configure setup scripts for Jules' virtual machines"
---


To start a new task:

1. Click the Jules icon to return to the home screen and a blank prompt input
2. Use the **+** button in the top navigation on the task view
3. From within a specific repo view, click **new task**

You can launch multiple tasks at a time to run them simultaneously. If you are viewing an existing task, or repo page when you kick off a new task, that task will load and begin running in the background. You will have to navigate to the task to check for updates, approve the plan, etc. 

Each task runs in its own virtual machine and maintains its own logs, environment setup, and code changes.

## Pausing or deleting tasks

Sometimes you need to stop Jules mid-task or clean up old runs.

- To **pause** a task: click the **pause**.
- To **delete** a task: hover over the task in the repo view and click the **trash icon**.

> Paused tasks can be resumed later; deleted tasks are removed permanently.

![Pause Task](../../../public/pause.png)
![Delete Task](../../../public/delete1.png)

## Managing repositories

Jules can only access repositories you explicitly allow through GitHub. In the future, Jules will work with more version control systems.

### Selecting a repo

If you've already granted Jules access to all your repos:

- Use the dropdown when starting a task to choose any authorized repo
- Enroll new from the left sidebar
- Search for your repo using the **repo selector**

![Enroll a new repo](../../../public/enrollrepo1.png)

### Granting access to more repos

To give Jules access to more of your repositories:

1. Go to [github.com](https://github.com)
2. Click your profile photo --> **settings**
3. In the left sidebar, click **applications**
4. Find **Google Labs Jules** and click **configure**
5. Under **repository access**, select additional repos
6. Click **save**

You can also authorize new repositories via the **repo selector** in Jules. Open the repo selector and scroll to the bottom to click on **+Add repository**. This will take you to GitHub, where you can select additional repositories to grant access for Jules.