<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">基于 HTTP 请求实现语音消息</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/4760.77ece367d4.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.782417a8ae.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/dev_how_to_guides_audio_message"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/dev_how_to_guides_audio_message.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/dev_how_to_guides_audio_message" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" style="width:300px" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b97434bdbc784e3ce84ce" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a55df9a4bdbc784e3c9738f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf30d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf317" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf31d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf325" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf334" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf32e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf35a" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf362" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8e614bdbc784e3cce185" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3e2c" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fa8" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc529d" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8bc84bdbc784e3cc52a5" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/dev_how_to_guides_realtime_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="智能音视频概述">智能音视频概述</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52ad" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/dev_how_to_guides_realtime_playground" data-discover="true"><span class="nodeTitle-ONnqtP" title="体验智能音视频 Demo">体验智能音视频 Demo</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52b5" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/dev_how_to_guides_realtime_access" data-discover="true"><span class="nodeTitle-ONnqtP" title="音视频接入方案对比">音视频接入方案对比</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52bf" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="基于 WebSocket 实现音频通话">基于 WebSocket 实现音频通话</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc52c6" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="基于 RTC 实现音视频通话">基于 RTC 实现音视频通话</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc52e5" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:40px" href="/dev_how_to_guides_audio_message" data-discover="true"><span class="nodeTitle-ONnqtP" title="基于 HTTP 请求实现语音消息">基于 HTTP 请求实现语音消息</span></a></div><div id="tree-node-6a3b8bc84bdbc784e3cc52ed" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="语音与音色">语音与音色</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc52f3" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="终端用户用量管控">终端用户用量管控</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc533c" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/dev_how_to_guides_realtime_faq" data-discover="true"><span class="nodeTitle-ONnqtP" title="音视频常见问题">音视频常见问题</span></a></div></div></div><div id="tree-node-6a3b8b8e4bdbc784e3cc445f" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/developer_guides_coze_cli" data-discover="true"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf33f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf369" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/guides_FAQ" data-discover="true"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA" style="width:calc(100% - 300px);--anchor-width:260px"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>音视频</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">基于 HTTP 请求实现语音消息</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">基于 HTTP 请求实现语音消息</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>本文介绍基于 HTTP 请求实现用户给智能体发送语音消息的功能。用户侧发送一条语音消息，智能体接收音频文件后，由大模型生成语音形式的回复。语音回复以流式音频片段的形式返回，应用程序可选择实时播放或在智能体回复完成后将音频片段合并后再播放。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>通过发起对话 API 发送语音消息的功能已停止迭代，推荐使用 WebSocket 语音通话，其具备更优性能、更低延迟，具体请参见<a href="/dev_how_to_guides/websocket_openapi" target="_blank">基于 WebSocket OpenAPI 实现音频通话</a>。</p>
</div>
<h2 id="76c9a091" tabindex="-1">步骤一：上传音频文件</h2>
<ol data-style="0">
<li>准备音频文件。<br>
调用<a href="/developer_guides/chat_v3" target="_blank">发起对话</a> API 之前，需要先准备待输入给智能体的音频文件，也就是语音形式的用户 Query。<br>
音频文件的格式需为 WAV 或 OGG 封装的 OPUS 格式。你可以使用扣子编程提供的<a href="/developer_guides/text_to_speech" target="_blank">语音合成</a> 接口，将指定的文本内容转成符合要求的音频文件。</li>
<li>上传音频文件。<br>
将音频文件上传至扣子编程或第三方存储工具，并获取相应的文件标识或链接。
<ul data-style="1">
<li><strong>上传到扣子编程</strong>：调用<a href="/developer_guides/upload_files" target="_blank">上传文件</a>接口，将音频文件上传到扣子编程，并在接口响应中获取文件的 <code>file_id</code>。</li>
<li><strong>上传到第三方存储工具</strong>：将文件上传到对象存储或其他第三方存储工具中，并获取一个公网可访问的链接，此链接为文件的 <code>file_url</code>。</li>
</ul>
</li>
</ol>
<h2 id="1be2449d" tabindex="-1">步骤二：调用发起对话 API</h2>
<h3 id="58cabdb2" tabindex="-1">请求结构</h3>
<p>调用<a href="/developer_guides/chat_v3" target="_blank">发起对话</a>时，需在入参中指定已上传的音频文件，并选择流式响应。必选输入参数的说明如下表所示。</p>
<!-- @cols-width: 210,570 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 210px;" /><col style="width: 570px;" /></colgroup><thead>
<tr>
<th>
<p><strong>请求参数</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>bot_id</p>
</td>
<td>
<p>智能体 ID。智能体开发页面 URL 中 <code>bot</code> 参数后的数字就是智能体 ID。</p>
</td>
</tr>
<tr>
<td>
<p>user_id</p>
</td>
<td>
<p>与智能体对话的用户 ID。不同的 user_id，其对话的上下文消息、数据库等对话记忆数据互相隔离。如果不需要用户数据隔离，可将此参数固定为一个任意字符串</p>
</td>
</tr>
<tr>
<td>
<p>stream</p>
</td>
<td>
<p>是否采用流式响应。语音场景下固定设置为 true，表示采用流式响应。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>语音消息只支持流式响应，所以此处 stream 必须设置为 true。</p>
</div>
</td>
</tr>
<tr>
<td>
<p>additional_messages</p>
</td>
<td>
<p>对话中的消息内容，包括对话的历史消息和本次对话中的用户问题。<br>
消息应按对话流程顺序排列，且最后一条消息应为 <code>role=user</code> 的记录，表示本次对话中的用户问题。<br>
数组长度限制为 100，即最多传入 100 条消息。<br>
additional_messages 的字段结构请参见下表。</p>
</td>
</tr>
</tbody>
</table>
</div><p><strong>additional_messages</strong> 为 JSON 数组格式，每个 JSON 对象代表一条独立的消息，其结构如下：</p>
<!-- @cols-width: 172,598 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 172px;" /><col style="width: 598px;" /></colgroup><thead>
<tr>
<th>
<p><strong>字段</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>role</p>
</td>
<td>
<p>发送消息的实体，取值包括：</p>
<ul data-style="0">
<li><strong>user</strong>：用户</li>
<li><strong>assistant</strong>：智能体</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>type</p>
</td>
<td>
<p>消息类型。默认为 <code>question</code>。</p>
<ul data-style="0">
<li>当 <code>role</code> 为 <code>user</code> 时，<code>type</code> 应设置为 <code>question</code>。</li>
<li>当 <code>role</code> 为 <code>assistant</code> 时，<code>type</code> 应设置为 <code>answer</code>。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>content</p>
</td>
<td>
<p>消息内容。在语音场景下，<code>content</code> 字段为一个经过序列化的 JSON 字符串，该字符串表示一个包含多个对象的数组，其中每个对象的类型为 object_string。包含 <code>type</code>、<code>file_id</code> 和 <code>file_url</code> 三个参数。<code>type</code> 固定为 <code>audio</code>。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<ul data-style="0">
<li>如果音频文件上传到扣子编程，在 content 中应指定 type、file_id。</li>
<li>如果音频文件上传到第三方的存储工具，在 content 中应指定 type 和 file_url。</li>
</ul>
</div>
</td>
</tr>
<tr>
<td>
<p>content_type</p>
</td>
<td>
<p>消息内容类型。语音场景下设置为 <code>object_string</code>，表示多模态内容。</p>
</td>
</tr>
</tbody>
</table>
</div><p>additional_messages 语音消息示例如下：</p>
<div class="tabs-tabs-wrapper">
  <div class="tabs-tabs-header">
    <button type="button" class="tabs-tab-button" data-tab="0">通过 API 上传的文件</button>
    <button type="button" class="tabs-tab-button" data-tab="1">通过第三方存储工具上传的文件</button>
  </div>
  <div class="tabs-tabs-container">
<div class="tabs-tab-content" data-index="0">

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">[</span>
        <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;user&quot;</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;[{\&quot;type\&quot;:\&quot;audio\&quot;,\&quot;file_id\&quot;:\&quot;736949598110202****\&quot;}]&quot;</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;object_string&quot;</span>
        <span class="hljs-punctuation">}</span>
    <span class="hljs-punctuation">]</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="[
        {
            &quot;role&quot;:&quot;user&quot;,
            &quot;content&quot;:&quot;[{\&quot;type\&quot;:\&quot;audio\&quot;,\&quot;file_id\&quot;:\&quot;736949598110202****\&quot;}]&quot;,
            &quot;content_type&quot;:&quot;object_string&quot;
        }
    ]" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p></p>
</div>
<div class="tabs-tab-content" data-index="1">

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">[</span>
        <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;user&quot;</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;[{\&quot;type\&quot;:\&quot;audio\&quot;,\&quot;file_url\&quot;:\&quot;https://example.com/image_search/src=http%3A%2F%2Fci.xiaohongshu.com%2Fe7368218-****-bda3-56ad-5672b2a113b2%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&amp;refer=http%3A%2F%2Fci.xiaohongshu.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1720005307&amp;t=1acd734e6e8937****625bcdb0dc57\&quot;}]&quot;</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;object_string&quot;</span>
        <span class="hljs-punctuation">}</span>
    <span class="hljs-punctuation">]</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="[
        {
            &quot;role&quot;:&quot;user&quot;,
            &quot;content&quot;:&quot;[{\&quot;type\&quot;:\&quot;audio\&quot;,\&quot;file_url\&quot;:\&quot;https://example.com/image_search/src=http%3A%2F%2Fci.xiaohongshu.com%2Fe7368218-****-bda3-56ad-5672b2a113b2%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&refer=http%3A%2F%2Fci.xiaohongshu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1720005307&t=1acd734e6e8937****625bcdb0dc57\&quot;}]&quot;,
            &quot;content_type&quot;:&quot;object_string&quot;
        }
    ]" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p></p>
</div>
  </div>
</div>
<h3 id="18d40473" tabindex="-1">响应结构</h3>
<p>语音场景下，<a href="/developer_guides/chat_v3" target="_blank">发起对话</a>接口的响应为流式响应。<code>conversation.audio.delta</code> 响应事件中包含模型回复的音频片段。<code>data</code>   字段为 <code>Message Object</code>，其中 <code>content_type</code> 为 <code>audio</code>，<code>content</code> 为音频片段的 Base64 编码字符串。<br>
根据输入音频文件格式，content 的格式有所不同：</p>
<ul data-style="0">
<li>若输入音频文件为 WAV 格式， <code>content</code> 为 PCM 音频片段的 Base64 编码字符串。音频片段采样率为 24kHz，16 位，单声道，little-endian。</li>
<li>若输入音频文件为 OGG_OPUS 格式，<code>content</code> 为 OPUS 音频片段的 Base64 编码字符串。音频片段码率为 48kbps，单声道，帧长为 10ms。如需自定义 OPUS 编码格式，可参考下文中的<a href="/dev_how_to_guides/audio_message#cf0e4de6" target="_blank">自定义 opus 编码</a>。</li>
</ul>
<div class="tabs-tabs-wrapper">
  <div class="tabs-tabs-header">
    <button type="button" class="tabs-tab-button" data-tab="0">请求示例</button>
    <button type="button" class="tabs-tab-button" data-tab="1">响应示例</button>
  </div>
  <div class="tabs-tabs-container">
<div class="tabs-tab-content" data-index="0">

<div style="position: relative">
	<pre><code class="hljs language-Bash">curl --location --request POST <span class="hljs-string">&#x27;https://api.coze.cn/v3/chat&#x27;</span> \ 
--header <span class="hljs-string">&#x27;Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****&#x27;</span> \ 
--header <span class="hljs-string">&#x27;Content-Type: application/json&#x27;</span> \ 
--data-raw <span class="hljs-string">&#x27;{ 
    &quot;bot_id&quot;: &quot;734829333445931****&quot;, 
    &quot;user_id&quot;: &quot;123456789&quot;, 
    &quot;stream&quot;: true, 
    &quot;auto_save_history&quot;:true, 
    &quot;additional_messages&quot;:[ 
        { 
            &quot;role&quot;:&quot;user&quot;, 
            &quot;content&quot;:&quot;[{\&quot;type\&quot;: \&quot;audio\&quot;, \&quot;file_id\&quot;: \&quot;734829333445931****\&quot;}]&quot;, 
            &quot;content_type&quot;:&quot;object_string&quot; 
        } 
    ] 
}&#x27;</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location --request POST &apos;https://api.coze.cn/v3/chat&apos; \ 
--header &apos;Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****&apos; \ 
--header &apos;Content-Type: application/json&apos; \ 
--data-raw &apos;{ 
    &quot;bot_id&quot;: &quot;734829333445931****&quot;, 
    &quot;user_id&quot;: &quot;123456789&quot;, 
    &quot;stream&quot;: true, 
    &quot;auto_save_history&quot;:true, 
    &quot;additional_messages&quot;:[ 
        { 
            &quot;role&quot;:&quot;user&quot;, 
            &quot;content&quot;:&quot;[{\&quot;type\&quot;: \&quot;audio\&quot;, \&quot;file_id\&quot;: \&quot;734829333445931****\&quot;}]&quot;, 
            &quot;content_type&quot;:&quot;object_string&quot; 
        } 
    ] 
}&apos;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p></p>
</div>
<div class="tabs-tab-content" data-index="1">

<div style="position: relative">
	<pre><code class="hljs language-JSON">event<span class="hljs-punctuation">:</span>conversation.chat.created 
<span class="hljs-comment">// 在 chat 事件里，data 字段中的 id 为 Chat ID，即会话 ID。</span>
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;completed_at&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">1718792949</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;last_error&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;status&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;created&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;usage&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;token_count&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;output_count&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;input_count&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">}</span> 
 
event<span class="hljs-punctuation">:</span>conversation.chat.in_progress 
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;completed_at&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">1718792949</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;last_error&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;status&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;in_progress&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;usage&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;token_count&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;output_count&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;input_count&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">}</span> 
 
event<span class="hljs-punctuation">:</span>conversation.message.delta 
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159494123470858&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;assistant&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;answer&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;2&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">}</span> 
 
event<span class="hljs-punctuation">:</span>conversation.message.delta 
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159494123470858&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;assistant&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;answer&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;0&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">}</span> 
<span class="hljs-comment">// 语音消息</span>
event<span class="hljs-punctuation">:</span>conversation.audio.delta 
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159494123470858&quot;</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;audio&quot;</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;DQATABQAEgAUABEADgARAA8ADgAMAAsACQAGAAQA/v/6//z/+v***&quot;</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;assistant&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;answer&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">}</span> 
 
<span class="hljs-comment">//省略模型回复的部分中间事件event:conversation.message.delta、conversation.audio.delta</span>
...... 
 
event<span class="hljs-punctuation">:</span>conversation.message.delta 
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159494123470858&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;assistant&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;answer&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;星期三&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">}</span> 
 
event<span class="hljs-punctuation">:</span>conversation.message.delta 
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159494123470858&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;assistant&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;answer&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;。&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">}</span> 
 
event<span class="hljs-punctuation">:</span>conversation.message.completed 
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159494123470858&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;assistant&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;answer&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;2024 年 10 月 1 日是星期三。&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">}</span> 
 
event<span class="hljs-punctuation">:</span>conversation.message.completed 
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159494123552778&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;assistant&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;verbose&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;{\&quot;msg_type\&quot;:\&quot;generate_answer_finish\&quot;,\&quot;data\&quot;:\&quot;\&quot;,\&quot;from_module\&quot;:null,\&quot;from_unit\&quot;:null}&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">}</span> 
 
event<span class="hljs-punctuation">:</span>conversation.chat.completed 
data<span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;7382159*****97202&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73814735*****78089&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;73794621****98898&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;completed_at&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">1718792949</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;last_error&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">0</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;status&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;completed&quot;</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;usage&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-punctuation">{</span><span class="hljs-attr">&quot;token_count&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">633</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;output_count&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">19</span><span class="hljs-punctuation">,</span><span class="hljs-attr">&quot;input_count&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-number">614</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">}</span> 
 
event<span class="hljs-punctuation">:</span>done 
data<span class="hljs-punctuation">:</span><span class="hljs-string">&quot;[DONE]&quot;</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="event:conversation.chat.created 
// 在 chat 事件里，data 字段中的 id 为 Chat ID，即会话 ID。
data:{&quot;id&quot;:&quot;7382159*****97202&quot;,&quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;completed_at&quot;:1718792949,&quot;last_error&quot;:{&quot;code&quot;:0,&quot;msg&quot;:&quot;&quot;},&quot;status&quot;:&quot;created&quot;,&quot;usage&quot;:{&quot;token_count&quot;:0,&quot;output_count&quot;:0,&quot;input_count&quot;:0}} 
 
event:conversation.chat.in_progress 
data:{&quot;id&quot;:&quot;7382159*****97202&quot;,&quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;completed_at&quot;:1718792949,&quot;last_error&quot;:{&quot;code&quot;:0,&quot;msg&quot;:&quot;&quot;},&quot;status&quot;:&quot;in_progress&quot;,&quot;usage&quot;:{&quot;token_count&quot;:0,&quot;output_count&quot;:0,&quot;input_count&quot;:0}} 
 
event:conversation.message.delta 
data:{&quot;id&quot;:&quot;7382159494123470858&quot;,&quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;role&quot;:&quot;assistant&quot;,&quot;type&quot;:&quot;answer&quot;,&quot;content&quot;:&quot;2&quot;,&quot;content_type&quot;:&quot;text&quot;,&quot;chat_id&quot;:&quot;7382159*****97202&quot;} 
 
event:conversation.message.delta 
data:{&quot;id&quot;:&quot;7382159494123470858&quot;,&quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;role&quot;:&quot;assistant&quot;,&quot;type&quot;:&quot;answer&quot;,&quot;content&quot;:&quot;0&quot;,&quot;content_type&quot;:&quot;text&quot;,&quot;chat_id&quot;:&quot;7382159*****97202&quot;} 
// 语音消息
event:conversation.audio.delta 
data:{&quot;id&quot;:&quot;7382159494123470858&quot;, &quot;content_type&quot;:&quot;audio&quot;, &quot;content&quot;:&quot;DQATABQAEgAUABEADgARAA8ADgAMAAsACQAGAAQA/v/6//z/+v***&quot;, &quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;role&quot;:&quot;assistant&quot;,&quot;type&quot;:&quot;answer&quot;,&quot;chat_id&quot;:&quot;7382159*****97202&quot;} 
 
//省略模型回复的部分中间事件event:conversation.message.delta、conversation.audio.delta
...... 
 
event:conversation.message.delta 
data:{&quot;id&quot;:&quot;7382159494123470858&quot;,&quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;role&quot;:&quot;assistant&quot;,&quot;type&quot;:&quot;answer&quot;,&quot;content&quot;:&quot;星期三&quot;,&quot;content_type&quot;:&quot;text&quot;,&quot;chat_id&quot;:&quot;7382159*****97202&quot;} 
 
event:conversation.message.delta 
data:{&quot;id&quot;:&quot;7382159494123470858&quot;,&quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;role&quot;:&quot;assistant&quot;,&quot;type&quot;:&quot;answer&quot;,&quot;content&quot;:&quot;。&quot;,&quot;content_type&quot;:&quot;text&quot;,&quot;chat_id&quot;:&quot;7382159*****97202&quot;} 
 
event:conversation.message.completed 
data:{&quot;id&quot;:&quot;7382159494123470858&quot;,&quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;role&quot;:&quot;assistant&quot;,&quot;type&quot;:&quot;answer&quot;,&quot;content&quot;:&quot;2024 年 10 月 1 日是星期三。&quot;,&quot;content_type&quot;:&quot;text&quot;,&quot;chat_id&quot;:&quot;7382159*****97202&quot;} 
 
event:conversation.message.completed 
data:{&quot;id&quot;:&quot;7382159494123552778&quot;,&quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;role&quot;:&quot;assistant&quot;,&quot;type&quot;:&quot;verbose&quot;,&quot;content&quot;:&quot;{\&quot;msg_type\&quot;:\&quot;generate_answer_finish\&quot;,\&quot;data\&quot;:\&quot;\&quot;,\&quot;from_module\&quot;:null,\&quot;from_unit\&quot;:null}&quot;,&quot;content_type&quot;:&quot;text&quot;,&quot;chat_id&quot;:&quot;7382159*****97202&quot;} 
 
event:conversation.chat.completed 
data:{&quot;id&quot;:&quot;7382159*****97202&quot;,&quot;conversation_id&quot;:&quot;73814735*****78089&quot;,&quot;bot_id&quot;:&quot;73794621****98898&quot;,&quot;completed_at&quot;:1718792949,&quot;last_error&quot;:{&quot;code&quot;:0,&quot;msg&quot;:&quot;&quot;},&quot;status&quot;:&quot;completed&quot;,&quot;usage&quot;:{&quot;token_count&quot;:633,&quot;output_count&quot;:19,&quot;input_count&quot;:614}} 
 
event:done 
data:&quot;[DONE]&quot;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p></p>
</div>
  </div>
</div>
<h3 id="5bf00212" tabindex="-1"><strong>自定义 opus 编码</strong></h3>
<p>若输入音频文件为 OGG_OPUS 格式，开发者可自定义返回的 OPUS 编码格式。在<a href="/developer_guides/chat_v3" target="_blank">发起对话</a>接口中，通过   <code>extra_params</code> 参数配置返回的 OPUS 音频片段编码格式，<code>audio_message_config</code>配置的值为 JSON 字符串，结构如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;opus_codec&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;bitrate&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">16000</span><span class="hljs-punctuation">,</span>   <span class="hljs-comment">// 码率，不传默认为48000，opus 支持 6kb/s 到 510kb/s 的码率</span>
        <span class="hljs-attr">&quot;use_cbr&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">false</span></span><span class="hljs-punctuation">,</span>   <span class="hljs-comment">// 是否使用 CBR 编码，默认为 false</span>
        <span class="hljs-attr">&quot;frame_size_ms&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">10</span>  <span class="hljs-comment">// opus 帧大小，默认为 10ms。opus 支持 2.5ms 到 60ms 的帧大小</span>
    <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;opus_codec&quot;: {
        &quot;bitrate&quot;: 16000,   // 码率，不传默认为48000，opus 支持 6kb/s 到 510kb/s 的码率
        &quot;use_cbr&quot;: false,   // 是否使用 CBR 编码，默认为 false
        &quot;frame_size_ms&quot;: 10  // opus 帧大小，默认为 10ms。opus 支持 2.5ms 到 60ms 的帧大小
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p>请求示例：</p>

<div style="position: relative">
	<pre><code class="hljs language-Bash">curl --location --request POST <span class="hljs-string">&#x27;https://api.coze.cn/v3/chat&#x27;</span> \ 
--header <span class="hljs-string">&#x27;Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****&#x27;</span> \ 
--header <span class="hljs-string">&#x27;Content-Type: application/json&#x27;</span> \ 
--data-raw <span class="hljs-string">&#x27;{ 
    &quot;bot_id&quot;: &quot;734829333445931****&quot;, 
    &quot;user_id&quot;: &quot;123456789&quot;, 
    &quot;stream&quot;: true, 
    &quot;auto_save_history&quot;:true, 
    &quot;additional_messages&quot;:[ 
        { 
            &quot;role&quot;:&quot;user&quot;, 
            &quot;content&quot;:&quot;[{\&quot;type\&quot;: \&quot;audio\&quot;, \&quot;file_id\&quot;: \&quot;734829333445931****\&quot;}]&quot;, 
            &quot;content_type&quot;:&quot;object_string&quot; 
        } 
    ],
    &quot;extra_params&quot;: {
        &quot;audio_message_config&quot;: &quot;{\&quot;opus_codec\&quot;: {\&quot;bitrate\&quot;: 16000, \&quot;use_cbr\&quot;: false, \&quot;frame_size_ms\&quot;: 60}}&quot;
    } 
}&#x27;</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location --request POST &apos;https://api.coze.cn/v3/chat&apos; \ 
--header &apos;Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****&apos; \ 
--header &apos;Content-Type: application/json&apos; \ 
--data-raw &apos;{ 
    &quot;bot_id&quot;: &quot;734829333445931****&quot;, 
    &quot;user_id&quot;: &quot;123456789&quot;, 
    &quot;stream&quot;: true, 
    &quot;auto_save_history&quot;:true, 
    &quot;additional_messages&quot;:[ 
        { 
            &quot;role&quot;:&quot;user&quot;, 
            &quot;content&quot;:&quot;[{\&quot;type\&quot;: \&quot;audio\&quot;, \&quot;file_id\&quot;: \&quot;734829333445931****\&quot;}]&quot;, 
            &quot;content_type&quot;:&quot;object_string&quot; 
        } 
    ],
    &quot;extra_params&quot;: {
        &quot;audio_message_config&quot;: &quot;{\&quot;opus_codec\&quot;: {\&quot;bitrate\&quot;: 16000, \&quot;use_cbr\&quot;: false, \&quot;frame_size_ms\&quot;: 60}}&quot;
    } 
}&apos;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h2 id="e3203a4c" tabindex="-1">步骤三：处理音频片段</h2>
<p>通过发起对话 API 的返回结果中获取音频片段后，开发者可选择实时播放，或在流式响应结束后将音频片段合并写入音频文件，一次性播放给用户。<br>
以下是使用 Go 语言处理音频片段的示例代码，展示如何使用 WAV 封装 PCM 和 OGG 封装 OPUS。</p>
<div class="tabs-tabs-wrapper">
  <div class="tabs-tabs-header">
    <button type="button" class="tabs-tab-button" data-tab="0">WAV 封装 PCM 格式音频</button>
    <button type="button" class="tabs-tab-button" data-tab="1">OGG 封装 OPUS 格式音频</button>
  </div>
  <div class="tabs-tabs-container">
<div class="tabs-tab-content" data-index="0">

<div style="position: relative">
	<pre><code class="hljs language-Go"><span class="hljs-keyword">import</span> (
    <span class="hljs-string">&quot;log&quot;</span>
    <span class="hljs-string">&quot;os&quot;</span>
    
    <span class="hljs-string">&quot;github.com/go-audio/audio&quot;</span>
    <span class="hljs-string">&quot;github.com/go-audio/wav&quot;</span>
)

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">callCoze</span><span class="hljs-params">()</span></span> {
    
    pcmData := <span class="hljs-built_in">make</span>([]<span class="hljs-type">byte</span>, <span class="hljs-number">0</span>)
   
    <span class="hljs-comment">// 调用 coze ，从 http response 中一直拿返回的 event 和 data</span>
    <span class="hljs-keyword">for</span> {
        <span class="hljs-comment">// 伪代码，从 http response 中流式读取 event 和 data</span>
        event, data := resp.Recv()
        <span class="hljs-comment">// 对于所有 event 为 conversation.audio.delta 的事件，取出 data 中的音频片段</span>
        <span class="hljs-keyword">if</span> event == <span class="hljs-string">&quot;conversation.audio.delta&quot;</span> {
            audioData := <span class="hljs-built_in">make</span>(<span class="hljs-keyword">map</span>[<span class="hljs-type">string</span>]<span class="hljs-keyword">interface</span>{})
            err := json.Unmarshal([]<span class="hljs-type">byte</span>(data), &amp;audioData)
            <span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> {
                log.Fatalf(<span class="hljs-string">&quot;Error Unmarshal: %v&quot;</span>, err)
            }
            <span class="hljs-keyword">if</span> base64AudioStr, exist := audioData[<span class="hljs-string">&quot;content&quot;</span>]; exist {
                pcmPart, err := base64.StdEncoding.DecodeString(base64AudioStr.(<span class="hljs-type">string</span>))
                <span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> {
                    log.Fatalf(<span class="hljs-string">&quot;Error DecodeString: %v&quot;</span>, err)
                }
                pcmData = <span class="hljs-built_in">append</span>(pcmData, pcmPart...)
            }
        }
        <span class="hljs-comment">// 结束事件，退出循环</span>
        <span class="hljs-keyword">if</span> event == <span class="hljs-string">&quot;done&quot;</span> {
            <span class="hljs-keyword">break</span>
        }
    }
    
    writeWav(pcmData)
}

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">writeWav</span><span class="hljs-params">(pcmData [][]<span class="hljs-type">byte</span>)</span></span> {
    <span class="hljs-comment">// 采样率</span>
    sampleRate := <span class="hljs-number">24000</span>
    <span class="hljs-comment">// 位深</span>
    bitDepth := <span class="hljs-number">16</span>
    <span class="hljs-comment">// 通道数</span>
    numChannels := <span class="hljs-number">1</span>
    f, err := os.Create(<span class="hljs-string">&quot;pcm-example.wav&quot;</span>)
    <span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> {
        log.Fatalf(<span class="hljs-string">&quot;Error Create: %v&quot;</span>, err)
    }
    
    intData := <span class="hljs-built_in">make</span>([]<span class="hljs-type">int</span>, <span class="hljs-number">0</span>)
    <span class="hljs-keyword">for</span> i := <span class="hljs-number">0</span>; i &lt; <span class="hljs-built_in">len</span>(pcmData); i += <span class="hljs-number">2</span> {
        intData = <span class="hljs-built_in">append</span>(intData, <span class="hljs-type">int</span>(<span class="hljs-type">uint16</span>(pcmData[i])|<span class="hljs-type">uint16</span>(pcmData[i+<span class="hljs-number">1</span>])&lt;&lt;<span class="hljs-number">8</span>))
    }
    intBuffer := &amp;audio.IntBuffer{
        Format: &amp;audio.Format{
           NumChannels: numChannels,
           SampleRate:  sampleRate,
        },
        Data:           intData,
        SourceBitDepth: bitDepth,
    }
    
    e := wav.NewEncoder(f, sampleRate, bitDepth, numChannels, <span class="hljs-number">1</span>)
    <span class="hljs-keyword">defer</span> e.Close()
    err = e.Write(intBuffer)
    <span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> {
        log.Fatalf(<span class="hljs-string">&quot;Error Write: %v&quot;</span>, err)
    }
    <span class="hljs-keyword">return</span> 
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import (
    &quot;log&quot;
    &quot;os&quot;
    
    &quot;github.com/go-audio/audio&quot;
    &quot;github.com/go-audio/wav&quot;
)

func callCoze() {
    
    pcmData := make([]byte, 0)
   
    // 调用 coze ，从 http response 中一直拿返回的 event 和 data
    for {
        // 伪代码，从 http response 中流式读取 event 和 data
        event, data := resp.Recv()
        // 对于所有 event 为 conversation.audio.delta 的事件，取出 data 中的音频片段
        if event == &quot;conversation.audio.delta&quot; {
            audioData := make(map[string]interface{})
            err := json.Unmarshal([]byte(data), &audioData)
            if err != nil {
                log.Fatalf(&quot;Error Unmarshal: %v&quot;, err)
            }
            if base64AudioStr, exist := audioData[&quot;content&quot;]; exist {
                pcmPart, err := base64.StdEncoding.DecodeString(base64AudioStr.(string))
                if err != nil {
                    log.Fatalf(&quot;Error DecodeString: %v&quot;, err)
                }
                pcmData = append(pcmData, pcmPart...)
            }
        }
        // 结束事件，退出循环
        if event == &quot;done&quot; {
            break
        }
    }
    
    writeWav(pcmData)
}

func writeWav(pcmData [][]byte) {
    // 采样率
    sampleRate := 24000
    // 位深
    bitDepth := 16
    // 通道数
    numChannels := 1
    f, err := os.Create(&quot;pcm-example.wav&quot;)
    if err != nil {
        log.Fatalf(&quot;Error Create: %v&quot;, err)
    }
    
    intData := make([]int, 0)
    for i := 0; i < len(pcmData); i += 2 {
        intData = append(intData, int(uint16(pcmData[i])|uint16(pcmData[i+1])<<8))
    }
    intBuffer := &audio.IntBuffer{
        Format: &audio.Format{
           NumChannels: numChannels,
           SampleRate:  sampleRate,
        },
        Data:           intData,
        SourceBitDepth: bitDepth,
    }
    
    e := wav.NewEncoder(f, sampleRate, bitDepth, numChannels, 1)
    defer e.Close()
    err = e.Write(intBuffer)
    if err != nil {
        log.Fatalf(&quot;Error Write: %v&quot;, err)
    }
    return 
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p></p>
</div>
<div class="tabs-tab-content" data-index="1">

<div style="position: relative">
	<pre><code class="hljs language-Go"><span class="hljs-keyword">import</span> (
    <span class="hljs-string">&quot;log&quot;</span>
    
    <span class="hljs-string">&quot;github.com/pion/webrtc/v3/pkg/media/oggwriter&quot;</span>
)

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">callCoze</span><span class="hljs-params">()</span></span> {
    
    opusData := <span class="hljs-built_in">make</span>([][]<span class="hljs-type">byte</span>, <span class="hljs-number">0</span>)
   
    <span class="hljs-comment">// 调用 coze ，从  http response 中一直拿返回的 event 和 data</span>
    <span class="hljs-keyword">for</span> {
        <span class="hljs-comment">// 伪代码，从 http response 中流式读取 event 和 data</span>
        event, data := resp.Recv()
        <span class="hljs-comment">// 对于所有 event 为 conversation.audio.delta 的事件，取出 data 中的音频片段</span>
        <span class="hljs-keyword">if</span> event == <span class="hljs-string">&quot;conversation.audio.delta&quot;</span> {
            audioData := <span class="hljs-built_in">make</span>(<span class="hljs-keyword">map</span>[<span class="hljs-type">string</span>]<span class="hljs-keyword">interface</span>{})
            err := json.Unmarshal([]<span class="hljs-type">byte</span>(data), &amp;audioData)
            <span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> {
                log.Fatalf(<span class="hljs-string">&quot;Error Unmarshal: %v&quot;</span>, err)
            }
            <span class="hljs-keyword">if</span> base64AudioStr, exist := audioData[<span class="hljs-string">&quot;content&quot;</span>]; exist {
                opusPart, err := base64.StdEncoding.DecodeString(base64AudioStr.(<span class="hljs-type">string</span>))
                <span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> {
                    log.Fatalf(<span class="hljs-string">&quot;Error DecodeString: %v&quot;</span>, err)
                }
                opusData = <span class="hljs-built_in">append</span>(opusData, opusPart)
            }
        }
        <span class="hljs-comment">// 结束事件，退出循环</span>
        <span class="hljs-keyword">if</span> event == <span class="hljs-string">&quot;done&quot;</span> {
            <span class="hljs-keyword">break</span>
        }
    }
    
    writeOgg(opusData)
}

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">writeOgg</span><span class="hljs-params">(opusData [][]<span class="hljs-type">byte</span>)</span></span> {
    <span class="hljs-comment">// 将 opus 写入到 opus-example.ogg 文件，采样率为 48000，单通道</span>
    writer, err := oggwriter.New(<span class="hljs-string">&quot;./opus-example.ogg&quot;</span>, <span class="hljs-number">48000</span>, <span class="hljs-number">1</span>)
    <span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> {
       log.Fatalf(<span class="hljs-string">&quot;Error creating OggWriter: %v&quot;</span>, err)
    }
    <span class="hljs-keyword">defer</span> writer.Close()

    <span class="hljs-keyword">for</span> idx, data := <span class="hljs-keyword">range</span> opusData {
       err = writer.WriteRTP(&amp;rtp.Packet{
          Payload: data,
          Header: rtp.Header{
             Timestamp: <span class="hljs-number">480</span> * <span class="hljs-type">uint32</span>(idx+<span class="hljs-number">1</span>),
          },
       })
       <span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> {
          log.Fatalf(<span class="hljs-string">&quot;Error writing to OggWriter: %v&quot;</span>, err)
       }
    }
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import (
    &quot;log&quot;
    
    &quot;github.com/pion/webrtc/v3/pkg/media/oggwriter&quot;
)

func callCoze() {
    
    opusData := make([][]byte, 0)
   
    // 调用 coze ，从  http response 中一直拿返回的 event 和 data
    for {
        // 伪代码，从 http response 中流式读取 event 和 data
        event, data := resp.Recv()
        // 对于所有 event 为 conversation.audio.delta 的事件，取出 data 中的音频片段
        if event == &quot;conversation.audio.delta&quot; {
            audioData := make(map[string]interface{})
            err := json.Unmarshal([]byte(data), &audioData)
            if err != nil {
                log.Fatalf(&quot;Error Unmarshal: %v&quot;, err)
            }
            if base64AudioStr, exist := audioData[&quot;content&quot;]; exist {
                opusPart, err := base64.StdEncoding.DecodeString(base64AudioStr.(string))
                if err != nil {
                    log.Fatalf(&quot;Error DecodeString: %v&quot;, err)
                }
                opusData = append(opusData, opusPart)
            }
        }
        // 结束事件，退出循环
        if event == &quot;done&quot; {
            break
        }
    }
    
    writeOgg(opusData)
}

func writeOgg(opusData [][]byte) {
    // 将 opus 写入到 opus-example.ogg 文件，采样率为 48000，单通道
    writer, err := oggwriter.New(&quot;./opus-example.ogg&quot;, 48000, 1)
    if err != nil {
       log.Fatalf(&quot;Error creating OggWriter: %v&quot;, err)
    }
    defer writer.Close()

    for idx, data := range opusData {
       err = writer.WriteRTP(&rtp.Packet{
          Payload: data,
          Header: rtp.Header{
             Timestamp: 480 * uint32(idx+1),
          },
       })
       if err != nil {
          log.Fatalf(&quot;Error writing to OggWriter: %v&quot;, err)
       }
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<p></p>
</div>
  </div>
</div>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/dev_how_to_guides_rtc_sdk" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">集成火山引擎 RTC SDK</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/dev_how_to_guides_asr_tts" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">语音合成与识别</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="步骤一：上传音频文件" href="#76c9a091" data-href="#76c9a091">步骤一：上传音频文件</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="步骤二：调用发起对话 API" href="#1be2449d" data-href="#1be2449d">步骤二：调用发起对话 API</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="请求结构" href="#58cabdb2" data-href="#58cabdb2">请求结构</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="响应结构" href="#18d40473" data-href="#18d40473">响应结构</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="自定义 opus 编码" href="#5bf00212" data-href="#5bf00212">自定义 opus 编码</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="步骤三：处理音频片段" href="#e3203a4c" data-href="#e3203a4c">步骤三：处理音频片段</a></div></div></div></div></div></div></div></div>
</body></html>