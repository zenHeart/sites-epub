<!DOCTYPE html>
<html><head><meta charset="utf-8"/><meta content="width=device-width,initial-scale=1,shrink-to-fit=no,viewport-fit=cover,minimum-scale=1,maximum-scale=1,user-scalable=no" name="viewport"/><meta content="ie=edge" http-equiv="x-ua-compatible"/><meta content="webkit" name="renderer"/><meta content="standard" name="layoutmode"/><meta content="force" name="imagemode"/><meta content="no" name="wap-font-scale"/><meta content="telephone=no" name="format-detection"/><title data-react-helmet="true">集成语音合成 SDK</title><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/main.0a4ac522c6.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/4760.77ece367d4.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/page.782417a8ae.css" rel="stylesheet"/><link href="//lf-arcosite.bytecdn.com/obj/arcosites/topic-cdn-1/static/css/async/rag-widget.89316741c1.css" rel="stylesheet"/> <link data-react-helmet="true" href="https://docs.coze.cn/dev_how_to_guides_install_wsspeech_sdk" rel="canonical"/><link data-react-helmet="true" href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png" rel="icon"/><link data-react-helmet="true" href="/dev_how_to_guides_install_wsspeech_sdk.md" rel="alternate" type="text/markdown"/><link data-react-helmet="true" href="/llms.txt" rel="alternate" type="text/plain"/>
<meta content="bYRLfQ-NyrDoYH7ELmQzOhVz5qBW5RpEOMsH9sVAuqE" data-react-helmet="true" name="google-site-verification"/>
<meta content="codeva-mJmA0HNtAv" name="baidu-site-verification"/></head><body><div id="root"><div class="container-IT4TcI" data-topic-nav="true"><div class="container-lAGFGi"><a class="brand-qR7tMP" href="https://www.coze.cn" rel="noreferrer" target="_blank"><img alt="扣子" class="siteIcon-qohRRP" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/135afe80ad8d4b4e93ec55ec2de2ce12~tplv-goo7wpa0wc-topic.png"/><div class="title-VkV7Dt">扣子</div></a><div class="divider-rNUHDJ"></div><div class="tabs-xFWbDf"><a class="tab-JssokC" data-discover="true" href="/what_is_coze">扣子</a><a class="tab-JssokC" data-discover="true" href="/guides_welcome">扣子编程</a><a class="tab-JssokC" data-discover="true" href="/ppt-plugin">教程</a><a class="tab-JssokC" data-discover="true" href="/coze_pro_billing_overview">定价</a><a class="tab-JssokC activeTab-g8RDKO" data-discover="true" href="/dev_how_to_guides_install_wsspeech_sdk"><span>资源</span><span class="arrow-nKMrBv"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></a></div></div><div class="container-RisWb7"><div class="container-NSGsG0"><svg fill="none" height="16" viewbox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1944_44928)"><path clip-rule="evenodd" d="M6.66768 1.0369C7.03352 0.996085 7.33357 1.2987 7.33369 1.66679C7.33369 2.03497 7.03309 2.32921 6.66865 2.38163C5.98178 2.48048 5.32258 2.73131 4.74092 3.11991C3.97349 3.63269 3.37538 4.36191 3.02217 5.21464C2.66898 6.06735 2.57648 7.0057 2.75654 7.91093C2.93663 8.8161 3.38129 9.64798 4.03389 10.3006C4.68637 10.9529 5.51766 11.3969 6.42256 11.5769C7.32775 11.757 8.26617 11.6645 9.11885 11.3113C9.97157 10.9581 10.7008 10.36 11.2136 9.59257C11.6022 9.01082 11.854 8.3518 11.9528 7.66483C12.0053 7.30039 12.2985 7.00077 12.6667 7.00077C13.0349 7.00077 13.3374 7.29989 13.2966 7.66581C13.1904 8.61707 12.8573 9.53257 12.322 10.3338C12.1812 10.5444 12.026 10.7435 11.861 10.9334C11.9395 10.9678 12.0136 11.0156 12.0778 11.0799L14.8308 13.8318C15.1071 14.1081 15.1069 14.5564 14.8308 14.8328C14.5544 15.1092 14.1062 15.1092 13.8298 14.8328L11.0769 12.0808C10.9995 12.0035 10.9459 11.9119 10.9118 11.8152C10.5178 12.1081 10.0879 12.3539 9.62959 12.5437C8.53325 12.9979 7.32666 13.117 6.16279 12.8855C4.99891 12.654 3.92964 12.0821 3.09053 11.243C2.25147 10.4039 1.68043 9.33453 1.44893 8.17069C1.21745 7.00685 1.33564 5.80021 1.78975 4.70389C2.24386 3.60767 3.01314 2.67076 3.99971 2.01151C4.80086 1.4762 5.71649 1.14308 6.66768 1.0369ZM10.3503 1.54179C10.484 1.04235 11.1932 1.04235 11.3269 1.54179C11.5619 2.41957 12.2479 3.10561 13.1257 3.34061C13.6247 3.47452 13.6248 4.18237 13.1257 4.3162C12.2511 4.55034 11.5672 5.23297 11.3317 6.10721L11.3269 6.12675C11.1925 6.62492 10.4857 6.62483 10.3513 6.12675C10.1135 5.24388 9.42356 4.55405 8.54072 4.3162C8.04227 4.18195 8.04227 3.47486 8.54072 3.34061L8.56026 3.33475C9.43418 3.09922 10.1161 2.41608 10.3503 1.54179Z" fill="url(#paint0_linear_1944_44928)" fill-rule="evenodd"></path></g><defs><lineargradient gradientunits="userSpaceOnUse" id="paint0_linear_1944_44928" x1="1.3335" x2="15.0379" y1="15.0401" y2="15.0401"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></lineargradient><clippath id="clip0_1944_44928"><rect fill="white" height="16" width="16"></rect></clippath></defs></svg><input class="input-tjtw6Q" placeholder="搜索" readonly="" type="text"/></div><div class="themeIcon-EcSp2T"><svg class="arco-icon" fill="currentColor" viewbox="5 5 22 22" xmlns="http://www.w3.org/2000/svg"><path d="M16.4092 22.9541C16.6349 22.9542 16.8182 23.1376 16.8184 23.3633V24.5908C16.8184 24.8167 16.6351 24.9999 16.4092 25H15.5908C15.3649 25 15.1816 24.8167 15.1816 24.5908V23.3633C15.1818 23.1375 15.365 22.9541 15.5908 22.9541H16.4092ZM10.2148 20.6279C10.3745 20.4686 10.6333 20.4686 10.793 20.6279L11.3721 21.207C11.5314 21.3667 11.5314 21.6255 11.3721 21.7852L10.5039 22.6533C10.3442 22.813 10.0856 22.8128 9.92578 22.6533L9.34668 22.0742C9.18721 21.9144 9.18704 21.6558 9.34668 21.4961L10.2148 20.6279ZM21.207 20.6279C21.3667 20.4686 21.6255 20.4686 21.7852 20.6279L22.6533 21.4961C22.813 21.6558 22.8128 21.9144 22.6533 22.0742L22.0742 22.6533C21.9144 22.8128 21.6558 22.813 21.4961 22.6533L20.6279 21.7852C20.4686 21.6255 20.4685 21.3667 20.6279 21.207L21.207 20.6279ZM16 10.2725C19.1631 10.2725 21.7275 12.8369 21.7275 16C21.7275 19.163 19.163 21.7275 16 21.7275C12.837 21.7275 10.2725 19.163 10.2725 16C10.2725 12.8369 12.8369 10.2725 16 10.2725ZM16 11.9092C13.7407 11.9092 11.9092 13.7407 11.9092 16C11.9092 18.2593 13.7407 20.0908 16 20.0908C18.2593 20.0908 20.0908 18.2593 20.0908 16C20.0908 13.7407 18.2593 11.9092 16 11.9092ZM8.63672 15.1816C8.86249 15.1818 9.0459 15.365 9.0459 15.5908V16.4092C9.04575 16.6349 8.8624 16.8182 8.63672 16.8184H7.40918C7.18334 16.8184 7.00015 16.635 7 16.4092V15.5908C7 15.3649 7.18325 15.1816 7.40918 15.1816H8.63672ZM24.5908 15.1816C24.8168 15.1816 25 15.3649 25 15.5908V16.4092C24.9999 16.635 24.8167 16.8184 24.5908 16.8184H23.3633C23.1376 16.8182 22.9542 16.6349 22.9541 16.4092V15.5908C22.9541 15.365 23.1375 15.1818 23.3633 15.1816H24.5908ZM9.92578 9.34668C10.0856 9.18713 10.3442 9.18699 10.5039 9.34668L11.3721 10.2148C11.5314 10.3746 11.5315 10.6333 11.3721 10.793L10.793 11.3711C10.6332 11.5309 10.3746 11.5309 10.2148 11.3711L9.34668 10.5039C9.18692 10.3441 9.18692 10.0846 9.34668 9.9248L9.92578 9.34668ZM21.4961 9.34668C21.6558 9.18699 21.9144 9.18713 22.0742 9.34668L22.6533 9.9248C22.8131 10.0846 22.8131 10.3441 22.6533 10.5039L21.7852 11.3711C21.6254 11.5309 21.3668 11.5309 21.207 11.3711L20.6279 10.793C20.4685 10.6333 20.4686 10.3746 20.6279 10.2148L21.4961 9.34668ZM16.4092 7C16.6351 7.00006 16.8184 7.18328 16.8184 7.40918V8.63672C16.8182 8.86247 16.635 9.04584 16.4092 9.0459H15.5908C15.365 9.04586 15.1818 8.86248 15.1816 8.63672V7.40918C15.1816 7.18327 15.3649 7.00004 15.5908 7H16.4092Z"></path></svg></div></div></div><div class="topic-rag-widget"><div><div class="topic-rag-agent-sideBtn"><span class="topic-rag-logo-light"><svg fill="none" height="48" viewbox="0 0 48 48" width="48" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#262E3B"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="white"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="white"></path></g><defs><clippath id="clip0_2_6"><rect fill="white" height="48" width="48"></rect></clippath></defs></svg></span><span class="topic-rag-logo-dark"><svg fill="none" height="48" viewbox="0 0 48 48" width="48" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2_6)"><path d="M36 0H12C5.37258 0 0 5.37258 0 12V36C0 42.6274 5.37258 48 12 48H36C42.6274 48 48 42.6274 48 36V12C48 5.37258 42.6274 0 36 0Z" fill="#DFDFDF"></path><path d="M24 13C24.8571 19.5185 27.8571 23.1852 33 24C27.8571 24.8148 24.8571 28.4815 24 35C23.1429 28.4815 20.1429 24.8148 15 24C20.1429 23.1852 23.1429 19.5185 24 13Z" fill="#262E3B"></path><path d="M33 16C33.5523 16 34 15.5523 34 15C34 14.4477 33.5523 14 33 14C32.4477 14 32 14.4477 32 15C32 15.5523 32.4477 16 33 16Z" fill="#262E3B"></path></g><defs><clippath id="clip0_2_6"><rect fill="#262E3B" height="48" width="48"></rect></clippath></defs></svg></span></div></div><div class="topic-rag-chat-modal" style="right:-450px"><div class="topic-rag-header"><span style="display:flex"><span><svg height="24" role="img" viewbox="0 0 40 40" width="24" xmlns="http://www.w3.org/2000/svg"><defs><lineargradient gradientunits="userSpaceOnUse" id="starGradient" x1="1.25" x2="29.602" y1="35.735" y2="29.277"><stop offset="0.1" stop-color="#3B91FF"></stop><stop offset="0.5" stop-color="#0D5EFF"></stop><stop offset="0.85" stop-color="#C069FF"></stop></lineargradient></defs><path d="M20 8 Q22 18 29 19 Q22 20 20 30 Q18 20 11 19 Q18 18 20 8 Z" fill="url(#starGradient)"></path><circle cx="29" cy="12" fill="url(#starGradient)" fill-opacity="0.8" r="1.2"></circle></svg></span><span style="line-height:24px">AI 助手</span></span><div><button class="arco-btn arco-btn-text arco-btn-size-mini arco-btn-shape-square arco-btn-icon-only" type="button"><svg aria-hidden="true" class="arco-icon arco-icon-close" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M9.857 9.858 24 24m0 0 14.142 14.142M24 24 38.142 9.858M24 24 9.857 38.142"></path></svg></button></div></div><div class="topic-rag-chat"><div class="topic-rag-chat-list"><div class="topic-rag-chat-welcome"><div class="topic-rag-chat-welcome-title"><span style="color:#737A87">扣子</span><span> <!-- -->AI 帮助与支持</span></div><div class="topic-rag-chat-welcome-desc">你好，我是 扣子 文档问答助手 🎉
你在阅读当前文档的过程中，无论对文档概念的解释，还是文档内容方面的疑问，都可以随时向我提问，我会全力为你解答</div><div class="topic-rag-chat-recommend"><div class="arco-space arco-space-horizontal arco-space-align-center"><div class="arco-space-item" style="margin-right:8px"><span style="display:flex;margin-left:4px"><svg fill="none" height="14" viewbox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_28960)"><path d="M8.74957 12.2503C8.91055 12.2503 9.04139 12.3804 9.04156 12.5413V13.1253C9.04138 13.2862 8.91054 13.4163 8.74957 13.4163H5.24957C5.08863 13.4162 4.95859 13.2863 4.95855 13.1253C4.95855 12.9471 4.95855 12.7198 4.95855 12.5413C4.9586 12.3804 5.08862 12.2503 5.24957 12.2503H8.74957ZM6.94293 0.584296C7.44408 0.575011 7.94178 0.638334 8.41949 0.770819C8.57621 0.81436 8.65772 0.983814 8.60308 1.13703L8.39898 1.70832C8.34543 1.85841 8.18115 1.9368 8.02691 1.8968C7.68281 1.80731 7.32512 1.7651 6.96539 1.7718C6.28892 1.78443 5.62844 1.97088 5.05328 2.31183C4.47821 2.6528 4.00964 3.13544 3.69488 3.70832C3.38011 4.2812 3.23072 4.92414 3.26129 5.57062C3.29187 6.21711 3.50098 6.84481 3.86871 7.38801C4.23653 7.93135 4.74971 8.37118 5.35504 8.66047C5.56344 8.76018 5.69586 8.96698 5.69586 9.19367V10.4788H8.38238V9.19367C8.38238 8.96633 8.51483 8.75885 8.72418 8.65949C8.8826 8.58429 9.22645 8.36143 9.4732 8.19367C9.59698 8.10951 9.76577 8.12821 9.86578 8.23957L10.313 8.73762C10.4173 8.85392 10.409 9.02977 10.2818 9.12043C10.0386 9.29368 9.7153 9.48154 9.59723 9.54914V10.6029C9.59723 10.8875 9.48009 11.159 9.27398 11.3577C9.06788 11.5562 8.78934 11.6663 8.50152 11.6663H5.57574C5.28792 11.6663 5.01034 11.5562 4.80426 11.3577C4.59789 11.159 4.48004 10.8876 4.48004 10.6029V9.54816C3.82878 9.17354 3.2722 8.6594 2.85504 8.04328C2.36679 7.32201 2.0872 6.48684 2.04644 5.62531C2.00574 4.7639 2.20537 3.90803 2.62359 3.1468C3.04187 2.38552 3.66396 1.74739 4.4234 1.29719C5.18275 0.847044 6.05277 0.600868 6.94293 0.584296ZM9.81305 2.34308C9.91705 1.94211 10.4863 1.94074 10.5923 2.34113L10.6978 2.73957C10.8458 3.29999 11.2829 3.7381 11.8433 3.88605L12.2418 3.99055C12.6425 4.09637 12.641 4.66593 12.2398 4.76984L11.8482 4.87141C11.2847 5.01743 10.8436 5.45602 10.6949 6.01887L10.5923 6.40851C10.4865 6.80928 9.91691 6.80787 9.81305 6.40656L9.71441 6.02473C9.56781 5.45829 9.12553 5.01519 8.55914 4.86848L8.17633 4.76984C7.7753 4.66583 7.77385 4.09646 8.17437 3.99055L8.56402 3.88801C9.12708 3.73933 9.56653 3.29847 9.71246 2.73469L9.81305 2.34308Z" fill="url(#paint0_linear_7153_28960)"></path></g><defs><lineargradient gradientunits="userSpaceOnUse" id="paint0_linear_7153_28960" x1="2.04126" x2="12.5415" y1="13.4163" y2="13.4163"><stop offset="0.01" stop-color="#3B91FF"></stop><stop offset="0.4" stop-color="#0D5EFF"></stop><stop offset="0.995" stop-color="#C069FF"></stop></lineargradient><clippath id="clip0_7153_28960"><rect fill="white" height="14" width="14"></rect></clippath></defs></svg></span></div><div class="arco-space-item">推荐问题</div></div><div class="arco-space arco-space-vertical topic-rag-chat-recommend-list"><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子 3.0 都有什么新特性？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item" style="margin-bottom:8px"><div><span class="arco-link topic-rag-chat-recommend-question">扣子和扣子编程有什么区别？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div><div class="arco-space-item"><div><span class="arco-link topic-rag-chat-recommend-question">扣子如何收费？<svg aria-hidden="true" class="arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></span></div></div></div></div></div><div class="topic-rag-chat-list-actions"><div class="topic-rag-chat-new-btn"><button class="arco-btn arco-btn-outline arco-btn-size-mini arco-btn-shape-square arco-btn-disabled" disabled="" style="border-radius:4px;height:28px" type="button"><svg aria-hidden="true" class="arco-icon arco-icon-plus" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M5 24h38M24 5v38"></path></svg><span>新对话</span></button></div></div><div></div></div><div class="topic-rag-chat-bottom"><div class="topic-rag-chat-input-border"><div class="topic-rag-chat-input"><textarea class="arco-textarea topic-rag-chat-textarea" placeholder="输入您的问题..."></textarea><button class="arco-btn arco-btn-text arco-btn-size-small arco-btn-shape-square arco-btn-icon-only arco-btn-disabled topic-rag-chat-send" disabled="" style="color:#c7ccd6" type="button"><svg fill="none" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_7153_32885)"><path clip-rule="evenodd" d="M4.875 4.50105V9.37605L4.8779 9.44199C4.89332 9.61674 4.96965 9.78136 5.09467 9.90638L7.18934 12.001L5.09467 14.0957L5.05009 14.1444C4.93743 14.2789 4.875 14.4492 4.875 14.626V19.501L4.877 19.5571C4.91534 20.0925 5.49859 20.4219 5.98164 20.1608L19.8566 12.6608L19.909 12.6299C20.3805 12.326 20.363 11.615 19.8566 11.3413L5.98164 3.84127L5.93134 3.81635C5.44214 3.59551 4.875 3.95195 4.875 4.50105ZM7.18934 12.001L6.44045 12.75H12.0001C12.2072 12.75 12.3751 12.5821 12.3751 12.375V11.625C12.3751 11.4179 12.2072 11.25 12.0001 11.25H6.43835L7.18934 12.001Z" fill="currentColor" fill-rule="evenodd"></path></g><defs><clippath id="clip0_7153_32885"><rect fill="white" height="18" transform="translate(3 3)" width="18"></rect></clippath></defs></svg></button></div></div></div></div></div></div><div class="floatingEntry-vueVAD"><div class="floatingEntryButton-FSWoD4">文档反馈</div></div><div class="container-EO_NtE"><div class="content-OAy9RZ"><div class="container-RkwAC2" data-topic-tree="true" style="width:300px"><div class="content-KOLZ20"><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b97434bdbc784e3ce84ce"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="低代码项目">低代码项目</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a55df9a4bdbc784e3c9738f"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="动态">动态</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf30d"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="快速开始">快速开始</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf317"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="智能体">智能体</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf31d"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="工作流">工作流</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf325"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="应用">应用</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf334"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="资源">资源</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf32e"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="发布">发布</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf35a"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="模型">模型</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf362"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="协作">协作</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8e614bdbc784e3cce185"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="开发工具">开发工具</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8d4bdbc784e3cc3e2c"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="API 参考">API 参考</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8d4bdbc784e3cc3fa8"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="SDK 参考">SDK 参考</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8bc84bdbc784e3cc529d"><div class="nodeContent-GigwSX" style="margin-left:24px" to="/"><span class="nodeTitle-ONnqtP" title="音视频">音视频</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52a5"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_overview" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="智能音视频概述">智能音视频概述</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52ad"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_playground" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="体验智能音视频 Demo">体验智能音视频 Demo</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52b5"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_access" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="音视频接入方案对比">音视频接入方案对比</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52bf"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="基于 WebSocket 实现音频通话">基于 WebSocket 实现音频通话</span><span class="arrow-l0IAct expanded-jh8lWp"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div><div class="children-Z8xymb"><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc94bdbc784e3cc5355"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_websocket_openapi" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="基于 WebSocket OpenAPI 实现音频通话">基于 WebSocket OpenAPI 实现音频通话</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc94bdbc784e3cc535c"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_install_wschat_sdk" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="集成 WebSocket 实时语音 Web SDK">集成 WebSocket 实时语音 Web SDK</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc94bdbc784e3cc5363"><a class="nodeContent-GigwSX active-dE_WV_" data-discover="true" href="/dev_how_to_guides_install_wsspeech_sdk" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="集成语音合成 SDK">集成语音合成 SDK</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="3" id="tree-node-6a3b8bc94bdbc784e3cc536a"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_install_wstranscription_sdk" style="margin-left:56px"><span class="nodeTitle-ONnqtP" title="集成语音识别 SDK">集成语音识别 SDK</span></a></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52c6"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="基于 RTC 实现音视频通话">基于 RTC 实现音视频通话</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52e5"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_audio_message" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="基于 HTTP 请求实现语音消息">基于 HTTP 请求实现语音消息</span></a></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52ed"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="语音与音色">语音与音色</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc52f3"><div class="nodeContent-GigwSX" style="margin-left:40px" to="/"><span class="nodeTitle-ONnqtP" title="终端用户用量管控">终端用户用量管控</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="2" id="tree-node-6a3b8bc84bdbc784e3cc533c"><a class="nodeContent-GigwSX" data-discover="true" href="/dev_how_to_guides_realtime_faq" style="margin-left:40px"><span class="nodeTitle-ONnqtP" title="音视频常见问题">音视频常见问题</span></a></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="1" id="tree-node-6a3b8b8e4bdbc784e3cc445f"><a class="nodeContent-GigwSX" data-discover="true" href="/developer_guides_coze_cli" style="margin-left:24px"><span class="nodeTitle-ONnqtP" title="Coze CLI">Coze CLI</span></a></div></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf33f"><div class="nodeContent-GigwSX" style="margin-left:8px" to="/"><span class="nodeTitle-ONnqtP" title="推广与变现">推广与变现</span><span class="arrow-l0IAct"><svg fill="currentColor" height="16" viewbox="0 0 24 24" width="16"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z"></path></svg></span></div></div><div class="nodeWrapper-woTZn5" data-tree-level="0" id="tree-node-6a3b8ae84bdbc784e3cbf369"><a class="nodeContent-GigwSX" data-discover="true" href="/guides_FAQ" style="margin-left:8px"><span class="nodeTitle-ONnqtP" title="常见问题">常见问题</span></a></div></div><div aria-label="拖拽调整目录宽度" aria-orientation="vertical" class="resizeHandle-lop5IL" role="separator"></div></div><div class="container-h8FsmA" data-topic-doc="true" style="width:calc(100% - 300px);--anchor-width:260px"><div class="content-gmBCKL"><div class="container-qOTtH7" data-topic-doc-header="true"><div class="main-HmKTLR"><div class="breadcrumb-i7qXyA"><span>低代码</span><span class="separator-KB9yMa">/</span><span>开发工具</span><span class="separator-KB9yMa">/</span><span>音视频</span><span class="separator-KB9yMa">/</span><span>基于 WebSocket 实现音频通话</span><span class="separator-KB9yMa">/</span><span class="currentCrumb-OqBki6">集成语音合成 SDK</span></div><div class="titleContainer-hr8uxx"><h1 class="title-C1b1pA" data-h0="true" id="doc_title">集成语音合成 SDK</h1><aside class="mdx-live-widget">
<p class="mdx-live-widget-label">Interactive explorer</p>
<p>This directory tree is interactive on the original page and cannot run inside an EPUB. Open it here: <a class="source-title" href="https://docs.coze.cn/dev_how_to_guides_install_wsspeech_sdk#explore-the-directory" rel="external">https://docs.coze.cn/dev_how_to_guides_install_wsspeech_sdk#explore-the-directory</a></p>
</aside><div class="actions-qfEaDN"><div class="copyButton-bnyWaE"><svg aria-hidden="true" class="copyIcon-iTB4A1 arco-icon arco-icon-copy" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M20 6h18a2 2 0 0 1 2 2v22M8 16v24c0 1.105.891 2 1.996 2h20.007A1.99 1.99 0 0 0 32 40.008V15.997A1.997 1.997 0 0 0 30 14H10a2 2 0 0 0-2 2Z"></path></svg></div><div class="moreButton-ZJ3qDg"><svg aria-hidden="true" class="arco-icon arco-icon-down" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M39.6 17.443 24.043 33 8.487 17.443"></path></svg></div></div></div></div></div><div class="topic-markdown" data-topic-doc-content="true"><p>语音合成 SDK（简称 WsSpeech SDK）基于双向流式语音合成 WebSocket OpenAPI 封装，提供了完整且高效的语音交互解决方案。它具备实时语音合成、文本播放、灵活的播放控制和丰富的音色选择等功能，适用于智能对话系统、语音导航和有声内容生成等多种应用场景，帮助开发者快速实现高质量的语音交互功能。更多接口详情请参考<a href="/developer_guides/tts_api" target="_blank">双向流式语音合成</a>。</p>
<h2 id="b74c4354" tabindex="-1">体验 Demo</h2>
<p>扣子提供<a href="https://www.coze.cn/open-platform/realtime/websocket?surl_token=FJvCs&amp;zlink_code=FFKdE&amp;utm_medium=docs&amp;utm_source=docs&amp;utm_content=landingpage&amp;utm_id=&amp;utm_campaign=&amp;utm_term=docs&amp;utm_source_platform=#/speech" target="_blank">语音合成 Demo</a> 和 TypeScript 格式的<a href="https://github.com/coze-dev/coze-js/tree/main/examples/realtime-websocket" target="_blank">语音合成示例源码</a>，帮助你快速体验语音合成的功能，并根据示例源码快速实现语音合成。</p>
<h3 id="3c7a17e1" tabindex="-1">Demo 功能简介</h3>
<p>Demo 的主要功能包括：</p>
<ul data-style="0">
<li>支持整句播放和流式播放两种模式</li>
<li>实时文本编辑和预览</li>
<li>支持停止或暂停播放</li>
</ul>
<p><img alt="Image" height="479" loading="lazy" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b91a39beff3b4e9a95efa136a801fa72~tplv-goo7wpa0wc-topic.webp" width="800"/></p>
<h3 id="4c4ffca4" tabindex="-1">使用 Demo</h3>
<ol data-style="0">
<li>
<p>配置参数。<br/>
单击右上角的 <strong>Settings</strong>，配置个人访问令牌和音色 ID，具体如下表所示。</p>
<!-- @cols-width: 141,638 -->
<div class="topic-table-container">
<table class="topic-table-fixed">
<colgroup><col style="width: 141px;"/><col style="width: 638px;"/></colgroup><thead>
<tr>
<th>
<p><strong>配置</strong></p>
</th>
<th>
<p><strong>说明</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Base WS URL</p>
</td>
<td>
<p>保持默认值 <code>wss://ws.coze.cn</code>。</p>
</td>
</tr>
<tr>
<td>
<p>个人访问令牌</p>
</td>
<td>
<p>扣子 API &amp; SDK 通过访问令牌进行 API &amp; SDK 请求的鉴权。<br/>
个人访问令牌的获取方式可参考<a href="/developer_guides/pat" target="_blank">添加个人访问令牌</a>。</p>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>应为令牌授予 <code>createSpeech</code>、<code>listVoice</code> 的权限。</p>
</div>
</td>
</tr>
<tr>
<td>
<p>音色 ID</p>
</td>
<td>
<p>设置智能体使用的音色。<br/>
扣子提供一系列系统音色，你可以在<a href="/dev_how_to_guides/sys_voice" target="_blank">系统音色列表</a>查看音色 ID，或通过<a href="/developer_guides/list_voices" target="_blank">查看音色列表</a> API 获取可用的音色列表。如果不指定 <code>voiceId</code> 或值为空，将使用默认的<code>柔美女友</code>音色，音色 ID 为 7426720361733046281。</p>
</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p>在文本框中输入待合成的文本，单击<strong>整句播放</strong>或<strong>流式播放</strong>。</p>
</li>
</ol>
<h2 id="dfac9b31" tabindex="-1">完整示例代码</h2>
<p>以下是基于 React 和 Antd 框架开发的语音合成示例代码，具备文本输入、播放控制和状态显示等核心功能，能帮助你快速了解语音合成的实现流程。<br/>
使用前需配置个人访问令牌（ACCESS_TOKEN），并安装<code>@coze/api</code>、<code>antd</code>、<code>react</code>等依赖，建议开发时开启调试模式。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, { useEffect, useRef, useState } <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> {
  <span class="hljs-title class_">Button</span>,
  <span class="hljs-title class_">Layout</span>,
  <span class="hljs-title class_">Space</span>,
  <span class="hljs-title class_">Typography</span>,
  message,
  <span class="hljs-title class_">Row</span>,
  <span class="hljs-title class_">Col</span>,
  <span class="hljs-title class_">Card</span>,
  <span class="hljs-title class_">Input</span>,
} <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> { <span class="hljs-title class_">WsSpeechClient</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/api/ws-tools'</span>;
<span class="hljs-keyword">import</span> {
  <span class="hljs-title class_">SoundOutlined</span>,
  <span class="hljs-title class_">PauseOutlined</span>,
  <span class="hljs-title class_">PlayCircleOutlined</span>,
  <span class="hljs-title class_">StopOutlined</span>,
} <span class="hljs-keyword">from</span> <span class="hljs-string">'@ant-design/icons'</span>;

<span class="hljs-keyword">const</span> { <span class="hljs-title class_">Title</span>, <span class="hljs-title class_">Paragraph</span>, <span class="hljs-title class_">Text</span> } = <span class="hljs-title class_">Typography</span>;
<span class="hljs-keyword">const</span> { <span class="hljs-title class_">TextArea</span> } = <span class="hljs-title class_">Input</span>;

<span class="hljs-comment">// 个人访问令牌</span>
<span class="hljs-keyword">const</span> <span class="hljs-variable constant_">ACCESS_TOKEN</span> =<span class="hljs-string">'pat_Qm47PKJR5dvMOP53v6DyzwCbTtvEZHQc2TVINEveg9v1T3iSYlTdScJ8***'</span>;
<span class="hljs-comment">// 音色ID</span>
<span class="hljs-keyword">const</span> <span class="hljs-variable constant_">VOICE_ID</span> = <span class="hljs-string">''</span>; <span class="hljs-comment">// 可选</span>

<span class="hljs-keyword">const</span> <span class="hljs-title class_">SpeechDemo</span>: <span class="hljs-title class_">React</span>.<span class="hljs-property">FC</span> = <span class="hljs-function">() =&gt;</span> {
  <span class="hljs-keyword">const</span> clientRef = useRef&lt;<span class="hljs-title class_">WsSpeechClient</span>&gt;();
  <span class="hljs-keyword">const</span> [transcriptionText, setTranscriptionText] =
    <span class="hljs-title function_">useState</span>(<span class="hljs-string">'你好，这是一个文本转语音测试。'</span>);
  <span class="hljs-keyword">const</span> [isPlaying, setIsPlaying] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> [isPaused, setIsPaused] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> [disabled, setDisabled] = <span class="hljs-title function_">useState</span>(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> [hasToken, setHasToken] = useState&lt;<span class="hljs-built_in">boolean</span>&gt;(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> [status, setStatus] = useState&lt;<span class="hljs-built_in">string</span>&gt;(<span class="hljs-string">'未开始'</span>);

  <span class="hljs-comment">// 检查令牌</span>
  <span class="hljs-title function_">useEffect</span>(<span class="hljs-function">() =&gt;</span> {
    <span class="hljs-keyword">const</span> <span class="hljs-title function_">checkRequirements</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) =&gt; {
      <span class="hljs-comment">// 检查是否配置了PAT令牌</span>
      <span class="hljs-keyword">const</span> hasConfiguredToken = !!<span class="hljs-variable constant_">ACCESS_TOKEN</span>;
      <span class="hljs-title function_">setHasToken</span>(hasConfiguredToken);
    };

    <span class="hljs-title function_">checkRequirements</span>();
  }, []);

  <span class="hljs-comment">// 初始化客户端</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">initClient</span> = (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">if</span> (!<span class="hljs-variable constant_">ACCESS_TOKEN</span>) {
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Error</span>(<span class="hljs-string">'请先配置个人访问令牌'</span>);
    }

    <span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> <span class="hljs-title class_">WsSpeechClient</span>({
      <span class="hljs-attr">token</span>: <span class="hljs-variable constant_">ACCESS_TOKEN</span>,
      <span class="hljs-attr">allowPersonalAccessTokenInBrowser</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">debug</span>: <span class="hljs-literal">false</span>,
    });

    <span class="hljs-comment">// 语音合成完成事件（含中断）</span>
    client.<span class="hljs-title function_">on</span>(<span class="hljs-string">'completed'</span>, <span class="hljs-function">() =&gt;</span> {
      <span class="hljs-title function_">setIsPlaying</span>(<span class="hljs-literal">false</span>);
      <span class="hljs-title function_">setIsPaused</span>(<span class="hljs-literal">false</span>);
      <span class="hljs-title function_">setStatus</span>(<span class="hljs-string">'已完成'</span>);
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'语音合成完成'</span>);
    });

    <span class="hljs-comment">// 注册所有事件</span>
    client.<span class="hljs-title function_">on</span>(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =&gt;</span> {
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'收到事件'</span>, event);
    });

    clientRef.<span class="hljs-property">current</span> = client;
  };

  <span class="hljs-comment">// 整句播放</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handleAppendAndComplete</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">try</span> {
      <span class="hljs-title function_">setDisabled</span>(<span class="hljs-literal">true</span>); <span class="hljs-comment">// 操作过程中禁用按钮，防止重复点击</span>

      <span class="hljs-keyword">if</span> (!clientRef.<span class="hljs-property">current</span>) {
        <span class="hljs-title function_">initClient</span>();
      }

      <span class="hljs-keyword">await</span> clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">connect</span>({
        <span class="hljs-attr">voiceId</span>: <span class="hljs-variable constant_">VOICE_ID</span>, <span class="hljs-comment">// 可以从配置中获取音色ID</span>
      });

      <span class="hljs-title function_">setIsPlaying</span>(<span class="hljs-literal">true</span>);
      <span class="hljs-title function_">setIsPaused</span>(<span class="hljs-literal">false</span>);
      <span class="hljs-title function_">setStatus</span>(<span class="hljs-string">'播放中'</span>);

      <span class="hljs-comment">// 开始语音合成</span>
      clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">appendAndComplete</span>(transcriptionText);
    } <span class="hljs-keyword">catch</span> (error) {
      message.<span class="hljs-title function_">error</span>(<span class="hljs-string">`操作失败：<span class="hljs-subst">${error}</span>`</span>);
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">error</span>(error);
      <span class="hljs-title function_">setStatus</span>(<span class="hljs-string">'发生错误'</span>);
    } <span class="hljs-keyword">finally</span> {
      <span class="hljs-title function_">setDisabled</span>(<span class="hljs-literal">false</span>);
    }
  };

  <span class="hljs-comment">// 流式播放</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handleAppend</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">try</span> {
      <span class="hljs-title function_">setDisabled</span>(<span class="hljs-literal">true</span>);

      <span class="hljs-keyword">if</span> (!clientRef.<span class="hljs-property">current</span>) {
        <span class="hljs-title function_">initClient</span>();
      }

      <span class="hljs-keyword">await</span> clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">connect</span>({
        <span class="hljs-attr">voiceId</span>: <span class="hljs-variable constant_">VOICE_ID</span>,
      });

      <span class="hljs-title function_">setIsPlaying</span>(<span class="hljs-literal">true</span>);
      <span class="hljs-title function_">setIsPaused</span>(<span class="hljs-literal">false</span>);
      <span class="hljs-title function_">setStatus</span>(<span class="hljs-string">'流式播放中'</span>);

      <span class="hljs-comment">// 逐字符发送文本</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i &lt; transcriptionText.<span class="hljs-property">length</span>; i++) {
        clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">append</span>(transcriptionText[i]);
        <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =&gt;</span> <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">100</span>));
      }

      <span class="hljs-comment">// 完成文本输入</span>
      clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">complete</span>();
    } <span class="hljs-keyword">catch</span> (error) {
      message.<span class="hljs-title function_">error</span>(<span class="hljs-string">`操作失败：<span class="hljs-subst">${error}</span>`</span>);
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">error</span>(error);
      <span class="hljs-title function_">setStatus</span>(<span class="hljs-string">'发生错误'</span>);
    } <span class="hljs-keyword">finally</span> {
      <span class="hljs-title function_">setDisabled</span>(<span class="hljs-literal">false</span>);
    }
  };

  <span class="hljs-comment">// 中断播放</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handleInterrupt</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">try</span> {
      <span class="hljs-keyword">await</span> clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">interrupt</span>();
      <span class="hljs-title function_">setIsPlaying</span>(<span class="hljs-literal">false</span>);
      <span class="hljs-title function_">setIsPaused</span>(<span class="hljs-literal">false</span>);
      <span class="hljs-title function_">setStatus</span>(<span class="hljs-string">'已中断'</span>);
    } <span class="hljs-keyword">catch</span> (error) {
      message.<span class="hljs-title function_">error</span>(<span class="hljs-string">`中断失败：<span class="hljs-subst">${error}</span>`</span>);
    }
  };

  <span class="hljs-comment">// 暂停播放</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handlePause</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">try</span> {
      <span class="hljs-keyword">await</span> clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">pause</span>();
      <span class="hljs-title function_">setIsPaused</span>(<span class="hljs-literal">true</span>);
      <span class="hljs-title function_">setStatus</span>(<span class="hljs-string">'已暂停'</span>);
    } <span class="hljs-keyword">catch</span> (error) {
      message.<span class="hljs-title function_">error</span>(<span class="hljs-string">`暂停失败：<span class="hljs-subst">${error}</span>`</span>);
    }
  };

  <span class="hljs-comment">// 恢复播放</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handleResume</span> = <span class="hljs-keyword">async</span> (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-keyword">try</span> {
      <span class="hljs-keyword">await</span> clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">resume</span>();
      <span class="hljs-title function_">setIsPaused</span>(<span class="hljs-literal">false</span>);
      <span class="hljs-title function_">setStatus</span>(<span class="hljs-string">'播放中'</span>);
    } <span class="hljs-keyword">catch</span> (error) {
      message.<span class="hljs-title function_">error</span>(<span class="hljs-string">`恢复失败：<span class="hljs-subst">${error}</span>`</span>);
    }
  };

  <span class="hljs-comment">// 设置变更处理</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handleSettingsChange</span> = (<span class="hljs-params"></span>) =&gt; {
    <span class="hljs-variable language_">window</span>.<span class="hljs-property">location</span>.<span class="hljs-title function_">reload</span>();
  };

  <span class="hljs-comment">// 组件卸载时清理资源</span>
  <span class="hljs-title function_">useEffect</span>(<span class="hljs-function">() =&gt;</span> {
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =&gt;</span> {
      clientRef.<span class="hljs-property">current</span>?.<span class="hljs-title function_">disconnect</span>();
    };
  }, []);

  <span class="hljs-keyword">return</span> (
    <span class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">Layout</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">height:</span> '<span class="hljs-attr">100</span>%' }}&gt;</span>
      <span class="hljs-tag">&lt;<span class="hljs-name">Layout.Content</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">background:</span> '#<span class="hljs-attr">fff</span>', <span class="hljs-attr">padding:</span> '<span class="hljs-attr">20px</span>' }}&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">Title</span> <span class="hljs-attr">level</span>=<span class="hljs-string">{2}</span>&gt;</span>语音合成 (TTS) 演示<span class="hljs-tag">&lt;/<span class="hljs-name">Title</span>&gt;</span>

        {/* 前置条件检查 */}
        <span class="hljs-tag">&lt;<span class="hljs-name">Card</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"前置条件检查"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">marginBottom:</span> '<span class="hljs-attr">20px</span>' }}&gt;</span>
          <span class="hljs-tag">&lt;<span class="hljs-name">Row</span> <span class="hljs-attr">gutter</span>=<span class="hljs-string">{[0,</span> <span class="hljs-attr">16</span>]}&gt;</span>
            <span class="hljs-tag">&lt;<span class="hljs-name">Col</span> <span class="hljs-attr">span</span>=<span class="hljs-string">{24}</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">Space</span>&gt;</span>
                <span class="hljs-tag">&lt;<span class="hljs-name">Text</span> <span class="hljs-attr">strong</span>&gt;</span>个人访问令牌 (PAT)：<span class="hljs-tag">&lt;/<span class="hljs-name">Text</span>&gt;</span>
                {hasToken ? (
                  <span class="hljs-tag">&lt;<span class="hljs-name">Text</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span>&gt;</span>已配置<span class="hljs-tag">&lt;/<span class="hljs-name">Text</span>&gt;</span>
                ) : (
                  <span class="hljs-tag">&lt;<span class="hljs-name">Text</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span>&gt;</span>未配置 - 请在右上角 Settings 中设置<span class="hljs-tag">&lt;/<span class="hljs-name">Text</span>&gt;</span>
                )}
              <span class="hljs-tag">&lt;/<span class="hljs-name">Space</span>&gt;</span>
            <span class="hljs-tag">&lt;/<span class="hljs-name">Col</span>&gt;</span>
            <span class="hljs-tag">&lt;<span class="hljs-name">Col</span> <span class="hljs-attr">span</span>=<span class="hljs-string">{24}</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">Space</span>&gt;</span>
                <span class="hljs-tag">&lt;<span class="hljs-name">Text</span> <span class="hljs-attr">strong</span>&gt;</span>音色配置：<span class="hljs-tag">&lt;/<span class="hljs-name">Text</span>&gt;</span>
                {VOICE_ID ? (
                  <span class="hljs-tag">&lt;<span class="hljs-name">Text</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span>&gt;</span>已配置 (ID: {VOICE_ID})<span class="hljs-tag">&lt;/<span class="hljs-name">Text</span>&gt;</span>
                ) : (
                  <span class="hljs-tag">&lt;<span class="hljs-name">Text</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"warning"</span>&gt;</span>未配置 - 将使用默认音色<span class="hljs-tag">&lt;/<span class="hljs-name">Text</span>&gt;</span>
                )}
              <span class="hljs-tag">&lt;/<span class="hljs-name">Space</span>&gt;</span>
            <span class="hljs-tag">&lt;/<span class="hljs-name">Col</span>&gt;</span>
          <span class="hljs-tag">&lt;/<span class="hljs-name">Row</span>&gt;</span>
        <span class="hljs-tag">&lt;/<span class="hljs-name">Card</span>&gt;</span>

        {/* 文本输入 */}
        <span class="hljs-tag">&lt;<span class="hljs-name">Card</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"文本输入"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">marginBottom:</span> '<span class="hljs-attr">20px</span>' }}&gt;</span>
          <span class="hljs-tag">&lt;<span class="hljs-name">TextArea</span>
            <span class="hljs-attr">rows</span>=<span class="hljs-string">{4}</span>
            <span class="hljs-attr">value</span>=<span class="hljs-string">{transcriptionText}</span>
            <span class="hljs-attr">onChange</span>=<span class="hljs-string">{e</span> =&gt;</span> setTranscriptionText(e.target.value)}
            placeholder="请输入要转换为语音的文本"
            style={{ marginBottom: '16px' }}
          /&gt;
        <span class="hljs-tag">&lt;/<span class="hljs-name">Card</span>&gt;</span>

        {/* 播放控制 */}
        <span class="hljs-tag">&lt;<span class="hljs-name">Card</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"播放控制"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">marginBottom:</span> '<span class="hljs-attr">20px</span>' }}&gt;</span>
          <span class="hljs-tag">&lt;<span class="hljs-name">Row</span> <span class="hljs-attr">justify</span>=<span class="hljs-string">"start"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">marginBottom:</span> '<span class="hljs-attr">16px</span>' }}&gt;</span>
            <span class="hljs-tag">&lt;<span class="hljs-name">Col</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">Text</span>&gt;</span>
                当前状态: <span class="hljs-tag">&lt;<span class="hljs-name">Text</span> <span class="hljs-attr">strong</span>&gt;</span>{status}<span class="hljs-tag">&lt;/<span class="hljs-name">Text</span>&gt;</span>
              <span class="hljs-tag">&lt;/<span class="hljs-name">Text</span>&gt;</span>
            <span class="hljs-tag">&lt;/<span class="hljs-name">Col</span>&gt;</span>
          <span class="hljs-tag">&lt;/<span class="hljs-name">Row</span>&gt;</span>
          <span class="hljs-tag">&lt;<span class="hljs-name">Row</span> <span class="hljs-attr">gutter</span>=<span class="hljs-string">{16}</span>&gt;</span>
            <span class="hljs-tag">&lt;<span class="hljs-name">Col</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">Button</span>
                <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>
                <span class="hljs-attr">icon</span>=<span class="hljs-string">{</span>&lt;<span class="hljs-attr">SoundOutlined</span> /&gt;</span>}
                disabled={disabled || !hasToken || (isPlaying &amp;&amp; !isPaused)}
                onClick={handleAppendAndComplete}
                size="large"
              &gt;
                整句播放
              <span class="hljs-tag">&lt;/<span class="hljs-name">Button</span>&gt;</span>
            <span class="hljs-tag">&lt;/<span class="hljs-name">Col</span>&gt;</span>
            <span class="hljs-tag">&lt;<span class="hljs-name">Col</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">Button</span>
                <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>
                <span class="hljs-attr">icon</span>=<span class="hljs-string">{</span>&lt;<span class="hljs-attr">SoundOutlined</span> /&gt;</span>}
                disabled={disabled || !hasToken || (isPlaying &amp;&amp; !isPaused)}
                onClick={handleAppend}
                size="large"
              &gt;
                流式播放
              <span class="hljs-tag">&lt;/<span class="hljs-name">Button</span>&gt;</span>
            <span class="hljs-tag">&lt;/<span class="hljs-name">Col</span>&gt;</span>
            {isPlaying &amp;&amp; (
              <span class="hljs-tag">&lt;&gt;</span>
                <span class="hljs-tag">&lt;<span class="hljs-name">Col</span>&gt;</span>
                  <span class="hljs-tag">&lt;<span class="hljs-name">Button</span>
                    <span class="hljs-attr">icon</span>=<span class="hljs-string">{</span>&lt;<span class="hljs-attr">StopOutlined</span> /&gt;</span>}
                    onClick={handleInterrupt}
                    size="large"
                    disabled={!isPlaying}
                  &gt;
                    中断
                  <span class="hljs-tag">&lt;/<span class="hljs-name">Button</span>&gt;</span>
                <span class="hljs-tag">&lt;/<span class="hljs-name">Col</span>&gt;</span>
                <span class="hljs-tag">&lt;<span class="hljs-name">Col</span>&gt;</span>
                  <span class="hljs-tag">&lt;<span class="hljs-name">Button</span>
                    <span class="hljs-attr">icon</span>=<span class="hljs-string">{isPaused</span> ? &lt;<span class="hljs-attr">PlayCircleOutlined</span> /&gt;</span> : <span class="hljs-tag">&lt;<span class="hljs-name">PauseOutlined</span> /&gt;</span>}
                    onClick={isPaused ? handleResume : handlePause}
                    size="large"
                    disabled={!isPlaying}
                  &gt;
                    {isPaused ? '恢复' : '暂停'}
                  <span class="hljs-tag">&lt;/<span class="hljs-name">Button</span>&gt;</span>
                <span class="hljs-tag">&lt;/<span class="hljs-name">Col</span>&gt;</span>
              <span class="hljs-tag">&lt;/&gt;</span>
            )}
          <span class="hljs-tag">&lt;/<span class="hljs-name">Row</span>&gt;</span>
        <span class="hljs-tag">&lt;/<span class="hljs-name">Card</span>&gt;</span>

        {/* 使用说明 */}
        <span class="hljs-tag">&lt;<span class="hljs-name">Card</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"使用说明"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">{{</span> <span class="hljs-attr">marginTop:</span> '<span class="hljs-attr">20px</span>' }}&gt;</span>
          <span class="hljs-tag">&lt;<span class="hljs-name">Paragraph</span>&gt;</span>
            <span class="hljs-tag">&lt;<span class="hljs-name">ol</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">li</span>&gt;</span>在代码中配置个人访问令牌 (PAT)<span class="hljs-tag">&lt;/<span class="hljs-name">li</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">li</span>&gt;</span>可选：在代码中配置音色 ID<span class="hljs-tag">&lt;/<span class="hljs-name">li</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">li</span>&gt;</span>在"文本输入"区域输入要转换为语音的文本<span class="hljs-tag">&lt;/<span class="hljs-name">li</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">li</span>&gt;</span>
                选择播放方式：
                <span class="hljs-tag">&lt;<span class="hljs-name">ul</span>&gt;</span>
                  <span class="hljs-tag">&lt;<span class="hljs-name">li</span>&gt;</span>
                    <span class="hljs-tag">&lt;<span class="hljs-name">strong</span>&gt;</span>整句播放<span class="hljs-tag">&lt;/<span class="hljs-name">strong</span>&gt;</span>：一次性将全部文本转换为语音
                  <span class="hljs-tag">&lt;/<span class="hljs-name">li</span>&gt;</span>
                  <span class="hljs-tag">&lt;<span class="hljs-name">li</span>&gt;</span>
                    <span class="hljs-tag">&lt;<span class="hljs-name">strong</span>&gt;</span>流式播放<span class="hljs-tag">&lt;/<span class="hljs-name">strong</span>&gt;</span>：逐字符转换，模拟实时生成效果
                  <span class="hljs-tag">&lt;/<span class="hljs-name">li</span>&gt;</span>
                <span class="hljs-tag">&lt;/<span class="hljs-name">ul</span>&gt;</span>
              <span class="hljs-tag">&lt;/<span class="hljs-name">li</span>&gt;</span>
              <span class="hljs-tag">&lt;<span class="hljs-name">li</span>&gt;</span>播放过程中可以使用"暂停"、"恢复"和"中断"按钮控制播放<span class="hljs-tag">&lt;/<span class="hljs-name">li</span>&gt;</span>
            <span class="hljs-tag">&lt;/<span class="hljs-name">ol</span>&gt;</span>
          <span class="hljs-tag">&lt;/<span class="hljs-name">Paragraph</span>&gt;</span>
        <span class="hljs-tag">&lt;/<span class="hljs-name">Card</span>&gt;</span>
      <span class="hljs-tag">&lt;/<span class="hljs-name">Layout.Content</span>&gt;</span></span>
    &lt;/<span class="hljs-title class_">Layout</span>&gt;
  );
};

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">SpeechDemo</span>;
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import React, { useEffect, useRef, useState } from 'react';
import {
  Button,
  Layout,
  Space,
  Typography,
  message,
  Row,
  Col,
  Card,
  Input,
} from 'antd';
import { WsSpeechClient } from '@coze/api/ws-tools';
import {
  SoundOutlined,
  PauseOutlined,
  PlayCircleOutlined,
  StopOutlined,
} from '@ant-design/icons';

const { Title, Paragraph, Text } = Typography;
const { TextArea } = Input;

// 个人访问令牌
const ACCESS_TOKEN ='pat_Qm47PKJR5dvMOP53v6DyzwCbTtvEZHQc2TVINEveg9v1T3iSYlTdScJ8***';
// 音色ID
const VOICE_ID = ''; // 可选

const SpeechDemo: React.FC = () =&gt; {
  const clientRef = useRef&lt;WsSpeechClient&gt;();
  const [transcriptionText, setTranscriptionText] =
    useState('你好，这是一个文本转语音测试。');
  const [isPlaying, setIsPlaying] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [disabled, setDisabled] = useState(false);
  const [hasToken, setHasToken] = useState&lt;boolean&gt;(false);
  const [status, setStatus] = useState&lt;string&gt;('未开始');

  // 检查令牌
  useEffect(() =&gt; {
    const checkRequirements = async () =&gt; {
      // 检查是否配置了PAT令牌
      const hasConfiguredToken = !!ACCESS_TOKEN;
      setHasToken(hasConfiguredToken);
    };

    checkRequirements();
  }, []);

  // 初始化客户端
  const initClient = () =&gt; {
    if (!ACCESS_TOKEN) {
      throw new Error('请先配置个人访问令牌');
    }

    const client = new WsSpeechClient({
      token: ACCESS_TOKEN,
      allowPersonalAccessTokenInBrowser: true,
      debug: false,
    });

    // 语音合成完成事件（含中断）
    client.on('completed', () =&gt; {
      setIsPlaying(false);
      setIsPaused(false);
      setStatus('已完成');
      console.log('语音合成完成');
    });

    // 注册所有事件
    client.on('data', event =&gt; {
      console.log('收到事件', event);
    });

    clientRef.current = client;
  };

  // 整句播放
  const handleAppendAndComplete = async () =&gt; {
    try {
      setDisabled(true); // 操作过程中禁用按钮，防止重复点击

      if (!clientRef.current) {
        initClient();
      }

      await clientRef.current?.connect({
        voiceId: VOICE_ID, // 可以从配置中获取音色ID
      });

      setIsPlaying(true);
      setIsPaused(false);
      setStatus('播放中');

      // 开始语音合成
      clientRef.current?.appendAndComplete(transcriptionText);
    } catch (error) {
      message.error(`操作失败：${error}`);
      console.error(error);
      setStatus('发生错误');
    } finally {
      setDisabled(false);
    }
  };

  // 流式播放
  const handleAppend = async () =&gt; {
    try {
      setDisabled(true);

      if (!clientRef.current) {
        initClient();
      }

      await clientRef.current?.connect({
        voiceId: VOICE_ID,
      });

      setIsPlaying(true);
      setIsPaused(false);
      setStatus('流式播放中');

      // 逐字符发送文本
      for (let i = 0; i &lt; transcriptionText.length; i++) {
        clientRef.current?.append(transcriptionText[i]);
        await new Promise(resolve =&gt; setTimeout(resolve, 100));
      }

      // 完成文本输入
      clientRef.current?.complete();
    } catch (error) {
      message.error(`操作失败：${error}`);
      console.error(error);
      setStatus('发生错误');
    } finally {
      setDisabled(false);
    }
  };

  // 中断播放
  const handleInterrupt = async () =&gt; {
    try {
      await clientRef.current?.interrupt();
      setIsPlaying(false);
      setIsPaused(false);
      setStatus('已中断');
    } catch (error) {
      message.error(`中断失败：${error}`);
    }
  };

  // 暂停播放
  const handlePause = async () =&gt; {
    try {
      await clientRef.current?.pause();
      setIsPaused(true);
      setStatus('已暂停');
    } catch (error) {
      message.error(`暂停失败：${error}`);
    }
  };

  // 恢复播放
  const handleResume = async () =&gt; {
    try {
      await clientRef.current?.resume();
      setIsPaused(false);
      setStatus('播放中');
    } catch (error) {
      message.error(`恢复失败：${error}`);
    }
  };

  // 设置变更处理
  const handleSettingsChange = () =&gt; {
    window.location.reload();
  };

  // 组件卸载时清理资源
  useEffect(() =&gt; {
    return () =&gt; {
      clientRef.current?.disconnect();
    };
  }, []);

  return (
    &lt;Layout style={{ height: '100%' }}&gt;
      &lt;Layout.Content style={{ background: '#fff', padding: '20px' }}&gt;
        &lt;Title level={2}&gt;语音合成 (TTS) 演示&lt;/Title&gt;

        {/* 前置条件检查 */}
        &lt;Card title=&quot;前置条件检查&quot; style={{ marginBottom: '20px' }}&gt;
          &lt;Row gutter={[0, 16]}&gt;
            &lt;Col span={24}&gt;
              &lt;Space&gt;
                &lt;Text strong&gt;个人访问令牌 (PAT)：&lt;/Text&gt;
                {hasToken ? (
                  &lt;Text type=&quot;success&quot;&gt;已配置&lt;/Text&gt;
                ) : (
                  &lt;Text type=&quot;danger&quot;&gt;未配置 - 请在右上角 Settings 中设置&lt;/Text&gt;
                )}
              &lt;/Space&gt;
            &lt;/Col&gt;
            &lt;Col span={24}&gt;
              &lt;Space&gt;
                &lt;Text strong&gt;音色配置：&lt;/Text&gt;
                {VOICE_ID ? (
                  &lt;Text type=&quot;success&quot;&gt;已配置 (ID: {VOICE_ID})&lt;/Text&gt;
                ) : (
                  &lt;Text type=&quot;warning&quot;&gt;未配置 - 将使用默认音色&lt;/Text&gt;
                )}
              &lt;/Space&gt;
            &lt;/Col&gt;
          &lt;/Row&gt;
        &lt;/Card&gt;

        {/* 文本输入 */}
        &lt;Card title=&quot;文本输入&quot; style={{ marginBottom: '20px' }}&gt;
          &lt;TextArea
            rows={4}
            value={transcriptionText}
            onChange={e =&gt; setTranscriptionText(e.target.value)}
            placeholder=&quot;请输入要转换为语音的文本&quot;
            style={{ marginBottom: '16px' }}
          /&gt;
        &lt;/Card&gt;

        {/* 播放控制 */}
        &lt;Card title=&quot;播放控制&quot; style={{ marginBottom: '20px' }}&gt;
          &lt;Row justify=&quot;start&quot; style={{ marginBottom: '16px' }}&gt;
            &lt;Col&gt;
              &lt;Text&gt;
                当前状态: &lt;Text strong&gt;{status}&lt;/Text&gt;
              &lt;/Text&gt;
            &lt;/Col&gt;
          &lt;/Row&gt;
          &lt;Row gutter={16}&gt;
            &lt;Col&gt;
              &lt;Button
                type=&quot;primary&quot;
                icon={&lt;SoundOutlined /&gt;}
                disabled={disabled || !hasToken || (isPlaying &amp;&amp; !isPaused)}
                onClick={handleAppendAndComplete}
                size=&quot;large&quot;
              &gt;
                整句播放
              &lt;/Button&gt;
            &lt;/Col&gt;
            &lt;Col&gt;
              &lt;Button
                type=&quot;primary&quot;
                icon={&lt;SoundOutlined /&gt;}
                disabled={disabled || !hasToken || (isPlaying &amp;&amp; !isPaused)}
                onClick={handleAppend}
                size=&quot;large&quot;
              &gt;
                流式播放
              &lt;/Button&gt;
            &lt;/Col&gt;
            {isPlaying &amp;&amp; (
              &lt;&gt;
                &lt;Col&gt;
                  &lt;Button
                    icon={&lt;StopOutlined /&gt;}
                    onClick={handleInterrupt}
                    size=&quot;large&quot;
                    disabled={!isPlaying}
                  &gt;
                    中断
                  &lt;/Button&gt;
                &lt;/Col&gt;
                &lt;Col&gt;
                  &lt;Button
                    icon={isPaused ? &lt;PlayCircleOutlined /&gt; : &lt;PauseOutlined /&gt;}
                    onClick={isPaused ? handleResume : handlePause}
                    size=&quot;large&quot;
                    disabled={!isPlaying}
                  &gt;
                    {isPaused ? '恢复' : '暂停'}
                  &lt;/Button&gt;
                &lt;/Col&gt;
              &lt;/&gt;
            )}
          &lt;/Row&gt;
        &lt;/Card&gt;

        {/* 使用说明 */}
        &lt;Card title=&quot;使用说明&quot; style={{ marginTop: '20px' }}&gt;
          &lt;Paragraph&gt;
            &lt;ol&gt;
              &lt;li&gt;在代码中配置个人访问令牌 (PAT)&lt;/li&gt;
              &lt;li&gt;可选：在代码中配置音色 ID&lt;/li&gt;
              &lt;li&gt;在&quot;文本输入&quot;区域输入要转换为语音的文本&lt;/li&gt;
              &lt;li&gt;
                选择播放方式：
                &lt;ul&gt;
                  &lt;li&gt;
                    &lt;strong&gt;整句播放&lt;/strong&gt;：一次性将全部文本转换为语音
                  &lt;/li&gt;
                  &lt;li&gt;
                    &lt;strong&gt;流式播放&lt;/strong&gt;：逐字符转换，模拟实时生成效果
                  &lt;/li&gt;
                &lt;/ul&gt;
              &lt;/li&gt;
              &lt;li&gt;播放过程中可以使用&quot;暂停&quot;、&quot;恢复&quot;和&quot;中断&quot;按钮控制播放&lt;/li&gt;
            &lt;/ol&gt;
          &lt;/Paragraph&gt;
        &lt;/Card&gt;
      &lt;/Layout.Content&gt;
    &lt;/Layout&gt;
  );
};

export default SpeechDemo;" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h2 id="fdc282b0" tabindex="-1">实现流程</h2>
<h3 id="96c8c507" tabindex="-1">步骤一：安装依赖</h3>
<p>运行以下命令安装 WsSpeech SDK  及其依赖项。</p>
<div style="position: relative">
<pre><code class="hljs language-Shell">npm install @coze/api
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="npm install @coze/api" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="a4db45e5" tabindex="-1">步骤二：导入所需模块</h3>
<p>在项目中导入 <code>WsSpeechClient</code> 类。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-keyword">import</span> { <span class="hljs-title class_">WsSpeechClient</span> } <span class="hljs-keyword">from</span> <span class="hljs-string">'@coze/api/ws-tools'</span>;
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="import { WsSpeechClient } from '@coze/api/ws-tools';" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="60e7c22e" tabindex="-1">步骤三：初始化客户端</h3>
<p>创建 WsSpeechClient 实例，并配置 <code>token</code> 等参数以初始化客户端。</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-comment">// 创建 WsSpeechClient 实例</span>
<span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> <span class="hljs-title class_">WsSpeechClient</span>({
  <span class="hljs-attr">token</span>: <span class="hljs-string">'pat_Qm47PKJR5dvMOP53v6DyzwCbTtvEZHQc2TVINEveg9v1T3iSYlTdScJ8***'</span>, <span class="hljs-comment">// 替换为你的个人访问令牌</span>
  <span class="hljs-attr">allowPersonalAccessTokenInBrowser</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 在浏览器环境中必需</span>
  <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 可选，启用调试日志</span>
});
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 创建 WsSpeechClient 实例
const client = new WsSpeechClient({
  token: 'pat_Qm47PKJR5dvMOP53v6DyzwCbTtvEZHQc2TVINEveg9v1T3iSYlTdScJ8***', // 替换为你的个人访问令牌
  allowPersonalAccessTokenInBrowser: true, // 在浏览器环境中必需
  debug: true, // 可选，启用调试日志
});" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<p>参数说明：</p>
<ul data-style="0">
<li><strong>token</strong>：访问密钥，用于身份认证与鉴权。体验或调试场景可以生成短期的个人访问令牌（PAT），以快速完成 WsChat SDK 的整体流程。个人访问令牌的获取方法请参见<a href="/developer_guides/pat" target="_blank">添加个人访问令牌</a>。在线上环境中，应使用服务访问令牌（SAT）或 OAuth 鉴权方案，详细说明请参见<a href="/developer_guides/authentication" target="_blank">鉴权方式概述</a>。<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<p>扣子 SDK 封装了多种鉴权方式，能够有效简化鉴权流程，你可以参考<a href="https://github.com/coze-dev/coze-py/tree/main/examples" target="_blank">鉴权示例代码</a>实现不同方式的 OAuth 认证，以获取和管理访问扣子 API 所需的令牌</p>
</div>
</li>
<li><strong>allowPersonalAccessTokenInBrowser</strong>：在浏览器环境中使用个人访问令牌时，必须设置为 true。</li>
<li><strong>debug</strong>：启用调试日志，便于开发和测试阶段的问题排查。</li>
</ul>
<h3 id="f4003ab9" tabindex="-1">步骤四：监听事件</h3>
<p>在初始化客户端后，通过 <code>client.on</code> 方法注册各种事件监听器。详细的事件说明请参见<a href="/developer_guides/tts_event" target="_blank">双向流式语音合成事件</a>。</p>
<div style="position: relative">
<pre><code class="hljs language-JavaScript"><span class="hljs-comment">// 注册事件监听器</span>
client.<span class="hljs-title function_">on</span>(<span class="hljs-string">'completed'</span>, <span class="hljs-function">() =&gt;</span> {
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'语音合成完成'</span>);
  <span class="hljs-comment">// 处理完成事件（例如，启用按钮，更新 UI）</span>
});

<span class="hljs-comment">// 可选：记录所有事件用于调试</span>
client.<span class="hljs-title function_">on</span>(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =&gt;</span> {
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'收到事件:'</span>, event);
});
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 注册事件监听器
client.on('completed', () =&gt; {
  console.log('语音合成完成');
  // 处理完成事件（例如，启用按钮，更新 UI）
});

// 可选：记录所有事件用于调试
client.on('data', (event) =&gt; {
  console.log('收到事件:', event);
});" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="7597c6fa" tabindex="-1">步骤五：建立连接</h3>
<p>调用 <code>client.connect</code> 方法建立客户端和服务端之间的连接，并配置音色。<br/>
扣子提供一系列系统音色，你可以在<a href="/dev_how_to_guides/sys_voice" target="_blank">系统音色列表</a>查看音色 ID，或通过<a href="/developer_guides/list_voices" target="_blank">查看音色列表</a> API 获取可用的音色列表。如果不指定 <code>voiceId</code> 或值为空，将使用默认的<code>柔美女友</code>音色，音色 ID 为 7426720361733046281。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-comment">// 可以选择指定音色 ID</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">connect</span>({ <span class="hljs-attr">voiceId</span>: <span class="hljs-string">'7426720361733046281'</span> });
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 可以选择指定音色 ID
await client.connect({ voiceId: '7426720361733046281' });" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h3 id="547a6b38" tabindex="-1">步骤六：将文本转换为语音</h3>
<p>WsSpeech SDK 提供了两种语音的播放模式：</p>
<ul data-style="0">
<li><strong>整句播放</strong>：一次性播放整段文本，适用于短文本播放、固定内容播放以及无需实时交互的场景。</li>
<li><strong>流式播放</strong>：逐字符实时播放文本，提供更自然的播放体验，适用于实时对话系统、打字机效果以及需要控制播放节奏的场景。</li>
</ul>
<p>两种模式的示例代码如下：</p>
<ul data-style="0">
<li>
<p>整句播放</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-comment">// 方法 1：一次性播放整段文本</span>
client.<span class="hljs-title function_">appendAndComplete</span>(<span class="hljs-string">'你好，这是一个文本转语音测试。'</span>);
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 方法 1：一次性播放整段文本
client.appendAndComplete('你好，这是一个文本转语音测试。');" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
<li>
<p>流式播放（逐字符）</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-comment">// 方法 2：逐字符流式播放文本</span>
<span class="hljs-keyword">const</span> text = <span class="hljs-string">'你好，这是一个流式文本转语音测试。'</span>;

<span class="hljs-comment">// 首先建立连接</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">connect</span>();

<span class="hljs-comment">// 逐字符发送文本</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i &lt; text.<span class="hljs-property">length</span>; i++) {
  client.<span class="hljs-title function_">append</span>(text[i]);
  <span class="hljs-comment">// 字符之间添加延迟（可选）</span>
  <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =&gt;</span> <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">100</span>));
}

<span class="hljs-comment">// 通知文本输入完成</span>
client.<span class="hljs-title function_">complete</span>();
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 方法 2：逐字符流式播放文本
const text = '你好，这是一个流式文本转语音测试。';

// 首先建立连接
await client.connect();

// 逐字符发送文本
for (let i = 0; i &lt; text.length; i++) {
  client.append(text[i]);
  // 字符之间添加延迟（可选）
  await new Promise(resolve =&gt; setTimeout(resolve, 100));
}

// 通知文本输入完成
client.complete();" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
</li>
</ul>
<h3 id="87765c16" tabindex="-1">步骤七：控制播放</h3>
<p>在播放过程中，你可以中断播放、暂停播放、恢复播放。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-comment">// 立即中断播放</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">interrupt</span>();

<span class="hljs-comment">// 暂停播放</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">pause</span>();

<span class="hljs-comment">// 恢复播放</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">resume</span>();

<span class="hljs-comment">// 切换播放/暂停</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">togglePlay</span>();

<span class="hljs-comment">// 检查是否正在播放</span>
<span class="hljs-keyword">const</span> isPlaying = client.<span class="hljs-title function_">isPlaying</span>();
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 立即中断播放
await client.interrupt();

// 暂停播放
await client.pause();

// 恢复播放
await client.resume();

// 切换播放/暂停
await client.togglePlay();

// 检查是否正在播放
const isPlaying = client.isPlaying();" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<div class="topic-callout tip"><p class="topic-callout-title">说明</p>
<ul data-style="0">
<li>在执行播放控制操作时，建议添加错误处理逻辑，以确保在操作失败时能够及时处理异常情况。</li>
<li>可以通过 <code>isPlaying</code> 状态更新用户界面，为用户提供更直观的反馈。</li>
</ul>
</div>
<h3 id="5d8936ed" tabindex="-1">步骤八：断开连接</h3>
<p>在组件卸载或不再需要语音合成功能时，调用 <code>disconnect</code> 方法断开连接，清理资源，以避免潜在的内存泄漏或其他资源占用问题。</p>
<div style="position: relative">
<pre><code class="hljs language-TypeScript"><span class="hljs-comment">// 完成后断开连接以清理资源</span>
<span class="hljs-keyword">await</span> client.<span class="hljs-title function_">disconnect</span>();
</code></pre>
<button class="markdown-it-code-copy topic-code-block__copy markdown-it-code-copy--custom" data-clipboard-text="// 完成后断开连接以清理资源
await client.disconnect();" style="position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none;" title="Copy">
<span class="topic-code-block__copy-icon" style="font-size: 21px; opacity: 0.4;"><svg aria-hidden="true" focusable="false" viewbox="0 0 16 16"><path d="M5.5 2A1.5 1.5 0 0 0 4 3.5v7A1.5 1.5 0 0 0 5.5 12h5A1.5 1.5 0 0 0 12 10.5v-7A1.5 1.5 0 0 0 10.5 2zM5 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5z"></path><path d="M2.5 5A1.5 1.5 0 0 0 1 6.5v6A1.5 1.5 0 0 0 2.5 14h5a1.5 1.5 0 0 0 1.5-1.5V12h-1v.5a.5.5 0 0 1-.5.5h-5a.5.5 0 0 1-.5-.5v-6a.5.5 0 0 1 .5-.5H3V5z"></path></svg></span>
</button>
</div>
<h2 id="265c3a6c" tabindex="-1"></h2>
</div><div class="container-ApkkZZ" data-topic-doc-footer="true"><div class="feedback-yTsEsj"><div class="feedbackTitle-UYegOR">文档对您有帮助吗?</div><div class="feedbackActions-hzIGU9"><button class="feedbackButton-GuivRC" type="button"><span class="feedbackButtonIcon-PqHraK"></span><span>有帮助</span></button><button class="feedbackButton-GuivRC" type="button"><span class="feedbackButtonIcon-PqHraK feedbackButtonIconDislike-FBH16L"></span><span>无帮助</span></button></div></div><div class="divider-sbHpm5"></div><div class="neighborList-cu6NCC"><a class="card-T4zaCm" data-discover="true" href="/dev_how_to_guides_install_wschat_sdk"><div class="cardLabel-sDu1uC"><svg aria-hidden="true" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-left" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="M20.272 11.27 7.544 23.998l12.728 12.728M43 24H8.705"></path></svg><span>上一篇</span></div><div class="cardTitle-yINH12">集成 WebSocket 实时语音 Web SDK</div></a><a class="card-T4zaCm nextCard-lFoioT" data-discover="true" href="/dev_how_to_guides_install_wstranscription_sdk"><div class="cardLabel-sDu1uC nextCardLabel-Qi4XVq"><span>下一篇</span><svg aria-hidden="true" class="cardIcon-mIgMBZ arco-icon arco-icon-arrow-right" fill="none" focusable="false" stroke="currentColor" stroke-width="4" viewbox="0 0 48 48"><path d="m27.728 11.27 12.728 12.728-12.728 12.728M5 24h34.295"></path></svg></div><div class="cardTitle-yINH12 nextCardTitle-cRAZDs">集成语音识别 SDK</div></a></div></div></div><div class="container-PtuqqI" data-topic-anchor="true"><div class="arco-anchor"><div class="arco-anchor-list"><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#b74c4354" href="#b74c4354" title="体验 Demo">体验 Demo</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#3c7a17e1" href="#3c7a17e1" title="Demo 功能简介">Demo 功能简介</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#4c4ffca4" href="#4c4ffca4" title="使用 Demo">使用 Demo</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#dfac9b31" href="#dfac9b31" title="完整示例代码">完整示例代码</a></div><div class="arco-anchor-link" style="margin-left:10px"><a class="arco-anchor-link-title" data-href="#fdc282b0" href="#fdc282b0" title="实现流程">实现流程</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#96c8c507" href="#96c8c507" title="步骤一：安装依赖">步骤一：安装依赖</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#a4db45e5" href="#a4db45e5" title="步骤二：导入所需模块">步骤二：导入所需模块</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#60e7c22e" href="#60e7c22e" title="步骤三：初始化客户端">步骤三：初始化客户端</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#f4003ab9" href="#f4003ab9" title="步骤四：监听事件">步骤四：监听事件</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#7597c6fa" href="#7597c6fa" title="步骤五：建立连接">步骤五：建立连接</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#547a6b38" href="#547a6b38" title="步骤六：将文本转换为语音">步骤六：将文本转换为语音</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#87765c16" href="#87765c16" title="步骤七：控制播放">步骤七：控制播放</a></div><div class="arco-anchor-link" style="margin-left:20px"><a class="arco-anchor-link-title" data-href="#5d8936ed" href="#5d8936ed" title="步骤八：断开连接">步骤八：断开连接</a></div></div></div></div></div></div></div></div>
</body></html>