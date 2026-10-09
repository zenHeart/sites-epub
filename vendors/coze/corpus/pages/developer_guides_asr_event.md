<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">双向流式语音识别事件</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/5956.1729cb00c0.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.ca52691239.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/developer_guides_asr_event"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/developer_guides_asr_event.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
  
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/developer_guides_asr_event" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b97434bdbc784e3ce84ce" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a55df9a4bdbc784e3c9738f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf30d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf317" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf31d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf325" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf334" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf32e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf35a" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf362" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8e614bdbc784e3cce185" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3e2c" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3ece" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_coze_api_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="API 介绍">API 介绍</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ed4" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_changelog" data-discover="true"><span class="nodeTitle-ONnqtP" title="更新日志">更新日志</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3edc" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_preparation" data-discover="true"><span class="nodeTitle-ONnqtP" title="准备工作">准备工作</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ee3" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_api_playground" data-discover="true"><span class="nodeTitle-ONnqtP" title="API Playground">API Playground</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e32" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="鉴权">鉴权</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e6a" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能体和应用">智能体和应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ee9" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="工作空间">工作空间</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3eef" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="文件夹">文件夹</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ef7" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="企业/组织">企业/组织</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3efe" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="会话与消息">会话与消息</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f04" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="对话">对话</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f0c" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f13" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="文件">文件</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f1a" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能音视频">智能音视频</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3f20" class="nodeWrapper-woTZn5" data-tree-level="3"><div to="/" class="nodeContent-GigwSX" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="ASR、TTS 与音色">ASR、TTS 与音色</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f27" class="nodeWrapper-woTZn5" data-tree-level="3"><div to="/" class="nodeContent-GigwSX" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="RTC 语音">RTC 语音</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f2e" class="nodeWrapper-woTZn5" data-tree-level="3"><div to="/" class="nodeContent-GigwSX" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="WebSocket 语音">WebSocket 语音</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc41ed" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX" style="margin-left:72px" href="/developer_guides_asr_api" data-discover="true"><span class="nodeTitle-ONnqtP" title="双向流式语音识别">双向流式语音识别</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc41f5" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:72px" href="/developer_guides_asr_event" data-discover="true"><span class="nodeTitle-ONnqtP" title="双向流式语音识别事件">双向流式语音识别事件</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc41fd" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX" style="margin-left:72px" href="/developer_guides_tts_api" data-discover="true"><span class="nodeTitle-ONnqtP" title="双向流式语音合成">双向流式语音合成</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4203" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX" style="margin-left:72px" href="/developer_guides_tts_event" data-discover="true"><span class="nodeTitle-ONnqtP" title="双向流式语音合成事件">双向流式语音合成事件</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc420b" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX" style="margin-left:72px" href="/developer_guides_streaming_chat_api" data-discover="true"><span class="nodeTitle-ONnqtP" title="双向流式语音对话">双向流式语音对话</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4211" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX" style="margin-left:72px" href="/developer_guides_streaming_chat_event" data-discover="true"><span class="nodeTitle-ONnqtP" title="双向流式对话上行事件">双向流式对话上行事件</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4219" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX" style="margin-left:72px" href="/developer_guides_streaming_chat_downlink_event" data-discover="true"><span class="nodeTitle-ONnqtP" title="双向流式对话下行事件">双向流式对话下行事件</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc42a6" class="nodeWrapper-woTZn5" data-tree-level="3"><div to="/" class="nodeContent-GigwSX" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="声纹识别">声纹识别</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f35" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="知识库">知识库</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f3b" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="数据库">数据库</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f43" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="插件">插件</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f49" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="变量">变量</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f51" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="渠道">渠道</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f58" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="用量限额">用量限额</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f5f" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="账单与权益">账单与权益</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f66" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="回调">回调</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f84" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_coze_error_codes" data-discover="true"><span class="nodeTitle-ONnqtP" title="错误码">错误码</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f99" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="API 教程">API 教程</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f8a" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_api_faq" data-discover="true"><span class="nodeTitle-ONnqtP" title="API 常见问题">API 常见问题</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fa8" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc529d" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8e4bdbc784e3cc445f" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/developer_guides_coze_cli" data-discover="true"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf33f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf369" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/guides_FAQ" data-discover="true"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>API 参考</span><span class="separator-KB9yMa">/</span><span>智能音视频</span><span class="separator-KB9yMa">/</span><span>WebSocket 语音</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">双向流式语音识别事件</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">双向流式语音识别事件</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg><span>复制页面</span></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><h2 id="3482fcbd" tabindex="-1">上行事件</h2>
<h3 id="a7ca67ab" tabindex="-1">更新语音识别配置</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>transcriptions.update</code></p>
</li>
<li>
<p><strong>事件说明</strong>：更新语音识别配置。若更新成功，会收到 <code>transcriptions.updated</code> 的下行事件，否则，会收到 <code>error</code> 下行事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 224,100,100,414 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 224px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 414px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>客户端自行生成的事件 ID，方便定位问题。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>transcriptions.update</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>事件数据，包含语音识别配置的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>输入音频格式。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.format</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>输入音频的格式，支持 <code>pcm</code>、<code>wav</code>、<code>ogg</code>。默认为 <code>wav</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.codec</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>输入音频的编码，支持 <code>pcm</code>、<code>opus</code>。默认为 <code>pcm</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.sample_rate</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>输入音频的采样率，默认 24000。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.channel</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>输入音频的声道数，默认是 1（单声道）。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.bit_depth</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>输入音频的位深，默认是 16。</p>
</td>
</tr>
<tr>
<td>
<p>data.asr_config</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>语音识别配置，包括热词和上下文信息，以便优化语音识别的准确性和相关性。</p>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.hot_words</p>
</td>
<td>
<p>Array<String></p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>输入热词列表，以便提升这些词汇的识别准确率。<br>
所有热词加起来最多100个 Tokens，超出部分将自动截断。</p>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.context</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>输入上下文信息。<br>
最多输入 800 个 Tokens，超出部分将自动截断。</p>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.user_language</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>用户说话的语种，默认为 <code>common</code>。选项包括：</p>
<ul data-style="1">
<li>common：大模型语音识别，可自动识别中英粤。</li>
<li>zh：小模型语音识别，中文。</li>
<li>cant：小模型语音识别，粤语。</li>
<li>sc：小模型语音识别，川渝。</li>
<li>en：小模型语音识别，英语。</li>
<li>ja：小模型语音识别，日语。</li>
<li>ko：小模型语音识别，韩语。</li>
<li>fr：小模型语音识别，法语。</li>
<li>id：小模型语音识别，印尼语。</li>
<li>es：小模型语音识别，西班牙语。</li>
<li>pt：小模型语音识别，葡萄牙语。</li>
<li>ms：小模型语音识别，马来语。</li>
<li>ru：小模型语音识别，俄语。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.enable_ddc</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>将语音转为文本时，是否启用语义顺滑。默认为 <code>true</code>。</p>
<ul data-style="1">
<li><code>true</code>：系统在进行语音处理时，会去掉识别结果中诸如 “啊”“嗯” 等语气词，使得输出的文本语义更加流畅自然，符合正常的语言表达习惯，尤其适用于对文本质量要求较高的场景，如正式的会议记录、新闻稿件生成等。</li>
<li><code>false</code>：系统不会对识别结果中的语气词进行处理，识别结果会保留原始的语气词。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.enable_itn</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>将语音转为文本时，是否开启文本规范化（ITN）处理，将识别结果转换为更符合书面表达习惯的格式以提升可读性。默认为 <code>true</code>。<br>
开启后，会将口语化数字转换为标准数字格式，示例：</p>
<ul data-style="1">
<li>将<code>两点十五分</code>转换为 <code>14:15</code>。</li>
<li>将<code>一百美元</code>转换为 <code>$100</code>。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.enable_punc</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>将语音转为文本时，是否给文本加上标点符号。默认为 <code>true</code>。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>
</li>
</ul>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_id&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;transcriptions.update&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;input_audio&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;format&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;pcm&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;codec&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;pcm&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;sample_rate&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">24000</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;channel&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;bit_depth&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">16</span>
      <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_id&quot;,
  &quot;event_type&quot;: &quot;transcriptions.update&quot;,
  &quot;data&quot;: {
      &quot;input_audio&quot;: {
          &quot;format&quot;: &quot;pcm&quot;,
          &quot;codec&quot;: &quot;pcm&quot;,
          &quot;sample_rate&quot;: 24000,
          &quot;channel&quot;: 1,
          &quot;bit_depth&quot;: 16
      }
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h3 id="9ef6e6ca" tabindex="-1">流式上传音频片段</h3>
<ul data-style="0">
<li><strong>事件类型</strong>：<code>input_audio_buffer.append</code></li>
<li><strong>事件说明</strong>：流式向服务端提交音频的片段。</li>
<li><strong>事件结构</strong>：</li>
</ul>
<!-- @cols-width: 100,100,100,387 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 387px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>客户端自行生成的事件 ID，方便定位问题。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>input_audio_buffer.append</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件数据，包含音频片段信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.delta</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>base64 编码后的音频片段。</p>
</td>
</tr>
</tbody>
</table>
</div><ul data-style="0">
<li><strong>事件示例</strong>：</li>
</ul>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_id&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;input_audio_buffer.append&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
     <span class="hljs-attr">&quot;delta&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;base64EncodedAudioDelta&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_id&quot;,
  &quot;event_type&quot;: &quot;input_audio_buffer.append&quot;,
  &quot;data&quot;: {
     &quot;delta&quot;: &quot;base64EncodedAudioDelta&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h3 id="f5d76c87" tabindex="-1">提交音频</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>input_audio_buffer.complete</code></p>
</li>
<li>
<p><strong>事件说明</strong>：客户端发送 <code>input_audio_buffer.complete</code> 事件来告诉服务端提交音频缓冲区的数据。服务端提交成功后会返回 <code>input_audio_buffer.completed</code> 事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,434 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 434px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>客户端自行生成的事件 ID，方便定位问题。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>input_audio_buffer.complete</code>。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_id&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;input_audio_buffer.complete&quot;</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_id&quot;,
  &quot;event_type&quot;: &quot;input_audio_buffer.complete&quot;
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h3 id="e98db543" tabindex="-1">清除缓冲区音频</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>input_audio_buffer.clear</code></p>
</li>
<li>
<p><strong>事件说明</strong>：客户端发送 <code>input_audio_buffer.clear</code> 事件来告诉服务端清除缓冲区的音频数据。服务端清除完后将返回 <code>input_audio_buffer.cleared</code> 事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,391 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 391px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>客户端自行生成的事件 ID，方便定位问题。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>input_audio_buffer.clear</code>。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_1&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;input_audio_buffer.clear&quot;</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;input_audio_buffer.clear&quot;
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="9f1a57d6" tabindex="-1">下行事件</h2>
<h3 id="06d772a3" tabindex="-1">连接成功</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>transcriptions.created</code></p>
</li>
<li>
<p><strong>事件说明</strong>：语音识别连接成功后，返回此事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>服务端生成的唯一 ID。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>transcriptions.created</code>。</p>
</td>
</tr>
<tr>
<td>
<p>detail</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件详情。</p>
</td>
</tr>
<tr>
<td>
<p>detail.logid</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考获取帮助和技术支持。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7446668538246561xxxx&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;transcriptions.created&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;20241210152726467C48D89D6DB2F3***&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;7446668538246561xxxx&quot;,
  &quot;event_type&quot;: &quot;transcriptions.created&quot;,
  &quot;detail&quot;: {
      &quot;logid&quot;: &quot;20241210152726467C48D89D6DB2F3***&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h3 id="3f842df1" tabindex="-1">配置更新成功</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>transcriptions.updated</code></p>
</li>
<li>
<p><strong>事件说明</strong>：配置更新成功后，会返回最新的配置。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 224,100,100,425 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 224px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 425px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>客户端自行生成的事件 ID，方便定位问题。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>transcriptions.updated</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件数据，包含语音识别配置的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>输入音频格式。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.format</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>输入音频的格式，支持 <code>pcm</code>、<code>wav</code>、<code>ogg</code>。默认为 <code>wav</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.codec</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>输入音频的编码，支持 <code>pcm</code>、<code>opus</code>。默认为 <code>pcm</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.sample_rate</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>输入音频的采样率，默认 24000。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.channel</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>输入音频的声道数，默认是 1（单声道）。</p>
</td>
</tr>
<tr>
<td>
<p>data.input_audio.bit_depth</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>输入音频的位深，默认是 16。</p>
</td>
</tr>
<tr>
<td>
<p>detail</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件详情。</p>
</td>
</tr>
<tr>
<td>
<p>detail.logid</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考获取帮助和技术支持。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_id&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;transcriptions.updated&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;input_audio&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;format&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;pcm&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;codec&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;pcm&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;sample_rate&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">24000</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;channel&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;bit_depth&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">16</span>
      <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;20241210152726467C48D89D6DB2F3***&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_id&quot;,
  &quot;event_type&quot;: &quot;transcriptions.updated&quot;,
  &quot;data&quot;: {
      &quot;input_audio&quot;: {
          &quot;format&quot;: &quot;pcm&quot;,
          &quot;codec&quot;: &quot;pcm&quot;,
          &quot;sample_rate&quot;: 24000,
          &quot;channel&quot;: 1,
          &quot;bit_depth&quot;: 16
      }
  },
  &quot;detail&quot;: {
      &quot;logid&quot;: &quot;20241210152726467C48D89D6DB2F3***&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h3 id="8d747148" tabindex="-1">音频提交完成</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>input_audio_buffer.completed</code></p>
</li>
<li>
<p><strong>事件说明</strong>：流式提交的音频完成后，返回此事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>客户端自行生成的事件 ID，方便定位问题。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>input_audio_buffer.completed</code>。</p>
</td>
</tr>
<tr>
<td>
<p>detail</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件详情。</p>
</td>
</tr>
<tr>
<td>
<p>detail.logid</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考获取帮助和技术支持。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_id&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;input_audio_buffer.completed&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;20241210152726467C48D89D6DB2F3***&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_id&quot;,
  &quot;event_type&quot;: &quot;input_audio_buffer.completed&quot;,
  &quot;detail&quot;: {
      &quot;logid&quot;: &quot;20241210152726467C48D89D6DB2F3***&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h3 id="8211875b" tabindex="-1">音频清除成功</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>input_audio_buffer.cleared</code></p>
</li>
<li>
<p><strong>事件说明</strong>：清除缓冲区音频成功后，返回此事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>客户端自行生成的事件 ID，方便定位问题。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>input_audio_buffer.cleared</code>。</p>
</td>
</tr>
<tr>
<td>
<p>detail</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件详情。</p>
</td>
</tr>
<tr>
<td>
<p>detail.logid</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考获取帮助和技术支持。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-Python">{
    <span class="hljs-string">&quot;id&quot;</span>: <span class="hljs-string">&quot;event_id&quot;</span>,
    <span class="hljs-string">&quot;event_type&quot;</span>: <span class="hljs-string">&quot;input_audio_buffer.cleared&quot;</span>,
    <span class="hljs-string">&quot;detail&quot;</span>: {
        <span class="hljs-string">&quot;logid&quot;</span>: <span class="hljs-string">&quot;20241210152726467C48D89D6DB2F3***&quot;</span>
    }
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;id&quot;: &quot;event_id&quot;,
    &quot;event_type&quot;: &quot;input_audio_buffer.cleared&quot;,
    &quot;detail&quot;: {
        &quot;logid&quot;: &quot;20241210152726467C48D89D6DB2F3***&quot;
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h3 id="772e6d2d" tabindex="-1">识别出文字</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>transcriptions.message.update</code></p>
</li>
<li>
<p><strong>事件说明</strong>：语音识别出文字后，返回此事件，每次都返回全量的识别出来的文字。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>客户端自行生成的事件 ID，方便定位问题。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>transcriptions.message.update</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件数据，包含识别出的文字。</p>
</td>
</tr>
<tr>
<td>
<p>data.content</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>识别出的文字。</p>
</td>
</tr>
<tr>
<td>
<p>detail</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件详情。</p>
</td>
</tr>
<tr>
<td>
<p>detail.logid</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考获取帮助和技术支持。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_id&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;transcriptions.message.update&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;text&quot;</span>
  <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;20241210152726467C48D89D6DB2F3***&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_id&quot;,
  &quot;event_type&quot;: &quot;transcriptions.message.update&quot;,
  &quot;data&quot;: {
      &quot;content&quot;: &quot;text&quot;
  },
  &quot;detail&quot;: {
      &quot;logid&quot;: &quot;20241210152726467C48D89D6DB2F3***&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h3 id="0c36158c" tabindex="-1">识别完成</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>transcriptions.message.completed</code></p>
</li>
<li>
<p><strong>事件说明</strong>：语音识别完成后，返回此事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>客户端自行生成的事件 ID，方便定位问题。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>transcriptions.message.completed</code>。</p>
</td>
</tr>
<tr>
<td>
<p>detail</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件详情。</p>
</td>
</tr>
<tr>
<td>
<p>detail.logid</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考获取帮助和技术支持。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-HTTP">{
  &quot;id&quot;: &quot;event_id&quot;,
  &quot;event_type&quot;: &quot;transcriptions.message.completed&quot;,
  &quot;detail&quot;: {
      &quot;logid&quot;: &quot;20241210152726467C48D89D6DB2F3***&quot;
  }
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_id&quot;,
  &quot;event_type&quot;: &quot;transcriptions.message.completed&quot;,
  &quot;detail&quot;: {
      &quot;logid&quot;: &quot;20241210152726467C48D89D6DB2F3***&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h3 id="06be77c0" tabindex="-1">发生错误</h3>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>error</code></p>
</li>
<li>
<p><strong>事件说明</strong>：识别过程中的错误事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>是否必选</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>服务端生成的唯一 ID。</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 <code>error</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件数据，包含错误信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.code</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>错误码。</p>
</td>
</tr>
<tr>
<td>
<p>data.msg</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>错误信息。</p>
</td>
</tr>
<tr>
<td>
<p>detail</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>事件详情。</p>
</td>
</tr>
<tr>
<td>
<p>detail.logid</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考获取帮助和技术支持。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_1&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;error&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;发生异常&quot;</span>
  <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;20241210152726467C48D89D6DB2F3***&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;error&quot;,
  &quot;data&quot;: {
      &quot;code&quot;: 1,
      &quot;msg&quot;: &quot;发生异常&quot;
  },
  &quot;detail&quot;: {
      &quot;logid&quot;: &quot;20241210152726467C48D89D6DB2F3***&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/developer_guides_asr_api" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">双向流式语音识别</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/developer_guides_tts_api" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">双向流式语音合成</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="上行事件" href="#3482fcbd" data-href="#3482fcbd">上行事件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="更新语音识别配置" href="#a7ca67ab" data-href="#a7ca67ab">更新语音识别配置</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="流式上传音频片段" href="#9ef6e6ca" data-href="#9ef6e6ca">流式上传音频片段</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="提交音频" href="#f5d76c87" data-href="#f5d76c87">提交音频</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="清除缓冲区音频" href="#e98db543" data-href="#e98db543">清除缓冲区音频</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="下行事件" href="#9f1a57d6" data-href="#9f1a57d6">下行事件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="连接成功" href="#06d772a3" data-href="#06d772a3">连接成功</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="配置更新成功" href="#3f842df1" data-href="#3f842df1">配置更新成功</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="音频提交完成" href="#8d747148" data-href="#8d747148">音频提交完成</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="音频清除成功" href="#8211875b" data-href="#8211875b">音频清除成功</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="识别出文字" href="#772e6d2d" data-href="#772e6d2d">识别出文字</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="识别完成" href="#0c36158c" data-href="#0c36158c">识别完成</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="发生错误" href="#06be77c0" data-href="#06be77c0">发生错误</a></div></div></div></div></div></div></div></div>
</body></html>