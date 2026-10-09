<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">配置访问密钥</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/5956.1729cb00c0.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.ca52691239.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/developer_guides_java_access_token"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/developer_guides_java_access_token.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
  
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/developer_guides_java_access_token" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b97434bdbc784e3ce84ce" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a55df9a4bdbc784e3c9738f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf30d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf317" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf31d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf325" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf334" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf32e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf35a" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf362" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8e614bdbc784e3cce185" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3e2c" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fa8" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc40e8" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Chat SDK">Chat SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc40ef" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Python SDK">Python SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc412c" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Node.js SDK">Node.js SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4132" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Java SDK">Java SDK</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc4180" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_java_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="Java SDK 概述">Java SDK 概述</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4185" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_java_installation" data-discover="true"><span class="nodeTitle-ONnqtP" title="安装 Java SDK">安装 Java SDK</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc418d" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:56px" href="/developer_guides_java_access_token" data-discover="true"><span class="nodeTitle-ONnqtP" title="配置访问密钥">配置访问密钥</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4194" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_java_getting_started" data-discover="true"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc41c6" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Go SDK">Go SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4245" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_vibe_coding_websdk" data-discover="true"><span class="nodeTitle-ONnqtP" title="Web SDK（AI 编程）">Web SDK（AI 编程）</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc424c" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_ui_builder_web_sdk" data-discover="true"><span class="nodeTitle-ONnqtP" title="Web SDK（低代码）">Web SDK（低代码）</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc4251" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Card SDK">Card SDK</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc529d" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8e4bdbc784e3cc445f" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/developer_guides_coze_cli" data-discover="true"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf33f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf369" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/guides_FAQ" data-discover="true"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>SDK 参考</span><span class="separator-KB9yMa">/</span><span>Java SDK</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">配置访问密钥</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">配置访问密钥</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg><span>复制页面</span></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>通过 Java SDK 方式调用扣子编程 OpenAPI 时，需要在 SDK 请求中配置访问密钥，用于身份信息认证和权限校验。扣子编程 OpenAPI 提供个人访问密钥和 OAuth 两种鉴权方式，你可以选择当前业务场景适合的鉴权方式，并获取对应的访问密钥。<br>
对于 OAuth 授权码等授权方式，Coze Java SDK 已经封装了这部分代码，并处理了不同的返回错误代码，简化你的操作。</p>
<h2 id="73e164bf" tabindex="-1">配置方式</h2>
<p>扣子编程 OpenAPI 目前支持的鉴权方式如下。</p>
<!-- @cols-width: 169,173,335,279 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 169px;" /><col style="width: 173px;" /><col style="width: 335px;" /><col style="width: 279px;" /></colgroup><thead>
<tr>
<th>
<p><strong>访问密钥类型</strong></p>
</th>
<th>
<p><strong>鉴权方式</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
<th>
<p><strong>示例文件</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>个人访问密钥（PAT）</p>
</td>
<td>
<p>个人访问密钥（PAT）</p>
</td>
<td>
<p>Personal Access Token，简称 PAT。扣子编程中生成的个人访问令牌。PAT 生成与使用便捷，适用于测试环境调试等场景。每个令牌可以关联多个空间，并开通指定的接口权限。生成方式可参考<a href="https://www.coze.cn/docs/developer_guides/pat" target="_blank">添加个人访问令牌</a>。</p>
</td>
<td rowspan="2">
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/TokenAuthExample.java" target="_blank">TokenAuthExample.java</a></p>
</td>
</tr>
<tr>
<td>
<p>服务访问令牌（SAT）</p>
</td>
<td>
<p>服务访问令牌（SAT）</p>
</td>
<td>
<p>Service Access Token（简称 SAT）是以服务身份创建的访问凭证，可<strong>长期有效</strong>访问扣子编程资源，通常用于服务/应用程序的身份验证和授权。SAT 与 OAuth JWT 鉴权方式相比，具有更长的有效期（可设置为永久有效），操作简单，能够有效简化授权流程。生成方式可参考<a href="/developer_guides/service_token" target="_blank">添加服务访问令牌</a>。<br>
SAT 的示例代码与 PAT 通用，可直接参考 PAT 的示例文件。</p>
</td>
</tr>
<tr>
<td rowspan="4">
<p>OAuth 认证</p>
</td>
<td>
<p>授权码授权<br>
（Authorization Code Flow）</p>
</td>
<td>
<p>适用于有显著前后端之分的应用程序授权场景。其中前端模块负责与用户交互，后端服务处理前端请求，与扣子授权服务器和 OpenAPI 交互。 实现流程可参考<a href="/developer_guides/oauth_code" target="_blank">OAuth 授权码授权</a>。</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/WebOAuthExample.java" target="_blank">WebOAuthExample.java</a></p>
</td>
</tr>
<tr>
<td>
<p>PKCE 授权<br>
（Authorization Code Flow with PKCE）</p>
</td>
<td>
<p>应用程序无后端服务，所有操作都发生在应用程序的前端。 实现流程可参考<a href="/developer_guides/oauth_pkce" target="_blank">OAuth PKCE</a>。</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/PKCEOAuthExample.java" target="_blank">PKCEOauthExample.java</a></p>
</td>
</tr>
<tr>
<td>
<p>设备码授权<br>
（Device Code Flow）</p>
</td>
<td>
<p>应用程序无后端服务，所有操作都发生在应用程序的 Command Line，且 Command Line 无法提供“同意授权”的操作。 实现流程可参考<a href="/developer_guides/oauth_device_code" target="_blank">OAuth 设备授权</a>。</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/DevicesOAuthExample.java" target="_blank">DevicesOAuthExample.java</a></p>
</td>
</tr>
<tr>
<td>
<p>JWT 授权<br>
（JWT Flow）</p>
</td>
<td>
<p>应用程序服务端直接调用扣子编程 OpenAPI。<br>
应用程序后端服务代理应用程序自己的用户获取身份凭据，应用程序用户基于凭据直接访问 OpenAPI。 实现流程可参考<a href="/developer_guides/oauth_jwt" target="_blank">OAuth JWT 授权（开发者）</a>。</p>
</td>
<td>
<p><a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/JWTOAuthExample.java" target="_blank">JWTsOauthExample.java</a></p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="364507dd" tabindex="-1">配置个人访问密钥（PAT）</h2>
<p>如果选择使用个人访问密钥鉴权，你需要先申请一个个人访问密钥，并添加指定空间和权限。操作步骤可参考<a href="https://www.coze.cn/docs/developer_guides/pat" target="_blank">添加个人访问令牌</a>。完整的示例代码请参见 <a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/TokenAuthExample.java" target="_blank">TokenAuthExample.java</a>。<br>
扣子编程建议你通过环境变量的方式管理访问密钥，避免在代码中通过硬编码方式进行编程，以免密钥泄露、引发安全风险。配置环境变量之后，您可以在不修改代码的情况下，将动态的鉴权参数传递到对应的函数，实现便捷安全的身份认证。</p>
<ol data-style="0">
<li>
<p>设置环境变量。<br>
其中 COZE_API_TOKEN 是扣子编程中申请的个人访问密钥。</p>

<div style="position: relative">
	<pre><code class="hljs language-Shell">export COZE_API_TOKEN=pat_****
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="export COZE_API_TOKEN=pat_****" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>初始化客户端。<br>
示例代码如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"><span class="hljs-keyword">import</span> com.coze.openapi.service.auth.TokenAuth;
<span class="hljs-keyword">import</span> com.coze.openapi.service.config.Consts;
<span class="hljs-keyword">import</span> com.coze.openapi.service.service.CozeAPI;
<span class="hljs-keyword">import</span> okhttp3.OkHttpClient;

<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">InitClientExample</span> {
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">main</span><span class="hljs-params">(String[] args)</span> {
        <span class="hljs-comment">// 从环境变量中获取个人访问密钥（PAT）</span>
        <span class="hljs-comment">// 推荐使用环境变量管理密钥，避免硬编码导致泄露</span>
        <span class="hljs-type">String</span> <span class="hljs-variable">token</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_API_TOKEN&quot;</span>);
        
        <span class="hljs-comment">// 创建TokenAuth对象，传入PAT作为身份认证凭据</span>
        <span class="hljs-type">TokenAuth</span> <span class="hljs-variable">authCli</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">TokenAuth</span>(token);

        <span class="hljs-comment">// 构建CozeAPI客户端实例，配置连接参数</span>
        <span class="hljs-type">CozeAPI</span> <span class="hljs-variable">coze</span> <span class="hljs-operator">=</span>
            <span class="hljs-keyword">new</span> <span class="hljs-title class_">CozeAPI</span>.Builder()
                .baseURL(Consts.COZE_CN_BASE_URLCOZE_COM_BASE_URL)  <span class="hljs-comment">// 设置扣子编程OpenAPI的 Endpoint</span>
                .auth(authCli)  <span class="hljs-comment">// 绑定鉴权对象，用于请求时的身份验证</span>
                .client(<span class="hljs-keyword">new</span> <span class="hljs-title class_">OkHttpClient</span>.Builder().build())  <span class="hljs-comment">// 配置HTTP客户端（使用默认OkHttpClient）</span>
                .build();  <span class="hljs-comment">// 完成客户端初始化</span>
    }
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import com.coze.openapi.service.auth.TokenAuth;
import com.coze.openapi.service.config.Consts;
import com.coze.openapi.service.service.CozeAPI;
import okhttp3.OkHttpClient;

public class InitClientExample {
    public static void main(String[] args) {
        // 从环境变量中获取个人访问密钥（PAT）
        // 推荐使用环境变量管理密钥，避免硬编码导致泄露
        String token = System.getenv(&quot;COZE_API_TOKEN&quot;);
        
        // 创建TokenAuth对象，传入PAT作为身份认证凭据
        TokenAuth authCli = new TokenAuth(token);

        // 构建CozeAPI客户端实例，配置连接参数
        CozeAPI coze =
            new CozeAPI.Builder()
                .baseURL(Consts.COZE_CN_BASE_URLCOZE_COM_BASE_URL)  // 设置扣子编程OpenAPI的 Endpoint
                .auth(authCli)  // 绑定鉴权对象，用于请求时的身份验证
                .client(new OkHttpClient.Builder().build())  // 配置HTTP客户端（使用默认OkHttpClient）
                .build();  // 完成客户端初始化
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ol>
<h2 id="b1e6ad12" tabindex="-1">配置 OAuth 授权码流程</h2>
<p>如果选择使用 OAuth 授权码方式完成授权，可参考以下流程及示例代码。完整的示例代码请参见 <a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/WebOAuthExample.java" target="_blank">WebOAuthExample.java</a>。</p>
<ol data-style="0">
<li>
<p>创建 OAuth 应用。<br>
具体操作步骤可参考<a href="/developer_guides/oauth_code" target="_blank">OAuth 授权码授权</a>。成功创建 OAuth 应用后，你将获得客户端 ID、客户端密钥和重定向地址。你需要妥善保管客户端密钥，以免数据泄露引发安全风险。</p>
</li>
<li>
<p>在代码中通过环境变量方式设置客户端 ID、客户端密钥和重定向地址。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">PKCEOauthExample</span> {
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">main</span><span class="hljs-params">(String[] args)</span> {
        <span class="hljs-comment">// 从环境变量中获取PKCE OAuth应用的重定向地址，创建PKCE类型OAuth应用时配置的前端回调地址</span>
        <span class="hljs-type">String</span> <span class="hljs-variable">redirectURI</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_PKCE_OAUTH_REDIRECT_URI&quot;</span>);
        
        <span class="hljs-comment">// 从环境变量中获取PKCE OAuth应用的客户端ID，创建PKCE类型OAuth应用时平台生成的唯一标识符</span>
        <span class="hljs-type">String</span> <span class="hljs-variable">clientID</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_PKCE_OAUTH_CLIENT_ID&quot;</span>);

        <span class="hljs-comment">// 创建PKCEOAuthClient实例，配置应用信息</span>
        <span class="hljs-type">PKCEOAuthClient</span> <span class="hljs-variable">oauth</span> <span class="hljs-operator">=</span>
            <span class="hljs-keyword">new</span> <span class="hljs-title class_">PKCEOAuthClient</span>.PKCEOAuthBuilder()
                .clientID(clientID)  <span class="hljs-comment">// 传入客户端ID，即从环境变量获取的PKCE应用客户端ID</span>
                <span class="hljs-comment">// 设置扣子授权服务器端点，由扣子编程固定提供的授权服务地址</span>
                .baseURL(Consts.COZE_CN_BASE_URLCOZE_COM_BASE_URL)
                .build();


        <span class="hljs-comment">/*
         * 生成PKCE授权链接
         * 1. SDK自动生成code_verifier和code_challenge
         * 2. 授权链接包含code_challenge和回调地址，用于引导用户授权
         */</span>
        <span class="hljs-comment">// 生成授权链接及code_verifier，返回包含授权URL和code_verifier的响应对象</span>
        <span class="hljs-type">GetPKCEAuthURLResp</span> <span class="hljs-variable">oauthURL</span> <span class="hljs-operator">=</span>
            oauth.genOAuthURL(
                redirectURI,  <span class="hljs-comment">// 重定向地址，即从环境变量获取的PKCE应用回调地址</span>
                <span class="hljs-string">&quot;state&quot;</span>,  <span class="hljs-comment">// 状态参数，用于防CSRF攻击，自定义字符串</span>
                <span class="hljs-comment">// 指定code_challenge的生成算法，固定使用SHA-256算法（S256）</span>
                PKCEOAuthClient.CodeChallengeMethod.S256
            );
        System.out.println(oauthURL);
        
        <span class="hljs-comment">// 打印SDK生成的code_verifier，SDK自动生成的随机字符串，用于后续换取令牌时验证</span>
        System.out.println(oauthURL.getCodeVerifier());
        
        <span class="hljs-comment">// 打印用户需要访问的授权链接，用户授权页面的URL，从GetPKCEAuthURLResp对象获取</span>
        System.out.println(oauthURL.getAuthorizationURL());


        <span class="hljs-comment">/*
         * 用户授权后，扣子会重定向到redirectURI，并在Query中携带code（授权码）
         */</span>
        <span class="hljs-comment">// 模拟从重定向地址Query中获取的授权码，用户授权后从redirectURI的Query参数（code）中提取</span>
        <span class="hljs-type">String</span> <span class="hljs-variable">code</span> <span class="hljs-operator">=</span> <span class="hljs-string">&quot;mock code&quot;</span>;

        <span class="hljs-comment">/*
         * 用授权码和code_verifier换取访问令牌
         * 必须传入genOAuthURL返回的code_verifier，否则验证失败
         */</span>
        <span class="hljs-type">OAuthToken</span> <span class="hljs-variable">resp</span> <span class="hljs-operator">=</span> oauth.getAccessToken(code, redirectURI, oauthURL.getCodeVerifier());
        System.out.println(resp);  <span class="hljs-comment">// 打印令牌信息</span>

        <span class="hljs-comment">// 使用access_token初始化Coze客户端</span>
        <span class="hljs-type">CozeAPI</span> <span class="hljs-variable">coze</span> <span class="hljs-operator">=</span>
            <span class="hljs-keyword">new</span> <span class="hljs-title class_">CozeAPI</span>.Builder()
                <span class="hljs-comment">// 用access_token创建鉴权对象，access_token从OAuthToken对象获取</span>
                .auth(<span class="hljs-keyword">new</span> <span class="hljs-title class_">TokenAuth</span>(resp.getAccessToken()))
                .baseURL(cozeAPIBase)  <span class="hljs-comment">// 设置OpenAPI服务端点</span>
                .build();

        <span class="hljs-comment">// 令牌过期时，使用refresh_token刷新，refresh_token从OAuthToken对象获取</span>
        resp = oauth.refreshToken(resp.getRefreshToken());
    }
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="public class PKCEOauthExample {
    public static void main(String[] args) {
        // 从环境变量中获取PKCE OAuth应用的重定向地址，创建PKCE类型OAuth应用时配置的前端回调地址
        String redirectURI = System.getenv(&quot;COZE_PKCE_OAUTH_REDIRECT_URI&quot;);
        
        // 从环境变量中获取PKCE OAuth应用的客户端ID，创建PKCE类型OAuth应用时平台生成的唯一标识符
        String clientID = System.getenv(&quot;COZE_PKCE_OAUTH_CLIENT_ID&quot;);

        // 创建PKCEOAuthClient实例，配置应用信息
        PKCEOAuthClient oauth =
            new PKCEOAuthClient.PKCEOAuthBuilder()
                .clientID(clientID)  // 传入客户端ID，即从环境变量获取的PKCE应用客户端ID
                // 设置扣子授权服务器端点，由扣子编程固定提供的授权服务地址
                .baseURL(Consts.COZE_CN_BASE_URLCOZE_COM_BASE_URL)
                .build();


        /*
         * 生成PKCE授权链接
         * 1. SDK自动生成code_verifier和code_challenge
         * 2. 授权链接包含code_challenge和回调地址，用于引导用户授权
         */
        // 生成授权链接及code_verifier，返回包含授权URL和code_verifier的响应对象
        GetPKCEAuthURLResp oauthURL =
            oauth.genOAuthURL(
                redirectURI,  // 重定向地址，即从环境变量获取的PKCE应用回调地址
                &quot;state&quot;,  // 状态参数，用于防CSRF攻击，自定义字符串
                // 指定code_challenge的生成算法，固定使用SHA-256算法（S256）
                PKCEOAuthClient.CodeChallengeMethod.S256
            );
        System.out.println(oauthURL);
        
        // 打印SDK生成的code_verifier，SDK自动生成的随机字符串，用于后续换取令牌时验证
        System.out.println(oauthURL.getCodeVerifier());
        
        // 打印用户需要访问的授权链接，用户授权页面的URL，从GetPKCEAuthURLResp对象获取
        System.out.println(oauthURL.getAuthorizationURL());


        /*
         * 用户授权后，扣子会重定向到redirectURI，并在Query中携带code（授权码）
         */
        // 模拟从重定向地址Query中获取的授权码，用户授权后从redirectURI的Query参数（code）中提取
        String code = &quot;mock code&quot;;

        /*
         * 用授权码和code_verifier换取访问令牌
         * 必须传入genOAuthURL返回的code_verifier，否则验证失败
         */
        OAuthToken resp = oauth.getAccessToken(code, redirectURI, oauthURL.getCodeVerifier());
        System.out.println(resp);  // 打印令牌信息

        // 使用access_token初始化Coze客户端
        CozeAPI coze =
            new CozeAPI.Builder()
                // 用access_token创建鉴权对象，access_token从OAuthToken对象获取
                .auth(new TokenAuth(resp.getAccessToken()))
                .baseURL(cozeAPIBase)  // 设置OpenAPI服务端点
                .build();

        // 令牌过期时，使用refresh_token刷新，refresh_token从OAuthToken对象获取
        resp = oauth.refreshToken(resp.getRefreshToken());
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>授权码流程中，会自动生成一个扣子编程授权页面，然后将其发送给需要授权的用户。扣子用户可访问此链接，并根据页面提示完成授权流程。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"> <span class="hljs-type">String</span> <span class="hljs-variable">oauthURL</span> <span class="hljs-operator">=</span> oauth.getOAuthURL(redirectURI, <span class="hljs-literal">null</span>);
 System.out.println(oauthURL);

    <span class="hljs-comment">/*
     * To restrict access to a specific WorkSpace, you can specify the WorkSpaceID when obtaining the URL.
      oauthURL = oauth.getOAuthURL(redirectURI, null, &quot;workspaceID&quot;);
    System.out.println(oauthURL);
     * */</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text=" String oauthURL = oauth.getOAuthURL(redirectURI, null);
 System.out.println(oauthURL);

    /*
     * To restrict access to a specific WorkSpace, you can specify the WorkSpaceID when obtaining the URL.
      oauthURL = oauth.getOAuthURL(redirectURI, null, &quot;workspaceID&quot;);
    System.out.println(oauthURL);
     * */" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>用户点击同意授权按钮后，扣子编程网页会将请求重定向到授权链接中配置的重定向地址，并通过 Query 在地址中携带授权码和状态参数。<br>
通过授权码（OAuth code）调用 OpenAPI 接口即可获取 OAuth Access Token。示例代码如下：</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"> <span class="hljs-comment">/*
         * 授权流程说明：
         * 1. 前端引导用户访问扣子授权页面，用户完成授权后，扣子会重定向到redirectURI
         * 2. 重定向地址的Query参数中会携带code（授权码）和state（状态参数，用于防CSRF）
         * 3. 后端从Query中提取code，用于换取访问令牌
         */</span>
        <span class="hljs-comment">// 模拟从重定向地址的Query中获取到的授权码，用户授权后从redirectURI的Query参数（code）中提取</span>
        <span class="hljs-type">String</span> <span class="hljs-variable">code</span> <span class="hljs-operator">=</span> <span class="hljs-string">&quot;mock code&quot;</span>;

        <span class="hljs-comment">/*
         * 用授权码换取访问令牌（access_token）
         * 调用getAccessToken方法，传入code和redirectURI（需与授权时使用的地址一致）
         */</span>
        <span class="hljs-type">OAuthToken</span> <span class="hljs-variable">resp</span> <span class="hljs-operator">=</span> oauth.getAccessToken(code, redirectURI);
        System.out.println(resp);  <span class="hljs-comment">// 打印令牌信息，包含访问令牌、过期时间等</span>

        <span class="hljs-comment">/*
         * 获取请求日志ID，用于问题排查，从令牌响应对象中通过getLogID()方法获取
         */</span>
        System.out.println(resp.getLogID());

        <span class="hljs-comment">// 使用获取到的access_token初始化Coze客户端</span>
        <span class="hljs-type">CozeAPI</span> <span class="hljs-variable">coze</span> <span class="hljs-operator">=</span>
            <span class="hljs-keyword">new</span> <span class="hljs-title class_">CozeAPI</span>.Builder()
                <span class="hljs-comment">// 用access_token创建鉴权对象，access_token从OAuthToken对象的getAccessToken()方法获取</span>
                .auth(<span class="hljs-keyword">new</span> <span class="hljs-title class_">TokenAuth</span>(resp.getAccessToken()))
                <span class="hljs-comment">// 设置OpenAPI服务端点，由扣子编程固定提供的OpenAPI访问地址</span>
                .baseURL(cozeAPIBase)
                .build();

        <span class="hljs-comment">/*
         * 令牌过期时，使用refresh_token刷新令牌，refresh_token从OAuthToken对象的getRefreshToken()方法获取
         */</span>
        resp = oauth.refreshToken(resp.getRefreshToken());
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text=" /*
         * 授权流程说明：
         * 1. 前端引导用户访问扣子授权页面，用户完成授权后，扣子会重定向到redirectURI
         * 2. 重定向地址的Query参数中会携带code（授权码）和state（状态参数，用于防CSRF）
         * 3. 后端从Query中提取code，用于换取访问令牌
         */
        // 模拟从重定向地址的Query中获取到的授权码，用户授权后从redirectURI的Query参数（code）中提取
        String code = &quot;mock code&quot;;

        /*
         * 用授权码换取访问令牌（access_token）
         * 调用getAccessToken方法，传入code和redirectURI（需与授权时使用的地址一致）
         */
        OAuthToken resp = oauth.getAccessToken(code, redirectURI);
        System.out.println(resp);  // 打印令牌信息，包含访问令牌、过期时间等

        /*
         * 获取请求日志ID，用于问题排查，从令牌响应对象中通过getLogID()方法获取
         */
        System.out.println(resp.getLogID());

        // 使用获取到的access_token初始化Coze客户端
        CozeAPI coze =
            new CozeAPI.Builder()
                // 用access_token创建鉴权对象，access_token从OAuthToken对象的getAccessToken()方法获取
                .auth(new TokenAuth(resp.getAccessToken()))
                // 设置OpenAPI服务端点，由扣子编程固定提供的OpenAPI访问地址
                .baseURL(cozeAPIBase)
                .build();

        /*
         * 令牌过期时，使用refresh_token刷新令牌，refresh_token从OAuthToken对象的getRefreshToken()方法获取
         */
        resp = oauth.refreshToken(resp.getRefreshToken());" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ol>
<h2 id="49962f9d" tabindex="-1">配置 OAuth PKCE 授权流程</h2>
<p>如果选择使用 OAuth PKCE 方式完成授权，可参考以下流程及示例代码。完整的示例代码请参见 <a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/PKCEOAuthExample.java" target="_blank">PKCEOauthExample.java</a>。</p>
<ol data-style="0">
<li>
<p>创建 OAuth 应用。<br>
具体操作步骤可参考<a href="/developer_guides/oauth_pkce" target="_blank">OAuth PKCE</a>。成功创建 OAuth 应用后，你将获得客户端 ID 和重定向地址。</p>
</li>
<li>
<p>在代码中通过环境变量方式设置客户端 ID 和重定向地址。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java">    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">main</span><span class="hljs-params">(String[] args)</span> {
        <span class="hljs-comment">// 从环境变量中获取PKCE OAuth应用的重定向地址，创建PKCE类型OAuth应用时配置的前端回调地址</span>
        <span class="hljs-type">String</span> <span class="hljs-variable">redirectURI</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_PKCE_OAUTH_REDIRECT_URI&quot;</span>);
        
        <span class="hljs-comment">// 从环境变量中获取PKCE OAuth应用的客户端ID，创建PKCE类型OAuth应用时平台生成的唯一标识符</span>
        <span class="hljs-type">String</span> <span class="hljs-variable">clientID</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_PKCE_OAUTH_CLIENT_ID&quot;</span>);

        <span class="hljs-comment">// 创建PKCEOAuthClient实例，配置应用信息</span>
        <span class="hljs-type">PKCEOAuthClient</span> <span class="hljs-variable">oauth</span> <span class="hljs-operator">=</span>
            <span class="hljs-keyword">new</span> <span class="hljs-title class_">PKCEOAuthClient</span>.PKCEOAuthBuilder()
                .clientID(clientID)  <span class="hljs-comment">// 传入客户端ID，即从环境变量获取的PKCE应用客户端ID</span>
                <span class="hljs-comment">// 设置扣子授权服务器端点，由扣子编程固定提供的授权服务地址</span>
                .baseURL(Consts.COZE_CN_BASE_URLCOZE_COM_BASE_URL)
                .build();
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="    public static void main(String[] args) {
        // 从环境变量中获取PKCE OAuth应用的重定向地址，创建PKCE类型OAuth应用时配置的前端回调地址
        String redirectURI = System.getenv(&quot;COZE_PKCE_OAUTH_REDIRECT_URI&quot;);
        
        // 从环境变量中获取PKCE OAuth应用的客户端ID，创建PKCE类型OAuth应用时平台生成的唯一标识符
        String clientID = System.getenv(&quot;COZE_PKCE_OAUTH_CLIENT_ID&quot;);

        // 创建PKCEOAuthClient实例，配置应用信息
        PKCEOAuthClient oauth =
            new PKCEOAuthClient.PKCEOAuthBuilder()
                .clientID(clientID)  // 传入客户端ID，即从环境变量获取的PKCE应用客户端ID
                // 设置扣子授权服务器端点，由扣子编程固定提供的授权服务地址
                .baseURL(Consts.COZE_CN_BASE_URLCOZE_COM_BASE_URL)
                .build();" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>在代码中实现 OAuth PKCE 授权流程。<br>
客户端生成一个随机值 code_verifier，并根据指定算法将其转换为 code_challenge，算法通常使用 SHA-256 算法。然后基于回调地址、code_challenge 和 code_challenge_method，生成一个授权链接。<br>
其中 code_verifier 会由 SDK 生成，并与 URL 一起返回给调用方。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"><span class="hljs-type">GetPKCEAuthURLResp</span> <span class="hljs-variable">oauthURL</span> <span class="hljs-operator">=</span>
    oauth.genOAuthURL(redirectURI, <span class="hljs-string">&quot;state&quot;</span>, PKCEOAuthClient.CodeChallengeMethod.S256);
System.out.println(oauthURL);
<span class="hljs-comment">// The code verifier generated by the SDK</span>
System.out.println(oauthURL.getCodeVerifier());
<span class="hljs-comment">// URL that users need to click.</span>
System.out.println(oauthURL.getAuthorizationURL());
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="GetPKCEAuthURLResp oauthURL =
    oauth.genOAuthURL(redirectURI, &quot;state&quot;, PKCEOAuthClient.CodeChallengeMethod.S256);
System.out.println(oauthURL);
// The code verifier generated by the SDK
System.out.println(oauthURL.getCodeVerifier());
// URL that users need to click.
System.out.println(oauthURL.getAuthorizationURL());" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>完成授权。<br>
开发者应该引导用户打开这个授权链接。当用户同意授权时，扣子编程会将页面重定向到开发者配置的回调地址，开发者可以获取这个 code，换取访问密钥。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"><span class="hljs-comment">/*
After the user clicks the authorization consent button, the coze web page will redirect
to the redirect address configured in the authorization link and carry the authorization
code and state parameters in the address via the query string.

Get from the query of the redirect interface: query.get(&#x27;code&#x27;)
* */</span>
<span class="hljs-type">String</span> <span class="hljs-variable">code</span> <span class="hljs-operator">=</span> <span class="hljs-string">&quot;mock code&quot;</span>;
 
<span class="hljs-comment">/*
After obtaining the code after redirection, the interface to exchange the code for a
token can be invoked to generate the coze access_token of the authorized user.
The developer should use code verifier returned by genOAuthURL() method
* */</span>
<span class="hljs-type">OAuthToken</span> <span class="hljs-variable">resp</span> <span class="hljs-operator">=</span> oauth.getAccessToken(code, redirectURI, oauthURL.getCodeVerifier());
System.out.println(resp);

<span class="hljs-comment">// use the access token to init Coze client</span>
<span class="hljs-type">CozeAPI</span> <span class="hljs-variable">coze</span> <span class="hljs-operator">=</span>
    <span class="hljs-keyword">new</span> <span class="hljs-title class_">CozeAPI</span>.Builder()
        .auth(<span class="hljs-keyword">new</span> <span class="hljs-title class_">TokenAuth</span>(resp.getAccessToken()))
        .baseURL(cozeAPIBase)
        .build();
<span class="hljs-comment">// When the token expires, you can also refresh and re-obtain the token</span>
resp = oauth.refreshToken(resp.getRefreshToken());
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="/*
After the user clicks the authorization consent button, the coze web page will redirect
to the redirect address configured in the authorization link and carry the authorization
code and state parameters in the address via the query string.

Get from the query of the redirect interface: query.get(&apos;code&apos;)
* */
String code = &quot;mock code&quot;;
 
/*
After obtaining the code after redirection, the interface to exchange the code for a
token can be invoked to generate the coze access_token of the authorized user.
The developer should use code verifier returned by genOAuthURL() method
* */
OAuthToken resp = oauth.getAccessToken(code, redirectURI, oauthURL.getCodeVerifier());
System.out.println(resp);

// use the access token to init Coze client
CozeAPI coze =
    new CozeAPI.Builder()
        .auth(new TokenAuth(resp.getAccessToken()))
        .baseURL(cozeAPIBase)
        .build();
// When the token expires, you can also refresh and re-obtain the token
resp = oauth.refreshToken(resp.getRefreshToken());" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ol>
<h2 id="319c9071" tabindex="-1">配置 OAuth 设备码授权流程</h2>
<p>如果选择使用 OAuth 设备码方式完成授权，可参考以下流程及示例代码。完整的示例代码请参见 <a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/DevicesOAuthExample.java" target="_blank">DevicesOAuthExample.java</a>。</p>
<ol data-style="0">
<li>
<p>创建 OAuth 应用。<br>
具体操作步骤可参考<a href="/developer_guides/oauth_device_code" target="_blank">OAuth 设备授权</a>。成功创建 OAuth 应用后，你将获得客户端 ID。</p>
</li>
<li>
<p>在代码中通过环境变量方式设置客户端 ID。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">main</span><span class="hljs-params">(String[] args)</span> {
    <span class="hljs-comment">// 从环境变量获取设备授权的客户端ID，创建设备码类型OAuth应用时平台生成的唯一标识符</span>
    <span class="hljs-type">String</span> <span class="hljs-variable">clientID</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_DEVICE_OAUTH_CLIENT_ID&quot;</span>);

    <span class="hljs-comment">// 创建设备授权客户端实例</span>
    <span class="hljs-type">DeviceOAuthClient</span> <span class="hljs-variable">oauth</span> <span class="hljs-operator">=</span>
        <span class="hljs-keyword">new</span> <span class="hljs-title class_">DeviceOAuthClient</span>.DeviceOAuthBuilder()
            .clientID(clientID)  <span class="hljs-comment">// 传入客户端ID，即从环境变量获取的设备应用客户端ID</span>
            <span class="hljs-comment">// 设置授权服务器端点，由扣子编程固定提供的授权服务地址</span>
            .baseURL(Consts.COZE_CN_BASE_URLCOZE_COM_BASE_URL)
            .build();
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="public static void main(String[] args) {
    // 从环境变量获取设备授权的客户端ID，创建设备码类型OAuth应用时平台生成的唯一标识符
    String clientID = System.getenv(&quot;COZE_DEVICE_OAUTH_CLIENT_ID&quot;);

    // 创建设备授权客户端实例
    DeviceOAuthClient oauth =
        new DeviceOAuthClient.DeviceOAuthBuilder()
            .clientID(clientID)  // 传入客户端ID，即从环境变量获取的设备应用客户端ID
            // 设置授权服务器端点，由扣子编程固定提供的授权服务地址
            .baseURL(Consts.COZE_CN_BASE_URLCOZE_COM_BASE_URL)
            .build();" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>通过 OAuth 设备码授权流程获得访问密钥。<br>
应用程序需要调用扣子编程 OpenAPI 生成设备代码，以获取 user_code 和 device_code。通过 user_code 生成授权链接，并引导用户打开该链接、填写 user_code、同意授权。应用程序调用扣子编程 OpenAPI，通过 device_code 生成访问密钥。<br>
如果用户尚未授权或拒绝了授权，接口将抛出异常并返回特定的错误代码。用户同意授权后，接口将成功并返回访问密钥。<br>
SDK 已经拼接了 URL，直接将 SDK 返回的 URL 交给用户打开即可。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"><span class="hljs-comment">/*
 * 第一步：获取设备码和用户码
 */</span>
<span class="hljs-comment">// 获取设备码响应对象，包含设备码、用户码、授权URL等信息</span>
<span class="hljs-type">DeviceAuthResp</span> <span class="hljs-variable">codeResp</span> <span class="hljs-operator">=</span> oauth.getDeviceCode();
System.out.println(codeResp);  <span class="hljs-comment">// 打印设备码相关信息</span>

<span class="hljs-comment">// 设备码，用于轮询访问令牌，从DeviceAuthResp对象的getDeviceCode()方法获取</span>
System.out.println(codeResp.getDeviceCode());

<span class="hljs-comment">// 用户需要访问的授权页面URL，用户输入user_code的页面地址，从DeviceAuthResp获取</span>
System.out.println(codeResp.getVerificationURL());
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="/*
 * 第一步：获取设备码和用户码
 */
// 获取设备码响应对象，包含设备码、用户码、授权URL等信息
DeviceAuthResp codeResp = oauth.getDeviceCode();
System.out.println(codeResp);  // 打印设备码相关信息

// 设备码，用于轮询访问令牌，从DeviceAuthResp对象的getDeviceCode()方法获取
System.out.println(codeResp.getDeviceCode());

// 用户需要访问的授权页面URL，用户输入user_code的页面地址，从DeviceAuthResp获取
System.out.println(codeResp.getVerificationURL());" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>应用程序还需要使用 device_code 来轮询扣子编程 OpenAPI 以获取访问密钥。<br>
Coze SDK for Java 已经封装了这部分代码，并处理了不同的返回错误代码。开发者只需要调用 get_access_token 即可。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"><span class="hljs-comment">/*
 * 第二步：轮询获取访问令牌
 */</span>
<span class="hljs-keyword">try</span> {
    <span class="hljs-comment">// 轮询获取访问令牌，传入device_code和自动轮询标识（true为自动处理）</span>
    <span class="hljs-type">OAuthToken</span> <span class="hljs-variable">resp</span> <span class="hljs-operator">=</span> oauth.getAccessToken(codeResp.getDeviceCode(), <span class="hljs-literal">true</span>);
    System.out.println(resp);  <span class="hljs-comment">// 用户授权成功后返回的访问令牌</span>

    <span class="hljs-comment">// 用access_token初始化Coze客户端</span>
    <span class="hljs-type">CozeAPI</span> <span class="hljs-variable">coze</span> <span class="hljs-operator">=</span>
        <span class="hljs-keyword">new</span> <span class="hljs-title class_">CozeAPI</span>.Builder()
            .auth(<span class="hljs-keyword">new</span> <span class="hljs-title class_">TokenAuth</span>(resp.getAccessToken()))  <span class="hljs-comment">// 传入访问令牌</span>
            .baseURL(cozeAPIBase)  <span class="hljs-comment">// 设置OpenAPI服务端点</span>
            .build();

    <span class="hljs-comment">// 令牌过期时刷新，refresh_token从OAuthToken对象获取</span>
    resp = oauth.refreshToken(resp.getRefreshToken());

} <span class="hljs-keyword">catch</span> (CozeAuthException e) {
    <span class="hljs-comment">// 处理授权失败的情况</span>
    <span class="hljs-keyword">if</span> (AuthErrorCode.ACCESS_DENIED.equals(e.getCode())) {
        <span class="hljs-comment">// 用户拒绝授权，需引导用户重新操作</span>
        System.out.println(<span class="hljs-string">&quot;access denied&quot;</span>);
    } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (AuthErrorCode.EXPIRED_TOKEN.equals(e.getCode())) {
        <span class="hljs-comment">// 令牌过期，需重新获取设备码并引导用户授权</span>
        System.out.println(<span class="hljs-string">&quot;expired token&quot;</span>);
    } <span class="hljs-keyword">else</span> {
        e.printStackTrace();
    }
} <span class="hljs-keyword">catch</span> (Exception e) {
    e.printStackTrace();
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="/*
 * 第二步：轮询获取访问令牌
 */
try {
    // 轮询获取访问令牌，传入device_code和自动轮询标识（true为自动处理）
    OAuthToken resp = oauth.getAccessToken(codeResp.getDeviceCode(), true);
    System.out.println(resp);  // 用户授权成功后返回的访问令牌

    // 用access_token初始化Coze客户端
    CozeAPI coze =
        new CozeAPI.Builder()
            .auth(new TokenAuth(resp.getAccessToken()))  // 传入访问令牌
            .baseURL(cozeAPIBase)  // 设置OpenAPI服务端点
            .build();

    // 令牌过期时刷新，refresh_token从OAuthToken对象获取
    resp = oauth.refreshToken(resp.getRefreshToken());

} catch (CozeAuthException e) {
    // 处理授权失败的情况
    if (AuthErrorCode.ACCESS_DENIED.equals(e.getCode())) {
        // 用户拒绝授权，需引导用户重新操作
        System.out.println(&quot;access denied&quot;);
    } else if (AuthErrorCode.EXPIRED_TOKEN.equals(e.getCode())) {
        // 令牌过期，需重新获取设备码并引导用户授权
        System.out.println(&quot;expired token&quot;);
    } else {
        e.printStackTrace();
    }
} catch (Exception e) {
    e.printStackTrace();
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ol>
<h2 id="53e78d5f" tabindex="-1">配置 OAuth JWT 授权流程</h2>
<p>如果选择使用 OAuth JWT 方式完成授权，可参考以下流程及示例代码。完整的示例代码请参见 <a href="https://github.com/coze-dev/coze-java/blob/main/example/src/main/java/example/auth/JWTOAuthExample.java" target="_blank">JWTsOauthExample.java</a>。</p>
<ol data-style="0">
<li>
<p>创建 OAuth 应用并授权。<br>
具体操作步骤可参考<a href="/developer_guides/oauth_jwt" target="_blank">OAuth JWT 授权（开发者）</a>。成功创建 OAuth 应用后，你将获得客户端 ID、公钥和私钥。你需要妥善保管公钥和私钥，以免数据泄露引发安全风险。</p>
</li>
<li>
<p>在代码中通过环境变量方式设置客户端 ID、公钥和私钥。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java">
<span class="hljs-type">String</span> <span class="hljs-variable">jwtOauthClientID</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_JWT_OAUTH_CLIENT_ID&quot;</span>);  <span class="hljs-comment">// 从环境变量获取JWT授权的客户端ID，创建JWT类型OAuth应用时平台生成的唯一标识符</span>
<span class="hljs-type">String</span> <span class="hljs-variable">jwtOauthPrivateKey</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_JWT_OAUTH_PRIVATE_KEY&quot;</span>);   <span class="hljs-comment">// 从环境变量获取 OAuth 应用的私钥，用于签署JWT，可以在 OAuth 应用页面找到这个应用，在操作列单击编辑图标，进入配置页面下载私钥文件</span>
<span class="hljs-type">String</span> <span class="hljs-variable">jwtOauthPrivateKeyFilePath</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_JWT_OAUTH_PRIVATE_KEY_FILE_PATH&quot;</span>);  <span class="hljs-comment">// 从环境变量获取私钥文件路径，私钥文件在本地的存储路径，开发者自行指定</span>
<span class="hljs-type">String</span> <span class="hljs-variable">jwtOauthPublicKeyID</span> <span class="hljs-operator">=</span> System.getenv(<span class="hljs-string">&quot;COZE_JWT_OAUTH_PUBLIC_KEY_ID&quot;</span>);  <span class="hljs-comment">// 从环境变量获取 OAuth 应用的公钥ID，可以在 OAuth 应用页面找到这个应用，在操作列单击编辑图标，进入配置页面查看公钥指纹。</span>

<span class="hljs-type">JWTOAuthClient</span> <span class="hljs-variable">oauth</span> <span class="hljs-operator">=</span> <span class="hljs-literal">null</span>;
<span class="hljs-keyword">try</span> {
  jwtOauthPrivateKey =
      <span class="hljs-keyword">new</span> <span class="hljs-title class_">String</span>(
          Files.readAllBytes(Paths.get(jwtOauthPrivateKeyFilePath)), StandardCharsets.UTF_8);
} <span class="hljs-keyword">catch</span> (IOException e) {
  e.printStackTrace();
}

<span class="hljs-comment">/*
The jwt oauth type requires using private to be able to issue a jwt token, and through
the jwt token, apply for an access_token from the coze service. The sdk encapsulates
this procedure, and only needs to use get_access_token to obtain the access_token under
the jwt oauth process.
Generate the authorization token
The default ttl is 900s, and developers can customize the expiration time, which can be
set up to 24 hours at most.
* */</span>
<span class="hljs-keyword">try</span> {
  oauth =
      <span class="hljs-keyword">new</span> <span class="hljs-title class_">JWTOAuthClient</span>.JWTOAuthBuilder()
          .clientID(jwtOauthClientID)  <span class="hljs-comment">//OAuth应用的客户端ID，创建 OAuth 应用时获取的客户端 ID。</span>
          .privateKey(jwtOauthPrivateKey)   <span class="hljs-comment">// OAuth 应用的私钥。</span>
          .publicKey(jwtOauthPublicKeyID)  <span class="hljs-comment">//OAuth 应用的公钥指纹。</span>
          .baseURL(Consts.COZE_CN_BASE_URL)  <span class="hljs-comment">//扣子 OpenAPI 的 Endpoint。</span>
          .build();
} <span class="hljs-keyword">catch</span> (Exception e) {
  e.printStackTrace();
  <span class="hljs-keyword">return</span>;
}
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="
String jwtOauthClientID = System.getenv(&quot;COZE_JWT_OAUTH_CLIENT_ID&quot;);  // 从环境变量获取JWT授权的客户端ID，创建JWT类型OAuth应用时平台生成的唯一标识符
String jwtOauthPrivateKey = System.getenv(&quot;COZE_JWT_OAUTH_PRIVATE_KEY&quot;);   // 从环境变量获取 OAuth 应用的私钥，用于签署JWT，可以在 OAuth 应用页面找到这个应用，在操作列单击编辑图标，进入配置页面下载私钥文件
String jwtOauthPrivateKeyFilePath = System.getenv(&quot;COZE_JWT_OAUTH_PRIVATE_KEY_FILE_PATH&quot;);  // 从环境变量获取私钥文件路径，私钥文件在本地的存储路径，开发者自行指定
String jwtOauthPublicKeyID = System.getenv(&quot;COZE_JWT_OAUTH_PUBLIC_KEY_ID&quot;);  // 从环境变量获取 OAuth 应用的公钥ID，可以在 OAuth 应用页面找到这个应用，在操作列单击编辑图标，进入配置页面查看公钥指纹。

JWTOAuthClient oauth = null;
try {
  jwtOauthPrivateKey =
      new String(
          Files.readAllBytes(Paths.get(jwtOauthPrivateKeyFilePath)), StandardCharsets.UTF_8);
} catch (IOException e) {
  e.printStackTrace();
}

/*
The jwt oauth type requires using private to be able to issue a jwt token, and through
the jwt token, apply for an access_token from the coze service. The sdk encapsulates
this procedure, and only needs to use get_access_token to obtain the access_token under
the jwt oauth process.
Generate the authorization token
The default ttl is 900s, and developers can customize the expiration time, which can be
set up to 24 hours at most.
* */
try {
  oauth =
      new JWTOAuthClient.JWTOAuthBuilder()
          .clientID(jwtOauthClientID)  //OAuth应用的客户端ID，创建 OAuth 应用时获取的客户端 ID。
          .privateKey(jwtOauthPrivateKey)   // OAuth 应用的私钥。
          .publicKey(jwtOauthPublicKeyID)  //OAuth 应用的公钥指纹。
          .baseURL(Consts.COZE_CN_BASE_URL)  //扣子 OpenAPI 的 Endpoint。
          .build();
} catch (Exception e) {
  e.printStackTrace();
  return;
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
<li>
<p>应用程序通过公钥和私钥签署 JWT，并通过扣子编程提供的 API 获取访问密钥。<br>
Coze SDK for Java 封装了这一过程，你只需要在OAuth JWT 流程中使用 get_access_token 来获取访问密钥即可。</p>

<div style="position: relative">
	<pre><code class="hljs language-Java"><span class="hljs-keyword">try</span> {
  <span class="hljs-type">OAuthToken</span> <span class="hljs-variable">resp</span> <span class="hljs-operator">=</span> oauth.getAccessToken();
  System.out.println(resp);
} <span class="hljs-keyword">catch</span> (Exception e) {
  e.printStackTrace();
}
<span class="hljs-comment">/*
The jwt oauth process does not support refreshing tokens. When the token expires,
just directly call get_access_token to generate a new token.
* */</span>
<span class="hljs-type">CozeAPI</span> <span class="hljs-variable">coze</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">CozeAPI</span>.Builder().auth(<span class="hljs-keyword">new</span> <span class="hljs-title class_">JWTOAuth</span>(oauth)).baseURL(Consts.COZE_CN_BASE_URL).build();
<span class="hljs-comment">// you can also specify the scope and session for it</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="try {
  OAuthToken resp = oauth.getAccessToken();
  System.out.println(resp);
} catch (Exception e) {
  e.printStackTrace();
}
/*
The jwt oauth process does not support refreshing tokens. When the token expires,
just directly call get_access_token to generate a new token.
* */
CozeAPI coze = new CozeAPI.Builder().auth(new JWTOAuth(oauth)).baseURL(Consts.COZE_CN_BASE_URL).build();
// you can also specify the scope and session for it" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</li>
</ol>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/developer_guides_java_installation" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">安装 Java SDK</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/developer_guides_java_getting_started" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">快速开始</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="配置方式" href="#73e164bf" data-href="#73e164bf">配置方式</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="配置个人访问密钥（PAT）" href="#364507dd" data-href="#364507dd">配置个人访问密钥（PAT）</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="配置 OAuth 授权码流程" href="#b1e6ad12" data-href="#b1e6ad12">配置 OAuth 授权码流程</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="配置 OAuth PKCE 授权流程" href="#49962f9d" data-href="#49962f9d">配置 OAuth PKCE 授权流程</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="配置 OAuth 设备码授权流程" href="#319c9071" data-href="#319c9071">配置 OAuth 设备码授权流程</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="配置 OAuth JWT 授权流程" href="#53e78d5f" data-href="#53e78d5f">配置 OAuth JWT 授权流程</a></div></div></div></div></div></div></div></div>
</body></html>