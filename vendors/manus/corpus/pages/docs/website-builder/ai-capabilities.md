> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Built-in AI Capabilities

> Learn how to incorporate AI capabilities into your web application

Manus-built web applications are not just static sites; they are intelligent, dynamic platforms with AI capabilities woven into their core. This allows you to create unique and engaging experiences for your users.

## Large Language Model (LLM)

You can integrate the power of large language models directly into your application to create features that understand and generate human-like text. This opens up a world of possibilities for interactivity and user assistance.

| Use Case                    | Example Prompt                                                                                                                                                                                                                           |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AI-Powered Chatbot**      | `"Add a chatbot to the bottom right corner of the site. It should be able to answer frequently asked questions about our pricing, features, and return policy."`                                                                         |
| **Content Generation Tool** | `"Create a new page called 'Blog Post Helper'. Add a text input field and a button. When the user enters a topic and clicks the button, call the LLM to generate a 100-word blog post introduction on that topic and display it below."` |
| **Natural Language Search** | `"Upgrade the search bar in the header to use natural language processing. When a user searches for 'cheap red shoes for running', it should understand the intent and show relevant products from the database."`                       |
| **Automated Summarization** | `"On the article pages, add a 'Summarize' button. When clicked, use the LLM to generate a three-bullet-point summary of the article's content."`                                                                                         |

## Image Generation

In addition to text-based AI, you can also incorporate dynamic image generation into your application. This enables a wide range of creative and personalized visual experiences.

| Use Case                       | Example Prompt                                                                                                                                                                                                                      |
| :----------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Personalized Avatars**       | `"On the user profile page, add a feature to generate a personalized avatar. The user can enter a text description like 'a friendly robot with a blue hat', and the app should generate and display the image."`                    |
| **Dynamic Product Mockups**    | `"On the product page for our custom t-shirts, add a section where users can input text. Use the image generation model to create a mockup of the t-shirt with their custom text printed on it."`                                   |
| **Creative Backgrounds**       | `"Create a 'background generator' tool. Add a text area where users can describe a scene, like 'a futuristic cityscape at sunset, in a watercolor style'. Generate a high-resolution background image based on their description."` |
| **AI-Generated Illustrations** | `"For our blog, create a feature that generates a unique header image for each new post based on the post's title and a summary of its content."`                                                                                   |

## Available LLM Models

LLM-powered features can run on any of ten models across three providers: OpenAI (GPT-5), Anthropic (Claude), and Google (Gemini). Every model supports vision, tool use, extended thinking/reasoning, and structured JSON output. They differ in speed, capability, and price. Pricing is per token, billed separately for input (the prompt) and output (the response), and is shown below in USD per 1,000,000 tokens.

| Model             | Provider  | Input (\$/1M) | Output (\$/1M) | Description                                     |
| ----------------- | --------- | ------------- | -------------- | ----------------------------------------------- |
| GPT-5 nano        | OpenAI    | \$0.05        | \$0.40         | OpenAI's smallest and lowest-cost model         |
| GPT-5 mini        | OpenAI    | \$0.25        | \$2.00         | A compact, lower-cost model in the GPT-5 family |
| GPT-5             | OpenAI    | \$1.25        | \$10.00        | OpenAI's general-purpose GPT-5 model            |
| GPT-5.5           | OpenAI    | \$5.00        | \$30.00        | OpenAI's highest-capability model               |
| Claude Haiku 4.5  | Anthropic | \$1.00        | \$5.00         | Anthropic's smallest and lowest-cost model      |
| Claude Sonnet 4.6 | Anthropic | \$3.00        | \$15.00        | A mid-tier model in the Claude family           |
| Claude Opus 4.6   | Anthropic | \$5.00        | \$25.00        | A high-capability model in the Claude family    |
| Claude Opus 4.7   | Anthropic | \$5.00        | \$25.00        | The latest model in the Claude Opus tier        |
| Gemini 3 Flash    | Google    | \$0.50        | \$3.00         | Google's lower-cost, high-speed model           |
| Gemini 3.1 Pro    | Google    | \$2.00        | \$12.00        | Google's highest-capability model               |

You can name a specific model in your prompt, or describe your goal and let Manus select one. Different features in the same application can use different models.

| Use Case                    | Example Prompt                                                                                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Select a Specific Model     | "Add a support chatbot in the bottom-right corner. Use Claude Haiku 4.5 to keep responses fast and inexpensive."                                              |
| Let Manus Choose            | "Add a 'Summarize' button to each article. I want good quality at low cost, so pick an appropriate model."                                                    |
| Compare Models Side by Side | "Build a page where I can enter one prompt, send it to GPT-5, Claude Sonnet 4.6, and Gemini 3.1 Pro at once, and compare their responses, latency, and cost." |
| Enable Extended Thinking    | "For the math-tutor feature, use GPT-5 with extended reasoning enabled so it works through problems step by step."                                            |
