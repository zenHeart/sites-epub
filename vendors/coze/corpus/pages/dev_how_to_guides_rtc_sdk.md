<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">集成火山引擎 RTC SDK</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/4760.77ece367d4.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.782417a8ae.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/dev_how_to_guides_rtc_sdk"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/dev_how_to_guides_rtc_sdk.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/dev_how_to_guides_rtc_sdk" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" style="width:300px" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b97434bdbc784e3ce84ce" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a55df9a4bdbc784e3c9738f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf30d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf317" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf31d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf325" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf334" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf32e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf35a" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf362" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8e614bdbc784e3cce185" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3e2c" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fa8" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc529d" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8bc84bdbc784e3cc52a5" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/dev_how_to_guides_realtime_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="智能音视频概述">智能音视频概述</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52ad" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/dev_how_to_guides_realtime_playground" data-discover="true"><span class="nodeTitle-ONnqtP" title="体验智能音视频 Demo">体验智能音视频 Demo</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52b5" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/dev_how_to_guides_realtime_access" data-discover="true"><span class="nodeTitle-ONnqtP" title="音视频接入方案对比">音视频接入方案对比</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52bf" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="基于 WebSocket 实现音频通话">基于 WebSocket 实现音频通话</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc52c6" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="基于 RTC 实现音视频通话">基于 RTC 实现音视频通话</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8bc84bdbc784e3cc52cc" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/dev_how_to_guides_access_process" data-discover="true"><span class="nodeTitle-ONnqtP" title="接入流程">接入流程</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52d5" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/dev_how_to_guides_Realtime_web" data-discover="true"><span class="nodeTitle-ONnqtP" title="集成音视频 Realtime Web SDK">集成音视频 Realtime Web SDK</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52dd" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/dev_how_to_guides_realtime_iOS" data-discover="true"><span class="nodeTitle-ONnqtP" title="集成音视频 Realtime iOS SDK">集成音视频 Realtime iOS SDK</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc5313" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/dev_how_to_guides_realtime_android" data-discover="true"><span class="nodeTitle-ONnqtP" title="集成音视频 Realtime Android SDK">集成音视频 Realtime Android SDK</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc5345" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/dev_how_to_guides_realtime_embedded" data-discover="true"><span class="nodeTitle-ONnqtP" title="集成音视频 Realtime 嵌入式 SDK">集成音视频 Realtime 嵌入式 SDK</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc534d" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:56px" href="/dev_how_to_guides_rtc_sdk" data-discover="true"><span class="nodeTitle-ONnqtP" title="集成火山引擎 RTC SDK">集成火山引擎 RTC SDK</span></a></div></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc52e5" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/dev_how_to_guides_audio_message" data-discover="true"><span class="nodeTitle-ONnqtP" title="基于 HTTP 请求实现语音消息">基于 HTTP 请求实现语音消息</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52ed" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="语音与音色">语音与音色</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc52f3" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="终端用户用量管控">终端用户用量管控</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc533c" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/dev_how_to_guides_realtime_faq" data-discover="true"><span class="nodeTitle-ONnqtP" title="音视频常见问题">音视频常见问题</span></a></div></div></div><div id="tree-node-6a3b8b8e4bdbc784e3cc445f" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/developer_guides_coze_cli" data-discover="true"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf33f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf369" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/guides_FAQ" data-discover="true"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA" style="width:calc(100% - 300px);--anchor-width:260px"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>音视频</span><span class="separator-KB9yMa">/</span><span>基于 RTC 实现音视频通话</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">集成火山引擎 RTC SDK</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">集成火山引擎 RTC SDK</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>本文介绍在 PC 端、微信小程序、Electron 等跨平台智能终端上，通过火山引擎 RTC SDK 实现与智能体的音视频通话功能。</p>
<h2 id="17b2d2af" tabindex="-1">前提条件</h2>
<p>开始集成 RTC SDK 前，请确保开发环境满足以下要求：</p>
   <!-- @cols-width: 158,658 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 158px;" /><col style="width: 658px;" /></colgroup><thead>
<tr>
<th>
<p><strong>操作</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>发布智能体</p>
</td>
<td>
<p>已成功搭建并发布智能体为 API 服务。搭建步骤可参考<a href="/tutorial/video_bot" target="_blank">搭建可视化智能体</a>或<a href="/tutorial/low_latency_voice_assistant" target="_blank">搭建低延时语音助手</a>，发布步骤请参见<a href="/guides/publish_agent_api" target="_blank">发布为 API 服务</a>。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>若需使用视频理解能力，请为智能体配置一个视觉模型，例如<strong>豆包视觉理解</strong>模型。</p>
</div>
</td>
</tr>
<tr>
<td>
<p>获取访问密钥</p>
</td>
<td>
<p>获取访问密钥，用于身份认证与鉴权。</p>
<ul data-style="0">
<li><strong>体验或调试场景</strong>：建议生成短期的个人访问令牌（PAT），以快速完成 Realtime SDK 的整体流程。个人访问令牌的获取方法请参见<a href="/developer_guides/pat" target="_blank">添加个人访问令牌</a>。</li>
<li><strong>线上环境</strong>：在线上环境中，应使用服务访问令牌（SAT）或 OAuth 鉴权方案，各鉴权方式的详细说明请参考<a href="/developer_guides/authentication" target="_blank">鉴权方式概述</a>。</li>
</ul>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>扣子编程 SDK 封装了多种鉴权方式，能够有效简化鉴权流程，你可以参考<a href="https://github.com/coze-dev/coze-js/tree/main/examples/coze-js-node/src/auth" target="_blank">鉴权示例代码</a>实现不同方式的 OAuth 认证，以获取和管理访问扣子编程 API 所需的令牌。</p>
</div>
</td>
</tr>
<tr>
<td>
<p>开通 RTC 服务</p>
</td>
<td>
<p>在<a href="https://console.volcengine.com/auth/login/" target="_blank">火山引擎控制台</a>上<a href="https://www.volcengine.com/docs/6348/69865" target="_blank">开通 RTC 服务</a>。</p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="4ba630b1" tabindex="-1">实现流程</h2>
<h3 id="449736f5" tabindex="-1">步骤一：创建智能体并发布为 API 服务</h3>
<p>搭建智能体，详细步骤请参见<a href="/guides/agent_quick_start" target="_blank">搭建一个低代码智能体</a>。<br>
发布智能体为 API 服务，详细步骤请参见<a href="/guides/publish_agent_api" target="_blank">发布为 API 服务</a>。</p>
<h3 id="e388df2e" tabindex="-1">步骤二：集成 RTC SDK</h3>
<p>根据业务需求选择合适的 SDK，以下是各平台的 SDK 集成指南：</p>
   <!-- @cols-width: 220,579 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 220px;" /><col style="width: 579px;" /></colgroup><thead>
<tr>
<th>
<p><strong>平台</strong></p>
</th>
<th>
<p><strong>SDK 集成指南</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>macOS</p>
</td>
<td>
<p><a href="https://www.volcengine.com/docs/6348/1169314" target="_blank">集成 macOS SDK (C++)</a><br>
<a href="https://www.volcengine.com/docs/6348/70131" target="_blank">集成 macOS SDK (Objective-C)</a></p>
</td>
</tr>
<tr>
<td>
<p>Windows</p>
</td>
<td>
<p><a href="https://www.volcengine.com/docs/6348/70130" target="_blank">集成 Windows SDK</a></p>
</td>
</tr>
<tr>
<td>
<p>Linux</p>
</td>
<td>
<p><a href="https://www.volcengine.com/docs/6348/131050" target="_blank">跑通 Linux 桌面版 Demo</a><br>
<a href="https://www.volcengine.com/docs/6348/141350" target="_blank">跑通 Linux 命令行版 Demo</a></p>
</td>
</tr>
<tr>
<td>
<p>微信小程序</p>
</td>
<td>
<p><a href="https://www.volcengine.com/docs/6348/78966" target="_blank">集成微信小程序 SDK</a></p>
</td>
</tr>
<tr>
<td>
<p>Electron</p>
</td>
<td>
<p><a href="https://www.volcengine.com/docs/6348/108795" target="_blank">集成 Electron SDK</a></p>
</td>
</tr>
<tr>
<td>
<p>Flutter</p>
</td>
<td>
<p><a href="https://www.volcengine.com/docs/6348/132236" target="_blank">集成 Flutter SDK</a></p>
</td>
</tr>
<tr>
<td>
<p>Unity</p>
</td>
<td>
<p><a href="https://www.volcengine.com/docs/6348/108610" target="_blank">集成 Unity SDK</a></p>
</td>
</tr>
<tr>
<td>
<p>嵌入式设备</p>
</td>
<td>
<p><a href="https://www.volcengine.com/docs/6348/1438400" target="_blank">场景搭建（嵌入式硬件）</a></p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="ed76bd44" tabindex="-1">步骤三：创建房间</h3>
<ol data-style="0">
<li>
<p>调用<a href="/developer_guides/create_room" target="_blank">创建房间</a> API 创建房间。<br>
调用扣子编程提供的<a href="/developer_guides/create_room" target="_blank">创建房间</a>  API，创建一个房间，并将指定的智能体加入房间，然后才能调用 RTC SDK 和智能体开始音视频通话。<br>
创建房间时可以通过 <code>voice_id</code> 参数指定智能体使用的音色，扣子编程提供一系列系统音色，如果没有合适的系统音色，你也可以调用<a href="/developer_guides/clone_voices" target="_blank">复刻音色</a>API，复刻指定音频文件中的人声音色。此外，你还可以设置房间内的音频编码格式，提高音频通话质量。<br>
<strong>创建房间后会返回 appID、roomID、userID 和 Token，调用 RTC SDK 加入房间时需要设置这些信息。</strong></p>
<div class="tabs-tabs-wrapper">
  <div class="tabs-tabs-header">
    <button type="button" class="tabs-tab-button" data-tab="0">请求示例</button>
    <button type="button" class="tabs-tab-button" data-tab="1">响应示例</button>
  </div>
  <div class="tabs-tabs-container">
<div class="tabs-tab-content" data-index="0">

<div style="position: relative">
	<pre><code class="hljs language-Bash">curl --location --request POST <span class="hljs-string">&#x27;https://api.coze.cn/v1/audio/rooms&#x27;</span> \
--header <span class="hljs-string">&#x27;Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****&#x27;</span> \
--header <span class="hljs-string">&#x27;Content-Type: application/json&#x27;</span> \
--data-raw <span class="hljs-string">&#x27;{
    &quot;bot_id&quot;: &quot;734829333445931****&quot;
}&#x27;</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location --request POST &apos;https://api.coze.cn/v1/audio/rooms&apos; \
--header &apos;Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****&apos; \
--header &apos;Content-Type: application/json&apos; \
--data-raw &apos;{
    &quot;bot_id&quot;: &quot;734829333445931****&quot;
}&apos;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p></p>
</div>
<div class="tabs-tab-content" data-index="1">

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;202410291302044CD1CC3B4AE0897***&quot;</span>
    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;room_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;room_id_7431057983427067913&quot;</span><span class="hljs-punctuation">,</span>   <span class="hljs-comment">// 房间 id</span>
        <span class="hljs-attr">&quot;app_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;6705332c79516e01****&quot;</span><span class="hljs-punctuation">,</span>       <span class="hljs-comment">// app_id</span>
        <span class="hljs-attr">&quot;token&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;0016705*****NzkxMxcANTE1MjkFAAAAAAAAAAEAAAAAAAIAAAAAAAMAAAAAAAQAAAAAACAA58QEAvxdy3LHNzSwq6apM9PUKM2rOsxIg/VB4b1xEFA=&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;uid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;uid_7431057983427051529&quot;</span>
    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;detail&quot;: {
        &quot;logid&quot;: &quot;202410291302044CD1CC3B4AE0897***&quot;
    },
    &quot;data&quot;: {
        &quot;room_id&quot;: &quot;room_id_7431057983427067913&quot;,   // 房间 id
        &quot;app_id&quot;: &quot;6705332c79516e01****&quot;,       // app_id
        &quot;token&quot;: &quot;0016705*****NzkxMxcANTE1MjkFAAAAAAAAAAEAAAAAAAIAAAAAAAMAAAAAAAQAAAAAACAA58QEAvxdy3LHNzSwq6apM9PUKM2rOsxIg/VB4b1xEFA=&quot;,
        &quot;uid&quot;: &quot;uid_7431057983427051529&quot;
    },
    &quot;code&quot;: 0,
    &quot;msg&quot;: &quot;&quot;
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p></p>
</div>
  </div>
</div>
</li>
<li>
<p>智能体加入房间。<br>
成功创建房间后，智能体会自动加入房间。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<ul data-style="1">
<li>创建房间后返回的 Token，其默认有效期为 3 分钟，如果 3 分钟内没有用户加入房间，或者用户静音 3 分钟，智能体将自动退出房间，房间随即被释放，后续若要再次和智能体对话，则需重新创建房间。</li>
<li>若有用户进入房间，智能体在房间中最长可以持续 24 小时，直至用户主动退出房间或用户设备异常断电等导致连接断开。</li>
</ul>
</div>
<h3 id="ada24e1e" tabindex="-1">步骤四：用户加入房间</h3>
<p>调用 RTC SDK 的 <code>joinRoom</code> API 加入 RTC 房间，即可在房间中与智能体开展音视频通话。具体实现方式请参见 RTC SDK 集成指南中的实现音视频通话相关内容。</p>
</li>
</ol>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/dev_how_to_guides_realtime_embedded" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">集成音视频 Realtime 嵌入式 SDK</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/dev_how_to_guides_audio_message" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">基于 HTTP 请求实现语音消息</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="前提条件" href="#17b2d2af" data-href="#17b2d2af">前提条件</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="实现流程" href="#4ba630b1" data-href="#4ba630b1">实现流程</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="步骤一：创建智能体并发布为 API 服务" href="#449736f5" data-href="#449736f5">步骤一：创建智能体并发布为 API 服务</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="步骤二：集成 RTC SDK" href="#e388df2e" data-href="#e388df2e">步骤二：集成 RTC SDK</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="步骤三：创建房间" href="#ed76bd44" data-href="#ed76bd44">步骤三：创建房间</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="步骤四：用户加入房间" href="#ada24e1e" data-href="#ada24e1e">步骤四：用户加入房间</a></div></div></div></div></div></div></div></div>
</body></html>