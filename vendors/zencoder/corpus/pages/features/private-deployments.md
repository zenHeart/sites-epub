> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Private Deployments

> Keep Zencoder inside infrastructure you control

<Card title="Custom models enable private deployments" icon="server">
  Custom models are the foundation of a private deployment—wire up your own endpoints with <strong>settings.json</strong>, then apply the additional steps on this page to keep Zencoder entirely inside your boundary.
</Card>

## What Is a Private Deployment?

The standard Zencoder cloud experience is already secure for most teams: code runs ephemerally, data is encrypted in transit and at rest, access is gated by role-based controls, and Zencoder maintains ISO 27001/42001 plus SOC 2 Type II certifications. If you are comfortable with those guarantees, you can keep using the default service without extra configuration.

A private deployment gives you deeper control by running agents, orchestration, and inference on infrastructure you operate. Typical benefits include:

* Full isolation inside your own network perimeter.
* Support for customer-hosted models and runtimes.
* Zero dependency on external endpoints for sensitive workloads.

Private deployments are recommended for regulated industries, strict data-residency mandates, air-gapped environments, and teams with proprietary models they must keep on-premise.

## Configure a Private Deployment

A full private deployment is a layered approach. Follow these steps to keep Zencoder inside infrastructure you manage:

1. **Configure custom models from local or VPC endpoints.** Use the [Custom Models configuration guide](/features/custom-models-configuration) to declare every model you plan to expose to your users. This is how agents call the runtimes that live within your network boundary.
2. **Hide the managed catalog.** Inside `settings.json`, set `"useDefaultProviders": false` so the selector only lists the providers you declared. This prevents accidental routing to Zencoder-hosted models after you stand up custom ones.
   After applying these steps, all interactive chat and agent runs are served by your endpoints.

<Note>
  We are actively building additional controls to make fully-private deployments even more seamless. Stay tuned for updates in the changelog.
</Note>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.