#### Advanced API Usage

# Troubleshooting Reasoning

Grok reasoning models think before they answer or call a tool, and they work best when each later request gives that reasoning back. When a multi-turn or tool-calling integration loses it, nothing fails: the API returns `200`, and results can get worse.

## Dropping the reasoning items

The `input` of your follow-up requests has `function_call` items or assistant messages with no `reasoning` item before them. This happens when code keeps only the answer text or the function calls from a response, reads only the text of a stream, or rebuilds the history from its own records.

To fix it, keep every item of each response's `output` array exactly as it arrived and append all of them, in order, to the history, then add your tool results. When you stream, take the items from the final `response.completed` or `response.incomplete` event:

```json addedLines="3"
[
  {"role": "user", "content": "What is the temperature in Paris?"},
  {"type": "reasoning", "summary": [], "encrypted_content": "Hfq+g7jQ...4QfQnY"},
  {"type": "function_call", "call_id": "call-5faadddf-0", "name": "get_temperature", "arguments": "{\"location\":\"Paris\"}"},
  {"type": "function_call_output", "call_id": "call-5faadddf-0", "output": "{\"temperature\":15}"}
]
```

To confirm the fix, log the `input` of a follow-up request and check that it holds every `reasoning` item of the earlier responses, each in its original place. For a complete loop in Python, see [Keep reasoning in agent loops](/developers/model-capabilities/text/best-practices#keep-reasoning-in-agent-loops).

## Not asking for encrypted reasoning

The `reasoning` items you send back have no `encrypted_content` field. `grok-4.7` returns `encrypted_content` on every response; earlier models, such as `grok-4.6` and `grok-4.5`, return it only when you ask.

To fix it, add `include` to every request of a conversation whose history you keep yourself, starting with the first. Apply this together with the first fix; asking for encrypted reasoning helps only if your requests send it back. In the xAI SDK, set `use_encrypted_content=True`.

```json addedLines="4"
{
  "model": "grok-4.6",
  "store": false,
  "include": ["reasoning.encrypted_content"],
  "input": [{"role": "user", "content": "What is the temperature in Paris?"}]
}
```

## Using Chat Completions for multi-turn conversations

Your multi-turn or tool-calling requests go to `/v1/chat/completions`. That endpoint has no field for encrypted reasoning, so your requests cannot send it back.

To fix it, send these conversations to `/v1/responses` and keep the history as in the first fix. The assistant turn changes from a `messages` entry to the output items of the response. The [comparison guide](/developers/model-capabilities/text/comparison) maps each parameter and field.

```json addedLines="3,4"
[
  {"role": "user", "content": "What is the temperature in Paris?"},
  {"type": "reasoning", "summary": [], "encrypted_content": "Hfq+g7jQ...4QfQnY"},
  {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "It is 15°C."}]},
  {"role": "user", "content": "And in Fahrenheit?"}
]
```

## Sending both the previous response ID and the history

A request sets `previous_response_id` and also resends the earlier turns in `input`. Nothing fails, but those turns are sent twice and `usage.input_tokens` grows much faster than the conversation.

To fix it, choose one way to continue a conversation. With `previous_response_id`, send only the new items. Without it, send the whole history. A `previous_response_id` that points at a response created with `store: false` returns `404`, so those conversations need the whole history.

> [!NOTE]
>
> With [Zero Data Retention (ZDR)](/developers/faq/security#what-is-zero-data-retention-zdr) enabled for your team, `previous_response_id` does not work for HTTP requests either, so send the whole history.

```json
{
  "model": "grok-4.7",
  "previous_response_id": "9a1e6c0e-5c1f-4f0b-b5a5-1c2f6f6f0d11",
  "input": [
    {"type": "function_call_output", "call_id": "call-5faadddf-0", "output": "{\"temperature\":15}"}
  ]
}
```

## Tool results that do not match their calls

A `function_call_output` has an empty `call_id` or one that matches no `function_call`, or a `function_call` has no result. The API accepts these requests, and the model cannot reliably tell which result answers which call. One cause is an unset field that serializes as `""`.

To fix it, copy the `call_id` of each `function_call` into the result that answers it, and send a result for every call:

```json addedLines="3"
[
  {"type": "function_call", "call_id": "call-5faadddf-0", "name": "get_temperature", "arguments": "{\"location\":\"Paris\"}"},
  {"type": "function_call_output", "call_id": "call-5faadddf-0", "output": "{\"temperature\":15}"}
]
```

## Changing reasoning items

A follow-up fails with `400` and `Could not decrypt the provided encrypted_content`. Something between the response and the next request shortened or rewrote the item, for example storage that truncates long strings.

To fix it, store and send every reasoning item unchanged:

```json addedLines="2"
[
  {"type": "reasoning", "summary": [], "encrypted_content": "Hfq+g7jQ...4QfQnY"}
]
```

## Fix it with a coding agent

Paste the following into your coding agent, or save it as a skill, for example as `.grok/skills/fix-grok-reasoning/SKILL.md` for [Grok Build](/build/features/skills-plugins-marketplaces). It finds these mistakes in your code and fixes them.

```text
---
name: fix-grok-reasoning
description: >-
  Find and fix code that loses a Grok model's reasoning between requests in
  multi-turn or tool-calling conversations on the xAI API. Use when results
  get worse over a conversation or agent loop, or when asked to check that
  reasoning is sent back to the model.
---

# Fix lost reasoning in xAI API conversations

Grok reasoning models return their reasoning as "reasoning" items in the
output array of a /v1/responses response. Each later request must give
them back, by exactly one of two routes:

- Stored: set previous_response_id and put only the new items in input.
  The previous response must have been created with store on (the
  default). Over HTTP, this route does not work for teams with Zero Data
  Retention.
- Stateless: no previous_response_id. Put the whole conversation in input,
  including every output item of every earlier response, unchanged and in
  order, and send include: ["reasoning.encrypted_content"] on every
  request.

A correct stateless follow-up after one tool call:

  {
    "model": "<same model>",
    "store": false,
    "include": ["reasoning.encrypted_content"],
    "tools": [<same tools>],
    "input": [
      {"role": "user", "content": "<the question>"},
      {"type": "reasoning", "id": "rs_...", "summary": [],
       "encrypted_content": "<as received>"},
      {"type": "function_call", "id": "fc_...", "call_id": "call-1",
       "name": "<tool>", "arguments": "<as received>"},
      {"type": "function_call_output", "call_id": "call-1",
       "output": "<your tool result>"}
    ]
  }

Real items carry more fields than shown here. Send all of them back.

Most of these mistakes return HTTP 200 and a plausible answer, so judge
from the request bodies, not from the responses.

1. Work only on calls to the xAI API; leave other providers alone. Find
   where a response's output is read and where the input of the next
   request is built. Search for /v1/responses, /v1/chat/completions,
   responses.create, chat.completions.create, previous_response_id, and
   function_call_output. Then follow the history between requests: where
   it is saved, loaded, converted, or logged. An SDK that runs the tool
   loop for you, a wrapper, or a storage layer can drop or change items
   after the code that builds them. Requests with no follow-up need no
   change.

2. Check each point. Fix every failure with the smallest change that works.
   a. Reasoning dropped. The code keeps only text or function calls,
      filters output by type, rebuilds items from its own types, or reads
      only the text deltas of a stream. Fix: keep each response's output
      items as raw JSON (from the response.completed or response.incomplete
      event when streaming) and append the whole array to the history,
      before the tool results.
   b. Encrypted reasoning not requested on the stateless route. Fix: send
      include: ["reasoning.encrypted_content"] on every request, including
      the first (use_encrypted_content=True in the xAI SDK; in the Vercel
      AI SDK, providerOptions.xai with store: false or include).
   c. Multi-turn or tool-calling requests sent to /v1/chat/completions,
      which cannot carry reasoning. Fix: move them to /v1/responses, then
      apply a and b. If the migration is too large to do safely, stop and
      report it.
   d. previous_response_id sent together with earlier turns. Fix: keep one
      route. If the id fails with 404, use the stateless route.
   e. A function_call_output with an empty call_id or one that matches no
      function_call, or a call left without a result. Fix: copy call_id
      from the function_call and answer every call.
   f. Reasoning items edited or truncated (error 400 "Could not decrypt
      the provided encrypted_content"). Look for length limits where the
      history is saved or logged. Fix: store and send the items unchanged.
      Keep a limit that other data relies on; exempt conversation items.

3. Verify with a test that sends two requests of one conversation (with a
   tool call if the code uses tools) and captures the body of the second.
   Stateless: it must hold every output item of the first response
   unchanged, each reasoning item with a non-empty encrypted_content.
   Stored: it must set previous_response_id and hold only new items.
   Either way, every function_call_output.call_id must match a
   function_call. If an API key is available, also run every multi-turn
   flow once against the API, including the ones you judged correct, and
   check the follow-up bodies it really sends. Some failures, such as the
   400 above, show up only then. Existing tests must still pass.

4. Report what was wrong, with file and line, what you changed, and what
   you could not check. Do not change models, prompts, or tools.
```
