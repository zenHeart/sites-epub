<!DOCTYPE html>
<html><head><meta charset="utf-8"/><meta content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no" name="viewport"/><meta content="ie=edge" http-equiv="x-ua-compatible"/><meta content="webkit" name="renderer"/><meta content="standard" name="layoutmode"/><meta content="force" name="imagemode"/><meta content="no" name="wap-font-scale"/><meta content="telephone=no" name="format-detection"/><title data-react-helmet="true">安装并使用 Card SDK</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/5956.1729cb00c0.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.ca52691239.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet"/> <link data-react-helmet="true" href="https://docs.coze.cn/developer_guides_card_sdk" rel="canonical"/><link data-react-helmet="true" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" rel="icon"/><link data-react-helmet="true" href="/developer_guides_card_sdk.md" rel="alternate" type="text/markdown"/><link data-react-helmet="true" href="/llms.txt" rel="alternate" type="text/plain"/>
<meta content="本文详细介绍了扣子Card SDK的安装与使用方法。它能助力开发者打造个性化交互消息展示体验，可自定义卡片结构内容、样式等，还给出了浏览器兼容性要求及具体配置流程，包括发布智能体、安装SDK及配置卡片属性等步骤，附示例代码与参数说明。" data-react-helmet="true" name="description"/><meta content="Card SDK,安装,使用,自定义,配置流程" data-react-helmet="true" name="keywords"/><meta content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE" data-react-helmet="true" name="google-site-verification"/>

<meta content="codeva-mJmA0HNtAv" name="baidu-site-verification"/></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a class="brand-qR7tMP" href="https://www.coze.cn" rel="noreferrer" target="_blank"><img alt="扣子" class="siteIcon-qohRRP" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" data-discover="true" href="/what_is_coze">扣子</a><a class="tab-JssokC" data-discover="true" href="/guides_welcome">扣子编程</a><a class="tab-JssokC" data-discover="true" href="/ppt-plugin">教程</a><a class="tab-JssokC" data-discover="true" href="/coze_pro_billing_overview">定价</a><a class="tab-JssokC activeTab-g8RDKO" data-discover="true" href="/developer_guides_card_sdk"><span>资源</span><span class="arrow-nKMrBv"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg fill="none" height="16" viewbox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)" fill-rule="evenodd"></path></g><defs><lineargradient gradientunits="userSpaceOnUse" id="paint0_linear_1944_44928" x1="1.3335" x2="15.0379" y1="15.0401" y2="15.0401"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></lineargradient><clippath id="clip0_1944_44928"><rect fill="white" height="16" width="16"></rect></clippath></defs></svg><input class="input-tjtw6Q" placeholder="搜索" readonly="" type="text"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" fill="currentColor" viewbox="5 5 22 22" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg fill="none" height="48" viewbox="0 0 48 48" width="48" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clippath id="clip0_2_6"><rect fill="white" height="48" width="48"></rect></clippath></defs></svg></span><span class="topic-rag-logo-dark"><svg fill="none" height="48" viewbox="0 0 48 48" width="48" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clippath id="clip0_2_6"><rect fill="#262E3B" height="48" width="48"></rect></clippath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg height="24" role="img" viewbox="0 0 40 40" width="24" xmlns="http://www.w3.org/2000/svg"><defs><lineargradient gradientunits="userSpaceOnUse" id="starGradient" x1="1.25" x2="29.602" y1="35.735" y2="29.277"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></lineargradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" fill="url(#starGradient)" fill-opacity="0.8" r="1.2"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg aria-hidden="true" class="arco-icon arco-icon-close" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg fill="none" height="14" viewbox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><lineargradient gradientunits="userSpaceOnUse" id="paint0_linear_7153_28960" x1="2.04126" x2="12.5415" y1="13.4163" y2="13.4163"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></lineargradient><clippath id="clip0_7153_28960"><rect fill="white" height="14" width="14"></rect></clippath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" disabled="" style="border-radius:4px;height:28px" type="button"><svg aria-hidden="true" class="arco-icon arco-icon-plus" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" disabled="" style="color:#c7ccd6" type="button"><svg fill="none" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor" fill-rule="evenodd"></path></g><defs><clippath id="clip0_7153_32885"><rect fill="white" height="18" transform="translate(3 3)" width="18"></rect></clippath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true"><div class="content-KOLZ20"><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b97434bdbc784e3ce84ce"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a55df9a4bdbc784e3c9738f"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf30d"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf317"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf31d"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf325"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf334"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf32e"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf35a"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf362"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8e614bdbc784e3cce185"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8d4bdbc784e3cc3e2c"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8d4bdbc784e3cc3fa8"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc40e8"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Chat SDK">Chat SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc40ef"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Python SDK">Python SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc412c"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Node.js SDK">Node.js SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc4132"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Java SDK">Java SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc41c6"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Go SDK">Go SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc4245"><a class="nodeContent-GigwSX" data-discover="true" href="/developer_guides_vibe_coding_websdk" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Web SDK（AI 编程）">Web SDK（AI 编程）</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc424c"><a class="nodeContent-GigwSX" data-discover="true" href="/developer_guides_ui_builder_web_sdk" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Web SDK（低代码）">Web SDK（低代码）</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc4251"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Card SDK">Card SDK</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8b8d4bdbc784e3cc4258"><a class="nodeContent-GigwSX active-dE_WV_" data-discover="true" href="/developer_guides_card_sdk" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="安装并使用 Card SDK">安装并使用 Card SDK</span></a></div></div></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8bc84bdbc784e3cc529d"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8e4bdbc784e3cc445f"><a class="nodeContent-GigwSX" data-discover="true" href="/developer_guides_coze_cli" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf33f"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf369"><a class="nodeContent-GigwSX" data-discover="true" href="/guides_FAQ" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div aria-label="拖拽调整目录宽度" aria-orientation="vertical" class="resizeHandle-lop5IL" role="separator"></div></div><div class="container-h8FsmA" data-topic-doc="true"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>SDK 参考</span><span class="separator-KB9yMa">/</span><span>Card SDK</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">安装并使用 Card SDK</span></div><div class="titleContainer-hr8uxx"><h1 class="title-C1b1pA" data-h0="true" id="doc_title">安装并使用 Card SDK</h1><aside class="mdx-live-widget">
<p class="mdx-live-widget-label">Interactive explorer</p>
<p>This directory tree is interactive on the original page and cannot run inside an EPUB. Open it here: <a class="source-title" href="https://docs.coze.cn/developer_guides_card_sdk#explore-the-directory" rel="external">https://docs.coze.cn/developer_guides_card_sdk#explore-the-directory</a></p>
</aside><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg aria-hidden="true" class="copyIcon-iTB4A1 arco-icon arco-icon-copy" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg><span>复制页面</span></div><div class="moreButton-ZJ3qDg"><svg aria-hidden="true" class="arco-icon arco-icon-down" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>本文介绍如何安装并使用扣子 Card SDK，开发者可以参考本文档自定义智能体对话消息中的卡片效果。</p>
<h2 id="b509274e" tabindex="-1">功能简介</h2>
<p>为了助力开发者打造更具个性化与交互性的消息展示体验，扣子提供 Card SDK。借助该 SDK，开发者可以灵活地定义卡片的结构和内容，并将渲染后的卡片集成到你自行实现的聊天应用中。</p>
<p>卡片是一种特殊的消息展示方式，它以结构化的布局和丰富的视觉元素呈现信息。与传统的纯文本消息相比，卡片可以包含图片、按钮、列表等多种元素，使得信息更加直观、易读。这不仅显著提升了用户体验，还提高了信息传递效率，增强了交互性。</p>
<h2 id="5efadaff" tabindex="-1">效果预览</h2>
<p><img alt="Image" height="355" loading="lazy" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/efe1e35df664419ab425cea205221abd~tplv-goo7wpa0wc-topic.webp" width="400"/></p>
<h2 id="08bd7843" tabindex="-1">功能简介</h2>
<!-- @cols-width: 166,706 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 166px;"/><col style="width: 706px;"/></colgroup><thead>
<tr>
<th><strong>功能</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>自定义内容格式</td>
<td>Card SDK 提供了强大的自定义功能，允许开发者根据具体需求定义卡片的布局和内容。开发者可以通过配置卡片的 DSL（Domain Specific Language，领域特定语言）数据，指定卡片中各个元素的类型、样式和交互逻辑。无论是简单的文本卡片，还是包含图片、按钮和列表的复杂卡片，都可以通过Card SDK 轻松实现。</td>
</tr>
<tr>
<td>自定义卡片样式</td>
<td>Card SDK 还允许开发者自定义卡片中按钮、图片等组件的渲染逻辑，实现个性化的样式和交互效果。通过 <code>customComponentMap</code> 接口，开发者可以为每个组件定义独特的渲染函数，从而实现更加丰富的视觉效果和交互行为。开发者可以根据具体的业务需求，设计出个性化的卡片样式。</td>
</tr>
</tbody>
</table>
</div><h2 id="783bdba5" tabindex="-1">浏览器兼容性</h2>
<p>Card  SDK 的运行环境要求如下表所示。</p>
<!-- @cols-width: 100,139,251 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;"/><col style="width: 139px;"/><col style="width: 251px;"/></colgroup><thead>
<tr>
<th><strong>操作系统</strong></th>
<th><strong>浏览器</strong></th>
<th><strong>版本限制</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">PC</td>
<td>Chrome</td>
<td>87.0 及以上</td>
</tr>
<tr>
<td>Edge</td>
<td>100.0 及以上</td>
</tr>
<tr>
<td>Safari</td>
<td>14.0 及以上</td>
</tr>
<tr>
<td>Firefox</td>
<td>79.0 及以上</td>
</tr>
<tr>
<td rowspan="2">Android</td>
<td>Chrome</td>
<td>100.0 及以上</td>
</tr>
<tr>
<td>Edge</td>
<td>100.0 及以上</td>
</tr>
<tr>
<td rowspan="2">iOS</td>
<td>Chrome</td>
<td>87.0 及以上</td>
</tr>
<tr>
<td>Safari</td>
<td>14.0 及以上</td>
</tr>
</tbody>
</table>
</div><h2 id="9e92dbac" tabindex="-1">配置流程</h2>
<h3 id="2c5fef61" tabindex="-1">步骤一：发布智能体</h3>
<p>在智能体的发布页面，选择 Chat SDK，并单击<strong>发布</strong>。发布的详细流程可参考<a href="/guides/publish_agent_to_chat_sdk" target="_blank">发布到 Chat SDK</a>。</p>
<h3 id="37fdb1a4" tabindex="-1">步骤二：安装 Card SDK</h3>
<p>创建一个新的 HTML 页面，并将以下代码添加到 <code>&lt;body&gt;</code> 的 <code>&lt;script&gt;</code> 标签中，保存并运行后会自动加载 Card SDK 的 JavaScript 代码。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>示例代码中的版本号（1.2.0-beta.8）需要替换为 Chat SDK 最新的版本号，版本信息请参见<a href="/developer_guides/web_sdk_changelog" target="_blank">Chat SDK 发布历史</a>。</p>
</div>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-keyword">let</span> c = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">'script'</span>);
c.<span class="hljs-property">src</span> = <span class="hljs-string">'https://lf-cdn.coze.cn/obj/unpkg/flow-platform/chat-app-sdk/1.2.0-beta.13/libs/cn/ui.js'</span>;
<span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">appendChild</span>(c);
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="let c = document.createElement('script');
c.src = 'https://lf-cdn.coze.cn/obj/unpkg/flow-platform/chat-app-sdk/1.2.0-beta.13/libs/cn/ui.js';
document.body.appendChild(c);" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="e8eff981" tabindex="-1">步骤三：配置卡片属性</h3>
<h4 id="48407e15" tabindex="-1">示例代码</h4>
<p>以下是基于 React 框架编写的示例代码，用于渲染卡片布局。</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, { useCallback, useEffect, useRef } <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-comment">// 定义 CozeCard 组件，用于创建和管理 CozeWebSDK.WebCardRuntime 实例</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">CozeCard</span> = (<span class="hljs-params"></span>) =&gt; {
  <span class="hljs-comment">// 使用 useRef 创建一个可变的引用对象，用于保存 CozeWebSDK.WebCardRuntime 实例</span>
  <span class="hljs-keyword">const</span> clientRef = <span class="hljs-title function_">useRef</span>();

  <span class="hljs-comment">// 使用 useCallback 缓存函数，避免组件重新渲染时函数重新创建</span>
  <span class="hljs-keyword">const</span> genCard = <span class="hljs-title function_">useCallback</span>(<span class="hljs-function">(<span class="hljs-params">elem</span>) =&gt;</span> {
    <span class="hljs-comment">// 如果传入的元素为空，直接返回</span>
    <span class="hljs-keyword">if</span> (!elem) {
      <span class="hljs-keyword">return</span>;data 
    }
    <span class="hljs-comment">// 如果之前已经存在 CozeWebSDK.WebCardRuntime 实例，先销毁它</span>
    <span class="hljs-keyword">if</span> (clientRef.<span class="hljs-property">current</span>) {
      clientRef.<span class="hljs-property">current</span>.<span class="hljs-title function_">destroy</span>();
    }
    <span class="hljs-comment">// 创建新的 CozeWebSDK.WebCardRuntime 实例并保存到 clientRef 中</span>
    clientRef.<span class="hljs-property">current</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">CozeWebSDK</span>.<span class="hljs-title class_">WebCardRuntime</span>({
      <span class="hljs-comment">// 指定要渲染的 DOM 元素</span>
      <span class="hljs-attr">el</span>: elem,
      <span class="hljs-comment">// 自定义组件映射，定义特定组件的渲染逻辑</span>
      <span class="hljs-attr">customComponentMap</span>: {
        <span class="hljs-comment">// 自定义 NewImage 组件的渲染逻辑</span>
        <span class="hljs-string">'@flowpd/cici-components/NewImage'</span>: <span class="hljs-function">(<span class="hljs-params">{ name, element, props }</span>) =&gt;</span> {
          <span class="hljs-comment">// 打印开发调试信息</span>
          <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"[dev]"</span>, { name, element, props });
          <span class="hljs-comment">// 设置元素的 HTML 内容</span>
          element.<span class="hljs-property">innerHTML</span> = <span class="hljs-string">`Test`</span>;
          <span class="hljs-comment">// 设置元素的宽度</span>
          element.<span class="hljs-property">style</span>.<span class="hljs-property">width</span> = <span class="hljs-string">'100px'</span>;
          <span class="hljs-comment">// 设置元素的高度</span>
          element.<span class="hljs-property">style</span>.<span class="hljs-property">height</span> = <span class="hljs-string">'100px'</span>;
          <span class="hljs-comment">// 设置元素的背景颜色</span>
          element.<span class="hljs-property">style</span>.<span class="hljs-property">background</span> = <span class="hljs-string">'red'</span>;
          <span class="hljs-comment">// 返回一个销毁函数，用于处理组件卸载时的清理工作</span>
          <span class="hljs-keyword">return</span> <span class="hljs-function">() =&gt;</span> {
            <span class="hljs-comment">// destroy, 例如react 等问题</span>
          };
        },
        <span class="hljs-comment">// 自定义 ColumnLayout1_2 组件的渲染逻辑</span>
        <span class="hljs-string">'@flowpd/cici-components/ColumnLayout1_2'</span>: <span class="hljs-function">(<span class="hljs-params">{ name, element, props, renderChildren }</span>) =&gt;</span> {
          <span class="hljs-comment">// 从 props 中解构出 Columns 属性</span>
          <span class="hljs-keyword">const</span> { <span class="hljs-title class_">Columns</span> } = props;
          <span class="hljs-comment">// 遍历 Columns 数组，渲染每个子元素</span>
          <span class="hljs-title class_">Columns</span>.<span class="hljs-title function_">map</span>(<span class="hljs-function">(<span class="hljs-params">column</span>) =&gt;</span> {
            <span class="hljs-keyword">const</span> { content } = column;
            <span class="hljs-keyword">const</span> elem = <span class="hljs-title function_">renderChildren</span>(<span class="hljs-title function_">content</span>());
            element.<span class="hljs-title function_">appendChild</span>(elem);
          });
          <span class="hljs-comment">// 打印开发调试信息</span>
          <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"[dev]"</span>, { name, element, props });
          <span class="hljs-comment">// 设置元素的背景颜色</span>
          element.<span class="hljs-property">style</span>.<span class="hljs-property">background</span> = <span class="hljs-string">'yellow'</span>;
          <span class="hljs-comment">// 设置元素的显示方式为弹性布局</span>
          element.<span class="hljs-property">style</span>.<span class="hljs-property">display</span> = <span class="hljs-string">'flex'</span>;
        },
      },
      <span class="hljs-comment">// 运行时配置选项</span>
      <span class="hljs-attr">runtimeOptions</span>: {
        <span class="hljs-comment">// 解析后的 JSON 数据，定义组件的结构和属性</span>
        <span class="hljs-attr">dsl</span>: <span class="hljs-title class_">JSON</span>.<span class="hljs-title function_">parse</span>(
          <span class="hljs-string">'{"elements":{"7c1EN9VHwU":{"id":"7c1EN9VHwU","name":"FlowpdCiciComponentsColumnLayout1_2","type":"@flowpd/cici-components/ColumnLayout1_2","props":{"Columns":[{"children":["DQKOI54sJV"],"config":{"vertical":"top","width":"auto"},"type":"slot"},{"children":["FE8Y2GcSwb","L3gNU6QxiI"],"config":{"vertical":"top","weight":2,"width":"weighted"},"type":"slot"}],"action":"enableUrl","backgroundColor":"transparent","enableClickEvent":true,"url":{"type":"expression","value":"{{url}}"}},"directives":{}},"DQKOI54sJV":{"id":"DQKOI54sJV","name":"FlowpdCiciComponentsNewImage","type":"@flowpd/cici-components/NewImage","props":{"action":"enableUrl","crop":"aspectFill","enableClickEvent":false,"enableCrop":false,"fixedSize":"medium","mode":"fixed","ratio":"1:1","src":{"type":"expression","value":"{{image}}"}},"directives":{}},"FE8Y2GcSwb":{"id":"FE8Y2GcSwb","name":"FlowpdCiciComponentsText","type":"@flowpd/cici-components/Text","props":{"action":"enableUrl","color":"neutral-100","content":{"type":"expression","value":"{{title}}"},"enableClickEvent":false,"enableLines":true,"fontSize":"large","fontWeight":"bold","lines":1,"textAlign":"left"},"directives":{}},"L3gNU6QxiI":{"id":"L3gNU6QxiI","name":"FlowpdCiciComponentsText","type":"@flowpd/cici-components/Text","props":{"action":"enableUrl","color":"neutral-70","content":{"type":"expression","value":"{{content}}"},"enableClickEvent":false,"enableLines":true,"fontSize":"small","fontWeight":"normal","lines":2,"textAlign":"left"},"directives":{}},"root":{"id":"root","name":"Root","type":"@flowpd/cici-components/PageContainer","children":["7c1EN9VHwU"],"directives":{}}},"rootID":"root","variables":{"content":{"ID":"content","name":"content","defaultValue":"26/22℃ 无持续风向3-4级 28/24℃ 无持续风向&lt;3级 30/25℃ 无持续风向&lt;3级 26/22℃ 无持续风向3-4级 28/24℃ 无持续风向&lt;3级 30/25℃ 无持续风向&lt;3级"},"image":{"ID":"image","name":"image","defaultValue":""},"title":{"ID":"title","name":"title","defaultValue":"【深圳天气预报15天_深圳天气预报15天查询】-中国天气网"},"url":{"ID":"url","name":"url"}}}'</span>
        ),
        <span class="hljs-comment">// 是否只读</span>
        <span class="hljs-attr">readonly</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-comment">// 是否强制远程加载</span>
        <span class="hljs-attr">remoteForce</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-comment">// 主题样式</span>
        <span class="hljs-attr">theme</span>: <span class="hljs-string">'dark'</span>,
        <span class="hljs-comment">// 语言设置</span>
        <span class="hljs-attr">lang</span>: <span class="hljs-string">'en'</span>,
        <span class="hljs-comment">// 渲染完成后的回调函数</span>
        <span class="hljs-attr">afterRender</span>: <span class="hljs-function">() =&gt;</span> {
          <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'[dev] afterRender'</span>);
        },
      },
    });
  }, []);

  <span class="hljs-comment">// 使用 useEffect 处理组件卸载时的清理工作</span>
  <span class="hljs-title function_">useEffect</span>(<span class="hljs-function">() =&gt;</span> {
    <span class="hljs-comment">// 返回一个清理函数，在组件卸载时销毁 CozeWebSDK.WebCardRuntime 实例</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =&gt;</span> {
      clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">destroy</span>();
    };
  }, []);

  <span class="hljs-comment">// 返回组件的 JSX 结构</span>
  <span class="hljs-keyword">return</span> (
    <span class="language-xml"><span class="hljs-tag">&lt;&gt;</span>
      {/* 定义一个按钮，点击时更新运行时的主题为 light */}
      <span class="hljs-tag">&lt;<span class="hljs-name">button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">{()</span> =&gt;</span> {
          clientRef.current?.updateRuntimeOptions({
            theme: 'light',
          });
        }}
      &gt;
        ChangeTheme
      <span class="hljs-tag">&lt;/<span class="hljs-name">button</span>&gt;</span>
      {/* 定义一个 div 元素，使用 ref 绑定 genCard 函数，用于初始化 CozeWebSDK.WebCardRuntime 实例 */}
      <span class="hljs-tag">&lt;<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">{elem</span> =&gt;</span> genCard(elem)} style={{
        margin: '10px',
        width: '500px'
      }} /&gt;
    <span class="hljs-tag">&lt;/&gt;</span></span>
  );
};

<span class="hljs-comment">// 定义 TestCardDemo 组件，用于渲染两个 CozeCard 组件</span>
<span class="hljs-keyword">const</span> <span class="hljs-title class_">TestCardDemo</span>: <span class="hljs-title class_">React</span>.<span class="hljs-property">FC</span> = <span class="hljs-function">() =&gt;</span> {
  <span class="hljs-keyword">return</span> (
    <span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">div</span>&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-name">CozeCard</span> /&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-name">CozeCard</span> /&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span></span>
  );
};

<span class="hljs-comment">// 导出 TestCardDemo 组件，供其他模块使用</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">TestCardDemo</span>;
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import React, { useCallback, useEffect, useRef } from 'react';

// 定义 CozeCard 组件，用于创建和管理 CozeWebSDK.WebCardRuntime 实例
const CozeCard = () =&gt; {
  // 使用 useRef 创建一个可变的引用对象，用于保存 CozeWebSDK.WebCardRuntime 实例
  const clientRef = useRef();

  // 使用 useCallback 缓存函数，避免组件重新渲染时函数重新创建
  const genCard = useCallback((elem) =&gt; {
    // 如果传入的元素为空，直接返回
    if (!elem) {
      return;data 
    }
    // 如果之前已经存在 CozeWebSDK.WebCardRuntime 实例，先销毁它
    if (clientRef.current) {
      clientRef.current.destroy();
    }
    // 创建新的 CozeWebSDK.WebCardRuntime 实例并保存到 clientRef 中
    clientRef.current = new CozeWebSDK.WebCardRuntime({
      // 指定要渲染的 DOM 元素
      el: elem,
      // 自定义组件映射，定义特定组件的渲染逻辑
      customComponentMap: {
        // 自定义 NewImage 组件的渲染逻辑
        '@flowpd/cici-components/NewImage': ({ name, element, props }) =&gt; {
          // 打印开发调试信息
          console.log(&quot;[dev]&quot;, { name, element, props });
          // 设置元素的 HTML 内容
          element.innerHTML = `Test`;
          // 设置元素的宽度
          element.style.width = '100px';
          // 设置元素的高度
          element.style.height = '100px';
          // 设置元素的背景颜色
          element.style.background = 'red';
          // 返回一个销毁函数，用于处理组件卸载时的清理工作
          return () =&gt; {
            // destroy, 例如react 等问题
          };
        },
        // 自定义 ColumnLayout1_2 组件的渲染逻辑
        '@flowpd/cici-components/ColumnLayout1_2': ({ name, element, props, renderChildren }) =&gt; {
          // 从 props 中解构出 Columns 属性
          const { Columns } = props;
          // 遍历 Columns 数组，渲染每个子元素
          Columns.map((column) =&gt; {
            const { content } = column;
            const elem = renderChildren(content());
            element.appendChild(elem);
          });
          // 打印开发调试信息
          console.log(&quot;[dev]&quot;, { name, element, props });
          // 设置元素的背景颜色
          element.style.background = 'yellow';
          // 设置元素的显示方式为弹性布局
          element.style.display = 'flex';
        },
      },
      // 运行时配置选项
      runtimeOptions: {
        // 解析后的 JSON 数据，定义组件的结构和属性
        dsl: JSON.parse(
          '{&quot;elements&quot;:{&quot;7c1EN9VHwU&quot;:{&quot;id&quot;:&quot;7c1EN9VHwU&quot;,&quot;name&quot;:&quot;FlowpdCiciComponentsColumnLayout1_2&quot;,&quot;type&quot;:&quot;@flowpd/cici-components/ColumnLayout1_2&quot;,&quot;props&quot;:{&quot;Columns&quot;:[{&quot;children&quot;:[&quot;DQKOI54sJV&quot;],&quot;config&quot;:{&quot;vertical&quot;:&quot;top&quot;,&quot;width&quot;:&quot;auto&quot;},&quot;type&quot;:&quot;slot&quot;},{&quot;children&quot;:[&quot;FE8Y2GcSwb&quot;,&quot;L3gNU6QxiI&quot;],&quot;config&quot;:{&quot;vertical&quot;:&quot;top&quot;,&quot;weight&quot;:2,&quot;width&quot;:&quot;weighted&quot;},&quot;type&quot;:&quot;slot&quot;}],&quot;action&quot;:&quot;enableUrl&quot;,&quot;backgroundColor&quot;:&quot;transparent&quot;,&quot;enableClickEvent&quot;:true,&quot;url&quot;:{&quot;type&quot;:&quot;expression&quot;,&quot;value&quot;:&quot;{{url}}&quot;}},&quot;directives&quot;:{}},&quot;DQKOI54sJV&quot;:{&quot;id&quot;:&quot;DQKOI54sJV&quot;,&quot;name&quot;:&quot;FlowpdCiciComponentsNewImage&quot;,&quot;type&quot;:&quot;@flowpd/cici-components/NewImage&quot;,&quot;props&quot;:{&quot;action&quot;:&quot;enableUrl&quot;,&quot;crop&quot;:&quot;aspectFill&quot;,&quot;enableClickEvent&quot;:false,&quot;enableCrop&quot;:false,&quot;fixedSize&quot;:&quot;medium&quot;,&quot;mode&quot;:&quot;fixed&quot;,&quot;ratio&quot;:&quot;1:1&quot;,&quot;src&quot;:{&quot;type&quot;:&quot;expression&quot;,&quot;value&quot;:&quot;{{image}}&quot;}},&quot;directives&quot;:{}},&quot;FE8Y2GcSwb&quot;:{&quot;id&quot;:&quot;FE8Y2GcSwb&quot;,&quot;name&quot;:&quot;FlowpdCiciComponentsText&quot;,&quot;type&quot;:&quot;@flowpd/cici-components/Text&quot;,&quot;props&quot;:{&quot;action&quot;:&quot;enableUrl&quot;,&quot;color&quot;:&quot;neutral-100&quot;,&quot;content&quot;:{&quot;type&quot;:&quot;expression&quot;,&quot;value&quot;:&quot;{{title}}&quot;},&quot;enableClickEvent&quot;:false,&quot;enableLines&quot;:true,&quot;fontSize&quot;:&quot;large&quot;,&quot;fontWeight&quot;:&quot;bold&quot;,&quot;lines&quot;:1,&quot;textAlign&quot;:&quot;left&quot;},&quot;directives&quot;:{}},&quot;L3gNU6QxiI&quot;:{&quot;id&quot;:&quot;L3gNU6QxiI&quot;,&quot;name&quot;:&quot;FlowpdCiciComponentsText&quot;,&quot;type&quot;:&quot;@flowpd/cici-components/Text&quot;,&quot;props&quot;:{&quot;action&quot;:&quot;enableUrl&quot;,&quot;color&quot;:&quot;neutral-70&quot;,&quot;content&quot;:{&quot;type&quot;:&quot;expression&quot;,&quot;value&quot;:&quot;{{content}}&quot;},&quot;enableClickEvent&quot;:false,&quot;enableLines&quot;:true,&quot;fontSize&quot;:&quot;small&quot;,&quot;fontWeight&quot;:&quot;normal&quot;,&quot;lines&quot;:2,&quot;textAlign&quot;:&quot;left&quot;},&quot;directives&quot;:{}},&quot;root&quot;:{&quot;id&quot;:&quot;root&quot;,&quot;name&quot;:&quot;Root&quot;,&quot;type&quot;:&quot;@flowpd/cici-components/PageContainer&quot;,&quot;children&quot;:[&quot;7c1EN9VHwU&quot;],&quot;directives&quot;:{}}},&quot;rootID&quot;:&quot;root&quot;,&quot;variables&quot;:{&quot;content&quot;:{&quot;ID&quot;:&quot;content&quot;,&quot;name&quot;:&quot;content&quot;,&quot;defaultValue&quot;:&quot;26/22℃ 无持续风向3-4级 28/24℃ 无持续风向&lt;3级 30/25℃ 无持续风向&lt;3级 26/22℃ 无持续风向3-4级 28/24℃ 无持续风向&lt;3级 30/25℃ 无持续风向&lt;3级&quot;},&quot;image&quot;:{&quot;ID&quot;:&quot;image&quot;,&quot;name&quot;:&quot;image&quot;,&quot;defaultValue&quot;:&quot;&quot;},&quot;title&quot;:{&quot;ID&quot;:&quot;title&quot;,&quot;name&quot;:&quot;title&quot;,&quot;defaultValue&quot;:&quot;【深圳天气预报15天_深圳天气预报15天查询】-中国天气网&quot;},&quot;url&quot;:{&quot;ID&quot;:&quot;url&quot;,&quot;name&quot;:&quot;url&quot;}}}'
        ),
        // 是否只读
        readonly: false,
        // 是否强制远程加载
        remoteForce: false,
        // 主题样式
        theme: 'dark',
        // 语言设置
        lang: 'en',
        // 渲染完成后的回调函数
        afterRender: () =&gt; {
          console.log('[dev] afterRender');
        },
      },
    });
  }, []);

  // 使用 useEffect 处理组件卸载时的清理工作
  useEffect(() =&gt; {
    // 返回一个清理函数，在组件卸载时销毁 CozeWebSDK.WebCardRuntime 实例
    return () =&gt; {
      clientRef.current?.destroy();
    };
  }, []);

  // 返回组件的 JSX 结构
  return (
    &lt;&gt;
      {/* 定义一个按钮，点击时更新运行时的主题为 light */}
      &lt;button
        onClick={() =&gt; {
          clientRef.current?.updateRuntimeOptions({
            theme: 'light',
          });
        }}
      &gt;
        ChangeTheme
      &lt;/button&gt;
      {/* 定义一个 div 元素，使用 ref 绑定 genCard 函数，用于初始化 CozeWebSDK.WebCardRuntime 实例 */}
      &lt;div ref={elem =&gt; genCard(elem)} style={{
        margin: '10px',
        width: '500px'
      }} /&gt;
    &lt;/&gt;
  );
};

// 定义 TestCardDemo 组件，用于渲染两个 CozeCard 组件
const TestCardDemo: React.FC = () =&gt; {
  return (
    &lt;div&gt;
      &lt;CozeCard /&gt;
      &lt;CozeCard /&gt;
    &lt;/div&gt;
  );
};

// 导出 TestCardDemo 组件，供其他模块使用
export default TestCardDemo;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h4 id="a014bab9" tabindex="-1"><strong>卡片参数</strong></h4>
<p>卡片初始化和个性化配置的关键参数说明如下表所示。</p>
<!-- @cols-width: 252,100,100,480 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 252px;"/><col style="width: 100px;"/><col style="width: 100px;"/><col style="width: 480px;"/></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>类型</strong></th>
<th><strong>是否必选</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>el</td>
<td>HTML Element</td>
<td>必选</td>
<td>卡片需要渲染的 HTML 元素。</td>
</tr>
<tr>
<td>customComponentMap</td>
<td>Object</td>
<td>必选</td>
<td>自定义组件样式，其中 key 为组件的名称。你可以从 data 字段的卡片配置中获取组件名称。例如：@flowpd/cici-components/NewImage。</td>
</tr>
<tr>
<td>runtimeOptions</td>
<td>Object</td>
<td>可选</td>
<td>运行时的选项。</td>
</tr>
<tr>
<td>runtimeOptions.dsl</td>
<td>Object</td>
<td>可选</td>
<td>DSL 数据，定义卡片的结构和内容。</td>
</tr>
<tr>
<td>
<p>runtimeOptions.remoteForce</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>是否每次都从远程拉取组件。</p>
<ul data-style="0">
<li><strong>true</strong>：每次自动拉取。</li>
<li><strong>false</strong>：不自动拉取。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>runtimeOptions.debug</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>是否打印报错信息。</p>
<ul data-style="0">
<li><strong>true</strong>：打印。</li>
<li><strong>false</strong>：不打印。</li>
</ul>
</td>
</tr>
<tr>
<td>runtimeOptions.readonly</td>
<td>Boolean</td>
<td>可选</td>
<td>是否开启只读模式，只读模式下卡片的交互效果不生效，例如无法跳转到其他网页等。</td>
</tr>
<tr>
<td>runtimeOptions.lang</td>
<td>String</td>
<td>可选</td>
<td>设置卡片内容的语言。例如 zh。</td>
</tr>
<tr>
<td>
<p>runtimeOptions.theme</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>卡片的深浅模式。</p>
<ul data-style="0">
<li><strong>light</strong>：浅色模式。</li>
<li><strong>dark</strong>：深色模式。</li>
</ul>
</td>
</tr>
<tr>
<td>runtimeOptions.afterRender</td>
<td>Function</td>
<td>可选</td>
<td>回调函数，在组件加载成功时自动触发。</td>
</tr>
<tr>
<td>runtimeOptions.onError</td>
<td>Function</td>
<td>可选</td>
<td>回调函数，在渲染卡片失败时自动触发。</td>
</tr>
<tr>
<td>
<p>runtimeOptions.eventCallbacks</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>交互事件的回调函数，包括：</p>
<ul data-style="0">
<li><strong>onElementOut（targetElemtent, linkurl）=&gt; void</strong>：当鼠标从卡片链接上移出的时候，触发此函数。</li>
<li><strong>onElementOver（targetElemtent, linkurl）=&gt; void</strong>：当鼠标在卡片链接上移动的时候，触发此函数。</li>
<li><strong>sendMsg</strong>：当点击发送消息按钮时触发此函数。</li>
<li><strong>previewImage（{url}）=&gt; void</strong>：当点击图片的时候触发此函数。</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><h4 id="87fc5c91" tabindex="-1">自定义卡片组件的样式</h4>
<p>卡片中的组件使用默认的展示效果，你也可以通过 Card SDK 的 <code>customComponentMap</code> 接口自定义组件的渲染逻辑，实现个性化的样式和交互效果。</p>
<p><code>customComponentMap</code> 接口的结构如下：</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">type</span> <span class="hljs-title class_">DestoryFunc</span> = <span class="hljs-function">() =&gt;</span> <span class="hljs-built_in">void</span>;
<span class="hljs-keyword">type</span> <span class="hljs-title class_">RenderCustomComponentFunc</span> = <span class="hljs-function">(<span class="hljs-params"><span class="hljs-attr">params</span>: {
    name: <span class="hljs-built_in">string</span>, 
    element: HTMLDivElement, 
    props: Record&lt;<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>&gt;, 
    renderChildren: (node: React.ReactNode) =&gt; HTMLDivElement}
</span>) =&gt;</span> <span class="hljs-title class_">DestoryFunc</span> | <span class="hljs-built_in">void</span>;

<span class="hljs-keyword">interface</span> {
     <span class="hljs-attr">customComponentMap</span>?: <span class="hljs-title class_">Record</span>&lt;<span class="hljs-built_in">string</span>, <span class="hljs-title class_">RenderCustomComponentFunc</span>&gt;;
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="type DestoryFunc = () =&gt; void;
type RenderCustomComponentFunc = (params: {
    name: string, 
    element: HTMLDivElement, 
    props: Record&lt;string, any&gt;, 
    renderChildren: (node: React.ReactNode) =&gt; HTMLDivElement}
) =&gt; DestoryFunc | void;

interface {
     customComponentMap?: Record&lt;string, RenderCustomComponentFunc&gt;;
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<p>说明：</p>
<ul data-style="0">
<li><code>RenderCustomComponentFunc</code> 是用于渲染卡片组件的渲染函数。你需要自行实现该函数，函数会接收到卡片组件传递的参数，并返回一个销毁函数。RenderCustomComponentFunc 支持的属性设置如下： <!-- @cols-width: 100,100,100,273,422 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;"/><col style="width: 100px;"/><col style="width: 100px;"/><col style="width: 273px;"/><col style="width: 422px;"/></colgroup><thead>
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
<td>name</td>
<td>String</td>
<td>必选</td>
<td>@flowpd/cici-components/NewImage</td>
<td>元素的名称，通常用于标识和描述元素。</td>
</tr>
<tr>
<td>element</td>
<td>Object</td>
<td>必选</td>
<td>{ style: { width: '100px', height: '100px' } }</td>
<td>指定挂载自定义组件的 HTML 元素，默认为一个空的 <div> 容器。</div></td>
</tr>
<tr>
<td>
<p>props</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>props:</p>
<p>{</p>
<p>blockId:{element.id}</p>
<p>children: {子节点}</p>
<p>lang: zh</p>
<p>cardState： （dsl.status</p>
<p>...elementProps (处理后的）</p>
<p>}</p>
</td>
<td>
<p>渲染组件时使用的属性，你可以从浏览器的开发者工具中查看 props 属性的值。</p>
</td>
</tr>
<tr>
<td>renderChildren</td>
<td>Function</td>
<td>必选</td>
<td>-</td>
<td>渲染子组件的方法。如果组件中有子组件，可以使用 renderChildren 函数将子组件渲染到指定的 HTML 元素中。</td>
</tr>
</tbody>
</table>
</div></li>
<li><code>RenderCustomComponentFunc</code> 的返回值是一个销毁函数，不需要某个组件时可以调用此函数销毁组件。你可以根据业务场景按需选择是否销毁组件。</li>
</ul>
<h4 id="eaf9d12b" tabindex="-1"><strong>设置样式的示例代码</strong></h4>
<p>以下是通过<code>customComponentMap</code>接口为组件 @flowpd/cici-components/NewImage 定制样式的示例代码。</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-attr">customComponentMap</span>: {
    <span class="hljs-string">'@flowpd/cici-components/NewImage'</span>: <span class="hljs-function">(<span class="hljs-params">{ name, element, props }</span>) =&gt;</span> {
      element.<span class="hljs-property">style</span>.<span class="hljs-property">width</span> = <span class="hljs-string">'100px'</span>;
      element.<span class="hljs-property">style</span>.<span class="hljs-property">height</span> = <span class="hljs-string">'100px'</span>;
      <span class="hljs-keyword">const</span> renderRoot = <span class="hljs-title function_">createRoot</span>(element); <span class="hljs-comment">//使用react渲染组件</span>
      renderRoot.<span class="hljs-title function_">render</span>(<span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span>
        <span class="hljs-attr">width:</span> '<span class="hljs-attr">100</span>%',
        <span class="hljs-attr">height:</span> '<span class="hljs-attr">100</span>%',
        <span class="hljs-attr">background:</span> '<span class="hljs-attr">red</span>',
      }}&gt;</span>
        Image Test
      <span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span></span>);
      <span class="hljs-keyword">return</span> <span class="hljs-function">() =&gt;</span> {
        renderRoot.<span class="hljs-title function_">unmount</span>(); <span class="hljs-comment">//销毁函数</span>
      }
    }
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="customComponentMap: {
    '@flowpd/cici-components/NewImage': ({ name, element, props }) =&gt; {
      element.style.width = '100px';
      element.style.height = '100px';
      const renderRoot = createRoot(element); //使用react渲染组件
      renderRoot.render(&lt;div style={{
        width: '100%',
        height: '100%',
        background: 'red',
      }}&gt;
        Image Test
      &lt;/div&gt;);
      return () =&gt; {
        renderRoot.unmount(); //销毁函数
      }
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h2 id="36eed146" tabindex="-1">常见问题</h2>
<h3 id="51823aba" tabindex="-1">Card SDK 可以在 Chat SDK 中使用吗？</h3>
<p>集成 Chat SDK 后无需再集成 Card SDK。Chat SDK 本身已内置对卡片功能的支持，无需额外集成 Card SDK。如果你的聊天应用中未使用 Chat SDK，但需要实现卡片效果，可以直接使用 Card SDK 将渲染后的卡片集成到你自行实现的聊天应用中。</p>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button class="feedbackButton-GuivRC" type="button"><span class="feedbackButtonIcon-PqHraK"></span><span>有帮助</span></button><button class="feedbackButton-GuivRC" type="button"><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm" data-discover="true" href="/developer_guides_ui_builder_web_sdk"><div class="cardLabel-sDu1uC"><svg aria-hidden="true" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12">Web SDK（低代码）</div></a><a class="card-T4zaCm nextCard-lFoioT" data-discover="true" href="/dev_how_to_guides_realtime_overview"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg aria-hidden="true" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">智能音视频概述</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#b509274e" href="#b509274e" title="功能简介">功能简介</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#5efadaff" href="#5efadaff" title="效果预览">效果预览</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#08bd7843" href="#08bd7843" title="功能简介">功能简介</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#783bdba5" href="#783bdba5" title="浏览器兼容性">浏览器兼容性</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#9e92dbac" href="#9e92dbac" title="配置流程">配置流程</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#2c5fef61" href="#2c5fef61" title="步骤一：发布智能体">步骤一：发布智能体</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#37fdb1a4" href="#37fdb1a4" title="步骤二：安装 Card SDK">步骤二：安装 Card SDK</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#e8eff981" href="#e8eff981" title="步骤三：配置卡片属性">步骤三：配置卡片属性</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#48407e15" href="#48407e15" title="示例代码">示例代码</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#a014bab9" href="#a014bab9" title="卡片参数">卡片参数</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#87fc5c91" href="#87fc5c91" title="自定义卡片组件的样式">自定义卡片组件的样式</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#eaf9d12b" href="#eaf9d12b" title="设置样式的示例代码">设置样式的示例代码</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#36eed146" href="#36eed146" title="常见问题">常见问题</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#51823aba" href="#51823aba" title="Card SDK 可以在 Chat SDK 中使用吗？">Card SDK 可以在 Chat SDK 中使用吗？</a></div></div></div></div></div></div></div></div>
</body></html>