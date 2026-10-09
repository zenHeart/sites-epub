<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><meta name="renderer" content="webkit"><meta name="layoutmode" content="standard"><meta name="imagemode" content="force"><meta name="wap-font-scale" content="no"><meta name="format-detection" content="telephone=no"><title data-react-helmet="true">查询工作流基本信息</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/5956.1729cb00c0.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.ca52691239.css" rel="stylesheet" /><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet" />  <link data-react-helmet="true" rel="canonical" href="https://docs.coze.cn/developer_guides_get_workflow_info"/><link data-react-helmet="true" rel="icon" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><link data-react-helmet="true" rel="alternate" type="text/markdown" href="/developer_guides_get_workflow_info.md"/><link data-react-helmet="true" rel="alternate" type="text/plain" href="/llms.txt"/>
  <meta data-react-helmet="true" name="google-site-verification" content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE"/>
  
<meta name="baidu-site-verification" content="codeva-mJmA0HNtAv" /></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a href="https://www.coze.cn" class="brand-qR7tMP" target="_blank" rel="noreferrer"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" alt="扣子" class="siteIcon-qohRRP"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" href="/what_is_coze" data-discover="true">扣子</a><a class="tab-JssokC" href="/guides_welcome" data-discover="true">扣子编程</a><a class="tab-JssokC" href="/ppt-plugin" data-discover="true">教程</a><a class="tab-JssokC" href="/coze_pro_billing_overview" data-discover="true">定价</a><a class="tab-JssokC activeTab-g8RDKO" href="/developer_guides_get_workflow_info" data-discover="true"><span>资源</span><span class="arrow-nKMrBv"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)"></path></g><defs><linearGradient id="paint0_linear_1944_44928" x1="1.3335" y1="15.0401" x2="15.0379" y2="15.0401" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_1944_44928"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><input readonly="" class="input-tjtw6Q" type="text" placeholder="搜索"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" viewBox="5 5 22 22" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="white"></rect></clipPath></defs></svg></span><span class="topic-rag-logo-dark"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clipPath id="clip0_2_6"><rect width="48" height="48" fill="#262E3B"></rect></clipPath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg width="24" height="24" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="starGradient" x1="1.25" y1="35.735" x2="29.602" y2="29.277" gradientUnits="userSpaceOnUse"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></linearGradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" r="1.2" fill="url(#starGradient)" fill-opacity="0.8"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-close"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><linearGradient id="paint0_linear_7153_28960" x1="2.04126" y1="13.4163" x2="12.5415" y2="13.4163" gradientUnits="userSpaceOnUse"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></linearGradient><clipPath id="clip0_7153_28960"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button style="border-radius:4px;height:28px" class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" type="button" disabled=""><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-plus"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button style="color:#c7ccd6" class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" type="button" disabled=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor"></path></g><defs><clipPath id="clip0_7153_32885"><rect width="18" height="18" fill="white" transform="translate(3 3)"></rect></clipPath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true"><div class="content-KOLZ20"><div id="tree-node-6a3b97434bdbc784e3ce84ce" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a55df9a4bdbc784e3c9738f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf30d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf317" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf31d" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf325" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf334" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf32e" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf35a" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf362" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8e614bdbc784e3cce185" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3e2c" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3ece" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_coze_api_overview" data-discover="true"><span class="nodeTitle-ONnqtP" title="API 介绍">API 介绍</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ed4" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_changelog" data-discover="true"><span class="nodeTitle-ONnqtP" title="更新日志">更新日志</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3edc" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_preparation" data-discover="true"><span class="nodeTitle-ONnqtP" title="准备工作">准备工作</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ee3" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_api_playground" data-discover="true"><span class="nodeTitle-ONnqtP" title="API Playground">API Playground</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e32" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="鉴权">鉴权</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3e6a" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能体和应用">智能体和应用</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ee9" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="工作空间">工作空间</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3eef" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="文件夹">文件夹</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3ef7" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="企业/组织">企业/组织</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3efe" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="会话与消息">会话与消息</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f04" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="对话">对话</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f0c" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct expanded-jh8lWp"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div id="tree-node-6a3b8b8d4bdbc784e3cc3fd0" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_workflow_run" data-discover="true"><span class="nodeTitle-ONnqtP" title="执行工作流">执行工作流</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc409a" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_workflow_stream_run" data-discover="true"><span class="nodeTitle-ONnqtP" title="执行工作流（流式响应）">执行工作流（流式响应）</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc40a3" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_workflow_resume" data-discover="true"><span class="nodeTitle-ONnqtP" title="恢复运行工作流（流式响应）">恢复运行工作流（流式响应）</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc40aa" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_resume_workflow" data-discover="true"><span class="nodeTitle-ONnqtP" title="恢复运行工作流">恢复运行工作流</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc40b1" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_workflow_history" data-discover="true"><span class="nodeTitle-ONnqtP" title="查询工作流异步运行结果">查询工作流异步运行结果</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc415c" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_workflow_chat" data-discover="true"><span class="nodeTitle-ONnqtP" title="执行对话流">执行对话流</span></a></div><div id="tree-node-6a3b8b8e4bdbc784e3cc42f0" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_get_node_execute_history_response" data-discover="true"><span class="nodeTitle-ONnqtP" title="查询输出节点的执行结果">查询输出节点的执行结果</span></a></div><div id="tree-node-6a3b8b8e4bdbc784e3cc42f8" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_get_workflow_list" data-discover="true"><span class="nodeTitle-ONnqtP" title="查询工作流列表">查询工作流列表</span></a></div><div id="tree-node-6a3b8b8e4bdbc784e3cc434c" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX active-dE_WV_" style="margin-left:56px" href="/developer_guides_get_workflow_info" data-discover="true"><span class="nodeTitle-ONnqtP" title="查询工作流基本信息">查询工作流基本信息</span></a></div><div id="tree-node-6a3b8b8e4bdbc784e3cc4353" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_list_workflow_version" data-discover="true"><span class="nodeTitle-ONnqtP" title="查询工作流的版本列表">查询工作流的版本列表</span></a></div><div id="tree-node-6a3b8b8e4bdbc784e3cc435b" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_switch_workflow_develop_mode" data-discover="true"><span class="nodeTitle-ONnqtP" title="开启或关闭工作流多人协作">开启或关闭工作流多人协作</span></a></div><div id="tree-node-6a3b8b8e4bdbc784e3cc43b9" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_add_workflow_collaborator" data-discover="true"><span class="nodeTitle-ONnqtP" title="添加工作流协作者">添加工作流协作者</span></a></div><div id="tree-node-6a3b8b8e4bdbc784e3cc43c1" class="nodeWrapper-woTZn5" data-tree-level="3"><a class="nodeContent-GigwSX" style="margin-left:56px" href="/developer_guides_remove_workflow_collaborator" data-discover="true"><span class="nodeTitle-ONnqtP" title="删除工作流协作者">删除工作流协作者</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f13" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="文件">文件</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f1a" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能音视频">智能音视频</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f35" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="知识库">知识库</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f3b" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="数据库">数据库</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f43" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="插件">插件</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f49" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="变量">变量</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f51" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="渠道">渠道</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f58" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="用量限额">用量限额</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f5f" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="账单与权益">账单与权益</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f66" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="回调">回调</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f84" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_coze_error_codes" data-discover="true"><span class="nodeTitle-ONnqtP" title="错误码">错误码</span></a></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f99" class="nodeWrapper-woTZn5" data-tree-level="2"><div to="/" class="nodeContent-GigwSX" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="API 教程">API 教程</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3f8a" class="nodeWrapper-woTZn5" data-tree-level="2"><a class="nodeContent-GigwSX" style="margin-left:40px" href="/developer_guides_api_faq" data-discover="true"><span class="nodeTitle-ONnqtP" title="API 常见问题">API 常见问题</span></a></div></div></div><div id="tree-node-6a3b8b8d4bdbc784e3cc3fa8" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8bc84bdbc784e3cc529d" class="nodeWrapper-woTZn5" data-tree-level="1"><div to="/" class="nodeContent-GigwSX" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8b8e4bdbc784e3cc445f" class="nodeWrapper-woTZn5" data-tree-level="1"><a class="nodeContent-GigwSX" style="margin-left:24px" href="/developer_guides_coze_cli" data-discover="true"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf33f" class="nodeWrapper-woTZn5" data-tree-level="0"><div to="/" class="nodeContent-GigwSX" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div id="tree-node-6a3b8ae84bdbc784e3cbf369" class="nodeWrapper-woTZn5" data-tree-level="0"><a class="nodeContent-GigwSX" style="margin-left:8px" href="/guides_FAQ" data-discover="true"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div class="resizeHandle-lop5IL" role="separator" aria-orientation="vertical" aria-label="拖拽调整目录宽度"></div></div><div data-topic-doc="true" class="container-h8FsmA"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>API 参考</span><span class="separator-KB9yMa">/</span><span>工作流</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">查询工作流基本信息</span></div><div class="titleContainer-hr8uxx"><h1 id="doc_title" class="title-C1b1pA" data-h0="true">查询工作流基本信息</h1><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="copyIcon-iTB4A1 arco-icon arco-icon-copy"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg><span>复制页面</span></div><div class="moreButton-ZJ3qDg"><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="arco-icon arco-icon-down"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>查询工作流的基本信息，包括工作流名称、描述、创建者信息等。</p>
<h2 id="基础信息" tabindex="-1">基础信息</h2>
<!-- @cols-width: 180,680 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 180px;" /><col style="width: 680px;" /></colgroup><thead>
<tr>
<th>
<p><strong>请求方式</strong></p>
</th>
<th>
<p>GET</p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>请求地址</strong></p>
</td>
<td>

<div style="position: relative">
	<pre><code class="hljs language-Plain">https://api.coze.cn/v1/workflows/:workflow_id
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="https://api.coze.cn/v1/workflows/:workflow_id" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
</td>
</tr>
<tr>
<td>
<p><strong>权限</strong></p>
</td>
<td>
<p><code>getMetaData</code><br>
确保调用该接口使用的访问令牌开通了 <code>getMetaData</code> 权限，详细信息参考<a href="https://docs.coze.cn/developer_guides/authentication" target="_blank">鉴权方式</a>。</p>
</td>
</tr>
<tr>
<td>
<p><strong>接口说明</strong></p>
</td>
<td>
<p>查询工作流基本信息。</p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="请求参数" tabindex="-1">请求参数</h2>
<h3 id="Header" tabindex="-1">Header</h3>
<!-- @cols-width: 144,165,551 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 144px;" /><col style="width: 165px;" /><col style="width: 551px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>取值</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Authorization</p>
</td>
<td>
<p>Bearer <em>$Access_Token</em></p>
</td>
<td>
<p>用于验证客户端身份的访问令牌。你可以在扣子编程中生成访问令牌，详细信息，参考<a href="https://docs.coze.cn/developer_guides/preparation" target="_blank">准备工作</a>。</p>
</td>
</tr>
<tr>
<td>
<p>Content-Type</p>
</td>
<td>
<p>application/json</p>
</td>
<td>
<p>解释请求正文的方式。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="Path" tabindex="-1">Path</h3>
<!-- @cols-width: 134,122,87,165,339 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 134px;" /><col style="width: 122px;" /><col style="width: 87px;" /><col style="width: 165px;" /><col style="width: 339px;" /></colgroup><thead>
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
<p><strong>示例</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>workflow_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>必选</p>
</td>
<td>
<p>73505836754923***</p>
</td>
<td>
<p>工作流 ID。<br>
进入工作流编排页面，在页面 URL 中，workflow 参数后的数字就是 Workflow ID。例如 <a href="https://www.coze.com/work_flow?space_id=42463***&amp;workflow_id=73505836754923" target="_blank">https://www.coze.com/work_flow?space_id=42463***&amp;workflow_id=73505836754923</a>***，Workflow ID 为 73505836754923***。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="Query" tabindex="-1">Query</h3>
<!-- @cols-width: 199,120,86,163,278 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 199px;" /><col style="width: 120px;" /><col style="width: 86px;" /><col style="width: 163px;" /><col style="width: 278px;" /></colgroup><thead>
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
<p><strong>示例</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>include_input_output</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>可选</p>
</td>
<td>
<p>true</p>
</td>
<td>
<p>是否在返回结果中返回输入和输出参数的结构体。</p>
<ul data-style="0">
<li><code>true</code>：返回输入输出参数结构体</li>
<li><code>false</code>：不返回输入输出参数结构体</li>
</ul>
<p>默认值为 <code>false</code>。</p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="返回参数" tabindex="-1">返回参数</h2>
<!-- @cols-width: 292,143,159,266 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 292px;" /><col style="width: 143px;" /><col style="width: 159px;" /><col style="width: 266px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>示例</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>code</p>
</td>
<td>
<p>Long</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>调用状态码。0 表示调用成功，其他值表示调用失败，你可以通过 msg 字段判断详细的错误原因。</p>
</td>
</tr>
<tr>
<td>
<p>msg</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>&quot;&quot;</p>
</td>
<td>
<p>状态信息。API 调用失败时可通过此字段查看详细错误信息。<br>
状态码为 0 时，msg 默认为空。</p>
</td>
</tr>
<tr>
<td>
<p>data</p>
</td>
<td>
<p>Object of <a href="#workflowinfo">WorkflowInfo</a></p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>工作流的详细信息。</p>
</td>
</tr>
<tr>
<td>
<p>detail</p>
</td>
<td>
<p>Object of <a href="#responsedetail">ResponseDetail</a></p>
</td>
<td>
<p>{&quot;logid&quot;:&quot;20241210152726467C48D89D6DB2****&quot;}</p>
</td>
<td>
<p>包含本次请求的日志信息，用于问题排查和技术支持。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="workflowinfo" tabindex="-1">WorkflowInfo</h3>
<!-- @cols-width: 170,147,250,293 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 170px;" /><col style="width: 147px;" /><col style="width: 250px;" /><col style="width: 293px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>示例</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>input</p>
</td>
<td>
<p>Object of <a href="#openapiworkflowinput">OpenAPIWorkflowInput</a></p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>工作流开始节点的输入参数的结构体。</p>
</td>
</tr>
<tr>
<td>
<p>output</p>
</td>
<td>
<p>Object of <a href="#openapiworkflowoutput">OpenAPIWorkflowOutput</a></p>
</td>
<td>
<p>{ &quot;parameters&quot;: { &quot;arr_obj_num&quot;: { &quot;required&quot;: false, &quot;type&quot;: &quot;number&quot; } }, &quot;terminate_plan&quot;: &quot;use_answer_content&quot;, &quot;content&quot;: &quot;输出为{{output}}&quot; }</p>
</td>
<td>
<p>工作流结束节点的输出参数的结构体。</p>
</td>
</tr>
<tr>
<td>
<p>workflow_detail</p>
</td>
<td>
<p>Object of <a href="#openapiworkflowbasic">OpenAPIWorkflowBasic</a></p>
</td>
<td>
<p>{&quot;app_id&quot;:&quot;744208683**&quot;,&quot;creator&quot;:{&quot;id&quot;:&quot;2478774393***&quot;,&quot;name&quot;:&quot;user41833***&quot;},&quot;icon_url&quot;:&quot;<a href="https://example.com/icon/workflow_123.png" target="_blank">https://example.com/icon/workflow_123.png</a>&quot;,&quot;created_at&quot;:1700000000,&quot;updated_at&quot;:&quot;1701234567&quot;,&quot;description&quot;:&quot;工作流测试&quot;,&quot;workflow_id&quot;:&quot;73505836754923***&quot;,&quot;workflow_name&quot;:&quot;workflow_example&quot;}</p>
</td>
<td>
<p>工作流的详细信息。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="openapiworkflowinput" tabindex="-1">OpenAPIWorkflowInput</h3>
<!-- @cols-width: 170,147,226,317 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 170px;" /><col style="width: 147px;" /><col style="width: 226px;" /><col style="width: 317px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>示例</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>parameters</p>
</td>
<td>
<p>JSON Map</p>
</td>
<td>
<p>{ &quot;CONVERSATION_NAME&quot;: { &quot;required&quot;: false, &quot;description&quot;: &quot;&quot;, &quot;default_value&quot;: &quot;&quot;, &quot;type&quot;: &quot;string&quot; }}</p>
</td>
<td>
<p>开始节点的输入参数结构体。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="parameters" tabindex="-1">Parameters</h3>
<!-- @cols-width: 140,148,165,407 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 140px;" /><col style="width: 148px;" /><col style="width: 165px;" /><col style="width: 407px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>示例</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>string</p>
</td>
<td>
<p>该参数的类型。</p>
</td>
</tr>
<tr>
<td>
<p>items</p>
</td>
<td>
<p>Object of <a href="#openapiparameter">OpenAPIParameter</a></p>
</td>
<td>
<p>{&quot;type&quot;:&quot;image&quot;}</p>
</td>
<td>
<p>当参数类型为 <code>array</code> 时，该字段用于定义数组元素的子类型。</p>
</td>
</tr>
<tr>
<td>
<p>required</p>
</td>
<td>
<p>Boolean</p>
</td>
<td>
<p>true</p>
</td>
<td>
<p>标识输入参数是否为必填项。</p>
<ul data-style="0">
<li><code>true</code>：该参数为必填项。</li>
<li><code>false</code>：该参数为可选项。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>properties</p>
</td>
<td>
<p>JSON Map</p>
</td>
<td>
<p>{ &quot;arr_obj_num&quot;: { &quot;required&quot;: false, &quot;type&quot;: &quot;number&quot; } }</p>
</td>
<td>
<p>当参数类型为 <code>object</code>时，该字段用于定义对象类型的子参数信息，采用键值对（key-value）结构，其中 key 为子参数的名称，value 为该子参数的定义信息（包含类型、是否必填等属性）。</p>
</td>
</tr>
<tr>
<td>
<p>description</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>上传的图片。</p>
</td>
<td>
<p>该参数的描述信息。</p>
</td>
</tr>
<tr>
<td>
<p>default_value</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>-</p>
</td>
<td>
<p>该参数配置的默认值。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="openapiworkflowoutput" tabindex="-1">OpenAPIWorkflowOutput</h3>
<!-- @cols-width: 155,147,164,394 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 155px;" /><col style="width: 147px;" /><col style="width: 164px;" /><col style="width: 394px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>示例</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>content</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>数量为{{arr_obj_num}}</p>
</td>
<td>
<p>工作流结束节点返回文本时，智能体回复内容的结构。仅当 <code>terminate_plan</code> 为 <code>use_answer_content</code> 时会返回。</p>
</td>
</tr>
<tr>
<td>
<p>parameters</p>
</td>
<td>
<p>JSON Map</p>
</td>
<td>
<p>{ &quot;output&quot;: { &quot;type&quot;: &quot;string&quot; } }</p>
</td>
<td>
<p>工作流结束节点输出变量的数组。以键值对形式存储，格式为<code> { &quot;变量名称&quot;: { &quot;type&quot;: &quot;变量类型&quot; } }</code>。</p>
</td>
</tr>
<tr>
<td>
<p>terminate_plan</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>return_variables</p>
</td>
<td>
<p>结束节点的返回类型，枚举值：</p>
<ul data-style="0">
<li><code>return_variables</code>：返回变量。</li>
<li><code>use_answer_content</code>：返回文本。</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><h3 id="openapiworkflowbasic" tabindex="-1">OpenAPIWorkflowBasic</h3>
<!-- @cols-width: 157,147,164,392 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 157px;" /><col style="width: 147px;" /><col style="width: 164px;" /><col style="width: 392px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>示例</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>app_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>744208683**</p>
</td>
<td>
<p>工作流关联的应用 ID。若工作流未关联任何应用，则该字段值为 <code>0</code>。</p>
</td>
</tr>
<tr>
<td>
<p>creator</p>
</td>
<td>
<p>Object of <a href="#openapiuserinfo">OpenAPIUserInfo</a></p>
</td>
<td>
<p>{&quot;id&quot;:&quot;2478774393***&quot;,&quot;name&quot;:&quot;user41833***&quot;}</p>
</td>
<td>
<p>工作流创建者的信息，包含创建者的用户 ID 和用户名。</p>
</td>
</tr>
<tr>
<td>
<p>icon_url</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p><a href="https://example.com/icon/workflow_123.png" target="_blank">https://example.com/icon/workflow_123.png</a></p>
</td>
<td>
<p>工作流图标的 URL 地址。</p>
</td>
</tr>
<tr>
<td>
<p>created_at</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>1752060786</p>
</td>
<td>
<p>工作流的创建时间，以 Unix 时间戳表示，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>updated_at</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>1752060827</p>
</td>
<td>
<p>工作流的最后更新时间，以 Unix 时间戳表示，单位为秒。</p>
</td>
</tr>
<tr>
<td>
<p>description</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>生成音乐的工作流</p>
</td>
<td>
<p>工作流的描述。</p>
</td>
</tr>
<tr>
<td>
<p>workflow_id</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>73505836754923***</p>
</td>
<td>
<p>工作流 ID。</p>
</td>
</tr>
<tr>
<td>
<p>workflow_name</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>workflow_example</p>
</td>
<td>
<p>工作流名称。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="openapiuserinfo" tabindex="-1">OpenAPIUserInfo</h3>
<!-- @cols-width: 100,149,166,445 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 149px;" /><col style="width: 166px;" /><col style="width: 445px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>示例</strong></p>
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
<p>2478774393***</p>
</td>
<td>
<p>工作流创建者的扣子用户 UID。</p>
</td>
</tr>
<tr>
<td>
<p>name</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>user41833***</p>
</td>
<td>
<p>工作流创建者的扣子用户名。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="responsedetail" tabindex="-1">ResponseDetail</h3>
<!-- @cols-width: 100,149,166,445 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;" /><col style="width: 149px;" /><col style="width: 166px;" /><col style="width: 445px;" /></colgroup><thead>
<tr>
<th>
<p><strong>参数</strong></p>
</th>
<th>
<p><strong>类型</strong></p>
</th>
<th>
<p><strong>示例</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>logid</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>20241210152726467C48D89D6DB2****</p>
</td>
<td>
<p>本次请求的日志 ID。如果遇到异常报错场景，且反复重试仍然报错，可以根据此 logid 及错误码联系扣子团队获取帮助。详细说明可参考<a href="https://docs.coze.cn/guides/help_and_support" target="_blank">获取帮助和技术支持</a>。</p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="示例" tabindex="-1">示例</h2>
<h3 id="请求示例" tabindex="-1">请求示例</h3>

<div style="position: relative">
	<pre><code class="hljs language-JSON">curl --location --request GET &#x27;https<span class="hljs-punctuation">:</span><span class="hljs-comment">//api.coze.cn/v1/workflows/7493*****453978?include_input_output=true&#x27; \</span>
--header &#x27;Authorization<span class="hljs-punctuation">:</span> Bearer pat_h******&#x27; \
--header &#x27;Content-Type<span class="hljs-punctuation">:</span> application/json&#x27;
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="curl --location --request GET &apos;https://api.coze.cn/v1/workflows/7493*****453978?include_input_output=true&apos; \
--header &apos;Authorization: Bearer pat_h******&apos; \
--header &apos;Content-Type: application/json&apos;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h3 id="返回示例" tabindex="-1">返回示例</h3>

<div style="position: relative">
	<pre><code class="hljs language-JSON"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">&quot;data&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;workflow_detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;workflow_name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;workflow_image&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;app_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;7493481****8294&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;creator&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;44246792*****&quot;</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;name&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;张三&quot;</span>
      <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;updated_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1747983675</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;workflow_id&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;750712******91219&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;description&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;统计图片数量&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;icon_url&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;https://*****pi.com/ocean-cloud-tos/plugin_icon/chatflow-icon.png?****&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;created_at&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">1747888248</span>
    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;input&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;parameters&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;CONVERSATION_NAME&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;required&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">false</span></span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;description&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;default_value&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;string&quot;</span>
        <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
        <span class="hljs-attr">&quot;USER_INPUT&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;string&quot;</span><span class="hljs-punctuation">,</span>
          <span class="hljs-attr">&quot;required&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-literal"><span class="hljs-keyword">false</span></span>
        <span class="hljs-punctuation">}</span>
      <span class="hljs-punctuation">}</span>
    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">&quot;output&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">&quot;parameters&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
        <span class="hljs-attr">&quot;arr_obj_num&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
          <span class="hljs-attr">&quot;type&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;number&quot;</span>
        <span class="hljs-punctuation">}</span>
      <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;terminate_plan&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;use_answer_content&quot;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">&quot;content&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;数量为{{arr_obj_num}}&quot;</span>
    <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;code&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-number">0</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;msg&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;&quot;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">&quot;detail&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">{</span>
    <span class="hljs-attr">&quot;logid&quot;</span><span class="hljs-punctuation">:</span> <span class="hljs-string">&quot;2025071621341*******4D&quot;</span>
  <span class="hljs-punctuation">}</span>
<span class="hljs-punctuation">}</span>
</code></pre>

	<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="{
  &quot;data&quot;: {
    &quot;workflow_detail&quot;: {
      &quot;workflow_name&quot;: &quot;workflow_image&quot;,
      &quot;app_id&quot;: &quot;7493481****8294&quot;,
      &quot;creator&quot;: {
        &quot;id&quot;: &quot;44246792*****&quot;,
        &quot;name&quot;: &quot;张三&quot;
      },
      &quot;updated_at&quot;: 1747983675,
      &quot;workflow_id&quot;: &quot;750712******91219&quot;,
      &quot;description&quot;: &quot;统计图片数量&quot;,
      &quot;icon_url&quot;: &quot;https://*****pi.com/ocean-cloud-tos/plugin_icon/chatflow-icon.png?****&quot;,
      &quot;created_at&quot;: 1747888248
    },
    &quot;input&quot;: {
      &quot;parameters&quot;: {
        &quot;CONVERSATION_NAME&quot;: {
          &quot;required&quot;: false,
          &quot;description&quot;: &quot;&quot;,
          &quot;default_value&quot;: &quot;&quot;,
          &quot;type&quot;: &quot;string&quot;
        },
        &quot;USER_INPUT&quot;: {
          &quot;type&quot;: &quot;string&quot;,
          &quot;required&quot;: false
        }
      }
    },
    &quot;output&quot;: {
      &quot;parameters&quot;: {
        &quot;arr_obj_num&quot;: {
          &quot;type&quot;: &quot;number&quot;
        }
      },
      &quot;terminate_plan&quot;: &quot;use_answer_content&quot;,
      &quot;content&quot;: &quot;数量为{{arr_obj_num}}&quot;
    }
  },
  &quot;code&quot;: 0,
  &quot;msg&quot;: &quot;&quot;,
  &quot;detail&quot;: {
    &quot;logid&quot;: &quot;2025071621341*******4D&quot;
  }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
		<span style="font-size: 21px; opacity: 0.4;" class="topic-code-block__copy-icon"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
	</button>
</div>
<h2 id="错误码" tabindex="-1">错误码</h2>
<p>如果成功调用扣子编程的 API，返回信息中 code 字段为 0。如果状态码为其他值，则表示接口调用失败。此时 msg 字段中包含详细错误信息，你可以参考<a href="https://www.coze.cn/docs/developer_guides/coze_error_codes" target="_blank">错误码</a>文档查看对应的解决方法。</p>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK "></span><span>有帮助</span></button><button type="button" class="feedbackButton-GuivRC "><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm " href="/developer_guides_get_workflow_list" data-discover="true"><div class="cardLabel-sDu1uC "><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12 ">查询工作流列表</div></a><a class="card-T4zaCm nextCard-lFoioT" href="/developer_guides_list_workflow_version" data-discover="true"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 48 48" aria-hidden="true" focusable="false" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">查询工作流的版本列表</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="基础信息" href="#基础信息" data-href="#基础信息">基础信息</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="请求参数" href="#请求参数" data-href="#请求参数">请求参数</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="Header" href="#Header" data-href="#Header">Header</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="Path" href="#Path" data-href="#Path">Path</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="Query" href="#Query" data-href="#Query">Query</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="返回参数" href="#返回参数" data-href="#返回参数">返回参数</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="WorkflowInfo" href="#workflowinfo" data-href="#workflowinfo">WorkflowInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="OpenAPIWorkflowInput" href="#openapiworkflowinput" data-href="#openapiworkflowinput">OpenAPIWorkflowInput</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="Parameters" href="#parameters" data-href="#parameters">Parameters</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="OpenAPIWorkflowOutput" href="#openapiworkflowoutput" data-href="#openapiworkflowoutput">OpenAPIWorkflowOutput</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="OpenAPIWorkflowBasic" href="#openapiworkflowbasic" data-href="#openapiworkflowbasic">OpenAPIWorkflowBasic</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="OpenAPIUserInfo" href="#openapiuserinfo" data-href="#openapiuserinfo">OpenAPIUserInfo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="ResponseDetail" href="#responsedetail" data-href="#responsedetail">ResponseDetail</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="示例" href="#示例" data-href="#示例">示例</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="请求示例" href="#请求示例" data-href="#请求示例">请求示例</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" title="返回示例" href="#返回示例" data-href="#返回示例">返回示例</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" title="错误码" href="#错误码" data-href="#错误码">错误码</a></div></div></div></div></div></div></div></div>
</body></html>