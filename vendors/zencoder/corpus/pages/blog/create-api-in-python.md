<!doctype html><html lang="en-us" class="antialiased leading-tight motion-safe:scroll-smooth" data-theme="dark"><head>
    <meta charset="utf-8">
    <script>!function(){var k="zencoder_theme",C={dark:"#0a0a0a",light:"#fafafa"},d=document.documentElement,m=matchMedia("(prefers-color-scheme:dark)"),s=function(){try{return localStorage.getItem(k)||"dark"}catch(e){return"dark"}},r=function(v){return v==="system"?m.matches?"dark":"light":v},t=function(v){var e=document.querySelector('meta[name="theme-color"]');if(!e){e=document.createElement("meta");e.setAttribute("name","theme-color");document.head.appendChild(e)}e.setAttribute("content",C[v]||C.dark)},a=function(v){var r2=r(v);d.setAttribute("data-theme",r2);t(r2)};a(s());m.addEventListener("change",function(){s()==="system"&&a("system")});window.themeSwitcher=function(){return{mode:s(),set:function(v){this.mode=v;try{localStorage.setItem(k,v)}catch(e){}a(v)}}}}()</script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#0a0a0a">

    
      
      
      
        
        
        
        
        
        
      
      <link rel="preload" as="image" imagesrcset="https://zencoder.ai/hs-fs/hubfs/api%20with%20python.jpg?width=768&amp;name=api%20with%20python.jpg 768w,
                         https://zencoder.ai/hs-fs/hubfs/api%20with%20python.jpg?width=1280&amp;name=api%20with%20python.jpg 1280w,
                         https://zencoder.ai/hs-fs/hubfs/api%20with%20python.jpg?width=1600&amp;name=api%20with%20python.jpg 1600w,
                         https://zencoder.ai/hs-fs/hubfs/api%20with%20python.jpg?width=2048&amp;name=api%20with%20python.jpg 2048w" imagesizes="(min-width: 1024px) 1024px, 100vw" fetchpriority="high">
    

    

<link rel="preload" as="font" type="font/woff2" href="//zencoder.ai/hubfs/raw_assets/public/forgood-tailwind-theme/css/fonts/inter-latin-wght-normal.woff2" crossorigin>

<style>
  @font-face {
    font-family: 'Inter';
    font-style: normal;
    font-display: swap;
    font-weight: 400 700;
    src: url('//zencoder.ai/hubfs/raw_assets/public/forgood-tailwind-theme/css/fonts/inter-latin-wght-normal.woff2') format('woff2');
  }
</style>

    <style>
      body{transition:background-color .3s ease,color .3s ease}
      @media (prefers-reduced-motion: reduce){body{transition:none}}
    </style>

    
      <title>How to Create an API in Python</title>
    

    
      <link rel="shortcut icon" href="//zencoder.ai/hubfs/export.png">
    

    
      <meta name="description" content="Discover how to build and deploy a robust API in Python, using frameworks like Flask and FastAPI to manage requests efficiently.">
    

    

    

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="http://zencoder.ai/blog/create-api-in-python">
    <meta property="og:title" content="How to Create an API in Python">
    <meta property="og:description" content="Discover how to build and deploy a robust API in Python, using frameworks like Flask and FastAPI to manage requests efficiently.">
    
      <meta property="og:image" content="//zencoder.ai/hubfs/api%20with%20python.jpg">
    
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="http://zencoder.ai/blog/create-api-in-python">
    <meta property="twitter:title" content="How to Create an API in Python">
    <meta property="twitter:description" content="Discover how to build and deploy a robust API in Python, using frameworks like Flask and FastAPI to manage requests efficiently.">
    
      <meta property="twitter:image" content="//zencoder.ai/hubfs/api%20with%20python.jpg">
    

    <!-- Schema.org Structured Data -->
    
<!--
  templateType: "none"
  isAvailableForNewContent: false
-->









































  












  





<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [

    
    {
      "@type": "Organization",
      "@id": "https://zencoder.ai/#organization",
      "name": "Zencoder",
      "alternateName": "Zencoder – The AI Coding Agent",
      "url": "https://zencoder.ai",
      "logo": {
        "@type": "ImageObject",
        "url": "https://zencoder.ai/hubfs/Logo-dark-1.svg"
      },
      "description": "Zencoder is an AI-powered coding agent that helps developers write, debug, and optimize code faster with intelligent code generation and chat assistance.",
      "email": "support@zencoder.ai",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "500 W Hamilton Ave, 112550",
        "addressLocality": "Campbell",
        "addressRegion": "CA",
        "postalCode": "95008",
        "addressCountry": "US"
      },
      "sameAs": [
        "https://www.linkedin.com/company/zencoderai/",
        "https://x.com/zencoderai",
        "https://www.instagram.com/zencoderai/",
        "https://www.youtube.com/@zencoderai",
        "https://github.com/zencoderai"
      ]
    },

    
    {
      "@type": "WebSite",
      "@id": "https://zencoder.ai/#website",
      "url": "https://zencoder.ai",
      "name": "Zencoder – The AI Coding Agent",
      "description": "Zencoder is an AI-powered coding agent that helps developers write, debug, and optimize code faster with intelligent code generation and chat assistance.",
      "publisher": { "@id": "https://zencoder.ai/#organization" },
      "inLanguage": "en-us"
    },

    
    {
      "@type":
        "WebPage",
      "@id": "http://zencoder.ai/blog/create-api-in-python#webpage",
      "url": "http://zencoder.ai/blog/create-api-in-python",
      "name": "How to Create an API in Python",
      "description": "Discover how to build and deploy a robust API in Python, using frameworks like Flask and FastAPI to manage requests efficiently.",
      "inLanguage": "en-us",
      "isPartOf": { "@id": "https://zencoder.ai/#website" }
      
      
    }

    
    
    ,{
      "@type": "BreadcrumbList",
      "@id": "http://zencoder.ai/blog/create-api-in-python#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://zencoder.ai/" }

        
          ,{ "@type": "ListItem", "position": 2, "name": "How to Create an API in Python",
             "item": "http://zencoder.ai/blog/create-api-in-python" }
        
      ]
    }
    

    
    

    
    

    
    

    
    
  ]
}
</script>

    

    

    <meta name="viewport" content="width=device-width, initial-scale=1">

    
    <meta property="og:description" content="Discover how to build and deploy a robust API in Python, using frameworks like Flask and FastAPI to manage requests efficiently.">
    <meta property="og:title" content="How to Create an API in Python">
    <meta name="twitter:description" content="Discover how to build and deploy a robust API in Python, using frameworks like Flask and FastAPI to manage requests efficiently.">
    <meta name="twitter:title" content="How to Create an API in Python">

    

    

    <style>
a.cta_button{-moz-box-sizing:content-box !important;-webkit-box-sizing:content-box !important;box-sizing:content-box !important;vertical-align:middle}.hs-breadcrumb-menu{list-style-type:none;margin:0px 0px 0px 0px;padding:0px 0px 0px 0px}.hs-breadcrumb-menu-item{float:left;padding:10px 0px 10px 10px}.hs-breadcrumb-menu-divider:before{content:'›';padding-left:10px}.hs-featured-image-link{border:0}.hs-featured-image{float:right;margin:0 0 20px 20px;max-width:50%}@media (max-width: 568px){.hs-featured-image{float:none;margin:0;width:100%;max-width:100%}}.hs-screen-reader-text{clip:rect(1px, 1px, 1px, 1px);height:1px;overflow:hidden;position:absolute !important;width:1px}
</style>

<link rel="stylesheet" href="//zencoder.ai/hubfs/hub_generated/template_assets/1/183886388261/1784548489352/template_tailwind-generated.min.css">

    <script type="application/ld+json">
{
  "mainEntityOfPage" : {
    "@type" : "WebPage",
    "@id" : "http://zencoder.ai/blog/create-api-in-python"
  },
  "author" : {
    "name" : "Federico Trotta",
    "url" : "http://zencoder.ai/blog/author/federico-trotta",
    "@type" : "Person"
  },
  "headline" : "How to Create an API in Python",
  "datePublished" : "2025-02-28T13:46:57.000Z",
  "dateModified" : "2026-05-17T13:17:23.372Z",
  "publisher" : {
    "name" : "Zencoder",
    "logo" : {
      "url" : "//zencoder.ai/hubfs/Logo-dark-1.png",
      "@type" : "ImageObject"
    },
    "@type" : "Organization"
  },
  "@context" : "https://schema.org",
  "@type" : "BlogPosting",
  "image" : [ "//zencoder.ai/hubfs/api%20with%20python.jpg" ]
}
</script>



    
<!--  Added by GoogleAnalytics4 integration -->
<script>
var _hsp = window._hsp = window._hsp || [];
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

var useGoogleConsentModeV2 = true;
var waitForUpdateMillis = 1000;


if (!window._hsGoogleConsentRunOnce) {
  window._hsGoogleConsentRunOnce = true;

  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'analytics_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'wait_for_update': waitForUpdateMillis
  });

  if (useGoogleConsentModeV2) {
    _hsp.push(['useGoogleConsentModeV2'])
  } else {
    _hsp.push(['addPrivacyConsentListener', function(consent){
      var hasAnalyticsConsent = consent && (consent.allowed || (consent.categories && consent.categories.analytics));
      var hasAdsConsent = consent && (consent.allowed || (consent.categories && consent.categories.advertisement));

      gtag('consent', 'update', {
        'ad_storage': hasAdsConsent ? 'granted' : 'denied',
        'analytics_storage': hasAnalyticsConsent ? 'granted' : 'denied',
        'ad_user_data': hasAdsConsent ? 'granted' : 'denied',
        'ad_personalization': hasAdsConsent ? 'granted' : 'denied'
      });
    }]);
  }
}

gtag('js', new Date());
gtag('set', 'developer_id.dZTQ1Zm', true);
gtag('config', 'G-MLV8VVHRDL');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MLV8VVHRDL"></script>

<!-- /Added by GoogleAnalytics4 integration -->

<!--  Added by GoogleTagManager integration -->
<script>
var _hsp = window._hsp = window._hsp || [];
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

var useGoogleConsentModeV2 = true;
var waitForUpdateMillis = 1000;

if (useGoogleConsentModeV2) {

  gtag('set','developer_id.dZTQ1Zm',true);

  gtag('consent', 'default', {
  'ad_storage': 'denied',
  'analytics_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'wait_for_update': waitForUpdateMillis
  });
}

var hsLoadGtm = function loadGtm() {
    if(window._hsGtmLoadOnce) {
      return;
    }

    if (useGoogleConsentModeV2) {
      _hsp.push(['useGoogleConsentModeV2'])
    }

    (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-NBR53RSB');

    window._hsGtmLoadOnce = true;
};

_hsp.push(['addPrivacyConsentListener', function(consent){
  if(consent.allowed || (consent.categories && consent.categories.analytics)){
    hsLoadGtm();
  }
}]);

</script>

<!-- /Added by GoogleTagManager integration -->


<script type="module" src="https://assets.sandbox.cello.so/attribution/latest/cello-attribution.js" async></script>
<link rel="amphtml" href="http://zencoder.ai/blog/create-api-in-python?hs_amp=true">

<meta property="og:image" content="//zencoder.ai/hubfs/api%20with%20python.jpg">
<meta property="og:image:width" content="2420">
<meta property="og:image:height" content="1210">

<meta name="twitter:image" content="//zencoder.ai/hubfs/api%20with%20python.jpg">


<meta property="og:url" content="http://zencoder.ai/blog/create-api-in-python">
<meta name="twitter:card" content="summary_large_image">

<link rel="canonical" href="http://zencoder.ai/blog/create-api-in-python">

<meta property="og:type" content="article">
<link rel="alternate" type="application/rss+xml" href="//zencoder.ai/blog/rss.xml">
<meta name="twitter:domain" content="zencoder.ai">
<script src="//platform.linkedin.com/in.js" type="text/javascript">
    lang: en_US
</script>

<meta http-equiv="content-language" content="en-us">






  <meta name="generator" content="HubSpot"></head>
  <body class="min-h-screen bg-background text-foreground pt-16">
<!--  Added by GoogleTagManager integration -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NBR53RSB" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<!-- /Added by GoogleTagManager integration -->

    
      <div data-global-resource-path="forgood-tailwind-theme/templates/partials/header.html"><div id="hs_cos_wrapper_module_17398143398242" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">


<header class="fixed w-full top-0 isolate z-50 bg-background" x-data="globalNav">
  
  <nav aria-label="Main navigation" class="container-page flex items-center justify-between py-4" :inert="mobileOpen">
    
    
    <div class="flex flex-1 relative" x-data="navLogo" @contextmenu="onContext($event)">
      <a href="/" class="-m-1.5 p-1.5">
        <span class="sr-only">Zencoder</span>
        <svg id="zc-brand-source" class="h-7 w-auto" viewbox="0 0 258 49" xmlns="http://www.w3.org/2000/svg">
          <g fill="#e65c2c" data-zc-mark>
            <path d="M20.463 33.724c-.624-2.107-1.68-4.61-3.838-5.532-2.187-.852-4.678.163-6.468 1.453-1.342.986-2.514 2.299-3.133 3.874-.21.537-.356 1.097-.426 1.663-.087.566-.163 1.138-.151 1.715.064 3.74 2.082 7.329 4.853 9.762 1.51 1.289 3.464 2.474 5.54 2.328 3.313-.338 3.949-4.429 4.305-7.084.152-1.097.158-2.205.105-3.308-.087-1.651-.338-3.279-.793-4.872Z" />
            <path d="M39.699 34.587c-.998-.484-2.048-.834-3.115-1.126-1.592-.426-3.225-.694-4.882-.753-2.193-.058-4.899.17-6.445 1.943-1.487 1.815-1.289 4.505-.612 6.606.525 1.581 1.411 3.098 2.718 4.177.443.362.933.677 1.452.922.513.257 1.032.508 1.587.677 3.575 1.097 7.611.286 10.778-1.599 1.686-1.033 3.424-2.532 3.92-4.557.7-3.256-2.986-5.123-5.407-6.284Z" />
            <path d="M49.241 16.616c-.466-1.926-1.347-4.044-3.114-5.141-2.876-1.675-5.792 1.26-7.647 3.198-.77.799-1.429 1.686-2.03 2.613-.898 1.383-1.656 2.854-2.222 4.406-.729 2.071-1.353 4.72-.146 6.728 1.266 1.972 3.879 2.62 6.084 2.626 1.668-.006 3.383-.385 4.812-1.295.484-.309.933-.677 1.324-1.097.402-.409.799-.829 1.131-1.296 2.147-3.063 2.626-7.153 1.808-10.754Z" />
            <path d="M30.88 18.115c2.269-.595 3.686-2.882 4.374-4.977.507-1.587.676-3.337.256-4.977-.146-.554-.356-1.096-.63-1.598-.262-.508-.536-1.016-.886-1.477C31.743 2.098 28.004.383 24.33.044 22.353-.107 20.072.08 18.48 1.421c-2.485 2.223-.595 5.905.676 8.263.525.974 1.167 1.878 1.861 2.736 1.038 1.284 2.199 2.457 3.505 3.478 1.739 1.336 4.066 2.742 6.358 2.217Z" />
            <path d="M11.632 25.59c1.54-.59 3.015-1.331 4.392-2.259 1.808-1.243 3.861-3.023 4.071-5.363.134-2.34-1.598-4.399-3.383-5.7-1.353-.974-2.963-1.675-4.654-1.785-.571-.035-1.149 0-1.709.105-.566.093-1.132.198-1.68.385C5.134 12.187 2.34 15.215.888 18.611c-.758 1.832-1.283 4.067-.501 5.992 1.348 3.046 5.43 2.387 8.061 1.908 1.091-.198 2.147-.531 3.179-.922Z" />
          </g>
          <g fill="currentColor" class="hidden lg:inline" data-zc-word>
            <path d="M65.316 30.03 77.081 20.222v-.391H65.602v-3.18h17.201v2.287L71.038 28.816v.689l11.765-.327v3.18H65.316v-2.328Z" />
            <path d="M106.676 25.455H90.467c.286 2.387 1.814 4.324 6.614 4.324 4.165 0 5.629-1.237 5.88-2.544h3.721c-.187 2.737-2.893 5.432-9.601 5.432-8.3 0-10.715-4.131-10.715-8.04 0-5.024 3.85-8.297 10.458-8.297 6.609 0 9.858 2.987 9.858 7.848v1.278Zm-3.715-2.544c0-2.095-1.686-3.688-5.979-3.688-3.943 0-5.85 1.336-6.387 3.781h12.366Z" />
            <path d="M111.319 16.651h4.071l-.064 4.603h.391c1.178-3.209 3.395-4.924 8.481-4.924 6.422 0 8.679 3.086 8.679 6.932v9.09h-4.071v-8.005c0-2.795-1.429-4.674-6.136-4.674-3.815 0-7.28 1.809-7.28 5.625v7.054h-4.071V16.651Z" />
            <path d="M137.356 24.499c0-4.452 3.465-8.169 10.365-8.169s9.601 2.946 9.601 6.348l-3.722.327c-.035-1.78-1.592-3.495-5.815-3.495s-6.358 2.194-6.358 4.989c0 2.638 1.651 4.989 6.201 4.989s6.007-1.651 6.036-3.431l3.722.327c0 3.273-2.572 6.284-9.916 6.284s-10.114-4.195-10.114-8.169Z" />
            <path d="M161.708 24.534c0-4.131 3.05-8.199 10.779-8.199s10.778 4.068 10.778 8.199-2.986 8.134-10.778 8.134-10.779-3.974-10.779-8.134Zm17.48 0c0-2.609-1.814-5.024-6.707-5.024-4.894 0-6.708 2.415-6.708 5.024 0 2.608 1.779 4.953 6.708 4.953 4.928 0 6.707-2.351 6.707-4.953Z" />
            <path d="M187.588 24.312c0-4.417 3.593-7.977 10.108-7.977 4.421 0 6.509 1.237 7.337 3.402h.362v-7.585h4.071v20.2h-4.071c.064-1.143.128-2.736.157-4.032h-.39c-.764 2.573-2.882 4.353-7.589 4.353-6.357 0-9.98-3.308-9.98-8.361Zm17.801.187v-.478c0-2.48-2.292-4.511-7.122-4.511-4.421 0-6.643 2.065-6.643 4.802 0 3.18 2.444 5.181 6.614 5.181 4.766 0 7.151-2.859 7.151-4.994Z" />
            <path d="M234.506 25.455h-16.209c.286 2.387 1.814 4.324 6.614 4.324 4.165 0 5.629-1.237 5.88-2.544h3.721c-.187 2.737-2.893 5.432-9.601 5.432-8.3 0-10.714-4.131-10.714-8.04 0-5.024 3.849-8.297 10.458-8.297 6.608 0 9.857 2.987 9.857 7.848v1.278Zm-3.721-2.544c0-2.095-1.686-3.688-5.979-3.688-3.943 0-5.85 1.336-6.387 3.781h12.366Z" />
            <path d="M239.149 16.651h4.071l-.064 4.802h.391c.985-2.83 2.881-5.118 7.302-5.118 5.185 0 7.151 2.859 7.151 7.247 0 1.208-.064 2.287-.093 2.795h-3.815c.035-.385.064-1.05.064-1.622 0-3.367-1.114-5.082-4.479-5.082-4.165 0-6.451 3.238-6.451 6.739v5.94h-4.071V16.651Z" />
          </g>
        </svg>
      </a>

      
      <template x-teleport="body">
        <div x-show="ctxOpen" class="fixed inset-0 z-[99]" @click="ctxOpen = false" @contextmenu.prevent="ctxOpen = false" x-cloak></div>
      </template>
      <template x-teleport="body">
        <div x-show="ctxOpen" x-ref="ctxMenu" x-transition:enter="transition ease-out duration-150" x-transition:enter-start="opacity-0 translate-y-2" x-transition:enter-end="opacity-100 translate-y-0" x-transition:leave="transition ease-in duration-100" x-transition:leave-start="opacity-100 translate-y-0" x-transition:leave-end="opacity-0 translate-y-2" :style="`left: ${ctxX}px; top: ${ctxY}px`" class="fixed z-[100] min-w-[12rem] bg-popover ring-1 ring-ring rounded-lg p-2 shadow-2xl" role="menu" aria-label="Brand assets" @click.outside="ctxOpen = false" @keydown.arrow-down.prevent="ctxFocus(ctxFocusIdx + 1)" @keydown.arrow-up.prevent="ctxFocus(ctxFocusIdx - 1)" @keydown.home.prevent="ctxFocus(0)" @keydown.end.prevent="ctxFocus(ctxItems.length - 1)" @keydown.tab="ctxOpen = false" @contextmenu.prevent.stop x-cloak>
          <button role="menuitem" tabindex="-1" @click="copySvg('logo'); ctxOpen = false" class="block w-full p-2 rounded-md text-sm/5 text-left text-secondary-foreground hover:bg-accent hover:text-foreground focus:bg-accent focus:text-foreground focus:outline-none transition-colors">
            <span x-text="copied === 'logo' ? 'Copied!' : copied === 'error' ? 'Copy failed' : 'Copy logo as SVG'"></span>
          </button>
          <button role="menuitem" tabindex="-1" @click="copySvg('wordmark'); ctxOpen = false" class="block w-full p-2 rounded-md text-sm/5 text-left text-secondary-foreground hover:bg-accent hover:text-foreground focus:bg-accent focus:text-foreground focus:outline-none transition-colors">
            <span x-text="copied === 'wordmark' ? 'Copied!' : copied === 'error' ? 'Copy failed' : 'Copy wordmark as SVG'"></span>
          </button>
          <a href="//zencoder.ai/hubfs/Zencoder-Logo-Kit.zip" role="menuitem" tabindex="-1" download class="block w-full p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground focus:bg-accent focus:text-foreground focus:outline-none transition-colors" @click="ctxOpen = false">
            Download brand assets
          </a>
        </div>
      </template>
    </div>

    
    <div class="flex lg:hidden items-center gap-6">
      
      <a href="https://auth.zencoder.ai/signup" class="btn btn-sm btn-default" data-utm-pass="true">
        Get started
      </a>
      
      
      <button x-ref="menuBtn" @click="closedByBtn = mobileOpen; mobileOpen = !mobileOpen; mobileSubmenu = null" type="button" :aria-expanded="mobileOpen.toString()" aria-controls="mobile-menu" class="-m-2 inline-flex items-center justify-center rounded-md p-2 text-neutral-800 dark:text-neutral-300">
        <span class="sr-only" x-text="mobileOpen ? 'Close main menu' : 'Open main menu'"></span>
        <svg x-show="!mobileOpen" class="size-4" viewbox="0 0 12 12" fill="currentColor" aria-hidden="true">
          <path d="m10.75,4H1.25c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h9.5c.414,0,.75.336.75.75s-.336.75-.75.75Z" stroke-width="0"></path>
          <path d="m10.75,9.5H1.25c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h9.5c.414,0,.75.336.75.75s-.336.75-.75.75Z" stroke-width="0"></path>
        </svg>
        <svg x-show="mobileOpen" x-cloak class="size-4" viewbox="0 0 12 12" fill="currentColor" aria-hidden="true">
          <path d="m2.25,10.5c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.22,1.72c.293-.293.768-.293,1.061,0s.293.768,0,1.061l-7.5,7.5c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
          <path d="m9.75,10.5c-.192,0-.384-.073-.53-.22L1.72,2.78c-.293-.293-.293-.768,0-1.061s.768-.293,1.061,0l7.5,7.5c.293.293.293.768,0,1.061-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
        </svg>
      </button>
    </div>

    
    <div class="hidden lg:flex lg:gap-x-1">
      
      <div class="relative" x-data="{ t: null }" @mouseenter="clearTimeout(t); openMenu = 1" @mouseleave="t = setTimeout(() => { if (openMenu === 1) openMenu = null }, 150)" @focusin="clearTimeout(t); openMenu = 1" @focusout="$nextTick(() => { if (!$el.contains(document.activeElement)) openMenu = null })">
        
        
        <button class="btn btn-sm btn-menu" :aria-expanded="(openMenu === 1).toString()" aria-haspopup="true" aria-controls="desktop-dropdown-1" @keydown.escape="openMenu = null">
          Product
        </button>
        

        
        
        
        
        
        
        <div id="desktop-dropdown-1" x-show="openMenu === 1" x-transition:enter="transition ease-out duration-150" x-transition:enter-start="opacity-0 translate-y-2" x-transition:enter-end="opacity-100 translate-y-0" x-transition:leave="transition ease-in duration-100" x-transition:leave-start="opacity-100 translate-y-0" x-transition:leave-end="opacity-0 translate-y-2" x-effect="if (openMenu === 1 &amp;&amp; $el.__lastMenu !== 1) { $el.__lastMenu = 1; $nextTick(() => { const r = $el.getBoundingClientRect(); const pad = 16; if (r.right > window.innerWidth - pad) $el.style.left = (window.innerWidth - pad - r.right + r.left - r.width / 2) + 'px'; else if (r.left < pad) $el.style.left = (pad - r.left + r.width / 2) + 'px'; else $el.style.left = ''; }) } else if (openMenu !== 1) { $el.__lastMenu = null; }" class="absolute left-1/2 -translate-x-1/2 top-full pt-2 z-50" @keydown.escape="openMenu = null; $el.closest('.relative')?.querySelector('button, a')?.focus()" x-cloak>
          
          <div class="bg-popover ring-1 ring-ring rounded-lg p-2 shadow-2xl flex flex-col gap-3">
            
            
            
            <div class="flex gap-3">
              
              
              <div class="min-w-[12rem]">
                
                <ul>
                  
                  <li>
                    <a href="//zencoder.ai/zenflow" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group">
                      Zenflow™ Code
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/zenflow-work" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group">
                      Zenflow™ Work
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/product/coding-agent" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group">
                      IDE Agents
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/marketplace" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group">
                      Marketplace
                      
                    </a>
                  </li>
                  
                </ul>
              </div>
              

              

              
              
            </div>
            

            
            
            
          </div>
        </div>
        
      </div>
      
      <div class="relative" x-data="{ t: null }" @mouseenter="clearTimeout(t); openMenu = 2" @mouseleave="t = setTimeout(() => { if (openMenu === 2) openMenu = null }, 150)" @focusin="clearTimeout(t); openMenu = 2" @focusout="$nextTick(() => { if (!$el.contains(document.activeElement)) openMenu = null })">
        
        
        <a class="btn btn-sm btn-menu" href="//zencoder.ai/pricing">
          Pricing
        </a>
        

        
        
      </div>
      
      <div class="relative" x-data="{ t: null }" @mouseenter="clearTimeout(t); openMenu = 3" @mouseleave="t = setTimeout(() => { if (openMenu === 3) openMenu = null }, 150)" @focusin="clearTimeout(t); openMenu = 3" @focusout="$nextTick(() => { if (!$el.contains(document.activeElement)) openMenu = null })">
        
        
        <button class="btn btn-sm btn-menu" :aria-expanded="(openMenu === 3).toString()" aria-haspopup="true" aria-controls="desktop-dropdown-3" @keydown.escape="openMenu = null">
          Enterprise
        </button>
        

        
        
        
        
        
        
        <div id="desktop-dropdown-3" x-show="openMenu === 3" x-transition:enter="transition ease-out duration-150" x-transition:enter-start="opacity-0 translate-y-2" x-transition:enter-end="opacity-100 translate-y-0" x-transition:leave="transition ease-in duration-100" x-transition:leave-start="opacity-100 translate-y-0" x-transition:leave-end="opacity-0 translate-y-2" x-effect="if (openMenu === 3 &amp;&amp; $el.__lastMenu !== 3) { $el.__lastMenu = 3; $nextTick(() => { const r = $el.getBoundingClientRect(); const pad = 16; if (r.right > window.innerWidth - pad) $el.style.left = (window.innerWidth - pad - r.right + r.left - r.width / 2) + 'px'; else if (r.left < pad) $el.style.left = (pad - r.left + r.width / 2) + 'px'; else $el.style.left = ''; }) } else if (openMenu !== 3) { $el.__lastMenu = null; }" class="absolute left-1/2 -translate-x-1/2 top-full pt-2 z-50" @keydown.escape="openMenu = null; $el.closest('.relative')?.querySelector('button, a')?.focus()" x-cloak>
          
          <div class="bg-popover ring-1 ring-ring rounded-lg p-2 shadow-2xl flex flex-col gap-3">
            
            
            
            <div class="flex gap-3">
              
              
              <div class="min-w-[12rem]">
                
                <ul>
                  
                  <li>
                    <a href="//zencoder.ai/enterprise" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group">
                      Zencoder for Enterprise
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/solutions/engineering-managers" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group">
                      Zenflow for Engineering Managers
                      
                    </a>
                  </li>
                  
                </ul>
              </div>
              

              

              
              
            </div>
            

            
            
            
          </div>
        </div>
        
      </div>
      
      <div class="relative" x-data="{ t: null }" @mouseenter="clearTimeout(t); openMenu = 4" @mouseleave="t = setTimeout(() => { if (openMenu === 4) openMenu = null }, 150)" @focusin="clearTimeout(t); openMenu = 4" @focusout="$nextTick(() => { if (!$el.contains(document.activeElement)) openMenu = null })">
        
        
        <button class="btn btn-sm btn-menu" :aria-expanded="(openMenu === 4).toString()" aria-haspopup="true" aria-controls="desktop-dropdown-4" @keydown.escape="openMenu = null">
          Resources
        </button>
        

        
        
        
        
        
        
        <div id="desktop-dropdown-4" x-show="openMenu === 4" x-transition:enter="transition ease-out duration-150" x-transition:enter-start="opacity-0 translate-y-2" x-transition:enter-end="opacity-100 translate-y-0" x-transition:leave="transition ease-in duration-100" x-transition:leave-start="opacity-100 translate-y-0" x-transition:leave-end="opacity-0 translate-y-2" x-effect="if (openMenu === 4 &amp;&amp; $el.__lastMenu !== 4) { $el.__lastMenu = 4; $nextTick(() => { const r = $el.getBoundingClientRect(); const pad = 16; if (r.right > window.innerWidth - pad) $el.style.left = (window.innerWidth - pad - r.right + r.left - r.width / 2) + 'px'; else if (r.left < pad) $el.style.left = (pad - r.left + r.width / 2) + 'px'; else $el.style.left = ''; }) } else if (openMenu !== 4) { $el.__lastMenu = null; }" class="absolute left-1/2 -translate-x-1/2 top-full pt-2 z-50" @keydown.escape="openMenu = null; $el.closest('.relative')?.querySelector('button, a')?.focus()" x-cloak>
          
          <div class="bg-popover ring-1 ring-ring rounded-lg p-2 shadow-2xl flex flex-col gap-3">
            
            
            
            <div class="flex gap-3">
              
              
              <div class="min-w-[12rem]">
                
                <ul>
                  
                  <li>
                    <a href="https://docs.zencoder.ai/" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group" target="_blank" rel="noopener noreferrer noopener">
                      Docs
                      
<svg class="h-2.5 w-2.5 text-secondary-foreground/90 group-hover:text-secondary-foreground" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" fill="currentColor">
  <path d="m1.75,11c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.543,1.396c.293-.293.768-.293,1.061,0s.293.768,0,1.061L2.28,10.78c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
  <path d="m10.25,7.25c-.414,0-.75-.336-.75-.75V2.5h-4c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h4.75c.414,0,.75.336.75.75v4.75c0,.414-.336.75-.75.75Z" stroke-width="0"></path>
</svg>

                    </a>
                  </li>
                  
                  <li>
                    <a href="https://discord.com/invite/zencoder" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group" target="_blank" rel="noopener noreferrer noopener">
                      Community
                      
<svg class="h-2.5 w-2.5 text-secondary-foreground/90 group-hover:text-secondary-foreground" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" fill="currentColor">
  <path d="m1.75,11c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.543,1.396c.293-.293.768-.293,1.061,0s.293.768,0,1.061L2.28,10.78c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
  <path d="m10.25,7.25c-.414,0-.75-.336-.75-.75V2.5h-4c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h4.75c.414,0,.75.336.75.75v4.75c0,.414-.336.75-.75.75Z" stroke-width="0"></path>
</svg>

                    </a>
                  </li>
                  
                  <li>
                    <a href="https://zencoder.ai/blog" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group">
                      Blog
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="https://docs.zencoder.ai/changelog/home" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors group" target="_blank" rel="noopener noreferrer noopener">
                      Changelog
                      
<svg class="h-2.5 w-2.5 text-secondary-foreground/90 group-hover:text-secondary-foreground" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" fill="currentColor">
  <path d="m1.75,11c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.543,1.396c.293-.293.768-.293,1.061,0s.293.768,0,1.061L2.28,10.78c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
  <path d="m10.25,7.25c-.414,0-.75-.336-.75-.75V2.5h-4c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h4.75c.414,0,.75.336.75.75v4.75c0,.414-.336.75-.75.75Z" stroke-width="0"></path>
</svg>

                    </a>
                  </li>
                  
                </ul>
              </div>
              

              
              <div class="w-px bg-ring"></div>
              

              
              
              <div class="min-w-[12rem]">
                
                <ul>
                  
                  <li>
                    <a href="//zencoder.ai/contact" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors">
                      Contact us
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/webinars" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors">
                      Webinars
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="https://zencoder.ai/customers" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors">
                      Customers
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="https://job-boards.greenhouse.io/zencoder" class="flex items-center gap-1 p-2 rounded-md text-sm/5 text-secondary-foreground hover:bg-accent hover:text-foreground transition-colors" target="_blank" rel="noopener noreferrer noopener">
                      Careers
                      
<svg class="h-2.5 w-2.5" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" fill="currentColor">
  <path d="m1.75,11c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.543,1.396c.293-.293.768-.293,1.061,0s.293.768,0,1.061L2.28,10.78c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
  <path d="m10.25,7.25c-.414,0-.75-.336-.75-.75V2.5h-4c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h4.75c.414,0,.75.336.75.75v4.75c0,.414-.336.75-.75.75Z" stroke-width="0"></path>
</svg>

                    </a>
                  </li>
                  
                </ul>
              </div>
              
            </div>
            

            
            
            
          </div>
        </div>
        
      </div>
      
    </div>

    
    <div class="hidden lg:flex lg:flex-1 lg:justify-end lg:gap-x-3">
      
      <a href="https://auth.zencoder.ai/signin" class="btn btn-sm btn-ghost" data-utm-pass="true" target="_blank" rel="noopener noreferrer noopener">
        Log in
      </a>
      
      
      <a href="https://auth.zencoder.ai/signup" class="btn btn-sm btn-default" data-utm-pass="true">
        Get started
      </a>
      
    </div>
  </nav>

  
  <div id="mobile-menu" role="dialog" aria-modal="true" aria-label="Mobile menu" x-show="mobileOpen" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100" x-transition:leave="transition ease-in duration-200" x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0" class="lg:hidden fixed inset-0 z-[60] bg-background h-dvh overscroll-contain touch-pan-y will-change-transform transform-gpu" @keydown.tab="onTabTrap($event)" x-cloak>
    
    <div class="flex flex-col h-full min-h-0">
      
      
      <div class="flex items-center justify-between px-6 h-16">
        <div class="flex-1">
          <template x-if="mobileSubmenu !== null">
            <button @click="mobileSubmenu = null; $nextTick(() => { if ($refs.menuScroll) $refs.menuScroll.scrollTop = 0 })" class="flex items-center gap-2 text-muted-foreground hover:text-foreground">
              <svg class="size-3" viewbox="0 0 12 12" fill="currentColor" aria-hidden="true">
                <path d="m7.75,11c-.192,0-.384-.073-.53-.22L2.97,6.53c-.293-.293-.293-.768,0-1.061L7.22,1.22c.293-.293.768-.293,1.061,0s.293.768,0,1.061l-3.72,3.72,3.72,3.72c.293.293.293.768,0,1.061-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
              </svg>
              <span class="text-base text-muted-foreground font-medium">Back</span>
            </button>
          </template>
        </div>
        <button x-ref="closeBtn" @click="closedByBtn = true; mobileOpen = false; mobileSubmenu = null; openMenu = null" class="p-2 -m-2 text-muted-foreground hover:text-foreground">
          <span class="sr-only">Close menu</span>
          <svg class="size-4" viewbox="0 0 12 12" fill="currentColor" aria-hidden="true">
            <path d="m2.25,10.5c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.22,1.72c.293-.293.768-.293,1.061,0s.293.768,0,1.061l-7.5,7.5c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
            <path d="m9.75,10.5c-.192,0-.384-.073-.53-.22L1.72,2.78c-.293-.293-.293-.768,0-1.061s.768-.293,1.061,0l7.5,7.5c.293.293.293.768,0,1.061-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
          </svg>
        </button>
      </div>

      
      <div class="relative flex-1 min-h-0 overflow-hidden">
        <div class="absolute inset-0 overflow-y-auto px-6 py-8 overscroll-contain" x-ref="menuScroll">
        
        
        <template x-if="mobileSubmenu === null">
          <nav aria-label="Mobile navigation" class="will-change-transform transform-gpu" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 -translate-x-4" x-transition:enter-end="opacity-100 translate-x-0" x-transition:leave="transition ease-in duration-150" x-transition:leave-start="opacity-100 translate-x-0" x-transition:leave-end="opacity-0 -translate-x-4">
            <ul class="space-y-2 pt-14">
              
              <li>
                
                <button @click="mobileSubmenu = 1; $nextTick(() => { if ($refs.menuScroll) $refs.menuScroll.scrollTop = 0 })" class="block w-full text-left text-3xl font-medium text-foreground hover:text-secondary-foreground">
                  Product
                </button>
                
              </li>
              
              <li>
                
                <a href="//zencoder.ai/pricing" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="block text-3xl font-medium text-foreground hover:text-secondary-foreground">
                  Pricing
                </a>
                
              </li>
              
              <li>
                
                <button @click="mobileSubmenu = 3; $nextTick(() => { if ($refs.menuScroll) $refs.menuScroll.scrollTop = 0 })" class="block w-full text-left text-3xl font-medium text-foreground hover:text-secondary-foreground">
                  Enterprise
                </button>
                
              </li>
              
              <li>
                
                <button @click="mobileSubmenu = 4; $nextTick(() => { if ($refs.menuScroll) $refs.menuScroll.scrollTop = 0 })" class="block w-full text-left text-3xl font-medium text-foreground hover:text-secondary-foreground">
                  Resources
                </button>
                
              </li>
              
            </ul>
          </nav>
        </template>

        
        <template x-if="mobileSubmenu !== null">
          <nav aria-label="Submenu navigation" class="will-change-transform transform-gpu" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-x-4" x-transition:enter-end="opacity-100 translate-x-0" x-transition:leave="transition ease-in duration-150" x-transition:leave-start="opacity-100 translate-x-0" x-transition:leave-end="opacity-0 translate-x-4">
            
            
            <div x-show="mobileSubmenu === 1">
              <h3 class="h-14 flex items-end pb-2 text-base font-medium text-muted-foreground">Product</h3>
              
              
              
              <div>
                <ul class="space-y-2">
                  
                  <li>
                    <a href="//zencoder.ai/zenflow" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      Zenflow™ Code
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/zenflow-work" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      Zenflow™ Work
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/product/coding-agent" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      IDE Agents
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/marketplace" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      Marketplace
                      
                    </a>
                  </li>
                  
                </ul>
              </div>
              

              
              
            </div>
            
            
            
            
            
            <div x-show="mobileSubmenu === 3">
              <h3 class="h-14 flex items-end pb-2 text-base font-medium text-muted-foreground">Enterprise</h3>
              
              
              
              <div>
                <ul class="space-y-2">
                  
                  <li>
                    <a href="//zencoder.ai/enterprise" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      Zencoder for Enterprise
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/solutions/engineering-managers" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      Zenflow for Engineering Managers
                      
                    </a>
                  </li>
                  
                </ul>
              </div>
              

              
              
            </div>
            
            
            
            <div x-show="mobileSubmenu === 4">
              <h3 class="h-14 flex items-end pb-2 text-base font-medium text-muted-foreground">Resources</h3>
              
              
              
              <div>
                <ul class="space-y-2">
                  
                  <li>
                    <a href="https://docs.zencoder.ai/" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true" target="_blank" rel="noopener noreferrer noopener">
                      Docs
                      
<svg class="h-3.5 w-3.5" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" fill="currentColor">
  <path d="m1.75,11c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.543,1.396c.293-.293.768-.293,1.061,0s.293.768,0,1.061L2.28,10.78c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
  <path d="m10.25,7.25c-.414,0-.75-.336-.75-.75V2.5h-4c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h4.75c.414,0,.75.336.75.75v4.75c0,.414-.336.75-.75.75Z" stroke-width="0"></path>
</svg>

                    </a>
                  </li>
                  
                  <li>
                    <a href="https://discord.com/invite/zencoder" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true" target="_blank" rel="noopener noreferrer noopener">
                      Community
                      
<svg class="h-3.5 w-3.5" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" fill="currentColor">
  <path d="m1.75,11c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.543,1.396c.293-.293.768-.293,1.061,0s.293.768,0,1.061L2.28,10.78c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
  <path d="m10.25,7.25c-.414,0-.75-.336-.75-.75V2.5h-4c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h4.75c.414,0,.75.336.75.75v4.75c0,.414-.336.75-.75.75Z" stroke-width="0"></path>
</svg>

                    </a>
                  </li>
                  
                  <li>
                    <a href="https://zencoder.ai/blog" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      Blog
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="https://docs.zencoder.ai/changelog/home" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true" target="_blank" rel="noopener noreferrer noopener">
                      Changelog
                      
<svg class="h-3.5 w-3.5" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" fill="currentColor">
  <path d="m1.75,11c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.543,1.396c.293-.293.768-.293,1.061,0s.293.768,0,1.061L2.28,10.78c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
  <path d="m10.25,7.25c-.414,0-.75-.336-.75-.75V2.5h-4c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h4.75c.414,0,.75.336.75.75v4.75c0,.414-.336.75-.75.75Z" stroke-width="0"></path>
</svg>

                    </a>
                  </li>
                  
                </ul>
              </div>
              

              
              
              <div>
                <ul class="space-y-2 mt-2">
                  
                  <li>
                    <a href="//zencoder.ai/contact" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      Contact us
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="//zencoder.ai/webinars" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      Webinars
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="https://zencoder.ai/customers" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true">
                      Customers
                      
                    </a>
                  </li>
                  
                  <li>
                    <a href="https://job-boards.greenhouse.io/zencoder" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex items-center gap-2 text-3xl font-medium text-secondary-foreground hover:text-foreground" data-utm-pass="true" target="_blank" rel="noopener noreferrer noopener">
                      Careers
                      
<svg class="h-3.5 w-3.5" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" fill="currentColor">
  <path d="m1.75,11c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061L9.543,1.396c.293-.293.768-.293,1.061,0s.293.768,0,1.061L2.28,10.78c-.146.146-.338.22-.53.22Z" stroke-width="0"></path>
  <path d="m10.25,7.25c-.414,0-.75-.336-.75-.75V2.5h-4c-.414,0-.75-.336-.75-.75s.336-.75.75-.75h4.75c.414,0,.75.336.75.75v4.75c0,.414-.336.75-.75.75Z" stroke-width="0"></path>
</svg>

                    </a>
                  </li>
                  
                </ul>
              </div>
              
            </div>
            
            
          </nav>
        </template>
        </div>
      </div>

      
      <div class="px-6 py-6 border-t border-border">
        <div class="flex gap-3">
          
          <a href="https://auth.zencoder.ai/" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex-1 justify-center btn btn-secondary" data-utm-pass="true">
            Log in
          </a>
          
          
          <a href="//zencoder.ai/contact/sales" @click="mobileOpen = false; mobileSubmenu = null; openMenu = null" class="flex-1 justify-center btn btn-default" data-utm-pass="true">
            Talk to sales
          </a>
          
        </div>
      </div>
    </div>
  </div>
  <noscript>
    <style>
      [x-cloak] { display: revert !important; }
      #mobile-menu { position: static !important; display: block !important; height: auto !important; opacity: 1 !important; }
      #mobile-menu [x-show] { display: block !important; }
    </style>
  </noscript>
</header></div></div>
    

    <main id="main-content">
      

<div class="bg-background">
  <div class="container-page section-py">
    <div class="max-w-2xl mx-auto">
      <div class="flex justify-center">
        
        
          
            
              
<!-- Breadcrumbs -->
<div class="mb-8">
  <nav class="flex" aria-label="Breadcrumb">
    <ol class="flex items-center space-x-2">
      <li>
        <a href="//zencoder.ai/blog" class="font-medium tracking-wider uppercase text-xs text-muted-foreground hover:text-accent-foreground">Blog</a>
      </li>
      <li>
        <span class="font-medium tracking-wider uppercase text-xs text-neutral-400 dark:text-neutral-600">/</span>
      </li>
      <li>
        
        <a href="//zencoder.ai/blog/tag/product" class="font-medium tracking-wider uppercase text-xs text-muted-foreground hover:text-accent-foreground">Product</a>
        
      </li>
    </ol>
  </nav>
</div>

            
          
        
      </div>

      <div class="mb-8">
        <h1 class="h1 text-pretty text-center"><span id="hs_cos_wrapper_name" class="hs_cos_wrapper hs_cos_wrapper_meta_field hs_cos_wrapper_type_text" data-hs-cos-general-type="meta_field">How to Create an API in Python</span></h1>
      </div>

      <div class="flex items-center justify-center mb-12">
        <a href="//zencoder.ai/blog/author/federico-trotta" class="text-center group">
          <p class="text-sm text-muted-foreground group-hover:text-foreground">Federico Trotta</p>
          <p class="text-sm text-muted-foreground">
            Published: <time datetime="2025-02-28">February 28, 2025</time>
            
          </p>
        </a>
      </div>
    </div>

    
    
    
    
      
      
      
      
      
      
    
    <div class="mb-12 max-w-5xl mx-auto">
      <img src="https://zencoder.ai/hs-fs/hubfs/api%20with%20python.jpg?width=1600&amp;height=900&amp;name=api%20with%20python.jpg" srcset="https://zencoder.ai/hs-fs/hubfs/api%20with%20python.jpg?width=768&amp;name=api%20with%20python.jpg 768w, https://zencoder.ai/hs-fs/hubfs/api%20with%20python.jpg?width=1280&amp;name=api%20with%20python.jpg 1280w, https://zencoder.ai/hs-fs/hubfs/api%20with%20python.jpg?width=1600&amp;name=api%20with%20python.jpg 1600w, https://zencoder.ai/hs-fs/hubfs/api%20with%20python.jpg?width=2048&amp;name=api%20with%20python.jpg 2048w" sizes="(min-width: 1024px) 1024px, 100vw" alt="How to Create an API in Python" width="1600" height="900" class="w-full h-auto rounded-2xl ring-1 ring-ring" loading="eager" fetchpriority="high" decoding="async">
    </div>
    

    <div class="pb-16 border-b border-ring">
      <article class="
        prose prose-neutral dark:prose-invert prose-base lg:prose-lg
        prose-headings:font-medium
        prose-a:font-normal prose-a:[text-underline-position:under] prose-a:[text-decoration-thickness:from-font]
        prose-pre:border prose-pre:border-ring prose-pre:text-sm prose-pre:text-wrap
        article max-w-2xl mx-auto post__content text-pretty
      ">
        <span id="hs_cos_wrapper_post_body" class="hs_cos_wrapper hs_cos_wrapper_meta_field hs_cos_wrapper_type_rich_text" style="" data-hs-cos-general-type="meta_field" data-hs-cos-type="rich_text"><p>APIs enable disparate systems to communicate, driving innovation in app development.</p>
<!--more-->
<p>In today's tech-driven world, Python stands as a pillar of API development due to its clear syntax and vast library ecosystem. Its popularity isn't just a passing trend; it's an acknowledgment of its prowess as a versatile and efficient programming language.&nbsp;</p>
<p>With powerful frameworks like Flask, Django, and FastAPI, Python is well-suited to creating resilient web services with minimal overhead and, in this article, we’ll give proof of that.</p>
<p style="font-weight: bold;">Here's what you'll learn here:</p>
<ul>
<li aria-level="1"><strong>Understanding APIs and Their Importance:</strong> We'll explore what APIs are and why they're the backbone of modern connectivity, enabling different software systems to communicate seamlessly.</li>
<li aria-level="1"><strong>The Advantages of Python for API Development:</strong> You’ll discover why Python is often the language of choice for API development due to its readability, extensive libraries, and supportive community.</li>
<li aria-level="1"><strong>Flask for Lightweight Python APIs:</strong> You’ll learn how to set up Flask for creating simple, lightweight APIs, and how to build basic endpoints and handle POST requests with JSON data.</li>
<li aria-level="1"><strong>Developing Scalable APIs with Django:</strong> You’ll understand how to build scalable APIs using Django and the Django REST Framework, including setting up projects and managing databases with Django ORM.</li>
<li aria-level="1"><strong>FastAPI for High-Performance Needs:</strong> You’ll find out how FastAPI addresses high-performance requirements by implementing asynchronous endpoints and validating data with Pydantic models.</li>
<li aria-level="1"><strong>Enhancing API Security:</strong> You’ll learn essential techniques for authenticating users, securing your APIs with HTTPS, and implementing rate limiting to protect against threats.</li>
<li aria-level="1"><strong>Deploying and Testing Python APIs:</strong> You’ll get insights into deploying your APIs using Docker and cloud services, and discover how to integrate APIs with front-end applications for a seamless user experience.</li>
<li aria-level="1"><strong>Leveraging Python APIs for AI and Data Processing:</strong> You’ll see how Python APIs can be leveraged for complex AI computations and data processing tasks, enabling efficient handling of vast datasets.</li>
<li aria-level="1"><strong>Implementing Best Practices in Python API Development:</strong> You’ll explore best practices to ensure your APIs are maintainable, scalable, and secure, including <a href="/blog/how-to-write-clean-code" rel="noopener" target="_blank">clean code</a> principles, documentation, and monitoring.</li>
</ul>
<p>Let’s dive in!</p>
<h2>Understanding APIs and Their Importance</h2>
<p>APIs—Application Programming Interfaces—are sets of rules containing definitions and protocols that enable different software applications to communicate with each other. They offer structured access to the functionalities of a program, often through a web-based interface, facilitating the movement of data between disparate systems. This modular approach not only encourages flexibility and scalability but also drastically reduces development times by allowing developers to leverage pre-existing functionalities rather than building from scratch.</p>
<p>To illustrate the idea, consider a hotel booking app that seamlessly integrates flight and cab booking functionalities. This integration is an example of APIs at work behind the scenes. By utilizing various APIs, the app connects to multiple service providers, unifying all transactions under a single user interface.</p>
<p>So, embracing APIs leads to a more interconnected world where applications deliver enriched user experiences by interfacing with numerous external services.</p>
<h2>The Advantages of Python for API Development</h2>
<p>When considering the many avenues for API development, Python emerges as a language of choice. Since its inception, Python has been celebrated for its readability, straightforward syntax, and comprehensive libraries, making it an ideal candidate for API development. Its rich ecosystem fosters rapid prototyping, allowing developers to bring ideas to fruition swiftly and efficiently.</p>
<p>Moreover, Python's vast array of libraries and frameworks specifically tailored for API development—such as Flask, Django, and FastAPI—provide powerful tools to create robust and efficient APIs.&nbsp;</p>
<p>Each framework brings unique strengths, enabling customization to suit any project demand and the versatility of the language ensures that even developers with basic programming experience can build functioning APIs without being overwhelmed. From a robust community to detailed documentation, Python’s support network simplifies the learning curve and problem-solving processes.</p>
<p>So, by combining simplicity with capability, Python empowers developers to unlock innovative solutions and build upon existing technologies efficiently.</p>
<h2>Flask for Lightweight Python APIs</h2>
<p>Flask stands out as an excellent choice for developers seeking to create small, lightweight APIs due to its minimalistic design.. With its simple setup and straightforward approach, Flask is particularly appealing for developing prototypes or applications where simplicity and speed are prioritized without sacrificing power or scalability.</p>
<p>Given Flask's inherent flexibility, you can seamlessly extend your application's capabilities using a myriad of plugins and extensions available in its ecosystem. So, whether for educational projects, hobbyist endeavors, or professional use cases, Flask is a compelling choice for lightweight Python API development, providing a solid foundation with minimal overhead.</p>
<h3>Setting Up Flask for Your API</h3>
<p>Setting up Flask for your API project involves straightforward steps—installing Flask, creating a basic Python file, and using its built-in development server. Flask empowers developers with its micro-framework philosophy, offering flexibility and control while maintaining simplicity and elegance.</p>
<p>To begin, install Flask using pip, Python's package manager:</p>
<table>
<tbody>
<tr>
<td>
<p>pip install flask</p>
</td>
</tr>
</tbody>
</table>
<p>Next, create a simple app.py file where your API logic will reside:</p>
<table>
<tbody>
<tr>
<td>
<p>from flask import Flask<br><br>app = Flask(__name__)<br><br>if __name__ == '__main__':<br>&nbsp; &nbsp; app.run(debug=True)</p>
</td>
</tr>
</tbody>
</table>
<p>This setup initializes a Flask application and runs a development server.</p>
<p>Creating Basic Endpoints with Flask</p>
<p>When crafting basic endpoints with Flask, the process involves creating routes that handle HTTP requests for specific paths. Each route corresponds to a unique URL path and defines what the server should do when a request is made.</p>
<p>Here's how to create a simple GET endpoint:</p>
<table>
<tbody>
<tr>
<td>
<p>from flask import Flask, jsonify<br><br>app = Flask(__name__)<br><br>@app.route('/api/hello', methods=['GET'])<br>def hello():<br>&nbsp; &nbsp; return jsonify(message='Hello, World!')<br><br>if __name__ == '__main__':<br>&nbsp; &nbsp; app.run(debug=True)</p>
</td>
</tr>
</tbody>
</table>
<p>In this example, the @app.route decorator defines the endpoint /api/hello, and the hello() function handles GET requests by returning a JSON response.</p>
<h3>Handling POST Requests and JSON in Flask</h3>
<p>POST requests allow users to send data to the server. In Flask, handling POST requests requires setting up the route with the appropriate HTTP method and utilizing the request object to access the data.</p>
<p>Here's how to handle POST requests and process JSON data:</p>
<table>
<tbody>
<tr>
<td>
<p>from flask import Flask, request, jsonify<br><br>app = Flask(__name__)<br><br>@app.route('/api/data', methods=['POST'])<br>def receive_data():<br>&nbsp; &nbsp; data = request.get_json()<br>&nbsp; &nbsp; # Ensure JSON validity before processing data<br>&nbsp; &nbsp; if not data:<br>&nbsp; &nbsp; &nbsp; &nbsp; return jsonify({'error': 'Invalid JSON data'}), 400<br>&nbsp; &nbsp; # Process the data (e.g., save to database)<br>&nbsp; &nbsp; return jsonify({'received': data}), 200<br><br>if __name__ == '__main__':<br>&nbsp; &nbsp; app.run(debug=True)</p>
</td>
</tr>
</tbody>
</table>
<p>In this code snippet, the receive_data() function retrieves the JSON payload from the request using request.get_json(). It then checks for validity before processing the data. Using POST and JSON effectively in Flask can address diverse needs, such as user registrations, form submissions, or any interactions requiring data transmission.</p>
<p>By efficiently managing incoming JSON payloads, you ensure that your Flask application remains robust, responsive, and ready to meet its functional requirements.</p>
<h2>Developing Scalable APIs with Django</h2>
<p>Django's robust framework architecture, driven by its comprehensive ORM (Object-Relational Mapping), serves as an excellent foundation for developing scalable APIs. Utilizing Django REST Framework (DRF), you can create robust data-driven API endpoints, paving the way for extensibility and integration into larger systems.</p>
<p>To accommodate the complexities of a growing user base, consider key scalability strategies:</p>
<ul>
<li aria-level="1">Load Balancing: Distribute traffic across multiple servers to prevent overload.</li>
<li aria-level="1">Horizontal Scaling: Add more servers to handle increased demand.</li>
<li aria-level="1">Caching Mechanisms: Optimize response times by storing frequently accessed data.</li>
</ul>
<p>By adopting these strategies in conjunction with Django's built-in capabilities—such as middleware for logging and performance improvement—you bolster your API's ability to handle increased demand.</p>
<h3>Installing Django and Setting Up a Project</h3>
<p>To embark on Django API development, setting up the initial project environment is crucial. Here’s how to do it:</p>
<ol>
<li aria-level="1">Install Python: Ensure you have Python 3.6 or later installed.</li>
<li aria-level="1">Set up a Virtual Environment:</li>
</ol>
<table>
<tbody>
<tr>
<td>
<p>python3 -m venv env<br>source env/bin/activate&nbsp; # On Windows: env\Scripts\activate</p>
</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Install Django:</li>
</ol>
<table>
<tbody>
<tr>
<td>
<p>pip install django</p>
</td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Initiate a Django Project:</li>
</ol>
<table>
<tbody>
<tr>
<td>
<p>django-admin startproject myproject<br>cd myproject</p>
</td>
</tr>
</tbody>
</table>
<ol start="5">
<li>Verify the Setup:</li>
</ol>
<table>
<tbody>
<tr>
<td>
<p>python manage.py runserver</p>
</td>
</tr>
</tbody>
</table>
<p>Now, navigate to http://127.0.0.1:8000/ to see the default Django welcome page.</p>
<h3>Utilizing Django Rest Framework</h3>
<p>Utilizing Django REST Framework (DRF) significantly enhances the development of robust web APIs as it builds upon Django's already impressive toolkit, offering powerful features like serialization and authentication.</p>
<p>Let’s see how it works.</p>
<h4>Getting Started with DRF</h4>
1. Install DRF:<br><br>
<table>
<tbody>
<tr>
<td>
<p>pip install djangorestframework</p>
</td>
</tr>
</tbody>
</table>
2. Add 'rest_framework' to INSTALLED_APPS in settings.py:<br>
<table>
<tbody>
<tr>
<td>
<p>INSTALLED_APPS = [<br>&nbsp; # ...<br>&nbsp; 'rest_framework',<br>]</p>
</td>
</tr>
</tbody>
</table>
3. Create an App:<br>
<table>
<tbody>
<tr>
<td>
<p>python manage.py startapp api</p>
</td>
</tr>
</tbody>
</table>
4. Define a Model in api/models.py:<br>
<table>
<tbody>
<tr>
<td>
<p>from django.db import models<br><br>class Article(models.Model):<br>&nbsp; &nbsp; title = models.CharField(max_length=100)<br>&nbsp; &nbsp; content = models.TextField()<br><br>&nbsp; &nbsp; def __str__(self):<br>&nbsp; &nbsp; &nbsp; &nbsp; return self.title</p>
</td>
</tr>
</tbody>
</table>
5. Create a Serializer in api/serializers.py:<br>
<table>
<tbody>
<tr>
<td>
<p>from rest_framework import serializers<br>from .models import Article<br><br>class ArticleSerializer(serializers.ModelSerializer):<br>&nbsp; &nbsp; class Meta:<br>&nbsp; &nbsp; &nbsp; &nbsp; model = Article<br>&nbsp; &nbsp; &nbsp; &nbsp; fields = '__all__'</p>
</td>
</tr>
</tbody>
</table>
6. Create Views in api/views.py:<br>
<table>
<tbody>
<tr>
<td>
<p>from rest_framework import generics<br>from .models import Article<br>from .serializers import ArticleSerializer<br><br>class ArticleList(generics.ListCreateAPIView):<br>&nbsp; &nbsp; queryset = Article.objects.all()<br>&nbsp; &nbsp; serializer_class = ArticleSerializer<br><br>class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):<br>&nbsp; &nbsp; queryset = Article.objects.all()<br>&nbsp; &nbsp; serializer_class = ArticleSerializer</p>
</td>
</tr>
</tbody>
</table>
7. Configure URLs in api/urls.py:<br>
<table>
<tbody>
<tr>
<td>
<p>from django.urls import path<br>from .views import ArticleList, ArticleDetail<br><br>urlpatterns = [<br>&nbsp; &nbsp; path('articles/', ArticleList.as_view(), name='article-list'),<br>&nbsp; &nbsp; path('articles/&lt;int:pk&gt;/', ArticleDetail.as_view(), name='article-detail'),<br>]</p>
</td>
</tr>
</tbody>
</table>
8. Include API URLs in myproject/urls.py:<br>
<table>
<tbody>
<tr>
<td>
<p>from django.urls import path, include<br><br>urlpatterns = [<br>&nbsp; &nbsp; path('api/', include('api.urls')),<br>]</p>
</td>
</tr>
</tbody>
</table>
<p>With these steps, you have a basic API that allows listing, creating, retrieving, updating, and deleting Article instances.&nbsp;</p>
<p>So, DRF’s serialization allows for the seamless conversion of complex data types into JSON, which is essential for API interaction with frontend applications.</p>
<h3>Managing Databases with Django ORM</h3>
<p>Django ORM empowers developers to interact with databases seamlessly using Python code. By abstracting the complexities of SQL syntax, it allows you to focus more on solving business logic.</p>
<p>For example, to create and query data:</p>
<table>
<tbody>
<tr>
<td>
<p># Create a new article<br>article = Article.objects.create(title='First Article', content='Hello, world!')<br><br># Query all articles<br>articles = Article.objects.all()<br><br># Filter articles<br>filtered_articles = Article.objects.filter(title__icontains='first')</p>
</td>
</tr>
</tbody>
</table>
<p>Data modeling with Django’s ORM involves defining models that directly correlate with database tables. The ORM's capability to handle one-to-many and many-to-many relationships ensures that you can map complex real-world data interactions into your applications effortlessly.</p>
<h2>FastAPI for High-Performance Needs</h2>
<p>FastAPI shines in scenarios demanding real-time, asynchronous capabilities where rapid responses are crucial to an application's success and efficiency. It leverages Python's typing features extensively, which allows you to implement modern standards and technologies like asynchronous programming smoothly.</p>
<p>Let’s see how to use it.</p>
<h3>Implementing Asynchronous Endpoints in FastAPI</h3>
<p>Developing asynchronous endpoints in FastAPI enhances application responsiveness, crucial for real-time web applications and services.</p>
<p>Here's how to create an asynchronous endpoint:</p>
<table>
<tbody>
<tr>
<td>
<p>from fastapi import FastAPI<br><br>app = FastAPI()<br><br>@app.get('/items/{item_id}')<br>async def read_item(item_id: int):<br>&nbsp; &nbsp; return {"item_id": item_id}</p>
</td>
</tr>
</tbody>
</table>
<p>In this example, the async def syntax allows the function to handle asynchronous operations efficiently. You can perform non-blocking I/O operations within these functions.</p>
<h3>Validating Data with Pydantic Models</h3>
<p>Validating data with Pydantic models ensures that incoming data complies with your application's stringent requirements.</p>
<p>Here's how to define and use Pydantic models:</p>
<table>
<tbody>
<tr>
<td>
<p>from fastapi import FastAPI<br>from pydantic import BaseModel<br><br>app = FastAPI()<br><br>class User(BaseModel):<br>&nbsp; &nbsp; username: str<br>&nbsp; &nbsp; email: str<br>&nbsp; &nbsp; is_active: bool = True<br><br>@app.post('/users/')<br>async def create_user(user: User):<br>&nbsp; &nbsp; return user</p>
</td>
</tr>
</tbody>
</table>
<p>In this example, the User model defines the expected data structure, including types and default values. FastAPI automatically:</p>
<ul>
<li aria-level="1">Parses JSON into defined objects.</li>
<li aria-level="1">Ensures type safety across application endpoints.</li>
<li aria-level="1">Defines validation rules effortlessly.</li>
<li aria-level="1">Raises informative errors for invalid input.</li>
</ul>
<p>By implementing Pydantic models, you ensure robust data integrity across various use cases.</p>
<h2>Enhancing API Security</h2>
<p>In today's digital landscape, safeguarding your APIs cannot be overstated. A well-secured API protects users' data and maintains the application's integrity. To enhance security you should:</p>
<ul>
<li aria-level="1">Adopt robust authentication methods (such as OAuth2) to verify user identities.</li>
<li aria-level="1">Employ SSL/TLS encryption to protect data in transit.</li>
<li aria-level="1">Implement rate limiting to prevent abuse.</li>
<li aria-level="1">Regularly update security practices to defend against evolving threats.</li>
</ul>
<p>So, let’s see how we can grant API security.</p>
<h3>Techniques for Authenticating Users</h3>
<p>Effective user authentication techniques are essential for safeguarding sensitive data, ensuring that only authorized users have access to your API's resources.</p>
<h4>Using OAuth2 with FastAPI</h4>
<p>FastAPI, for example, provides built-in support for OAuth2. Here’s an example:</p>
<table>
<tbody>
<tr>
<td>
<p>from fastapi import Depends, FastAPI<br>from fastapi.security import OAuth2PasswordBearer<br><br>app = FastAPI()<br>oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')<br><br>@app.get('/users/me')<br>async def read_users_me(token: str = Depends(oauth2_scheme)):<br>&nbsp; &nbsp; return {"token": token}</p>
</td>
</tr>
</tbody>
</table>
<h4>Implementing JWT Authentication</h4>
<p>JWT offers a secure way to transmit information between parties as a JSON object. Here’s an example:</p>
<table>
<tbody>
<tr>
<td>
<p>from fastapi import Depends, FastAPI, HTTPException<br>from fastapi.security import OAuth2PasswordBearer<br>from jose import JWTError, jwt<br><br>SECRET_KEY = 'your-secret-key'<br>ALGORITHM = 'HS256'<br>oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')<br><br>app = FastAPI()<br><br>def verify_token(token: str):<br>&nbsp; &nbsp; try:<br>&nbsp; &nbsp; &nbsp; &nbsp; payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])<br>&nbsp; &nbsp; &nbsp; &nbsp; return payload.get('sub')<br>&nbsp; &nbsp; except JWTError:<br>&nbsp; &nbsp; &nbsp; &nbsp; return None<br><br>@app.get('/protected')<br>async def protected_route(token: str = Depends(oauth2_scheme)):<br>&nbsp; &nbsp; user = verify_token(token)<br>&nbsp; &nbsp; if user is None:<br>&nbsp; &nbsp; &nbsp; &nbsp; raise HTTPException(status_code=401, detail='Invalid token')<br>&nbsp; &nbsp; return {'user': user}</p>
</td>
</tr>
</tbody>
</table>
<h3>Protecting APIs with HTTPS and Rate Limiting</h3>
<p>Securing APIs with HTTPS encrypts data in transit, safeguarding against eavesdropping and ensuring data integrity between clients and servers.</p>
<p>Let’s see how we can use these techniques.</p>
<h4>Enabling HTTPS</h4>
<p>In production environments, deploy your API behind a reverse proxy like Nginx that handles SSL termination. For development purposes, you can use tools like sslify for Flask:</p>
<table>
<tbody>
<tr>
<td>
<p>from flask import Flask<br>from flask_sslify import SSLify<br><br>app = Flask(__name__)<br>sslify = SSLify(app)</p>
</td>
</tr>
</tbody>
</table>
<h4>Implementing Rate Limiting</h4>
<p>Rate limiting controls the number of requests a client can make to your API in a given timeframe.</p>
<p>For Flask:</p>
<table>
<tbody>
<tr>
<td>
<p>from flask import Flask<br>from flask_limiter import Limiter<br><br>app = Flask(__name__)<br>limiter = Limiter(app, key_func=get_remote_address)<br><br>@app.route('/api/resource')<br>@limiter.limit('5 per minute')<br>def limited_resource():<br>&nbsp; &nbsp; return 'This is a rate-limited resource.'</p>
</td>
</tr>
</tbody>
</table>
<p>For FastAPI:</p>
<table>
<tbody>
<tr>
<td>
<p>from fastapi import FastAPI, Request<br>from slowapi import Limiter, _rate_limit_exceeded_handler<br>from slowapi.util import get_remote_address<br><br>app = FastAPI()<br>limiter = Limiter(key_func=get_remote_address)<br>app.state.limiter = limiter<br>app.add_exception_handler(429, _rate_limit_exceeded_handler)<br><br>@app.get('/api/resource')<br>@limiter.limit('5/minute')<br>async def limited_resource(request: Request):<br>&nbsp; &nbsp; return 'This is a rate-limited resource.'</p>
</td>
</tr>
</tbody>
</table>
<p>Both HTTPS and rate limiting are critical for protecting APIs, enhancing both security and resilience against various threats.</p>
<h2>Deploying APIs</h2>
<p>Deploying an API effectively is akin to orchestrating a finely-tuned system where each component harmoniously plays its part. Containers like Docker simplify this <a href="/glossary/container-orchestration" rel="noopener" target="_blank">orchestration</a>, allowing developers to package their applications with all dependencies for consistent execution across environments.</p>
<h3>Using Docker and Cloud Services for Deployment</h3>
<p>Docker containers are lightweight and provide a standardized unit that runs reliably across different computing environments. This ensures your applications behave the same, whether in local testing or production.</p>
<h4>Dockerizing a Flask Application</h4>
<p>Here’s how to dockerize a Flask application:</p>
<table>
<tbody>
<tr>
<td>
<p>Create a Dockerfile:<br>FROM python:3.8-slim<br><br>WORKDIR /app<br><br>COPY requirements.txt requirements.txt<br>RUN pip install -r requirements.txt<br><br>COPY . .<br><br>EXPOSE 5000<br><br>CMD ["python", "app.py"]</p>
</td>
</tr>
</tbody>
</table>
<p>Build and run the Docker image:</p>
<table>
<tbody>
<tr>
<td>
<p>docker build -t my-flask-app .<br>docker run -d -p 5000:5000 my-flask-app</p>
</td>
</tr>
</tbody>
</table>
<h4>Deploying to Cloud Platforms</h4>
<p>Cloud platforms like AWS, Heroku, and Google Cloud offer robust architectures for hosting these Docker containers. They provide scalable, secure, and affordable solutions for deploying and managing applications.</p>
<p>Here’s some basic information you should know before choosing a service rather than another for deployment:</p>
<ul>
<li aria-level="1">AWS Elastic Beanstalk: Supports Docker deployments with ease.</li>
<li aria-level="1">Heroku: Use a Dockerfile and heroku.yml for container deployments.</li>
<li aria-level="1">Google Cloud Run: Deploy containers directly with automatic scaling.</li>
</ul>
<p>&nbsp;</p>
<h2>Implementing Best Practices in Python API Development</h2>
<p>Implementing best practices in Python API development is paramount to ensure maintainability, scalability, and security of your applications, while also enhancing the user experience.</p>
<p>Here we provide common ideas and patterns.</p>
<h3>Clean and Reusable Code</h3>
<p>Prioritize clean and reusable code to maximize efficiency:</p>
<ul>
<li aria-level="1">Follow PEP 8 Style Guidelines: Enhance readability and consistency.</li>
<li aria-level="1">Use Modular Design: Break code into reusable modules and functions.</li>
<li aria-level="1">Apply the DRY Principle: Don't Repeat Yourself; avoid code duplication.</li>
</ul>
<h3>Documentation and Versioning</h3>
<p>Comprehensive documentation acts as a source of truth for both current and future developers:</p>
<ul>
<li aria-level="1">Write Clear Docstrings: Explain functions, classes, and modules.</li>
<li aria-level="1">Use Tools like Sphinx or Swagger: <a href="/blog/automated-docstrings-industry-use" rel="noopener">Generate documentation automatically</a>.</li>
<li aria-level="1">Implement API Versioning: Maintain backward compatibility while iterating.</li>
</ul>
<h3>Monitoring and Optimization</h3>
<p>Continuous monitoring and optimization are vital:</p>
<ul>
<li aria-level="1">Use Logging: Implement logging to track application behavior.</li>
<li aria-level="1">Monitor Performance: Tools like Prometheus or New Relic can observe your API's health.</li>
<li aria-level="1">Optimize Queries: Analyze and optimize database queries to improve performance.</li>
</ul>
<h2>Conclusions</h2>
<p>The versatility of Python, coupled with its rich library ecosystem, makes it an ideal choice for creating APIs that cater to diverse application needs. From building lightweight APIs with Flask to harnessing the power of Django's robust tools and exploiting FastAPI's high performance, Python covers a wide array of development scenarios. Consequently, you can select frameworks aligning perfectly with your project specifications and desired scalability.</p>
<p>We'd love to hear your thoughts and experiences with Python API development. So, feel free to leave comments below, and start developing your APIs in Python by using <a href="https://zencoder.ai/">Zencoder’s AI-driven code generation</a> for enhanced productivity!</p>
<p>Explore more Python tutorials from our blog: <br><a href="https://zencoder.ai/blog/python-flask-web-development-snippets">Essential Python Snippets for Web Development with Flask</a>, <br><a href="https://zencoder.ai/blog/python-debugging-tips-code-snippets">Debugging in Python: 6 Snippets to Make Your Life Easier</a>, <br><a href="https://zencoder.ai/blog/python-database-sqlite-sqlalchemy-snippets">Python Snippets for Working with Databases: SQLite and SQLAlchemy</a></p></span>
      </article>
    </div>

    
    <div class="mt-16">
      <h2 class="h3 mb-8">Latest in Product</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        
        
          
          
            
            
            
              
                
                
                
                <a href="//zencoder.ai/blog/how-does-zenflow-handle-testing-a-full-comparison" class="group relative block transition-colors duration-200" aria-label="Read more about How does Zenflow handle testing? A full comparison">
  
  
  
  
    
    
    
    
    
    
  
  <div class="aspect-2/1 overflow-hidden rounded ring-1 ring-ring">
    <img src="https://zencoder.ai/hs-fs/hubfs/How%20does%20Zenflow%20handle%20testing.webp?width=800&amp;height=400&amp;name=How%20does%20Zenflow%20handle%20testing.webp" srcset="https://zencoder.ai/hs-fs/hubfs/How%20does%20Zenflow%20handle%20testing.webp?width=400&amp;name=How%20does%20Zenflow%20handle%20testing.webp 400w, https://zencoder.ai/hs-fs/hubfs/How%20does%20Zenflow%20handle%20testing.webp?width=600&amp;name=How%20does%20Zenflow%20handle%20testing.webp 600w, https://zencoder.ai/hs-fs/hubfs/How%20does%20Zenflow%20handle%20testing.webp?width=800&amp;name=How%20does%20Zenflow%20handle%20testing.webp 800w, https://zencoder.ai/hs-fs/hubfs/How%20does%20Zenflow%20handle%20testing.webp?width=1200&amp;name=How%20does%20Zenflow%20handle%20testing.webp 1200w" sizes="(min-width: 1024px) 400px, (min-width: 768px) 50vw, 100vw" alt="How does Zenflow handle testing? A full comparison" width="800" height="400" loading="lazy" decoding="async" class="h-full w-full object-cover group-hover:scale-103 transition-transform duration-300">
  </div>
  
  <div class="py-6">
    <div class="flex items-center gap-x-1">

      
      
      
      
      <span class="relative z-10 text-sm text-muted-foreground">Product</span>
      <span class="text-sm text-muted-foreground">•</span>
      
      
      
      
      

      
      <span class="text-sm text-muted-foreground">
        May 16, 2026
      </span>
      
    </div>
    <h3 class="mt-2 text-lg font-normal font-sans text-secondary-foreground group-hover:text-foreground transition-colors duration-300">
      How does Zenflow handle testing? A full comparison
    </h3>
  </div>
</a>
                
              
            
              
                
                
                
                <a href="//zencoder.ai/blog/ai-agent-survival-guide-part-4-your-agent-army-awaits" class="group relative block transition-colors duration-200" aria-label="Read more about AI Agent Survival Guide, Part 4: Your Agent Army Awaits">
  
  
  
  
    
    
    
    
    
    
  
  <div class="aspect-2/1 overflow-hidden rounded ring-1 ring-ring">
    <img src="https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%204.webp?width=800&amp;height=400&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%204.webp" srcset="https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%204.webp?width=400&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%204.webp 400w, https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%204.webp?width=600&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%204.webp 600w, https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%204.webp?width=800&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%204.webp 800w, https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%204.webp?width=1200&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%204.webp 1200w" sizes="(min-width: 1024px) 400px, (min-width: 768px) 50vw, 100vw" alt="AI Agent Survival Guide, Part 4: Your Agent Army Awaits" width="800" height="400" loading="lazy" decoding="async" class="h-full w-full object-cover group-hover:scale-103 transition-transform duration-300">
  </div>
  
  <div class="py-6">
    <div class="flex items-center gap-x-1">

      
      
      
      
      <span class="relative z-10 text-sm text-muted-foreground">Product</span>
      <span class="text-sm text-muted-foreground">•</span>
      
      
      
      
      

      
      <span class="text-sm text-muted-foreground">
        August 28, 2026
      </span>
      
    </div>
    <h3 class="mt-2 text-lg font-normal font-sans text-secondary-foreground group-hover:text-foreground transition-colors duration-300">
      AI Agent Survival Guide, Part 4: Your Agent Army Awaits
    </h3>
  </div>
</a>
                
              
            
              
                
                
                
                <a href="//zencoder.ai/blog/ai-agent-survival-guide-part-3-that-mcp-server-you-just-installed" class="group relative block transition-colors duration-200" aria-label="Read more about AI Agent Survival Guide, Part 3: That MCP Server You Just Installed">
  
  
  
  
    
    
    
    
    
    
  
  <div class="aspect-2/1 overflow-hidden rounded ring-1 ring-ring">
    <img src="https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%203.webp?width=800&amp;height=400&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%203.webp" srcset="https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%203.webp?width=400&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%203.webp 400w, https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%203.webp?width=600&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%203.webp 600w, https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%203.webp?width=800&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%203.webp 800w, https://zencoder.ai/hs-fs/hubfs/AI%20Agent%20Survival%20Guide%20_%20Part%203.webp?width=1200&amp;name=AI%20Agent%20Survival%20Guide%20_%20Part%203.webp 1200w" sizes="(min-width: 1024px) 400px, (min-width: 768px) 50vw, 100vw" alt="AI Agent Survival Guide, Part 3: That MCP Server You Just Installed" width="800" height="400" loading="lazy" decoding="async" class="h-full w-full object-cover group-hover:scale-103 transition-transform duration-300">
  </div>
  
  <div class="py-6">
    <div class="flex items-center gap-x-1">

      
      
      
      
      <span class="relative z-10 text-sm text-muted-foreground">Product</span>
      <span class="text-sm text-muted-foreground">•</span>
      
      
      
      
      

      
      <span class="text-sm text-muted-foreground">
        February 12, 2026
      </span>
      
    </div>
    <h3 class="mt-2 text-lg font-normal font-sans text-secondary-foreground group-hover:text-foreground transition-colors duration-300">
      AI Agent Survival Guide, Part 3: That MCP Server You Just Installed
    </h3>
  </div>
</a>
                
              
            
              
            
          
        
      </div>
    </div>
    
  </div>
</div>

    </main>

    
      <div data-global-resource-path="forgood-tailwind-theme/templates/partials/footer.html"><div id="hs_cos_wrapper_module_17376119765712" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">






<footer class="relative overflow-hidden isolate">
  <div class="bg-secondary border-y border-ring">
    <div class="container-page">
      <div class="py-32 flex flex-col items-center text-center gap-8">
        <h2 class="h1">Build complex. Stay simple</h2>
        
        

<div class="flex items-center justify-center gap-x-3">
  
    
    

    
    

    
    
    <a data-utm-pass="true" href="https://auth.zencoder.ai/signup" class="btn btn-default ">
      
      Get started
      
    </a>
  
    
    

    
    
      
    

    
    
    <a data-utm-pass="true" href="//zencoder.ai/contact/sales" class="btn btn-secondary ">
      
      Contact sales
      
        
<svg class="h-2.5 w-2.5 ml-1" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" fill="currentColor">
  <path d="m4.25,11c-.192,0-.384-.073-.53-.22-.293-.293-.293-.768,0-1.061l3.72-3.72-3.72-3.72c-.293-.293-.293-.768,0-1.061s.768-.293,1.061,0l4.25,4.25c.293.293.293.768,0,1.061l-4.25,4.25c-.146.146-.338.22-.53.22Z"></path>
</svg>

      
    </a>
  
</div>


      </div>
    </div>
  </div>

  <div class="bg-card">
    <div class="container-page">
      <div class="py-16 md:grid md:grid-cols-3 md:gap-8 lg:grid-cols-5">
        <div class="flex justify-start">
          
  <svg class="h-7 w-7 text-secondary-foreground" viewbox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Zencoder logo">
    <g fill="currentColor">
      <path d="M20.463 33.724c-.624-2.107-1.68-4.61-3.838-5.532-2.187-.852-4.678.163-6.468 1.453-1.342.986-2.514 2.299-3.133 3.874-.21.537-.356 1.097-.426 1.663-.087.566-.163 1.138-.151 1.715.064 3.74 2.082 7.329 4.853 9.762 1.51 1.289 3.464 2.474 5.54 2.328 3.313-.338 3.949-4.429 4.305-7.084.152-1.097.158-2.205.105-3.308-.087-1.651-.338-3.279-.793-4.872Z" />
      <path d="M39.699 34.587c-.998-.484-2.048-.834-3.115-1.126-1.592-.426-3.225-.694-4.882-.753-2.193-.058-4.899.17-6.445 1.943-1.487 1.815-1.289 4.505-.612 6.606.525 1.581 1.411 3.098 2.718 4.177.443.362.933.677 1.452.922.513.257 1.032.508 1.587.677 3.575 1.097 7.611.286 10.778-1.599 1.686-1.033 3.424-2.532 3.92-4.557.7-3.256-2.986-5.123-5.407-6.284Z" />
      <path d="M49.241 16.616c-.466-1.926-1.347-4.044-3.114-5.141-2.876-1.675-5.792 1.26-7.647 3.198-.77.799-1.429 1.686-2.03 2.613-.898 1.383-1.656 2.854-2.222 4.406-.729 2.071-1.353 4.72-.146 6.728 1.266 1.972 3.879 2.62 6.084 2.626 1.668-.006 3.383-.385 4.812-1.295.484-.309.933-.677 1.324-1.097.402-.409.799-.829 1.131-1.296 2.147-3.063 2.626-7.153 1.808-10.754Z" />
      <path d="M30.88 18.115c2.269-.595 3.686-2.882 4.374-4.977.507-1.587.676-3.337.256-4.977-.146-.554-.356-1.096-.63-1.598-.262-.508-.536-1.016-.886-1.477C31.743 2.098 28.004.383 24.33.044 22.353-.107 20.072.08 18.48 1.421c-2.485 2.223-.595 5.905.676 8.263.525.974 1.167 1.878 1.861 2.736 1.038 1.284 2.199 2.457 3.505 3.478 1.739 1.336 4.066 2.742 6.358 2.217Z" />
      <path d="M11.632 25.59c1.54-.59 3.015-1.331 4.392-2.259 1.808-1.243 3.861-3.023 4.071-5.363.134-2.34-1.598-4.399-3.383-5.7-1.353-.974-2.963-1.675-4.654-1.785-.571-.035-1.149 0-1.709.105-.566.093-1.132.198-1.68.385C5.134 12.187 2.34 15.215.888 18.611c-.758 1.832-1.283 4.067-.501 5.992 1.348 3.046 5.43 2.387 8.061 1.908 1.091-.198 2.147-.531 3.179-.922Z" />
    </g>
  </svg>

        </div>

        <div class="mt-8 grid grid-cols-2 gap-8 md:col-span-2 md:mt-0 lg:col-span-4 lg:grid-cols-5">
          
            
  <div>
    <h3 class="text-sm/6 capitalize tracking-[.015em] text-muted-foreground font-normal">Product</h3>
    <ul role="list" class="mt-2 space-y-2">
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/zenflow">
            Zenflow™ Code
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/zenflow-work">
            Zenflow™ Work
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/product/coding-agent">
            IDE Agents
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/product/universal-ai-platform">
            CLI
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/product/integrations">
            Integrations
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/enterprise">
            Enterprise
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/pricing">
            Pricing
          </a>
        </li>
      
      
    </ul>
  </div>

          
            
  <div>
    <h3 class="text-sm/6 capitalize tracking-[.015em] text-muted-foreground font-normal">Resources</h3>
    <ul role="list" class="mt-2 space-y-2">
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://docs.zencoder.ai/" target="_blank" rel="noopener noreferrer noopener">
            Docs
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/marketplace">
            Marketplace
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/newsletter">
            Newsletter
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/webinars">
            Webinars
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://status.zencoder.ai/" target="_blank" rel="noopener noreferrer noopener">
            Status
          </a>
        </li>
      
      
    </ul>
  </div>

          
            
  <div>
    <h3 class="text-sm/6 capitalize tracking-[.015em] text-muted-foreground font-normal">Company</h3>
    <ul role="list" class="mt-2 space-y-2">
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/about">
            About
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://job-boards.greenhouse.io/zencoder" target="_blank" rel="noopener noreferrer noopener">
            Careers
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/blog">
            Blog
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/customers">
            Customers
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/newsroom">
            Newsroom
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/events">
            Events
          </a>
        </li>
      
      
    </ul>
  </div>

          
            
  <div>
    <h3 class="text-sm/6 capitalize tracking-[.015em] text-muted-foreground font-normal">Legal</h3>
    <ul role="list" class="mt-2 space-y-2">
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://zencoder.ai/legal/terms-of-service" target="_blank" rel="noopener noreferrer noopener">
            Terms – Zencoder
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://zencoder.ai/legal/terms-of-service-zenflow" target="_blank" rel="noopener noreferrer noopener">
            Terms – Zenflow
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://zencoder.ai/legal/privacy-policy" target="_blank" rel="noopener noreferrer noopener">
            Privacy Policy
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://zencoder.ai/legal/acceptable-use-policy" target="_blank" rel="noopener noreferrer noopener">
            Usage Policy
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://trust.zencoder.ai/" target="_blank" rel="noopener noreferrer noopener">
            Trust Center
          </a>
        </li>
      
      
        <li>
          <button type="button" class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors cursor-pointer" onclick="(function(){ var _hsp = window._hsp = window._hsp || []; _hsp.push(['showBanner']); })()">
            Manage Cookies
          </button>
        </li>
        <li>
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors flex items-center gap-2" href="#" data-acsb-custom-trigger="true" aria-label="Accessibility widget">
            <span>Accessibility</span>
          </a>
        </li>
      
    </ul>
  </div>

          
          
  <div>
    <h3 class="text-sm/6 capitalize tracking-[.015em] text-muted-foreground font-normal">Connect</h3>
    <ul role="list" class="mt-2 space-y-2">
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="//zencoder.ai/contact">
            Contact us
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://discord.com/invite/zencoder" target="_blank" rel="noopener noreferrer noopener">
            Community
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://www.linkedin.com/company/zencoderai" target="_blank" rel="noopener noreferrer noopener">
            LinkedIn
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://www.youtube.com/@zencoderai" target="_blank" rel="noopener noreferrer noopener">
            YouTube
          </a>
        </li>
      
        <li>
          
          
          <a class="text-base/6 sm:text-sm/6 capitalize tracking-[.015em] text-secondary-foreground hover:text-foreground transition-colors" href="https://x.com/zencoderai" target="_blank" rel="noopener noreferrer noopener">
            X
          </a>
        </li>
      
      
    </ul>
  </div>

        </div>
      </div>

      <div class="py-8 space-y-6 md:space-y-0 md:grid md:grid-cols-3 md:items-center md:gap-6">
        <p class="text-sm/6 font-sans text-muted-foreground">© 2026 For Good AI Inc. All rights reserved.</p>

        <div class="md:justify-self-center" x-data="themeSwitcher()">
          <fieldset class="contents">
            <legend class="sr-only">Color theme</legend>
            <div class="inline-flex rounded-full bg-secondary ring-1 ring-inset ring-ring p-1">
              <div class="relative grid grid-cols-3 rounded-full">
                <input class="peer/light sr-only" type="radio" name="theme" value="light" id="theme-light" :checked="mode === 'light'" @change="set('light')">
                <label for="theme-light" class="relative z-10 cursor-pointer rounded-full px-3 py-1.5 transition-colors text-muted-foreground hover:text-secondary-foreground peer-checked/light:text-secondary-foreground flex items-center justify-center" aria-label="Light theme">
                  <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" class="w-3.5 h-3.5"><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" stroke="currentColor"><circle cx="6" cy="6" r="2.25"></circle><line x1="6" y1=".75" x2="6" y2="1.5"></line><line x1="9.712" y1="2.288" x2="9.182" y2="2.818"></line><line x1="11.25" y1="6" x2="10.5" y2="6"></line><line x1="9.712" y1="9.712" x2="9.182" y2="9.182"></line><line x1="6" y1="11.25" x2="6" y2="10.5"></line><line x1="2.288" y1="9.712" x2="2.818" y2="9.182"></line><line x1=".75" y1="6" x2="1.5" y2="6"></line><line x1="2.288" y1="2.288" x2="2.818" y2="2.818"></line></g></svg>
                </label>
                <input class="peer/system sr-only" type="radio" name="theme" value="system" id="theme-system" :checked="mode === 'system'" @change="set('system')">
                <label for="theme-system" class="relative z-10 cursor-pointer rounded-full px-3 py-1.5 transition-colors text-muted-foreground hover:text-secondary-foreground peer-checked/system:text-secondary-foreground flex items-center justify-center" aria-label="System theme">
                  <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" class="w-3.5 h-3.5"><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" stroke="currentColor"><path d="m9,11.25c-2-.667-4-.667-6,0"></path><line x1="6" y1="10.75" x2="6" y2="8.25"></line><rect x=".75" y=".75" width="10.5" height="7.5" rx="2" ry="2" transform="translate(12 9) rotate(180)"></rect></g></svg>
                </label>
                <input class="peer/dark sr-only" type="radio" name="theme" value="dark" id="theme-dark" :checked="mode === 'dark'" @change="set('dark')">
                <label for="theme-dark" class="relative z-10 cursor-pointer rounded-full px-3 py-1.5 transition-colors text-muted-foreground hover:text-secondary-foreground peer-checked/dark:text-secondary-foreground flex items-center justify-center" aria-label="Dark theme">
                  <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 12 12" class="w-3.5 h-3.5"><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" stroke="currentColor"><path d="m8.5,7.75c-2.347,0-4.25-1.903-4.25-4.25,0-1.018.373-1.939.969-2.671C2.693,1.208.75,3.368.75,6c0,2.899,2.351,5.25,5.25,5.25,2.632,0,4.792-1.943,5.171-4.469-.732.597-1.653.969-2.671.969Z"></path></g></svg>
                </label>
                <span class="pointer-events-none absolute inset-y-0 left-0 w-1/3 rounded-full bg-accent ring-1 ring-inset ring-ring transition-transform duration-150 ease-[cubic-bezier(0.65,0,0.35,1)] peer-checked/system:translate-x-full peer-checked/dark:translate-x-[200%]" aria-hidden="true"></span>
              </div>
            </div>
          </fieldset>
        </div>

      
        
        
        <div class="md:justify-self-end">
          <div class="flex flex-wrap items-center gap-2">
            <p class="text-sm/6 font-sans text-muted-foreground mr-2">Ask AI about Zencoder</p>
            <div class="inline-flex p-1">
              
                <a target="_blank" rel="noopener noreferrer" aria-label="Ask ChatGPT about Zencoder" class="cursor-pointer rounded-full px-3 py-1.5 transition-colors text-muted-foreground hover:text-secondary-foreground flex items-center justify-center" href="https://chatgpt.com/?prompt=What+is+Zencoder+and+how+does+it+help+developers+code+faster%3F+Summarize+https%3A%2F%2Fzencoder.ai">
                  <svg aria-hidden="true" class="w-4 h-4" viewbox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M38.3545 36.0751V26.6598C38.3545 25.8668 38.652 25.2719 39.3455 24.8759L58.2754 13.9741C60.8525 12.4877 63.925 11.7942 67.0958 11.7942C78.9887 11.7942 86.5212 21.0114 86.5212 30.8227C86.5212 31.5162 86.5212 32.3092 86.4217 33.1022L66.7983 21.6055C65.6092 20.912 64.4196 20.912 63.2304 21.6055L38.3545 36.0751ZM82.5562 72.7451V50.2471C82.5562 48.8592 81.9617 47.8684 80.7725 47.1746L55.8967 32.7052L64.0233 28.0468C64.7171 27.6508 65.3121 27.6508 66.0054 28.0468L84.9354 38.9486C90.3867 42.1205 94.0533 48.8592 94.0533 55.4001C94.0533 62.9321 89.5937 69.8705 82.5562 72.7451ZM32.5072 52.9238L24.3804 48.1667C23.6869 47.7709 23.3894 47.1759 23.3894 46.383V24.5793C23.3894 13.9751 31.5162 5.94685 42.5175 5.94685C46.6804 5.94685 50.5446 7.33477 53.8162 9.81222L34.2921 21.1109C33.1031 21.8044 32.5081 22.7954 32.5081 24.1833L32.5072 52.9238ZM50 63.0326L38.3545 56.4917V42.6167L50 36.0761L61.6446 42.6167V56.4917L50 63.0326ZM57.4825 93.1617C53.3196 93.1617 49.4554 91.7738 46.1837 89.2963L65.7079 77.9976C66.8971 77.3042 67.4917 76.313 67.4917 74.9251V46.1838L75.7179 50.9409C76.4117 51.3367 76.7092 51.9317 76.7092 52.7246V74.5284C76.7092 85.1326 68.4829 93.1617 57.4825 93.1617ZM33.9937 71.0609L15.0637 60.1588C9.61233 56.9871 5.94588 50.2484 5.94588 43.7076C5.94588 36.0761 10.5048 29.2377 17.5411 26.3633V48.9596C17.5411 50.3476 18.1361 51.3388 19.3251 52.0321L44.1025 66.4021L35.9756 71.0609C35.2821 71.4567 34.6872 71.4567 33.9937 71.0609ZM32.9042 87.3142C21.705 87.3142 13.4787 78.8901 13.4787 68.4838C13.4787 67.6909 13.5781 66.898 13.6767 66.1051L33.2007 77.4034C34.3897 78.0971 35.5796 78.0971 36.7686 77.4034L61.6446 63.0334V72.4488C61.6446 73.2417 61.3471 73.8367 60.6533 74.2326L41.7233 85.1342C39.1466 86.6209 36.0751 87.3142 32.9042 87.3142ZM57.4825 99.1076C69.4746 99.1076 79.4842 90.5846 81.7646 79.2859C92.8642 76.4117 100 66.0055 100 55.4013C100 48.4634 97.0271 41.7246 91.675 36.8681C92.1708 34.7866 92.4683 32.7052 92.4683 30.6247C92.4683 16.4526 80.9713 5.84735 67.6908 5.84735C65.0154 5.84735 62.4383 6.24335 59.8617 7.13581C55.4012 2.77494 49.2562 0 42.5175 0C30.5252 0 20.516 8.52281 18.2355 19.8215C7.13583 22.6959 0 33.1022 0 43.7063C0 50.6442 2.97294 57.383 8.32479 62.2396C7.82933 64.3209 7.53183 66.4021 7.53183 68.483C7.53183 82.6551 19.0285 93.2601 32.3092 93.2601C34.9847 93.2601 37.5616 92.8642 40.1385 91.9717C44.5979 96.3326 50.7429 99.1076 57.4825 99.1076Z" fill="currentColor" />
                  </svg>
                </a>
              
                <a target="_blank" rel="noopener noreferrer" aria-label="Ask Claude about Zencoder" class="cursor-pointer rounded-full px-3 py-1.5 transition-colors text-muted-foreground hover:text-secondary-foreground flex items-center justify-center" href="https://claude.ai/new?q=What+is+Zencoder+and+how+does+it+help+developers+code+faster%3F+Summarize+https%3A%2F%2Fzencoder.ai">
                  <svg aria-hidden="true" class="w-4 h-4" viewbox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M19.6203 66.4812L39.2911 55.4516L39.6203 54.4903L39.2911 53.959H38.3291L35.038 53.7566L23.7975 53.4531L14.0506 53.0483L4.6076 52.5424L2.22785 52.0364L0 49.1019L0.227848 47.6347L2.22785 46.294L5.08861 46.5469L11.4177 46.977L20.9114 47.6347L27.7975 48.0395L38 49.1019H39.6203L39.8481 48.4442L39.2911 48.0395L38.8608 47.6347L29.038 40.9815L18.4051 33.9489L12.8354 29.9013L9.82278 27.8523L8.3038 25.9297L7.64557 21.7303L10.3797 18.72L14.0506 18.9729L14.9873 19.2259L18.7089 22.0845L26.6582 28.2317L37.038 35.8715L38.557 37.1364L39.1646 36.7063L39.2405 36.4027L38.557 35.2644L32.9114 25.0696L26.8861 14.6977L24.2025 10.3972L23.4937 7.81685C23.2405 6.75436 23.0633 5.86896 23.0633 4.78118L26.1772 0.556539L27.8987 0L32.0506 0.556539L33.7975 2.07437L36.3797 7.96863L40.557 17.2527L47.038 29.876L48.9367 33.62L49.9494 37.0858L50.3291 38.1482H50.9873V37.5411L51.519 30.4326L52.5063 21.705L53.4684 10.4731L53.7975 7.3109L55.3671 3.51632L58.481 1.46724L60.9114 2.63091L62.9114 5.4895L62.6329 7.3362L61.443 15.0519L59.1139 27.1439L57.5949 35.2391H58.481L59.4937 34.2272L63.5949 28.7883L70.481 20.1872L73.519 16.7721L77.0633 13.0028L79.3418 11.2067H83.6456L86.8101 15.912L85.3924 20.769L80.962 26.385L77.2911 31.1409L72.0253 38.2241L68.7342 43.8907L69.038 44.3461L69.8228 44.2702L81.7215 41.7405L88.1519 40.5768L95.8228 39.2613L99.2911 40.8803L99.6709 42.5247L98.3038 45.8892L90.1013 47.913L80.481 49.8356L66.1519 53.2254L65.9747 53.3519L66.1772 53.6049L72.6329 54.212L75.3924 54.3638H82.1519L94.7342 55.2998L98.0253 57.4753L100 60.1315L99.6709 62.1553L94.6076 64.7356L87.7721 63.1166L71.8228 59.322L66.3544 57.956H65.5949V58.4113L70.1519 62.8637L78.5063 70.4022L88.962 80.1164L89.4937 82.5196L88.1519 84.4169L86.7342 84.2145L77.5443 77.3084L74 74.1968L65.9747 67.4425H65.443V68.1508L67.2911 70.8576L77.0633 85.53L77.5696 90.0329L76.8608 91.5001L74.3291 92.3855L71.5443 91.8796L65.8228 83.8604L59.9241 74.8292L55.1646 66.7341L54.5823 67.063L51.7722 97.2932L50.4557 98.8363L47.4177 100L44.8861 98.0774L43.5443 94.9658L44.8861 88.8186L46.5063 80.7994L47.8228 74.4245L49.0127 66.5065L49.7215 63.8755L49.6709 63.6985L49.0886 63.7744L43.1139 71.9707L34.0253 84.2398L26.8354 91.9302L25.1139 92.6132L22.1266 91.0701L22.4051 88.3127L24.0759 85.8588L34.0253 73.2102L40.0253 65.3681L43.8987 60.8399L43.8734 60.1821H43.6456L17.2152 77.3337L12.5063 77.9408L10.481 76.0435L10.7342 72.932L11.6962 71.9201L19.6456 66.4559L19.6203 66.4812Z" fill="currentColor" />
                  </svg>
                </a>
              
                <a target="_blank" rel="noopener noreferrer" aria-label="Ask Perplexity about Zencoder" class="cursor-pointer rounded-full px-3 py-1.5 transition-colors text-muted-foreground hover:text-secondary-foreground flex items-center justify-center" href="https://www.perplexity.ai/search?q=What+is+Zencoder+and+how+does+it+help+developers+code+faster%3F+Summarize+https%3A%2F%2Fzencoder.ai">
                  <svg aria-hidden="true" class="w-4 h-4" viewbox="0 0 86 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M85.9451 29.9462H74.1376V0L45.3625 26.8123V0H40.5825V26.8123L11.8076 0V29.9462H0V73.0925H11.7759V100L40.5825 74.3587V100H45.3625V74.3587L74.1689 100V73.0925H85.9451V29.9462ZM69.3258 11.0161V29.9462H49.0345L69.3258 11.0161ZM16.5876 11.0161L36.8787 29.9462H16.5876V11.0161ZM4.78 68.3125V34.7578H36.8154L11.7759 57.7714V68.3125H4.81169H4.78ZM16.5559 59.8607L40.5825 37.7968V67.9644L16.5559 89.3319V59.8607ZM69.3576 89.3319L45.3308 67.9644V37.7968L69.3576 59.8607V89.3319ZM81.1332 68.3125H74.1689V57.7714L49.1295 34.7578H81.1651V68.3125H81.1332Z" fill="currentColor" />
                  </svg>
                </a>
              
                <a target="_blank" rel="noopener noreferrer" aria-label="Ask Gemini about Zencoder" class="cursor-pointer rounded-full px-3 py-1.5 transition-colors text-muted-foreground hover:text-secondary-foreground flex items-center justify-center" href="https://www.google.com/search?udm=50&amp;aep=11&amp;q=What+is+Zencoder+and+how+does+it+help+developers+code+faster%3F+Summarize+https%3A%2F%2Fzencoder.ai">
                  <svg aria-hidden="true" class="w-4 h-4" viewbox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M50.0001 0C51.0487 0 51.9608 0.716212 52.2166 1.73358C53.0009 4.84542 54.024 7.88069 55.2971 10.8334C58.6134 18.5376 63.1637 25.2811 68.9419 31.0586C74.7219 36.8359 81.4625 41.3866 89.1669 44.703C92.1219 45.976 95.155 46.9991 98.2662 47.7834C99.2837 48.0392 100 48.9514 100 50.0001C100 51.0487 99.2837 51.9609 98.2662 52.2166C95.155 53.0009 92.1194 54.024 89.1669 55.2971C81.4625 58.6136 74.7187 63.1637 68.9419 68.9419C63.1637 74.7219 58.6136 81.4625 55.2971 89.1669C54.024 92.1219 53.0009 95.155 52.2166 98.2662C51.9609 99.2837 51.0487 100 50.0001 100C48.9514 100 48.0392 99.2837 47.7834 98.2662C46.9991 95.155 45.976 92.1194 44.703 89.1669C41.3866 81.4625 36.8387 74.7187 31.0586 68.9419C25.2781 63.1637 18.5376 58.6134 10.8334 55.2971C7.87788 54.024 4.84542 53.0009 1.73358 52.2166C0.716212 51.9608 0 51.0487 0 50.0001C0 48.9514 0.7163 48.0392 1.73358 47.7834C4.84543 46.9991 7.88069 45.9762 10.8334 44.703C18.5378 41.3864 25.2811 36.8361 31.0586 31.0586C36.8361 25.2811 41.3864 18.5378 44.703 10.8334C45.9762 7.87788 46.9991 4.84543 47.7834 1.73358C48.0392 0.7163 48.9514 0 50.0001 0Z" fill="currentColor" />
                  </svg>
                </a>
              
                <a target="_blank" rel="noopener noreferrer" aria-label="Ask Grok about Zencoder" class="cursor-pointer rounded-full px-3 py-1.5 transition-colors text-muted-foreground hover:text-secondary-foreground flex items-center justify-center" href="https://grok.com/?q=What+is+Zencoder+and+how+does+it+help+developers+code+faster%3F+Summarize+https%3A%2F%2Fzencoder.ai">
                  <svg aria-hidden="true" class="w-4 h-4" viewbox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M38.6218 64.1904L71.8668 38.596C73.4968 37.3413 75.8263 37.8307 76.6031 39.7798C80.69 50.0583 78.8642 62.4108 70.7321 70.8916C62.6 79.3723 51.285 81.2325 40.9429 76.9963L29.6451 82.4518C45.8495 94.0028 65.5268 91.1464 77.8232 78.3137C87.5763 68.1416 90.5974 54.2765 87.7726 41.7732L87.7984 41.7998C83.7021 23.4318 88.8053 16.0899 99.2584 1.07681C99.5058 0.720841 99.7532 0.364869 100.001 0L86.2453 14.3456V14.3011L38.6134 64.1992" fill="currentColor" /><path d="M31.7604 70.4102C20.1297 58.8231 22.1349 40.8911 32.0589 30.5504C39.3974 22.8969 51.4206 19.7733 61.9163 24.3653L73.1884 18.9367C71.1579 17.4061 68.5553 15.7597 65.5684 14.6028C52.0693 8.80939 35.9074 11.6927 24.9338 23.1283C14.3783 34.1366 11.0589 51.063 16.7591 65.5067C21.0171 76.3016 14.037 83.937 7.00568 91.6437C4.51402 94.3756 2.01381 97.108 0 100L31.7517 70.419" fill="currentColor" />
                  </svg>
                </a>
              
            </div>
          </div>
        </div>
      
      </div>
    </div>
  </div>
  
  <div role="complementary" aria-label="Accessibility Information">
    <div id="accessibility-help-content" class="sr-only">
      <h2>Accessibility Screen-Reader Guide, Feedback, and Issue Reporting</h2>
      <p>This website is designed to be accessible to all users, including those using screen readers and other assistive technologies.</p>
    </div>
  </div>
</footer></div></div>
    

    <script defer src="https://cdn.jsdelivr.net/npm/@alpinejs/collapse@3.14.8/dist/cdn.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.14.8/dist/cdn.min.js"></script>

    

    <script>
      (function () {
        var load = function () {
          var s = document.createElement('script');
          s.src = 'https://kit.fontawesome.com/ef6cb0bdd9.js';
          s.crossOrigin = 'anonymous';
          s.defer = true;
          document.head.appendChild(s);
        };
        if ('requestIdleCallback' in window) {
          requestIdleCallback(load, { timeout: 2000 });
        } else {
          window.addEventListener('load', function () { setTimeout(load, 200); });
        }
      })();
    </script>

    
<!-- HubSpot performance collection script -->
<script defer src="/hs/hsstatic/content-cwv-embed/static-1.1293/embed.js"></script>
<script defer src="//zencoder.ai/hubfs/hub_generated/template_assets/1/184211210880/1784045155848/template_script-main.min.js"></script>
<script>
var hsVars = hsVars || {}; hsVars['language'] = 'en-us';
</script>

<script src="/hs/hsstatic/cos-i18n/static-1.53/bundles/project.js"></script>
<script src="//zencoder.ai/hubfs/hub_generated/module_assets/1/185251510178/1788971510946/module_global-navigation.min.js"></script>


<!-- Start of HubSpot Analytics Code -->
<script type="text/javascript">
var _hsq = _hsq || [];
_hsq.push(["setContentType", "blog-post"]);
_hsq.push(["setCanonicalUrl", "http:\/\/zencoder.ai\/blog\/create-api-in-python"]);
_hsq.push(["setPageId", "182979991932"]);
_hsq.push(["setContentMetadata", {
    "contentPageId": 182979991932,
    "legacyPageId": "182979991932",
    "contentFolderId": null,
    "contentGroupId": 167002545819,
    "abTestId": null,
    "languageVariantId": 182979991932,
    "languageCode": "en-us",
    
    
}]);
</script>

<script type="text/javascript" id="hs-script-loader" async defer src="/hs/scriptloader/46014728.js"></script>
<!-- End of HubSpot Analytics Code -->


<script type="text/javascript">
var hsVars = {
    render_id: "cfcb458c-55bf-4c74-84ee-8aaa33bbde00",
    ticks: 1788971793292,
    page_id: 182979991932,
    
    content_group_id: 167002545819,
    portal_id: 46014728,
    app_hs_base_url: "https://app.hubspot.com",
    cp_hs_base_url: "https://cp.hubspot.com",
    language: "en-us",
    analytics_page_type: "blog-post",
    scp_content_type: "",
    
    analytics_page_id: "182979991932",
    category_id: 3,
    folder_id: 0,
    is_hubspot_user: false
}
</script>


<script defer src="/hs/hsstatic/HubspotToolsMenu/static-1.640/js/index.js"></script>

<script>
(function () {
  function loadAcsb() {
    // prevent multiple injections
    if (window._acsbLoaded) return;
    window._acsbLoaded = true;
    var s = document.createElement('script');
    s.src = 'https://acsbapp.com/apps/app/dist/js/app.js';
    s.async = true;
    s.onload = function () {
      window.acsbJS && window.acsbJS.init();
    };
    document.head.appendChild(s);
  }

  // Load the accessibility script after the page's load event
  window.addEventListener('load', function () {
    // Use requestIdleCallback if supported to run during idle time
    if ('requestIdleCallback' in window) {
      requestIdleCallback(loadAcsb, { timeout: 2000 });
    } else {
      // Fallback: queue the task with a zero‑delay timeout
      setTimeout(loadAcsb, 0);
    }
  }, { once: true });
})();
</script>

<div id="fb-root"></div>
  <script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
  fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));</script> <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="https://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
 


  
</body></html>