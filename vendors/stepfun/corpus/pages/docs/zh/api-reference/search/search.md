> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 网页搜索

网页搜索接口检索互联网公开信息，并针对重点领域优化了信源的权威性，适合深入研究等对信源质量要求较高的场景。

## 请求地址

`POST https://api.stepfun.com/v1/search`

## 请求参数

* `query` `string` ***required***<br />检索关键词。
* `n` `int` ***optional***<br />返回结果条数，默认为 `10`，取值范围 1\~20。
* `category` `string` ***optional***<br />检索场景，默认为空，表示检索全部场景。

  <Expandable>
    * `programming`<br />代码编程。
    * `research`<br />学术研究。
    * `gov`<br />政务信息。
    * `business`<br />商业财经。
  </Expandable>

## 请求响应

* `query` `string`<br />检索关键词，回显请求参数。
* `category` `string`<br />检索场景，回显请求参数，未指定时为空字符串。
* `results` `object array`<br />检索结果列表。

  <Expandable>
    * `url` `string`<br />结果网页地址。
    * `position` `int`<br />结果排序位置，从 `1` 开始。
    * `title` `string`<br />结果网页标题。
    * `time` `string`<br />结果网页的索引时间。
    * `snippet` `string`<br />结果网页的摘要内容。
    * `content` `string`<br />结果网页的完整内容。
  </Expandable>

## 示例

```bash theme={null}
curl -X POST "https://api.stepfun.com/v1/search" \
    -H 'Content-Type: application/json; charset=utf-8' \
    -H 'Authorization: Bearer $STEPFUN_API_KEY' \
    -d '{
        "query": "Python 新手入门教程",
        "n": 1,
        "category": "programming"
    }'
```

返回示例（`snippet`、`content` 内容较长，此处省略）：

```json theme={null}
{
  "query": "Python 新手入门教程",
  "category": "programming",
  "results": [
    {
      "url": "https://developer.aliyun.com/article/1718189",
      "position": 1,
      "title": "Python入门教程（新手必看）（一）",
      "time": "2026-03-20T00:00:00",
      "snippet": "Python 以简洁语法和强大生态成为编程入门首选，广泛应用于 Web 开发、数据分析、AI、自动化等领域...",
      "content": "Python 以简洁语法和强大生态成为编程入门首选...本文详解 Python 安装配置、基础语法（缩进、变量、输入输出、运算符）及首个程序实践，助新手快速上手..."
    }
  ]
}
```
