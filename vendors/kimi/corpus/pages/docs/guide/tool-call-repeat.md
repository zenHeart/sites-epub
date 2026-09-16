> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何解决重复调用问题

> 排查 tool_calls 消息布局，并在业务侧检测重复工具调用，通过系统提示词提醒模型停止对同一工具的重复调用。

在使用工具调用 `tool_calls` 的过程中，模型可能会根据上下文连续发起多次工具调用。

如果你发现模型连续多次调用同一个 **工具**，并且每次调用使用的 `function.name` 与 `function.arguments` 完全相同，且工具返回结果没有带来新的有效信息，可以将其视为重复工具调用。

## 排查消息布局

在处理这类问题时，我们建议先排查消息布局是否正确：

1. 当 Kimi API 返回 `finish_reason=tool_calls` 时，是否已将返回的 `choice.message` 原封不动地添加到 `messages` 列表；
2. 每个 `tool_call` 是否都有一条对应的 `role=tool` 消息；
3. `role=tool` 消息中的 `tool_call_id` 是否与对应的 `tool_call.id` 完全一致；
4. 如果你使用流式输出 `stream=True`，是否已正确拼接分片返回的 `tool_calls`，尤其是 `function.arguments` 字段。

## 业务侧重复调用检测

如果上述消息布局没有问题，但模型仍然重复调用同一个工具和同一组参数，可以在业务侧增加重复调用检测，并在下一轮请求的系统提示词 system prompt 中追加提醒。

当同一个工具和同一组参数连续重复 3 次时，可以追加：

```text theme={null}
<system-reminder>
You are repeating the exact same tool call with identical parameters. Please carefully analyze the previous result. If the task is not yet complete, try a different method or parameters instead of repeating the same call.
</system-reminder>
```

当重复调用达到 5 次时，可以追加更明确的提示，并包含工具名、重复次数和参数：

```text theme={null}
<system-reminder>
You have repeatedly called the same tool with identical parameters many times.
Repeated tool call detected:
- tool: {tool_name}
- repeated_times: {repeat_count}
- arguments: {tool_arguments}
The previous repeated calls did not make progress. Do not call this exact same tool with the exact same arguments again.
Carefully inspect the latest tool result and choose a different next action, different parameters, or finish the task if enough evidence has been gathered.
</system-reminder>
```

如果同一个工具和同一组参数连续重复达到 8 次，建议再次追加上述提示。

需要注意的是，`<system-reminder>` 只是一个提示词示例，不是 Kimi API 的特殊字段。你可以将其中内容合并到下一轮请求的 `role=system` 消息中，也可以按照自己的消息管理方式写入系统提示词。为了避免误判，建议仅在"同一个工具、同一组参数、连续多次重复、工具结果没有新进展"同时成立时触发这类提示。
