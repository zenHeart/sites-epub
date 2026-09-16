<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">内置集成费用</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/4760.77ece367d4.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.782417a8ae.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/coze_pro_internal_integrations_fee"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/coze_pro_internal_integrations_fee.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="description" content="该文档主要介绍了AI编程项目中内置集成费用的相关内容，包括计费服务类型，重点阐述了大语言模型的计费公式，详细说明了不同模型在不同条件下输入、输出及缓存命中token的单价计算方式，帮助开发者了解使用内置AI功能的费用情况。"/><meta data-react-helmet="true" name="keywords" content="内置集成费用,AI编程项目,大语言模型,计费公式,单价"/><meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC activeTab-g8RDKO" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC" href="/coze_pro_internal_integrations_fee" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" style="width:300px" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b8ac14bdbc784e3cbd1c3" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/coze_pro_billing_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="计费概述">计费概述</span></a></div><div id="tree-node-6a3b8ac14bdbc784e3cbd1ca" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/coze_pro_credits" data-discover="true"><span class="nodeTitle-ONnqtP" title="积分">积分</span></a></div><div id="tree-node-6a3b8ae84bdbc784e3cbf393" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="活动与公告">活动与公告</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ac14bdbc784e3cbd1d0" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="订阅套餐">订阅套餐</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ac14bdbc784e3cbd1fc" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="计费项">计费项</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8ac14bdbc784e3cbd20b" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="扣子计费项">扣子计费项</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ac14bdbc784e3cbd22e" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="AI 编程计费项">AI 编程计费项</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8ac14bdbc784e3cbd23d" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/coze_pro_task_fee" data-discover="true"><span class="nodeTitle-ONnqtP" title="扣子编程任务费用">扣子编程任务费用</span></a></div><div id="tree-node-6a3b8ac14bdbc784e3cbd245" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:40px" href="/coze_pro_internal_integrations_fee" data-discover="true"><span class="nodeTitle-ONnqtP" title="内置集成费用">内置集成费用</span></a></div><div id="tree-node-6a3b8ac14bdbc784e3cbd2e4" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/coze_pro_service_hosting_fee" data-discover="true"><span class="nodeTitle-ONnqtP" title="部署服务托管费用">部署服务托管费用</span></a></div></div></div><div id="tree-node-6a3b8ac14bdbc784e3cbd222" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="低代码计费项">低代码计费项</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ac14bdbc784e3cbd236" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="罗盘计费项">罗盘计费项</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div></div></div><div id="tree-node-6a3b8ac14bdbc784e3cbd2b1" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/coze_pro_Issue_invoice" data-discover="true"><span class="nodeTitle-ONnqtP" title="开具发票">开具发票</span></a></div><div id="tree-node-6a3b8ac14bdbc784e3cbd1f6" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/coze_pro_bills_and_usage" data-discover="true"><span class="nodeTitle-ONnqtP" title="账单与用量">账单与用量</span></a></div><div id="tree-node-6a3b8a2d4bdbc784e3cbb5f0" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ac14bdbc784e3cbd271" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="历史版本">历史版本</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA" style="width:calc(100% - 300px);--anchor-width:260px"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>定价</span><span class="separator-KB9yMa">/</span><span>计费项</span><span class="separator-KB9yMa">/</span><span>AI 编程计费项</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">内置集成费用</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">内置集成费用</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>内置集成费用是你在开发 AI 编程项目时，使用了扣子编程已经打包好的各种 AI 功能和服务所产生的费用。这些内置功能就像已经准备好的“即用工具箱”，直接取用即可增强应用的能力，但使用它们会产生相应的费用。</p>
<p>目前主要涉及的计费服务包括：</p>
<ul data-style="0">
<li>大语言模型调用：调用豆包、Kimi 等模型，进行对话、生成内容等。</li>
<li>图像生成：调用模型进行文生图或图生图。</li>
<li>视频生成：调用模型生成有声或无声视频。</li>
<li>语音功能：调用模型进行语音识别和语音合成。</li>
<li>联网搜索：调用工具实时联网检索信息。</li>
<li>内容处理：调用工具剪辑视频或提取链接内容。</li>
</ul>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>分享 AI 编程项目给他人使用时，产生的相关费用均从项目开发者账户中抵扣。</p>
</div>
<h2 id="58d09be6" tabindex="-1">大语言模型</h2>
<h3 id="4ab3eb91" tabindex="-1">计费公式</h3>
<p>扣子的大语言模型根据模型推理时消耗的 token 数量计费，计费公式如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">模型费用 🟰 输入单价 ✖️ (输入token ➖ 缓存命中token)
➕ 缓存命中单价 ✖️ 缓存命中token
➕ 输出单价 ✖️ 输出token
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="模型费用 🟰 输入单价 ✖️ (输入token ➖ 缓存命中token)
➕ 缓存命中单价 ✖️ 缓存命中token
➕ 输出单价 ✖️ 输出token" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p>在大语言模型中，token 是文本处理的基本单位，token 可以是单词、字符、子词片段或其他形式的文本片段，具体的划分方式取决于模型使用的分词算法，所以 token 的计算和处理方式可能会根据模型的具体架构和设计而有所不同。</p>
<ul data-style="0">
<li><strong>输入 token</strong>：将推理输入的内容（包括但不限于文字、图片）转化为 token 数进行计费。</li>
<li><strong>输出 token</strong>：将推理输出的内容（包括但不限于文字、图片）转化为 token 数进行计费。</li>
<li><strong>缓存命中 token</strong>：当你的请求被系统判断命中了缓存内容时，被命中的 token 会按照缓存命中 token 单价来计费，其价格低于输入 token 单价。关于缓存的更多信息，请参考<a href="https://docs.coze.cn/guides/internal_integrations#21651dc4" target="_blank">开启缓存</a>。</li>
</ul>
<h3 id="58d916d6" tabindex="-1">单价</h3>
<p>为项目接入大语言模型内置集成后，项目将支持大语言模型调用能力，根据模型消耗的 token 数量计算并收取费用。每个模型 token 的单价不同，具体如下：</p>
<!-- @cols-width: 188,186,139,168,193 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 188px;" /><col style="width: 186px;" /><col style="width: 139px;" /><col style="width: 168px;" /><col style="width: 193px;" /></colgroup><thead>
<tr>
<th>
<p><strong>模型名称/计费项</strong></p>
</th>
<th>
<p><strong>条件（千 tokens）</strong></p>
</th>
<th>
<p><strong>输入/输出/缓存命中</strong></p>
</th>
<th>
<p><strong>单价-积分结算</strong></p>
<p><strong>（积分/千tokens）</strong></p>
</th>
<th>
<p><strong>单价-现金结算</strong></p>
<p><strong>（元/千tokens）</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="9">doubao-seed-2.0-pro</td>
<td rowspan="3">输入长度 [0, 32]</td>
<td>输入</td>
<td>3.2</td>
<td>0.0032</td>
</tr>
<tr>
<td>输出</td>
<td>16</td>
<td>0.016</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.64</td>
<td>0.00064</td>
</tr>
<tr>
<td rowspan="3">输入长度  (32, 128]</td>
<td>输入</td>
<td>4.8</td>
<td>0.0048</td>
</tr>
<tr>
<td>输出</td>
<td>24</td>
<td>0.024</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.96</td>
<td>0.00096</td>
</tr>
<tr>
<td rowspan="3">输入长度(128, 256]</td>
<td>输入</td>
<td>9.6</td>
<td>0.0096</td>
</tr>
<tr>
<td>输出</td>
<td>48</td>
<td>0.048</td>
</tr>
<tr>
<td>缓存命中</td>
<td>1.92</td>
<td>0.00192</td>
</tr>
<tr>
<td rowspan="9">doubao-seed-2.0-lite</td>
<td rowspan="3">输入长度 [0, 32]</td>
<td>输入</td>
<td>0.6</td>
<td>0.0006</td>
</tr>
<tr>
<td>输出</td>
<td>3.6</td>
<td>0.0036</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.12</td>
<td>0.00012</td>
</tr>
<tr>
<td rowspan="3">输入长度  (32, 128]</td>
<td>输入</td>
<td>0.9</td>
<td>0.0009</td>
</tr>
<tr>
<td>输出</td>
<td>5.4</td>
<td>0.0054</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.18</td>
<td>0.00018</td>
</tr>
<tr>
<td rowspan="3">输入长度(128, 256]</td>
<td>输入</td>
<td>1.8</td>
<td>0.0018</td>
</tr>
<tr>
<td>输出</td>
<td>10.8</td>
<td>0.0108</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.36</td>
<td>0.00036</td>
</tr>
<tr>
<td rowspan="9">doubao-seed-2.0-mini</td>
<td rowspan="3">输入长度 [0, 32]</td>
<td>输入</td>
<td>0.2</td>
<td>0.0002</td>
</tr>
<tr>
<td>输出</td>
<td>2</td>
<td>0.002</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.04</td>
<td>0.00004</td>
</tr>
<tr>
<td rowspan="3">输入长度  (32, 128]</td>
<td>输入</td>
<td>0.4</td>
<td>0.0004</td>
</tr>
<tr>
<td>输出</td>
<td>4</td>
<td>0.004</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.08</td>
<td>0.00008</td>
</tr>
<tr>
<td rowspan="3">输入长度(128, 256]</td>
<td>输入</td>
<td>0.8</td>
<td>0.0008</td>
</tr>
<tr>
<td>输出</td>
<td>8</td>
<td>0.008</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.16</td>
<td>0.00016</td>
</tr>
<tr>
<td rowspan="9">
<p>GLM-4.7</p>
</td>
<td rowspan="3">
<p>输入长度 [0, 32]且</p>
<p>输出长度 [0, 0.2]</p>
<blockquote>
<p>对应<strong>GLM-4.7-特惠区推理</strong>计费项</p>
</blockquote>
</td>
<td>
<p>输入</p>
</td>
<td>
<p>2</p>
</td>
<td>
<p>0.002</p>
</td>
</tr>
<tr>
<td>输出</td>
<td>8</td>
<td>0.008</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.4</td>
<td>0.0004</td>
</tr>
<tr>
<td rowspan="3">
<p>输入长度 [0, 32] 且</p>
<p>输出长度 (0.2, +∞)</p>
</td>
<td>
<p>输入</p>
</td>
<td>
<p>3</p>
</td>
<td>
<p>0.003</p>
</td>
</tr>
<tr>
<td>输出</td>
<td>14</td>
<td>0.014</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.6</td>
<td>0.0006</td>
</tr>
<tr>
<td rowspan="3">输入长度  (32, 200]</td>
<td>输入</td>
<td>4</td>
<td>0.004</td>
</tr>
<tr>
<td>输出</td>
<td>16</td>
<td>0.016</td>
</tr>
<tr>
<td>缓存命中</td>
<td>0.8</td>
<td>0.0008</td>
</tr>
</tbody>
</table>
</div><h2 id="c9f203d3" tabindex="-1">生图模型</h2>
<p>为项目接入生图模型内置集成后，项目将支持图片生成功能，根据生成图片的张数计算并收取费用。生图模型的单价如下：</p>
<!-- @cols-width: 189,227,205,220 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 189px;" /><col style="width: 227px;" /><col style="width: 205px;" /><col style="width: 220px;" /></colgroup><thead>
<tr>
<th><strong>模型名称</strong></th>
<th><strong>计费项</strong></th>
<th><strong>单价-积分结算（积分/张）</strong></th>
<th><strong>单价-现金结算（元/张）</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Doubao-Seedream-5.0</td>
<td>文生图-Seedream 5.0</td>
<td>220</td>
<td>0.22</td>
</tr>
<tr>
<td>图生图-Seedream 5.0</td>
<td>220</td>
<td>0.22</td>
</tr>
<tr>
<td rowspan="2">Doubao-Seedream-4.5</td>
<td>文生图-Seedream 4.5</td>
<td>250</td>
<td>0.25</td>
</tr>
<tr>
<td>图生图-Seedream 4.5</td>
<td>250</td>
<td>0.25</td>
</tr>
</tbody>
</table>
</div><h2 id="c9330b00" tabindex="-1">视频生成大模型</h2>
<p>为项目接入视频生成大模型内置集成后，项目将支持视频生成功能，根据生成视频消耗的 token 计算并收取费用。视频生成大模型的单价如下：</p>
<!-- @cols-width: 190,217,231,223 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 190px;" /><col style="width: 217px;" /><col style="width: 231px;" /><col style="width: 223px;" /></colgroup><thead>
<tr>
<th><strong>模型名称</strong></th>
<th><strong>计费项</strong></th>
<th><strong>单价-积分结算（积分/千tokens）</strong></th>
<th><strong>单价-现金结算（元/千tokens）</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">seedance-1.5pro</td>
<td>有声视频</td>
<td>16</td>
<td>0.016</td>
</tr>
<tr>
<td>无声视频</td>
<td>8</td>
<td>0.008</td>
</tr>
</tbody>
</table>
</div><h2 id="9cec8703" tabindex="-1">语音大模型</h2>
<p>为项目接入语音大模型内置集成后，项目将支持语音合成、语音识别功能，根据语音合成的总字符数或语音识别的音频时长计算并收取费用。语音大模型的单价如下：</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<ul data-style="0">
<li>字符是指计算机中使用的文字和符号等，1 个汉字、英文字母、希腊字母、标点符号、特殊符号、空格、回车等都算 1 个字符。</li>
<li>语音识别根据小时计算费用，不足 1 小时部分，将按比例折算。</li>
</ul>
</div>
<!-- @cols-width: 295,220,283 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 295px;" /><col style="width: 220px;" /><col style="width: 283px;" /></colgroup><thead>
<tr>
<th><strong>计费项</strong></th>
<th><strong>单价-积分结算（积分）</strong></th>
<th><strong>单价-现金结算（元）</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>大模型录音文件识别（极速版）</td>
<td>4500 积分/小时</td>
<td>4.5 元/小时</td>
</tr>
<tr>
<td>豆包语音合成2.0-系统音色文字转语音字数</td>
<td>0.3 积分/字符</td>
<td>0.0003 元/字符</td>
</tr>
</tbody>
</table>
</div><h2 id="dba8e094" tabindex="-1">联网搜索</h2>
<p>为项目接入联网搜索内置集成后，项目将支持联网搜索功能，根据搜索 API 的调用次数计算并收取费用。联网搜索的单价如下：</p>
<!-- @cols-width: 163,222,234 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 163px;" /><col style="width: 222px;" /><col style="width: 234px;" /></colgroup><thead>
<tr>
<th><strong>计费项</strong></th>
<th><strong>单价-积分结算（积分/次）</strong></th>
<th><strong>单价-现金结算（元/次）</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>联网搜索</td>
<td>20</td>
<td>0.02</td>
</tr>
</tbody>
</table>
</div><h2 id="b02e961a" tabindex="-1">内容处理</h2>
<p>内容处理包括链接提取、视频剪辑两个集成服务。</p>
<ul data-style="0">
<li>链接提取：提供 URL 即可快速抓取并解析多类型网页内容的通用工具，根据工具调用次数计算并收取费用。</li>
<li>视频剪辑：为项目接入内容处理内置集成后，项目将支持视频剪辑功能。内容处理内置集成的计费方式为<strong>单价✖️抵扣系数✖️时长（分钟）</strong>，对应单价如下：<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>输出视频或音频的时长不足 1 分钟的部分，将按实际秒数折算，例如 1 分 30 秒折算为 1.5 分钟。</p>
</div>
</li>
</ul>
<!-- @cols-width: 163,224,233 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 163px;" /><col style="width: 224px;" /><col style="width: 233px;" /></colgroup><thead>
<tr>
<th><strong>计费项</strong></th>
<th><strong>单价-积分结算</strong></th>
<th><strong>单价-现金结算</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>链接提取</td>
<td>30（积分/次）</td>
<td>0.03（元/次）</td>
</tr>
<tr>
<td>视频剪辑</td>
<td>10（积分/分钟）</td>
<td>0.01（元/分钟）</td>
</tr>
</tbody>
</table>
</div><p>其中，不同视频剪辑工具输出不同分辨率的视频或音频时，对应的抵扣系数不同，抵扣系数列表如下。</p>
<p>例如调用 audio_to_subtitle 工具输出一个 90 秒视频，视频分辨率固定为 1080P，则该工具对应的计费抵扣系数为 7，消耗的积分为 <code>10 积分/分钟 ✖️ 7（系数） ✖️ 1.5 分钟    = 105 积分</code><strong>。</strong></p>
<!-- @cols-width: 239,396 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 239px;" /><col style="width: 396px;" /></colgroup><thead>
<tr>
<th><strong>工具</strong></th>
<th><strong>抵扣系数</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>concat_videos</p>
</td>
<td rowspan="5">
<p>该类工具中，不同视频输出规格对应的抵扣系数如下：</p>
<ul data-style="0">
<li>4K（3840x2160）分辨率及以下：24</li>
<li>2K（2560x1440）分辨率及以下：12</li>
<li>1080P（1920x1080)分辨率及以下：6</li>
<li>720P（1280x720）分辨率及以下：3</li>
<li>540P （720x540）分辨率及以下：2</li>
<li>480P （640x480）分辨率及以下：1.5</li>
<li>360P（480x360）分辨率及以下：1</li>
<li>音频：1</li>
</ul>
</td>
</tr>
<tr>
<td>add_subtitles</td>
</tr>
<tr>
<td>audio_extract</td>
</tr>
<tr>
<td>video_trim</td>
</tr>
<tr>
<td>compile_video_audio</td>
</tr>
<tr>
<td>audio_to_subtitle</td>
<td>7</td>
</tr>
</tbody>
</table>
</div></div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/coze_pro_task_fee" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">扣子编程任务费用</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/coze_pro_service_hosting_fee" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">部署服务托管费用</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="大语言模型" href="#58d09be6" data-href="#58d09be6">大语言模型</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="计费公式" href="#4ab3eb91" data-href="#4ab3eb91">计费公式</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="单价" href="#58d916d6" data-href="#58d916d6">单价</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="生图模型" href="#c9f203d3" data-href="#c9f203d3">生图模型</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="视频生成大模型" href="#c9330b00" data-href="#c9330b00">视频生成大模型</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="语音大模型" href="#9cec8703" data-href="#9cec8703">语音大模型</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="联网搜索" href="#dba8e094" data-href="#dba8e094">联网搜索</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="内容处理" href="#b02e961a" data-href="#b02e961a">内容处理</a></div></div></div></div></div></div></div></div>
</body></html>