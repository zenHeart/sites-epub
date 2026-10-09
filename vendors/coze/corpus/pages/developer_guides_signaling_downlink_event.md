<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">Realtime 下行事件</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/5956.1729cb00c0.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.ca52691239.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/developer_guides_signaling_downlink_event"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/developer_guides_signaling_downlink_event.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
  
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/developer_guides_signaling_downlink_event" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b97434bdbc784e3ce84ce" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a55df9a4bdbc784e3c9738f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf30d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf317" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf31d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf325" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf334" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf32e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf35a" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf362" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8e614bdbc784e3cce185" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3e2c" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3ece" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_coze_api_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="API 介绍">API 介绍</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ed4" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_changelog" data-discover="true"><span class="nodeTitle-ONnqtP" title="更新日志">更新日志</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3edc" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_preparation" data-discover="true"><span class="nodeTitle-ONnqtP" title="准备工作">准备工作</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ee3" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_api_playground" data-discover="true"><span class="nodeTitle-ONnqtP" title="API Playground">API Playground</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e32" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="鉴权">鉴权</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e6a" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能体和应用">智能体和应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ee9" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="工作空间">工作空间</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3eef" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="文件夹">文件夹</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ef7" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="企业/组织">企业/组织</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3efe" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="会话与消息">会话与消息</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f04" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="对话">对话</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f0c" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f13" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="文件">文件</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f1a" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能音视频">智能音视频</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3f20" class="nodeWrapper-woTZn5" data-tree-level="3"><div to="/" class="nodeContent-GigwSX" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="ASR、TTS 与音色">ASR、TTS 与音色</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f27" class="nodeWrapper-woTZn5" data-tree-level="3"><div to="/" class="nodeContent-GigwSX" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="RTC 语音">RTC 语音</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc41b7" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX" style="margin-left:72px" href="/developer_guides_create_room" data-discover="true"><span class="nodeTitle-ONnqtP" title="创建房间">创建房间</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4220" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX" style="margin-left:72px" href="/developer_guides_signaling_uplink_event" data-discover="true"><span class="nodeTitle-ONnqtP" title="Realtime 上行事件">Realtime 上行事件</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4228" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:72px" href="/developer_guides_signaling_downlink_event" data-discover="true"><span class="nodeTitle-ONnqtP" title="Realtime 下行事件">Realtime 下行事件</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc422e" class="nodeWrapper-woTZn5" data-tree-level="4"><a class="nodeContent-GigwSX" style="margin-left:72px" href="/developer_guides_realtime_error_codes" data-discover="true"><span class="nodeTitle-ONnqtP" title="Realtime 事件错误码">Realtime 事件错误码</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f2e" class="nodeWrapper-woTZn5" data-tree-level="3"><div to="/" class="nodeContent-GigwSX" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="WebSocket 语音">WebSocket 语音</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc42a6" class="nodeWrapper-woTZn5" data-tree-level="3"><div to="/" class="nodeContent-GigwSX" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="声纹识别">声纹识别</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f35" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="知识库">知识库</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f3b" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="数据库">数据库</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f43" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="插件">插件</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f49" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="变量">变量</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f51" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="渠道">渠道</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f58" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="用量限额">用量限额</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f5f" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="账单与权益">账单与权益</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f66" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="回调">回调</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f84" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_coze_error_codes" data-discover="true"><span class="nodeTitle-ONnqtP" title="错误码">错误码</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f99" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="API 教程">API 教程</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f8a" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_api_faq" data-discover="true"><span class="nodeTitle-ONnqtP" title="API 常见问题">API 常见问题</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fa8" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc529d" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8e4bdbc784e3cc445f" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/developer_guides_coze_cli" data-discover="true"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf33f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf369" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/guides_FAQ" data-discover="true"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>API 参考</span><span class="separator-KB9yMa">/</span><span>智能音视频</span><span class="separator-KB9yMa">/</span><span>RTC 语音</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">Realtime 下行事件</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">Realtime 下行事件</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg><span>复制页面</span></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>本文介绍扣子编程智能语音信令事件中的下行事件。</p>
<h2 id="2a980f88" tabindex="-1">房间配置成功</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>session.created</code></p>
</li>
<li>
<p><strong>事件说明</strong>：用户成功进房后会发送此事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 104,100,100,411 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 104px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 411px;" /></colgroup><thead>
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
<p>固定为<code>session.created</code>。</p>
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
<p>事件数据，包含对话的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.voice_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>音色 ID。</p>
</td>
</tr>
<tr>
<td>
<p>data.log_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>服务端日志 ID，用于查找问题。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7446668538246561800&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;session.created&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;voice_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;134&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;log_id&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;xxx&quot;</span>
    <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;id&quot;: &quot;7446668538246561800&quot;,
    &quot;event_type&quot;: &quot;session.created&quot;,
    &quot;data&quot;: {
        &quot;voice_id&quot;: &quot;134&quot;,
        &quot;log_id&quot;:&quot;xxx&quot;
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="5c7c0c03" tabindex="-1">房间配置更新成功</h2>
<ul data-style="0">
<li><strong>事件类型</strong>：<code>session.updated</code></li>
<li><strong>事件说明</strong>：房间内的配置更新成功，返回房间内最新的配置。</li>
<li><strong>事件结构</strong>：</li>
</ul>
<!-- @cols-width: 186,115,100,453 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 186px;" /><col style="width: 115px;" /><col style="width: 100px;" /><col style="width: 453px;" /></colgroup><thead>
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
<p>固定为<code>session.updated</code>。</p>
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
<p>事件数据，包含对话的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.voice_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>音色 ID。</p>
</td>
</tr>
<tr>
<td>
<p>data.speech_rate</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>模型回复的语速，取值范围 [-50, 100]，默认为 0。-50 表示 0.5 倍速，100 表示 2 倍速。</p>
</td>
</tr>
<tr>
<td>
<p>data.loudness_rate</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>输出音频的音量，取值范围 [-50, 100]，默认为 0。-50 表示 0.5 倍音量，100 表示 2 倍音量。</p>
</td>
</tr>
<tr>
<td>
<p>data.longest_silence_ms</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>当智能体处于长时间沉默状态时，房间将自动解散。此时间以毫秒（ms）为单位计量，默认时长为 180,000 毫秒。</p>
</td>
</tr>
<tr>
<td>
<p>data.event_subscriptions</p>
</td>
<td>
<p>Array<String></p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>订阅的下行事件的事件类型列表。</p>
</td>
</tr>
<tr>
<td>
<p>data.chat_config</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>聊天配置信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.chat_config.meta_data</p>
</td>
<td>
<p>Map&lt;String, String&gt;</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>附加信息，通常用于封装一些业务相关的字段。查看对话消息详情时，系统会透传此附加信息。自定义键值对，应指定为 Map 对象格式。长度为 16 对键值对，其中键（key）的长度范围为 1～64 个字符，值（value）的长度范围为 1～512 个字符。</p>
</td>
</tr>
<tr>
<td>
<p>data.chat_config.custom_variables</p>
</td>
<td>
<p>Map&lt;String, String&gt;</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>智能体中定义的变量。在智能体 prompt 中设置变量 {{key}} 后，可以通过该参数传入变量值，同时支持 Jinja2 语法。变量名只支持英文字母和下划线。</p>
</td>
</tr>
<tr>
<td>
<p>data.chat_config.extra_params</p>
</td>
<td>
<p>Map&lt;String, String&gt;</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>附加参数，通常用于特殊场景下指定一些必要参数供模型判断，例如指定经纬度，并询问智能体此位置的天气。自定义键值对格式，其中键（key）仅支持设置为：</p>
<ul data-style="0">
<li>latitude（纬度，值为纬度值，例如 39.9800718）</li>
<li>longitude（经度，值为经度值，例如 116.309314）。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.chat_config.plugin_interrupt_mode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>端插件执行模式，可选值有 <code>blocking</code> / <code>nonblocking</code>，默认为 <code>nonblocking</code>。</p>
<ul data-style="0">
<li><code>blocking</code> 模式下，遇到端插件执行后，会阻塞后续的对话，直到提交端插件结果。</li>
<li><code>nonblocking</code> 模式下，遇到端插件执行后，若未提交端插件结果继续对话，则端插件请求会被丢弃。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.chat_config.allow_voice_interrupt</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>是否打开语音打断功能，默认为 <code>true</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data.chat_config.interrupt_config</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>语音打断配置，仅在 allow_voice_interrupt 为<code>true</code>时生效</p>
</td>
</tr>
<tr>
<td>
<p>data.chat_config.interrupt_config.mode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>语音打断模式，可选值有<code>all</code> / <code>keyword_contains</code> / <code>keyword_prefix</code>，默认为<code>all</code>。</p>
<ul data-style="0">
<li><code>all</code>模式下，任意内容都可以打断模型回复。</li>
<li><code>keyword_contains</code>模式下，说话内容<strong>包含</strong>关键词才会打断模型回复。</li>
<li><code>keyword_prefix</code>模式下，说话内容<strong>前缀匹配</strong>关键词才会打断模型回复。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.chat_config.interrupt_config.keywords</p>
</td>
<td>
<p>Array<String></p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>关键词列表，每个关键词长度不超过8个字，最多10个关键词，仅在<code>keyword_contains</code>/<code>keyword_prefix</code>模式下生效。</p>
</td>
</tr>
<tr>
<td>
<p>data.turn_detection</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>声音检测配置。</p>
</td>
</tr>
<tr>
<td>
<p>data.turn_detection.type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>语音检测模式，默认为 <code>server_vad</code>，可选项包括：</p>
<ul data-style="0">
<li><code>server_vad</code>：语音活动检测由扣子编程服务端完成，客户端将音频流持续发送到服务端，服务端在接收到音频后，通过服务端 VAD 检测语音的开始和结束。</li>
<li><code>client_vad</code>：客户端使用自己的 VAD 检测语音的开始和结束，并将检测到的语音片段发送到服务器进行识别。</li>
<li><code>semantic_vad</code>：采用语义判停的自由对话模式（<strong>此功能仅对企业旗舰版用户开放</strong>），由服务端识别语义来判断是否停止说话。</li>
</ul>
<p>详细的检测逻辑请参见<a href="/dev_how_to_guides/realtime_faq#044b8bcc" target="_blank">如何设置扣子的语音检测模式？</a>。</p>
</td>
</tr>
<tr>
<td>
<p>data.turn_detection.silence_duration_ms</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p><code>server_vad</code> 模式下，检测语音停止的静音持续时间，单位为 ms。默认为 500ms。</p>
</td>
</tr>
<tr>
<td>
<p>data.turn_detection.semantic_vad_config</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p><code>semantic_vad</code> 模式下，配置判定语音停止的语义检测策略。</p>
</td>
</tr>
<tr>
<td>
<p>data.turn_detection.semantic_vad_config.silence_threshold_ms</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>当用户暂停说话时，持续静音多久后，触发语义判停检测。单位为 ms。默认为 300ms。</p>
</td>
</tr>
<tr>
<td>
<p>data.turn_detection.semantic_vad_config.semantic_unfinished_wait_time_ms</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>当语义检测判断该语句未结束时，持续静音多久后，扣子编程认定语音结束。单位为 ms。默认为 500ms。</p>
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
<ul data-style="0">
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
<p>将语音转为文本时，是否启用顺滑，默认为 <code>true</code>。</p>
<ul data-style="0">
<li><code>true</code>：系统在进行语音处理时，会去掉识别结果中诸如 “啊”“嗯” 等语气词，使得输出的文本语义更加流畅自然，符合正常的语言表达习惯，尤其适用于对文本质量要求较高的场景，如正式的会议记录、新闻稿件生成等。</li>
<li><code>false</code>：系统不会对识别结果中的语气词进行处理，识别结果会保留原始的语气词。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.enable_nostream</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>当前是否开启<strong>二次识别模式</strong>，枚举值：</p>
<ul data-style="0">
<li><code>true</code>：已开启二次识别模式。会实时返回逐字识别的文本；当一句话结束时，会结合整句音频进行上下文分析并重新识别，生成优化后的识别结果并返回。这种机制既能满足客户实时上屏的需求，又能确保最终结果的识别准确率。</li>
<li><code>false</code>：未开启二次识别模式。仅进行一次实时识别，逐字返回文本，不会在一句话结束时重新识别分句，可能存在一定的识别误差。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.enable_emotion</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>当前是否开启说话人情绪识别功能，枚举值：</p>
<ul data-style="0">
<li><code>true</code>：已开启情绪识别，会返回说话人的情绪标签，仅在 <code>data.asr_config.stream_mode</code> 为 <code>output_no_stream</code> 时生效。</li>
<li><code>false</code>：未开启情绪识别。</li>
</ul>
<p>支持的情绪标签包括：</p>
<ul data-style="0">
<li><code>angry</code>：表示情绪为生气</li>
<li><code>happy</code>：表示情绪为开心</li>
<li><code>neutral</code>：表示情绪为平静或中性</li>
<li><code>sad</code>：表示情绪为悲伤</li>
<li><code>surprise</code>：表示情绪为惊讶</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.enable_gender</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>当前是否开启说话人性别识别功能，枚举值：</p>
<ul data-style="0">
<li><code>true</code>：已开启性别识别，会返回说话人性别（<code>male</code>/<code>female</code>），仅在 <code>data.asr_config.stream_mode</code> 为 <code>output_no_stream</code> 时生效。</li>
<li><code>false</code>：未开启性别识别。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.sensitive_words_filter</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>当前敏感词过滤功能的配置状态，支持以下 3 种过滤方式：</p>
<ul data-style="0">
<li>过滤系统敏感词，并替换为<code>*</code>。</li>
<li>过滤自定义敏感词，并替换为空。</li>
<li>过滤自定义敏感词，并替换为<code>*</code>。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.sensitive_words_filter.system_reserved_filter</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>当前是否启用系统自带敏感词过滤（匹配到的敏感词替换为<code>*</code>），枚举值：</p>
<ul data-style="0">
<li><code>true</code>：已启用，系统会过滤系统自带敏感词（主要包含限制级词汇）并替换为<code>*</code>。</li>
<li><code>false</code>：未启用系统自带敏感词的过滤。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.sensitive_words_filter.filter_with_empty</p>
</td>
<td>
<p>Array<string></p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>自定义的需替换为空的敏感词列表。</p>
</td>
</tr>
<tr>
<td>
<p>data.asr_config.sensitive_words_filter.filter_with_signed</p>
</td>
<td>
<p>Array<string></p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>自定义的需替换为 <code>*</code> 的敏感词列表。</p>
</td>
</tr>
<tr>
<td>
<p>data.voice_print_config</p>
</td>
<td>
<p>Array<String></p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>声纹识别配置。</p>
</td>
</tr>
<tr>
<td>
<p>data.voice_print_config.group_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>声纹组 ID。语音通话时，扣子编程会在该声纹组内进行查找匹配对应的声纹，当声纹匹配度高于 <code>score</code> 阈值，则认为是同一个人的声音。</p>
</td>
</tr>
<tr>
<td>
<p>data.voice_print_config.score</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>声纹匹配的命中阈值，即声音匹配度的最低标准。当声音匹配度达到或超过该阈值时，扣子编程才会认定声纹匹配成功。你可以根据应用的安全性要求进行自定义设置。如果匹配了多轮声纹，扣子编程会取相似度最高的一个。<br>
取值范围：0~100，默认值：40。</p>
</td>
</tr>
<tr>
<td>
<p>data.voice_print_config.reuse_voice_info</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>当本轮对话未命中任何声纹时，是否沿用历史声纹信息。默认为 <code>false</code>。</p>
<ul data-style="0">
<li><code>true</code>：未命中声纹时，智能体将返回上一次命中的声纹。适用于连续对话场景，当收音不好等情况导致声纹没能正确被识别时，保障对话的连贯性。</li>
<li><code>false</code>：未命中声纹时，智能体返回空的声纹信息。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.voice_processing_config</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>语音降噪配置。默认不启用降噪。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>仅扣子企业旗舰版支持该配置。</p>
</div>
</td>
</tr>
<tr>
<td>
<p>data.voice_processing_config.enable_ans</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>主动噪声抑制。自动识别并过滤掉背景环境中的各种噪音（如键盘声、空调声、街道嘈杂声），让说话者的声音更清晰。<br>
此功能与下面的 <code>enable_pdns</code>（声纹降噪）只能<strong>二选一开启</strong>，不能同时使用。</p>
</td>
</tr>
<tr>
<td>
<p>data.voice_processing_config.enable_pdns</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>声纹降噪。专门针对<strong>特定说话人</strong>的声音进行优化，能更精准地保留目标人声。<br>
此功能与上面的 <code>enable_ans</code>只能<strong>二选一开启</strong>，不能同时使用。<br>
提供两种模式，你可以根据需要选择：</p>
<ul data-style="0">
<li>自动提取：设置简单，开箱即用。默认为该模式。<strong>降噪生效稍微有延迟</strong>，服务端需要先听你说一会儿话才能提取出你的声纹特征，在此期间降噪效果可能不佳。另外，提取声纹会受到用户说话场景影响，准确性上可能会弱于主动设置。</li>
<li>主动设置：<strong>降噪效果更精准、更快速</strong>，在对话开始时就立即生效。不过需要提前录制声纹并在 <code>voice_print_feature_id</code> 中设置声纹 ID。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.voice_print_config.feature_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>目标说话人的声纹 ID。当你选择开启 <code>enable_pdns</code>（声纹降噪）并希望使用<strong>主动设置</strong>模式时，需要在此处填入你提前录制好的声纹 ID。</p>
</td>
</tr>
</tbody>
</table>
</div><ul data-style="0">
<li><strong>事件示例</strong>：
<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7446668538246561890&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;session.update&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;voice_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span> <span class="hljs-comment">// 音色 ID</span>
        <span class="hljs-attr">&quot;speech_rate&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span> <span class="hljs-comment">// [-50, 100]</span>
        <span class="hljs-attr">&quot;longest_silence_ms&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">180000</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;event_subscriptions&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;chat_config&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;meta_data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;a&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span>
            <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;custom_variables&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;a&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span>
            <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;extra_params&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;a&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span>
            <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;allow_voice_interrupt&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">true</span></span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;interrupt_config&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;mode&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;keyword_prefix&quot;</span><span class="hljs-punctuation">,</span>
                <span class="hljs-attr">&quot;keyword&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">&quot;扣子&quot;</span><span class="hljs-punctuation">]</span>
            <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;plugin_interrupt_mode&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;nonblocking&quot;</span> <span class="hljs-comment">// 控制收到端插件执行中断信号后，没有提交端执行请求时的模型</span>
            <span class="hljs-comment">// 端插件的执行模型，默认不阻塞，blocking/nonblocking，阻塞的场景如果不提交端执行请求就会让语音链路一直block住</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;turn_detection&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;server_vad&quot;</span> <span class="hljs-comment">// server_vad/client_vad</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;asr_config&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;hot_words&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">&quot;扣子&quot;</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;enable_itn&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">true</span></span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;enable_punc&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">true</span></span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;enable_ddc&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">true</span></span>
        <span class="hljs-punctuation">}</span> 
    <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;id&quot;: &quot;7446668538246561890&quot;,
    &quot;event_type&quot;: &quot;session.update&quot;,
    &quot;data&quot;: {
        &quot;voice_id&quot;: &quot;123&quot;, // 音色 ID
        &quot;speech_rate&quot;: 0, // [-50, 100]
        &quot;longest_silence_ms&quot;: 180000,
        &quot;event_subscriptions&quot;: [],
        &quot;chat_config&quot;: {
            &quot;meta_data&quot;: {
                &quot;a&quot;: &quot;123&quot;
            },
            &quot;custom_variables&quot;: {
                &quot;a&quot;: &quot;123&quot;
            },
            &quot;extra_params&quot;: {
                &quot;a&quot;: &quot;123&quot;
            },
            &quot;allow_voice_interrupt&quot;: true,
            &quot;interrupt_config&quot;: {
                &quot;mode&quot;: &quot;keyword_prefix&quot;,
                &quot;keyword&quot;: [&quot;扣子&quot;]
            },
            &quot;plugin_interrupt_mode&quot;: &quot;nonblocking&quot; // 控制收到端插件执行中断信号后，没有提交端执行请求时的模型
            // 端插件的执行模型，默认不阻塞，blocking/nonblocking，阻塞的场景如果不提交端执行请求就会让语音链路一直block住
        },
        &quot;turn_detection&quot;: {
            &quot;type&quot;: &quot;server_vad&quot; // server_vad/client_vad
        },
        &quot;asr_config&quot;: {
            &quot;hot_words&quot;: [&quot;扣子&quot;],
            &quot;enable_itn&quot;: true,
            &quot;enable_punc&quot;: true,
            &quot;enable_ddc&quot;: true
        } 
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="0a12551c" tabindex="-1">会话创建成功</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>conversation.created</code></p>
</li>
<li>
<p><strong>事件说明</strong>：用户成功进房后会发送此事件，收到此事件即表明<strong>房间初始化完成。</strong></p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 160,100,100,441 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 160px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 441px;" /></colgroup><thead>
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
<p>固定为<code>conversation.created</code>。</p>
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
<p>事件数据，包含对话的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.conversation_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>会话 ID，整个房间的交互都会发生在此会话下。</p>
</td>
</tr>
<tr>
<td>
<p>data.prologue</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>智能体的开场白。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7446668538246561891&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.created&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;prologue&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span>
    <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;id&quot;: &quot;7446668538246561891&quot;,
    &quot;event_type&quot;: &quot;conversation.created&quot;,
    &quot;data&quot;: {
        &quot;conversation_id&quot;: &quot;123&quot;,
        &quot;prologue&quot;: &quot;&quot;
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="b5369292" tabindex="-1">对话开始</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>conversation.chat.created</code></p>
</li>
<li>
<p><strong>事件说明</strong>：创建对话的事件，表示对话开始。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 185,111,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 185px;" /><col style="width: 111px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
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
<p>固定为conversation.chat.created。</p>
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
<p>事件数据，包含对话的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>对话 ID，即对话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.conversation_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>会话 ID，即会话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.bot_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>要进行会话聊天的智能体 ID。</p>
</td>
</tr>
<tr>
<td>
<p>data.created_at</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话创建的时间。格式为 10 位的 Unixtime 时间戳，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>data.last_error</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话运行异常时，此字段中返回详细的错误信息，包括：</p>
<ul data-style="1">
<li>Code：错误码。Integer 类型。0 表示成功，其他值表示失败。</li>
<li>Msg：错误信息。String 类型。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.meta_data</p>
</td>
<td>
<p>Map&lt;String, String&gt;</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>创建消息时的附加消息，用于传入使用方的自定义数据，获取消息时也会返回此附加消息。自定义键值对，应指定为 Map 对象格式。长度为 16 对键值对，其中键（key）的长度范围为 1～64 个字符，值（value）的长度范围为 1～512 个字符。</p>
</td>
</tr>
<tr>
<td>
<p>data.status</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的运行状态。取值为 created，即对话已创建。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的 Token 使用情况。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.token_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>本次对话消耗的 Token 总数，包括 input 和 output 部分的消耗。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.output_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>output 部分消耗的 Token 总数。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.input_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>input 部分消耗的 Token 总数。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7446668538246561892&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.chat.created&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;222&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;created_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1710348675</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;completed_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">null</span></span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;last_error&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">null</span></span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;meta_data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;status&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;created&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;usage&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">null</span></span>
  <span class="hljs-punctuation">}</span>    
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;7446668538246561892&quot;,
  &quot;event_type&quot;: &quot;conversation.chat.created&quot;,
  &quot;data&quot;: {
      &quot;id&quot;: &quot;123&quot;,
      &quot;conversation_id&quot;: &quot;123&quot;,
      &quot;bot_id&quot;: &quot;222&quot;,
      &quot;created_at&quot;: 1710348675,
      &quot;completed_at&quot;: null,
      &quot;last_error&quot;: null,
      &quot;meta_data&quot;: {},
      &quot;status&quot;: &quot;created&quot;,
      &quot;usage&quot;: null
  }    
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="1f5f6f91" tabindex="-1">对话处理中</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>conversation.chat.in_progress</code></p>
</li>
<li>
<p><strong>事件说明</strong>：服务端正在处理对话。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 184,152,100,404 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 184px;" /><col style="width: 152px;" /><col style="width: 100px;" /><col style="width: 404px;" /></colgroup><thead>
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
<p>固定为conversation.chat.in_progress。</p>
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
<p>事件数据，包含对话的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>对话 ID，即对话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.conversation_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>会话 ID，即会话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.bot_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>要进行会话聊天的智能体 ID。</p>
</td>
</tr>
<tr>
<td>
<p>data.created_at</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话创建的时间。格式为 10 位的 Unixtime 时间戳，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>data.last_error</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话运行异常时，此字段中返回详细的错误信息，包括：</p>
<ul data-style="1">
<li>Code：错误码。Integer 类型。0 表示成功，其他值表示失败。</li>
<li>Msg：错误信息。String 类型。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.meta_data</p>
</td>
<td>
<p>Map&lt;String, String&gt;</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>创建消息时的附加消息，用于传入使用方的自定义数据，获取消息时也会返回此附加消息。自定义键值对，应指定为 Map 对象格式。长度为 16 对键值对，其中键（key）的长度范围为 1～64 个字符，值（value）的长度范围为 1～512 个字符。</p>
</td>
</tr>
<tr>
<td>
<p>data.status</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的运行状态。取值为 in_progress，即智能体正在处理中。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的 Token 使用情况。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.token_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>本次对话消耗的 Token 总数，包括 input 和 output 部分的消耗。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.output_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>output 部分消耗的 Token 总数。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.input_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>input 部分消耗的 Token 总数。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>事件示例</strong>：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7446668538246561892&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.chat.in_progress&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;222&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;created_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1710348675</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;completed_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">null</span></span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;last_error&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">null</span></span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;meta_data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;status&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;in_progress&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;usage&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">null</span></span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;7446668538246561892&quot;,
  &quot;event_type&quot;: &quot;conversation.chat.in_progress&quot;,
  &quot;data&quot;: {
      &quot;id&quot;: &quot;123&quot;,
      &quot;conversation_id&quot;: &quot;123&quot;,
      &quot;bot_id&quot;: &quot;222&quot;,
      &quot;created_at&quot;: 1710348675,
      &quot;completed_at&quot;: null,
      &quot;last_error&quot;: null,
      &quot;meta_data&quot;: {},
      &quot;status&quot;: &quot;in_progress&quot;,
      &quot;usage&quot;: null
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="17fc454e" tabindex="-1">增量消息</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>conversation.message.delta</code></p>
</li>
<li>
<p><strong>事件说明</strong>：增量消息，通常是 <code>type=answer</code> 时的增量消息。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 160,152,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 160px;" /><col style="width: 152px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
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
<p>固定为<code>conversation.message.delta</code>。</p>
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
<p>事件数据，包含消息的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>Message ID，即消息的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.conversation_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>此消息所在的会话 ID。</p>
</td>
</tr>
<tr>
<td>
<p>data.bot_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>编写此消息的智能体 ID。此参数仅在对话产生的消息中返回。</p>
</td>
</tr>
<tr>
<td>
<p>data.chat_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>Chat ID。此参数仅在对话产生的消息中返回。</p>
</td>
</tr>
<tr>
<td>
<p>data.meta_data</p>
</td>
<td>
<p>Map&lt;String, String&gt;</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>创建消息时的附加消息，获取消息时也会返回此附加消息。</p>
</td>
</tr>
<tr>
<td>
<p>data.role</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>发送这条消息的实体。取值：<code>user</code>（代表该条消息内容是用户发送的）、<code>assistant</code>（代表该条消息内容是智能体发送的）。</p>
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
<p>消息的内容，支持纯文本、多模态（文本、图片、文件混合输入）、卡片等多种类型的内容。</p>
</td>
</tr>
<tr>
<td>
<p>data.content_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>消息内容的类型，取值包括：</p>
<ul data-style="1">
<li>text：文本。</li>
<li>object_string：多模态内容，即文本和文件的组合、文本和图片的组合。</li>
<li>card：卡片。此枚举值仅在接口响应中出现，不支持作为入参。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>消息类型。</p>
<ul data-style="1">
<li><strong>question</strong>：用户输入内容。</li>
<li><strong>answer</strong>：智能体返回给用户的消息内容，支持增量返回。如果工作流绑定了 messge 节点，可能会存在多 answer 场景，此时可以用流式返回的结束标志来判断所有 answer 完成。</li>
<li><strong>function_call</strong>：智能体对话过程中调用函数（function call）的中间结果。</li>
<li><strong>tool_output</strong>：调用工具 （function call）后返回的结果。</li>
<li><strong>tool_response</strong>：调用工具 （function call）后返回的结果。</li>
<li><strong>follow_up</strong>：如果在智能体上配置打开了用户问题建议开关，则会返回推荐问题相关的回复内容。</li>
<li><strong>verbose</strong>：多 answer 场景下，服务端会返回一个 verbose 包，对应的 content 为 JSON 格式，content.msg_type =generate_answer_finish 代表全部 answer 回复完成。</li>
</ul>
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
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.message.delta&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;msg_006&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;assistant&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;answer&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;你好你好&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;222&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;conversation.message.delta&quot;,
  &quot;data&quot;: {
      &quot;id&quot;: &quot;msg_006&quot;,
      &quot;role&quot;: &quot;assistant&quot;,
      &quot;type&quot;: &quot;answer&quot;,
      &quot;content&quot;: &quot;你好你好&quot;,
      &quot;content_type&quot;: &quot;text&quot;,
      &quot;chat_id&quot;: &quot;123&quot;,
      &quot;conversation_id&quot;: &quot;123&quot;,
      &quot;bot_id&quot;: &quot;222&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="aa18a150" tabindex="-1">消息已完成</h2>
<ul data-style="0">
<li><strong>事件类型</strong>：<code>conversation.message.completed</code></li>
<li><strong>事件说明</strong>：消息已完成（用户或智能体）。此时事件中带有所有 <code>message.delta</code> 的拼接结果，且每个消息均为 <code>completed</code> 状态。</li>
<li><strong>事件结构</strong>：</li>
</ul>
<!-- @cols-width: 160,152,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 160px;" /><col style="width: 152px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
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
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>服务端生成的唯一 ID</p>
</td>
</tr>
<tr>
<td>
<p>event_type</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为<code>conversation.message.completed</code></p>
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
<p>事件数据，包含消息的详细信息</p>
</td>
</tr>
<tr>
<td>
<p>data.id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>Message ID，即消息的唯一标识</p>
</td>
</tr>
<tr>
<td>
<p>data.conversation_id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>此消息所在的会话 ID</p>
</td>
</tr>
<tr>
<td>
<p>data.bot_id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>编写此消息的智能体ID。此参数仅在对话产生的消息中返回</p>
</td>
</tr>
<tr>
<td>
<p>data.chat_id</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>Chat ID。此参数仅在对话产生的消息中返回</p>
</td>
</tr>
<tr>
<td>
<p>data.meta_data</p>
</td>
<td>
<p>map&lt;string,string&gt;</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>创建消息时的附加消息，获取消息时也会返回此附加消息</p>
</td>
</tr>
<tr>
<td>
<p>data.role</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>发送这条消息的实体。取值：<code>user</code>（代表该条消息内容是用户发送的）、<code>assistant</code>（代表该条消息内容是智能体发送的）</p>
</td>
</tr>
<tr>
<td>
<p>data.content</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>消息的内容，支持纯文本、多模态（文本、图片、文件混合输入）、卡片等多种类型的内容</p>
</td>
</tr>
<tr>
<td>
<p>data.content_type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>消息内容的类型，取值包括：</p>
<ul data-style="0">
<li>text：文本。</li>
<li>object_string：多模态内容，即文本和文件的组合、文本和图片的组合。</li>
<li>card：卡片。此枚举值仅在接口响应中出现，不支持作为入参。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>消息类型。</p>
<ul data-style="0">
<li><strong>question</strong>：用户输入内容。</li>
<li><strong>answer</strong>：智能体返回给用户的消息内容，支持增量返回。如果工作流绑定了 messge 节点，可能会存在多 answer 场景，此时可以用流式返回的结束标志来判断所有 answer 完成。</li>
<li><strong>function_call</strong>：智能体对话过程中调用函数（function call）的中间结果。</li>
<li><strong>tool_output</strong>：调用工具 （function call）后返回的结果。</li>
<li><strong>tool_response</strong>：调用工具 （function call）后返回的结果。</li>
<li><strong>follow_up</strong>：如果在智能体上配置打开了用户问题建议开关，则会返回推荐问题相关的回复内容。</li>
<li><strong>verbose</strong>：多 answer 场景下，服务端会返回一个 verbose 包，对应的 content 为 JSON 格式，content.msg_type =generate_answer_finish 代表全部 answer 回复完成。</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><ul data-style="0">
<li>事件示例：</li>
</ul>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_1&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.message.completed&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;msg_002&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;role&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;assistant&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;function_call&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;{\&quot;name\&quot;:\&quot;toutiaosousuo-search\&quot;,\&quot;arguments\&quot;:{\&quot;cursor\&quot;:0,\&quot;input_query\&quot;:\&quot;今天的体育新闻\&quot;,\&quot;plugin_id\&quot;:7281192623887548473,\&quot;api_id\&quot;:7288907006982012986,\&quot;plugin_type\&quot;:1}}&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;content_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;text&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;222&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;conversation.message.completed&quot;,
  &quot;data&quot;: {
    &quot;id&quot;: &quot;msg_002&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;type&quot;: &quot;function_call&quot;,
    &quot;content&quot;: &quot;{\&quot;name\&quot;:\&quot;toutiaosousuo-search\&quot;,\&quot;arguments\&quot;:{\&quot;cursor\&quot;:0,\&quot;input_query\&quot;:\&quot;今天的体育新闻\&quot;,\&quot;plugin_id\&quot;:7281192623887548473,\&quot;api_id\&quot;:7288907006982012986,\&quot;plugin_type\&quot;:1}}&quot;,
    &quot;content_type&quot;: &quot;text&quot;,
    &quot;chat_id&quot;: &quot;123&quot;,
    &quot;conversation_id&quot;: &quot;123&quot;,
    &quot;bot_id&quot;: &quot;222&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h2 id="79fd1eaf" tabindex="-1">对话完成</h2>
<ul data-style="0">
<li><strong>事件类型</strong>：<code>conversation.chat.completed</code></li>
<li><strong>事件说明</strong>：表示对话已完成。</li>
<li><strong>事件结构</strong>：</li>
</ul>
<!-- @cols-width: 184,152,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 184px;" /><col style="width: 152px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
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
<p>固定为<code>conversation.chat.completed</code>。</p>
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
<p>事件数据，包含对话的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>对话 ID，即对话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.conversation_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>会话 ID，即会话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.bot_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>要进行会话聊天的智能体 ID。</p>
</td>
</tr>
<tr>
<td>
<p>data.created_at</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话创建的时间。格式为 10 位的 Unixtime 时间戳，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>data.completed_at</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话结束的时间。格式为 10 位的 Unixtime 时间戳，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>data.last_error</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话运行异常时，此字段中返回详细的错误信息，包括：</p>
<ul data-style="0">
<li>Code：错误码。Integer 类型。0 表示成功，其他值表示失败。</li>
<li>Msg：错误信息。String 类型。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.meta_data</p>
</td>
<td>
<p>Map&lt;String, String&gt;</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>创建消息时的附加消息，用于传入使用方的自定义数据，获取消息时也会返回此附加消息。自定义键值对，应指定为 Map 对象格式。长度为 16 对键值对，其中键（key）的长度范围为 1～64 个字符，值（value）的长度范围为 1～512 个字符。</p>
</td>
</tr>
<tr>
<td>
<p>data.status</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的运行状态。取值为 <code>completed</code>，即智能体已完成处理，本次对话结束。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的 Token 使用情况。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.token_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>本次对话消耗的 Token 总数，包括 input 和 output 部分的消耗。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.output_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>output 部分消耗的 Token 总数。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.input_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>input 部分消耗的 Token 总数。</p>
</td>
</tr>
</tbody>
</table>
</div><ul data-style="0">
<li><strong>事件示例</strong>：</li>
</ul>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_1&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.chat.completed&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;222&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;created_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1710348675</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;completed_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1710348675</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;last_error&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">null</span></span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;meta_data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;status&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;completed&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;usage&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;token_count&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">3397</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;output_tokens&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1173</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;input_tokens&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">2224</span>
      <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">}</span>   
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;conversation.chat.completed&quot;,
  &quot;data&quot;: {
      &quot;id&quot;: &quot;123&quot;,
      &quot;chat_id&quot;: &quot;123&quot;,
      &quot;conversation_id&quot;: &quot;123&quot;,
      &quot;bot_id&quot;: &quot;222&quot;,
      &quot;created_at&quot;: 1710348675,
      &quot;completed_at&quot;: 1710348675,
      &quot;last_error&quot;: null,
      &quot;meta_data&quot;: {},
      &quot;status&quot;: &quot;completed&quot;,
      &quot;usage&quot;: {
          &quot;token_count&quot;: 3397,
          &quot;output_tokens&quot;: 1173,
          &quot;input_tokens&quot;: 2224
      }
  }   
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h2 id="1575c709" tabindex="-1">端插件请求</h2>
<ul data-style="0">
<li><strong>事件类型</strong>：conversation.chat.requires_action</li>
<li><strong>事件说明</strong>：对话中断，需要使用方上报工具的执行结果。</li>
<li><strong>事件结构</strong>：</li>
</ul>
<!-- @cols-width: 157,111,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 157px;" /><col style="width: 111px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
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
<p>固定为<code>conversation.chat.requires_action</code>。</p>
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
<p>事件数据，包含对话的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>对话 ID，即对话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.conversation_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>会话 ID，即会话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.bot_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>要进行会话聊天的智能体 ID。</p>
</td>
</tr>
<tr>
<td>
<p>data.created_at</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话创建的时间。格式为 10 位的 Unixtime 时间戳，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>data.completed_at</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话完成的时间。格式为 10 位的 Unixtime 时间戳，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>data.last_error</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话运行异常时，此字段中返回详细的错误信息，包括：</p>
<ul data-style="0">
<li>Code：错误码。Integer 类型。0 表示成功，其他值表示失败。</li>
<li>Msg：错误信息。String 类型。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.meta_data</p>
</td>
<td>
<p>Map&lt;String, String&gt;</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>创建消息时的附加消息，用于传入使用方的自定义数据，获取消息时也会返回此附加消息。自定义键值对，应指定为 Map 对象格式。长度为 16 对键值对，其中键（key）的长度范围为 1～64 个字符，值（value）的长度范围为 1～512 个字符。</p>
</td>
</tr>
<tr>
<td>
<p>data.status</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的运行状态。取值为 <code>created</code>，即对话已创建。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的 Token 使用情况。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.token_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>本次对话消耗的 Token 总数，包括 input 和 output 部分的消耗。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.output_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>output 部分消耗的 Token 总数。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.input_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>input 部分消耗的 Token 总数。</p>
</td>
</tr>
<tr>
<td>
<p>data.required_action</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>需要执行的额外操作。</p>
</td>
</tr>
<tr>
<td>
<p>data.required_action.type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>额外操作的类型，枚举值为 <code>submit_tool_outputs</code>。</p>
</td>
</tr>
<tr>
<td>
<p>data.required_action.submit_tool_outputs</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>需要提交的结果详情，通过提交接口上传，并可以继续聊天。</p>
</td>
</tr>
<tr>
<td>
<p>data.required_action.submit_tool_outputs.tool_outputs</p>
</td>
<td>
<p>Array</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>具体上报信息详情。</p>
</td>
</tr>
<tr>
<td>
<p>data.required_action.submit_tool_outputs.tool_outputs[].id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>上报运行结果的 ID。</p>
</td>
</tr>
<tr>
<td>
<p>data.required_action.submit_tool_outputs.tool_outputs[].type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>工具类型，枚举值包括：</p>
<ul data-style="0">
<li><strong>function</strong>: 端插件中断，需要通过上行事件<a href="/developer_guides/signaling_uplink_event#99e14cb2" target="_blank">提交端插件执行结果</a>信令来提交执行结果。</li>
<li><strong>reply_message</strong>: 问答中断，只需要继续正常对话。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.required_action.submit_tool_outputs.tool_outputs[].function</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>执行方法 function 的定义。</p>
</td>
</tr>
<tr>
<td>
<p>data.required_action.submit_tool_outputs.tool_outputs[].function.name</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>方法名。</p>
</td>
</tr>
<tr>
<td>
<p>data.required_action.submit_tool_outputs.tool_outputs[].function.arguments</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>方法参数。</p>
</td>
</tr>
</tbody>
</table>
</div><ul data-style="0">
<li><strong>事件示例</strong>：
<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7446668538246561821&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.chat.requires_action&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7434369946098090003&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7434368393420996671&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7379165428687536166&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;created_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1730949143</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;completed_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1730949146</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;last_error&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;status&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;requires_action&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;usage&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;token_count&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;output_count&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;input_count&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;required_action&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;submit_tool_outputs&quot;</span><span class="hljs-punctuation">,</span>
            <span class="hljs-attr">&quot;submit_tool_outputs&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
                <span class="hljs-attr">&quot;tool_calls&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
                    <span class="hljs-punctuation">{</span>
                        <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;BUJJS0JKQ0dHR0VeFkNCQF5HEEZBXhJFEUJeEhFCRkESSktDREISSUI=&quot;</span><span class="hljs-punctuation">,</span>
                        <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;function&quot;</span><span class="hljs-punctuation">,</span>
                        <span class="hljs-attr">&quot;function&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
                            <span class="hljs-attr">&quot;name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;get_current_temperature&quot;</span><span class="hljs-punctuation">,</span>
                            <span class="hljs-attr">&quot;arguments&quot;</span><span class="hljs-punctuation">:</span><span class="hljs-string">&quot;{\&#x27;location\&quot;:\&#x27;深圳\&#x27;}&quot;</span>
                        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
                        <span class="hljs-attr">&quot;require_info&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">null</span></span>
                    <span class="hljs-punctuation">}</span>
                <span class="hljs-punctuation">]</span>
            <span class="hljs-punctuation">}</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;section_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7434368393420996671&quot;</span>
    <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span> 
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;id&quot;: &quot;7446668538246561821&quot;,
    &quot;event_type&quot;: &quot;conversation.chat.requires_action&quot;,
    &quot;data&quot;: {
        &quot;id&quot;: &quot;7434369946098090003&quot;,
        &quot;conversation_id&quot;: &quot;7434368393420996671&quot;,
        &quot;bot_id&quot;: &quot;7379165428687536166&quot;,
        &quot;created_at&quot;: 1730949143,
        &quot;completed_at&quot;: 1730949146,
        &quot;last_error&quot;: {
            &quot;code&quot;: 0,
            &quot;msg&quot;: &quot;&quot;
        },
        &quot;status&quot;: &quot;requires_action&quot;,
        &quot;usage&quot;: {
            &quot;token_count&quot;: 0,
            &quot;output_count&quot;: 0,
            &quot;input_count&quot;: 0
        },
        &quot;required_action&quot;: {
            &quot;type&quot;: &quot;submit_tool_outputs&quot;,
            &quot;submit_tool_outputs&quot;: {
                &quot;tool_calls&quot;: [
                    {
                        &quot;id&quot;: &quot;BUJJS0JKQ0dHR0VeFkNCQF5HEEZBXhJFEUJeEhFCRkESSktDREISSUI=&quot;,
                        &quot;type&quot;: &quot;function&quot;,
                        &quot;function&quot;: {
                            &quot;name&quot;: &quot;get_current_temperature&quot;,
                            &quot;arguments&quot;:&quot;{\&apos;location\&quot;:\&apos;深圳\&apos;}&quot;
                        },
                        &quot;require_info&quot;: null
                    }
                ]
            }
        },
        &quot;section_id&quot;: &quot;7434368393420996671&quot;
    }
} " style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="bca97e88" tabindex="-1">对话失败</h2>
<ul data-style="0">
<li><strong>事件类型</strong>：<code>conversation.chat.failed</code></li>
<li><strong>事件说明</strong>：此事件用于标识对话失败。</li>
<li><strong>事件结构</strong>：</li>
</ul>
<!-- @cols-width: 184,152,100,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 184px;" /><col style="width: 152px;" /><col style="width: 100px;" /><col style="width: 500px;" /></colgroup><thead>
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
<p>固定为<code>conversation.chat.failed</code>。</p>
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
<p>事件数据，包含对话的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>对话 ID，即对话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.conversation_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>会话 ID，即会话的唯一标识。</p>
</td>
</tr>
<tr>
<td>
<p>data.bot_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>要进行会话聊天的智能体 ID。</p>
</td>
</tr>
<tr>
<td>
<p>data.created_at</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话创建的时间。格式为 10 位的 Unixtime 时间戳，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>data.failed_at</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话失败的时间。格式为 10 位的 Unixtime 时间戳，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>data.last_error</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话运行异常时，此字段中返回详细的错误信息，包括：Code：错误码。Integer 类型。0 表示成功，其他值表示失败。Msg：错误信息。String 类型。</p>
</td>
</tr>
<tr>
<td>
<p>data.meta_data</p>
</td>
<td>
<p>Map&lt;String, String&gt;</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>创建消息时的附加消息，用于传入使用方的自定义数据，获取消息时也会返回此附加消息。自定义键值对，应指定为 Map 对象格式。长度为 16 对键值对，其中键（key）的长度范围为 1～64 个字符，值（value）的长度范围为 1～512 个字符。</p>
</td>
</tr>
<tr>
<td>
<p>data.status</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的运行状态。取值为 <code>failed</code>，即对话失败。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话的 Token 使用情况。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.token_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>本次对话消耗的 Token 总数，包括 input 和 output 部分的消耗。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.output_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>output 部分消耗的 Token 总数。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.input_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>input 部分消耗的 Token 总数。</p>
</td>
</tr>
</tbody>
</table>
</div><ul data-style="0">
<li><strong>事件示例</strong>：</li>
</ul>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_1&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.chat.failed&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;chat_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;conversation_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;123&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;222&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;created_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1710348675</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;failed_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1710348675</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;last_error&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;发生异常&quot;</span>
      <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;meta_data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;status&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;failed&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;usage&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;token_count&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">3397</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;output_tokens&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1173</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;input_tokens&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">2224</span>
      <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">}</span>   
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;conversation.chat.failed&quot;,
  &quot;data&quot;: {
      &quot;id&quot;: &quot;123&quot;,
      &quot;chat_id&quot;: &quot;123&quot;,
      &quot;conversation_id&quot;: &quot;123&quot;,
      &quot;bot_id&quot;: &quot;222&quot;,
      &quot;created_at&quot;: 1710348675,
      &quot;failed_at&quot;: 1710348675,
      &quot;last_error&quot;: {
          &quot;code&quot;: 1,
          &quot;msg&quot;: &quot;发生异常&quot;
      },
      &quot;meta_data&quot;: {},
      &quot;status&quot;: &quot;failed&quot;,
      &quot;usage&quot;: {
          &quot;token_count&quot;: 3397,
          &quot;output_tokens&quot;: 1173,
          &quot;input_tokens&quot;: 2224
      }
  }   
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h2 id="d25ab9d1" tabindex="-1">用户开始说话</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>audio.user.speech_started</code></p>
</li>
<li>
<p><strong>事件说明</strong>：此事件表示服务端识别到用户正在说话。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,415 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 415px;" /></colgroup><thead>
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
<p>固定为<code>audio.user.speech_started</code>。</p>
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
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;audio.user.speech_started&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;audio.user.speech_started&quot;,
  &quot;data&quot;: {}
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="9242e241" tabindex="-1">用户结束说话</h2>
<ul data-style="0">
<li><strong>事件类型</strong>：<code>audio.user.speech_stopped</code></li>
<li><strong>事件说明</strong>：此事件表示服务端识别到用户已停止说话。</li>
<li><strong>事件结构</strong>：</li>
</ul>
<!-- @cols-width: 100,100,100,430 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 430px;" /></colgroup><thead>
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
<p>固定为<code>audio.user.speech_stopped</code>。</p>
</td>
</tr>
</tbody>
</table>
</div><ul data-style="0">
<li><strong>事件示例</strong>：</li>
</ul>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;event_1&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;audio.user.speech_stopped&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;audio.user.speech_stopped&quot;,
  &quot;data&quot;: {}
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h2 id="8e71ba6b" tabindex="-1">智能体开始说话</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>audio.agent.speech_started</code></p>
</li>
<li>
<p><strong>事件说明</strong>：此事件表示智能体正在说话。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,402 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 402px;" /></colgroup><thead>
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
<p>固定为<code>audio.agent.speech_started</code>。</p>
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
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;audio.agent.speech_started&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;audio.agent.speech_started&quot;,
  &quot;data&quot;: {}
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="78b17cf2" tabindex="-1">智能体结束说话</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>audio.agent.speech_stopped</code></p>
</li>
<li>
<p><strong>事件说明</strong>：此事件表示智能体已停止说话。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,487 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 487px;" /></colgroup><thead>
<tr>
<th>
<p>参数</p>
</th>
<th>
<p>类型</p>
</th>
<th>
<p>是否必选</p>
</th>
<th>
<p>说明</p>
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
<p>固定为<code>audio.agent.speech_stopped</code>。</p>
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
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;audio.agent.speech_stopped&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;audio.agent.speech_stopped&quot;,
  &quot;data&quot;: {}
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="f4f632c3" tabindex="-1">安抚配置更新成功</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>session.pre_answer.updated</code></p>
</li>
<li>
<p><strong>事件说明</strong>：房间内的安抚配置更新成功，返回房间内最新的安抚配置。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 162,104,100,455 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 162px;" /><col style="width: 104px;" /><col style="width: 100px;" /><col style="width: 455px;" /></colgroup><thead>
<tr>
<th>
<p>参数</p>
</th>
<th>
<p>类型</p>
</th>
<th>
<p>是否必选</p>
</th>
<th>
<p>说明</p>
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
<p>固定为 <code>session.pre_answer.updated</code>。</p>
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
<p>事件数据，包含安抚策略的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.pre_answer</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>安抚策略配置。</p>
</td>
</tr>
<tr>
<td>
<p>data.pre_answer.type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>安抚策略类型，可选类型有：</p>
<ul data-style="1">
<li><code>none</code>：取消安抚策略，默认值。</li>
<li><code>audio</code>：根据用户上传的音频文件作为安抚语。</li>
<li><code>text</code>：根据用户输入的文本生成安抚语。</li>
<li><code>bot</code>：指定另一个智能体作为安抚语的生成载体。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.pre_answer.file_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>仅在 <code>audio</code> 模式下生效，用户需要先通过上传文件接口上传一个音频文件，传入该接口返回的 <code>file_id</code>。当前仅支持 <code>wav</code>/<code>mp3</code> 音频文件。</p>
</td>
</tr>
<tr>
<td>
<p>data.pre_answer.pre_answer_list</p>
</td>
<td>
<p>Array<String></p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>仅在 <code>text</code> 模式下生效，用户可以输入一批文本，会在触发安抚策略时随机选取一段文本作为安抚语播放。</p>
</td>
</tr>
<tr>
<td>
<p>data.pre_answer.bot_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>仅在 <code>bot</code> 模式下生效，ASR 识别的文本会同时请求这个 <code>BotID</code>，并将该智能体回复的内容作为安抚语。传入的智能体必须是属于当前用户的智能体。该策略会消耗额外的 Token。</p>
</td>
</tr>
<tr>
<td>
<p>data.trigger</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>安抚策略的触发配置。</p>
</td>
</tr>
<tr>
<td>
<p>data.trigger.type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>安抚策略的触发类型，可选类型有：</p>
<ul data-style="1">
<li><code>mandatory</code>：必定触发安抚策略，默认值。</li>
<li><code>time-trigger</code>：一段时间后模型没有生成回复，就会触发安抚策略。</li>
<li><code>event-driven</code>：模型触发 function call 就会触发安抚策略。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>data.trigger.time_after</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>仅在 <code>time-trigger</code> 模式下生效，指定在等待多长时间后触发安抚策略，单位为 ms，取值范围 [0, 3000]，默认值为 1500ms。</p>
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
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;session.pre_answer.updated&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;pre_answer&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;bot&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;file_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;pre_answer_list&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;bot_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;23452423&quot;</span>
      <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;trigger&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;mandatory&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;time_after&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1500</span>
      <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;session.pre_answer.updated&quot;,
  &quot;data&quot;: {
      &quot;pre_answer&quot;: {
          &quot;type&quot;: &quot;bot&quot;,
          &quot;file_id&quot;: &quot;&quot;,
          &quot;pre_answer_list&quot;: [&quot;&quot;],
          &quot;bot_id&quot;: &quot;23452423&quot;
      },
      &quot;trigger&quot;: {
          &quot;type&quot;: &quot;mandatory&quot;,
          &quot;time_after&quot;: 1500
      }
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="d071e868" tabindex="-1">安抚已生成</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>conversation.chat.pre_answer</code></p>
</li>
<li>
<p><strong>事件说明</strong>：此事件表明触发了安抚策略。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 184,100,100,439 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 184px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 439px;" /></colgroup><thead>
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
<p>固定为 <code>conversation.chat.pre_answer</code>。</p>
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
<p>事件数据，包含安抚语的详细信息。</p>
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
<p>可选</p>
</td>
<td>
<p>安抚语的内容。若选择 <code>audio</code> 安抚策略，则该字段为空。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>本次安抚语消耗的 Token 信息，仅在使用 <code>bot</code> 安抚策略时展示该字段。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.token_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>本次安抚语消耗的 Token 总数，包括 input 和 output 部分的消耗。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.output_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>output 部分消耗的 Token 总数。</p>
</td>
</tr>
<tr>
<td>
<p>data.usage.input_count</p>
</td>
<td>
<p>Integer</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>input 部分消耗的 Token 总数。</p>
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
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.chat.pre_answer&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;usage&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;token_count&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;output_tokens&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;input_tokens&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span>
      <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;conversation.chat.pre_answer&quot;,
  &quot;data&quot;: {
      &quot;content&quot;: &quot;&quot;,
      &quot;usage&quot;: {
          &quot;token_count&quot;: 0,
          &quot;output_tokens&quot;: 0,
          &quot;input_tokens&quot;: 0
      }
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="3cc6bf07" tabindex="-1">用户语音识别字幕</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>conversation.audio_transcript.delta</code></p>
</li>
<li>
<p><strong>事件说明</strong>：用户语音识别的中间值，每次返回都是全量文本。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,522 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 522px;" /></colgroup><thead>
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
<p>固定为<code>conversation.audio_transcript.delta</code>。</p>
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
<p>事件数据，包含语音识别的中间值。</p>
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
<p>语音识别的中间值。</p>
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
  <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;conversation.audio_transcript.delta&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;今天的&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;conversation.audio_transcript.delta&quot;,
  &quot;data&quot;: {
      &quot;content&quot;: &quot;今天的&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="54a9c02b" tabindex="-1">更新房间模式成功</h2>
<ul data-style="0">
<li><strong>事件类型</strong>：<code>mode.updated</code></li>
<li><strong>事件说明</strong>：房间模式更新成功，返回最新的房间模式设置。</li>
<li><strong>事件结构</strong>：</li>
</ul>
<!-- @cols-width: 240,148,172,272 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 240px;" /><col style="width: 148px;" /><col style="width: 172px;" /><col style="width: 272px;" /></colgroup><thead>
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
<p>固定为 <code>mode.updated</code>。</p>
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
<p>事件数据，包含房间模式和对话设置。</p>
</td>
</tr>
<tr>
<td>
<p>data.mode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>房间模式。<br>
默认为 chat，即对话模式，跟智能体进行聊天。</p>
</td>
</tr>
<tr>
<td>
<p>data.mode.chat</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>对话模式下的设置，仅当 <code>mode</code> 为 <code>chat</code> 时生效。</p>
</td>
</tr>
<tr>
<td rowspan="14">
<p>data.mode.chat.user_language</p>
</td>
<td rowspan="14">
<p>String</p>
</td>
<td rowspan="14">
<p>可选</p>
</td>
<td rowspan="14">
<p>用户说话的语种，默认为 <code>common</code>。选项包括：</p>
<ul data-style="0">
<li>common：大模型语音识别，支持中英文、上海话、闽南语，四川、陕西、粤语识别。</li>
<li>英语：en-US</li>
<li>日语：ja-JP</li>
<li>印尼语：id-ID</li>
<li>西班牙语：es-MX</li>
<li>葡萄牙语：pt-BR</li>
<li>德语：de-DE</li>
<li>法语：fr-FR</li>
<li>韩语：ko-KR</li>
<li>菲律宾语：fil-PH</li>
<li>马来语：ms-MY</li>
<li>泰语：th-TH</li>
<li>阿拉伯语：ar-SA</li>
</ul>
</td>
</tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
</tbody>
</table>
</div><ul data-style="0">
<li><strong>事件示例</strong>：</li>
</ul>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;mode.updated&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;mode&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;chat&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;chat&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
            <span class="hljs-attr">&quot;user_language&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;common&quot;</span>
        <span class="hljs-punctuation">}</span>
    <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;id&quot;: &quot;&quot;,
    &quot;event_type&quot;: &quot;mode.updated&quot;,
    &quot;data&quot;: {
        &quot;mode&quot;: &quot;chat&quot;,
        &quot;chat&quot;: {
            &quot;user_language&quot;: &quot;common&quot;
        }
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h2 id="d0aa714c" tabindex="-1">用户开始说话</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>input_audio_buffer.started</code></p>
</li>
<li>
<p><strong>事件说明</strong>：表示服务端成功处理用户开始说话事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,381 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 381px;" /></colgroup><thead>
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
<p>string</p>
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
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 input_audio_buffer.started。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p>事件示例：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7446668538246561827&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;input_audio_buffer.start&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;id&quot;: &quot;7446668538246561827&quot;,
    &quot;event_type&quot;: &quot;input_audio_buffer.start&quot;,
    &quot;data&quot;: {}
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="2cd78201" tabindex="-1">用户结束说话</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>input_audio_buffer.completed</code></p>
</li>
<li>
<p><strong>事件说明</strong>：表示服务端成功处理用户结束说话事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 100,100,100,381 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 381px;" /></colgroup><thead>
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
<p>string</p>
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
<p>string</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>固定为 input_audio_buffer.completed。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p>事件示例：</p>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7446668538246561827&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;event_type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;input_audio_buffer.completed&quot;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span><span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
    &quot;id&quot;: &quot;7446668538246561827&quot;,
    &quot;event_type&quot;: &quot;input_audio_buffer.completed&quot;,
    &quot;data&quot;: {}
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="dbc236b8" tabindex="-1"></h2>
<h2 id="6617d50e" tabindex="-1">发生错误</h2>
<ul data-style="0">
<li>
<p><strong>事件类型</strong>：<code>error</code></p>
</li>
<li>
<p><strong>事件说明</strong>：对话过程中的错误事件。</p>
</li>
<li>
<p><strong>事件结构</strong>：</p>
 <!-- @cols-width: 136,100,100,416 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 136px;" /><col style="width: 100px;" /><col style="width: 100px;" /><col style="width: 416px;" /></colgroup><thead>
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
<p>固定为<code>error</code>。</p>
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
<p>事件数据，包含错误的详细信息。</p>
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
<p>错误码。错误码列表请参见<a href="/developer_guides/realtime_error_codes" target="_blank">Realtime 事件错误码</a>。</p>
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
<p>data.detail</p>
</td>
<td>
<p>Object</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>错误的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>data.detail.logid</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>服务端日志 ID。</p>
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
      <span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;发生异常&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span>
      <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;id&quot;: &quot;event_1&quot;,
  &quot;event_type&quot;: &quot;error&quot;,
  &quot;data&quot;: {
      &quot;code&quot;: 1,
      &quot;msg&quot;: &quot;发生异常&quot;,
      &quot;detail&quot;: {
          &quot;logid&quot;: &quot;&quot;
      }
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ul>
<h2 id="edb84e66" tabindex="-1"></h2>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/developer_guides_signaling_uplink_event" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">Realtime 上行事件</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/developer_guides_realtime_error_codes" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">Realtime 事件错误码</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="房间配置成功" href="#2a980f88" data-href="#2a980f88">房间配置成功</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="房间配置更新成功" href="#5c7c0c03" data-href="#5c7c0c03">房间配置更新成功</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="会话创建成功" href="#0a12551c" data-href="#0a12551c">会话创建成功</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="对话开始" href="#b5369292" data-href="#b5369292">对话开始</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="对话处理中" href="#1f5f6f91" data-href="#1f5f6f91">对话处理中</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="增量消息" href="#17fc454e" data-href="#17fc454e">增量消息</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="消息已完成" href="#aa18a150" data-href="#aa18a150">消息已完成</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="对话完成" href="#79fd1eaf" data-href="#79fd1eaf">对话完成</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="端插件请求" href="#1575c709" data-href="#1575c709">端插件请求</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="对话失败" href="#bca97e88" data-href="#bca97e88">对话失败</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="用户开始说话" href="#d25ab9d1" data-href="#d25ab9d1">用户开始说话</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="用户结束说话" href="#9242e241" data-href="#9242e241">用户结束说话</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="智能体开始说话" href="#8e71ba6b" data-href="#8e71ba6b">智能体开始说话</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="智能体结束说话" href="#78b17cf2" data-href="#78b17cf2">智能体结束说话</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="安抚配置更新成功" href="#f4f632c3" data-href="#f4f632c3">安抚配置更新成功</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="安抚已生成" href="#d071e868" data-href="#d071e868">安抚已生成</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="用户语音识别字幕" href="#3cc6bf07" data-href="#3cc6bf07">用户语音识别字幕</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="更新房间模式成功" href="#54a9c02b" data-href="#54a9c02b">更新房间模式成功</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="用户开始说话" href="#d0aa714c" data-href="#d0aa714c">用户开始说话</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="用户结束说话" href="#2cd78201" data-href="#2cd78201">用户结束说话</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="发生错误" href="#6617d50e" data-href="#6617d50e">发生错误</a></div></div></div></div></div></div></div></div>
</body></html>