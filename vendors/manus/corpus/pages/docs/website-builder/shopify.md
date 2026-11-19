> ## Documentation Index
> Fetch the complete documentation index at: https://manus.im/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Shopify

> Build a custom storefront for your Shopify store in a Website Builder project, and manage your store from the chat with the Shopify connector.

## What it is

[YouTube video player](https://www.youtube.com/embed/F_diWtE8vuo)

With Shopify on Manus, you build a custom storefront for a Shopify store in a Website Builder project. Manus builds the website that your customers shop on. Shopify runs the commerce side: products, inventory, checkout, payments, taxes, shipping and orders.

You can connect a Shopify store that you already run. If you do not have a store, Manus can create one for you.

Shopify on Manus has two parts:

| Part | What it does | Where you use it |
| - | - | - |
| **Shopify storefront** | Builds and hosts the website for your store | A Website Builder project |
| **Shopify connector** | Adds and updates products, variants, inventory and discount codes in your store | Any Manus chat |

You can use the connector with or without a storefront. For an overview, read [Introducing Shopify on Manus](https://manus.im/blog/manus-shopify-connector).

## How to use it

### Build a Shopify storefront

**1. Describe your storefront**

Open a Website Builder project, or start a new one. Tell Manus that you want a Shopify storefront. Describe what you sell, who your customers are and the look you want. If you sell in a currency other than USD, say so.

> "Build a Shopify storefront for my handmade candle store. The audience is people who buy gifts for holidays. Use a warm, minimal design."

**2. Choose your Shopify setup**

Manus shows a **Choose your Shopify setup** card. Select one option:

* **Connect an existing store.** Select a store that you already connected. Or add a store: paste your Shopify admin URL, for example `https://admin.shopify.com/store/store-name`, then approve access in Shopify.
* **Create a new store.** Manus creates a Shopify development store for your project. You do not need a Shopify account yet. Before you can sell, you must claim the store. Read [Claim a store that Manus created](#claim-a-store-that-manus-created).

**3. Review and refine**

Manus builds the storefront with the products and collections in your store. For a new store, Manus also adds products, collections and images. If you do not list any products, Manus adds two sample products. Review the result in Preview, then ask Manus for changes in the chat.

**4. Publish the storefront**

Publish your project to put the storefront online. For details, read [Publishing](https://manus.im/docs/website-builder/publishing.md). Optional: connect a custom domain. For details, read [Custom domains](https://manus.im/docs/website-builder/custom-domains.md).

### Claim a store that Manus created

If you selected **Create a new store**, Manus owns the development store until you claim it. Claim the store when you are ready to take real orders.

> [!WARNING]
>
> Claim your store within 30 days. If you do not, Shopify removes the development store. Your website code and data are not affected, but you must create a new store and add your products again.

1. In the project panel, go to **Settings → Integrations → Shopify** and select **Claim store**. You can also ask Manus in the chat for a claim link.
2. Sign in to Shopify, or create a Shopify account. You are now the owner of the store.
3. In your Shopify admin, choose a paid plan. This removes the storefront password.
4. In your Shopify admin, set up payments, shipping, taxes and store policies.
5. In your Shopify admin, go to **Settings → Domains**. Add your storefront domain as an **external storefront**. Links from checkout then return customers to your Manus storefront.
6. Give Manus access to the store again. In **Settings → Integrations → Shopify**, select **Add to Connectors**, then approve access in Shopify. After you claim a store, Manus has no admin access to it until you complete this step.

### Manage your store with the Shopify connector

The Shopify connector lets Manus do store work from the chat. Use it for bulk product uploads, catalog clean-up, inventory updates and discount codes.

**1. Open Connectors**

In Manus, open your settings and go to **Connectors**. Find **Shopify** and select **Connect**.

If you claimed a store that Manus created, select **Add to Connectors** in the project settings instead.

**2. Enter your Shopify admin URL**

Paste the URL of your Shopify admin, for example `https://admin.shopify.com/store/store-name`. Manus sends you to Shopify.

**3. Approve access**

Sign in to Shopify and approve the access that Manus requests. To learn what you approve, read Shopify's guide [Authorizing AI tool access to your store](https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/authorizing-access).

**4. Ask Manus to do store work**

In a Manus chat, describe the task and mention Shopify. Attach spreadsheets or images when the task needs them.

Use these prompts as a starting point.

**Add and update products**

* "Here is my supplier's spreadsheet and a folder of product images. Create a Shopify listing for each row and match each image to its SKU. Write descriptions in our brand voice."
* "Add Small, Medium and Large variants to every T-shirt in my store, priced at $24, $26 and \$28."

**Keep your catalog clean**

* "Audit my Shopify products. Find listings with no description, alt text or price, and fix them."
* "Update inventory counts from this spreadsheet. List anything below five units."

**Run promotions**

* "Create a 15% discount code called SPRING15 for all candles. It expires on Sunday."
* "Create a free shipping code for orders over \$50."

## What you need to know

### All Shopify features

* **Availability.** Shopify on Manus is available on paid Manus plans.
* **Shopify stays in charge of commerce.** Checkout, payments, shipping, taxes and order fulfillment stay in Shopify. Manus does not process payments.
* **You do not paste Shopify credentials.** Manus manages the connection for you. Do not paste Shopify tokens or API keys into the chat.
* **You pay Shopify and Manus separately.** Shopify bills your Shopify plan. Manus bills your Manus usage. For Manus costs, read [Usage and pricing](https://manus.im/docs/website-builder/getting-started/usage-and-pricing.md).

### Shopify storefronts

* **Checkout runs on Shopify.** When a customer is ready to pay, the storefront sends them to Shopify's hosted checkout.
* **Your Shopify theme stays the same.** The storefront is a separate website. Your current theme stays in your Shopify admin.
* **Choose Stripe or Shopify before you start.** A project can use Stripe or Shopify, but not both. After you connect Shopify to a project, you cannot switch that project to Stripe. To accept payments with Stripe, use a different project. For details, read [Payments](https://manus.im/docs/website-builder/payments.md).
* **How Manus builds the storefront.** For a new project, Manus uses Shopify's Hydrogen toolkit. Pages are rendered on the server, and the cart is kept on the server. If you add Shopify to an existing project, Manus keeps the project's current framework.
* **The cart can behave differently in Preview.** Some browsers block the cart cookie inside the embedded Preview. Always test the cart outside the embedded Preview as well.
* **The external storefront domain option depends on who created the store.** Shopify offers **Add an external storefront** only for stores that a partner created. If you connected an existing store, you do not see this option. For details, read Shopify's guide [Building a store with a vibe code partner](https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/vibe-code-partners).

### Stores that Manus creates

* **A development store cannot take real payments.** The store is password protected until you claim it and choose a Shopify plan.
* **You have 30 days to claim the store.** After 30 days, Shopify removes an unclaimed development store. Manus then shows "Your development store is no longer available". Ask Manus to create a new store.
* **Manus access changes when you claim the store.** Before you claim it, Manus can change your products, collections, inventory and images directly. After you claim it, select **Add to Connectors** to give Manus access again.

### Shopify connector

* **Changes go straight to your live store.** Products, prices, variants, inventory and discount codes that Manus changes appear in your Shopify admin. Your customers can see them right away.
* **Manus confirms before destructive actions.** Before Manus deletes a product, a variant or a discount code, it shows a confirmation card. Nothing changes until you confirm. Other destructive actions, such as archiving, also need your confirmation.
* **You can connect more than one store.** Each store is a separate connector account. Tell Manus which store to use.
* **The connector does not edit your theme.** It changes store data, not the look of your Shopify theme.

## Tips

### Build a better storefront

* **Give Manus a detailed first prompt.** Include what you sell, your audience, the visual style, the currency and the pages you need.
* **Point Manus at your best products.** For an existing store, name the collections or products that the home page should feature.
* **Test the cart outside Preview.** Open the standalone site and add items to the cart. Confirm that the cart keeps its items when you change pages.
* **Test the full checkout before launch.** On a development store, ask Manus to create a 100% off discount code with free shipping. Then place a test order with that code.
* **Finish catalog work before you claim a new store.** Before you claim it, Manus can add products, collections and images directly. Complete the bulk work first, but claim within 30 days.

### Get more from the connector

* **Ask for a preview before bulk changes.** For example: "Before you apply this, list the products that will change." Approve the list, then let Manus apply it.
* **Be specific about which products to change.** Name a tag, vendor, collection or date range. A precise filter gives a faster and safer result.
* **Name the store if you connected more than one.** For example: "In my wholesale store, update the prices from this sheet."
* **Connect your marketing accounts.** If you also connect email, social or ad accounts, Manus can turn new products and discount codes into a draft email, post or ad.

## FAQ

> [accordion] Can I build a storefront for a Shopify store that I already run?
>
> Yes. On the **Choose your Shopify setup** card, select **Connect an existing store**. Manus builds the storefront with your real products and collections. Your current Shopify theme stays the same.

> [accordion] Do I need a Shopify account to start?
>
> No. If you select **Create a new store**, Manus creates a development store for you. You sign in to Shopify, or create an account, when you claim the store.

> [accordion] What happens if I do not claim my store within 30 days?
>
> Shopify removes the development store. Your website code and data in Manus are not affected. Ask Manus to create a new store, then add your products again.

> [accordion] Do I need a storefront to use the Shopify connector?
>
> No. After you connect your store in **Connectors**, you can ask Manus to do store work in any Manus chat.

> [accordion] Can I connect more than one Shopify store?
>
> Yes. Connect each store separately. In your prompt, say which store Manus should use.

> [accordion] Why does Manus no longer update my store after I claimed it?
>
> When you claim a store, Manus loses direct admin access to it. To give Manus access again, go to **Settings → Integrations → Shopify** in the project panel. Select **Add to Connectors**, then approve access in Shopify.

> [accordion] Can I use Stripe and Shopify in the same project?
>
> No. A Website Builder project can use Stripe or Shopify, but not both. After you connect Shopify to a project, you cannot switch that project to Stripe. To use Stripe, create a different project.

> [accordion] Where do my customers check out?
>
> Customers check out on Shopify's hosted checkout. Manus does not process payments.

> [accordion] Why is my cart empty, or different, in Preview?
>
> Some browsers block the cart cookie inside the embedded Preview. Test the cart outside the embedded Preview.

> [accordion] Does Manus access my customer data?
>
> When you approve access, Shopify shows the data that Manus can read. This includes products, inventory, orders and customer details. Manus uses this data to complete the tasks that you ask for. Manus does not store customer personal data, such as names, addresses or payment details, outside the session.

> [accordion] Who do I contact for help?
>
> Contact Manus about the storefront, your prompts, platform errors, Manus billing and any store that you have not claimed yet. Use the [Manus Help Center](https://help.manus.im/). Contact [Shopify Support](https://help.shopify.com/en/manual/your-account/contact-shopify-support) about your Shopify account, plan, products, orders, payments and claiming your store.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.