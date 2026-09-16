> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pi

> 在 Pi 开源终端编程 Agent 中使用最新的 MiniMax M 系列模型。

<div style={{background:"#fffbeb",borderLeft:"4px solid #d97706",padding:"12px 16px",borderRadius:"6px",margin:"16px 0"}}>[**Pi**](https://github.com/earendil-works/pi) 是 earendil-works 出品的开源终端编程 Agent，通过统一 LLM API 接入任意服务商。</div>

## 配置 MiniMax

<Tabs sync={false}>
  <Tab title="方式一：一键配置向导">
    Pi 的自动安装要求 Node.js 22.19 或更高版本。直接运行：

    ```bash theme={null}
    npx -y mmx-cli@latest agent setup
    ```

    在工具列表中选择 **Pi**。如果尚未安装，在第二个多选列表中保留 Pi。向导会安装官方 npm 包、检查版本，并把 MiniMax M3 写入 Pi 的模型和默认设置。

    完成后直接运行：

    ```bash theme={null}
    pi
    ```

    详细参数和备份说明请见 [一键安装向导](/docs/token-plan/agent-setup)。
  </Tab>

  <Tab title="方式二：手动配置">
    <Steps>
      <Step title="安装 Pi">
        ```bash theme={null}
        npm install -g @earendil-works/pi-coding-agent
        ```
      </Step>

      <Step title="设环境变量并启动">
        把 [订阅 Key](https://platform.minimaxi.com/user-center/payment/token-plan)（前缀 `sk-cp-…`）设到环境变量后启动 Pi：

        ```bash theme={null}
        export MINIMAX_CN_API_KEY=sk-cp-...
        pi --provider minimax-cn --model MiniMax-M3
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>
