> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manus Flex

> Run Manus with your own API key from a supported inference provider. Learn how to connect a provider, choose a model, and see who bills each cost.

## What it is

**Manus Flex** lets you run Manus with your own API key from a supported inference provider. You choose the provider, the model, and the effort level. Manus still plans the work, uses tools, and runs tasks in the same projects, automations, and execution environments.

Flex is for users who already have an account, credits, or a contract with an inference provider. With Flex, you can use that provider relationship inside Manus.

> [!NOTE]
>
> Manus Flex is in beta. Third-party model performance may vary, and Manus does not guarantee it.

***

## How to use it

### Connect your provider

1. Open the **mode menu** in the top-left corner of the workspace. The menu shows your current mode, for example **Manus 2.0**.
2. Select **Manus Flex**.
3. In **Provider**, select your inference provider.
4. In **API key**, paste your API key.
5. Read the confirmation message and confirm. The message explains which costs your provider bills and which costs use Manus credits.

### Choose your model and effort level

1. Open **Manage your Flex models** from the mode menu. *(Exact entry point unverified.)*
2. In **Primary model**, select the model that runs your main work. The list depends on your provider.
3. In **Effort**, select a level. A higher level can improve quality, but it is slower and uses more of your provider's usage.
4. Optional: turn on **Use lightweight model for side tasks** to send smaller tasks to a lighter model. *(Behavior unverified.)*

When Flex is active, the mode menu shows Flex and your model, for example **Manus Flex · \[model name]**.

### Change your API key or provider

1. Open **Manage your Flex models**.
2. Select **Change API key**.
3. Enter the new key, or select a different provider and enter its key.

### Switch back to standard Manus

1. Open the mode menu in the top-left corner.
2. Select a standard Manus mode, for example **Manus 2.0 Max**, **Manus 2.0**, or **Manus 2.0 Lite**.

Your new tasks then use Manus models and Manus credits again.

***

## What you need to know

### Supported providers

Manus Flex works with these providers:

* OpenAI
* Anthropic
* Google AI Studio
* xAI
* Meta
* OpenRouter
* Fireworks
* Modal

![Manus Flex setup window with the Provider list open, showing OpenAI, Anthropic, Google AI Studio, xAI, Meta, OpenRouter, Fireworks, and Modal](https://mintcdn.com/docs-manus/Ej49R8O1iLGCaWcb/images/manus-flex-providers.png?fit=max\&auto=format\&n=Ej49R8O1iLGCaWcb\&q=85\&s=3bf13a0787b0cb5409953548a273a3c6)

The Provider list in the Manus Flex setup window.

OpenRouter, Fireworks, and Modal are the first partners in the **Flex Inference Partner Program**. Through them, you can use models from many model families.

### Who pays for what

Flex splits the cost of a task into two parts:

| Cost | Who bills you |
| :- | :- |
| **Model usage** (the language model that runs the agent) | Your inference provider, through your API key |
| **Cloud sandbox** (temporary) | Covered by Manus at no additional cost |
| **Images, videos, Cloud Computer, web app hosting, and other paid features** | Manus credits |

> [!WARNING]
>
> Flex does not replace your Manus credits. Media generation with [built-in models](https://manus.im/docs/models/built-in-models.md) and other paid features still use Manus credits. Keep enough credits on your account.

### What stays the same

* **Your workspace:** Projects, files, automations, and connectors work as before.
* **The agent:** Manus still plans the task, calls tools, and runs work in its execution environments.
* **Built-in models:** Video, image, audio, and 3D generation still use the Manus built-in models, not your provider.

### What depends on your provider

* **Model list:** The models in **Primary model** come from your provider. Different providers show different models.
* **Rate limits and quotas:** Your provider's limits apply. If your key reaches a limit or runs out of balance, tasks can stop or fail. *(Error behavior unverified.)*
* **Quality and speed:** Results depend on the model and effort level you choose. Manus does not guarantee third-party model performance.

***

## Tips

* **Use a dedicated API key.** Create a separate key for Manus. Then you can track usage and revoke the key without affecting your other apps.
* **Set a spending limit with your provider.** Agent tasks can run many steps. A limit in your provider's dashboard protects you from unexpected costs.
* **Start with a medium effort level.** Compare the quality and cost on a few tasks, then raise or lower the effort level.
* **Use OpenRouter to compare models.** One OpenRouter key gives you access to models from several model families, so you can test them without new keys.
* **Test on a real task first.** Run one of your usual tasks with Flex and compare it with a standard Manus mode before you switch your automations.
* **Switch modes for each task.** Use Flex for tasks where your own model fits best, and a standard Manus mode for everything else.

***

## FAQ

> [accordion] Do I still need Manus credits if I use Flex?
>
> Yes. Your provider bills model usage. Images, videos, Cloud Computer, web app hosting, and other paid features still use Manus credits.

> [accordion] Which providers can I connect?
>
> OpenAI, Anthropic, Google AI Studio, xAI, Meta, OpenRouter, Fireworks, and Modal.

> [accordion] Can I use Flex for image or video generation?
>
> No. Flex connects the language model that runs the agent. Image, video, audio, and 3D generation use the [built-in models](https://manus.im/docs/models/built-in-models.md) and Manus credits.

> [accordion] Can I connect a custom endpoint or a self-hosted model?
>
> The setup form has fields for a provider and an API key only. It does not have a custom endpoint field. To use open models, connect a supported provider that hosts them, such as Modal.

> [accordion] Do my projects and automations work with Flex?
>
> Yes. Flex uses the same projects, tools, execution environments, and automations as standard Manus.

> [accordion] How do I stop using Flex?
>
> Open the mode menu in the top-left corner and select a standard Manus mode, such as Manus 2.0.

> [accordion] Is Flex available on every plan?
>
> Plan availability is not yet confirmed. *(Unverified.)* See [Plans and Pricing](https://manus.im/docs/introduction/plans.md).

***

Further reading: [Introducing Manus Flex](https://manus.im/blog/introducing-manus-flex)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.