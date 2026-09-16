> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 创建并使用项目 API Key

加入组织后，您可以在所参与的项目下创建 API Key。用它发起的调用由组织的 Credit 账户承担费用，不消耗您个人账号的额度。

## 接受邀请

主账号发起邀请后，您会收到一条含邀请链接的短信。点击链接进入邀请页面：

* 手机号已注册平台账号：点击「确认加入组织」，即成为该组织的成员。
* 手机号尚未注册：点击「去注册」完成注册，注册成功后自动加入该组织。

邀请链接自发起时刻起 7 天内有效，过期后请联系邀请人重新发送。

## 切换到组织空间

通过控制台右上角的「用户中心 > 空间切换」进入组织空间。项目下 API Key 的创建与用量查询都在该空间下进行。如需退出组织，请联系主账号。

## 创建 API Key

1. 在组织空间进入「账户管理 > 接口密钥」。该页面按项目列出您参与的每个项目，每个项目下最多创建一个 API Key。
2. 在目标项目行点击「创建密钥」，填写名称（不超过 20 字）后确认。
3. 复制并妥善保存完整的 API Key。

<Warning>
  请妥善保管您的 API Key，不要写入代码仓库或分享给他人。任何获得该 Key 的人都能以您的身份调用模型，并消耗组织的 Credit。
</Warning>

已创建的 API Key 可以修改名称或删除。删除后该 API Key 立即失效且无法撤回，如需继续使用可在该项目下重新创建。

状态显示为「已被管理员禁用」时，该 API Key 已由主账号禁用，请联系主账号处理。

## 发起调用

项目下 API Key 的使用方式与个人 API Key 一致，不需要额外传递组织或项目标识。

```bash theme={null}
curl https://api.stepfun.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $STEPFUN_API_KEY" \
  -d '{
    "model": "step-3.7-flash",
    "messages": [
      {
        "role": "user",
        "content": "你好"
      }
    ]
  }'
```

调用产生的费用从组织的 Credit 账户扣减，并计入对应的项目与成员。完整的接口说明见 [Chat Completions](/docs/zh/api-reference/chat/chat-completion-create)。

## 查看自己的用量

「账户管理 > 使用详情」展示您的调用明细，每一行对应一个计费项，可按密钥名称、模型与日期区间筛选，并导出当前筛选结果。

「账户管理 > 接口密钥」中的「Credit 已用 / 上限」一列展示您在该项目下的当期用量。上限显示为「不限」时，表示主账号未对您单独设置上限，此时仍受项目整体上限与组织 Credit 余额的约束。上限于每月 1 号 00:00 重置。

## 调用被拒绝时的排查

| 现象                                         | 原因                            | 处理方式                        |
| ------------------------------------------ | ----------------------------- | --------------------------- |
| 402 `insufficient_credit`                  | 组织的 Credit 账户余额不足             | 联系主账号补充 Credit              |
| 429 `project_credit_limit_exceeded`        | 所在项目达到当期 Credit 上限            | 联系主账号调高项目上限，或等待下月 1 号重置     |
| 429 `member_project_credit_limit_exceeded` | 您在该项目内达到当期 Credit 上限          | 联系主账号调高您的上限，或等待下月 1 号重置     |
| API Key 不可用                                | API Key 已被禁用或删除，或您已被移出该项目、该组织 | 在「账户管理 > 接口密钥」确认状态，必要时联系主账号 |

额度上限与速率限制返回的状态码同为 429，收到 429 时请以错误标识区分两种情况，错误标识的对照见[错误码](/docs/zh/api-reference/error-codes)。额度规则的完整说明见 [Credit 额度规则](/docs/zh/guides/organization/credits)。
