<!DOCTYPE html>
<html><head><meta charset="utf-8"/><meta content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no" name="viewport"/><meta content="ie=edge" http-equiv="x-ua-compatible"/><meta content="webkit" name="renderer"/><meta content="standard" name="layoutmode"/><meta content="force" name="imagemode"/><meta content="no" name="wap-font-scale"/><meta content="telephone=no" name="format-detection"/><title data-react-helmet="true">Web SDK（AI 编程）</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/5956.1729cb00c0.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.ca52691239.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet"/> <link data-react-helmet="true" href="https://docs.coze.cn/developer_guides_vibe_coding_websdk" rel="canonical"/><link data-react-helmet="true" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" rel="icon"/><link data-react-helmet="true" href="/developer_guides_vibe_coding_websdk.md" rel="alternate" type="text/markdown"/><link data-react-helmet="true" href="/llms.txt" rel="alternate" type="text/plain"/>
<meta content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE" data-react-helmet="true" name="google-site-verification"/>

<meta content="codeva-mJmA0HNtAv" name="baidu-site-verification"/></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a class="brand-qR7tMP" href="https://www.coze.cn" rel="noreferrer" target="_blank"><img alt="扣子" class="siteIcon-qohRRP" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" data-discover="true" href="/what_is_coze">扣子</a><a class="tab-JssokC" data-discover="true" href="/guides_welcome">扣子编程</a><a class="tab-JssokC" data-discover="true" href="/ppt-plugin">教程</a><a class="tab-JssokC" data-discover="true" href="/coze_pro_billing_overview">定价</a><a class="tab-JssokC activeTab-g8RDKO" data-discover="true" href="/developer_guides_vibe_coding_websdk"><span>资源</span><span class="arrow-nKMrBv"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg fill="none" height="16" viewbox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)" fill-rule="evenodd"></path></g><defs><lineargradient gradientunits="userSpaceOnUse" id="paint0_linear_1944_44928" x1="1.3335" x2="15.0379" y1="15.0401" y2="15.0401"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></lineargradient><clippath id="clip0_1944_44928"><rect fill="white" height="16" width="16"></rect></clippath></defs></svg><input class="input-tjtw6Q" placeholder="搜索" readonly="" type="text"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" fill="currentColor" viewbox="5 5 22 22" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg fill="none" height="48" viewbox="0 0 48 48" width="48" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clippath id="clip0_2_6"><rect fill="white" height="48" width="48"></rect></clippath></defs></svg></span><span class="topic-rag-logo-dark"><svg fill="none" height="48" viewbox="0 0 48 48" width="48" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clippath id="clip0_2_6"><rect fill="#262E3B" height="48" width="48"></rect></clippath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg height="24" role="img" viewbox="0 0 40 40" width="24" xmlns="http://www.w3.org/2000/svg"><defs><lineargradient gradientunits="userSpaceOnUse" id="starGradient" x1="1.25" x2="29.602" y1="35.735" y2="29.277"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></lineargradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" fill="url(#starGradient)" fill-opacity="0.8" r="1.2"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg aria-hidden="true" class="arco-icon arco-icon-close" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg fill="none" height="14" viewbox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><lineargradient gradientunits="userSpaceOnUse" id="paint0_linear_7153_28960" x1="2.04126" x2="12.5415" y1="13.4163" y2="13.4163"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></lineargradient><clippath id="clip0_7153_28960"><rect fill="white" height="14" width="14"></rect></clippath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" disabled="" style="border-radius:4px;height:28px" type="button"><svg aria-hidden="true" class="arco-icon arco-icon-plus" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" disabled="" style="color:#c7ccd6" type="button"><svg fill="none" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor" fill-rule="evenodd"></path></g><defs><clippath id="clip0_7153_32885"><rect fill="white" height="18" transform="translate(3 3)" width="18"></rect></clippath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true"><div class="content-KOLZ20"><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b97434bdbc784e3ce84ce"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a55df9a4bdbc784e3c9738f"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf30d"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf317"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf31d"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf325"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf334"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf32e"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf35a"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf362"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8e614bdbc784e3cce185"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8d4bdbc784e3cc3e2c"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8d4bdbc784e3cc3fa8"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc40e8"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Chat SDK">Chat SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc40ef"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Python SDK">Python SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc412c"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Node.js SDK">Node.js SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc4132"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Java SDK">Java SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc41c6"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Go SDK">Go SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc4245"><a class="nodeContent-GigwSX active-dE_WV_" data-discover="true" href="/developer_guides_vibe_coding_websdk" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Web SDK（AI 编程）">Web SDK（AI 编程）</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc424c"><a class="nodeContent-GigwSX" data-discover="true" href="/developer_guides_ui_builder_web_sdk" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="Web SDK（低代码）">Web SDK（低代码）</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8b8d4bdbc784e3cc4251"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="Card SDK">Card SDK</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8bc84bdbc784e3cc529d"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8e4bdbc784e3cc445f"><a class="nodeContent-GigwSX" data-discover="true" href="/developer_guides_coze_cli" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf33f"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf369"><a class="nodeContent-GigwSX" data-discover="true" href="/guides_FAQ" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div aria-label="拖拽调整目录宽度" aria-orientation="vertical" class="resizeHandle-lop5IL" role="separator"></div></div><div class="container-h8FsmA" data-topic-doc="true"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>SDK 参考</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">Web SDK（AI 编程）</span></div><div class="titleContainer-hr8uxx"><h1 class="title-C1b1pA" data-h0="true" id="doc_title">Web SDK（AI 编程）</h1><aside class="mdx-live-widget">
<p class="mdx-live-widget-label">Interactive explorer</p>
<p>This directory tree is interactive on the original page and cannot run inside an EPUB. Open it here: <a class="source-title" href="https://docs.coze.cn/developer_guides_vibe_coding_websdk#explore-the-directory" rel="external">https://docs.coze.cn/developer_guides_vibe_coding_websdk#explore-the-directory</a></p>
</aside><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg aria-hidden="true" class="copyIcon-iTB4A1 arco-icon arco-icon-copy" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg><span>复制页面</span></div><div class="moreButton-ZJ3qDg"><svg aria-hidden="true" class="arco-icon arco-icon-down" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>本文介绍如何安装并使用扣子编程 Web SDK，开发者可以参考本文档在自己开发的网站中快速添加一个 AI 智能体或工作流，为网站集成智能服务。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>扣子编程提供两种不同的 Web SDK，分别适用于 AI 编程项目和低代码应用。本文档适用于 AI 编程项目，如需在网站中嵌入低代码应用，请参见<a href="/developer_guides/ui_builder_web_sdk" target="_blank">Web SDK（低代码）</a>。</p>
</div>
<h2 id="708de81d" tabindex="-1">Web SDK 介绍</h2>
<p>扣子编程 Web SDK 是专为 AI 编程场景设计的 Web 开发工具包，可帮助你将 AI 编程搭建的智能体与工作流快速集成到网页应用中。它提供 JavaScript、React 组件和 Iframe 多种嵌入方式，实现对话交互与业务自动化。<br/>
扣子编程 Web SDK 适用于需要在各类网页应用中快速集成扣子 AI 编程智能体和工作流的场景。</p>
<ul data-style="0">
<li><strong>网页内嵌对话机器人</strong>：在你的网站任意位置嵌入一个对话窗口，提供 7x24 小时的智能客服、产品导览、信息查询等服务。</li>
<li><strong>触发式自动化工作流</strong>：在用户完成特定操作（如填写表单、点击按钮）后，自动触发一个预设的工作流，完成数据处理、信息同步、发送通知等一系列后台任务。</li>
</ul>
<p><strong>效果预览</strong><br/>
在网页应用中，开发者可以直接使用已部署的智能体与工作流。</p>
<ul data-style="0">
<li>智能体：可在网页内以对话界面形式呈现，用户能直接与智能体交互，获取智能问答、任务处理等 AI 能力。<br/>
<img alt="Image" height="321" loading="lazy" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/434a346c28d64b69879a96fe579158ec~tplv-goo7wpa0wc-topic.webp" width="601"/></li>
<li>工作流：可在网页中直接触发和运行预设的自动化工作流，实现复杂业务流程的线上执行。<br/>
<img alt="Image" height="321" loading="lazy" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0324ae55539a449aa03b66c8f81cfa00~tplv-goo7wpa0wc-topic.webp" width="602"/></li>
</ul>
<h2 id="01197823" tabindex="-1">准备工作</h2>
<p>接入 Web SDK 前，应完成以下准备工作：</p>
<!-- @cols-width: 194,713 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 194px;"/><col style="width: 713px;"/></colgroup><thead>
<tr>
<th>
<p><strong>项目</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>部署并开启 Web SDK 渠道</p>
</td>
<td>
<p>已成功部署智能体或工作流，并开启了 Web SDK 渠道。详情请参见<a href="/guides/deploy_agent_as_api_service" target="_blank">部署智能体</a>、<a href="/guides/deploy_vibe_workflow" target="_blank">部署工作流</a>。</p>
</td>
</tr>
<tr>
<td>
<p>检查浏览器版本</p>
</td>
<td>
<ul data-style="0">
<li>Chrome：87.0 及以上</li>
<li>Edge：88.0 及以上</li>
<li>Safari：14.0 及以上</li>
<li>Firefox：78.0 及以上</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>获取 ProjectId</p>
</td>
<td>
<ul data-style="0">
<li><strong>从 Web SDK 嵌入代码中获取</strong>：项目部署后，平台会提供 Web SDK 的嵌入代码。 <code>ProjectId</code> 已被自动填充在代码中，可直接复制使用。<br/>
<img alt="Image" height="202" loading="lazy" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a49215b49cbd469c845572c420427e6c~tplv-goo7wpa0wc-topic.webp" width="351"/></li>
<li><strong>从浏览器地址栏获取</strong>：进入项目详情页后，查看浏览器地址栏的 URL（格式示例：<code>https://code.coze.cn/p/:projectId/xxxx</code>），其中 <code>:projectId</code> 对应的字符串即为当前项目的 <code>ProjectId</code>。<br/>
<img alt="Image" height="163" loading="lazy" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/dfe3a8eb62b541eb80706fe4f96074ea~tplv-goo7wpa0wc-topic.webp" width="346"/></li>
</ul>
</td>
</tr>
<tr>
<td>
<p>获取访问令牌（Token）</p>
</td>
<td>
<ul data-style="0">
<li><strong>支持的 Token 类型</strong>：OAuth 访问令牌、个人访问令牌（PAT）和服务访问令牌（ SAT）。</li>
<li><strong>推荐的获取方式</strong>：
<ul data-style="1">
<li><strong>快速体验</strong>：可使用个人访问令牌，详细说明可参考<a href="/developer_guides/pat" target="_blank">添加个人访问令牌</a>。</li>
<li><strong>线上环境</strong>：推荐使用 <strong>OAuth JWT 授权（开发者）</strong> 模式获取 Token，详情请参见<a href="/developer_guides/oauth_jwt" target="_blank">OAuth JWT 授权（开发者）</a>。</li>
</ul>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>安全起见，建议使用 JWT 方式生成 Token 时，在 Payload 中添加<code>“session_context.connector_info.connector_id” : “2001”</code>。此参数控制 Token 的使用范围仅限于 Web SDK，以免 Token 泄露引发安全风险。</p>
</div>
</li>
<li><strong>权限要求</strong>
<ul data-style="1">
<li><code>convertFileType</code></li>
<li><code>uploadFileToStorage</code></li>
<li><code>getMetadata(VibeProject)</code></li>
<li><code>run(VibeProject)</code></li>
</ul>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div><h2 id="5c5ef996" tabindex="-1">快速体验</h2>
<p>以下是扣子编程 Web SDK 快速接入示例，采用 CDN 方式引入，帮助你在 Web 页面可视化体验智能体或工作流。</p>
<ol data-style="0">
<li>
<p>新建 HTML 文件。<br/>
在本地新建记事本，复制以下完整代码，粘贴后保存为 <code>coze-web-sdk-demo.html</code>，并保存至桌面。注意文件后缀必须为 <code>.html</code>，不可为 <code>.txt</code>。</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript">&lt;!doctype html&gt;
<span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-name">head</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">title</span>&gt;</span>Coze Web SDK<span class="hljs-tag">&lt;/<span class="hljs-name">title</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">style</span>&gt;</span><span class="language-css">
      * { <span class="hljs-attribute">box-sizing</span>: border-box;}
      <span class="hljs-selector-tag">html</span> { <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>; <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>; }
      <span class="hljs-selector-tag">body</span> { <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>; <span class="hljs-attribute">padding</span>: <span class="hljs-number">8px</span>; <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>; }
    </span><span class="hljs-tag">&lt;/<span class="hljs-name">style</span>&gt;</span>
  <span class="hljs-tag">&lt;/<span class="hljs-name">head</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-name">body</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://lf-cdn.coze.cn/obj/unpkg/latest/coze/web-sdk/dist/js-umd/index.min.js"</span>&gt;</span><span class="hljs-tag">&lt;/<span class="hljs-name">script</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-name">script</span>&gt;</span><span class="language-javascript">
      <span class="hljs-comment">// 初始化 Web SDK。</span>
      cozeWebSDK.<span class="hljs-title function_">init</span>({
        <span class="hljs-comment">// 替换为你的项目 ID，用于指定要加载的智能体或工作流。</span>
        <span class="hljs-attr">projectId</span>: <span class="hljs-string">'761559609158873****'</span>,
        <span class="hljs-comment">// 替换为 Token。作为初始化时的访问凭证，用于首次加载 Web SDK 时完成身份验证。</span>
        <span class="hljs-attr">refreshToken</span>: <span class="hljs-function">() =&gt;</span> <span class="hljs-title class_">Promise</span>.<span class="hljs-title function_">resolve</span>(<span class="hljs-string">"czs_qrDe********"</span>),
      });
    </span><span class="hljs-tag">&lt;/<span class="hljs-name">script</span>&gt;</span>
  <span class="hljs-tag">&lt;/<span class="hljs-name">body</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-name">html</span>&gt;</span></span>
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot; /&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot; /&gt;
    &lt;title&gt;Coze Web SDK&lt;/title&gt;
    &lt;style&gt;
      * { box-sizing: border-box;}
      html { margin: 0; height: 100%; }
      body { margin: 0; padding: 8px; height: 100%; }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;script src=&quot;https://lf-cdn.coze.cn/obj/unpkg/latest/coze/web-sdk/dist/js-umd/index.min.js&quot;&gt;&lt;/script&gt;
    &lt;script&gt;
      // 初始化 Web SDK。
      cozeWebSDK.init({
        // 替换为你的项目 ID，用于指定要加载的智能体或工作流。
        projectId: '761559609158873****',
        // 替换为 Token。作为初始化时的访问凭证，用于首次加载 Web SDK 时完成身份验证。
        refreshToken: () =&gt; Promise.resolve(&quot;czs_qrDe********&quot;),
      });
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>
<p>替换鉴权信息，并保存文件。<br/>
打开 <code>coze-web-sdk-demo.html</code> 文件，替换以下内容：</p>
<ul data-style="1">
<li><code>你的Project ID</code>：替换为<strong>准备工作</strong>中获取的 Project ID。</li>
<li><code>你的Token</code> ：替换为<strong>准备工作</strong>中获取的个人访问令牌。</li>
</ul>
</li>
<li>
<p>运行体验。<br/>
双击打开 <code>coze-web-sdk-demo.html</code> 文件，等待 1-2 秒，即可在浏览器中直观体验智能体或工作流能力在网页中的呈现效果。</p>
</li>
</ol>
<h2 id="4931f21c" tabindex="-1">接入方式</h2>
<p>扣子编程 Web SDK 支持以下三种接入方式。</p>
<!-- @cols-width: 100,316,500 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 100px;"/><col style="width: 316px;"/><col style="width: 500px;"/></colgroup><thead>
<tr>
<th>
<p><strong>接入方式</strong></p>
</th>
<th>
<p><strong>方案优势</strong></p>
</th>
<th>
<p><strong>适用场景</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>JavaScript</p>
</td>
<td>
<ul data-style="0">
<li>支持自定义触发方式、UI 样式与交互逻辑，可与产品深度融合。</li>
<li>适配各类前端项目与静态页面。</li>
</ul>
</td>
<td>
<p>适用于需要深度定制，且要求功能模块在视觉和交互上与产品无缝融合，以提供原生体验的场景。</p>
</td>
</tr>
<tr>
<td>
<p>React 组件</p>
</td>
<td>
<ul data-style="0">
<li>对 React 项目无缝集成，开发效率高。</li>
<li>支持通过 Props 配置、生命周期管理实例，代码结构清晰易维护。</li>
</ul>
</td>
<td>
<p>技术栈为 React 的项目首选。</p>
</td>
</tr>
<tr>
<td>
<p>Iframe</p>
</td>
<td>
<ul data-style="0">
<li>仅需粘贴 HTML 代码，开发成本极低。</li>
<li>沙箱安全隔离，无样式与脚本冲突风险。</li>
</ul>
</td>
<td>
<p>快速上线、无需深度定制、优先保证稳定性的场景。</p>
</td>
</tr>
</tbody>
</table>
</div><h2 id="6ca31889" tabindex="-1">接入流程</h2>
<p>你可以根据项目的定制需求和开发效率，选择合适的接入方式。</p>
<h3 id="cd64cb2b" tabindex="-1">JavaScript</h3>
<p>采用 JavaScript 接入方式时，可参照以下操作步骤，同时结合对应的配置参考调整相关参数，确保接入效果符合需求。</p>
<h4 id="b63cf96a" tabindex="-1">操作步骤</h4>
<ol data-style="0">
<li>
<p>安装或引入 Web SDK。<br/>
你可以选择通过 npm 安装或直接在 HTML 中引用 CDN。</p>
<ul data-style="1">
<li>
<p><strong>方式一：使用 npm</strong></p>
<div style="position: relative">
<pre><code class="hljs language-Bash">npm i @coze/web-sdk@latest
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="npm i @coze/web-sdk@latest" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>
<p><strong>方式二：引用 CDN</strong></p>
<div style="position: relative">
<pre><code class="hljs language-HTML"><span class="hljs-tag">&lt;<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://lf-cdn.coze.cn/obj/unpkg/latest/coze/web-sdk/dist/js-umd/index.min.js"</span>&gt;</span><span class="hljs-tag">&lt;/<span class="hljs-name">script</span>&gt;</span>
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text='&lt;script src="https://lf-cdn.coze.cn/obj/unpkg/latest/coze/web-sdk/dist/js-umd/index.min.js"&gt;&lt;/script&gt;' style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ul>
</li>
<li>
<p>初始化 Web SDK 实例。</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-comment">// 如果使用 npm 包，需要先引入。</span>
<span class="hljs-keyword">import</span> { cozeWebSDK } <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/web-sdk/js'</span>; 
 
<span class="hljs-comment">// 如果是引用 CDN，实例默认挂载在 window 对象上 (window.cozeWebSDK) </span>
 
<span class="hljs-comment">// 初始化 Web SDK。</span>
cozeWebSDK.<span class="hljs-title function_">init</span>({ 
  <span class="hljs-comment">// 替换为你的项目 ID，用于指定要加载的智能体或工作流。</span>
  <span class="hljs-attr">projectId</span>: <span class="hljs-string">'YOUR_PROJECT_ID'</span>, 
  <span class="hljs-comment">// 替换为 Token。作为初始化时的访问凭证，用于首次加载 SDK 时完成身份验证。</span>
  <span class="hljs-attr">refreshToken</span>: <span class="hljs-function">() =&gt;</span> <span class="hljs-string">'YOUR_TOKEN'</span>, 
  <span class="hljs-comment">// 可选：指定挂载容器。</span>
  <span class="hljs-comment">// container: document.getElementById('sdk-container'), </span>
});
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 如果使用 npm 包，需要先引入。
import { cozeWebSDK } from '@coze/web-sdk/js'; 
 
// 如果是引用 CDN，实例默认挂载在 window 对象上 (window.cozeWebSDK) 
 
// 初始化 Web SDK。
cozeWebSDK.init({ 
  // 替换为你的项目 ID，用于指定要加载的智能体或工作流。
  projectId: 'YOUR_PROJECT_ID', 
  // 替换为 Token。作为初始化时的访问凭证，用于首次加载 SDK 时完成身份验证。
  refreshToken: () =&gt; 'YOUR_TOKEN', 
  // 可选：指定挂载容器。
  // container: document.getElementById('sdk-container'), 
});" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ol>
<h4 id="dfc82e7b" tabindex="-1">配置参考</h4>
<ul data-style="0">
<li>
<p><strong>init(options: CozeWebSDKInitOptions): void（初始化 Web SDK 实例配置</strong>）</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript">type <span class="hljs-title class_">CozeWebSDKInitOptions</span> {
    <span class="hljs-attr">projectId</span>: string;
    ...
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="type CozeWebSDKInitOptions {
    projectId: string;
    ...
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<p>初始化 Web SDK 实例可配置参数如下：</p>
<!-- @cols-width: 152,144,100,125,491 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 152px;"/><col style="width: 144px;"/><col style="width: 100px;"/><col style="width: 125px;"/><col style="width: 491px;"/></colgroup><thead>
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
<p><strong>projectId</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>761559609158873****</p>
</td>
<td>
<p>项目 ID，用于指定要加载的智能体或工作流。</p>
</td>
</tr>
<tr>
<td>
<p><strong>container</strong></p>
</td>
<td>
<p>Element</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>js-cdn</p>
</td>
</tr>
<tr>
<td>
<p><strong>theme</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>light</p>
</td>
<td>
<p>界面主题模式。取值如下：</p>
<ul data-style="1">
<li>light（默认值）：明亮模式。</li>
<li>dark：暗黑模式。</li>
</ul>
</td>
</tr>
<tr>
<td>
<p><strong>className</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>coze-sdk-container</p>
</td>
<td>
<p>Web SDK 容器的 CSS 类名。</p>
</td>
</tr>
<tr>
<td>
<p><strong>style</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>width: 100%; height: 600px; border: 1px solid #e5e7eb; border-radius: 8px;</p>
</td>
<td>
<p>设置 Web SDK 容器的内联样式，例如宽高、边框等。</p>
</td>
</tr>
<tr>
<td>
<p><strong>refreshToken</strong></p>
</td>
<td>
<p>() =&gt; string</p>
</td>
<td>
<p>Promise<string></string></p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>async () =&gt; { const res = await fetch('/api/get-coze-token'); const data = await res.json(); return data.access_token; }</p>
</td>
</tr>
<tr>
<td>
<p><strong>token</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>czs_hsk**********</p>
</td>
<td>
<p>访问令牌，用于 Web SDK 鉴权。若传入此参数，Web SD 将优先使用该令牌进行身份验证，优先级高于 <code>refreshToken</code>。若无特殊需求，推荐直接使用 <code>refreshToken</code> 以实现自动续期。</p>
</td>
</tr>
<tr>
<td>
<p><strong>unauthorizedDescription</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>鉴权失败</p>
</td>
<td>
<p>未授权或鉴权失败时，界面展示的提示文案。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onIframeReady</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>Web SDK 内部 iframe 加载并初始化完成。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onIframeDestroy</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>组件卸载或 iframe 被销毁。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onProjectInfoLoaded</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>成功获取到 AI 编程智能体或工作流项目的基础信息（如名称、图标等）。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onTokenExpired</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>当前 Token 已过期。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onTokenInvalid</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>Token 校验失败（如格式错误、权限不足）。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onNetworkError</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>Web SDK 内部请求发生网络故障。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onNotify</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>接收到 Web SDK 发送的系统通知或状态变更。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>updateConfig(config: Config): void;  （更新 Web SDK 配置）</strong></p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript">interface <span class="hljs-title class_">Config</span> {
   <span class="hljs-attr">theme</span>: string;
   ....
}
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="interface Config {
   theme: string;
   ....
}" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<p>支持的配置项如下：</p>
<!-- @cols-width: 184,144,100,125,272 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 184px;"/><col style="width: 144px;"/><col style="width: 100px;"/><col style="width: 125px;"/><col style="width: 272px;"/></colgroup><thead>
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
<p><strong>theme</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>light</p>
</td>
<td>
<p>界面主题模式。取值如下：<br/>
light（默认值）：明亮模式。<br/>
dark：暗黑模式。</p>
</td>
</tr>
<tr>
<td>
<p><strong>className</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>coze-sdk-container</p>
</td>
<td>
<p>Web SDK 容器的 CSS 类名。</p>
</td>
</tr>
<tr>
<td>
<p><strong>style</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>width: 100%; height: 600px; border: 1px solid #e5e7eb; border-radius: 8px;</p>
</td>
<td>
<p>设置 Web SDK 容器的内联样式，例如宽高、边框等。</p>
</td>
</tr>
<tr>
<td>
<p><strong>unauthorizedDescription</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>鉴权失败</p>
</td>
<td>
<p>未授权或鉴权失败时，界面展示的提示文案。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>updateToken(token: string): void;</strong><br/>
<code>JavaScript     // 手动更新访问令牌。     cozeWebSDK.updateToken('YOUR_NEW_TOKEN');     </code></p>
</li>
<li>
<p><strong>destory(): void;</strong><br/>
<code>JavaScript     // 销毁 SDK 实例，移除 DOM 并解除所有事件监听。     cozeWebSDK.destroy();     </code></p>
</li>
</ul>
<h3 id="33d6d246" tabindex="-1">React 组件</h3>
<p>采用 React 组件 接入方式时，可参照以下操作步骤，同时结合对应的配置参考调整相关参数，确保接入效果符合需求。</p>
<h4 id="2d979767" tabindex="-1">操作步骤</h4>
<ol data-style="0">
<li>
<p>安装 Web SDK 依赖包。<br/>
在项目根目录下执行以下命令：</p>
<div style="position: relative">
<pre><code class="hljs language-Bash">npm i @coze/web-sdk@latest
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="npm i @coze/web-sdk@latest" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>
<p>引入并初始化组件。<br/>
在你的 React 应用中，引入 <code>CozeWebSDK</code>组件并进行基础配置。最简单的渲染方式如下：</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">CozeWebSDK</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/web-sdk/react'</span>;

<span class="hljs-keyword">const</span> <span class="hljs-title function_">CozeChatPage</span> = (<span class="hljs-params"></span>) =&gt; {
  <span class="hljs-keyword">return</span> (
    <span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">height:</span> '<span class="hljs-attr">600px</span>', <span class="hljs-attr">width:</span> '<span class="hljs-attr">100</span>%' }}&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-name">CozeWebSDK</span>
        // <span class="hljs-attr">替换为你的项目</span> <span class="hljs-attr">ID</span>，<span class="hljs-attr">用于指定要加载的智能体或工作流</span>。
        <span class="hljs-attr">projectId</span>=<span class="hljs-string">"YOUR_PROJECT_ID"</span> 
        <span class="hljs-attr">refreshToken</span>=<span class="hljs-string">{async</span> () =&gt;</span> { 
          // 在 Token 过期时，自动获取 Token。
          const data = await fetch('https://YOUR_SERVICE/GET_TOKEN_API'); 
          const result = await data.json(); 
          return result.token; 
        }} 
      /&gt;
    <span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span></span>
  );
};
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { CozeWebSDK } from '@coze/web-sdk/react';

const CozeChatPage = () =&gt; {
  return (
    &lt;div style={{ height: '600px', width: '100%' }}&gt;
      &lt;CozeWebSDK
        // 替换为你的项目 ID，用于指定要加载的智能体或工作流。
        projectId=&quot;YOUR_PROJECT_ID&quot; 
        refreshToken={async () =&gt; { 
          // 在 Token 过期时，自动获取 Token。
          const data = await fetch('https://YOUR_SERVICE/GET_TOKEN_API'); 
          const result = await data.json(); 
          return result.token; 
        }} 
      /&gt;
    &lt;/div&gt;
  );
};" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>
<p>配置 Token。</p>
<ul data-style="1">
<li>
<p><strong>方式一：Token 过期时自动获取（推荐）</strong><br/>
出于安全考虑，Token 通常具有较短的有效期。建议使用 <code>refreshToken</code> 属性，让 SDK 在 Token 过期时自动获取 Token，避免用户对话中断。</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript">&lt;<span class="hljs-title class_">CozeWebSDK</span>
  <span class="hljs-comment">// 替换为你的项目 ID，用于指定要加载的智能体或工作流。 </span>
  projectId=<span class="hljs-string">'YOUR_PROJECT_ID'</span> 
  refreshToken={<span class="hljs-title function_">async</span> () =&gt; { 
    <span class="hljs-comment">// 在 Token 过期时，自动获取 Token。</span>
    <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> <span class="hljs-title function_">fetch</span>(<span class="hljs-string">'https://YOUR_SERVICE/GET_TOKEN_API'</span>); 
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> data.<span class="hljs-title function_">json</span>(); 
    <span class="hljs-keyword">return</span> result.<span class="hljs-property">token</span>; 
  }} 
/&gt;
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="&lt;CozeWebSDK
  // 替换为你的项目 ID，用于指定要加载的智能体或工作流。 
  projectId='YOUR_PROJECT_ID' 
  refreshToken={async () =&gt; { 
    // 在 Token 过期时，自动获取 Token。
    const data = await fetch('https://YOUR_SERVICE/GET_TOKEN_API'); 
    const result = await data.json(); 
    return result.token; 
  }} 
/&gt;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<ul data-style="2">
<li>组件初始化完成后会立即调用一次<code>refreshToken</code>获取初始 Token。</li>
<li>当 Token 过期后，SDK 会自动调用<code>refreshToken</code>进行重试（最多等待 5000 毫秒）。</li>
<li>如果超时仍未获取到 Token，SDK 将上报<code>NETWORK_ERROR</code>事件。</li>
</ul>
</div>
</li>
<li>
<p><strong>方式二：手动刷新 Token（不推荐）</strong><br/>
通过 React 的 State 来管理 Token。出于安全考虑，不推荐将 Token 作为 State 频繁更新。如果使用此方式，建议你在后端服务为 Token 设置较短的过期时间。</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-comment">// 填写准备工作中获取的 Token。</span>
<span class="hljs-keyword">const</span> [token, setToken] = <span class="hljs-title function_">useState</span>(<span class="hljs-string">'YOUR_TOKEN'</span>); 
 
<span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">CozeWebSDK</span> 
  <span class="hljs-attr">projectId</span>=<span class="hljs-string">'YOUR_PROJECT_ID'</span> 
  <span class="hljs-attr">token</span>=<span class="hljs-string">{token}</span> 
/&gt;</span></span>
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 填写准备工作中获取的 Token。
const [token, setToken] = useState('YOUR_TOKEN'); 
 
&lt;CozeWebSDK 
  projectId='YOUR_PROJECT_ID' 
  token={token} 
/&gt;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ul>
</li>
</ol>
<h4 id="4a124046" tabindex="-1">配置参考</h4>
<p>配置 CozeWebSDK 组件属性 ，以满足定制化需求。</p>
<!-- @cols-width: 152,144,100,125,491 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 152px;"/><col style="width: 144px;"/><col style="width: 100px;"/><col style="width: 125px;"/><col style="width: 491px;"/></colgroup><thead>
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
<p><strong>projectId</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>是</p>
</td>
<td>
<p>761559609158873****</p>
</td>
<td>
<p>项目 ID，用于指定要加载的智能体或工作流。</p>
</td>
</tr>
<tr>
<td>
<p><strong>theme</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>light</p>
</td>
<td>
<p>界面主题模式。取值如下：<br/>
light（默认值）：明亮模式。<br/>
dark：暗黑模式。</p>
</td>
</tr>
<tr>
<td>
<p><strong>className</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>coze-sdk-container</p>
</td>
<td>
<p>Web SDK 容器的 CSS 类名。</p>
</td>
</tr>
<tr>
<td>
<p><strong>style</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>width: 100%; height: 600px; border: 1px solid #e5e7eb; border-radius: 8px;</p>
</td>
<td>
<p>设置 Web SDK 容器的内联样式，例如宽高、边框等。</p>
</td>
</tr>
<tr>
<td>
<p><strong>wrapClassName</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>coze-sdk-wrapper</p>
</td>
<td>
<p>外层包装元素的 CSS 类名，可用于全局样式控制。</p>
</td>
</tr>
<tr>
<td>
<p><strong>wrapStyle</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>margin: 20px auto; max-width: 1200px;</p>
</td>
<td>
<p>外层包装元素的内联样式，例如居中、最大宽度、外边距等。</p>
</td>
</tr>
<tr>
<td>
<p><strong>refreshToken</strong></p>
</td>
<td>
<p>() =&gt; string</p>
</td>
<td>
<p>Promise<string></string></p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>async () =&gt; { const res = await fetch('/api/get-coze-token'); const data = await res.json(); return data.access_token; }</p>
</td>
</tr>
<tr>
<td>
<p><strong>token</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>czs_hsk**********</p>
</td>
<td>
<p>访问令牌，用于 Web SDK 鉴权。若传入此参数，Web SD 将优先使用该令牌进行身份验证，优先级高于 <code>refreshToken</code>。若无特殊需求，推荐直接使用 <code>refreshToken</code> 以实现自动续期。</p>
</td>
</tr>
<tr>
<td>
<p><strong>unauthorizedDescription</strong></p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>鉴权失败</p>
</td>
<td>
<p>未授权或鉴权失败时，界面展示的提示文案。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onIframeReady</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>Web SDK 内部 iframe 加载并初始化完成。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onIframeDestroy</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>组件卸载或 iframe 被销毁。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onProjectInfoLoaded</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>成功获取到 AI 编程智能体或工作流项目的基础信息（如名称、图标等）。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onTokenExpired</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>当前 Token 已过期。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onTokenInvalid</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>Token 校验失败（如格式错误、权限不足）。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onNetworkError</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>Web SDK 内部请求发生网络故障。</p>
</td>
</tr>
<tr>
<td>
<p><strong>onNotify</strong></p>
</td>
<td>
<p>() =&gt; void</p>
</td>
<td>
<p>否</p>
</td>
<td>
<p>\</p>
</td>
<td>
<p>接收到 Web SDK 发送的系统通知或状态变更。</p>
</td>
</tr>
</tbody>
</table>
</div><h3 id="a6b4f59d" tabindex="-1">Iframe</h3>
<p>通过 Iframe 接入 Web SDK 的操作步骤如下。</p>
<ol data-style="0">
<li>添加 Iframe 标签。<br/>
在你的 HTML 页面中添加一个 <code>&lt;iframe&gt;</code> 标签。</li>
<li>添加通信脚本。<br/>
添加以下脚本来处理与 Iframe 的双向通信，包括发送初始化指令和响应 Token 更新请求。添加脚本时，需替换为实际的 <code>token</code>和<code>projectId</code>。
<div style="position: relative">
<pre><code class="hljs language-HTML"><span class="hljs-tag">&lt;<span class="hljs-name">script</span>&gt;</span><span class="language-javascript">
  <span class="hljs-keyword">const</span> cozeWebSDK = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"coze-web-sdk"</span>);  
  <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">COZE_WEB_SDK_ORIGIN</span> = <span class="hljs-string">"https://sdk.coze.site"</span>;
  <span class="hljs-variable language_">window</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">"message"</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =&gt;</span> {
    <span class="hljs-comment">// 只处理来自 SDK 的消息。</span>
    <span class="hljs-keyword">if</span> (event.<span class="hljs-property">origin</span> !== <span class="hljs-variable constant_">COZE_WEB_SDK_ORIGIN</span>) {
      <span class="hljs-keyword">return</span>;
    }
    <span class="hljs-keyword">const</span> data = event.<span class="hljs-property">data</span>;
    <span class="hljs-comment">// 监听到 IFRAME_READY 事件后，表示 WebSDK 已准备就绪。</span>
    <span class="hljs-keyword">if</span> (data.<span class="hljs-property">type</span> === <span class="hljs-string">"IFRAME_READY"</span>) {
      <span class="hljs-comment">// 初始化 WebSDK。</span>
      cozeWebSDK.<span class="hljs-property">contentWindow</span>.<span class="hljs-title function_">postMessage</span>({
        <span class="hljs-attr">type</span>: <span class="hljs-string">"INIT"</span>,
        <span class="hljs-attr">payload</span>: {
          <span class="hljs-comment">// 替换为你创建的 Token。作为初始化时的访问凭证，用于首次加载 WebSDK 时完成身份验证。</span>
          <span class="hljs-attr">token</span>: <span class="hljs-string">'YOUR_TOKEN'</span>, 
          <span class="hljs-comment">// 替换为你的项目 ID，用于指定要加载的智能体或工作流。</span>
          <span class="hljs-attr">projectId</span>: <span class="hljs-string">'YOUR_PROJECT_ID'</span>
        }
      }, <span class="hljs-variable constant_">COZE_WEB_SDK_ORIGIN</span>);
    }
    <span class="hljs-comment">// Token 过期通知。</span>
    <span class="hljs-keyword">if</span> (data.<span class="hljs-property">type</span> === <span class="hljs-string">"TOKEN_EXPIRED"</span>) {
      <span class="hljs-comment">// 更新 Token。</span>
      cozeWebSDK.<span class="hljs-property">contentWindow</span>.<span class="hljs-title function_">postMessage</span>({
        <span class="hljs-attr">type</span>: <span class="hljs-string">"UPDATE_TOKEN"</span>,
        <span class="hljs-attr">payload</span>: {
          <span class="hljs-attr">token</span>: <span class="hljs-string">'YOUR_NEW_TOKEN'</span>,
        }
      }, <span class="hljs-variable constant_">COZE_WEB_SDK_ORIGIN</span>);
    }
  });
</span><span class="hljs-tag">&lt;/<span class="hljs-name">script</span>&gt;</span>
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="&lt;script&gt;
  const cozeWebSDK = document.getElementById(&quot;coze-web-sdk&quot;);  
  const COZE_WEB_SDK_ORIGIN = &quot;https://sdk.coze.site&quot;;
  window.addEventListener(&quot;message&quot;, (event) =&gt; {
    // 只处理来自 SDK 的消息。
    if (event.origin !== COZE_WEB_SDK_ORIGIN) {
      return;
    }
    const data = event.data;
    // 监听到 IFRAME_READY 事件后，表示 WebSDK 已准备就绪。
    if (data.type === &quot;IFRAME_READY&quot;) {
      // 初始化 WebSDK。
      cozeWebSDK.contentWindow.postMessage({
        type: &quot;INIT&quot;,
        payload: {
          // 替换为你创建的 Token。作为初始化时的访问凭证，用于首次加载 WebSDK 时完成身份验证。
          token: 'YOUR_TOKEN', 
          // 替换为你的项目 ID，用于指定要加载的智能体或工作流。
          projectId: 'YOUR_PROJECT_ID'
        }
      }, COZE_WEB_SDK_ORIGIN);
    }
    // Token 过期通知。
    if (data.type === &quot;TOKEN_EXPIRED&quot;) {
      // 更新 Token。
      cozeWebSDK.contentWindow.postMessage({
        type: &quot;UPDATE_TOKEN&quot;,
        payload: {
          token: 'YOUR_NEW_TOKEN',
        }
      }, COZE_WEB_SDK_ORIGIN);
    }
  });
&lt;/script&gt;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ol>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button class="feedbackButton-GuivRC" type="button"><span class="feedbackButtonIcon-PqHraK"></span><span>有帮助</span></button><button class="feedbackButton-GuivRC" type="button"><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm" data-discover="true" href="/developer_guides_go_getting_started"><div class="cardLabel-sDu1uC"><svg aria-hidden="true" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12">快速开始</div></a><a class="card-T4zaCm nextCard-lFoioT" data-discover="true" href="/developer_guides_ui_builder_web_sdk"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg aria-hidden="true" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">Web SDK（低代码）</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#708de81d" href="#708de81d" title="Web SDK 介绍">Web SDK 介绍</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#01197823" href="#01197823" title="准备工作">准备工作</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#5c5ef996" href="#5c5ef996" title="快速体验">快速体验</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#4931f21c" href="#4931f21c" title="接入方式">接入方式</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#6ca31889" href="#6ca31889" title="接入流程">接入流程</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#cd64cb2b" href="#cd64cb2b" title="JavaScript">JavaScript</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#b63cf96a" href="#b63cf96a" title="操作步骤">操作步骤</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#dfc82e7b" href="#dfc82e7b" title="配置参考">配置参考</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#33d6d246" href="#33d6d246" title="React 组件">React 组件</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#2d979767" href="#2d979767" title="操作步骤">操作步骤</a></div><div class="arco-anchor-link" style="margin-left:30px"><a class="arco-anchor-link-title" data-href="#4a124046" href="#4a124046" title="配置参考">配置参考</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#a6b4f59d" href="#a6b4f59d" title="Iframe">Iframe</a></div></div></div></div></div></div></div></div>
</body></html>