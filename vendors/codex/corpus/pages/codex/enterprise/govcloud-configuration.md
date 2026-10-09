# Bedrock GovCloud configuration

> For the complete documentation index, see [llms.txt](https://learn.chatgpt.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

This guide covers security settings for running Codex with AWS GovCloud in API mode. Review these settings before authorizing sensitive workflows.

[Verification checklist](#4-verify-the-deployment) · [Capability reference](#reference-bedrock-capability-restrictions) · [Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)

This guide isn't legal advice and does not grant an authorization to operate
  (ATO). Review the final configuration and selected AWS services with your
  security and authorizing officials against agency security policies,
  applicable data handling requirements, your system security plan, endpoint
  controls, and data-flow documentation.

## Shared responsibility

AWS and your organization share responsibility for securing the cloud deployment. Review the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) and the selected services' documentation to identify provider controls and your responsibilities. Your agency is responsible for authorizing its system's use of those services.

For a supported deployment, Codex sends inference requests to the reviewed Amazon Bedrock endpoint using AWS authentication. ChatGPT workspace requirements and RBAC don't apply to this API-mode path. Configure AWS identity, service access, and the workstation where Codex runs.

Your workstation configuration, including its Codex TOML policy files, governs local file access, command execution, network access, plugins, MCP tools, and browser capabilities. You're responsible for securing workstations, credentials, repositories, local records, and any enabled third-party services. Assign owners for device policy, network controls, updates, and deployment validation.

AWS GovCloud and these settings alone don't establish that your complete workflow meets agency requirements. Review the exact services, models, Regions, destinations, and data flows in your deployment, and document your customer responsibilities in the system security plan.

## Before you begin

Confirm GovCloud support for your version of Codex.

| Prepare            | What you need                                                                                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS access         | Approved account, IAM identity, and credential mechanism; permitted model, GovCloud Region, and endpoint.                                                                    |
| Deployment package | Supported desktop and bundled app-server release, reviewed Bedrock requirements policy, approved authentication/storage/operational destinations, and rollback instructions. |
| Device management  | Access to system configuration or MDM, with reviewed application/device and agent-command network policies.                                                                  |

## 1. Prepare AWS access

Select the approved AWS account and IAM identity, with access to the selected model and Region. Provision credentials through your organization’s approved mechanism. Keep credentials out of TOML.

For a named profile, protect its configuration, credential source, and credential helper from task writes.





## 2. Deploy device requirements

Deploy the reviewed Bedrock `requirements.toml` through system configuration or MDM before app launch or authentication. API-mode sessions do not receive ChatGPT workspace requirements or RBAC.

Use the complete requirements below as the baseline for your supported Bedrock deployment. Review the [capability reference](#reference-bedrock-capability-restrictions), local skills, and command access for the approved workflow.

Follow [Managed configuration](https://learn.chatgpt.com/docs/enterprise/managed-configuration) for system-file locations and MDM delivery. Protect the managed policy and verify its effective settings on the execution host in [step 4](#4-verify-the-deployment).

### Recommended `requirements.toml`

This configuration intentionally restricts features. It's recommended for GovCloud unless your organization enforces other restrictions. See the [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference) for details on each setting.

The final `[windows]` table applies only to Windows. Confirm support for `sandbox_private_desktop` in your approved runtime.

requirements.toml

```toml
allowed_login_methods = ["api"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
allowed_approvals_reviewers = ["user"]
allowed_approval_policies = [
  { granular = { sandbox_approval = false, rules = true, mcp_elicitations = false, request_permissions = false, skill_approval = true } },
]
allowed_web_search_modes = ["disabled", "cached"]
allow_browser_and_computer_use = false
allow_appshots = false
allow_remote_control = false
allow_login_shell = false
allow_managed_hooks_only = true
check_for_update_on_startup = false
mcp_servers = {}

[feedback]
enabled = false

[features]
network_proxy = true
in_app_chat = false
in_app_dictation = false
in_app_browser = false
browser_use = false
browser_use_external = false
browser_use_full_cdp_access = false
computer_use = false
in_app_updates = false
image_generation = false
memories = false
chronicle = false
external_agent_memory_import = false
guardian_approval = false
guardianv2 = false
guardian_ext = false
apps = false
enable_mcp_apps = false
plugins = false
remote_plugin = false
plugin_sharing = false
recommended_plugins = false
skill_mcp_dependency_install = false
skill_search = false
workspace_dependencies = false
hooks = false
standalone_web_search = false

[experimental_network]
enabled = true
managed_allowed_domains_only = true
domains = {}
unix_sockets = {}
allow_upstream_proxy = false
dangerously_allow_non_loopback_proxy = false
dangerously_allow_all_unix_sockets = false
allow_local_binding = false

# Application destinations

[application.network]
enabled = true

[application.network.domains]
"bedrock-mantle.us-gov-west-1.api.aws" = "allow"

# OpenAI / ChatGPT, including auth and telemetry.

"api.openai.com" = "deny"
"chat.openai.com" = "deny"
"chatgpt.com" = "deny"
"ab.chatgpt.com" = "deny"
"platform.openai.com" = "deny"
"auth.openai.com" = "deny"

# FedRAMP OpenAI endpoints are also outside this Bedrock profile.

"gov.api.openai.com" = "deny"
"gov.chatgpt.com" = "deny"
"sdfedpreastus2.oaiusercontent.com" = "deny"

# Crash reporting and distribution.

"o33249.ingest.us.sentry.io" = "deny"
"persistent.oaistatic.com" = "deny"
"oaisidekickupdates.blob.core.windows.net" = "deny"

# Windows only

[windows]
allowed_sandbox_implementations = ["elevated"]
sandbox_private_desktop = true
```






## 3. Configure provider routing and network controls

Set the provider, model, Region, and endpoint in `config.toml` or managed defaults, separately from `requirements.toml`. Users can change provider defaults unless managed policy constrains them.

### Recommended `config.toml`

For a confirmed Mantle deployment in `us-gov-west-1`, replace the model ID and profile with approved values. If the approved endpoint or Region differs, update the URL, Region, and network policy together.

These defaults set the inference route, match the managed approval policy, and turn off optional diagnostics and data sharing. Users can change defaults within the managed requirements. Keep AWS credentials outside the TOML file. The final `[windows]` table applies only to Windows and must match your approved runtime.

config.toml

```toml
model = "REPLACE_WITH_APPROVED_MODEL_ID"
model_provider = "amazon-bedrock"
forced_login_method = "api"
approval_policy = { granular = { sandbox_approval = false, rules = true, mcp_elicitations = false, request_permissions = false, skill_approval = true } }
approvals_reviewer = "user"
sandbox_mode = "workspace-write"
web_search = "cached"
allow_login_shell = false
check_for_update_on_startup = false

[model_providers.amazon-bedrock]
base_url = "https://bedrock-mantle.us-gov-west-1.api.aws/openai/v1"
wire_api = "responses"
requires_openai_auth = false
supports_websockets = false
supports_standalone_web_search = false

[model_providers.amazon-bedrock.aws]
region = "us-gov-west-1"
profile = "codex-il5"

[sandbox_workspace_write]
network_access = false

[features]
network_proxy = true

[analytics]
enabled = false

[feedback]
enabled = false

[otel]
exporter = "none"
trace_exporter = "none"
metrics_exporter = "none"
log_user_prompt = false

[memories]
generate_memories = false
use_memories = false

[skills.bundled]
enabled = false

[apps._default]
enabled = false

# Windows only

[windows]
sandbox = "elevated"
```


AWS authentication is still required when `requires_openai_auth = false`. Bedrock Runtime and bearer-token gateways need their own approved provider and authentication configuration; do not reuse this Mantle URL or signing service.

### Apply network controls

Apply the reviewed application and device network policies, plus the separate policy for agent commands. Cover inference, credential acquisition and refresh, telemetry, storage, and updates. Routing inference through Bedrock doesn't make all desktop traffic AWS-only.

Application network policy covers supported application and bundled app-server requests. It's separate from agent-sandbox controls and isn't an operating-system firewall. Native updater traffic, Git, SSH, external apps, credential helpers, and subprocess networking require separate controls.

The example selects cached search in `us-gov-west-1`. Check regional availability in the [AWS Bedrock web search documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/web-search.html), and use cached search only when the deployment owner approves the service. Otherwise, set `web_search = "disabled"`.





## 4. Verify the deployment

1. Restart the app. On the execution host, confirm effective requirements, AWS identity, provider, model, Region, and endpoint.

1. Run an approved workflow with example data.

1. Confirm required capability restrictions take effect. Test conflicting user settings, invalid or expired credentials, and routing failures; content must not fall back to an unapproved destination.

Record the desktop and app-server versions, effective configuration, results, and rollback procedure. Resolve failed or blocked checks before expanding access.

## Troubleshoot common problems

| Problem                             | What to check                                                                                                                     |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| GovCloud endpoint is unsupported    | Confirm the exact desktop/app-server release, endpoint, and model with OpenAI. Changing the URL alone does not establish support. |
| Wrong AWS identity is used          | Inspect the effective credential source and named profile. Check whether a Bedrock API key takes precedence over the profile.     |
| Capability restrictions are missing | Inspect the full effective requirements after restart. The API-only sign-in setting does not apply the capability policy.         |





## Reference: Bedrock capability restrictions

These settings describe the initial Bedrock deployment profile. Apply the complete policy supplied for your supported release, including AWS network controls. Local automation and real-time voice require additional controls: `in_app_local_automation` and `realtime_conversation` are not set in the baseline above. Review these restrictions for your deployment.

The values below are managed requirements, not user defaults. Setting a feature to `true` does not bypass account, workspace, provider, or operating-system restrictions. Omitting a requirement leaves normal configuration and availability checks in place.

| Capability                                       | Policy setting                                                                                 | Behavior in this profile                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT conversations and Quick Chat             | `[features]` `in_app_chat = false`                                                             | `false` hides the ChatGPT conversation and Quick Chat interfaces. This setting doesn't stop existing cloud tasks or disable ChatGPT Voice.                                                                                                                                                                                                                  |
| Local automation                                 | `[features]` `in_app_local_automation = false`                                                 | `false` prevents local scheduled tasks from starting, including after restart. `true` permits local scheduling when otherwise supported. Cloud schedules are handled by separate controls.                                                                                                                                                                  |
| Dictation, transcription, and real-time voice    | `in_app_dictation = false`; `realtime_conversation = false`                                    | `in_app_dictation` controls speech-to-text input in the desktop app: `false` disables it, while `true` permits it when dictation available. `realtime_conversation` controls `/voice` in Codex CLI. Setting it to `false` does not provide a blanket block on desktop ChatGPT Voice or app-server voice sessions.                                           |
| In-app browser and browser automation            | `in_app_browser`, `browser_use`, `browser_use_external`, `browser_use_full_cdp_access = false` | `in_app_browser` controls the browser pane available within the app. `browser_use` lets the agent browse and `browser_use_external` extends that to signed-in browser sessions. `browser_use_full_cdp_access` permits full browser debugging. Setting each to `false` blocks that path; `true` still requires the other feature, site, and approval checks. |
| Computer control, Appshots, and computer history | `computer_use = false`; top-level `allow_appshots = false`; `chronicle = false`                | `computer_use = false` blocks native-app control, `allow_appshots = false` blocks capture of window images and text. `true` permits each subject to its other controls. `chronicle = false` is used to stop Computer History collection.                                                                                                                    |
| Cross-session memory                             | `memories = false`; `external_agent_memory_import = false`                                     | `memories = false` disables generating and using local memories across chats. `true` permits both, subject to `memories.generate_memories` and `memories.use_memories`. `external_agent_memory_import = false` also blocks memory imports from other coding agents, even if local memories are enabled.                                                     |
| Image generation                                 | `image_generation = false`                                                                     | `false` disables the built-in image-generation tool; `true` makes it available when the client, model, and provider support it. This switch doesn't disable image inputs or access to existing image files; validate those workflows in [step 4](#4-verify-the-deployment).                                                                                 |
| Web search                                       | Follow the approved deployment's web-search policy.                                            | `cached` uses the search cache; `disabled` removes the web-search tool. `live` permits live web access, while `indexed` gates external access through the search index. The requirements above allow only `cached` or `disabled`. Confirm provider support and approved destinations in [step 3](#3-configure-provider-routing-and-network-controls).       |
| Apps, plugins, MCP, and automatic downloads      | `apps = false`; `plugins = false`; explicit empty `[mcp_servers]`                              | `false` turns apps and plugins off by default. An empty `mcp_servers` allowlist blocks all configured MCP servers. Enable based on organization-specific requirements and security posture.                                                                                                                                                                 |
| Automatic approval                               | `allowed_approvals_reviewers = ["user"]`; `guardian_approval = false`; `guardianv2 = false`    | `["user"]` restricts approval review to the user. Allowing `auto_review` and the Guardian features would permit automatic review where supported. The reviewer setting controls who reviews requests and `approval_policy` still determines which actions require approval.                                                                                 |
| Device remote control                            | top-level `allow_remote_control = false`                                                       | `false` blocks device remote control. `true` or an omitted requirement allows normal remote-control setup where supported; neither value establishes a connection by itself.                                                                                                                                                                                |

### Additional deployment controls

| Area                       | Required control                                                                                                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Cloud and remote workflows | Keep cloud execution and schedules, SSH, sharing, Library persistence, hosted project knowledge, and network-delivered notifications unavailable. Enforce these separately; individual feature flags do not cover every entry point. |
| Telemetry                  | Review analytics, feedback, OpenTelemetry, crash reports, and background traffic independently. `feedback.enabled = false` does not disable every telemetry channel.                                                                 |
| App distribution           | For customer-controlled distribution of app updates, set `in_app_updates = false` under `[features]` where supported, then restart. Manage external packages, patching, revocation, rollback, and supported versions separately.     |