<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">通过 API 运行应用工作流</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/4760.77ece367d4.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.782417a8ae.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/guides_run_app_as_api"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/guides_run_app_as_api.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/guides_run_app_as_api" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" style="width:300px" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b97434bdbc784e3ce84ce" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a55df9a4bdbc784e3c9738f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf30d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf317" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf31d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf325" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf334" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf32e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8aea4bdbc784e3cbfae6" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/guides_publish_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="了解项目发布">了解项目发布</span></a></div><div id="tree-node-6a3b8ae94bdbc784e3cbf516" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="发布智能体">发布智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8aea4bdbc784e3cbfaed" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="发布应用">发布应用</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8aea4bdbc784e3cbfb23" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_api" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布为 API 服务">发布为 API 服务</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb29" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:40px" href="/guides_run_app_as_api" data-discover="true"><span class="nodeTitle-ONnqtP" title="通过 API 运行应用工作流">通过 API 运行应用工作流</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb31" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_app_to_web_sdk" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布为 Chat SDK">发布为 Chat SDK</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb39" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_app_to_douyin_microapp" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布到抖音小程序">发布到抖音小程序</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb40" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_app_to_wechat_mini_program" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布到微信小程序">发布到微信小程序</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb49" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_app_to_lark" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布到飞书">发布到飞书</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb51" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_app_to_wechat_customerService" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布到微信客服">发布到微信客服</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb57" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_app_to_wechat_serviceAccount" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布到微信服务号">发布到微信服务号</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb5e" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_app_to_wechat_subscriptionAccount" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布到微信订阅号">发布到微信订阅号</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb67" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_to_store" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布到商店">发布到商店</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb6f" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_app_enterprise_store" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布到企业商店">发布到企业商店</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb75" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_to_template" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布为模板">发布为模板</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbff2d" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_publish_to_space" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布为 MCP 工具">发布为 MCP 工具</span></a></div><div id="tree-node-6a3b8aeb4bdbc784e3cbffb6" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/guides_app_publish_ui_builder" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布为 Web SDK">发布为 Web SDK</span></a></div></div></div><div id="tree-node-6a3b8aea4bdbc784e3cbfaf6" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="发布到公共渠道">发布到公共渠道</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8aea4bdbc784e3cbfafb" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="发布管理">发布管理</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae94bdbc784e3cbf947" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="数据分析">数据分析</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc530b" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="渠道入驻">渠道入驻</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8aea4bdbc784e3cbfb04" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/guides_manage_published_project" data-discover="true"><span class="nodeTitle-ONnqtP" title="管理发布产物">管理发布产物</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfea0" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/guides_manage_channels" data-discover="true"><span class="nodeTitle-ONnqtP" title="管理发布渠道">管理发布渠道</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbfed3" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/guides_channels_differences" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布渠道能力差异">发布渠道能力差异</span></a></div><div id="tree-node-6a3b8aea4bdbc784e3cbff72" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/guides_publish_faq" data-discover="true"><span class="nodeTitle-ONnqtP" title="发布常见问题">发布常见问题</span></a></div></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf35a" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf362" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8e614bdbc784e3cce185" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf33f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf369" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/guides_FAQ" data-discover="true"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA" style="width:calc(100% - 300px);--anchor-width:260px"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>发布</span><span class="separator-KB9yMa">/</span><span>发布应用</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">通过 API 运行应用工作流</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">通过 API 运行应用工作流</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>业务逻辑的本质是工作流的编排，它是 AI 应用执行任务时所遵循的规则和步骤。将应用发布为 API 服务之后，你可以调用工作流相关的 OpenAPI，将应用集成到你的业务系统中。</p>
<div class="topic-callout notice"><p class="topic-callout-title">注意</p>
<ul data-style="0">
<li>首次使用 OpenAPI 的用户，建议先阅读<a href="/developer_guides/coze_api_overview" target="_blank">API 介绍</a>，了解使用 OpenAPI 的方式和使用限制。</li>
<li>调用工作流 API 时，响应信息中会返回 debug_url，通过浏览器访问此链接，即可通过可视化界面查看工作流的试运行过程，其中包含每个执行节点的输入输出等详细信息，帮助你在线调试或排障。如果 debug_url 中包括字符 <code>\u0026</code>，需要手动替换为 <code>&amp;</code>，之后再访问此链接。</li>
</ul>
</div>
<h3 id="eefbaf53" tabindex="-1">同步运行</h3>
<p>工作流默认同步运行。你可以选择流式响应或非流式响应的方式运行应用中的指定工作流，运行工作流时需要通过请求参数 app_id 指定应用的 ID，以便工作流节点使用应用资源库的数据和知识。</p>
<h4 id="232e8e11" tabindex="-1">非流式响应</h4>
<p><a href="/developer_guides/workflow_run" target="_blank">执行工作流</a>接口采用非流式响应模式，执行结果会直接封装在响应信息中返回给开发者，适用于不包含流式响应节点的工作流。<br>
请求示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-Bash">curl --location --request POST <span class="hljs-string">&#x27;https://api.coze.cn/v1/workflow/run&#x27;</span> \
  --header <span class="hljs-string">&#x27;Authorization: Bearer pat_hfwkehfncaf****&#x27;</span> \
  --header <span class="hljs-string">&#x27;Content-Type: application/json&#x27;</span> \
  --data-raw <span class="hljs-string">&#x27;{
    &quot;workflow_id&quot;: &quot;73664689170551*****&quot;,
    &quot;parameters&quot;: {
      &quot;user_id&quot;: &quot;12345&quot;,
      &quot;user_name&quot;: &quot;George&quot;
    },
    &quot;app_id&quot;: &quot;743962661420117****&quot;
}&#x27;</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location --request POST &apos;https://api.coze.cn/v1/workflow/run&apos; \
  --header &apos;Authorization: Bearer pat_hfwkehfncaf****&apos; \
  --header &apos;Content-Type: application/json&apos; \
  --data-raw &apos;{
    &quot;workflow_id&quot;: &quot;73664689170551*****&quot;,
    &quot;parameters&quot;: {
      &quot;user_id&quot;: &quot;12345&quot;,
      &quot;user_name&quot;: &quot;George&quot;
    },
    &quot;app_id&quot;: &quot;743962661420117****&quot;
}&apos;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p>你可以从响应信息查看工作流的执行结果，包含运行状态、结束节点的输出等信息。响应示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span> 
    <span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span> 
    <span class="hljs-attr">&quot;cost&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span> 
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;{\&quot;output\&quot;:\&quot;北京的经度为116.4074°E，纬度为39.9042°N。\&quot;}&quot;</span><span class="hljs-punctuation">,</span> 
    <span class="hljs-attr">&quot;debug_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;https://www.coze.cn/work_flow?execute_id=741364789030728****&amp;space_id=736142423532160****&amp;workflow_id=738958910358870****&quot;</span><span class="hljs-punctuation">,</span> 
    <span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;Success&quot;</span><span class="hljs-punctuation">,</span> 
    <span class="hljs-attr">&quot;token&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">98</span> 
<span class="hljs-punctuation">}</span> 
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{ 
    &quot;code&quot;: 0, 
    &quot;cost&quot;: &quot;0&quot;, 
    &quot;data&quot;: &quot;{\&quot;output\&quot;:\&quot;北京的经度为116.4074°E，纬度为39.9042°N。\&quot;}&quot;, 
    &quot;debug_url&quot;: &quot;https://www.coze.cn/work_flow?execute_id=741364789030728****&space_id=736142423532160****&workflow_id=738958910358870****&quot;, 
    &quot;msg&quot;: &quot;Success&quot;, 
    &quot;token&quot;: 98 
} " style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h4 id="272e3b21" tabindex="-1">流式响应</h4>
<p><a href="/developer_guides/workflow_stream_run" target="_blank">执行工作流（流式响应）</a>接口采用流式响应模式，在后端处理的同时发送响应信息，呈现类似打字机的效果。调用此 API 时需要使用流式响应方式接收响应数据，适用于以下场景：</p>
<ul data-style="0">
<li>包含开启了流式响应节点的工作流。输出节点、结束节点支持流式响应，包含这两个节点的工作流建议使用此 API。</li>
<li>包含问答节点的工作流。</li>
</ul>
<p>请求示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-Bash">curl --location --request POST <span class="hljs-string">&#x27;https://api.coze.cn/v1/workflow/stream_run&#x27;</span> \ 
--header <span class="hljs-string">&#x27;Authorization: Bearer pat_fhwefweuk****&#x27;</span> \ 
--header <span class="hljs-string">&#x27;Content-Type: application/json&#x27;</span> \ 
--data-raw <span class="hljs-string">&#x27;{
    &quot;workflow_id&quot;: &quot;73664689170551*****&quot;, 
    &quot;parameters&quot;: { 
        &quot;user_id&quot;:&quot;12345&quot;, 
        &quot;user_name&quot;:&quot;George&quot;
    },
    &quot;app_id&quot;:&quot;743962661420117****&quot; 
}
</span></code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location --request POST &apos;https://api.coze.cn/v1/workflow/stream_run&apos; \ 
--header &apos;Authorization: Bearer pat_fhwefweuk****&apos; \ 
--header &apos;Content-Type: application/json&apos; \ 
--data-raw &apos;{
    &quot;workflow_id&quot;: &quot;73664689170551*****&quot;, 
    &quot;parameters&quot;: { 
        &quot;user_id&quot;:&quot;12345&quot;, 
        &quot;user_name&quot;:&quot;George&quot;
    },
    &quot;app_id&quot;:&quot;743962661420117****&quot; 
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p>你可以从响应信息的 event 和 data 字段查看工作流的各个执行事件。你需要持续接收 Message 事件，直到观察到 Error、Done 或 Interrupt 事件。其中：</p>
<ul data-style="0">
<li>Message：工作流节点输出消息，例如输出节点、结束节点的输出消息。可以在 data 中查看具体的消息内容。</li>
<li>Error：报错。观察到此事件时，需要在 data 中查看 error_code 和 error_message，排查问题。</li>
<li>Interrupt：中断。观察到此事件时，表示工作流中断，此时 data 字段中包含具体的中断信息。</li>
<li>Done：结束。表示工作流执行结束，此时 data 中返回 debug_url。</li>
</ul>
<p>响应示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON">id<span class="hljs-punctuation">:</span> <span class="hljs-number">0</span> 
event<span class="hljs-punctuation">:</span> Message 
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;msg&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_is_finish&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-literal"><span class="hljs-keyword">false</span></span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_seq_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_title&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;Message&quot;</span><span class="hljs-punctuation">}</span> 
 
id<span class="hljs-punctuation">:</span> <span class="hljs-number">1</span> 
event<span class="hljs-punctuation">:</span> Message 
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;为&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_is_finish&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-literal"><span class="hljs-keyword">false</span></span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_seq_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;1&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_title&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;Message&quot;</span><span class="hljs-punctuation">}</span> 
 
id<span class="hljs-punctuation">:</span> <span class="hljs-number">2</span> 
event<span class="hljs-punctuation">:</span> Message 
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;什么小明要带一把尺子去看电影？\n因&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_is_finish&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-literal"><span class="hljs-keyword">false</span></span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_seq_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;2&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_title&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;Message&quot;</span><span class="hljs-punctuation">}</span> 
 
id<span class="hljs-punctuation">:</span> <span class="hljs-number">3</span> 
event<span class="hljs-punctuation">:</span> Message 
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;为他听说电影很长，怕&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_is_finish&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-literal"><span class="hljs-keyword">false</span></span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_seq_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;3&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_title&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;Message&quot;</span><span class="hljs-punctuation">}</span> 
 
id<span class="hljs-punctuation">:</span> <span class="hljs-number">4</span> 
event<span class="hljs-punctuation">:</span> Message 
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;坐不下！&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_is_finish&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-literal"><span class="hljs-keyword">true</span></span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_seq_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;4&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_title&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;Message&quot;</span><span class="hljs-punctuation">}</span> 
 
id<span class="hljs-punctuation">:</span> <span class="hljs-number">5</span> 
event<span class="hljs-punctuation">:</span> Message 
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;{\&quot;output\&quot;:\&quot;为什么小明要带一把尺子去看电影？\\n因为他听说电影很长，怕坐不下！\&quot;}&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;cost&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;0.00&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_is_finish&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-literal"><span class="hljs-keyword">true</span></span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_seq_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_title&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;token&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">}</span> 
 
id<span class="hljs-punctuation">:</span> <span class="hljs-number">6</span> 
event<span class="hljs-punctuation">:</span> Done 
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;debug_url&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;https://www.coze.cn/work_flow?execute_id=744119270952162****&amp;space_id=743984899418202****\&amp;workflow_id=743985075059477****&quot;</span><span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="id: 0 
event: Message 
data: {&quot;content&quot;:&quot;msg&quot;,&quot;node_is_finish&quot;:false,&quot;node_seq_id&quot;:&quot;0&quot;,&quot;node_title&quot;:&quot;Message&quot;} 
 
id: 1 
event: Message 
data: {&quot;content&quot;:&quot;为&quot;,&quot;node_is_finish&quot;:false,&quot;node_seq_id&quot;:&quot;1&quot;,&quot;node_title&quot;:&quot;Message&quot;} 
 
id: 2 
event: Message 
data: {&quot;content&quot;:&quot;什么小明要带一把尺子去看电影？\n因&quot;,&quot;node_is_finish&quot;:false,&quot;node_seq_id&quot;:&quot;2&quot;,&quot;node_title&quot;:&quot;Message&quot;} 
 
id: 3 
event: Message 
data: {&quot;content&quot;:&quot;为他听说电影很长，怕&quot;,&quot;node_is_finish&quot;:false,&quot;node_seq_id&quot;:&quot;3&quot;,&quot;node_title&quot;:&quot;Message&quot;} 
 
id: 4 
event: Message 
data: {&quot;content&quot;:&quot;坐不下！&quot;,&quot;node_is_finish&quot;:true,&quot;node_seq_id&quot;:&quot;4&quot;,&quot;node_title&quot;:&quot;Message&quot;} 
 
id: 5 
event: Message 
data: {&quot;content&quot;:&quot;{\&quot;output\&quot;:\&quot;为什么小明要带一把尺子去看电影？\\n因为他听说电影很长，怕坐不下！\&quot;}&quot;,&quot;cost&quot;:&quot;0.00&quot;,&quot;node_is_finish&quot;:true,&quot;node_seq_id&quot;:&quot;0&quot;,&quot;node_title&quot;:&quot;&quot;,&quot;token&quot;:0} 
 
id: 6 
event: Done 
data: {&quot;debug_url&quot;:&quot;https://www.coze.cn/work_flow?execute_id=744119270952162****&space_id=743984899418202****\&workflow_id=743985075059477****&quot;}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h4 id="6054d52e" tabindex="-1">中断场景</h4>
<p>包含问答节点和输入节点的工作流，需要使用<a href="/developer_guides/workflow_stream_run" target="_blank">执行工作流（流式响应）</a>接口来调用应用，并在工作流中断时，调用<a href="/developer_guides/workflow_resume" target="_blank">恢复运行工作流（流式响应）</a>回答问题或提交输入信息，并恢复运行工作流。对于问答节点，如果用户的响应和智能体预期提取的信息不匹配，例如缺少必选的字段，或字段数据类型不一致，工作流会再次中断并追问。如果询问 3 次仍未收到符合预期的回复，则判定为工作流执行失败。<br>
以查看天气工作为例，完整的接口调用示例如下。</p>
<ol data-style="0">
<li>
<p>调用接口<a href="/developer_guides/workflow_stream_run" target="_blank">执行工作流（流式响应）</a>，要求查看天气。<br>
请求示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">curl --location &#x27;https://api.coze.cn/v1/workflow/stream_run&#x27; \
--header &#x27;Authorization: Bearer pat_vTG1****&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data &#x27;{
    &quot;workflow_id&quot;: &quot;739739507914235****&quot;,
    &quot;parameters&quot;: {
        &quot;BOT_USER_INPUT&quot;:&quot;查看天气&quot;
    },
    &quot;app_id&quot;:&quot;743962661420117****&quot; 
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location &apos;https://api.coze.cn/v1/workflow/stream_run&apos; \
--header &apos;Authorization: Bearer pat_vTG1****&apos; \
--header &apos;Content-Type: application/json&apos; \
--data &apos;{
    &quot;workflow_id&quot;: &quot;739739507914235****&quot;,
    &quot;parameters&quot;: {
        &quot;BOT_USER_INPUT&quot;:&quot;查看天气&quot;
    },
    &quot;app_id&quot;:&quot;743962661420117****&quot; 
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>触发问答节点，工作流中断，响应信息中返回智能体提出的问题，要求用户提供城市和日期。<br>
返回示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON">id<span class="hljs-punctuation">:</span> <span class="hljs-number">0</span>
event<span class="hljs-punctuation">:</span> Message
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;请问你想查看哪个城市、哪一天的天气呢&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_is_finish&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-literal"><span class="hljs-keyword">true</span></span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_seq_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_title&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;问答&quot;</span><span class="hljs-punctuation">}</span>

id<span class="hljs-punctuation">:</span> <span class="hljs-number">1</span>
event<span class="hljs-punctuation">:</span> Interrupt
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;interrupt_data&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;event_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7404831988202520614/6302059919516746633&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">2</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_title&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;问答&quot;</span><span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="id: 0
event: Message
data: {&quot;content&quot;:&quot;请问你想查看哪个城市、哪一天的天气呢&quot;,&quot;content_type&quot;:&quot;text&quot;,&quot;node_is_finish&quot;:true,&quot;node_seq_id&quot;:&quot;0&quot;,&quot;node_title&quot;:&quot;问答&quot;}

id: 1
event: Interrupt
data: {&quot;interrupt_data&quot;:{&quot;data&quot;:&quot;&quot;,&quot;event_id&quot;:&quot;7404831988202520614/6302059919516746633&quot;,&quot;type&quot;:2},&quot;node_title&quot;:&quot;问答&quot;}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>调用接口<a href="/developer_guides/workflow_resume" target="_blank">恢复运行工作流（流式响应）</a>，回复智能体城市和日期。<br>
请求示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-Plain">curl --location &#x27;https://api.coze.cn/v1/workflow/stream_resume&#x27; \
--header &#x27;Authorization: Bearer pat_vTG1****&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data &#x27;{
    &quot;event_id&quot;:&quot;740483727529459****/433802199567434****&quot;,
    &quot;interrupt_type&quot;:2,
    &quot;resume_data&quot;:&quot;杭州，2024-08-20&quot;,
    &quot;workflow_id&quot;:&quot;739739507914235****&quot;
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location &apos;https://api.coze.cn/v1/workflow/stream_resume&apos; \
--header &apos;Authorization: Bearer pat_vTG1****&apos; \
--header &apos;Content-Type: application/json&apos; \
--data &apos;{
    &quot;event_id&quot;:&quot;740483727529459****/433802199567434****&quot;,
    &quot;interrupt_type&quot;:2,
    &quot;resume_data&quot;:&quot;杭州，2024-08-20&quot;,
    &quot;workflow_id&quot;:&quot;739739507914235****&quot;
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>工作流执行完毕，完成天气查询，返回工作流输出消息。<br>
返回示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON">id<span class="hljs-punctuation">:</span> <span class="hljs-number">0</span> 
event<span class="hljs-punctuation">:</span> Message 
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;{\&quot;output\&quot;:[{\&quot;condition\&quot;:\&quot;中到大雨\&quot;,\&quot;humidity\&quot;:72,\&quot;predict_date\&quot;:\&quot;2024-08-20\&quot;,\&quot;temp_high\&quot;:35,\&quot;temp_low\&quot;:26,\&quot;weather_day\&quot;:\&quot;中到大雨\&quot;,\&quot;wind_dir_day\&quot;:\&quot;西风\&quot;,\&quot;wind_dir_night\&quot;:\&quot;西风\&quot;,\&quot;wind_level_day\&quot;:\&quot;3\&quot;,\&quot;wind_level_night\&quot;:\&quot;3\&quot;}]}&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;cost&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_is_finish&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-literal"><span class="hljs-keyword">true</span></span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_seq_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;node_title&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;End&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;token&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">386</span><span class="hljs-punctuation">}</span> 
 
id<span class="hljs-punctuation">:</span> <span class="hljs-number">1</span> 
event<span class="hljs-punctuation">:</span> Done 
data<span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;debug_url&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;https://www.coze.cn/work_flow?execute_id=744119270952162****&amp;space_id=743984899418202****\&amp;workflow_id=743985075059477****&quot;</span><span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="id: 0 
event: Message 
data: {&quot;content&quot;:&quot;{\&quot;output\&quot;:[{\&quot;condition\&quot;:\&quot;中到大雨\&quot;,\&quot;humidity\&quot;:72,\&quot;predict_date\&quot;:\&quot;2024-08-20\&quot;,\&quot;temp_high\&quot;:35,\&quot;temp_low\&quot;:26,\&quot;weather_day\&quot;:\&quot;中到大雨\&quot;,\&quot;wind_dir_day\&quot;:\&quot;西风\&quot;,\&quot;wind_dir_night\&quot;:\&quot;西风\&quot;,\&quot;wind_level_day\&quot;:\&quot;3\&quot;,\&quot;wind_level_night\&quot;:\&quot;3\&quot;}]}&quot;,&quot;content_type&quot;:&quot;text&quot;,&quot;cost&quot;:&quot;0&quot;,&quot;node_is_finish&quot;:true,&quot;node_seq_id&quot;:&quot;0&quot;,&quot;node_title&quot;:&quot;End&quot;,&quot;token&quot;:386} 
 
id: 1 
event: Done 
data: {&quot;debug_url&quot;:&quot;https://www.coze.cn/work_flow?execute_id=744119270952162****&space_id=743984899418202****\&workflow_id=743985075059477****&quot;}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ol>
<h3 id="a3ef2d3a" tabindex="-1">异步运行</h3>
<p>扣子支持异步运行工作流，适用于工作流执行耗时较长，导致运行超时的情况。异步运行时，工作流整体超时时间限制由 10 分钟延长至 24 小时，其他节点的超时时间限制不变，详细说明可参考<a href="/guides/workflow_limits" target="_blank">低代码工作流使用限制</a>。异步运行后可通过本接口返回的 execute_id 调用<a href="/developer_guides/workflow_history" target="_blank">查询工作流异步运行结果</a>接口获取工作流的执行结果。<br>
API 调用流程如下：</p>
<ol data-style="0">
<li>
<p>调用<a href="/developer_guides/workflow_run" target="_blank">执行工作流</a>接口。其中请求参数 <strong>is_async</strong> 参数应设置为 true。<br>
请求示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-Shell">curl --location --request POST &#x27;https://api.coze.cn/v1/workflow/run&#x27; \ 
--header &#x27;Authorization: Bearer pat_hfwkehfncaf****&#x27; \ 
--header &#x27;Content-Type: application/json&#x27; \ 
--data-raw &#x27;{ 
    &quot;workflow_id&quot;: &quot;73664689170551*****&quot;, 
    &quot;parameters&quot;: { 
        &quot;user_id&quot;:&quot;12345&quot;, 
        &quot;user_name&quot;:&quot;George&quot; 
    }, 
    &quot;is_async&quot;: true,
    &quot;app_id&quot;:&quot;743962661420117****&quot; 
} 
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location --request POST &apos;https://api.coze.cn/v1/workflow/run&apos; \ 
--header &apos;Authorization: Bearer pat_hfwkehfncaf****&apos; \ 
--header &apos;Content-Type: application/json&apos; \ 
--data-raw &apos;{ 
    &quot;workflow_id&quot;: &quot;73664689170551*****&quot;, 
    &quot;parameters&quot;: { 
        &quot;user_id&quot;:&quot;12345&quot;, 
        &quot;user_name&quot;:&quot;George&quot; 
    }, 
    &quot;is_async&quot;: true,
    &quot;app_id&quot;:&quot;743962661420117****&quot; 
} " style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p>从响应中获取到 execute_id，即异步运行的执行 ID。响应示例如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-Shell">{ 
    &quot;code&quot;: 0, 
    &quot;debug_url&quot;: &quot;https://www.coze.cn/work_flow?execute_id=742482313128840****&amp;space_id=731375784444321****&amp;workflow_id=74243949454920****&quot;, 
    &quot;execute_id&quot;: &quot;74248231312884****&quot;, 
    &quot;msg&quot;: &quot;Success&quot; 
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{ 
    &quot;code&quot;: 0, 
    &quot;debug_url&quot;: &quot;https://www.coze.cn/work_flow?execute_id=742482313128840****&space_id=731375784444321****&workflow_id=74243949454920****&quot;, 
    &quot;execute_id&quot;: &quot;74248231312884****&quot;, 
    &quot;msg&quot;: &quot;Success&quot; 
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>调用<a href="/developer_guides/workflow_history" target="_blank">查询工作流异步运行结果</a>接口。<br>
在 API 请求中指定 execute_id。例如以下请求示例中，path 参数 <code>743104097880585****</code> 是 execute_id。</p>

<div style="position: relative">
	<pre><code class="hljs language-Shell">curl --location &#x27;https://api.coze.cn/v1/workflows/742963539464539****/run_histories/743104097880585****&#x27; \ 
--header &#x27;Authorization: Bearer pat_********&#x27; 
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location &apos;https://api.coze.cn/v1/workflows/742963539464539****/run_histories/743104097880585****&apos; \ 
--header &apos;Authorization: Bearer pat_********&apos; " style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p>以下响应示例表示工作流异步执行完成，且状态为执行成功。如果执行异常，你还可以在响应信息中获取 debug_url，通过浏览器访问这个地址，可以查看各个节点的执行结果。</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span> 
        <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;20241029152003BC531DC784F1897B****&quot;</span> 
    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span> 
    <span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span> 
    <span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span> 
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span> 
        <span class="hljs-punctuation">{</span> 
            <span class="hljs-attr">&quot;update_time&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1730174065</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;cost&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;0.00000&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;output&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;{\&quot;Output\&quot;:\&quot;{\\\&quot;content_type\\\&quot;:1,\\\&quot;data\\\&quot;:\\\&quot;来找姐姐有什么事呀\\\&quot;,\\\&quot;original_result\\\&quot;:null,\\\&quot;type_for_model\\\&quot;:2}\&quot;}&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;742963486232569****&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;token&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;execute_status&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;Success&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;connector_uid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;223687073464****&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;run_mode&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;connector_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;1024&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;20241029115423ED85C3401395715F726E&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;debug_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;https://www.coze.cn/work_flow?execute_id=743104097880585****&amp;space_id=730976060439760****&amp;workflow_id=742963539464539****&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;error_code&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;error_message&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;execute_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;743104097880585****&quot;</span><span class="hljs-punctuation">,</span> 
            <span class="hljs-attr">&quot;create_time&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1730174063</span> 
        <span class="hljs-punctuation">}</span> 
    <span class="hljs-punctuation">]</span> 
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;detail&quot;: { 
        &quot;logid&quot;: &quot;20241029152003BC531DC784F1897B****&quot; 
    }, 
    &quot;code&quot;: 0, 
    &quot;msg&quot;: &quot;&quot;, 
    &quot;data&quot;: [ 
        { 
            &quot;update_time&quot;: 1730174065, 
            &quot;cost&quot;: &quot;0.00000&quot;, 
            &quot;output&quot;: &quot;{\&quot;Output\&quot;:\&quot;{\\\&quot;content_type\\\&quot;:1,\\\&quot;data\\\&quot;:\\\&quot;来找姐姐有什么事呀\\\&quot;,\\\&quot;original_result\\\&quot;:null,\\\&quot;type_for_model\\\&quot;:2}\&quot;}&quot;, 
            &quot;bot_id&quot;: &quot;742963486232569****&quot;, 
            &quot;token&quot;: &quot;0&quot;, 
            &quot;execute_status&quot;: &quot;Success&quot;, 
            &quot;connector_uid&quot;: &quot;223687073464****&quot;, 
            &quot;run_mode&quot;: 0, 
            &quot;connector_id&quot;: &quot;1024&quot;, 
            &quot;logid&quot;: &quot;20241029115423ED85C3401395715F726E&quot;, 
            &quot;debug_url&quot;: &quot;https://www.coze.cn/work_flow?execute_id=743104097880585****&space_id=730976060439760****&workflow_id=742963539464539****&quot;, 
            &quot;error_code&quot;: &quot;&quot;, 
            &quot;error_message&quot;: &quot;&quot;, 
            &quot;execute_id&quot;: &quot;743104097880585****&quot;, 
            &quot;create_time&quot;: 1730174063 
        } 
    ] 
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ol>
<h3 id="dbd7159b" tabindex="-1">如何获取应用 ID？</h3>
<p>运行工作流时需要通过请求参数 app_id 指定应用的 ID，以便工作流节点使用应用资源库的数据和知识。你可以通过应用的业务编排页面 URL 中获取应用 ID，也就是 URL 中 project-ide 参数后的一串字符，例如 <code>https://www.coze.cn/space/739174157340921****/project-ide/743996105122521****/workflow/744102227704147****</code> 中，应用的 ID 为 <code>743996105122521****</code>。</p>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/guides_publish_api" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">发布为 API 服务</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/guides_publish_app_to_web_sdk" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">发布为 Chat SDK</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="同步运行" href="#eefbaf53" data-href="#eefbaf53">同步运行</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="非流式响应" href="#232e8e11" data-href="#232e8e11">非流式响应</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="流式响应" href="#272e3b21" data-href="#272e3b21">流式响应</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" title="中断场景" href="#6054d52e" data-href="#6054d52e">中断场景</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="异步运行" href="#a3ef2d3a" data-href="#a3ef2d3a">异步运行</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="如何获取应用 ID？" href="#dbd7159b" data-href="#dbd7159b">如何获取应用 ID？</a></div></div></div></div></div></div></div></div>
</body></html>