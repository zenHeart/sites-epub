<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">查看智能体配置</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/5956.1729cb00c0.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.ca52691239.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/developer_guides_get_metadata_draft_published"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/developer_guides_get_metadata_draft_published.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="description" content="该文档介绍了查看智能体配置的相关内容，包括请求方式、参数及返回参数等。通过特定接口，可依据智能体ID查看其已发布或草稿版本的配置信息，详细说明了请求各参数的具体要求和含义，以及返回参数所包含的内容，为开发者提供了查看智能体配置的操作指南。"/><meta data-react-helmet="true" name="keywords" content="智能体配置,请求参数,返回参数,查看接口"/><meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
  
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/developer_guides_get_metadata_draft_published" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b97434bdbc784e3ce84ce" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a55df9a4bdbc784e3c9738f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf30d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf317" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf31d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf325" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf334" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf32e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf35a" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf362" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8e614bdbc784e3cce185" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3e2c" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3ece" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_coze_api_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="API 介绍">API 介绍</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ed4" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_changelog" data-discover="true"><span class="nodeTitle-ONnqtP" title="更新日志">更新日志</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3edc" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_preparation" data-discover="true"><span class="nodeTitle-ONnqtP" title="准备工作">准备工作</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ee3" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_api_playground" data-discover="true"><span class="nodeTitle-ONnqtP" title="API Playground">API Playground</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e32" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="鉴权">鉴权</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e6a" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能体和应用">智能体和应用</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3e72" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_create_bot" data-discover="true"><span class="nodeTitle-ONnqtP" title="创建智能体">创建智能体</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e79" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_update_bot" data-discover="true"><span class="nodeTitle-ONnqtP" title="更新智能体">更新智能体</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e81" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_publish_bot" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布智能体">发布智能体</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e87" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_bots_list_draft_published" data-discover="true"><span class="nodeTitle-ONnqtP" title="查看智能体列表">查看智能体列表</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e8e" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:56px" href="/developer_guides_get_metadata_draft_published" data-discover="true"><span class="nodeTitle-ONnqtP" title="查看智能体配置">查看智能体配置</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e95" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_switch_bot_develop_mode" data-discover="true"><span class="nodeTitle-ONnqtP" title="开启或关闭智能体多人协作">开启或关闭智能体多人协作</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e9c" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_add_bot_collaborator" data-discover="true"><span class="nodeTitle-ONnqtP" title="添加智能体的协作者">添加智能体的协作者</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ea4" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_add_app_collaborator" data-discover="true"><span class="nodeTitle-ONnqtP" title="添加应用的协作者">添加应用的协作者</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3eaa" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_remove_bot_collaborator" data-discover="true"><span class="nodeTitle-ONnqtP" title="删除智能体的协作者">删除智能体的协作者</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3eb2" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_remove_app_collaborator" data-discover="true"><span class="nodeTitle-ONnqtP" title="删除应用的协作者">删除应用的协作者</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3eb9" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_list_bot_versions" data-discover="true"><span class="nodeTitle-ONnqtP" title="查看智能体版本列表">查看智能体版本列表</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ec0" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_copy_resource_task" data-discover="true"><span class="nodeTitle-ONnqtP" title="复制资源">复制资源</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ec8" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_query_resource_copy_execution_result" data-discover="true"><span class="nodeTitle-ONnqtP" title="查询资源复制的结果">查询资源复制的结果</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fb5" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_unpublish_agent" data-discover="true"><span class="nodeTitle-ONnqtP" title="下架智能体">下架智能体</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fbd" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_bot_object" data-discover="true"><span class="nodeTitle-ONnqtP" title="Bot object">Bot object</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fc4" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_published_apps_list" data-discover="true"><span class="nodeTitle-ONnqtP" title="查看应用列表">查看应用列表</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fcb" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_agent_callback_messages" data-discover="true"><span class="nodeTitle-ONnqtP" title="智能体发布回调事件">智能体发布回调事件</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc429f" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_agent_delete_callback_messages" data-discover="true"><span class="nodeTitle-ONnqtP" title="智能体删除回调事件">智能体删除回调事件</span></a></div><div id="tree-node-6a3b8b8e4bdbc784e3cc4363" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_agent_unpublished_callback_messages" data-discover="true"><span class="nodeTitle-ONnqtP" title="智能体下架回调事件">智能体下架回调事件</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ee9" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="工作空间">工作空间</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3eef" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="文件夹">文件夹</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ef7" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="企业/组织">企业/组织</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3efe" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="会话与消息">会话与消息</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f04" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="对话">对话</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f0c" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f13" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="文件">文件</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f1a" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能音视频">智能音视频</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f35" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="知识库">知识库</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f3b" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="数据库">数据库</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f43" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="插件">插件</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f49" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="变量">变量</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f51" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="渠道">渠道</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f58" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="用量限额">用量限额</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f5f" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="账单与权益">账单与权益</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f66" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="回调">回调</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f84" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_coze_error_codes" data-discover="true"><span class="nodeTitle-ONnqtP" title="错误码">错误码</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f99" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="API 教程">API 教程</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f8a" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_api_faq" data-discover="true"><span class="nodeTitle-ONnqtP" title="API 常见问题">API 常见问题</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fa8" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc529d" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8e4bdbc784e3cc445f" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/developer_guides_coze_cli" data-discover="true"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf33f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf369" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/guides_FAQ" data-discover="true"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>API 参考</span><span class="separator-KB9yMa">/</span><span>智能体和应用</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">查看智能体配置</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">查看智能体配置</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg><span>复制页面</span></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>查看指定智能体的配置信息，你可以查看该智能体已发布版本的配置，或当前草稿版本的配置。</p>
<h2 id="基础信息" tabindex="-1">基础信息</h2>
<!-- @cols-width: 180,680 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 180px;" /><col style="width: 680px;" /></colgroup><thead>
<tr>
<th><strong>请求方式</strong></th>
<th>GET</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>请求地址</strong></p>
</td>
<td>

<div style="position: relative">
	<pre><code class="hljs language-Plain">https://api.coze.cn/v1/bots/:bot_id
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="https://api.coze.cn/v1/bots/:bot_id" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</td>
</tr>
<tr>
<td>
<p><strong>权限</strong></p>
</td>
<td>
<p><code>getMetadata</code></p>
<p>确保调用该接口使用的访问令牌开通了 <code>getMedata</code> 权限，详细信息参考<a href="https://docs.coze.cn/developer_guides/authentication" target="_blank">鉴权方式</a>。</p>
</td>
</tr>
<tr>
<td><strong>接口说明</strong></td>
<td>查看指定智能体的配置信息。</td>
</tr>
</tbody>
</table>
</div><h2 id="请求参数" tabindex="-1">请求参数</h2>
<h3 id="Header" tabindex="-1">Header</h3>
<!-- @cols-width: 144,165,551 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 144px;" /><col style="width: 165px;" /><col style="width: 551px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>取值</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer $AccessToken</td>
<td>用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息，参考<a href="https://docs.coze.cn/developer_guides/preparation" target="_blank">准备工作</a>。</td>
</tr>
<tr>
<td>Content-Type</td>
<td>application/json</td>
<td>解释请求正文的方式。</td>
</tr>
</tbody>
</table>
</div><h3 id="Path" tabindex="-1">Path</h3>
<!-- @cols-width: 100,122,87,166,372 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 122px;" /><col style="width: 87px;" /><col style="width: 166px;" /><col style="width: 372px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>是否必选</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>bot_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>73428668*****</p>
</td>
<td>
<p>要查看的智能体 ID。</p>
<p>进入智能体的开发页面，开发页面 URL 中 <code>bot</code> 参数后的数字就是智能体 ID。例如<code>https://www.coze.cn/space/341****/bot/73428668*****</code>，bot ID 为<code>73428668*****</code>。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>确保该智能体的所属空间已经生成了访问令牌。</p>
</div>
</td>
</tr>
</tbody>
</table>
</div><h3 id="Query" tabindex="-1">Query</h3>
<!-- @cols-width: 136,121,87,165,338 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 136px;" /><col style="width: 121px;" /><col style="width: 87px;" /><col style="width: 165px;" /><col style="width: 338px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>是否必选</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>is_published</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>true</p>
</td>
<td>
<p>根据智能体的发布状态筛选对应版本。默认值为 <code>true</code>。</p>
<ul data-style="0">
<li><code>true</code> ：查看已发布版本的配置。</li>
<li><code>false</code> ：查看当前草稿版本的配置。</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><h2 id="返回参数" tabindex="-1">返回参数</h2>
<!-- @cols-width: 314,142,158,246 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 314px;" /><col style="width: 142px;" /><col style="width: 158px;" /><col style="width: 246px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>data</td>
<td>Object of <a href="#botinfo">BotInfo</a></td>
<td>\</td>
<td>返回的智能体配置信息。</td>
</tr>
<tr>
<td>code</td>
<td>Long</td>
<td>0</td>
<td>调用状态码。0 表示调用成功，其他值表示调用失败，你可以通过 msg 字段判断详细的错误原因。</td>
</tr>
<tr>
<td>
<p>msg</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>“”</p>
</td>
<td>
<p>状态信息。API 调用失败时可通过此字段查看详细错误信息。</p>
<p>状态码为 0 时，msg 默认为空。</p>
</td>
</tr>
<tr>
<td>detail</td>
<td>Object of <a href="#responsedetail">ResponseDetail</a></td>
<td>{“logid”:“1234567890****”}</td>
<td>包含请求的详细日志信息，用于问题排查和调试。</td>
</tr>
</tbody>
</table>
</div><h3 id="botinfo" tabindex="-1">BotInfo</h3>
<!-- @cols-width: 299,142,159,260 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 299px;" /><col style="width: 142px;" /><col style="width: 159px;" /><col style="width: 260px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>bot_id</td>
<td>String</td>
<td>73428668*****</td>
<td>智能体的唯一标识。</td>
</tr>
<tr>
<td>name</td>
<td>String</td>
<td>新闻</td>
<td>智能体的名称。</td>
</tr>
<tr>
<td>description</td>
<td>String</td>
<td>每天给我推送 AI 相关的新闻。</td>
<td>智能体的描述信息。</td>
</tr>
<tr>
<td>icon_url</td>
<td>String</td>
<td><a href="https://example.com/icon.png" target="_blank">https://example.com/icon.png</a></td>
<td>智能体的头像地址，用于展示智能体的图标。</td>
</tr>
<tr>
<td>create_time</td>
<td>Long</td>
<td>1715689059</td>
<td>创建时间，格式为 10 位的 Unixtime 时间戳，单位为秒（s）。</td>
</tr>
<tr>
<td>update_time</td>
<td>Long</td>
<td>1716388526</td>
<td>更新时间，格式为 10 位的 Unixtime 时间戳，单位为秒（s）。</td>
</tr>
<tr>
<td>version</td>
<td>String</td>
<td>171638852****</td>
<td>智能体最新版本的版本号。</td>
</tr>
<tr>
<td>prompt_info</td>
<td>Object of <a href="#promptinfo">PromptInfo</a></td>
<td>{“prompt”: “调用getToutiaoNews工具推送最新的科技新闻。”}</td>
<td>智能体的提示词配置。</td>
</tr>
<tr>
<td>onboarding_info</td>
<td>Object of <a href="#onboardinginfov2">OnboardingInfoV2</a></td>
<td>{ “prologue”: “你好，我可以为你提供最新、最有趣的科技新闻。让我们一起探索科技的世界吧！”, “suggested_questions”: [ “你能给我推荐一些最新的科技新闻吗？”, “你知道最近有哪些科技趋势吗？”, “你能告诉我如何获得更多关于科技的信息吗？” ] }</td>
<td>智能体的开场白配置。</td>
</tr>
<tr>
<td>
<p>bot_mode</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>智能体模式，取值：</p>
<ul data-style="0">
<li><strong>0</strong>：单 Agent 模式</li>
<li><strong>1</strong>：多 Agent 模式</li>
</ul>
</td>
</tr>
<tr>
<td>plugin_info_list</td>
<td>Array of <a href="#plugininfo">PluginInfo</a></td>
<td>[{“plugin_id”:“730197029480849****”,“name”:“头条新闻”,“icon_url”:“<a href="https://example.com/plugin_icon.png" target="_blank">https://example.com/plugin_icon.png</a>”,“description”:“持续更新，了解最新的头条新闻和新闻文章。”,“api_info_list”:[{“api_id”:“730197029480851****”,“name”:“getToutiaoNews”,“description”:“搜索新闻讯息”}]}]</td>
<td>智能体配置的插件列表，包含插件的名称、图标、描述及工具信息。</td>
</tr>
<tr>
<td>model_info</td>
<td>Object of <a href="#modelinfo">ModelInfo</a></td>
<td>{“top_k”:50,“top_p”:1,“model_id”:“1706077826”,“max_tokens”:4096,“model_name”:“豆包·Function call模型”,“parameters”:{“thinking_type”:“enabled”},“temperature”:1,“context_round”:30,“response_format”:“text”,“presence_penalty”:0,“frequency_penalty”:0}</td>
<td>智能体绑定的模型配置信息，包括模型 ID、名称、生成参数等。</td>
</tr>
<tr>
<td>folder_id</td>
<td>String</td>
<td>752316125533***</td>
<td>智能体所属的文件夹 ID。</td>
</tr>
<tr>
<td>knowledge</td>
<td>Object of <a href="#commonknowledge">CommonKnowledge</a></td>
<td>{ “knowledge_infos”: [ { “id”: “738694398580390****”, “name”: “text” } ] }</td>
<td>智能体绑定的知识库。</td>
</tr>
<tr>
<td>variables</td>
<td>Array of <a href="#variable">Variable</a></td>
<td>-</td>
<td>智能体配置的变量列表。</td>
</tr>
<tr>
<td>media_config</td>
<td>Object of <a href="#mediaconfig">MediaConfig</a></td>
<td>{“is_voice_call_closed”:false}</td>
<td>智能体的语音通话配置，是否关闭语音通话功能。</td>
</tr>
<tr>
<td>owner_user_id</td>
<td>String</td>
<td>368567*****</td>
<td>智能体创建者的扣子用户 ID。</td>
</tr>
<tr>
<td>voice_info_list</td>
<td>Array of <a href="#voice">Voice</a></td>
<td>[ { “voice_id”: “7468512265134800000”, “language_code”: “zh” } ]</td>
<td>智能体配置的音色。</td>
</tr>
<tr>
<td>shortcut_commands</td>
<td>Array of <a href="#shortcutcommandinfo">ShortcutCommandInfo</a></td>
<td>[{“id”:“745701083352557****”,“name”:“示例快捷指令”,“command”:“/sc_demo”,“description”:“快捷指令示例”,“query_template”:“搜索今天的新闻讯息”,“icon_url”:“<a href="https://" target="_blank">https://</a>****”,“components”:[{“name”:“query”,“description”:“新闻搜索关键词”,“type”:“text”,“tool_parameter”:“query”,“default_value”:“”,“is_hide”:false}],“tool”:{“name”:“头条新闻”,“type”:“plugin”}}]</td>
<td>智能体配置的快捷指令。</td>
</tr>
<tr>
<td>workflow_info_list</td>
<td>Array of <a href="#workflowinfo">WorkflowInfo</a></td>
<td>[{“id”:“746049108611037****”,“name”:“示例工作流”,“description”:“工作流示例”,“icon_url”:“<a href="https://example.com/workflow_icon.png" target="_blank">https://example.com/workflow_icon.png</a>”}]</td>
<td>智能体配置的工作流列表，包含工作流的 ID、名称、图标及描述信息。</td>
</tr>
<tr>
<td>background_image_info</td>
<td>Object of <a href="#backgroundimageinfo">BackgroundImageInfo</a></td>
<td>\</td>
<td>智能体背景的图片配置信息，包含 Web 端和移动端的背景图 URL、主题颜色、裁剪位置及渐变效果等。</td>
</tr>
<tr>
<td>
<p>default_user_input_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>text</p>
</td>
<td>
<p>默认的用户输入方式。枚举值如下：</p>
<ul data-style="0">
<li>text：打字输入。</li>
<li>voice：语音输入。</li>
<li>call：语音通话。</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><h3 id="promptinfo" tabindex="-1">PromptInfo</h3>
<!-- @cols-width: 182,146,164,368 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 182px;" /><col style="width: 146px;" /><col style="width: 164px;" /><col style="width: 368px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>prompt</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>你是一位经验丰富的中餐大厨，能够熟练传授各类中餐的烹饪技巧，每日为大学生厨师小白教学一道经典中餐的制作方法。</p>
</td>
<td>
<p>智能体的人设与回复逻辑。长度为 0~ 20,000 个字符。默认为空。</p>
<p>开启前缀缓存后，不支持通过 <code>prompt</code> 参数设置提示词，需要通过 <code>prefix_prompt_info</code> 参数设置提示词。</p>
</td>
</tr>
<tr>
<td>
<p>prompt_mode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>standard</p>
</td>
<td>
<p>提示词模式，用于指定智能体的人设与回复逻辑的配置方式。枚举值：</p>
<ul data-style="0">
<li><code>standard</code>（默认值）：标准模式。未开启前缀缓存时使用该模式。</li>
<li><code>prefix</code>：前缀缓存模式，提示词会分为缓存提示词和非缓存提示词两部分。开启前缀缓存后需要设置为该模式。</li>
</ul>
</td>
</tr>
<tr>
<td>prefix_prompt_info</td>
<td>Object of <a href="#prefixpromptinfo">PrefixPromptInfo</a></td>
<td>\</td>
<td>通过 <code>cache_type</code> 或 <code>parameters.caching.type</code>开启前缀缓存后，你需要通过该参数设置<strong>缓存提示词</strong>（<code>prefix_prompt</code>）和 <strong>非缓存提示词</strong>（<code>dynamic_prompt</code>）。不支持通过 <code>prompt</code> 参数设置提示词。</td>
</tr>
</tbody>
</table>
</div><h3 id="prefixpromptinfo" tabindex="-1">PrefixPromptInfo</h3>
<!-- @cols-width: 163,147,164,386 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 163px;" /><col style="width: 147px;" /><col style="width: 164px;" /><col style="width: 386px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>prefix_prompt</td>
<td>String</td>
<td>\</td>
<td>缓存提示词，大量重复出现的固定规则、模板框架或背景信息，用于指引大模型输出格式与风格。扣子编程会将其缓存并复用，大模型无需重新解析这部分固定信息。</td>
</tr>
<tr>
<td>dynamic_prompt</td>
<td>String</td>
<td>\</td>
<td>非缓存提示词，动态变化的个性化信息，仅针对当前请求生效。</td>
</tr>
</tbody>
</table>
</div><h3 id="onboardinginfov2" tabindex="-1">OnboardingInfoV2</h3>
<!-- @cols-width: 196,146,163,355 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 196px;" /><col style="width: 146px;" /><col style="width: 163px;" /><col style="width: 355px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>prologue</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>你好，我可以为你提供最新、最有趣的科技新闻。让我们一起探索科技的世界吧！</p>
</td>
<td>
<p>智能体配置的开场白内容。</p>
<p>开场白中如果设置了用户名称变量<code>{{user_name}}</code>，API 场景中需要业务方自行处理，例如展示开场白时将此变量替换为业务侧的用户名称。</p>
</td>
</tr>
<tr>
<td>suggested_questions</td>
<td>Array of String</td>
<td>[“你能给我推荐一些最新的科技新闻吗？”,“你知道最近有哪些科技趋势吗？”,“你能告诉我如何获得更多关于科技的信息吗？”]</td>
<td>智能体配置的推荐问题列表。未开启用户问题建议时，不返回此字段。</td>
</tr>
</tbody>
</table>
</div><h3 id="plugininfo" tabindex="-1">PluginInfo</h3>
<!-- @cols-width: 143,147,165,405 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 143px;" /><col style="width: 147px;" /><col style="width: 165px;" /><col style="width: 405px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>plugin_id</td>
<td>String</td>
<td>730197029480849****</td>
<td>插件唯一标识。</td>
</tr>
<tr>
<td>name</td>
<td>String</td>
<td>头条新闻</td>
<td>插件名称。</td>
</tr>
<tr>
<td>icon_url</td>
<td>String</td>
<td><a href="https://example.com/plugin_icon.png" target="_blank">https://example.com/plugin_icon.png</a></td>
<td>插件的头像地址，用于展示插件的图标。</td>
</tr>
<tr>
<td>description</td>
<td>String</td>
<td>持续更新，了解最新的头条新闻和新闻文章。</td>
<td>插件的描述信息，用于说明插件的功能或用途。</td>
</tr>
<tr>
<td>api_info_list</td>
<td>Array of <a href="#apiinfo">ApiInfo</a></td>
<td>[ { “api_id”: “730197029480851****”, “name”: “getToutiaoNews”, “description”: “搜索新闻讯息” } ]</td>
<td>插件的工具列表信息。</td>
</tr>
</tbody>
</table>
</div><h3 id="apiinfo" tabindex="-1">ApiInfo</h3>
<!-- @cols-width: 128,148,165,419 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 128px;" /><col style="width: 148px;" /><col style="width: 165px;" /><col style="width: 419px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>api_id</td>
<td>String</td>
<td>730197029480851****</td>
<td>插件工具的 ID。</td>
</tr>
<tr>
<td>name</td>
<td>String</td>
<td>getToutiaoNews</td>
<td>插件工具的名称。</td>
</tr>
<tr>
<td>description</td>
<td>String</td>
<td>搜索新闻讯息</td>
<td>插件工具的描述。</td>
</tr>
</tbody>
</table>
</div><h3 id="modelinfo" tabindex="-1">ModelInfo</h3>
<!-- @cols-width: 174,147,164,375 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 174px;" /><col style="width: 147px;" /><col style="width: 164px;" /><col style="width: 375px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>top_k</td>
<td>Integer</td>
<td>50</td>
<td>生成文本时，采样候选集的大小。该参数控制模型在生成每个词时考虑的候选词数量，值越小生成的文本越保守和确定，值越大生成的文本越多样和随机。</td>
</tr>
<tr>
<td>top_p</td>
<td>Double</td>
<td>1</td>
<td>Top P 采样参数，用于控制生成文本时的多样性。取值范围为 <code>0</code> 到 <code>1</code>，值越小生成的文本越保守和确定，值越大生成的文本越多样和随机。</td>
</tr>
<tr>
<td>model_id</td>
<td>String</td>
<td>1706077826</td>
<td>智能体绑定的模型的 ID。</td>
</tr>
<tr>
<td>max_tokens</td>
<td>Integer</td>
<td>4096</td>
<td>模型输出的 Tokens 长度上限。</td>
</tr>
<tr>
<td>model_name</td>
<td>String</td>
<td>豆包·Function call模型</td>
<td>智能体绑定的模型名称。</td>
</tr>
<tr>
<td>
<p>parameters</p>
</td>
<td>
<p>JSON Map</p>
</td>
<td>
<p>{“thinking_type”: “enabled”}</p>
</td>
<td>
<p>模型深度思考相关配置。开发者可以设置开启或关闭深度思考，从而灵活控制模型在交互过程中的 Token 消耗。</p>
<p><code>thinking_type</code> 的值可以设置为：</p>
<ul data-style="0">
<li><code>enabled</code>：（默认值）开启深度思考。智能体在与用户对话时会先输出一段思维链内容，通过逐步拆解问题、梳理逻辑，提升最终输出答案的准确性。但该模式会因额外的推理步骤消耗更多 Token。</li>
</ul>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>开启深度思考后：</p>
<ul data-style="0">
<li>模型不支持 Function Call，即工具调用。</li>
<li>智能体不能使用插件、触发器、变量、数据库、文件盒子、不能添加工作流和对话流。</li>
<li>不支持使用插件和工作流相关的快捷指令。</li>
</ul>
</div>
<ul data-style="0">
<li><code>disabled</code>：关闭深度思考。智能体将直接生成最终答案，不再经过额外的思维链推理过程，可有效降低 Token 消耗，提升响应速度。</li>
<li><code>auto</code>：当前仅<strong>豆包·1.6·自动深度思考·多模态模型</strong>支持该参数。启用自动模式后，模型会根据对话内容的复杂度，自动判断是否启用深度思考</li>
</ul>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>当前仅如下模型支持深度思考开关配置：</p>
<ul data-style="0">
<li>豆包·1.6·自动深度思考·多模态模型</li>
<li>豆包·1.6·极致速度·多模态模型</li>
<li>豆包·1.5·Pro·视觉深度思考</li>
<li>豆包·GUI·Agent模型</li>
</ul>
</div>
</td>
</tr>
<tr>
<td>temperature</td>
<td>Double</td>
<td>1</td>
<td>生成随机性。</td>
</tr>
<tr>
<td>context_round</td>
<td>Integer</td>
<td>30</td>
<td>携带上下文轮数。</td>
</tr>
<tr>
<td>
<p>response_format</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>text</p>
</td>
<td>
<p>输出格式。枚举值：</p>
<ul data-style="0">
<li>text：文本。</li>
<li>markdown：Markdown 格式。</li>
<li>json：json 格式。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>presence_penalty</p>
</td>
<td>
<p>Double</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>重复主题惩罚。用于控制模型输出相同主题的频率。</p>
<p>当该值为正时，会阻止模型频繁讨论相同的主题，从而增加输出内容的多样性。</p>
</td>
</tr>
<tr>
<td>
<p>frequency_penalty</p>
</td>
<td>
<p>Double</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>重复语句惩罚。用于控制模型输出重复语句的频率。</p>
<p>当该值为正时，会阻止模型频繁使用相同的词汇和短语，从而增加输出内容的多样性。</p>
</td>
</tr>
<tr>
<td>
<p>api_mode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>chat_api</p>
</td>
<td>
<p>模型的 API 协议类型，用于指定智能体与模型交互时使用的 API 协议。枚举值：</p>
<ul data-style="0">
<li><code>chat_api</code>：智能体需要在请求时带上对话历史作为上下文。适用于日常闲聊、基础咨询、简单文本生成等轻量化需求。</li>
<li><code>responses_api</code>：模型新推出的 API，不仅延续了 Chat API 的易用性，还原生支持高效的上下文管理和前缀缓存。适用于需要多步推理等复杂任务链处理的场景。</li>
</ul>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>仅部分模型支持<code>responses_api</code>协议，具体支持的模型请参见<a href="https://docs.coze.cn/developer_guides/model_api_param_support" target="_blank">模型能力差异</a>。</p>
</div>
</td>
</tr>
</tbody>
</table>
</div><h3 id="commonknowledge" tabindex="-1">CommonKnowledge</h3>
<!-- @cols-width: 166,147,164,383 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 166px;" /><col style="width: 147px;" /><col style="width: 164px;" /><col style="width: 383px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>knowledge_infos</td>
<td>Array of <a href="#knowledgeinfo">KnowledgeInfo</a></td>
<td>[ { “id”: “738694398580390****”, “name”: “text” } ]</td>
<td>智能体绑定的知识库信息。</td>
</tr>
</tbody>
</table>
</div><h3 id="knowledgeinfo" tabindex="-1">KnowledgeInfo</h3>
<!-- @cols-width: 100,149,166,445 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 149px;" /><col style="width: 166px;" /><col style="width: 445px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td>String</td>
<td>738694398580390****</td>
<td>知识库 ID。</td>
</tr>
<tr>
<td>name</td>
<td>String</td>
<td>智能助手知识库</td>
<td>知识库名称。</td>
</tr>
</tbody>
</table>
</div><h3 id="variable" tabindex="-1">Variable</h3>
<!-- @cols-width: 152,147,165,396 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 152px;" /><col style="width: 147px;" /><col style="width: 165px;" /><col style="width: 396px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>enable</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>true</p>
</td>
<td>
<p>是否启用该变量。</p>
<ul data-style="0">
<li>true：启用该变量。</li>
<li>false：未启用该变量。</li>
</ul>
</td>
</tr>
<tr>
<td>channel</td>
<td>String</td>
<td>custom</td>
<td>变量的类型。当前只支持展示用户自定义变量（custom）。</td>
</tr>
<tr>
<td>keyword</td>
<td>String</td>
<td>name</td>
<td>变量名。</td>
</tr>
<tr>
<td>description</td>
<td>String</td>
<td>姓名</td>
<td>变量描述。</td>
</tr>
<tr>
<td>default_value</td>
<td>String</td>
<td>-</td>
<td>变量的默认值。</td>
</tr>
<tr>
<td>
<p>prompt_enable</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>true</p>
</td>
<td>
<p>是否允许该变量被 Prompt 访问。</p>
<ul data-style="0">
<li>true：变量支持在 Prompt 中访问。</li>
<li>false：变量不支持在 Prompt 中访问，仅能在工作流中访问。</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><h3 id="mediaconfig" tabindex="-1">MediaConfig</h3>
<!-- @cols-width: 189,146,163,362 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 189px;" /><col style="width: 146px;" /><col style="width: 163px;" /><col style="width: 362px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>is_voice_call_closed</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>false</p>
</td>
<td>
<p>是否关闭智能体的语音通话功能。</p>
<ul data-style="0">
<li><code>true</code>：关闭语音通话。</li>
<li><code>false</code>：开启语音通话（默认）。</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><h3 id="voice" tabindex="-1">Voice</h3>
<!-- @cols-width: 153,147,165,395 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 153px;" /><col style="width: 147px;" /><col style="width: 165px;" /><col style="width: 395px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>voice_id</td>
<td>String</td>
<td>7468512265134899251</td>
<td>音色的 ID。获取方法请参见<a href="https://docs.coze.cn/developer_guides/list_voices" target="_blank">查看音色列表</a>。</td>
</tr>
<tr>
<td>language_code</td>
<td>String</td>
<td>zh</td>
<td>此音色的语种代号。获取方法请参见<a href="https://docs.coze.cn/developer_guides/list_voices" target="_blank">查看音色列表</a>。</td>
</tr>
</tbody>
</table>
</div><h3 id="shortcutcommandinfo" tabindex="-1">ShortcutCommandInfo</h3>
<!-- @cols-width: 216,145,162,337 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 216px;" /><col style="width: 145px;" /><col style="width: 162px;" /><col style="width: 337px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td>String</td>
<td>745701083352557****</td>
<td>快捷指令的唯一标识。</td>
</tr>
<tr>
<td>name</td>
<td>String</td>
<td>示例快捷指令</td>
<td>快捷指令的按钮名称。</td>
</tr>
<tr>
<td>tool</td>
<td>Object of <a href="#shortcutcommandtoolinfo">ShortcutCommandToolInfo</a></td>
<td>{“name”:“头条新闻”,“type”:“plugin”}</td>
<td>快捷指令使用的工具信息。</td>
</tr>
<tr>
<td>command</td>
<td>String</td>
<td>/sc_demo</td>
<td>快捷指令的指令名称。</td>
</tr>
<tr>
<td>agent_id</td>
<td>String</td>
<td>745705134267144****</td>
<td>对于多 Agent 类型的智能体，此参数返回快捷指令指定回答的节点 ID。</td>
</tr>
<tr>
<td>icon_url</td>
<td>String</td>
<td><a href="https://example.com/icon***.png" target="_blank">https://example.com/icon***.png</a></td>
<td>快捷指令的图标地址。</td>
</tr>
<tr>
<td>description</td>
<td>String</td>
<td>快捷指令示例</td>
<td>快捷指令的描述。</td>
</tr>
<tr>
<td>query_template</td>
<td>String</td>
<td>搜索今天的新闻讯息</td>
<td>快捷指令的指令内容。</td>
</tr>
</tbody>
</table>
</div><h3 id="shortcutcommandtoolinfo" tabindex="-1">ShortcutCommandToolInfo</h3>
<!-- @cols-width: 100,149,166,445 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 149px;" /><col style="width: 166px;" /><col style="width: 445px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>name</td>
<td>String</td>
<td>头条新闻</td>
<td>快捷指令的工具名称。</td>
</tr>
<tr>
<td>
<p>type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>plugin</p>
</td>
<td>
<p>工具类型。取值为：</p>
<ul data-style="0">
<li>workflow：工作流。</li>
<li>plugin：插件。</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><h3 id="workflowinfo" tabindex="-1">WorkflowInfo</h3>
<!-- @cols-width: 128,148,165,419 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 128px;" /><col style="width: 148px;" /><col style="width: 165px;" /><col style="width: 419px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td>String</td>
<td>746049108611037****</td>
<td>工作流的 ID。</td>
</tr>
<tr>
<td>name</td>
<td>String</td>
<td>示例工作流</td>
<td>工作流的名称。</td>
</tr>
<tr>
<td>icon_url</td>
<td>String</td>
<td><a href="https://example.com/workflow_icon.png" target="_blank">https://example.com/workflow_icon.png</a></td>
<td>工作流的头像地址，用于展示工作流的图标。</td>
</tr>
<tr>
<td>description</td>
<td>String</td>
<td>工作流示例</td>
<td>工作流的描述。</td>
</tr>
</tbody>
</table>
</div><h3 id="backgroundimageinfo" tabindex="-1">BackgroundImageInfo</h3>
<!-- @cols-width: 233,145,162,320 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 233px;" /><col style="width: 145px;" /><col style="width: 162px;" /><col style="width: 320px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>web_background_image</td>
<td>Object of <a href="#backgroundimagedetail">BackgroundImageDetail</a></td>
<td>-</td>
<td>Web 端背景图。</td>
</tr>
<tr>
<td>mobile_background_image</td>
<td>Object of <a href="#backgroundimagedetail">BackgroundImageDetail</a></td>
<td>-</td>
<td>移动端背景图。</td>
</tr>
</tbody>
</table>
</div><h3 id="backgroundimagedetail" tabindex="-1">BackgroundImageDetail</h3>
<!-- @cols-width: 170,147,164,379 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 170px;" /><col style="width: 147px;" /><col style="width: 164px;" /><col style="width: 379px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>image_url</td>
<td>String</td>
<td><a href="https://example.com/image.jpg" target="_blank">https://example.com/image.jpg</a></td>
<td>背景图片的 URL 地址。</td>
</tr>
<tr>
<td>theme_color</td>
<td>String</td>
<td>#FFFFFF</td>
<td>背景图片的主题颜色，通常用于与图片搭配的其他元素的颜色。格式为十六进制颜色代码。</td>
</tr>
<tr>
<td>canvas_position</td>
<td>Object of <a href="#canvasposition">CanvasPosition</a></td>
<td>{“top”:100,“left”:50,“width”:300,“height”:200}</td>
<td>背景图片在原始图片中的位置坐标及尺寸参数，即背景图片在画布中的实际显示区域范围。包括图片顶部 / 左侧的偏移量、宽度和高度。</td>
</tr>
<tr>
<td>gradient_position</td>
<td>Object of <a href="#gradientposition">GradientPosition</a></td>
<td>{ “left”: 0.0, “right”: 800.0 }</td>
<td>设置背景图渐变效果。通过指定渐变的左右边界位置，控制渐变的起始和结束点，从而实现背景图的渐变效果。</td>
</tr>
</tbody>
</table>
</div><h3 id="canvasposition" tabindex="-1">CanvasPosition</h3>
<!-- @cols-width: 100,149,166,445 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 149px;" /><col style="width: 166px;" /><col style="width: 445px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>top</p>
</td>
<td>
<p>Double</p>
</td>
<td>
<p>100</p>
</td>
<td>
<p>裁剪区域顶部起始坐标，距原始图片顶部的像素值（px）。值越大，裁剪区域越向下移动。</p>
<p><code>top</code> 和 <code>left</code> 的值不能超过画布的实际尺寸</p>
</td>
</tr>
<tr>
<td>left</td>
<td>Double</td>
<td>50</td>
<td>裁剪区域左侧起始坐标，距原始图片左侧的像素值（px）。值越大，裁剪区域越向右移动。</td>
</tr>
<tr>
<td>width</td>
<td>Double</td>
<td>300</td>
<td>裁剪区域的宽度，单位为像素（px）。此值决定了裁剪区域的水平范围，必须为正数。</td>
</tr>
<tr>
<td>height</td>
<td>Double</td>
<td>200</td>
<td>裁剪区域的高度，单位为像素（px）。此值决定了裁剪区域的垂直范围，必须为正数。</td>
</tr>
</tbody>
</table>
</div><h3 id="gradientposition" tabindex="-1">GradientPosition</h3>
<!-- @cols-width: 100,149,166,445 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 149px;" /><col style="width: 166px;" /><col style="width: 445px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>left</td>
<td>Double</td>
<td>0</td>
<td>渐变效果的左侧边界位置，单位为像素（px）。此值表示渐变从画布左侧开始的位置，值越小，渐变起始点越靠近画布左侧。</td>
</tr>
<tr>
<td>right</td>
<td>Double</td>
<td>800</td>
<td>渐变效果的右侧边界位置，单位为像素（px）。此值表示渐变在画布右侧结束的位置，值越大，渐变结束点越靠近画布右侧。</td>
</tr>
</tbody>
</table>
</div><h3 id="responsedetail" tabindex="-1">ResponseDetail</h3>
<!-- @cols-width: 100,149,166,445 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 149px;" /><col style="width: 166px;" /><col style="width: 445px;" /></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>示例</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>logid</td>
<td>String</td>
<td>20241210152726467C48D89D6DB2****</td>
<td>本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考<a href="https://docs.coze.cn/guides/help_and_support" target="_blank">获取帮助和技术支持</a>。</td>
</tr>
</tbody>
</table>
</div><h2 id="示例" tabindex="-1">示例</h2>
<h3 id="请求示例" tabindex="-1">请求示例</h3>

<div style="position: relative">
	<pre><code class="hljs language-JSON">curl --location --request GET &#x27;https<span class="hljs-punctuation">:</span><span class="hljs-comment">//api.coze.cn/v1/bots/749865007353125***?is_published=true&#x27; \</span>
--header &#x27;Authorization<span class="hljs-punctuation">:</span> Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****&#x27; \
--header &#x27;Content-Type<span class="hljs-punctuation">:</span> application/json&#x27;
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location --request GET &apos;https://api.coze.cn/v1/bots/749865007353125***?is_published=true&apos; \
--header &apos;Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****&apos; \
--header &apos;Content-Type: application/json&apos;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h3 id="返回示例" tabindex="-1">返回示例</h3>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;description&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;***&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;bot_mode&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;model_info&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;temperature&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0.8</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;context_round&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">3</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;max_tokens&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">4096</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;model_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;173752***&quot;</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;model_name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;ep-20250122125445-ck9wp&quot;</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;knowledge&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;knowledge_infos&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-punctuation">]</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7515437*****&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;folder_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;752316125533542***&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;version&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;voice_data_list&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;plugin_info_list&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
            <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;api_info_list&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
                    <span class="hljs-punctuation">{</span>
                        <span class="hljs-attr">&quot;description&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;当你需要获取网页、pdf 内容时，使用此工具。可以获取url链接下的标题和内容。&quot;</span><span class="hljs-punctuation">,</span>
                        <span class="hljs-attr">&quot;api_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span>
                        <span class="hljs-attr">&quot;name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;browse&quot;</span>
                    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
                    <span class="hljs-punctuation">{</span>
                        <span class="hljs-attr">&quot;api_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span>
                        <span class="hljs-attr">&quot;name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;search&quot;</span><span class="hljs-punctuation">,</span>
                        <span class="hljs-attr">&quot;description&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;搜索用户询问的内容&quot;</span>
                    <span class="hljs-punctuation">}</span>
                <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;plugin_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7372463719***&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;头条搜索&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;description&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;使用头条的搜索功能来阅读或搜索URL链接，由于个别网站自身站点限制，无法获取网页内容。&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;icon_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;https://example.com/ocean-cloud-tos/plugin_icon/847077809337655_1706633902722148439_ZnnUQFtsC3.png?lk3s=cd508e2b&amp;x-expires=1752598956&amp;x-signature=H9xqNxbMc*****&quot;</span>
            <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
            <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;icon_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;https://example.com/ocean-cloud-tos/plugin_icon/default_icon.png?lk3s=cd508e2b&amp;x-expires=1752598956&amp;x-signature=O8qWv%2F5dCJq****&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;api_info_list&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
                    <span class="hljs-punctuation">{</span>
                        <span class="hljs-attr">&quot;api_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span>
                        <span class="hljs-attr">&quot;name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;sousuo&quot;</span><span class="hljs-punctuation">,</span>
                        <span class="hljs-attr">&quot;description&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;查询解析: 系统需要能够理解用户的查询意图，并将其转换为可执行的搜索指令。\n\n数据库: 一个包含学术资源的大型数据库，如期刊文章、会议论文、学位论文等。\n\n索引: 为了提高搜索效率，数据库中的信息需要被索引，以便快速检索。\n\n搜索算法: 算法需要能够根据相关性对搜索结果进行排序。\n\n过滤和排序: 用户应能够根据日期、作者、出版物、领域等标准过滤和排序结果。\n\n高级搜索选项: 允许用户使用布尔运算符（如AND, OR, NOT）进行更精确的搜索。\n\n摘要和引用: 为每个搜索结果提供简短的摘要和引用信息。\n\n全文访问: 如果可能，提供对全文的访问链接。\n\n个性化: 根据用户的历史搜索和偏好，提供个性化的搜索建议。\n\n反馈机制: 允许用户对搜索结果进行反馈，以改进搜索算法。\n\n安全性和隐私: 确保用户数据的安全，并尊重隐私。\n\n可扩展性: 系统应能够随着数据量的增加而扩展。\n\nAPI: 提供API接口，允许其他应用程序或服务集成搜索功能。\n\n多语言支持: 支持多种语言的搜索和结果展示。\n\n移动兼容性: 确保系统在移动设备上也能良好工作。\n\n辅助功能: 为有特殊需求的用户提供辅助功能，如屏幕阅读器兼容性。\n\n帮助和支持: 提供帮助文档和客户支持。&quot;</span>
                    <span class="hljs-punctuation">}</span>
                <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;plugin_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;736618610612***&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;学术搜索&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;description&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;学术问题？来问我&quot;</span>
            <span class="hljs-punctuation">}</span>
        <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;shortcut_commands&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;owner_1&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;owner_user_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;3290203****&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;prompt_info&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;prompt&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;onboarding_info&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;Prologue&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;嗨，你好！我对各种新鲜事物都很了解哦。&quot;</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;SuggestedQuestions&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
                <span class="hljs-string">&quot;有啥新鲜好玩的地方推荐吗？&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-string">&quot;最近有啥新奇的科技产品吗？&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-string">&quot;哪里能体验到独特的新鲜事物？&quot;</span>
            <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;OnboardingMode&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">2</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;CustomizedOnboardingPrompt&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;SuggestedQuestionsShowMode&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;workflow_info_list&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
            <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;icon_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;https://example.com/plugin_icon/workflow.png?lk3s=81d4c505&amp;x-expires=1750010557&amp;x-signature=D910MNbN%2F****&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;751616845608***&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;summarize_article_1_903&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;description&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;示例：总结提炼文章中的要点&quot;</span>
            <span class="hljs-punctuation">}</span>
        <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;voice_info_list&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;default_user_input_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;background_image_info&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;web_background_image&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;theme_color&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;gradient_position&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;canvas_position&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;origin_image_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;image_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span>
            <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;mobile_background_image&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;origin_image_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;image_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;theme_color&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;gradient_position&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;canvas_position&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span>
            <span class="hljs-punctuation">}</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;update_time&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1749994397</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;icon_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;https://example.com/FileBizType.BIZ_BOT_ICON/***.jpeg&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;suggest_reply_info&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;reply_mode&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;enable&quot;</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;customized_prompt&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;variables&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;create_time&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1749972247</span>
    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;code&quot;: 0,
    &quot;data&quot;: {
        &quot;description&quot;: &quot;***&quot;,
        &quot;bot_mode&quot;: 0,
        &quot;model_info&quot;: {
            &quot;temperature&quot;: 0.8,
            &quot;context_round&quot;: 3,
            &quot;max_tokens&quot;: 4096,
            &quot;model_id&quot;: &quot;173752***&quot;,
            &quot;model_name&quot;: &quot;ep-20250122125445-ck9wp&quot;
        },
        &quot;knowledge&quot;: {
            &quot;knowledge_infos&quot;: []
        },
        &quot;bot_id&quot;: &quot;7515437*****&quot;,
        &quot;folder_id&quot;: &quot;752316125533542***&quot;,
        &quot;version&quot;: &quot;&quot;,
        &quot;voice_data_list&quot;: [],
        &quot;plugin_info_list&quot;: [
            {
                &quot;api_info_list&quot;: [
                    {
                        &quot;description&quot;: &quot;当你需要获取网页、pdf 内容时，使用此工具。可以获取url链接下的标题和内容。&quot;,
                        &quot;api_id&quot;: &quot;0&quot;,
                        &quot;name&quot;: &quot;browse&quot;
                    },
                    {
                        &quot;api_id&quot;: &quot;0&quot;,
                        &quot;name&quot;: &quot;search&quot;,
                        &quot;description&quot;: &quot;搜索用户询问的内容&quot;
                    }
                ],
                &quot;plugin_id&quot;: &quot;7372463719***&quot;,
                &quot;name&quot;: &quot;头条搜索&quot;,
                &quot;description&quot;: &quot;使用头条的搜索功能来阅读或搜索URL链接，由于个别网站自身站点限制，无法获取网页内容。&quot;,
                &quot;icon_url&quot;: &quot;https://example.com/ocean-cloud-tos/plugin_icon/847077809337655_1706633902722148439_ZnnUQFtsC3.png?lk3s=cd508e2b&x-expires=1752598956&x-signature=H9xqNxbMc*****&quot;
            },
            {
                &quot;icon_url&quot;: &quot;https://example.com/ocean-cloud-tos/plugin_icon/default_icon.png?lk3s=cd508e2b&x-expires=1752598956&x-signature=O8qWv%2F5dCJq****&quot;,
                &quot;api_info_list&quot;: [
                    {
                        &quot;api_id&quot;: &quot;0&quot;,
                        &quot;name&quot;: &quot;sousuo&quot;,
                        &quot;description&quot;: &quot;查询解析: 系统需要能够理解用户的查询意图，并将其转换为可执行的搜索指令。\n\n数据库: 一个包含学术资源的大型数据库，如期刊文章、会议论文、学位论文等。\n\n索引: 为了提高搜索效率，数据库中的信息需要被索引，以便快速检索。\n\n搜索算法: 算法需要能够根据相关性对搜索结果进行排序。\n\n过滤和排序: 用户应能够根据日期、作者、出版物、领域等标准过滤和排序结果。\n\n高级搜索选项: 允许用户使用布尔运算符（如AND, OR, NOT）进行更精确的搜索。\n\n摘要和引用: 为每个搜索结果提供简短的摘要和引用信息。\n\n全文访问: 如果可能，提供对全文的访问链接。\n\n个性化: 根据用户的历史搜索和偏好，提供个性化的搜索建议。\n\n反馈机制: 允许用户对搜索结果进行反馈，以改进搜索算法。\n\n安全性和隐私: 确保用户数据的安全，并尊重隐私。\n\n可扩展性: 系统应能够随着数据量的增加而扩展。\n\nAPI: 提供API接口，允许其他应用程序或服务集成搜索功能。\n\n多语言支持: 支持多种语言的搜索和结果展示。\n\n移动兼容性: 确保系统在移动设备上也能良好工作。\n\n辅助功能: 为有特殊需求的用户提供辅助功能，如屏幕阅读器兼容性。\n\n帮助和支持: 提供帮助文档和客户支持。&quot;
                    }
                ],
                &quot;plugin_id&quot;: &quot;736618610612***&quot;,
                &quot;name&quot;: &quot;学术搜索&quot;,
                &quot;description&quot;: &quot;学术问题？来问我&quot;
            }
        ],
        &quot;shortcut_commands&quot;: [],
        &quot;name&quot;: &quot;owner_1&quot;,
        &quot;owner_user_id&quot;: &quot;3290203****&quot;,
        &quot;prompt_info&quot;: {
            &quot;prompt&quot;: &quot;&quot;
        },
        &quot;onboarding_info&quot;: {
            &quot;Prologue&quot;: &quot;嗨，你好！我对各种新鲜事物都很了解哦。&quot;,
            &quot;SuggestedQuestions&quot;: [
                &quot;有啥新鲜好玩的地方推荐吗？&quot;,
                &quot;最近有啥新奇的科技产品吗？&quot;,
                &quot;哪里能体验到独特的新鲜事物？&quot;
            ],
            &quot;OnboardingMode&quot;: 2,
            &quot;CustomizedOnboardingPrompt&quot;: &quot;&quot;,
            &quot;SuggestedQuestionsShowMode&quot;: 0
        },
        &quot;workflow_info_list&quot;: [
            {
                &quot;icon_url&quot;: &quot;https://example.com/plugin_icon/workflow.png?lk3s=81d4c505&x-expires=1750010557&x-signature=D910MNbN%2F****&quot;,
                &quot;id&quot;: &quot;751616845608***&quot;,
                &quot;name&quot;: &quot;summarize_article_1_903&quot;,
                &quot;description&quot;: &quot;示例：总结提炼文章中的要点&quot;
            }
        ],
        &quot;voice_info_list&quot;: [],
        &quot;default_user_input_type&quot;: &quot;text&quot;,
        &quot;background_image_info&quot;: {
            &quot;web_background_image&quot;: {
                &quot;theme_color&quot;: &quot;&quot;,
                &quot;gradient_position&quot;: {},
                &quot;canvas_position&quot;: {},
                &quot;origin_image_url&quot;: &quot;&quot;,
                &quot;image_url&quot;: &quot;&quot;
            },
            &quot;mobile_background_image&quot;: {
                &quot;origin_image_url&quot;: &quot;&quot;,
                &quot;image_url&quot;: &quot;&quot;,
                &quot;theme_color&quot;: &quot;&quot;,
                &quot;gradient_position&quot;: {},
                &quot;canvas_position&quot;: {}
            }
        },
        &quot;update_time&quot;: 1749994397,
        &quot;icon_url&quot;: &quot;https://example.com/FileBizType.BIZ_BOT_ICON/***.jpeg&quot;,
        &quot;suggest_reply_info&quot;: {
            &quot;reply_mode&quot;: &quot;enable&quot;,
            &quot;customized_prompt&quot;: &quot;&quot;
        },
        &quot;variables&quot;: [],
        &quot;create_time&quot;: 1749972247
    },
    &quot;msg&quot;: &quot;&quot;,
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h2 id="错误码" tabindex="-1">错误码</h2>
<p>如果成功调用扣子编程的 API，返回信息中 code 字段为 0。如果状态码为其他值，则表示接口调用失败。此时 msg 字段中包含详细错误信息，你可以参考<a href="https://docs.coze.cn/developer_guides/coze_error_codes" target="_blank">错误码</a>文档查看对应的解决方法。</p>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/developer_guides_bots_list_draft_published" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">查看智能体列表</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/developer_guides_switch_bot_develop_mode" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">开启或关闭智能体多人协作</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="基础信息" href="#基础信息" data-href="#基础信息">基础信息</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="请求参数" href="#请求参数" data-href="#请求参数">请求参数</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="Header" href="#Header" data-href="#Header">Header</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="Path" href="#Path" data-href="#Path">Path</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="Query" href="#Query" data-href="#Query">Query</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="返回参数" href="#返回参数" data-href="#返回参数">返回参数</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="BotInfo" href="#botinfo" data-href="#botinfo">BotInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="PromptInfo" href="#promptinfo" data-href="#promptinfo">PromptInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="PrefixPromptInfo" href="#prefixpromptinfo" data-href="#prefixpromptinfo">PrefixPromptInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="OnboardingInfoV2" href="#onboardinginfov2" data-href="#onboardinginfov2">OnboardingInfoV2</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="PluginInfo" href="#plugininfo" data-href="#plugininfo">PluginInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="ApiInfo" href="#apiinfo" data-href="#apiinfo">ApiInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="ModelInfo" href="#modelinfo" data-href="#modelinfo">ModelInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="CommonKnowledge" href="#commonknowledge" data-href="#commonknowledge">CommonKnowledge</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="KnowledgeInfo" href="#knowledgeinfo" data-href="#knowledgeinfo">KnowledgeInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="Variable" href="#variable" data-href="#variable">Variable</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="MediaConfig" href="#mediaconfig" data-href="#mediaconfig">MediaConfig</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="Voice" href="#voice" data-href="#voice">Voice</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="ShortcutCommandInfo" href="#shortcutcommandinfo" data-href="#shortcutcommandinfo">ShortcutCommandInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="ShortcutCommandToolInfo" href="#shortcutcommandtoolinfo" data-href="#shortcutcommandtoolinfo">ShortcutCommandToolInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="WorkflowInfo" href="#workflowinfo" data-href="#workflowinfo">WorkflowInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="BackgroundImageInfo" href="#backgroundimageinfo" data-href="#backgroundimageinfo">BackgroundImageInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="BackgroundImageDetail" href="#backgroundimagedetail" data-href="#backgroundimagedetail">BackgroundImageDetail</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="CanvasPosition" href="#canvasposition" data-href="#canvasposition">CanvasPosition</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="GradientPosition" href="#gradientposition" data-href="#gradientposition">GradientPosition</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="ResponseDetail" href="#responsedetail" data-href="#responsedetail">ResponseDetail</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="示例" href="#示例" data-href="#示例">示例</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="请求示例" href="#请求示例" data-href="#请求示例">请求示例</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="返回示例" href="#返回示例" data-href="#返回示例">返回示例</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="错误码" href="#错误码" data-href="#错误码">错误码</a></div></div></div></div></div></div></div></div>
</body></html>