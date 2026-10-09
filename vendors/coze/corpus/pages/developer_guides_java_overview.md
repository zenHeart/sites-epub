<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">Java SDK 概述</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/5956.1729cb00c0.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.ca52691239.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/developer_guides_java_overview"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/developer_guides_java_overview.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
  
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/developer_guides_java_overview" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b97434bdbc784e3ce84ce" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a55df9a4bdbc784e3c9738f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf30d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf317" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf31d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf325" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf334" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf32e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf35a" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf362" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8e614bdbc784e3cce185" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3e2c" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fa8" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc40e8" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Chat SDK">Chat SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc40ef" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Python SDK">Python SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc412c" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Node.js SDK">Node.js SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4132" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Java SDK">Java SDK</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc4180" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:56px" href="/developer_guides_java_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="Java SDK 概述">Java SDK 概述</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4185" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_java_installation" data-discover="true"><span class="nodeTitle-ONnqtP" title="安装 Java SDK">安装 Java SDK</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc418d" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_java_access_token" data-discover="true"><span class="nodeTitle-ONnqtP" title="配置访问密钥">配置访问密钥</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4194" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_java_getting_started" data-discover="true"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc41c6" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Go SDK">Go SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4245" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_vibe_coding_websdk" data-discover="true"><span class="nodeTitle-ONnqtP" title="Web SDK（AI 编程）">Web SDK（AI 编程）</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc424c" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_ui_builder_web_sdk" data-discover="true"><span class="nodeTitle-ONnqtP" title="Web SDK（低代码）">Web SDK（低代码）</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4251" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Card SDK">Card SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc529d" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8e4bdbc784e3cc445f" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/developer_guides_coze_cli" data-discover="true"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf33f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf369" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/guides_FAQ" data-discover="true"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>SDK 参考</span><span class="separator-KB9yMa">/</span><span>Java SDK</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">Java SDK 概述</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">Java SDK 概述</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg><span>复制页面</span></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>Coze API SDK for Java 是一个扣子官方提供的 SDK 工具包，你可以通过 Java SDK 将扣子的 OpenAPI 集成到你的应用程序中。Coze Java SDK 支持所有扣子的官方鉴权方式，具备高度的灵活性和高可用性，显著提升 OpenAPI 的使用效率。你可以通过 maven 仓库快速安装 Coze Java SDK，用你的访问密钥初始化 SDK，然后就可以开始安全、高效地通过 OpenAPI 访问你的 AI 智能体。<br>
Coze Java SDK 遵循用户友好的设计风格，可简化你的开发工作，且适用于所有技能水平开发者使用。</p>
<h2 id="22a61062" tabindex="-1">源码地址</h2>
<p>访问 <a href="https://github.com/coze-dev/coze-java" target="_blank">GitHub</a> 获取 Coze API SDK for Java 源码。</p>
<div class="topic-callout notice"><p class="topic-callout-title">注意</p>
<p>从扣子 GitHub 仓库获取的源码和示例代码中，<code>base_url</code> 默认设置为域名 <code>COZE_COM_BASE_URL</code>，使用源码前应手动将其修改为域名 <code>COZE_CN_BASE_URL</code>。</p>
</div>
<h2 id="05bfc7c7" tabindex="-1">示例代码</h2>
<p>Coze Java SDK 提供各种授权方式、各种使用方式的示例代码，便于开发者直接参考使用。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<ul data-style="0">
<li>Coze Java SDK 支持扣子所有 OpenAPI，对应的 API 文档可参考 <a href="/developer_guides/coze_api_overview" target="_blank">API 介绍</a>。</li>
<li>示例代码将持续更新和补充，各种场景的 Coze Java SDK <strong>最新版本</strong>示例代码可参考 <a href="https://github.com/coze-dev/coze-java" target="_blank">GitHub</a>。</li>
</ul>
</div>
<p>常见场景的示例代码及说明如下：</p>
<!-- @cols-width: 121,200,403 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 121px;" /><col style="width: 200px;" /><col style="width: 403px;" /></colgroup><thead>
<tr>
<th>
<p><strong>模块</strong></p>
</th>
<th>
<p><strong>示例文件</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">
<p>授权</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/TokenAuthExample.java" target="_blank">TokenAuthExample.java</a></p>
</td>
<td>
<p>通过个人访问密钥实现 OpenAPI 鉴权。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/WebOAuthExample.java" target="_blank">WebOAuthExample.java</a></p>
</td>
<td>
<p>通过 OAuth 授权码方式实现授权与 OpenAPI 鉴权。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/JWTOAuthExample.java" target="_blank">JWTsOauthExample.java</a></p>
</td>
<td>
<p>通过 OAuth JWT 方式实现授权与 OpenAPI 鉴权。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/PKCEOAuthExample.java" target="_blank">PKCEOauthExample.java</a></p>
</td>
<td>
<p>通过 OAuth PKCE 方式实现授权与 OpenAPI 鉴权。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/DevicesOAuthExample.java" target="_blank">DevicesOAuthExample.java</a></p>
</td>
<td>
<p>通过 OAuth 设备码方式实现授权与 OpenAPI 鉴权。</p>
</td>
</tr>
<tr>
<td rowspan="4">
<p>对话</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/chat/ChatExample.java" target="_blank">ChatExample.java</a></p>
</td>
<td>
<p>发起对话，响应方式为非流式响应。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/chat/StreamChatExample.java" target="_blank">StreamChatExample.java</a></p>
</td>
<td>
<p>发起对话，响应方式为流式响应。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/chat/ChatWithImageExample.java" target="_blank">ChatWithImageExample.java</a></p>
</td>
<td>
<p>发起对话，对话中上传文件，并发送多模态内容。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/chat/SubmitToolOutputExample.java" target="_blank">SubmitToolOutputExample.java</a></p>
</td>
<td>
<p>端插件。</p>
</td>
</tr>
<tr>
<td rowspan="4">
<p>会话与消息管理</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/conversation/ConversationCreateExample.java" target="_blank">CreateConversationExample.java</a></p>
</td>
<td>
<p>创建会话。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/conversation/ConversationsListExample.java" target="_blank">ListConversationsExample.java</a></p>
</td>
<td>
<p>查询会话列表。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/conversation/message/MessageCrudExample.java" target="_blank">MessageCrudExample.java</a></p>
</td>
<td>
<p>创建、更新、删除消息。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/conversation/message/MessageListExample.java" target="_blank">MessageListExample.java</a></p>
</td>
<td>
<p>查询指定对话中的消息列表。</p>
</td>
</tr>
<tr>
<td rowspan="4">
<p>工作流</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/workflow/RunWorkflowExample.java" target="_blank">RunWorkflowExample.java</a></p>
</td>
<td>
<p>运行工作流，响应方式为非流式响应。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/workflow/StreamWorkflowExample.java" target="_blank">StreamWorkflowExample.java</a></p>
</td>
<td>
<p>运行工作流，响应方式为流式响应，且工作流中包含问答节点。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/workflow/StreamWorkflowChatExample.java" target="_blank">StreamWorkflowChatExample.java</a></p>
</td>
<td>
<p>运行对话流。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/workflow/AsyncRunWorkflowExample.java" target="_blank">AsyncRunWorkflowExample.java</a></p>
</td>
<td>
<p>异步运行工作流。</p>
</td>
</tr>
<tr>
<td>
<p>智能体管理</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/bot/BotPublishExample.java" target="_blank">BotPublishExample.java</a></p>
</td>
<td>
<p>创建一个草稿状态的智能体，更新智能体，并发布智能体为 API 服务。</p>
</td>
</tr>
<tr>
<td rowspan="5">
<p>语音</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/audio/room/AudioRoomsCreateExample.java" target="_blank">AudioRoomsCreateExample.java</a></p>
</td>
<td>
<p>RTC 音视频通话场景中，创建音视频房间。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/audio/speech/SpeechCreateExample.java" target="_blank">SpeechCreateExample.java</a></p>
</td>
<td>
<p>语音合成，将文本转为语音，并将生成的语音保存为音频文件。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/audio/transcriptions/CreateTranscriptionExample.java" target="_blank">CreateTranscriptionExample.java</a></p>
</td>
<td>
<p>语音识别，将指定音频文件转录为文本。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/audio/voice/VoiceCloneExample.java" target="_blank">VoiceCloneExample.java</a></p>
</td>
<td>
<p>克隆音色。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/audio/voice/VoiceListExample.java" target="_blank">VoiceListExample.java</a></p>
</td>
<td>
<p>查询音色列表。</p>
</td>
</tr>
<tr>
<td rowspan="3">
<p>WebSocket 语音通话</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/websocket/chat/ChatExample.java" target="_blank">ChatExample.java</a></p>
</td>
<td>
<p>WebSocket 语音通话。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/websocket/audio/speech/WebsocketAudioSpeechExample.java" target="_blank">WebsocketAudioSpeechExample.java</a></p>
</td>
<td>
<p>语音合成，将文本转为语音，并将生成的语音保存为音频文件。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/websocket/audio/transcriptions/WebsocketTranscriptionsExample.java" target="_blank">WebsocketTranscriptionsExample.java</a></p>
</td>
<td>
<p>语音识别，将指定音频文件转录为文本。</p>
</td>
</tr>
<tr>
<td>
<p>工作空间</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/workspace/WorkspaceListExample.java" target="_blank">ListWorkspaceExample.java</a></p>
</td>
<td>
<p>查询工作空间列表。</p>
</td>
</tr>
<tr>
<td rowspan="4">
<p>知识库</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/datasets/DatasetCrudExample.java" target="_blank">DatasetCrudExample.java</a></p>
</td>
<td>
<p>创建、更新和删除知识库。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/datasets/DatasetListExample.java" target="_blank">DatasetListExample.java</a></p>
</td>
<td>
<p>查询指定工作空间下的知识库。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/tree/main/example/src/main/java/example/datasets/image" target="_blank">datasets/image</a></p>
</td>
<td>
<p>图片知识库管理，包含：</p>
<ul data-style="0">
<li>上传图片类型的知识库文件。</li>
<li>更新知识库的图片描述。</li>
<li>查看知识库图片列表。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/tree/main/example/src/main/java/example/datasets/document" target="_blank">datasets/document</a></p>
</td>
<td>
<p>文本知识库管理，包含：</p>
<ul data-style="0">
<li>上传文本类型的知识库文件。</li>
<li>查询、修改和删除文本知识库文件。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>文件</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/file/FileExample.java" target="_blank">FileExample.java</a></p>
</td>
<td>
<p>文件上传，包含：</p>
<ul data-style="0">
<li>文件上传。</li>
<li>获取文件详情。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>变量</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/variables/VariableExample.java" target="_blank">VariableExample.java</a></p>
</td>
<td>
<p>变量管理，包含：</p>
<ul data-style="0">
<li>获取用户变量的值。</li>
<li>设置用户变量的值。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>复制模板</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/template/TemplateDuplicateExample.java" target="_blank">TemplateDuplicateExample.java</a></p>
</td>
<td>
<p>复制商店中的模板到指定工作空间。</p>
</td>
</tr>
<tr>
<td rowspan="2">
<p>账单和权益额度</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/commerce/benefit/bill/CrudExample.java" target="_blank">benefit/bill/CrudExample.java</a></p>
</td>
<td>
<p>导出账单并查询账单文件。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/commerce/benefit/limitations/CrudExample.java" target="_blank">benefit/limitations/CrudExample.java</a></p>
</td>
<td>
<p>创建、查询、更新硬件设备的权益额度。</p>
</td>
</tr>
<tr>
<td>
<p>异常处理</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/HandlerExceptionExample.java" target="_blank">HandlerExceptionExample.java</a></p>
</td>
<td>
<p>处理 API 异常。</p>
</td>
</tr>
<tr>
<td rowspan="3">
<p>客户端管理</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/HandlerExceptionExample.java" target="_blank">HandlerExceptionExample.java</a></p>
</td>
<td>
<p>修改日志级别。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/service/SetRequestTimeoutExample.java" target="_blank">SetRequestTimeoutExample.java</a></p>
</td>
<td>
<p>设置请求超时时间。</p>
</td>
</tr>
<tr>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/service/InitClientExample.java" target="_blank">InitServiceExample.java</a></p>
</td>
<td>
<p>初始化客户端。</p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="dcc539a5" tabindex="-1">异常处理</h2>
<p>当调用 API 失败时，SDK 会抛出 <a href="https://github.com/coze-dev/coze-java/blob/main/api/src/main/java/com/coze/openapi/client/exception/CozeApiExcetion.java" target="_blank">CozeAPIException</a> 异常；当鉴权失败的时候，SDK 会抛出 <a href="https://github.com/coze-dev/coze-java/blob/main/api/src/main/java/com/coze/openapi/client/exception/CozeAuthException.java" target="_blank">CozeAuthException</a> 异常。开发者可以根据自己的需求捕获对应的异常，其中 <a href="https://github.com/coze-dev/coze-java/blob/main/api/src/main/java/com/coze/openapi/client/exception/CozeApiExcetion.java" target="_blank">CozeAPIException</a> 异常会获取到异常接口的错误码，API 错误码的相关说明及处理方式可参考<a href="/developer_guides/coze_error_codes" target="_blank">错误码</a>。</p>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/developer_guides_nodejs_getting_started" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">快速开始</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/developer_guides_java_installation" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">安装 Java SDK</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="源码地址" href="#22a61062" data-href="#22a61062">源码地址</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="示例代码" href="#05bfc7c7" data-href="#05bfc7c7">示例代码</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="异常处理" href="#dcc539a5" data-href="#dcc539a5">异常处理</a></div></div></div></div></div></div></div></div>
</body></html>