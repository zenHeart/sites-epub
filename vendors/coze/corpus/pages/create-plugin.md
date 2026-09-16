<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">创建插件</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/4760.77ece367d4.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.782417a8ae.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/create-plugin"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/create-plugin.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="description" content="本文介绍了插件的基本概念，包括其定义、作用、组成部分和类型。详细说明了如何使用自然语言创建插件，涵盖描述需求、补充关键信息以及等待生成和检查等步骤，还介绍了创建不包含Panel的插件的相关内容，帮助用户了解并掌握插件的创建方法。"/><meta data-react-helmet="true" name="keywords" content="插件,创建,自然语言,Agent,Panel"/><meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC activeTab-g8RDKO" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC" href="/create-plugin" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" style="width:300px" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b8acf4bdbc784e3cbd81c" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/what_is_coze" data-discover="true"><span class="nodeTitle-ONnqtP" title="了解扣子">了解扣子</span></a></div><div id="tree-node-6a3b8acf4bdbc784e3cbd823" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8acf4bdbc784e3cbd831" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="使用扣子">使用扣子</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a9e80b47ae6de79d68c2cfc" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="和扣子一起工作">和扣子一起工作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a9ea8f07ae6de79d69632b1" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发扩展能力">开发扩展能力</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a9fbf0c75515a01c0d4b1ae" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/extended-ability-introduction" data-discover="true"><span class="nodeTitle-ONnqtP" title="扩展能力介绍">扩展能力介绍</span></a></div><div id="tree-node-6a9fbf0c75515a01c0d4b1af" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:24px" href="/create-plugin" data-discover="true"><span class="nodeTitle-ONnqtP" title="创建插件">创建插件</span></a></div><div id="tree-node-6a3b8acf4bdbc784e3cbd8b2" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/cozespace_create_skill" data-discover="true"><span class="nodeTitle-ONnqtP" title="开发技能">开发技能</span></a></div><div id="tree-node-6a3b8acf4bdbc784e3cbd8dc" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/cozespace_skill_revenue_settlement" data-discover="true"><span class="nodeTitle-ONnqtP" title="技能收入结算">技能收入结算</span></a></div></div></div><div id="tree-node-6a9e81417ae6de79d68c57a7" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="管理与设置">管理与设置</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8acf4bdbc784e3cbd888" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/cozespace_coze_billing_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="套餐与定价">套餐与定价</span></a></div><div id="tree-node-6a3b8acf4bdbc784e3cbd88f" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/cozespace_coze_app_faq" data-discover="true"><span class="nodeTitle-ONnqtP" title="扣子常见问题">扣子常见问题</span></a></div><div id="tree-node-6a3b8acf4bdbc784e3cbd896" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/cozespace_help_and_support" data-discover="true"><span class="nodeTitle-ONnqtP" title="获取帮助">获取帮助</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA" style="width:calc(100% - 300px);--anchor-width:260px"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>扣子</span><span class="separator-KB9yMa">/</span><span>开发扩展能力</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">创建插件</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">创建插件</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>插件可以把一套完成任务的方法、需要调用的工具，以及可操作的界面组合起来，交给 Agent 持续使用。你不需要理解协议、撰写代码，只需要用自然语言说明想用插件解决的问题，Agent 就能帮你梳理需求、生成插件，并在你验证并确认后发布。</p>
<p>本文介绍插件的基本概念，以及如何创建、测试、发布和管理插件。</p>
<h2 id="hHyipTqtl" tabindex="-1">了解插件</h2>
<h3 id="hCKW2IeTF" tabindex="-1">什么是插件</h3>
<p>插件是一组可以安装到 Agent 的能力。安装后，Agent 可以按照预设的方法完成任务、调用外部工具，也可以通过 Panel 和你共同处理同一份内容。</p>
<p>例如，你可以创建一个订单对账插件。它可以定期读取不同平台的订单，按照固定规则核对金额，并把异常订单展示在右侧的对账看板中。之后，无论是继续核对新订单，还是调整筛选条件，都不需要重新解释整套工作方法。</p>
<p>与一次性的对话任务相比，插件更适合承载需要反复执行、持续积累或多人复用的工作。</p>
<h3 id="hUGEWx5aj" tabindex="-1">为什么需要插件</h3>
<p>对话适合表达意图。任务涉及大量对象、不断变化的数据或需要反复调整的结果时，只向 Agent 描述需求并接收文字回复，往往不够直观。</p>
<p>插件可以帮助 Agent 完成以下工作：</p>
<ul data-style="0">
<li><strong>沉淀工作方法。</strong> 将固定步骤、判断标准和注意事项交给 Agent，后续不需要重复说明。</li>
<li><strong>连接真实工具和数据。</strong> Agent 可以通过 MCP 查询数据、调用外部服务或执行操作，而不是只给出操作建议。</li>
<li><strong>提供更合适的工作界面。</strong> 画布、看板、表格、时间线等内容可以通过 Panel 展示和操作，信息更直观。</li>
<li><strong>持续完成同一项工作。</strong> 插件可以保留业务数据。你和 Agent 可以围绕同一份结果继续查看、修改和推进任务。</li>
<li><strong>复用成熟能力。</strong> 创建并发布后，可以把插件添加到需要它的 Agent；上架到企业团队商店后，还可以提供给团队成员使用。</li>
</ul>
<p>插件为 Agent 提供完成任务所需的方法和能力；Panel 提供可以共同查看和操作的工作界面。</p>
<h3 id="hxYZLKmda" tabindex="-1">插件的组成</h3>
<p>一个插件可以包含 Skill、MCP 和 Panel。创建插件时不要求三者同时存在，Agent 会根据任务选择需要的组成部分。</p>
<!-- @cols-width: 100,400,328 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 400px;" /><col style="width: 328px;" /></colgroup><thead>
<tr>
<th><strong>组成部分</strong></th>
<th><strong>作用</strong></th>
<th><strong>适合的场景</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Skill</td>
<td>为 Agent 提供完成任务所需的步骤、知识和判断规则。</td>
<td>按固定标准审阅内容、生成周报、执行团队 SOP。</td>
</tr>
<tr>
<td>MCP</td>
<td>让 Agent 连接外部工具、服务和数据，并执行查询或操作。</td>
<td>查询业务数据、更新第三方系统、操作本地软件。</td>
</tr>
<tr>
<td>Panel</td>
<td>在对话旁提供可查看、可操作的界面，并将你的选择和修改传递给 Agent。</td>
<td>编辑画布、查看数据看板、管理任务、处理音视频时间线。</td>
</tr>
</tbody>
</table>
</div><p>例如，一个客户跟进插件可以使用 Skill 规定客户分级和跟进流程，使用 MCP 读取 CRM 数据，再通过 Panel 展示客户列表和待办事项。</p>
<h3 id="hXKSb6zUO" tabindex="-1">插件有哪些类型</h3>
<p>按照是否提供独立界面，插件分为以下两类：</p>
<ul data-style="0">
<li><strong>能力插件</strong>：不包含独立 Panel，主要通过对话使用。它可以是纯 Skill、纯 MCP，也可以同时包含 Skill 和 MCP。适合结果主要以文字或文件交付、不需要长期操作界面的任务。</li>
<li><strong>交互式插件</strong>：包含一个或多个 Panel，并可以按需搭配 Skill 和 MCP。适合需要持续查看信息、选择对象或直接修改内容的任务。</li>
</ul>
<p>如果用户需要在界面中查看和操作持续变化的内容，例如拖动画布元素、筛选看板数据或管理任务状态，适合创建交互式插件。如果只需要 Agent 按固定流程生成总结或文件，能力插件通常已经足够。</p>
<h2 id="hYg4P4tBi" tabindex="-1">创建插件</h2>
<p>你可以使用自然语言从零创建插件，也可以导入已有插件包。</p>
<h3 id="hzL1SkVpd" tabindex="-1">使用自然语言创建插件</h3>
<p>创建插件时，不需要先决定具体技术方案。优先说清楚业务问题、使用对象、输入和期望结果，Agent 会据此判断需要哪些能力。</p>
<h4 id="hL0qpAtvt" tabindex="-1">步骤一：描述插件需求</h4>
<p>在 <a href="https://www.coze.cn/new-task?surl_token=FJvCs&amp;zlink_code=FFKdE&amp;utm_medium=docs&amp;utm_source=docs&amp;utm_content=landingpage&amp;utm_id=&amp;utm_campaign=&amp;utm_term=docs&amp;utm_source_platform=" target="_blank">Agent 私聊或项目</a>中，<code>@插件创建器</code>，直接说明你希望创建什么插件。</p>
<p>一段有效的需求通常包含以下信息：</p>
<ul data-style="0">
<li>要解决什么问题。</li>
<li>有哪些可用的 MCP 或技能。</li>
<li>是否需要可视化展示。</li>
<li>是否需要用户登录或鉴权。</li>
</ul>
<p>你不需要一次写全。Agent 会继续询问会影响插件形态、权限或安全边界的信息。名称、普通文案、默认布局等细节，可以先让 Agent 给出方案，再在预览阶段调整。</p>
<p><strong>提示词模板</strong></p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">@插件创建器，帮我创建一个插件，名为[插件名称],功能是[功能 1][功能 2][功能 3]，有一个用户界面来[Panel 的作用（可选）]。
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="@插件创建器，帮我创建一个插件，名为[插件名称],功能是[功能 1][功能 2][功能 3]，有一个用户界面来[Panel 的作用（可选）]。" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p><strong>提示词示例</strong></p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">@插件创建器，帮我创建一个插件，名为[扣子知识问答],功能是通过扣子产品文档 MCP 来查看和检索官方文档、总结提炼信息，并准确回答用户问题。
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="@插件创建器，帮我创建一个插件，名为[扣子知识问答],功能是通过扣子产品文档 MCP 来查看和检索官方文档、总结提炼信息，并准确回答用户问题。" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h4 id="hIxtWuQku" tabindex="-1">步骤二：补充关键信息</h4>
<p>根据 Agent 的提问，确认数据来源、主要操作和使用范围。涉及以下操作时，请重点核对 Agent 给出的说明：</p>
<ul data-style="0">
<li>付款、下单等交易操作。</li>
<li>对外发送消息或发布内容。</li>
<li>删除、覆盖或批量修改数据。</li>
<li>读取本地目录、操作本地软件或设备。</li>
<li>使用敏感数据或扩大账号权限。</li>
</ul>
<p>这些操作应在真正执行前再次向你展示操作对象、范围和影响。创建插件时同意接入某项能力，不等于提前同意以后发生的每一次敏感操作。</p>
<h4 id="hbTZhQ3Bc" tabindex="-1">步骤三：等待生成和检查</h4>
<p>Agent 会生成插件所需的 Skill、MCP 和 Panel，并自动检查插件结构、能力声明、调用关系和敏感操作确认流程。</p>
<p>生成过程中，你仍然可以补充要求。</p>
<p>生成完成后，插件会进入“草稿预览”。此时可以测试和修改，但还没有正式发布。</p>
<h3 id="hsVIIQWKG" tabindex="-1">创建不包含 Panel 的插件</h3>
<p>如果任务主要由 Agent 在后台完成，并且结果可以通过消息或文件返回，可以明确要求创建不包含 Panel 的能力插件。</p>
<p>根据需要，能力插件可以采用以下组合：</p>
<ul data-style="0">
<li>纯 Skill：主要沉淀知识、规则和工作流程。</li>
<li>纯 MCP：主要提供外部数据或工具调用能力。</li>
<li>Skill + MCP：既规定处理方法，又连接真实工具执行任务。</li>
</ul>
<p><strong>示例提示词</strong></p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">帮我创建一个合同审阅插件，不需要 Panel。

用户上传合同时，先识别合同类型，再按照我提供的审阅技能来审阅规则检查付款条件、违约责任、知识产权和自动续约条款。输出风险等级、原文位置、风险原因和修改建议。如果信息不足，不要猜测，直接列出需要确认的问题。
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="帮我创建一个合同审阅插件，不需要 Panel。

用户上传合同时，先识别合同类型，再按照我提供的审阅技能来审阅规则检查付款条件、违约责任、知识产权和自动续约条款。输出风险等级、原文位置、风险原因和修改建议。如果信息不足，不要猜测，直接列出需要确认的问题。" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h3 id="hfX6AOaRY" tabindex="-1">创建包含 Panel 的插件</h3>
<p>如果用户需要持续查看、选择或修改结构化内容，可以要求 Agent 创建交互式插件。</p>
<p>描述 Panel 时，重点说明以下信息即可：</p>
<ul data-style="0">
<li>Panel 中要展示哪些对象，例如订单、图片、任务或指标。</li>
<li>用户最常执行哪些操作，例如筛选、拖动、选择、编辑或确认。</li>
<li>用户完成操作后，Agent 应如何继续处理。</li>
<li>是否需要多个 Panel，以及每个 Panel 分别解决什么问题。</li>
</ul>
<p>一个插件可以包含多个 Panel。例如，项目管理插件可以分别提供“任务看板”和“进度统计”两个 Panel。它们可以独立打开和调试，但属于同一个插件，共享插件版本和项目业务数据。发布时会发布完整插件，不能只发布其中一个 Panel。</p>
<p>在草稿预览中，你可以切换查看 Web 和移动端的展示效果。</p>
<p><strong>示例提示词</strong></p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">@插件创建器，帮我创建一个插件，名为[扣子知识问答],功能是通过扣子产品文档 MCP 来查看和检索官方文档、总结提炼信息，并准确回答用户问题。需要一个用户界面来让我输入问题/关键词，并展示 Agent 的回复。
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="@插件创建器，帮我创建一个插件，名为[扣子知识问答],功能是通过扣子产品文档 MCP 来查看和检索官方文档、总结提炼信息，并准确回答用户问题。需要一个用户界面来让我输入问题/关键词，并展示 Agent 的回复。" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h3 id="hQLIX0u39" tabindex="-1">创建需要身份认证的插件</h3>
<p>如果插件需要访问飞书、CRM、电商平台等外部服务，你需要在创建时告诉 Agent：连接什么服务、使用什么认证方式、需要哪些权限，以及用户应在什么时候完成认证。</p>
<p>常见认证方式包括：</p>
<ul data-style="0">
<li><strong>用户自行填写 API Key 或 Token</strong>：在 Skill 中说明配置步骤和使用要求，并让用户通过插件提供的安全配置入口填写。不要把真实 API Key、Token、密码或验证码写进 Skill、提示词或插件包。</li>
<li><strong>MCP 身份认证</strong>：MCP 需要用户 Token 或 OAuth 授权时，在插件中声明对应的连接和权限要求。用户首次使用、授权失效或权限范围扩大时，由系统引导其完成认证。</li>
<li><strong>本地应用或设备连接</strong>：插件需要操作本地应用、目录或设备时，应声明所需的桌面端环境和连接步骤，并说明未连接时哪些能力不可用。</li>
</ul>
<p>每位用户使用自己的账号和凭证。团队成员不会继承插件创建者或其他成员的授权，因此测试时要覆盖首次认证、取消认证、凭证失效和重新连接等情况。</p>
<p><strong>示例提示词</strong></p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">@插件创建器，帮我创建一个客户查询插件。插件通过 CRM MCP 查询客户资料，用户首次使用时需要完成 OAuth 授权，只申请读取客户和跟进记录的权限。请不要在插件文件中保存用户 Token；授权失效时，引导用户重新连接账号。
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="@插件创建器，帮我创建一个客户查询插件。插件通过 CRM MCP 查询客户资料，用户首次使用时需要完成 OAuth 授权，只申请读取客户和跟进记录的权限。请不要在插件文件中保存用户 Token；授权失效时，引导用户重新连接账号。" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h3 id="hrilydSgf" tabindex="-1">导入插件包</h3>
<p>如果你自行开发了插件，或从 Codex、Claude Code 等平台导出了插件包，可以直接导入扣子，不需要重新通过对话创建。插件包需要符合插件规范，并且压缩前、压缩后均小于 500 MB。</p>
<ol data-style="0">
<li>进入<strong>扩展 &gt;</strong><a href="https://www.coze.cn/skills?capability=plugin&amp;tab=space&amp;zlink_code=FFKdE&amp;utm_medium=docs&amp;utm_source=docs&amp;utm_content=landingpage&amp;utm_id=&amp;utm_campaign=&amp;utm_term=docs&amp;utm_source_platform=" target="_blank">插件</a>，在页面右上角单击<strong>上传插件包。</strong></li>
<li>点击<strong>选择文件</strong>，上传 ZIP 格式的插件包。<br>
插件包要求：
<ul data-style="1">
<li>符合 <a href="https://agent-plugins.org/schemas/1.0.0/plugin.schema.json" target="_blank">Agent Plugins 1.0.0 协议</a>插件规范，例如在扣子或 Codex 中生成的插件。</li>
<li>压缩前、压缩后均小于 500 MB。</li>
</ul>
</li>
<li>等待系统检查并解析插件包。</li>
<li>在插件资料页面确认插件名称和图标。</li>
<li>点击<strong>保存</strong>。</li>
<li>保存成功后，在<strong>我的插件</strong>中即可查看导入结果。<br>
如果系统提示该插件已上传，请先到<strong>我的插件</strong>中查找同一插件，不要反复上传。上传失败时，根据页面显示的问题修正插件包，再重新选择文件。<br>
导入后，建议先检查 Skill、MCP 和 Panel 是否被正确识别，再完成测试和发布。</li>
</ol>
<h2 id="hRROPVK9d" tabindex="-1">测试、调优和发布插件</h2>
<h3 id="hzvtA4P59" tabindex="-1">预览插件</h3>
<p>插件生成并检查通过后，Agent 会发送草稿卡片。点击卡片或对应的 Panel 入口，即可查看草稿。</p>
<p>对于包含 Panel 的插件，你可以分别预览 Web 和移动端效果，检查信息展示、操作流程和多端适配是否符合预期。</p>
<h3 id="hg67HRAFz" tabindex="-1">测试插件</h3>
<p>测试时除了检查正常使用流程，还要覆盖失败和异常情况。建议至少检查以下内容：</p>
<!-- @cols-width: 193,531 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 193px;" /><col style="width: 531px;" /></colgroup><thead>
<tr>
<th><strong>检查项</strong></th>
<th><strong>建议测试方法</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>是否会正确使用插件</td>
<td>分别输入明确请求、口语化请求和容易混淆的请求，确认 Agent 能在合适的时候调用插件。</td>
</tr>
<tr>
<td>MCP 是否可用</td>
<td>测试查询、写入和失败场景，确认返回结果来自正确账号和数据范围。</td>
</tr>
<tr>
<td>
<p>Panel 是否可用</p>
</td>
<td>
<p>点击各个按钮，是否有异常报错、信息展示是否完整。</p>
<p>检查信息是否容易找到，选择、编辑和筛选操作是否能被 Agent 正确理解。</p>
</td>
</tr>
<tr>
<td>多端是否可用</td>
<td>分别预览 Web 和移动端，检查布局、只读能力和不支持状态是否符合预期。</td>
</tr>
<tr>
<td>身份认证是否完整</td>
<td>测试首次授权、取消授权、授权失效和重新连接。</td>
</tr>
</tbody>
</table>
</div><p>测试时可以准备一组固定案例，每次修改后重复执行。固定案例应同时包括：最常见的正常任务、信息不完整的任务、边界输入，以及至少一个预期失败的任务。这样更容易判断一次修改是否解决了问题，又是否破坏了原有能力。</p>
<h3 id="hCDDFXh8p" tabindex="-1">调优插件</h3>
<p>发现问题后，直接在当前对话中说明出现了什么问题、期望结果是什么，以及如何复现。提供具体案例，可以帮助 Agent 更准确地修改插件。</p>
<p><strong>示例提示词</strong></p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">请修改当前订单对账插件：
1. 退款中的订单不要标记为金额异常，单独归入“退款处理中”。
2. 对账看板默认只显示异常订单，但保留“查看全部”筛选项。
3. 点击订单后，先展示订单号、平台和差额，再让 Agent 分析原因。
4. 保持现有数据，不要创建新的插件。

请修改后重新检查，并停留在草稿预览，不要发布。
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="请修改当前订单对账插件：
1. 退款中的订单不要标记为金额异常，单独归入“退款处理中”。
2. 对账看板默认只显示异常订单，但保留“查看全部”筛选项。
3. 点击订单后，先展示订单号、平台和差额，再让 Agent 分析原因。
4. 保持现有数据，不要创建新的插件。

请修改后重新检查，并停留在草稿预览，不要发布。" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p>修改后先复测受影响的场景，再执行一遍原有核心案例。对于多个 Panel 的插件，从任一 Panel 进入调试后，所有 Panel 都属于同一份插件草稿；即使只修改了一个 Panel，再次发布时仍会发布完整插件。</p>
<h3 id="hIrFuZbXU" tabindex="-1">发布插件</h3>
<p>草稿测试完成后，发布插件，才能让 Agent 使用正式版本。</p>
<p>你可以使用以下方式触发发布：</p>
<ul data-style="0">
<li>点击草稿 Panel 顶部的<strong>发布</strong>。</li>
<li>在对话中明确要求 Agent 代为发布。</li>
</ul>
<p>单 Panel 插件或不包含 Panel 的插件会直接进入发布流程。包含多个 Panel 时，如果由你在界面中发布，系统会再次展示本次包含的 Panel 数量；确认后发布完整插件。</p>
<p>发布成功后：</p>
<ul data-style="0">
<li>插件会出现在<a href="https://www.coze.cn/skills?capability=plugin&amp;tab=my?surl_token=FJvCs&amp;zlink_code=FFKdE&amp;utm_medium=docs&amp;utm_source=docs&amp;utm_content=landingpage&amp;utm_id=&amp;utm_campaign=&amp;utm_term=docs&amp;utm_source_platform=" target="_blank">我的插件</a>中。</li>
<li>在 Agent 私聊中创建插件时，当前 Agent 会安装或更新该插件。</li>
<li>在项目中发布插件时，项目会使用最新正式版本；已经启用该插件的 Agent 会自动跟随更新。</li>
</ul>
<p>如果发布失败，系统会保留当前草稿、上一次成功发布的版本和业务数据。你可以点击<strong>重新尝试</strong>，或选择<strong>交给 Agent 修复</strong>。如果其他人已经发布了更新，系统会阻止当前草稿直接覆盖新版本；Agent 需要基于最新版本重新适配并检查，然后由你再次发布。</p>
<h2 id="hTMGDrFQX" tabindex="-1">将插件上架到企业团队商店</h2>
<p>如果希望在团队内共享插件，需要将已经发布的插件上架到企业团队商店。上架后，其他企业成员可以在商店中查看并添加该插件。</p>
<p>企业团队商店默认关闭审核，插件提交后直接自动上架。企业管理员也可以在管理后台开启审核；开启后，插件需要通过审核才能正式上架。正式上架后，企业成员可以在企业团队商店中发现并添加插件。</p>
<p>完成插件发布并准备好展示资料后，可以上架插件：</p>
<ol data-style="0">
<li>进入<a href="https://www.coze.cn/skills?capability=plugin&amp;tab=my?surl_token=FJvCs&amp;zlink_code=FFKdE&amp;utm_medium=docs&amp;utm_source=docs&amp;utm_content=landingpage&amp;utm_id=&amp;utm_campaign=&amp;utm_term=docs&amp;utm_source_platform=" target="_blank">我的插件</a>。</li>
<li>找到要上架的插件，在右侧单击 <strong>···</strong>。</li>
<li>选择<strong>上架到企业商店</strong>。</li>
<li>填写企业商店中的展示名称、简介和截图。<br>
为了让团队成员快速判断插件是否适用，建议展示信息至少回答三个问题：插件解决什么问题、适合谁使用、使用前需要连接什么账号或设备。截图应展示真实核心界面和关键结果，不要只使用装饰性封面。</li>
<li>点击<strong>确认上架</strong>或<strong>提交审核</strong>。<br>
提交成功后，在插件列表中查看上架状态。状态显示为“审核中”表示已进入审核流程，不代表已经上架完成。</li>
</ol>
<p>如果要修改已经上架的展示信息，可以在插件右侧的<strong>更多</strong>中展开<strong>企业上架管理</strong>，选择<strong>更新上架信息</strong>。如果不再希望团队成员发现该插件，可以在同一位置选择<strong>下架</strong>。下架不会自动移除成员已经添加到 Agent 的插件。</p>
<h2 id="hF969e2pn" tabindex="-1">相关操作</h2>
<h3 id="hhHnX2SOE" tabindex="-1">修改插件</h3>
<p>你可以在原对话中继续修改插件，也可以在新的对话或项目中提出修改要求。系统会根据当前正式版本创建草稿；只有在你确认并发布新版本后，修改才会在线上生效。</p>
<p><strong>示例提示词</strong></p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">@插件创建器，修改“订单对账”插件：新增“退款处理中”状态；对账看板默认只展示异常订单，并保留“查看全部”筛选项。请保留现有数据，完成后生成草稿供我测试，不要直接发布。
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="@插件创建器，修改“订单对账”插件：新增“退款处理中”状态；对账看板默认只展示异常订单，并保留“查看全部”筛选项。请保留现有数据，完成后生成草稿供我测试，不要直接发布。" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h3 id="hQw9sDWLC" tabindex="-1">管理我的插件</h3>
<p>在<a href="https://www.coze.cn/skills?capability=plugin&amp;tab=my?surl_token=FJvCs&amp;zlink_code=FFKdE&amp;utm_medium=docs&amp;utm_source=docs&amp;utm_content=landingpage&amp;utm_id=&amp;utm_campaign=&amp;utm_term=docs&amp;utm_source_platform=" target="_blank">我的插件</a>中，可以查看当前账号拥有的插件资产。列表会展示插件来源，例如<strong>插件商店</strong>或<strong>我创建的</strong>，并显示连接状态、上架状态和已添加的 Agent 数量。</p>
<p>常用操作包括：</p>
<ul data-style="0">
<li><strong>修改名称和图标</strong>：点击插件右侧的<strong>更多</strong>，选择<strong>编辑插件信息</strong>，修改后保存。</li>
<li><strong>管理 Agent</strong>：点击<strong>X 个 Agent</strong>，查看已添加和未添加的 Agent，并将插件添加到目标 Agent 或从 Agent 移除。</li>
<li><strong>停用或重新启用</strong>：停用后，新对话不再加载该插件；重新启用后使用最新正式版本。</li>
<li><strong>从 Agent 移除</strong>：只解除插件与当前 Agent 的关系，不会删除插件、正式版本或业务数据。</li>
<li><strong>管理企业上架状态</strong>：更新企业商店展示信息，或下架插件。</li>
<li><strong>删除插件资产</strong>：在<strong>更多</strong>中选择<strong>删除插件</strong>并确认。删除后，你的所有 Agent 都无法继续使用该插件，且无法恢复。</li>
</ul>
<p>同一项目中的插件版本和业务数据可以共享，但每个 Agent 是否启用插件需要单独管理。将插件添加到一个 Agent，不会自动让项目中的其他 Agent 获得该插件。</p>
<h2 id="hcNYbdyEU" tabindex="-1">常见问题</h2>
<h3 id="hvBja709B" tabindex="-1">什么情况下需要创建 Panel？</h3>
<p>当用户需要持续查看或直接操作画布、看板、表格、任务列表等内容时，建议创建 Panel。例如，用户需要筛选订单、拖动画布元素、修改任务状态，或在查看数据后继续让 Agent 处理，都适合使用 Panel。</p>
<p>如果插件只需要让 Agent 按固定流程完成任务，并通过消息或文件返回结果，通常不需要 Panel。例如，合同审阅、资料总结或固定格式周报可以使用能力插件。如果用户需要在界面中持续查看和操作内容，例如筛选订单或调整任务状态，则建议创建 Panel。</p>
<h3 id="hQy2hsLEp" tabindex="-1">发布和上架有什么区别？</h3>
<p>发布和上架解决的问题不同。发布会把测试完成的草稿生成正式版本，让当前 Agent 或项目中已经启用该插件的 Agent 使用。发布后，插件不会自动出现在企业团队商店中。</p>
<p>如果希望将插件共享给团队成员，还需要把已发布插件上架到企业团队商店。上架后，其他成员可以在商店中查看并添加插件。企业团队商店默认关闭审核；管理员开启审核后，插件需要通过审核才能正式上架。仅供自己或指定 Agent 使用时，完成发布即可，不需要上架。</p>
<h3 id="htP24dazZ" tabindex="-1">可以导入 Codex 或 Claude Code 的插件吗？</h3>
<p>可以。你可以导入在扣子开发或从 Codex、Claude Code 导出的插件包。插件包需要：</p>
<ul data-style="0">
<li>符合 <a href="https://agent-plugins.org/schemas/1.0.0/plugin.schema.json" target="_blank">Agent Plugins 1.0.0 协议</a>插件规范。</li>
<li>压缩前、压缩后均小于 500 MB。</li>
</ul>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/extended-ability-introduction" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">扩展能力介绍</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/cozespace_create_skill" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">开发技能</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="了解插件" href="#hHyipTqtl" data-href="#hHyipTqtl">了解插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="什么是插件" href="#hCKW2IeTF" data-href="#hCKW2IeTF">什么是插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="为什么需要插件" href="#hUGEWx5aj" data-href="#hUGEWx5aj">为什么需要插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="插件的组成" href="#hxYZLKmda" data-href="#hxYZLKmda">插件的组成</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="插件有哪些类型" href="#hXKSb6zUO" data-href="#hXKSb6zUO">插件有哪些类型</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="创建插件" href="#hYg4P4tBi" data-href="#hYg4P4tBi">创建插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="使用自然语言创建插件" href="#hzL1SkVpd" data-href="#hzL1SkVpd">使用自然语言创建插件</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="步骤一：描述插件需求" href="#hL0qpAtvt" data-href="#hL0qpAtvt">步骤一：描述插件需求</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="步骤二：补充关键信息" href="#hIxtWuQku" data-href="#hIxtWuQku">步骤二：补充关键信息</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="步骤三：等待生成和检查" href="#hbTZhQ3Bc" data-href="#hbTZhQ3Bc">步骤三：等待生成和检查</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="创建不包含 Panel 的插件" href="#hsVIIQWKG" data-href="#hsVIIQWKG">创建不包含 Panel 的插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="创建包含 Panel 的插件" href="#hfX6AOaRY" data-href="#hfX6AOaRY">创建包含 Panel 的插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="创建需要身份认证的插件" href="#hQLIX0u39" data-href="#hQLIX0u39">创建需要身份认证的插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="导入插件包" href="#hrilydSgf" data-href="#hrilydSgf">导入插件包</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="测试、调优和发布插件" href="#hRROPVK9d" data-href="#hRROPVK9d">测试、调优和发布插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="预览插件" href="#hzvtA4P59" data-href="#hzvtA4P59">预览插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="测试插件" href="#hg67HRAFz" data-href="#hg67HRAFz">测试插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="调优插件" href="#hCDDFXh8p" data-href="#hCDDFXh8p">调优插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="发布插件" href="#hIrFuZbXU" data-href="#hIrFuZbXU">发布插件</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="将插件上架到企业团队商店" href="#hTMGDrFQX" data-href="#hTMGDrFQX">将插件上架到企业团队商店</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="相关操作" href="#hF969e2pn" data-href="#hF969e2pn">相关操作</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="修改插件" href="#hhHnX2SOE" data-href="#hhHnX2SOE">修改插件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="管理我的插件" href="#hQw9sDWLC" data-href="#hQw9sDWLC">管理我的插件</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="常见问题" href="#hcNYbdyEU" data-href="#hcNYbdyEU">常见问题</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="什么情况下需要创建 Panel？" href="#hvBja709B" data-href="#hvBja709B">什么情况下需要创建 Panel？</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="发布和上架有什么区别？" href="#hQy2hsLEp" data-href="#hQy2hsLEp">发布和上架有什么区别？</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="可以导入 Codex 或 Claude Code 的插件吗？" href="#htP24dazZ" data-href="#htP24dazZ">可以导入 Codex 或 Claude Code 的插件吗？</a></div></div></div></div></div></div></div></div>
</body></html>