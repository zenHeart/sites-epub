<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">OpenTelemetry 字段映射</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/4760.77ece367d4.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.782417a8ae.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/cozeloop_opentelemetry_field_mapping"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/cozeloop_opentelemetry_field_mapping.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/cozeloop_opentelemetry_field_mapping" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" style="width:300px" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b8b064bdbc784e3cc133a" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/cozeloop_cozeloop-release-notes" data-discover="true"><span class="nodeTitle-ONnqtP" title="新功能发布记录">新功能发布记录</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc1341" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/cozeloop_what-is-cozeloop" data-discover="true"><span class="nodeTitle-ONnqtP" title="什么是扣子罗盘">什么是扣子罗盘</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc134b" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/cozeloop_explore-cozeloop" data-discover="true"><span class="nodeTitle-ONnqtP" title="体验扣子罗盘">体验扣子罗盘</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc1352" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/cozeloop_openclaw_trace_report" data-discover="true"><span class="nodeTitle-ONnqtP" title="把 OpenClaw 的 Trace 上报到扣子罗盘">把 OpenClaw 的 Trace 上报到扣子罗盘</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc1358" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="提示词管理">提示词管理</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b064bdbc784e3cc1360" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="评测">评测</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b064bdbc784e3cc1368" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="观测">观测</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b064bdbc784e3cc139d" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/cozeloop_what-is-trace" data-discover="true"><span class="nodeTitle-ONnqtP" title="什么是观测">什么是观测</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc13a6" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="数据上报">数据上报</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b064bdbc784e3cc152f" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/cozeloop_trace_integrate" data-discover="true"><span class="nodeTitle-ONnqtP" title="数据上报概述">数据上报概述</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc1538" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="OpenTelemetry">OpenTelemetry</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b064bdbc784e3cc1540" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/cozeloop_opentelemetry_trace_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="OpenTelemetry Trace">OpenTelemetry Trace</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc1548" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/cozeloop_opentelemetry_sdk_trace_report" data-discover="true"><span class="nodeTitle-ONnqtP" title="通过 OpenTelemetry SDK 上报 Trace">通过 OpenTelemetry SDK 上报 Trace</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc1552" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:56px" href="/cozeloop_opentelemetry_field_mapping" data-discover="true"><span class="nodeTitle-ONnqtP" title="OpenTelemetry 字段映射">OpenTelemetry 字段映射</span></a></div></div></div><div id="tree-node-6a3b8b064bdbc784e3cc1558" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="AI 框架">AI 框架</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b064bdbc784e3cc1562" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Model Provider">Model Provider</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b064bdbc784e3cc156b" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="网关">网关</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b064bdbc784e3cc1570" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="AI 编码助手">AI 编码助手</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b064bdbc784e3cc158b" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/cozeloop_get_workspace_id_and_token" data-discover="true"><span class="nodeTitle-ONnqtP" title="获取扣子罗盘空间 ID">获取扣子罗盘空间 ID</span></a></div></div></div><div id="tree-node-6a3b8b064bdbc784e3cc13ac" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="查看数据">查看数据</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b064bdbc784e3cc13cd" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/cozeloop_auto-evaluation" data-discover="true"><span class="nodeTitle-ONnqtP" title="Trace 自动评测">Trace 自动评测</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc160b" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/cozeloop_manual_annotation" data-discover="true"><span class="nodeTitle-ONnqtP" title="人工标注 Trace">人工标注 Trace</span></a></div><div id="tree-node-6a3b8b064bdbc784e3cc13bd" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="数据回流">数据回流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div></div></div><div id="tree-node-6a3b8b064bdbc784e3cc1380" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用注册">应用注册</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a7575994bdbc784e3ab711e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="API">API</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b064bdbc784e3cc1390" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="SDK">SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b064bdbc784e3cc13e1" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="实践教程">实践教程</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA" style="width:calc(100% - 300px);--anchor-width:260px"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>扣子罗盘</span><span class="separator-KB9yMa">/</span><span>观测</span><span class="separator-KB9yMa">/</span><span>数据上报</span><span class="separator-KB9yMa">/</span><span>OpenTelemetry</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">OpenTelemetry 字段映射</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">OpenTelemetry 字段映射</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>在使用 OpenTelemetry 向扣子罗盘发送 Trace 数据时，以下属性将映射为扣子罗盘字段。这些映射关系确保了数据的一致性和可读性，同时也遵循了 OpenTelemetry 的语义规范。<br>
OpenTelemetry 协议的语义规范，请参考<a href="https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/" target="_blank">Semantic conventions for generative client AI spans</a>。</p>
<h2 id="7acd4c6b" tabindex="-1">字段优先级</h2>
<p>字段的优先级按照以下原则：</p>
<ul data-style="0">
<li>细粒度优先级高于粗粒度，例如 <code>gen_ai.prompt.{n}.role</code> 优先于 <code>gen_ai.prompt</code>。</li>
<li>事件（Event）的优先级高于属性（Attribute），例如 Message 事件优先级高于 <code>gen_ai.prompt</code> 属性，Choice 事件优先级高于 <code>gen_ai.completion</code> 属性。</li>
</ul>
<h2 id="359f8a66" tabindex="-1">通用字段</h2>
<p>通用字段涵盖了 Span 的标识、时间、基本信息等核心字段。</p>
<h3 id="824b1d91" tabindex="-1">属性（Attribute）</h3>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<ul data-style="0">
<li>不支持用户设置时，对应的字段值将依赖 OpenTelemetry 自动生成。</li>
<li><code>cozeloop.span_type</code> 字段不一定被使用，优先使用具体类型的 Span 节点中的 <code>span_type</code> 属性，如 Model Span 的属性 <code>gen_ai.operation.name</code>。</li>
</ul>
</div>
<!-- @cols-width: 153,174,136,130,100,100,205 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 153px;" /><col style="width: 174px;" /><col style="width: 136px;" /><col style="width: 130px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 205px;" /></colgroup><thead>
<tr>
<th>
<p><strong>OpenTelemetry</strong><br>
<strong>Span 主字段</strong></p>
</th>
<th>
<p><strong>OpenTelemetry</strong><br>
<strong>Span Attributes 子字段</strong></p>
</th>
<th>
<p><strong>字段类型</strong></p>
</th>
<th>
<p><strong>扣子罗盘字段</strong></p>
</th>
<th>
<p><strong>是否必填</strong></p>
</th>
<th>
<p><strong>是否支持设置</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>SpanId</p>
</td>
<td>
<p>-</p>
</td>
<td>
<p>[]byte</p>
</td>
<td>
<p>Span ID</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>Span ID。</p>
</td>
</tr>
<tr>
<td>
<p>TraceId</p>
</td>
<td>
<p>-</p>
</td>
<td>
<p>[]byte</p>
</td>
<td>
<p>Trace ID</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>Trace ID。</p>
</td>
</tr>
<tr>
<td>
<p>ParentSpanId</p>
</td>
<td>
<p>-</p>
</td>
<td>
<p>[]byte</p>
</td>
<td>
<p>Parent Span ID</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>父级 Span ID。</p>
</td>
</tr>
<tr>
<td>
<p>StartTimeUnixNano</p>
</td>
<td>
<p>-</p>
</td>
<td>
<p>int</p>
</td>
<td>
<p>Start Time</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>Span 开始时间，单位：微秒。</p>
</td>
</tr>
<tr>
<td>
<p>StartTimeUnixNano<br>
EndTimeUnixNano</p>
</td>
<td>
<p>-</p>
</td>
<td>
<p>int<br>
int</p>
</td>
<td>
<p>Duration</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>Span 持续时间，单位：微秒。</p>
</td>
</tr>
<tr>
<td>
<p>Name</p>
</td>
<td>
<p>-</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Span Name</p>
</td>
<td>
<p><s>是</s></p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>Span 节点名称。</p>
</td>
</tr>
<tr>
<td>
<p>Attributes</p>
</td>
<td>
<p>cozeloop.workspace_id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>WorkSpace ID</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>扣子罗盘工作空间 ID，用于鉴权。<br>
只有在同一个服务需要上报多个空间的 Trace 时，才需要填写，优先级高于 Header 中的<code>cozeloop-workspace-id</code>。</p>
</td>
</tr>
<tr>
<td>
<p>Attributes</p>
</td>
<td>
<p>cozeloop.span_type</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Span Type</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>Span 节点类型，可选值：</p>
<ul data-style="0">
<li>model：大模型节点</li>
<li>prompt：Prompt节点</li>
<li>retriever：RAG 召回节点</li>
<li>tool：Tool Call 节点</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>Attributes</p>
</td>
<td>
<p>cozeloop.input</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>输入内容，可以为任意内容。</p>
</td>
</tr>
<tr>
<td>
<p>Attributes</p>
</td>
<td>
<p>cozeloop.output</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>输出内容，可以为任意内容。</p>
</td>
</tr>
<tr>
<td>
<p>Attributes</p>
</td>
<td>
<p>session.id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.thread_id</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>会话（会话、线程）的唯一标识符，用于存储和关联此会话中的消息。</p>
</td>
</tr>
<tr>
<td>
<p>Attributes</p>
</td>
<td>
<p>user.id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.user_id</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>用户 ID。</p>
</td>
</tr>
<tr>
<td>
<p>Attributes</p>
</td>
<td>
<p>messaging.message.id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.message_id</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>消息 ID。</p>
</td>
</tr>
<tr>
<td>
<p>Attributes</p>
</td>
<td>
<p>error.type</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.error</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>错误信息。<br>
未设置 <code>status_code</code> 时，将默认为 -1。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="d485b76d" tabindex="-1">事件（Event）</h3>
<p>Event 用于记录在 Span 执行过程中发生的特定事件，例如异常或用户交互。</p>
<h4 id="8421c158" tabindex="-1">Exception 事件</h4>
<p>Exception（异常）事件的字段映射如下：</p>
<!-- @cols-width: 164,126,319,244 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 164px;" /><col style="width: 126px;" /><col style="width: 319px;" /><col style="width: 244px;" /></colgroup><thead>
<tr>
<th>
<p><strong>event Attributes 字段</strong></p>
</th>
<th>
<p><strong>字段类型</strong></p>
</th>
<th>
<p><strong>罗盘字段</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>exception.message</p>
</td>
<td>
<p>string</p>
</td>
<td>
<ul data-style="0">
<li>status_code<br>
未设置 <code>status_code</code> 时，将默认为 -1。</li>
<li>error message</li>
</ul>
</td>
<td>
<p>error 获取优先级：<br>
exception 事件的优先级高于 <code>error.message</code>。</p>
</td>
</tr>
<tr>
<td>
<p>exception.stacktrace</p>
</td>
<td>
<p>string</p>
</td>
<td>
<ul data-style="0">
<li>status_code<br>
未设置 <code>status_code</code> 时，将默认为 -1。</li>
<li>error message<br>
补充添加到error message之后</li>
</ul>
</td>
<td>
<p>error 获取优先级：<br>
exception 事件的优先级高于 <code>error.message</code>。</p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="a048c53c" tabindex="-1">Model 节点</h2>
<p>Model 节点用于记录与 AI 模型调用相关的详细信息，包括输入、输出和调用参数。</p>
<h3 id="30583d69" tabindex="-1">属性（Attribute）</h3>
<h4 id="ded14089" tabindex="-1">标准字段</h4>
<!-- @cols-width: 235,102,209,317 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 235px;" /><col style="width: 102px;" /><col style="width: 209px;" /><col style="width: 317px;" /></colgroup><thead>
<tr>
<th>
<p><strong>OpenTelemetry attribute字段</strong></p>
</th>
<th>
<p><strong>字段类型</strong></p>
</th>
<th>
<p><strong>扣子罗盘字段</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>gen_ai.system</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.model_provider</p>
</td>
<td>
<p>模型提供方，例如 openai、anthropic。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.operation.name<br>
gen_ai.request.type（traceLoop使用该字段）</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>span_type</p>
</td>
<td>
<p>Span 节点类型。映射转换关系：</p>
<ul data-style="0">
<li>chat：转换为 model</li>
<li>create_agent：不转换</li>
<li>embeddings：不转换</li>
<li>execute_tool：转换为 tool</li>
<li>generate_content：转换为 model</li>
<li>invoke_agent：不转换</li>
<li>text_completion：转换为 model</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>gen_ai.prompt</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input</p>
</td>
<td>
<p>大模型输入，优先级比 Event 低。<br>
(opentelemetry 已废弃，不推荐使用)</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.completion</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output</p>
</td>
<td>
<p>大模型输出，优先级比 Event 低。<br>
(opentelemetry 已废弃，不推荐使用)</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.prompt.{n}.role</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].role</p>
</td>
<td>
<p>输入消息的Role，优先级比 event 低。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.prompt.{n}.content</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].content</p>
</td>
<td>
<p>输入消息的内容，优先级比 event 低。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.completion.{n}.role</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output.messages[n].role</p>
</td>
<td>
<p>输出消息的 Role，优先级比 event 低。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.completion.{n}.content</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output.messages[n].content</p>
</td>
<td>
<p>输出消息的内容，优先级比 event 低。</p>
</td>
</tr>
<tr>
<td>
<p>cozeloop.time_to_first_token</p>
</td>
<td>
<p>int</p>
</td>
<td>
<p>Tags.latency_first_resp</p>
</td>
<td>
<p>流式调用模型时，首包返回的时间戳, 单位：微秒。会自动计算出从 Span 开始到首包返回的耗时。</p>
</td>
</tr>
<tr>
<td>
<p>cozeloop.stream</p>
</td>
<td>
<p>boolean</p>
</td>
<td>
<p>Tags.stream</p>
</td>
<td>
<p>是否流式输出。</p>
</td>
</tr>
</tbody>
</table>
</div><h4 id="c16900d1" tabindex="-1">Request 参数</h4>
<p>Request 参数用于记录调用 AI 模型时的请求参数，例如模型名称、token 数量等。</p>
<!-- @cols-width: 219,111,222,304 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 219px;" /><col style="width: 111px;" /><col style="width: 222px;" /><col style="width: 304px;" /></colgroup><thead>
<tr>
<th>
<p><strong>OpenTelemetry 字段</strong></p>
</th>
<th>
<p><strong>字段类型</strong></p>
</th>
<th>
<p><strong>扣子罗盘字段</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>gen_ai.request.model</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.model_name</p>
</td>
<td>
<p>模型名字，不区分 request 和 response。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.response.model</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.model_name</p>
</td>
<td>
<p>模型名字，不区分 request 和 response。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.request.temperature</p>
</td>
<td>
<p>double</p>
</td>
<td>
<p>Tags.call_options.temperature</p>
</td>
<td>
<p>Temperature 配置。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.request.top_p</p>
</td>
<td>
<p>double</p>
</td>
<td>
<p>Tags.call_options.top_p</p>
</td>
<td>
<p>top_p 采样配置。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.request.top_k</p>
</td>
<td>
<p>double</p>
</td>
<td>
<p>Tags.call_options.top_k</p>
</td>
<td>
<p>top_k 采样配置。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.request.max_tokens</p>
</td>
<td>
<p>int</p>
</td>
<td>
<p>Tags.call_options.max_tokens</p>
</td>
<td>
<p>控制生成文本的最大 tokens。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.request.frequency_penalty</p>
</td>
<td>
<p>double</p>
</td>
<td>
<p>Tags.call_options.frequency_penalty</p>
</td>
<td>
<p>Frequency penalty 配置。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.request.presence_penalty</p>
</td>
<td>
<p>double</p>
</td>
<td>
<p>Tags.call_options.presence_penalty</p>
</td>
<td>
<p>Presence penalty 配置。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.request.stop_sequences</p>
</td>
<td>
<p>string[]</p>
</td>
<td>
<p>Tags.call_options.stop</p>
</td>
<td>
<p>指定生成文本时的停止序列。</p>
</td>
</tr>
</tbody>
</table>
</div><h4 id="62065609" tabindex="-1">Usage参数</h4>
<p>Usage 参数用于记录 AI 模型调用的使用情况，例如输入和输出的令牌数。</p>
<!-- @cols-width: 218,112,221,310 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 218px;" /><col style="width: 112px;" /><col style="width: 221px;" /><col style="width: 310px;" /></colgroup><thead>
<tr>
<th>
<p><strong>OpenTelemetry Attribute</strong></p>
</th>
<th>
<p><strong>字段类型</strong></p>
</th>
<th>
<p><strong>扣子罗盘字段</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>gen_ai.usage.input_tokens</p>
</td>
<td>
<p>int</p>
</td>
<td>
<p>Tags.input_tokens</p>
</td>
<td>
<p>输入的 tokens，会和 output tokens 取和自动计算出 tokens。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.usage.output_tokens</p>
</td>
<td>
<p>int</p>
</td>
<td>
<p>Tags.output_tokens</p>
</td>
<td>
<p>输出的 tokens，会和 input tokens 取和自动计算出 tokens。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.usage.prompt_tokens</p>
</td>
<td>
<p>int</p>
</td>
<td>
<p>Tags.input_tokens</p>
</td>
<td>
<p>Opentelemetry 已废弃，不推荐使用。</p>
</td>
</tr>
<tr>
<td>
<p>gen_ai.usage.completion_tokens</p>
</td>
<td>
<p>int</p>
</td>
<td>
<p>Tags.output_tokens</p>
</td>
<td>
<p>Opentelemetry 已废弃，不推荐使用。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="147b4ba1" tabindex="-1">事件（Event）</h3>
<p>OpenTelemetry Model 节点相关的 Event 说明，请参考 <a href="https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/#event-gen_aiassistantmessage" target="_blank">Event</a>。</p>
<h4 id="f59c3558" tabindex="-1">Message 事件</h4>
<p>罗列了消息相关的事件字段，事件名称为 gen_ai.system.message、gen_ai.user.message、gen_ai.assistant.message、gen_ai.tool.message。</p>
<!-- @cols-width: 203,231,142,245 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 203px;" /><col style="width: 231px;" /><col style="width: 142px;" /><col style="width: 245px;" /></colgroup><thead>
<tr>
<th>
<p><strong>事件名称</strong></p>
</th>
<th>
<p><strong>Event Attributes 字段</strong></p>
</th>
<th>
<p><strong>字段类型</strong></p>
</th>
<th>
<p><strong>扣子罗盘字段</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">
<p>gen_ai.system.message<br>
gen_ai.user.message</p>
</td>
<td>
<p>content</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].content</p>
</td>
</tr>
<tr>
<td>
<p>role</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].role</p>
</td>
</tr>
<tr>
<td rowspan="8">
<p>gen_ai.assistant.message</p>
</td>
<td>
<p>content</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].content</p>
</td>
</tr>
<tr>
<td>
<p>role</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].role</p>
</td>
</tr>
<tr>
<td>
<p>tool_calls</p>
</td>
<td>
<p>map[]</p>
</td>
<td>
<p>Input.messages[n].tool_calls</p>
</td>
</tr>
<tr>
<td>
<p>tool_calls.{n}.id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].tool_calls.id</p>
</td>
</tr>
<tr>
<td>
<p>tool_calls.{n}.type</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].tool_calls.type</p>
</td>
</tr>
<tr>
<td>
<p>tool_calls.{n}.function</p>
</td>
<td>
<p>map</p>
</td>
<td>
<p>Input.messages[n].tool_calls.function</p>
</td>
</tr>
<tr>
<td>
<p>tool_calls.{n}.function.name</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].tool_calls.function.name</p>
</td>
</tr>
<tr>
<td>
<p>tool_calls.{n}.function.arguments</p>
</td>
<td>
<p>undefined</p>
</td>
<td>
<p>Input.messages[n].tool_calls.function.arguments</p>
</td>
</tr>
<tr>
<td rowspan="3">
<p>gen_ai.tool.message</p>
</td>
<td>
<p>content</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].content</p>
</td>
</tr>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].name</p>
</td>
</tr>
<tr>
<td>
<p>role</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Input.messages[n].role</p>
</td>
</tr>
</tbody>
</table>
</div><h4 id="4f1cf9f6" tabindex="-1">Choice 事件</h4>
<p>罗列了决策相关的事件字段，事件名称为 gen_ai.choice。</p>
<!-- @cols-width: 132,328,100,440 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 132px;" /><col style="width: 328px;" /><col style="width: 100px;" /><col style="width: 440px;" /></colgroup><thead>
<tr>
<th>
<p><strong>事件名称</strong></p>
</th>
<th>
<p><strong>Event 字段</strong></p>
</th>
<th>
<p><strong>字段类型</strong></p>
</th>
<th>
<p><strong>扣子罗盘字段</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="11">
<p>gen_ai.choice</p>
</td>
<td>
<p>finish_reason</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output.choices[0].finish_reason</p>
</td>
</tr>
<tr>
<td>
<p>index</p>
</td>
<td>
<p>int</p>
</td>
<td>
<p>Output.choices[0].index</p>
</td>
</tr>
<tr>
<td>
<p>message</p>
</td>
<td>
<p>map</p>
</td>
<td>
<p>Output.choices[0].message</p>
</td>
</tr>
<tr>
<td>
<p>message.content</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output.choices[0].message.content</p>
</td>
</tr>
<tr>
<td>
<p>message.role</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output.choices[0].message.role</p>
</td>
</tr>
<tr>
<td>
<p>message.tool_calls</p>
</td>
<td>
<p>map[]</p>
</td>
<td>
<p>Output.choices[0].message.tool_calls</p>
</td>
</tr>
<tr>
<td>
<p>message.tool_calls.{n}.id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output.choices[0].message.tool_calls.id</p>
</td>
</tr>
<tr>
<td>
<p>message.tool_calls.{n}.type</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output.choices[0].message.tool_calls.type</p>
</td>
</tr>
<tr>
<td>
<p>message.tool_calls.{n}.function</p>
</td>
<td>
<p>map</p>
</td>
<td>
<p>Output.choices[0].message.tool_calls.function</p>
</td>
</tr>
<tr>
<td>
<p>message.tool_calls.{n}.function.name</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Output.choices[0].message.tool_calls.function.name</p>
</td>
</tr>
<tr>
<td>
<p>message.tool_calls.{n}.function.arguments</p>
</td>
<td>
<p>undefined</p>
</td>
<td>
<p>Output.choices[0].message.tool_calls.function.arguments</p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="7a217e95" tabindex="-1">Prompt节点</h2>
<p>Prompt 节点用于记录与 AI 模型调用相关的提示信息，包括唯一标识符、版本和提供方信息。Attribute 的标准字段如下：</p>
<!-- @cols-width: 250,123,194,292 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 250px;" /><col style="width: 123px;" /><col style="width: 194px;" /><col style="width: 292px;" /></colgroup><thead>
<tr>
<th>
<p><strong>OpenTelemetry attribute</strong></p>
</th>
<th>
<p><strong>字段类型</strong></p>
</th>
<th>
<p><strong>扣子罗盘字段</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>cozeloop.prompt_key</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.prompt_key</p>
</td>
<td>
<p>Prompt key。</p>
</td>
</tr>
<tr>
<td>
<p>cozeloop.prompt_version</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.prompt_version</p>
</td>
<td>
<p>Prompt 版本。</p>
</td>
</tr>
<tr>
<td>
<p>cozeloop.prompt_provider</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>Tags.prompt_provider</p>
</td>
<td>
<p>Prompt 提供方。</p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="730a0d17" tabindex="-1">其他字段</h2>
<ul data-style="0">
<li>其他未提及的用户自定义属性字段，默认存放在 <code>Tags</code> 字段，前端页面展示在 <code>Metadata</code> 中。</li>
<li>其他未提及的事件，不保留，直接丢弃。</li>
</ul>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/cozeloop_opentelemetry_sdk_trace_report" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">通过 OpenTelemetry SDK 上报 Trace</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/cozeloop_ccepfu6a" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">AutoGen</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="字段优先级" href="#7acd4c6b" data-href="#7acd4c6b">字段优先级</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="通用字段" href="#359f8a66" data-href="#359f8a66">通用字段</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="属性（Attribute）" href="#824b1d91" data-href="#824b1d91">属性（Attribute）</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="事件（Event）" href="#d485b76d" data-href="#d485b76d">事件（Event）</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="Exception 事件" href="#8421c158" data-href="#8421c158">Exception 事件</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="Model 节点" href="#a048c53c" data-href="#a048c53c">Model 节点</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="属性（Attribute）" href="#30583d69" data-href="#30583d69">属性（Attribute）</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="标准字段" href="#ded14089" data-href="#ded14089">标准字段</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="Request 参数" href="#c16900d1" data-href="#c16900d1">Request 参数</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="Usage参数" href="#62065609" data-href="#62065609">Usage参数</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="事件（Event）" href="#147b4ba1" data-href="#147b4ba1">事件（Event）</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="Message 事件" href="#f59c3558" data-href="#f59c3558">Message 事件</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="Choice 事件" href="#4f1cf9f6" data-href="#4f1cf9f6">Choice 事件</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="Prompt节点" href="#7a217e95" data-href="#7a217e95">Prompt节点</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="其他字段" href="#730a0d17" data-href="#730a0d17">其他字段</a></div></div></div></div></div></div></div></div>
</body></html>