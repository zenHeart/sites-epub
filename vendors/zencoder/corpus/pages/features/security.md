> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Security & Privacy

> How Zencoder protects your code, data handling practices, compliance certifications, and enterprise security controls

## Security Overview

Zencoder is built for teams that care about code security. Your code is never used for model training, data is encrypted at every layer, and enterprise controls give administrators full visibility.

<Card title="Trust Center" icon="shield-halved" href="https://trust.zencoder.ai">
  Visit the Zencoder Trust Center for up-to-date certifications, security controls, and compliance documentation.
</Card>

## Data Handling

### What Data Does Zencoder Access?

When you use the Coding Agent, Zencoder processes:

| Data Type | Purpose | Retention |
| - | - | - |
| **Code in active files** | Provide context for agent responses | Not retained after session |
| **Project structure** | Understand file layout and dependencies | Not retained after session |
| **Chat messages** | Process your prompts and generate responses | Retained per your org's settings |
| **Indexed repositories** | Power Multi-Repository Search | Stored encrypted; deletable on demand |
| **Usage metadata** | Analytics dashboard, billing | Retained per data policy |

### What Zencoder Does NOT Do

* **No model training on your code** — Your code is never used to train or fine-tune any AI model
* **No code retention** — Code context is processed ephemerally unless you explicitly enable persistence
* **No cross-customer data sharing** — Customer workspaces are logically isolated
* **No unauthorized access** — Internal access follows least-privilege principles

## Encryption

| Layer | Standard |
| - | - |
| **In transit** | TLS 1.2+ for all API and data communication |
| **At rest** | AES-256 encryption for stored data |
| **API keys (BYOK)** | Encrypted before storage; never logged or exposed |

## Compliance & Certifications

Zencoder maintains industry-standard certifications:

| Certification | Status |
| - | - |
| **SOC 2 Type II** | Certified |
| **ISO 27001** | Certified |
| **ISO 42001** | Certified (AI-specific management) |
| **GDPR** | Compliant |

<Info>
  For detailed audit reports and certification documents, visit the [Trust Center](https://trust.zencoder.ai) or contact your account manager.
</Info>

## Enterprise Security Controls

Available on Pro Plus, Pro Max, and Enterprise plans:

### SSO (Single Sign-On)

Integrate with your identity provider for centralized authentication:

* SAML 2.0 and OIDC support
* Enforce SSO-only login for your organization
* Automatic user provisioning and deprovisioning

### Audit Logs

Track all significant actions across your organization:

* Agent usage and tool invocations
* Configuration changes
* User management actions
* Export logs for compliance and review

### Role-Based Access Control

| Role | Capabilities |
| - | - |
| **Owner** | Full organization control — billing, users, settings, repositories |
| **Manager** | User management, repository management, analytics access |
| **Member** | Use agents, manage personal settings |

### Credit Controls

Admins can set per-user credit caps to prevent any single user from consuming the organization's shared credit pool. See [Team & Admin Controls](/faq/pricing#team--admin-controls).

## BYOK (Bring Your Own Key)

When you use your own API key (OpenAI, Anthropic, Gemini), LLM calls are routed through your key:

* Calls go directly to the provider under your API agreement
* No bundled credits are consumed
* Your provider's data policies apply to those calls
* Available on all plans, including Free

## Private Deployments

For teams requiring full infrastructure control, [Private Deployments](/features/private-deployments) let you run agents and inference on your own infrastructure:

* Custom model endpoints (local, VPC, or third-party)
* Option to hide the managed model catalog
* Zero dependency on external endpoints for sensitive workloads

See the [Private Deployments guide](/features/private-deployments) and [Custom Models Configuration](/features/custom-models-configuration) for setup instructions.

## MCP Tool Security

Agents request explicit permission before invoking MCP tools:

* **Per-invocation approval** by default
* **"Always allow"** option for trusted tools
* Full visibility into which tools are being called and with what parameters

## Responsible AI

Zencoder follows responsible AI practices. To report concerns or incidents related to AI behavior, use the [AI Adverse Impact Reporting Form](https://docs.google.com/forms/d/e/1FAIpQLScPgka564_ZDc3c30fL17VFuyRQmwUb95rxpe9bGjlb3kFdOA/viewform).

## Data Rights

Depending on your jurisdiction, you may have the right to:

* Access your personal information
* Correct inaccuracies
* Request deletion
* Restrict processing

Contact [support](/get-started/community-support) to exercise any of these rights.

## Related

<CardGroup cols={2}>
  <Card title="Privacy & Ethics FAQ" icon="lock" href="/faq/privacy">
    Frequently asked questions about data privacy
  </Card>

  <Card title="Private Deployments" icon="server" href="/features/private-deployments">
    Run Zencoder on your own infrastructure
  </Card>

  <Card title="Custom Models" icon="puzzle-piece" href="/features/custom-models-configuration">
    BYOM — configure your own model endpoints
  </Card>

  <Card title="Trust Center" icon="shield-halved" href="https://trust.zencoder.ai">
    Certifications, controls, and compliance docs
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.