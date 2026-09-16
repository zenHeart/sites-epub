<!DOCTYPE html>
<html><head><meta charset="utf-8"/><meta content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no" name="viewport"/><meta content="ie=edge" http-equiv="x-ua-compatible"/><meta content="webkit" name="renderer"/><meta content="standard" name="layoutmode"/><meta content="force" name="imagemode"/><meta content="no" name="wap-font-scale"/><meta content="telephone=no" name="format-detection"/><title data-react-helmet="true">集成音视频 Realtime Web SDK</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/4760.77ece367d4.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.782417a8ae.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet"/> <link data-react-helmet="true" href="https://docs.coze.cn/dev_how_to_guides_Realtime_web" rel="canonical"/><link data-react-helmet="true" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" rel="icon"/><link data-react-helmet="true" href="/dev_how_to_guides_Realtime_web.md" rel="alternate" type="text/markdown"/><link data-react-helmet="true" href="/llms.txt" rel="alternate" type="text/plain"/>
<meta content="本文档介绍集成扣子Realtime Web SDK，将AI智能体集成到Web应用。先说明准备工作，如发布智能体、获取访问密钥、准备开发环境。还给出跑通示例项目的方法，包括项目源码及创建运行步骤，核心功能有实时语音交互等，助开发者快速集成。" data-react-helmet="true" name="description"/><meta content="扣子Realtime Web SDK,AI智能体,Web应用集成,音视频链路,鉴权" data-react-helmet="true" name="keywords"/><meta content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE" data-react-helmet="true" name="google-site-verification"/>
<meta content="codeva-mJmA0HNtAv" name="baidu-site-verification"/></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a class="brand-qR7tMP" href="https://www.coze.cn" rel="noreferrer" target="_blank"><img alt="扣子" class="siteIcon-qohRRP" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" data-discover="true" href="/what_is_coze">扣子</a><a class="tab-JssokC" data-discover="true" href="/guides_welcome">扣子编程</a><a class="tab-JssokC" data-discover="true" href="/ppt-plugin">教程</a><a class="tab-JssokC" data-discover="true" href="/coze_pro_billing_overview">定价</a><a class="tab-JssokC activeTab-g8RDKO" data-discover="true" href="/dev_how_to_guides_Realtime_web"><span>资源</span><span class="arrow-nKMrBv"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg fill="none" height="16" viewbox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)" fill-rule="evenodd"></path></g><defs><lineargradient gradientunits="userSpaceOnUse" id="paint0_linear_1944_44928" x1="1.3335" x2="15.0379" y1="15.0401" y2="15.0401"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></lineargradient><clippath id="clip0_1944_44928"><rect fill="white" height="16" width="16"></rect></clippath></defs></svg><input class="input-tjtw6Q" placeholder="搜索" readonly="" type="text"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" fill="currentColor" viewbox="5 5 22 22" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg fill="none" height="48" viewbox="0 0 48 48" width="48" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clippath id="clip0_2_6"><rect fill="white" height="48" width="48"></rect></clippath></defs></svg></span><span class="topic-rag-logo-dark"><svg fill="none" height="48" viewbox="0 0 48 48" width="48" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clippath id="clip0_2_6"><rect fill="#262E3B" height="48" width="48"></rect></clippath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg height="24" role="img" viewbox="0 0 40 40" width="24" xmlns="http://www.w3.org/2000/svg"><defs><lineargradient gradientunits="userSpaceOnUse" id="starGradient" x1="1.25" x2="29.602" y1="35.735" y2="29.277"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></lineargradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" fill="url(#starGradient)" fill-opacity="0.8" r="1.2"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg aria-hidden="true" class="arco-icon arco-icon-close" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg fill="none" height="14" viewbox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><lineargradient gradientunits="userSpaceOnUse" id="paint0_linear_7153_28960" x1="2.04126" x2="12.5415" y1="13.4163" y2="13.4163"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></lineargradient><clippath id="clip0_7153_28960"><rect fill="white" height="14" width="14"></rect></clippath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" disabled="" style="border-radius:4px;height:28px" type="button"><svg aria-hidden="true" class="arco-icon arco-icon-plus" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" disabled="" style="color:#c7ccd6" type="button"><svg fill="none" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor" fill-rule="evenodd"></path></g><defs><clippath id="clip0_7153_32885"><rect fill="white" height="18" transform="translate(3 3)" width="18"></rect></clippath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true" style="width:300px"><div class="content-KOLZ20"><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b97434bdbc784e3ce84ce"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a55df9a4bdbc784e3c9738f"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf30d"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf317"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf31d"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf325"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf334"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf32e"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf35a"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf362"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8e614bdbc784e3cce185"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8d4bdbc784e3cc3e2c"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8d4bdbc784e3cc3fa8"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8bc84bdbc784e3cc529d"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52a5"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_overview" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能音视频概述">智能音视频概述</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52ad"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_playground" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="体验智能音视频 Demo">体验智能音视频 Demo</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52b5"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_access" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="音视频接入方案对比">音视频接入方案对比</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52bf"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="基于 WebSocket 实现音频通话">基于 WebSocket 实现音频通话</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52c6"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="基于 RTC 实现音视频通话">基于 RTC 实现音视频通话</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc84bdbc784e3cc52cc"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_access_process" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="接入流程">接入流程</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc84bdbc784e3cc52d5"><a class="nodeContent-GigwSX active-dE_WV_" data-discover="true" href="/dev_how_to_guides_Realtime_web" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="集成音视频 Realtime Web SDK">集成音视频 Realtime Web SDK</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc84bdbc784e3cc52dd"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_iOS" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="集成音视频 Realtime iOS SDK">集成音视频 Realtime iOS SDK</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc84bdbc784e3cc5313"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_android" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="集成音视频 Realtime Android SDK">集成音视频 Realtime Android SDK</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc84bdbc784e3cc5345"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_embedded" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="集成音视频 Realtime 嵌入式 SDK">集成音视频 Realtime 嵌入式 SDK</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc84bdbc784e3cc534d"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_rtc_sdk" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="集成火山引擎 RTC SDK">集成火山引擎 RTC SDK</span></a></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52e5"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_audio_message" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="基于 HTTP 请求实现语音消息">基于 HTTP 请求实现语音消息</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52ed"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="语音与音色">语音与音色</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52f3"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="终端用户用量管控">终端用户用量管控</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc533c"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_faq" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="音视频常见问题">音视频常见问题</span></a></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8e4bdbc784e3cc445f"><a class="nodeContent-GigwSX" data-discover="true" href="/developer_guides_coze_cli" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf33f"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf369"><a class="nodeContent-GigwSX" data-discover="true" href="/guides_FAQ" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div aria-label="拖拽调整目录宽度" aria-orientation="vertical" class="resizeHandle-lop5IL" role="separator"></div></div><div class="container-h8FsmA" data-topic-doc="true" style="width:calc(100% - 300px);--anchor-width:260px"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>音视频</span><span class="separator-KB9yMa">/</span><span>基于 RTC 实现音视频通话</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">集成音视频 Realtime Web SDK</span></div><div class="titleContainer-hr8uxx"><h1 class="title-C1b1pA" data-h0="true" id="doc_title">集成音视频 Realtime Web SDK</h1><aside class="mdx-live-widget">
<p class="mdx-live-widget-label">Interactive explorer</p>
<p>This directory tree is interactive on the original page and cannot run inside an EPUB. Open it here: <a class="source-title" href="https://docs.coze.cn/dev_how_to_guides_Realtime_web#explore-the-directory" rel="external">https://docs.coze.cn/dev_how_to_guides_Realtime_web#explore-the-directory</a></p>
</aside><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg aria-hidden="true" class="copyIcon-iTB4A1 arco-icon arco-icon-copy" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg></div><div class="moreButton-ZJ3qDg"><svg aria-hidden="true" class="arco-icon arco-icon-down" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>本文档介绍如何集成扣子 Realtime Web SDK，将你在扣子编程中搭建的 AI 智能体集成到你的 Web 应用中。</p>
<p>扣子 Realtime Web SDK 封装了火山引擎 Web RTC 音视频链路相关 API，接入流程简洁高效。</p>
<h2 id="b5aea001" tabindex="-1">准备工作</h2>
<p>在开始集成 Realtime SDK 之前，你需要先完成以下准备工作。</p>
<!-- @cols-width: 158,658 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 158px;"/><col style="width: 658px;"/></colgroup><thead>
<tr>
<th><strong>操作</strong></th>
<th><strong>说明</strong></th>
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
<p>扣子 SDK 封装了多种鉴权方式，能够有效简化鉴权流程，你可以参考<a href="https://github.com/coze-dev/coze-js/tree/main/examples/coze-js-node/src/auth" target="_blank">鉴权示例代码</a>实现不同方式的 OAuth 认证，以获取和管理访问扣子 API 所需的令牌。</p>
</div>
</td>
</tr>
<tr>
<td>
<p>准备开发环境</p>
</td>
<td>
<ul data-style="0">
<li>安装Node.js 及 npm，具体请参见 <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm" target="_blank">Node.js</a><a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm" target="_blank"> 及 npm</a>，Node.js 版本需为 16 及以上版本。</li>
<li>安装最新稳定版本的<a href="https://www.google.com/chrome/" target="_blank"> Google Chrome 浏览器</a>。</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><h2 id="eb0752df" tabindex="-1">跑通示例项目</h2>
<h3 id="11a294fc" tabindex="-1">项目源码</h3>
<p>扣子提供基于 <a href="https://github.com/coze-dev/coze-js/tree/main/examples/realtime-quickstart-react" target="_blank">React 框架的示例项目源码</a>和 <a href="https://github.com/coze-dev/coze-js/tree/main/examples/realtime-quickstart-vue" target="_blank">Vue 框架的示例项目源码</a>。通过扣子的 Realtime API 和 Ant Design 的 UI 组件库，实现一个简单的语音通话应用。项目的核心功能包括实时语音交互、消息显示、视频通话（可选）以及麦克风控制等。</p>
<p>你可根据自身需求选择合适的框架。</p>
<h3 id="baeda4e1" tabindex="-1">创建并运行示例项目</h3>
<ol data-style="0">
<li>创建项目。<br/>
在本地终端执行以下命令，创建一个基于 Vite 和 React 的新项目，并进行初始化和安装依赖。
<div style="position: relative">
<pre><code class="hljs language-Bash">npm create vite@latest my-react-app -- --template react-ts
<span class="hljs-built_in">cd</span> my-react-app
npm install
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="npm create vite@latest my-react-app -- --template react-ts
cd my-react-app
npm install" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>安装依赖。<br/>
运行以下命令，安装项目所需的依赖包。其中， <code>antd</code>  是 Ant Design 的 React UI 组件库，用于构建高质量的用户界面：
<div style="position: relative">
<pre><code class="hljs language-Bash">npm install @coze/realtime-api @coze/api antd
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="npm install @coze/realtime-api @coze/api antd" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>创建基础文件。
<ol data-style="1">
<li>进入本地项目目录。</li>
<li>在 <code>src</code> 目录下创建新文件 <code>hooks.ts</code>，并添加以下内容：
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title function_">useTokenWithPat</span> = (<span class="hljs-params"></span>) =&gt; {
  <span class="hljs-comment">// 替换成你的 PAT</span>
  <span class="hljs-keyword">const</span> token = <span class="hljs-string">"你的PAT令牌"</span>; <span class="hljs-comment">// Access Token</span>
  <span class="hljs-keyword">return</span> {
    <span class="hljs-attr">getToken</span>: <span class="hljs-function">() =&gt;</span> token
  };
};
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text='export const useTokenWithPat = () =&gt; {
  // 替换成你的 PAT
  const token = "你的PAT令牌"; // Access Token
  return {
    getToken: () =&gt; token
  };
};' style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ol>
</li>
<li>在 <code>src</code> 目录中找到 <code>App.tsx</code>，并用以下内容完全替换原文件内容。<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>请将 <code>botId </code>参数的值替换为你的智能体 ID，并在 <code>App()</code> 中补全代码。完整的代码示例请参见<a href="https://github.com/coze-dev/coze-js/blob/main/examples/realtime-quickstart-react/src/App.tsx" target="_blank">示例项目中的App.tsx</a>。</p>
</div>
</li>
</ol>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { useRef, useState } <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> {
  <span class="hljs-title class_">EventNames</span>,
  <span class="hljs-title class_">RealtimeAPIError</span>,
  <span class="hljs-title class_">RealtimeClient</span>,
  <span class="hljs-title class_">RealtimeError</span>,
  <span class="hljs-title class_">RealtimeUtils</span>,
} <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/realtime-api'</span>;
<span class="hljs-keyword">import</span> { <span class="hljs-title class_">Button</span>, <span class="hljs-title class_">Space</span>, <span class="hljs-title class_">List</span>, message } <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> { <span class="hljs-title class_">CozeAPI</span>, <span class="hljs-variable constant_">COZE_CN_BASE_URL</span>, <span class="hljs-title class_">ChatEventType</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/api'</span>;
<span class="hljs-keyword">import</span> { useTokenWithPat } <span class="hljs-keyword">from</span> <span class="hljs-string">'./hooks'</span>;

<span class="hljs-comment">// ⚠️ 替换成你的智能体ID</span>
<span class="hljs-keyword">const</span> botId = <span class="hljs-string">'在这里填入你的智能体ID'</span>;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">App</span>(<span class="hljs-params"></span>) {
  <span class="hljs-comment">// ... [这里的代码请参考：https://github.com/coze-dev/coze-js/blob/main/examples/realtime-quickstart-react/src/App.tsx ] ...</span>
}

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">App</span>;
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { useRef, useState } from 'react';
import {
  EventNames,
  RealtimeAPIError,
  RealtimeClient,
  RealtimeError,
  RealtimeUtils,
} from '@coze/realtime-api';
import { Button, Space, List, message } from 'antd';
import { CozeAPI, COZE_CN_BASE_URL, ChatEventType } from '@coze/api';
import { useTokenWithPat } from './hooks';

// ⚠️ 替换成你的智能体ID
const botId = '在这里填入你的智能体ID';

function App() {
  // ... [这里的代码请参考：https://github.com/coze-dev/coze-js/blob/main/examples/realtime-quickstart-react/src/App.tsx ] ...
}

export default App;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<ol data-style="0" start="5">
<li>编辑文件 <code>src/main.tsx</code>，新增 <code>antd</code> 样式，删除 <code>import './index.css'</code>或清空 <code>index.css</code> 内容。
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">StrictMode</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> { createRoot } <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom/client'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'antd/dist/reset.css'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.tsx'</span>

<span class="hljs-title function_">createRoot</span>(<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'root'</span>)!).<span class="hljs-title function_">render</span>(
  <span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">StrictMode</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">App</span> /&gt;</span>
  <span class="hljs-tag">&lt;/<span class="hljs-name">StrictMode</span>&gt;</span></span>,
)
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import 'antd/dist/reset.css';
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  &lt;StrictMode&gt;
    &lt;App /&gt;
  &lt;/StrictMode&gt;,
)" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>运行项目。
<ol data-style="1">
<li>执行以下命令，在开发环境中启动项目。
<div style="position: relative">
<pre><code class="hljs language-Shell">npm run dev
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="npm run dev" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>等待浏览器自动打开项目页面。<br/>
项目页面通常部署在本地主机的 3000 端口，须保证此端口未被占用。浏览器会自动访问 <code>http://localhost:3000</code>。</li>
<li>在打开的项目页面中单击<strong>连接</strong>按钮，连接成功后即可开始对话。<br/>
<img alt="Image" height="287" loading="lazy" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/dc0f92e27a874cd68fcbddc5c68f7299~tplv-goo7wpa0wc-topic.webp" width="438"/></li>
</ol>
</li>
</ol>
<h3 id="9f8e12cc" tabindex="-1">源码解析</h3>
<p>本项目的核心代码位于 <a href="https://github.com/coze-dev/coze-js/blob/main/examples/realtime-quickstart-react/src/App.tsx" target="_blank">src/App.tsx</a>，其中包含了 Demo 项目的主要业务逻辑。Demo 项目结合 React、Coze API 和 Ant Design 构建了一个简单的语音通话界面。</p>
<h4 id="21fab927" tabindex="-1">基础设置和依赖</h4>
<p>以下代码是 React 组件的导入部分，通过以下代码引入必要的依赖和类型定义：</p>
<ul data-style="0">
<li>使用 React 的状态管理和引用功能来管理组件状态和 DOM 操作。</li>
<li>通过 <code>@coze/realtime-api</code> 和 <code>@coze/api</code> 与扣子智能体进行实时通信和交互。</li>
<li>使用 Ant Design 的 UI 组件来构建用户界面，提供良好的用户体验。</li>
</ul>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { useRef, useState } <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> {
  <span class="hljs-title class_">EventNames</span>,
  <span class="hljs-title class_">RealtimeAPIError</span>,
  <span class="hljs-title class_">RealtimeClient</span>,
  <span class="hljs-title class_">RealtimeError</span>,
  <span class="hljs-title class_">RealtimeUtils</span>,
} <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/realtime-api'</span>;
<span class="hljs-keyword">import</span> { <span class="hljs-title class_">Button</span>, <span class="hljs-title class_">Space</span>, <span class="hljs-title class_">List</span>, message } <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> { <span class="hljs-title class_">CozeAPI</span>, <span class="hljs-variable constant_">COZE_CN_BASE_URL</span>, <span class="hljs-title class_">ChatEventType</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/api'</span>;
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { useRef, useState } from 'react';
import {
  EventNames,
  RealtimeAPIError,
  RealtimeClient,
  RealtimeError,
  RealtimeUtils,
} from '@coze/realtime-api';
import { Button, Space, List, message } from 'antd';
import { CozeAPI, COZE_CN_BASE_URL, ChatEventType } from '@coze/api';" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h4 id="ebb85879" tabindex="-1">状态管理设置</h4>
<p>智能语音通话项目通常需要管理客户端的状态和行为。示例项目定义了一个名为 <code>App</code> 的 React 函数组件，通过 <code>useRef</code> 和 <code>useState</code> 钩子来管理组件状态和 DOM 操作。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">function</span> <span class="hljs-title function_">App</span>(<span class="hljs-params"></span>) {
  <span class="hljs-comment">// 客户端引用</span>
  <span class="hljs-keyword">const</span> clientRef = useRef&lt;<span class="hljs-title class_">RealtimeClient</span> | <span class="hljs-literal">null</span>&gt;(<span class="hljs-literal">null</span>);
  
  <span class="hljs-comment">// 核心状态管理</span>
  <span class="hljs-keyword">const</span> [messageList, setMessageList] = useState&lt;<span class="hljs-built_in">string</span>[]&gt;([]); <span class="hljs-comment">// 消息列表</span>
  <span class="hljs-keyword">const</span> [isConnecting, setIsConnecting] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">false</span>);     <span class="hljs-comment">// 连接状态</span>
  <span class="hljs-keyword">const</span> [isConnected, setIsConnected] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">false</span>);       <span class="hljs-comment">// 已连接状态</span>
  <span class="hljs-keyword">const</span> [audioEnabled, setAudioEnabled] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">true</span>);      <span class="hljs-comment">// 麦克风状态</span>
  <span class="hljs-keyword">const</span> [isSupportVideo, setIsSupportVideo] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">false</span>); <span class="hljs-comment">// 视频支持状态</span>
  <span class="hljs-comment">// ...其它代码</span>
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="function App() {
  // 客户端引用
  const clientRef = useRef&lt;RealtimeClient | null&gt;(null);
  
  // 核心状态管理
  const [messageList, setMessageList] = useState&lt;string[]&gt;([]); // 消息列表
  const [isConnecting, setIsConnecting] = useState(false);     // 连接状态
  const [isConnected, setIsConnected] = useState(false);       // 已连接状态
  const [audioEnabled, setAudioEnabled] = useState(true);      // 麦克风状态
  const [isSupportVideo, setIsSupportVideo] = useState(false); // 视频支持状态
  // ...其它代码
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h4 id="5db247bc" tabindex="-1">鉴权配置</h4>
<p>开发者可以选择不同的认证方式来获取访问令牌（Token）。本示例中通过个人访问令牌（PAT）来鉴权，生产环境请切换为更安全的 OAuth 2.0 认证方式。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript">  <span class="hljs-comment">// 选择一种认证方式</span>
  <span class="hljs-keyword">const</span> { getToken } = <span class="hljs-title function_">useTokenWithPat</span>();
  <span class="hljs-comment">// 其他认证方式：</span>
  <span class="hljs-comment">// const { getToken } = useTokenWithDevice();</span>
  <span class="hljs-comment">// const { getToken } = useTokenWithJWT();</span>
  <span class="hljs-comment">// const { getToken } = useTokenWithPKCE();</span>
  <span class="hljs-comment">// const { getToken } = useTokenWithWeb();</span>
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="  // 选择一种认证方式
  const { getToken } = useTokenWithPat();
  // 其他认证方式：
  // const { getToken } = useTokenWithDevice();
  // const { getToken } = useTokenWithJWT();
  // const { getToken } = useTokenWithPKCE();
  // const { getToken } = useTokenWithWeb();" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h4 id="b2918b9a" tabindex="-1">语音配置</h4>
<p>定义一个异步函数 <code>getVoices</code>，通过 OpenAPI 获取可用的音色列表。该步骤为可选操作，你使用系统默认音色，也可以在代码中输入音色 ID 修改为其他音色。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript">  <span class="hljs-keyword">async</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">getVoices</span>(<span class="hljs-params"></span>) {
    <span class="hljs-keyword">const</span> api = <span class="hljs-keyword">new</span> <span class="hljs-title class_">CozeAPI</span>({
      <span class="hljs-attr">token</span>: getToken,
      <span class="hljs-attr">baseURL</span>: <span class="hljs-variable constant_">COZE_CN_BASE_URL</span>,
      <span class="hljs-attr">allowPersonalAccessTokenInBrowser</span>: <span class="hljs-literal">true</span>,
    });
    <span class="hljs-keyword">const</span> voices = <span class="hljs-keyword">await</span> api.<span class="hljs-property">audio</span>.<span class="hljs-property">voices</span>.<span class="hljs-title function_">list</span>();
    <span class="hljs-keyword">return</span> voices.<span class="hljs-property">voice_list</span>;
  }
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="  async function getVoices() {
    const api = new CozeAPI({
      token: getToken,
      baseURL: COZE_CN_BASE_URL,
      allowPersonalAccessTokenInBrowser: true,
    });
    const voices = await api.audio.voices.list();
    return voices.voice_list;
  }" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h4 id="8263c110" tabindex="-1">客户端初始化</h4>
<p>定义一个异步函数 <code>initClient</code>，用于初始化一个实时通话客户端（<code>RealtimeClient</code>）。该函数包括检查设备权限、获取音色列表、配置客户端参数，并最终创建客户端实例。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript">  <span class="hljs-keyword">async</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">initClient</span>(<span class="hljs-params"></span>) {
    <span class="hljs-comment">// 检查设备权限</span>
    <span class="hljs-keyword">const</span> permission = <span class="hljs-keyword">await</span> <span class="hljs-title class_">RealtimeUtils</span>.<span class="hljs-title function_">checkDevicePermission</span>(<span class="hljs-literal">true</span>);
    <span class="hljs-keyword">if</span> (!permission.<span class="hljs-property">audio</span>) {
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Error</span>(<span class="hljs-string">'需要麦克风访问权限'</span>);
    }
    <span class="hljs-title function_">setIsSupportVideo</span>(permission.<span class="hljs-property">video</span>);

    <span class="hljs-comment">// 获取音色列表</span>
    <span class="hljs-keyword">const</span> voices = <span class="hljs-keyword">await</span> <span class="hljs-title function_">getVoices</span>();

    <span class="hljs-comment">// 初始化客户端</span>
    <span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> <span class="hljs-title class_">RealtimeClient</span>({
      <span class="hljs-attr">accessToken</span>: getToken,
      botId,
      <span class="hljs-attr">connectorId</span>: <span class="hljs-string">'1024'</span>,
      <span class="hljs-attr">voiceId</span>: voices.<span class="hljs-property">length</span> &gt; <span class="hljs-number">0</span> ? voices[<span class="hljs-number">0</span>].<span class="hljs-property">voice_id</span> : <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">allowPersonalAccessTokenInBrowser</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">videoConfig</span>: permission.<span class="hljs-property">video</span>
        ? { <span class="hljs-attr">renderDom</span>: <span class="hljs-string">'local-player'</span> }
        : <span class="hljs-literal">undefined</span>,
    });

    clientRef.<span class="hljs-property">current</span> = client;
    <span class="hljs-title function_">handleMessageEvent</span>(); <span class="hljs-comment">// 下面会实现</span>
  }
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="  async function initClient() {
    // 检查设备权限
    const permission = await RealtimeUtils.checkDevicePermission(true);
    if (!permission.audio) {
      throw new Error('需要麦克风访问权限');
    }
    setIsSupportVideo(permission.video);

    // 获取音色列表
    const voices = await getVoices();

    // 初始化客户端
    const client = new RealtimeClient({
      accessToken: getToken,
      botId,
      connectorId: '1024',
      voiceId: voices.length &gt; 0 ? voices[0].voice_id : undefined,
      allowPersonalAccessTokenInBrowser: true,
      debug: true,
      videoConfig: permission.video
        ? { renderDom: 'local-player' }
        : undefined,
    });

    clientRef.current = client;
    handleMessageEvent(); // 下面会实现
  }" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h4 id="d9819ed7" tabindex="-1">消息处理</h4>
<p>定义了一个异步函数 <code>handleMessageEvent</code>，它是一个消息事件监听器，用于处理从实时通话服务器接收到的消息事件，并根据事件类型更新消息列表。</p>
<p>本示例代码仅对部分消息类型进行了处理，主要用于展示实时语音交互中的文本消息内容。开发者可根据实际需求对消息处理逻辑进行扩展或调整。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript">  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handleMessageEvent</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">let</span> <span class="hljs-attr">lastEvent</span>: <span class="hljs-built_in">any</span>;

    clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">on</span>(<span class="hljs-title class_">EventNames</span>.<span class="hljs-property">ALL_SERVER</span>, <span class="hljs-function">(<span class="hljs-params">eventName, <span class="hljs-attr">event</span>: <span class="hljs-built_in">any</span></span>) =&gt;</span> {
      <span class="hljs-comment">// 只处理消息增量更新和完成事件</span>
      <span class="hljs-keyword">if</span> (
        event.<span class="hljs-property">event_type</span> !== <span class="hljs-title class_">ChatEventType</span>.<span class="hljs-property">CONVERSATION_MESSAGE_DELTA</span> &amp;&amp;
        event.<span class="hljs-property">event_type</span> !== <span class="hljs-title class_">ChatEventType</span>.<span class="hljs-property">CONVERSATION_MESSAGE_COMPLETED</span>
      ) {
        <span class="hljs-keyword">return</span>;
      }
      
      <span class="hljs-keyword">const</span> content = event.<span class="hljs-property">data</span>.<span class="hljs-property">content</span>;
      <span class="hljs-title function_">setMessageList</span>(<span class="hljs-function"><span class="hljs-params">prev</span> =&gt;</span> {
        <span class="hljs-comment">// 处理增量更新</span>
        <span class="hljs-keyword">if</span> (lastEvent?.<span class="hljs-property">event_type</span> === <span class="hljs-title class_">ChatEventType</span>.<span class="hljs-property">CONVERSATION_MESSAGE_DELTA</span>) {
          <span class="hljs-keyword">return</span> [...prev.<span class="hljs-title function_">slice</span>(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>), prev[prev.<span class="hljs-property">length</span> - <span class="hljs-number">1</span>] + content];
        }
        <span class="hljs-comment">// 处理新消息</span>
        <span class="hljs-keyword">if</span> (event.<span class="hljs-property">event_type</span> === <span class="hljs-title class_">ChatEventType</span>.<span class="hljs-property">CONVERSATION_MESSAGE_DELTA</span>) {
          <span class="hljs-keyword">return</span> [...prev, content];
        }
        <span class="hljs-keyword">return</span> prev;
      });
      lastEvent = event;
    });
  };
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="  const handleMessageEvent = async () =&gt; {
    let lastEvent: any;

    clientRef.current?.on(EventNames.ALL_SERVER, (eventName, event: any) =&gt; {
      // 只处理消息增量更新和完成事件
      if (
        event.event_type !== ChatEventType.CONVERSATION_MESSAGE_DELTA &amp;&amp;
        event.event_type !== ChatEventType.CONVERSATION_MESSAGE_COMPLETED
      ) {
        return;
      }
      
      const content = event.data.content;
      setMessageList(prev =&gt; {
        // 处理增量更新
        if (lastEvent?.event_type === ChatEventType.CONVERSATION_MESSAGE_DELTA) {
          return [...prev.slice(0, -1), prev[prev.length - 1] + content];
        }
        // 处理新消息
        if (event.event_type === ChatEventType.CONVERSATION_MESSAGE_DELTA) {
          return [...prev, content];
        }
        return prev;
      });
      lastEvent = event;
    });
  };" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h4 id="cc20150a" tabindex="-1">核心功能实现</h4>
<p>语音通话的核心功能包括连接、断开、打断以及麦克风控制。以下是相关功能函数的实现：</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript">  <span class="hljs-comment">// 连接</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handleConnect</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">try</span> {
      <span class="hljs-keyword">if</span> (!clientRef.<span class="hljs-property">current</span>) {
        <span class="hljs-keyword">await</span> <span class="hljs-title function_">initClient</span>();
      }
      <span class="hljs-keyword">await</span> clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">connect</span>();
      <span class="hljs-title function_">setIsConnected</span>(<span class="hljs-literal">true</span>);
    } <span class="hljs-keyword">catch</span> (error) {
      <span class="hljs-comment">// 错误处理...</span>
    }
  };

  <span class="hljs-comment">// 打断</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handleInterrupt</span> = (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">try</span> {
      clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">interrupt</span>();
    } <span class="hljs-keyword">catch</span> (error) {
      message.<span class="hljs-title function_">error</span>(<span class="hljs-string">'打断失败：'</span> + error);
    }
  };

  <span class="hljs-comment">// 断开连接</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handleDisconnect</span> = (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">try</span> {
      clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">disconnect</span>();
      clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">clearEventHandlers</span>();
      clientRef.<span class="hljs-property">current</span> = <span class="hljs-literal">null</span>;
      <span class="hljs-title function_">setIsConnected</span>(<span class="hljs-literal">false</span>);
    } <span class="hljs-keyword">catch</span> (error) {
      message.<span class="hljs-title function_">error</span>(<span class="hljs-string">'断开失败：'</span> + error);
    }
  };

  <span class="hljs-comment">// 麦克风控制</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">toggleMicrophone</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">try</span> {
      <span class="hljs-keyword">await</span> clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">setAudioEnable</span>(!audioEnabled);
      <span class="hljs-title function_">setAudioEnabled</span>(!audioEnabled);
    } <span class="hljs-keyword">catch</span> (error) {
      message.<span class="hljs-title function_">error</span>(<span class="hljs-string">'切换麦克风状态失败：'</span> + error);
    }
  };
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="  // 连接
  const handleConnect = async () =&gt; {
    try {
      if (!clientRef.current) {
        await initClient();
      }
      await clientRef.current?.connect();
      setIsConnected(true);
    } catch (error) {
      // 错误处理...
    }
  };

  // 打断
  const handleInterrupt = () =&gt; {
    try {
      clientRef.current?.interrupt();
    } catch (error) {
      message.error('打断失败：' + error);
    }
  };

  // 断开连接
  const handleDisconnect = () =&gt; {
    try {
      clientRef.current?.disconnect();
      clientRef.current?.clearEventHandlers();
      clientRef.current = null;
      setIsConnected(false);
    } catch (error) {
      message.error('断开失败：' + error);
    }
  };

  // 麦克风控制
  const toggleMicrophone = async () =&gt; {
    try {
      await clientRef.current?.setAudioEnable(!audioEnabled);
      setAudioEnabled(!audioEnabled);
    } catch (error) {
      message.error('切换麦克风状态失败：' + error);
    }
  };" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h4 id="97ee360b" tabindex="-1">UI 实现</h4>
<p>通过以下代码构建一个实时通话应用的用户界面，包括控制按钮、视频显示区域和消息显示区域。</p>
<p>整个组件的布局是一个居中的 <code>div</code>，包含以下部分：</p>
<ul data-style="0">
<li><strong>控制按钮</strong>：用于管理实时通话的连接状态和麦克风状态。</li>
<li><strong>视频显示区域</strong>：如果设备支持视频功能，则显示本地视频流。</li>
<li><strong>消息显示区域</strong>：显示实时语音回复的消息列表。</li>
</ul>
<div style="position: relative">
<pre><code class="hljs language-TypeScript">  <span class="hljs-keyword">return</span> (
    <span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">textAlign:</span> '<span class="hljs-attr">center</span>' }}&gt;</span>
      {/* 控制按钮 */}
      <span class="hljs-tag">&lt;<span class="hljs-name">Space</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">padding:</span> '<span class="hljs-attr">20px</span>' }}&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">{handleConnect}</span>&gt;</span>连接<span class="hljs-tag">&lt;/<span class="hljs-name">Button</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">{handleInterrupt}</span>&gt;</span>打断<span class="hljs-tag">&lt;/<span class="hljs-name">Button</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">Button</span> <span class="hljs-attr">danger</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">{handleDisconnect}</span>&gt;</span>断开<span class="hljs-tag">&lt;/<span class="hljs-name">Button</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">{toggleMicrophone}</span>&gt;</span>
          {audioEnabled ? '静音' : '取消静音'}
        <span class="hljs-tag">&lt;/<span class="hljs-name">Button</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-name">Space</span>&gt;</span>

      {/* 视频显示区域 */}
      {isSupportVideo &amp;&amp; (
        <span class="hljs-tag">&lt;<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"local-player"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{width:</span> <span class="hljs-attr">400</span>, <span class="hljs-attr">height:</span> <span class="hljs-attr">400</span>}}&gt;</span><span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span>
      )}

      {/* 消息显示区域 */}
      <span class="hljs-tag">&lt;<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{width:</span> '<span class="hljs-attr">400px</span>', <span class="hljs-attr">overflowY:</span> '<span class="hljs-attr">auto</span>'}}&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">h3</span>&gt;</span>实时语音回复<span class="hljs-tag">&lt;/<span class="hljs-name">h3</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">List</span>
          <span class="hljs-attr">dataSource</span>=<span class="hljs-string">{messageList}</span>
          <span class="hljs-attr">renderItem</span>=<span class="hljs-string">{(message,</span> <span class="hljs-attr">index</span>) =&gt;</span> (
            <span class="hljs-tag">&lt;<span class="hljs-name">List.Item</span> <span class="hljs-attr">key</span>=<span class="hljs-string">{index}</span>&gt;</span>{message}<span class="hljs-tag">&lt;/<span class="hljs-name">List.Item</span>&gt;</span>
          )}
        /&gt;
      <span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span>
    <span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span></span>
  );
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="  return (
    &lt;div style={{ textAlign: 'center' }}&gt;
      {/* 控制按钮 */}
      &lt;Space style={{ padding: '20px' }}&gt;
        &lt;Button type=&quot;primary&quot; onClick={handleConnect}&gt;连接&lt;/Button&gt;
        &lt;Button onClick={handleInterrupt}&gt;打断&lt;/Button&gt;
        &lt;Button danger onClick={handleDisconnect}&gt;断开&lt;/Button&gt;
        &lt;Button onClick={toggleMicrophone}&gt;
          {audioEnabled ? '静音' : '取消静音'}
        &lt;/Button&gt;
      &lt;/Space&gt;

      {/* 视频显示区域 */}
      {isSupportVideo &amp;&amp; (
        &lt;div id=&quot;local-player&quot; style={{width: 400, height: 400}}&gt;&lt;/div&gt;
      )}

      {/* 消息显示区域 */}
      &lt;div style={{width: '400px', overflowY: 'auto'}}&gt;
        &lt;h3&gt;实时语音回复&lt;/h3&gt;
        &lt;List
          dataSource={messageList}
          renderItem={(message, index) =&gt; (
            &lt;List.Item key={index}&gt;{message}&lt;/List.Item&gt;
          )}
        /&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  );" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h2 id="8540cce2" tabindex="-1">集成 SDK</h2>
<h3 id="9ffe794e" tabindex="-1">步骤一：安装依赖</h3>
<p>在开始集成之前，请确保项目环境已正确配置。运行以下命令安装项目所需的依赖包：</p>
<div style="position: relative">
<pre><code class="hljs language-Bash">npm install @coze/realtime-api @coze/api
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="npm install @coze/realtime-api @coze/api" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="fc37c5e0" tabindex="-1">步骤二：检查设备权限</h3>
<p>在初始化 SDK 之前，需确保当前项目已获取设备的麦克风访问权限。如果项目涉及视频通话功能，还需申请摄像头权限。以下是检查设备权限的代码示例：</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">RealtimeUtils</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">"@coze/realtime-api"</span>;

<span class="hljs-comment">// 检查设备权限</span>
<span class="hljs-keyword">const</span> checkVideo = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 如需申请摄像头权限，请设置为 true</span>
<span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> <span class="hljs-title class_">RealtimeUtils</span>.<span class="hljs-title function_">checkDevicePermission</span>();

<span class="hljs-comment">// 检查麦克风权限</span>
<span class="hljs-keyword">if</span> (!result.<span class="hljs-property">audio</span>) {
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Error</span>(<span class="hljs-string">"需要麦克风访问权限"</span>);
}
<span class="hljs-comment">// 如果申请摄像头权限，还需检查摄像头权限</span>
<span class="hljs-keyword">if</span> (checkVideo &amp;&amp; !result.<span class="hljs-property">video</span>) {
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Error</span>(<span class="hljs-string">"需要摄像头访问权限"</span>);
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text='import { RealtimeUtils } from "@coze/realtime-api";

// 检查设备权限
const checkVideo = false; // 如需申请摄像头权限，请设置为 true
const result = await RealtimeUtils.checkDevicePermission();

// 检查麦克风权限
if (!result.audio) {
    throw new Error("需要麦克风访问权限");
}
// 如果申请摄像头权限，还需检查摄像头权限
if (checkVideo &amp;&amp; !result.video) {
    throw new Error("需要摄像头访问权限");
}' style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="7c097d74" tabindex="-1">步骤三：初始化 SDK</h3>
<p>参考以下示例代码初始化 SDK。初始化时需要传入访问密钥 <code>accessToken</code>、智能体 ID <code>botId</code>和渠道 ID <code>connectorId</code>。</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">RealtimeClient</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">"@coze/realtime-api"</span>;

<span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> <span class="hljs-title class_">RealtimeClient</span>({
    <span class="hljs-attr">accessToken</span>: <span class="hljs-string">'your access token'</span>,   <span class="hljs-comment">// 替换为准备工作中获取的访问密钥</span>
    <span class="hljs-attr">botId</span>: <span class="hljs-string">'your bot id'</span>,              <span class="hljs-comment">// 替换为智能体 ID</span>
    <span class="hljs-attr">connectorId</span>: <span class="hljs-string">'1024'</span>,              <span class="hljs-comment">// 渠道 ID，固定为 1024</span>
    <span class="hljs-attr">allowPersonalAccessTokenInBrowser</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">// 可选：允许在浏览器中使用个人访问令牌</span>
});
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { RealtimeClient } from &quot;@coze/realtime-api&quot;;

const client = new RealtimeClient({
    accessToken: 'your access token',   // 替换为准备工作中获取的访问密钥
    botId: 'your bot id',              // 替换为智能体 ID
    connectorId: '1024',              // 渠道 ID，固定为 1024
    allowPersonalAccessTokenInBrowser: true,  // 可选：允许在浏览器中使用个人访问令牌
});" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<p>关键参数说明如下表所示。</p>
<!-- @cols-width: 127,686 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 127px;"/><col style="width: 686px;"/></colgroup><thead>
<tr>
<th><strong>参数</strong></th>
<th><strong>说明</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>accessToken</td>
<td>请替换为准备工作中获取的访问密钥，用于身份认证与鉴权。</td>
</tr>
<tr>
<td>
<p>botId</p>
</td>
<td>
<p>智能体 ID，获取方法如下：</p>
<p>进入智能体的开发页面，开发页面 URL 中 <code>bot</code> 参数后的数字即为智能体 ID。例如， URL 为<code>https://www.coze.cn/space/341****/bot/73428668*****</code>，则智能体 ID 为<code>73428668*****</code>。</p>
</td>
</tr>
<tr>
<td>connectorId</td>
<td>渠道 ID，固定为 1024。</td>
</tr>
</tbody>
</table>
</div><h3 id="72b4e187" tabindex="-1">步骤四：监听事件</h3>
<p>调用 <code>client.on</code> 监听事件。</p>
<p>SDK 提供了一系列信令事件，建议监听所有信令事件。以下是监听事件的代码示例：</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">EventNames</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">"@coze/realtime-api"</span>;

<span class="hljs-comment">// 监听所有事件</span>
client.<span class="hljs-title function_">on</span>(<span class="hljs-title class_">EventNames</span>.<span class="hljs-property">ALL</span>, <span class="hljs-function">(<span class="hljs-params">eventName, data</span>) =&gt;</span> {
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(eventName, data);
});
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text='import { EventNames } from "@coze/realtime-api";

// 监听所有事件
client.on(EventNames.ALL, (eventName, data) =&gt; {
    console.log(eventName, data);
});' style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="5a920583" tabindex="-1">步骤五：建立连接</h3>
<p>在开始对话前，调用 <code>client.connect</code> 方法建立客户端和服务端之间的连接。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">await</span> client.<span class="hljs-title function_">connect</span>(); 
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="await client.connect(); " style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="cc16fcee" tabindex="-1">步骤六：断开连接</h3>
<p>当结束对话时，调用 <code>client.disconnect</code> 方法，断开客户端和服务端之间的连接。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">await</span> client.<span class="hljs-title function_">disconnect</span>(); 
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="await client.disconnect(); " style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="cbaacab0" tabindex="-1">示例代码</h3>
<p>完整的示例代码如下。你也可以参考<a href="/dev_how_to_guides/Realtime_web#eb0752df" target="_blank">跑通示例项目</a>获取更多示例代码。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">EventNames</span>, <span class="hljs-title class_">RealtimeClient</span>, <span class="hljs-title class_">RealtimeUtils</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">"@coze/realtime-api"</span>;

<span class="hljs-keyword">async</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">initClient</span>(<span class="hljs-params"></span>) {
    <span class="hljs-keyword">try</span> {
        <span class="hljs-comment">// 1. 检查设备权限</span>
        <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> <span class="hljs-title class_">RealtimeUtils</span>.<span class="hljs-title function_">checkDevicePermission</span>();
        <span class="hljs-keyword">if</span> (!result.<span class="hljs-property">audio</span>) {
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Error</span>(<span class="hljs-string">"需要麦克风访问权限"</span>);
        }

        <span class="hljs-comment">// 2. 初始化客户端</span>
        <span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> <span class="hljs-title class_">RealtimeClient</span>({
            <span class="hljs-attr">accessToken</span>: <span class="hljs-string">'your access token'</span>,
            <span class="hljs-attr">botId</span>: <span class="hljs-string">'your bot id'</span>,
            <span class="hljs-attr">connectorId</span>: <span class="hljs-string">'1024'</span>,
            <span class="hljs-attr">allowPersonalAccessTokenInBrowser</span>: <span class="hljs-literal">true</span>,
        });

        <span class="hljs-comment">// 3. 配置事件监听</span>
        client.<span class="hljs-title function_">on</span>(<span class="hljs-title class_">EventNames</span>.<span class="hljs-property">ALL</span>, <span class="hljs-function">(<span class="hljs-params">eventName, data</span>) =&gt;</span> {
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(eventName, data);
        });

        <span class="hljs-comment">// 4. 建立与服务端的连接</span>
        <span class="hljs-keyword">await</span> client.<span class="hljs-title function_">connect</span>();
        
        <span class="hljs-comment">// 返回初始化完成的客户端实例</span>
        <span class="hljs-keyword">return</span> client;
    } <span class="hljs-keyword">catch</span> (error) {
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">error</span>(<span class="hljs-string">'初始化失败:'</span>, error);
        <span class="hljs-keyword">throw</span> error;
    }
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { EventNames, RealtimeClient, RealtimeUtils } from &quot;@coze/realtime-api&quot;;

async function initClient() {
    try {
        // 1. 检查设备权限
        const result = await RealtimeUtils.checkDevicePermission();
        if (!result.audio) {
            throw new Error(&quot;需要麦克风访问权限&quot;);
        }

        // 2. 初始化客户端
        const client = new RealtimeClient({
            accessToken: 'your access token',
            botId: 'your bot id',
            connectorId: '1024',
            allowPersonalAccessTokenInBrowser: true,
        });

        // 3. 配置事件监听
        client.on(EventNames.ALL, (eventName, data) =&gt; {
            console.log(eventName, data);
        });

        // 4. 建立与服务端的连接
        await client.connect();
        
        // 返回初始化完成的客户端实例
        return client;
    } catch (error) {
        console.error('初始化失败:', error);
        throw error;
    }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h2 id="26809d57" tabindex="-1">进阶功能</h2>
<h3 id="624f6e9c" tabindex="-1">客户端初始配置</h3>
<p>Realtime SDK 支持丰富的初始配置选项，初始化时除了必选的 accessToken、botId 及 connectorId 之外，还支持设置音色、开启调试模式、配置噪声抑制等功能。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>各个配置项的详细说明，可参考<a href="https://github.com/coze-dev/coze-js/blob/6abc5230c7db11a479d4731b405b335e17409af2/packages/realtime-api/src/index.ts#L12" target="_blank">示例项目源码</a>中的构造函数注释。</p>
</div>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">interface</span> <span class="hljs-title class_">RealtimeClientConfig</span> {
  <span class="hljs-comment">// 必填项</span>
  <span class="hljs-attr">accessToken</span>: <span class="hljs-built_in">string</span>;    <span class="hljs-comment">// 访问令牌</span>
  <span class="hljs-attr">botId</span>: <span class="hljs-built_in">string</span>;         <span class="hljs-comment">// Bot ID</span>
  <span class="hljs-attr">connectorId</span>: <span class="hljs-built_in">string</span>;   <span class="hljs-comment">// 渠道 ID</span>
  
  <span class="hljs-comment">// 可选项</span>
  <span class="hljs-attr">voiceId</span>?: <span class="hljs-built_in">string</span>;      <span class="hljs-comment">// 音色 ID</span>
  <span class="hljs-attr">conversationId</span>?: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 会话 ID</span>
  <span class="hljs-attr">baseURL</span>?: <span class="hljs-built_in">string</span>;      <span class="hljs-comment">// Base URL, 默认为 https://api.coze.cn</span>
  <span class="hljs-attr">userId</span>?: <span class="hljs-built_in">string</span>;        <span class="hljs-comment">// 自定义用户Id</span>
  <span class="hljs-attr">workflowId</span>?: <span class="hljs-built_in">string</span>;    <span class="hljs-comment">// 工作流Id</span>
  <span class="hljs-attr">debug</span>?: <span class="hljs-built_in">boolean</span>;       <span class="hljs-comment">// 调试模式，建议开发模式下启用</span>
  <span class="hljs-attr">allowPersonalAccessTokenInBrowser</span>?: <span class="hljs-built_in">boolean</span>; <span class="hljs-comment">// 允许在浏览器中使用个人访问令牌，不建议在生成环境下使用</span>
  <span class="hljs-attr">audioMutedDefault</span>?: <span class="hljs-built_in">boolean</span>; <span class="hljs-comment">// 是否默认开启音频，默认 true</span>
  <span class="hljs-attr">suppressStationaryNoise</span>?: <span class="hljs-built_in">boolean</span>;    <span class="hljs-comment">// 静态噪声抑制，默认 false</span>
  <span class="hljs-attr">suppressNonStationaryNoise</span>?: <span class="hljs-built_in">boolean</span>; <span class="hljs-comment">// 非静态噪声抑制，默认 false</span>
  <span class="hljs-attr">videoConfig</span>?: <span class="hljs-title class_">VideoConfig</span>;    <span class="hljs-comment">// 视频配置</span>
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="interface RealtimeClientConfig {
  // 必填项
  accessToken: string;    // 访问令牌
  botId: string;         // Bot ID
  connectorId: string;   // 渠道 ID
  
  // 可选项
  voiceId?: string;      // 音色 ID
  conversationId?: string; // 会话 ID
  baseURL?: string;      // Base URL, 默认为 https://api.coze.cn
  userId?: string;        // 自定义用户Id
  workflowId?: string;    // 工作流Id
  debug?: boolean;       // 调试模式，建议开发模式下启用
  allowPersonalAccessTokenInBrowser?: boolean; // 允许在浏览器中使用个人访问令牌，不建议在生成环境下使用
  audioMutedDefault?: boolean; // 是否默认开启音频，默认 true
  suppressStationaryNoise?: boolean;    // 静态噪声抑制，默认 false
  suppressNonStationaryNoise?: boolean; // 非静态噪声抑制，默认 false
  videoConfig?: VideoConfig;    // 视频配置
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="4364f856" tabindex="-1">音视频控制</h3>
<p>Realtime SDK 提供了完整的音频控制功能，可控制音频状态、视频状态，设置输入设备和输出设备。</p>
<ul data-style="0">
<li>控制音频状态：<br/>
你可以通过如下代码控制音频状态，例如开启或关闭麦克风。
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-comment">// 开启/关闭麦克风 </span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">setAudioEnable</span>(<span class="hljs-literal">true</span>);  <span class="hljs-comment">// 开启麦克风</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">setAudioEnable</span>(<span class="hljs-literal">false</span>); <span class="hljs-comment">// 关闭麦克风 </span>
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 开启/关闭麦克风 
await client.setAudioEnable(true);  // 开启麦克风
await client.setAudioEnable(false); // 关闭麦克风 " style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>控制视频状态：<br/>
你可以通过如下代码实现视频功能，但需要在初始化时配置视频相关的设置。
<div style="position: relative">
<pre><code class="hljs language-TypeScript">  
<span class="hljs-keyword">import</span> { <span class="hljs-title class_">RealtimeClient</span>, <span class="hljs-title class_">RealtimeUtils</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">"@coze/realtime-api"</span>;

<span class="hljs-comment">// 需要检查视频设备权限</span>
<span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> <span class="hljs-title class_">RealtimeUtils</span>.<span class="hljs-title function_">checkDevicePermission</span>(<span class="hljs-literal">true</span>);
<span class="hljs-keyword">if</span> (!result.<span class="hljs-property">video</span>) {
   <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Error</span>(<span class="hljs-string">"需要视频访问权限"</span>);
}
 
<span class="hljs-comment">// 首先，初始化时需要增加视频配置</span>
<span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> <span class="hljs-title class_">RealtimeClient</span>({
    <span class="hljs-attr">accessToken</span>: <span class="hljs-string">'your access token'</span>,
    <span class="hljs-attr">botId</span>: <span class="hljs-string">'your bot id'</span>,
    <span class="hljs-attr">connectorId</span>: <span class="hljs-string">'1024'</span>,
    <span class="hljs-comment">// ... 其它配置</span>
    <span class="hljs-attr">videoConfig</span>: { <span class="hljs-comment">// 视频配置</span>
        <span class="hljs-attr">renderDom</span>: <span class="hljs-string">'local-player'</span>, <span class="hljs-comment">// 视频渲染dom</span>
        <span class="hljs-attr">videoOnDefault</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 默认开启视频</span>
    }
});

<span class="hljs-comment">// 其次，需要将视频渲染到指定的dom</span>
<span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">div</span>
<span class="hljs-attr">style</span>=<span class="hljs-string">{{</span>
  <span class="hljs-attr">width:</span> '<span class="hljs-attr">300px</span>',
  <span class="hljs-attr">height:</span> '<span class="hljs-attr">300px</span>',
  <span class="hljs-attr">position:</span> '<span class="hljs-attr">relative</span>',
  <span class="hljs-attr">background:</span> '#<span class="hljs-attr">000</span>',
}}
<span class="hljs-attr">id</span>=<span class="hljs-string">{</span>'<span class="hljs-attr">local-player</span>'}
&gt;</span><span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span></span>


<span class="hljs-comment">// 最后，才可以使用启用/禁用视频功能</span>
client.<span class="hljs-title function_">setVideoEnable</span>(<span class="hljs-literal">true</span>); <span class="hljs-comment">// 启用视频</span>
client.<span class="hljs-title function_">setVideoEnable</span>(<span class="hljs-literal">false</span>); <span class="hljs-comment">// 禁用视频</span>
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="  
import { RealtimeClient, RealtimeUtils } from &quot;@coze/realtime-api&quot;;

// 需要检查视频设备权限
const result = await RealtimeUtils.checkDevicePermission(true);
if (!result.video) {
   throw new Error(&quot;需要视频访问权限&quot;);
}
 
// 首先，初始化时需要增加视频配置
const client = new RealtimeClient({
    accessToken: 'your access token',
    botId: 'your bot id',
    connectorId: '1024',
    // ... 其它配置
    videoConfig: { // 视频配置
        renderDom: 'local-player', // 视频渲染dom
        videoOnDefault: true, // 默认开启视频
    }
});

// 其次，需要将视频渲染到指定的dom
&lt;div
style={{
  width: '300px',
  height: '300px',
  position: 'relative',
  background: '#000',
}}
id={'local-player'}
&gt;&lt;/div&gt;


// 最后，才可以使用启用/禁用视频功能
client.setVideoEnable(true); // 启用视频
client.setVideoEnable(false); // 禁用视频" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>控制输入设备、输出设备：<br/>
你可以通过如下代码获取和设置音频输入设备和输出设备。
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">RealtimeUtils</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">"@coze/realtime-api"</span>;

<span class="hljs-keyword">const</span> devices = <span class="hljs-keyword">await</span> <span class="hljs-title class_">RealtimeUtils</span>.<span class="hljs-title function_">getAudioDevices</span>();  <span class="hljs-comment">// 获取输入、输出设备</span>
client.<span class="hljs-title function_">setAudioInputDevice</span>(devices.<span class="hljs-property">audioInputs</span>[<span class="hljs-number">0</span>].<span class="hljs-property">deviceId</span>); <span class="hljs-comment">// 设置音频输入设备</span>
client.<span class="hljs-title function_">setAudioOutputDevice</span>(devices.<span class="hljs-property">audioOutputs</span>[<span class="hljs-number">0</span>].<span class="hljs-property">deviceId</span>); <span class="hljs-comment">// 设置音频输出设备</span>
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text='import { RealtimeUtils } from "@coze/realtime-api";

const devices = await RealtimeUtils.getAudioDevices();  // 获取输入、输出设备
client.setAudioInputDevice(devices.audioInputs[0].deviceId); // 设置音频输入设备
client.setAudioOutputDevice(devices.audioOutputs[0].deviceId); // 设置音频输出设备' style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ul>
<h3 id="7794046b" tabindex="-1">调试功能</h3>
<p>在调试模式（debug: true）下，可以使用以下功能来帮助开发和问题排查。</p>
<ul data-style="0">
<li>开启音频属性报告：<br/>
定期输出音频相关的调试信息，帮助开发者了解音频状态。
<div style="position: relative">
<pre><code class="hljs language-TypeScript">client.<span class="hljs-title function_">enableAudioPropertiesReport</span>({
    <span class="hljs-attr">interval</span>: <span class="hljs-number">100</span>  <span class="hljs-comment">// 报告间隔(毫秒)</span>
}); 
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="client.enableAudioPropertiesReport({
    interval: 100  // 报告间隔(毫秒)
}); " style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>设备测试：<br/>
播放测试音频，帮助用户确认音频输出设备是否正常工作。
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-comment">// 开始音频播放设备测试</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">startAudioPlaybackDeviceTest</span>();
 
<span class="hljs-comment">// 停止音频播放设备测试</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">stopAudioPlaybackDeviceTest</span>();
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 开始音频播放设备测试
await client.startAudioPlaybackDeviceTest();
 
// 停止音频播放设备测试
await client.stopAudioPlaybackDeviceTest();" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>打印控制台日志：<br/>
在调试模式下，<code>RealtimeClient</code> 会输出详细的日志信息，日志以 <code>[RealtimeClient]</code>开头，后面跟着事件名称和相关数据，帮助开发者了解客户端和服务端的交互情况。
<div style="position: relative">
<pre><code class="hljs language-TypeScript">[<span class="hljs-title class_">RealtimeClient</span>] on realtime.<span class="hljs-property">event</span> event 
[<span class="hljs-title class_">RealtimeClient</span>] on realtime.<span class="hljs-property">event</span> event
[<span class="hljs-title class_">RealtimeClient</span>] dispatch server.<span class="hljs-property">bot</span>.<span class="hljs-property">join</span> event
[<span class="hljs-title class_">RealtimeClient</span>] dispatch server.<span class="hljs-property">session</span>.<span class="hljs-property">created</span> event
[<span class="hljs-title class_">RealtimeClient</span>] dispatch server.<span class="hljs-property">conversation</span>.<span class="hljs-property">created</span> event
[<span class="hljs-title class_">RealtimeClient</span>] dispatch client.<span class="hljs-property">connected</span> event
[<span class="hljs-title class_">RealtimeClient</span>] dispatch server.<span class="hljs-property">audio</span>.<span class="hljs-property">user</span>.<span class="hljs-property">speech_started</span> event
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="[RealtimeClient] on realtime.event event 
[RealtimeClient] on realtime.event event
[RealtimeClient] dispatch server.bot.join event
[RealtimeClient] dispatch server.session.created event
[RealtimeClient] dispatch server.conversation.created event
[RealtimeClient] dispatch client.connected event
[RealtimeClient] dispatch server.audio.user.speech_started event" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ul>
<h3 id="5336fba1" tabindex="-1">噪声抑制</h3>
<p>扣子 Realtime API 提供了两种噪声抑制模式，即静态噪声抑制和非静态噪声抑制。这两种模式可以同时启用，系统会根据具体场景自动选择最佳的抑制策略。</p>
<p>静态噪声抑制技术旨在通过多种技术手段降低或消除那些在一定时间段内保持恒定水平的噪声，这类噪声通常被称作静态噪声，例如持续的机器运转声或稳定的道路交通背景声。该技术的主要目标是增强信号的清晰度，特别是在语音通信、音频编辑和语音识别等场景中，通过减少背景噪声来提高语音信号与噪声的比例（信噪比），从而提升语音的清晰度和可理解性。</p>
<ul data-style="0">
<li>开启静态噪声抑制
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> <span class="hljs-title class_">RealtimeClient</span>({
  <span class="hljs-comment">// ... 其他配置 </span>
  <span class="hljs-attr">suppressStationaryNoise</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">// 启用静态噪声抑制</span>
});
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="const client = new RealtimeClient({
  // ... 其他配置 
  suppressStationaryNoise: true,  // 启用静态噪声抑制
});" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>开启非静态噪声抑制
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> <span class="hljs-title class_">RealtimeClient</span>({
  <span class="hljs-comment">// ... 其他配置</span>
  <span class="hljs-attr">suppressNonStationaryNoise</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">// 启用非静态噪声抑制</span>
}); 
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="const client = new RealtimeClient({
  // ... 其他配置
  suppressNonStationaryNoise: true,  // 启用非静态噪声抑制
}); " style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ul>
<h3 id="6959395e" tabindex="-1">音色配置</h3>
<p>系统默认采用<code>柔美女友</code>音色，音色 ID 为 7426720361733046281。在初始化 Realtime SDK 时，你可以通过指定 <code>voiceId</code> 来自定义智能体的音色。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<ul data-style="0">
<li>每个音色都有不同的特征，例如性别、语言、风格等特征。</li>
<li>如果不指定 <code>voiceId</code> 或值为空，智能体将使用系统默认音色。</li>
</ul>
</div>
<p>配置方式如下：</p>
<ol data-style="0">
<li>获取可用的音色 ID。<br/>
你可以通过<a href="/developer_guides/list_voices" target="_blank">查看音色列表</a>获取可用的音色列表。
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">CozeAPI</span>, <span class="hljs-variable constant_">COZE_CN_BASE_URL</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/api'</span>;
<span class="hljs-keyword">const</span> api = <span class="hljs-keyword">new</span> <span class="hljs-title class_">CozeAPI</span>({
    <span class="hljs-attr">token</span>: <span class="hljs-string">'your-access-token'</span>,
    <span class="hljs-attr">baseURL</span>: <span class="hljs-variable constant_">COZE_CN_BASE_URL</span>,
}); 
<span class="hljs-comment">// 获取可用的音色列表</span>
<span class="hljs-keyword">const</span> voices = <span class="hljs-keyword">await</span> api.<span class="hljs-property">audio</span>.<span class="hljs-property">voices</span>.<span class="hljs-title function_">list</span>();
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { CozeAPI, COZE_CN_BASE_URL } from '@coze/api';
const api = new CozeAPI({
    token: 'your-access-token',
    baseURL: COZE_CN_BASE_URL,
}); 
// 获取可用的音色列表
const voices = await api.audio.voices.list();" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>在 Realtime SDK 中使用音色 ID。<br/>
获取到想要使用的音色 ID 后，你可以在初始化 Realtime 客户端时指定 <code>voiceId</code>，以使用这个音色。
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">RealtimeClient</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">"@coze/realtime-api"</span>;
 
<span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> <span class="hljs-title class_">RealtimeClient</span>({
    <span class="hljs-attr">accessToken</span>: <span class="hljs-string">'your-access-token'</span>,
    <span class="hljs-attr">botId</span>: <span class="hljs-string">'your-bot-id'</span>,
    <span class="hljs-attr">connectorId</span>: <span class="hljs-string">'1024'</span>,
    <span class="hljs-attr">voiceId</span>: <span class="hljs-string">'7426725529589661723'</span>, <span class="hljs-comment">// 你想使用的音色 ID</span>
    <span class="hljs-comment">// ... 其他配置项</span>
});
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { RealtimeClient } from &quot;@coze/realtime-api&quot;;
 
const client = new RealtimeClient({
    accessToken: 'your-access-token',
    botId: 'your-bot-id',
    connectorId: '1024',
    voiceId: '7426725529589661723', // 你想使用的音色 ID
    // ... 其他配置项
});" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ol>
<h3 id="045a541a" tabindex="-1">信令事件</h3>
<p>信令事件指的是在通话过程中，硬件端和服务端通过信令通道交互的事件，例如硬件端可以通过事件去设置自己的降噪模型，服务端会通过信令事件发送对话文字内容等。通过信令事件可在硬件设备上实现丰富的交互效果，例如获取设备端的数据、解析超链接或图片内容、控制设备去播放音乐、动态调整音色、设置智能体说话速度等。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<ul data-style="0">
<li>事件 ID：每个上行事件 ID 建议不要重复，故障排查场景下便于定位问题。</li>
<li>事件顺序：确保在监听到 Realtime SDK 的 onUserJoined 回调智能体进房后再发送上行事件。</li>
<li>插件模式：根据需求选择 <code>blocking</code> 或 <code>nonblocking</code> 模式，控制插件执行是否阻塞对话。</li>
<li>信令事件需要发送给房间内的智能体，传入的 UID 就是建房的 BotID，广播是不生效的。</li>
<li>每个事件有 ID 和 EventType， 通过 EventType 可以区分具体的事件类型，每个事件类型对应的 Payload 在 Data 中，开发者可以按需去提取需要的内容。</li>
</ul>
</div>
<h4 id="bf2d55ff" tabindex="-1"><strong>事件类型</strong></h4>
<p>智能语音信令事件包括上行事件和下行事件。每个事件有 ID 和 EventType， 通过 EventType 可以区分具体的事件类型，每个事件类型对应的 Payload 在 Data 中，开发者可以按需去提取需要的内容。</p>
<ul data-style="0">
<li><strong>上行事件</strong>：设备端上报给服务端的事件。应用程序需要根据扣子编程提供的事件结构，在触发事件时填充字段内容并上报事件。设备端需要在监听到 Realtime SDK 的 onUserJoined 回调智能体进房后才能发送上行事件，可通过 Realtime SDK 的 <code>sendUserMessage</code> 发送，如果是嵌入式设备集成音视频，可通过 Realtime SDK 的 <code>byte_rtc_rts_send_message</code> 发送。详细信息可参考<a href="/developer_guides/signaling_uplink_event" target="_blank">Realtime 上行事件</a>。</li>
<li><strong>下行事件</strong>：服务端下发给设备端的事件，可订阅 Realtime SDK的 <code>onUserMessageReceived</code>回调，如果是嵌入式设备集成音视频，可订阅 Realtime SDK 的 <code> on_message_received</code>回调，接收下行事件。应用程序需要解析下行事件，并根据业务需求进行下一步操作。详细信息可参考<a href="/developer_guides/signaling_downlink_event" target="_blank">Realtime 下行事件</a>。</li>
</ul>
<h4 id="9a5a84e9" tabindex="-1"><strong>公共参数</strong></h4>
<p>智能语音信令事件的公共参数如下：</p>
<!-- @cols-width: 100,162,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;"/><col style="width: 162px;"/><col style="width: 500px;"/></colgroup><thead>
<tr>
<th><strong>参数名称</strong></th>
<th><strong>类型</strong></th>
<th><strong>描述</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>id</td>
<td>String</td>
<td>事件 ID，也就是事件的唯一标识。由客户端或服务端生成，在故障排查场景下用于定位具体的事件，便于排查问题。</td>
</tr>
<tr>
<td>event_type</td>
<td>String</td>
<td>事件的类型。</td>
</tr>
<tr>
<td>data</td>
<td>JSON</td>
<td>事件的详细信息，其中包含具体事件的业务字段。</td>
</tr>
</tbody>
</table>
</div><h4 id="7d36f407" tabindex="-1">信令事件的使用流程</h4>
<p>信令事件的使用流程如下：</p>
<ol data-style="0">
<li>初始化。通过监听 <code>bot.join</code> 事件，确认房间初始化完成。</li>
<li>发送请求。使用上行事件（如 <code>conversation.message.create</code>）向智能体发送消息。</li>
<li>处理响应。监听下行事件（如 <code>conversation.message.delta</code>）获取智能体的增量回复。</li>
<li>插件交互。在收到事件 <code>conversation.chat.requires_action</code> 后，执行插件操作并通过事件 <code>conversation.chat.submit_tool_outputs</code> 提交结果。</li>
<li>错误处理。通过监听 <code>error</code> 事件捕获和处理异常情况。</li>
</ol>
<p>使用示例如下：</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-comment">// 使用示例</span>
client.<span class="hljs-title function_">on</span>(<span class="hljs-title class_">EventNames</span>.<span class="hljs-property">ALL_SERVER</span>, <span class="hljs-function">(<span class="hljs-params">eventName, <span class="hljs-attr">event</span>: <span class="hljs-built_in">any</span></span>) =&gt;</span> {
  <span class="hljs-keyword">if</span> (eventName === <span class="hljs-string">'server.bot.join'</span>) { <span class="hljs-comment">// 这里需要加个 server. 前缀</span>
    client.<span class="hljs-title function_">sendMessage</span>({
      <span class="hljs-string">"id"</span>: <span class="hljs-string">""</span>,
      <span class="hljs-string">"event_type"</span>: <span class="hljs-string">"conversation.message.create"</span>,
      <span class="hljs-string">"data"</span>: {
        <span class="hljs-string">"role"</span>: <span class="hljs-string">"user"</span>,
        <span class="hljs-string">"content_type"</span>: <span class="hljs-string">"text"</span>,
        <span class="hljs-string">"content"</span>: <span class="hljs-string">"你好"</span>
      }
    });
  } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (eventName === <span class="hljs-string">'server.conversation.message.delta'</span>) {
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'delta'</span>, event);
  }
});
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 使用示例
client.on(EventNames.ALL_SERVER, (eventName, event: any) =&gt; {
  if (eventName === 'server.bot.join') { // 这里需要加个 server. 前缀
    client.sendMessage({
      &quot;id&quot;: &quot;&quot;,
      &quot;event_type&quot;: &quot;conversation.message.create&quot;,
      &quot;data&quot;: {
        &quot;role&quot;: &quot;user&quot;,
        &quot;content_type&quot;: &quot;text&quot;,
        &quot;content&quot;: &quot;你好&quot;
      }
    });
  } else if (eventName === 'server.conversation.message.delta') {
    console.log('delta', event);
  }
});" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h4 id="0aebcc94" tabindex="-1">信令事件的处理思路</h4>
<p>在处理信令事件时，建议采用以下思路：</p>
<ul data-style="0">
<li><strong>监听所有事件</strong>：捕获客户端和服务端的所有交互，便于调试和监控。扣子编程推荐你监听所有的事件，你也可以根据实际的业务需求，监听不同类型的事件，例如客户端事件、服务端事件等。</li>
<li><strong>处理特定事件</strong>：根据业务需求，监听和处理特定的事件，例如连接成功、中断、断开、音频状态变化等。</li>
<li><strong>错误处理</strong>：捕获和处理错误事件，确保应用的稳定性和用户体验。</li>
</ul>
<p>以下是支持的事件类型及其说明：</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>事件的详细说明，可参考<a href="https://github.com/coze-dev/coze-js/blob/6abc5230c7db11a479d4731b405b335e17409af2/packages/realtime-api/src/event-handler.ts#L3" target="_blank">示例项目源码</a>。</p>
</div>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-comment">// 事件监听示例 </span>
client.<span class="hljs-title function_">on</span>(<span class="hljs-title class_">EventNames</span>.<span class="hljs-property">ALL</span>, <span class="hljs-function">(<span class="hljs-params">eventName, data</span>) =&gt;</span> {
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`收到事件: <span class="hljs-subst">${eventName}</span>`</span>, data);
});

<span class="hljs-comment">// 支持的事件类型</span>
<span class="hljs-keyword">enum</span> <span class="hljs-title class_">EventNames</span> {
  <span class="hljs-variable constant_">ALL</span> = <span class="hljs-string">'realtime.event'</span>,           <span class="hljs-comment">// 所有事件</span>
  <span class="hljs-variable constant_">ALL_CLIENT</span> = <span class="hljs-string">'client.*'</span>,          <span class="hljs-comment">// 所有客户端事件</span>
  <span class="hljs-variable constant_">ALL_SERVER</span> = <span class="hljs-string">'server.*'</span>,          <span class="hljs-comment">// 所有服务端事件</span>
  <span class="hljs-variable constant_">CONNECTED</span> = <span class="hljs-string">'client.connected'</span>,    <span class="hljs-comment">// 客户端已连接</span>
  <span class="hljs-variable constant_">INTERRUPTED</span> = <span class="hljs-string">'client.interrupted'</span>, <span class="hljs-comment">// 客户端已中断</span>
  <span class="hljs-variable constant_">DISCONNECTED</span> = <span class="hljs-string">'client.disconnected'</span>, <span class="hljs-comment">// 客户端已断开</span>
  <span class="hljs-variable constant_">AUDIO_UNMUTED</span> = <span class="hljs-string">'client.audio.unmuted'</span>, <span class="hljs-comment">// 音频已取消静音</span>
  <span class="hljs-variable constant_">AUDIO_MUTED</span> = <span class="hljs-string">'client.audio.muted'</span>,     <span class="hljs-comment">// 音频已静音</span>
  <span class="hljs-variable constant_">ERROR</span> = <span class="hljs-string">'client.error'</span>            <span class="hljs-comment">// 客户端发生错误</span>
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 事件监听示例 
client.on(EventNames.ALL, (eventName, data) =&gt; {
  console.log(`收到事件: ${eventName}`, data);
});

// 支持的事件类型
enum EventNames {
  ALL = 'realtime.event',           // 所有事件
  ALL_CLIENT = 'client.*',          // 所有客户端事件
  ALL_SERVER = 'server.*',          // 所有服务端事件
  CONNECTED = 'client.connected',    // 客户端已连接
  INTERRUPTED = 'client.interrupted', // 客户端已中断
  DISCONNECTED = 'client.disconnected', // 客户端已断开
  AUDIO_UNMUTED = 'client.audio.unmuted', // 音频已取消静音
  AUDIO_MUTED = 'client.audio.muted',     // 音频已静音
  ERROR = 'client.error'            // 客户端发生错误
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="e0e55ad4" tabindex="-1">错误处理</h3>
<p>系统定义了一个错误处理机制，用于处理 <code>RealtimeClient</code> 在运行过程中可能遇到的各种错误。通过定义一个枚举 <code>RealtimeError</code>，系统将不同的错误类型进行了分类，便于开发者根据具体的错误类型进行针对性的处理。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">enum</span> <span class="hljs-title class_">RealtimeError</span> { 
  <span class="hljs-variable constant_">DEVICE_ACCESS_ERROR</span> = <span class="hljs-string">'DEVICE_ACCESS_ERROR'</span>,         <span class="hljs-comment">// 设备访问错误</span>
  <span class="hljs-variable constant_">CONNECTION_ERROR</span> = <span class="hljs-string">'CONNECTION_ERROR'</span>,               <span class="hljs-comment">// 连接错误</span>
  <span class="hljs-variable constant_">DISCONNECTION_ERROR</span> = <span class="hljs-string">'DISCONNECTION_ERROR'</span>,         <span class="hljs-comment">// 断开连接错误</span>
  <span class="hljs-variable constant_">INTERRUPT_ERROR</span> = <span class="hljs-string">'INTERRUPT_ERROR'</span>,                 <span class="hljs-comment">// 中断错误</span>
  <span class="hljs-variable constant_">EVENT_HANDLER_ERROR</span> = <span class="hljs-string">'EVENT_HANDLER_ERROR'</span>,         <span class="hljs-comment">// 事件处理错误</span>
  <span class="hljs-variable constant_">NETWORK_ERROR</span> = <span class="hljs-string">'NETWORK_ERROR'</span>,                     <span class="hljs-comment">// 网络错误</span>
  <span class="hljs-variable constant_">CREATE_ROOM_ERROR</span> = <span class="hljs-string">'CREATE_ROOM_ERROR'</span>             <span class="hljs-comment">// 创建房间错误</span>
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="enum RealtimeError { 
  DEVICE_ACCESS_ERROR = 'DEVICE_ACCESS_ERROR',         // 设备访问错误
  CONNECTION_ERROR = 'CONNECTION_ERROR',               // 连接错误
  DISCONNECTION_ERROR = 'DISCONNECTION_ERROR',         // 断开连接错误
  INTERRUPT_ERROR = 'INTERRUPT_ERROR',                 // 中断错误
  EVENT_HANDLER_ERROR = 'EVENT_HANDLER_ERROR',         // 事件处理错误
  NETWORK_ERROR = 'NETWORK_ERROR',                     // 网络错误
  CREATE_ROOM_ERROR = 'CREATE_ROOM_ERROR'             // 创建房间错误
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<p>以下是一个完整的示例，展示如何在实际应用中使用错误处理机制：</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">AuthenticationError</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/api'</span>;
 
<span class="hljs-keyword">try</span> {
  <span class="hljs-keyword">await</span> client.<span class="hljs-title function_">connect</span>();
} <span class="hljs-keyword">catch</span> (error) {
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">error</span>(error);
      <span class="hljs-keyword">if</span> (error <span class="hljs-keyword">instanceof</span> <span class="hljs-title class_">RealtimeAPIError</span>) {
        <span class="hljs-keyword">switch</span> (error.<span class="hljs-property">code</span>) {
          <span class="hljs-keyword">case</span> <span class="hljs-title class_">RealtimeError</span>.<span class="hljs-property">CREATE_ROOM_ERROR</span>:
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`创建房间失败: <span class="hljs-subst">${error.message}</span>`</span>);
            <span class="hljs-keyword">break</span>;
          <span class="hljs-keyword">case</span> <span class="hljs-title class_">RealtimeError</span>.<span class="hljs-property">CONNECTION_ERROR</span>:
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`加入房间失败: <span class="hljs-subst">${error.message}</span>`</span>);
            <span class="hljs-keyword">break</span>;
          <span class="hljs-keyword">case</span> <span class="hljs-title class_">RealtimeError</span>.<span class="hljs-property">DEVICE_ACCESS_ERROR</span>:
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`获取设备失败: <span class="hljs-subst">${error.message}</span>`</span>);
            <span class="hljs-keyword">break</span>;
          <span class="hljs-attr">default</span>:
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`发生错误: <span class="hljs-subst">${error.message}</span>`</span>);
        }
      } <span class="hljs-keyword">else</span> {
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">error</span>(<span class="hljs-string">'未知错误：'</span>, error);
      }
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { AuthenticationError } from '@coze/api';
 
try {
  await client.connect();
} catch (error) {
      console.error(error);
      if (error instanceof RealtimeAPIError) {
        switch (error.code) {
          case RealtimeError.CREATE_ROOM_ERROR:
            console.log(`创建房间失败: ${error.message}`);
            break;
          case RealtimeError.CONNECTION_ERROR:
            console.log(`加入房间失败: ${error.message}`);
            break;
          case RealtimeError.DEVICE_ACCESS_ERROR:
            console.log(`获取设备失败: ${error.message}`);
            break;
          default:
            console.log(`发生错误: ${error.message}`);
        }
      } else {
        console.error('未知错误：', error);
      }
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="b6698241" tabindex="-1"></h3>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button class="feedbackButton-GuivRC" type="button"><span class="feedbackButtonIcon-PqHraK"></span><span>有帮助</span></button><button class="feedbackButton-GuivRC" type="button"><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm" data-discover="true" href="/dev_how_to_guides_access_process"><div class="cardLabel-sDu1uC"><svg aria-hidden="true" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12">接入流程</div></a><a class="card-T4zaCm nextCard-lFoioT" data-discover="true" href="/dev_how_to_guides_realtime_iOS"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg aria-hidden="true" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">集成音视频 Realtime iOS SDK</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#b5aea001" href="#b5aea001" title="准备工作">准备工作</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#eb0752df" href="#eb0752df" title="跑通示例项目">跑通示例项目</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#11a294fc" href="#11a294fc" title="项目源码">项目源码</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#baeda4e1" href="#baeda4e1" title="创建并运行示例项目">创建并运行示例项目</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#9f8e12cc" href="#9f8e12cc" title="源码解析">源码解析</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#21fab927" href="#21fab927" title="基础设置和依赖">基础设置和依赖</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#ebb85879" href="#ebb85879" title="状态管理设置">状态管理设置</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#5db247bc" href="#5db247bc" title="鉴权配置">鉴权配置</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#b2918b9a" href="#b2918b9a" title="语音配置">语音配置</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#8263c110" href="#8263c110" title="客户端初始化">客户端初始化</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#d9819ed7" href="#d9819ed7" title="消息处理">消息处理</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#cc20150a" href="#cc20150a" title="核心功能实现">核心功能实现</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#97ee360b" href="#97ee360b" title="UI 实现">UI 实现</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#8540cce2" href="#8540cce2" title="集成 SDK">集成 SDK</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#9ffe794e" href="#9ffe794e" title="步骤一：安装依赖">步骤一：安装依赖</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#fc37c5e0" href="#fc37c5e0" title="步骤二：检查设备权限">步骤二：检查设备权限</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#7c097d74" href="#7c097d74" title="步骤三：初始化 SDK">步骤三：初始化 SDK</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#72b4e187" href="#72b4e187" title="步骤四：监听事件">步骤四：监听事件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#5a920583" href="#5a920583" title="步骤五：建立连接">步骤五：建立连接</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#cc16fcee" href="#cc16fcee" title="步骤六：断开连接">步骤六：断开连接</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#cbaacab0" href="#cbaacab0" title="示例代码">示例代码</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#26809d57" href="#26809d57" title="进阶功能">进阶功能</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#624f6e9c" href="#624f6e9c" title="客户端初始配置">客户端初始配置</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#4364f856" href="#4364f856" title="音视频控制">音视频控制</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#7794046b" href="#7794046b" title="调试功能">调试功能</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#5336fba1" href="#5336fba1" title="噪声抑制">噪声抑制</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#6959395e" href="#6959395e" title="音色配置">音色配置</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#045a541a" href="#045a541a" title="信令事件">信令事件</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#bf2d55ff" href="#bf2d55ff" title="事件类型">事件类型</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#9a5a84e9" href="#9a5a84e9" title="公共参数">公共参数</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#7d36f407" href="#7d36f407" title="信令事件的使用流程">信令事件的使用流程</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#0aebcc94" href="#0aebcc94" title="信令事件的处理思路">信令事件的处理思路</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#e0e55ad4" href="#e0e55ad4" title="错误处理">错误处理</a></div></div></div></div></div></div></div></div>
</body></html>