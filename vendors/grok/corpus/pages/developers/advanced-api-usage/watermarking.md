#### Advanced API Usage

# Output Watermarking

Text responses from supported Grok models include an invisible watermark. The watermark lets SpaceXSI later recognize text as model-generated, and it requires no change to your requests: there is no parameter to send, and your integration works the same way with or without it.

SpaceXSI watermarks text model output to comply with the EU AI Act. The watermark is enabled on every SpaceXSI API endpoint, including the global endpoint, `https://api.x.ai`, and any [regional endpoint](/developers/advanced-api-usage/regions).

Watermarking is controlled per model for your whole team. Team admins can opt out in the SpaceXSI Console; see [Opting out](#opting-out).

## Which outputs are watermarked

Watermarking applies to text output from text generation requests, for each model that has watermarking turned on for your team.

Starting November 7, 2026, responses from these models include a watermark. It's on by default, and you can [opt out per model](#opting-out).

* grok-4.7
* grok-4.6
* grok-4.5
* grok-4.3
* grok-4.20-reasoning
* grok-4.20-non-reasoning
* grok-4.20-multi-agent

Watermarking applies to outputs from every text generation API, including the Responses API and the Chat Completions API. It covers the generated text you receive in the response: ordinary text responses, [structured outputs](/developers/model-capabilities/text/structured-outputs), and [tool call](/developers/tools/function-calling) arguments.

### Checking whether a response was watermarked

To check whether a response was watermarked, read the `x-watermark` header on the Responses API or Chat Completions API response. `x-watermark: true` means the output for that request was generated with the watermark. Any other value, or no header at all, means it was not.

```javascript customLanguage="javascriptAISDK"
import { xai } from '@ai-sdk/xai';
import { generateText } from 'ai';

const { text, response } = await generateText({
  model: xai.responses('grok-4.7'),
  prompt: 'Write a haiku about the ocean.',
});

console.log(response.headers?.['x-watermark']);
console.log(text);
```

```python customLanguage="pythonOpenAISDK"
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)

raw = client.responses.with_raw_response.create(
    model="grok-4.7",
    input="Write a haiku about the ocean.",
)
response = raw.parse()

print(raw.headers.get("x-watermark"))
print(response.output_text)
```

```javascript customLanguage="javascriptOpenAISDK"
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.XAI_API_KEY,
  baseURL: 'https://api.x.ai/v1',
});

const { data: response, response: raw } = await client.responses
  .create({
    model: 'grok-4.7',
    input: 'Write a haiku about the ocean.',
  })
  .withResponse();

console.log(raw.headers.get('x-watermark'));
console.log(response.output_text);
```

```bash customLanguage="bash"
curl -i https://api.x.ai/v1/responses \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "grok-4.7",
    "input": "Write a haiku about the ocean."
  }'
```

## How it works

The watermark is not visible. It is applied while the model generates text: it slightly shapes which tokens the model picks, so it adds no characters, markup, or hidden text to the response.

Detection is statistical. SpaceXSI scores a piece of text against the watermark and reports whether it is watermarked, not watermarked, or uncertain. Longer text gives a stronger signal.

> [!WARNING]
>
> Access to watermark detection is granted by application. You can submit a request for the detection API through [this form](https://docs.google.com/forms/d/e/1FAIpQLSc6zpONhSgvde0GbNmfGajT6QoyO0T-fX8UBMhmd14h-UtabQ/viewform).

## Opting out

Team admins can turn watermarking off for some or all models in the SpaceXSI Console. The setting applies to every API key on the team.

1. Open the [Team settings page](https://console.x.ai/team/default/settings/team?utm_source=docs\&utm_medium=referral\&utm_campaign=developers-watermarking\&utm_content=team-settings) and find the **Model output watermarking** row. It shows **On (all models)**, **Off (all models)**, or **Custom**. Only team admins see this row.
2. Select the settings icon next to it, then clear the checkbox for each model you want to opt out. **Select all** turns every model on or off at once.
3. Select **Save**. If you turned a model off, confirm with **Opt Out**.

Changes apply to new requests within 5 minutes. After you opt a model out, its new requests stop including the watermark; after you opt back in, they start including it again.

Opting out asks you to confirm that an exception under applicable law applies to your use, and that you are solely responsible for any marking, disclosure, or other legal requirement.

Some models may be locked on for your team. Locked models are listed in the dialog but cannot be turned off from the Console. To ask about a locked model, see [Why can't I turn watermarking off for a model?](#why-cant-i-turn-watermarking-off-for-a-model)

Every opt-in and opt-out is recorded in your team's audit log. Team admins can view it on the [Audit Log page](https://console.x.ai/team/default/audit?utm_source=docs\&utm_medium=referral\&utm_campaign=developers-watermarking\&utm_content=audit) in the SpaceXSI Console. To find a change, search by event ID, description, or user, and use the time filter to narrow the results to a range of dates. For screenshots of these filters, see [Do you have audit logs?](/developers/faq/security#do-you-have-audit-logs) in the security FAQ.

## FAQ

### Do I need to change my code?

No. Watermarking has no request parameter, and the response format is unchanged apart from the `x-watermark` header.

### Does opting out apply to all of my API keys?

Yes. The setting belongs to the team, so it applies to every API key on the team. You choose it separately for each model.

### Why can't I turn watermarking off for a model?

The model is locked on for your team. Locked models show in the watermarking dialog without a checkbox.

For questions about a locked model, contact your team admin. If you still have questions, email [support@x.ai](mailto:support@x.ai).

### Does watermarking affect quality or speed?

No. Watermarking doesn't change response quality or speed.
