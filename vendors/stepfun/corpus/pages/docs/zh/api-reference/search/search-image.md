> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 文搜图

文搜图接口根据文字描述检索相关图片，可用于内容自动配图等场景，图片数据来自百度搜图。该接口仅在 [Step Plan](/docs/zh/step-plan/overview) 通道提供，按调用次数计费，具体价格见[计费详情](/docs/zh/guides/pricing/details)。

<Warning>
  返回图片的版权归原站点所有，接口不进行版权检测或商用授权判断，请在使用前自行评估合规性。
</Warning>

## 请求地址

`POST https://api.stepfun.com/step_plan/v1/search-image`

## 请求参数

* `query` `string` ***required***<br />搜索词，建议使用中文，也支持英文。
* `topk` `int` ***optional***<br />返回图片张数的上限。

## 请求响应

* `code` `int`<br />状态码，`0` 表示成功。
* `msg` `string`<br />提示信息，成功时为空字符串。
* `data` `object`<br />返回数据。

  <Expandable>
    * `result` `object`<br />搜索结果。

        <Expandable>
          * `block` `bool`<br />是否命中审核拦截。`true` 表示命中拦截，此时 `search_results` 为空；`false` 表示未拦截。
          * `search_results` `object array`<br />图片结果列表，可能为空。

                <Expandable>
                  * `contentUrl` `string`<br />原图地址。
                  * `snippet` `string`<br />图片描述，可用作 alt 文本。
                  * `width` `int`<br />原图宽度，单位为像素。
                  * `height` `int`<br />原图高度，单位为像素。
                  * `hostPageUrl` `string`<br />图片所在网页地址。
                  * `hostname` `string`<br />图片来源域名。
                </Expandable>
        </Expandable>
  </Expandable>

## 示例

<Tabs>
  <Tab title="cURL">
    ```bash theme={null}
    curl --location 'https://api.stepfun.com/step_plan/v1/search-image' \
        -H 'Content-Type: application/json' \
        -H 'Authorization: Bearer $STEPFUN_API_KEY' \
        -d '{
            "query": "故宫",
            "topk": 2
        }'
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={null}
    import os
    import requests

    resp = requests.post(
        "https://api.stepfun.com/step_plan/v1/search-image",
        headers={
            "Authorization": f"Bearer {os.environ['STEPFUN_API_KEY']}",
            "Content-Type": "application/json",
        },
        json={"query": "故宫", "topk": 2},
    )

    result = resp.json()["data"]["result"]
    for item in result["search_results"]:
        print(item["contentUrl"], item["snippet"])
    ```
  </Tab>
</Tabs>

返回示例：

```json theme={null}
{
  "code": 0,
  "msg": "",
  "data": {
    "result": {
      "block": false,
      "search_results": [
        {
          "contentUrl": "http://q1.itc.cn/images01/20250921/4aefdeaeff0f4f2999ce3e959a902265.jpeg",
          "snippet": "故宫博物院,中国最大的古代文化艺术博物馆",
          "width": 5650,
          "height": 3687,
          "hostPageUrl": "http://travel.sohu.com/a/937199080_122365627",
          "hostname": "travel.sohu.com"
        },
        {
          "contentUrl": "http://q2.itc.cn/images01/20251010/bf333868e5e243a6808ad887067a7766.jpeg",
          "snippet": "北京故宫博物院今天过100岁生日",
          "width": 1920,
          "height": 1080,
          "hostPageUrl": "http://gov.sohu.com/a/942413642_120479584",
          "hostname": "gov.sohu.com"
        }
      ]
    }
  }
}
```
