








<!doctype html>
<html 
      lang="en"
      dir="ltr">
  <head>
    <meta name="google-signin-client-id" content="157101835696-ooapojlodmuabs2do2vuhhnf90bccmoi.apps.googleusercontent.com"><meta name="google-signin-scope"
          content="profile email https://www.googleapis.com/auth/developerprofiles https://www.googleapis.com/auth/developerprofiles.award https://www.googleapis.com/auth/devprofiles.full_control.firstparty"><meta property="og:site_name" content="Google AI for Developers">
    <meta property="og:type" content="website"><meta name="theme-color" content="#1967d2"><meta charset="utf-8">
    <meta content="IE=Edge" http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    

    <link rel="manifest" href="/_pwa/googledevai/manifest.json"
          crossorigin="use-credentials">
    <link rel="preconnect" href="//www.gstatic.com" crossorigin>
    <link rel="preconnect" href="//fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="//www.google-analytics.com" crossorigin><link rel="stylesheet" href="//fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700|Inter:400,500|Inter+Tight:300,500,600&display=swap">
      <link rel="stylesheet"
            href="//fonts.googleapis.com/css2?family=Material+Icons&family=Material+Symbols+Outlined&display=block"><link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/css/app.css">
      
        <link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/css/dark-theme.css" disabled>
      <link rel="shortcut icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/favicon-new.png">
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq" /><title>Interactions API: Breaking changes migration guide (May 2026) &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Interactions API: Breaking changes migration guide (May 2026) &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta name="description" content="Guide for migrating to upcoming breaking changes in the Interactions API, including the steps schema and response format changes.">
  <meta property="og:description" content="Guide for migrating to upcoming breaking changes in the Interactions API, including the steps schema and response format changes."><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675"><meta property="og:locale" content="en"><meta name="twitter:card" content="summary_large_image">
  

  

  

  


    </head>
  <body class="gemini-api color-scheme--light"
        template="page"
        theme="googledevai-theme"
        type="article"
        
        appearance
        
        layout="docs"
        
        
        
        
        
        display-toc
        pending>
  
    <devsite-progress type="indeterminate" id="app-progress"></devsite-progress>
  
  
    <a href="#main-content" class="skip-link button">
      
      Skip to main content
    </a>
    <section class="devsite-wrapper">
      <devsite-cookie-notification-bar></devsite-cookie-notification-bar>
        <devsite-header role="banner" keep-tabs-visible>
  
    





















<div class="devsite-header--inner" data-nosnippet>
  <div class="devsite-top-logo-row-wrapper-wrapper">
    <div class="devsite-top-logo-row-wrapper">
      <div class="devsite-top-logo-row">
        <button type="button" id="devsite-hamburger-menu"
          class="devsite-header-icon-button button-flat material-icons gc-analytics-event"
          data-category="Site-Wide Custom Events"
          data-label="Navigation menu button"
          visually-hidden
          aria-label="Open menu">
        </button>
        
<div class="devsite-product-name-wrapper">

  <a href="/" class="devsite-site-logo-link gc-analytics-event"
   data-category="Site-Wide Custom Events" data-label="Site logo" track-type="globalNav"
   track-name="geminiAPI" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://ai.google.dev/_static/googledevai/images/gemini-api-logo-dark-theme.svg"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg" class="devsite-site-logo" alt="Gemini API">
  </picture>
  
</a>



  
  
  <span class="devsite-product-name">
    <ul class="devsite-breadcrumb-list"
  >
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
      
    
  </li>
  
</ul>
  </span>

</div>
        <div class="devsite-top-logo-row-middle">
          <div class="devsite-header-upper-tabs">
            
           </div>
          
<devsite-search
    enable-signin
    enable-search
    enable-suggestions
      enable-query-completion
    
    enable-search-summaries
    project-name="Gemini API"
    tenant-name="Google AI for Developers"
    project-scope="/gemini-api"
    url-scoped="https://ai.google.dev/s/results/gemini-api"
    
    
    
    >
  <form class="devsite-search-form" action="https://ai.google.dev/s/results" method="GET">
    <div class="devsite-search-container">
      <button type="button"
              search-open
              class="devsite-search-button devsite-header-icon-button button-flat material-icons"
              
              aria-label="Open search"></button>
      <div class="devsite-searchbox">
        <input
          aria-activedescendant=""
          aria-autocomplete="list"
          
          aria-label="Search"
          aria-expanded="false"
          aria-haspopup="listbox"
          autocomplete="off"
          class="devsite-search-field devsite-search-query"
          name="q"
          
          placeholder="Search"
          role="combobox"
          type="text"
          value=""
          >
          <div class="devsite-search-image material-icons" aria-hidden="true">
            
              <svg class="devsite-search-ai-image" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <g clip-path="url(#clip0_6641_386)">
                    <path d="M19.6 21L13.3 14.7C12.8 15.1 12.225 15.4167 11.575 15.65C10.925 15.8833 10.2333 16 9.5 16C7.68333 16 6.14167 15.375 4.875 14.125C3.625 12.8583 3 11.3167 3 9.5C3 7.68333 3.625 6.15 4.875 4.9C6.14167 3.63333 7.68333 3 9.5 3C10.0167 3 10.5167 3.05833 11 3.175C11.4833 3.275 11.9417 3.43333 12.375 3.65L10.825 5.2C10.6083 5.13333 10.3917 5.08333 10.175 5.05C9.95833 5.01667 9.73333 5 9.5 5C8.25 5 7.18333 5.44167 6.3 6.325C5.43333 7.19167 5 8.25 5 9.5C5 10.75 5.43333 11.8167 6.3 12.7C7.18333 13.5667 8.25 14 9.5 14C10.6667 14 11.6667 13.625 12.5 12.875C13.35 12.1083 13.8417 11.15 13.975 10H15.975C15.925 10.6333 15.7833 11.2333 15.55 11.8C15.3333 12.3667 15.05 12.8667 14.7 13.3L21 19.6L19.6 21ZM17.5 12C17.5 10.4667 16.9667 9.16667 15.9 8.1C14.8333 7.03333 13.5333 6.5 12 6.5C13.5333 6.5 14.8333 5.96667 15.9 4.9C16.9667 3.83333 17.5 2.53333 17.5 0.999999C17.5 2.53333 18.0333 3.83333 19.1 4.9C20.1667 5.96667 21.4667 6.5 23 6.5C21.4667 6.5 20.1667 7.03333 19.1 8.1C18.0333 9.16667 17.5 10.4667 17.5 12Z" fill="#5F6368"/>
                  </g>
                <defs>
                <clipPath id="clip0_6641_386">
                <rect width="24" height="24" fill="white"/>
                </clipPath>
                </defs>
              </svg>
            
          </div>
          <div class="devsite-search-shortcut-icon-container" aria-hidden="true">
            <kbd class="devsite-search-shortcut-icon">/</kbd>
          </div>
      </div>
    </div>
  </form>
  <button type="button"
          search-close
          class="devsite-search-button devsite-header-icon-button button-flat material-icons"
          
          aria-label="Close search"></button>
</devsite-search>

        </div>

        

          

          

          

          <devsite-appearance-selector></devsite-appearance-selector>

          
<devsite-language-selector>
  <ul role="presentation">
    
    
    <li role="presentation">
      <a role="menuitem" lang="en"
        >English</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="de"
        >Deutsch</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="es_419"
        >Español – América Latina</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fr"
        >Français</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="id"
        >Indonesia</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="it"
        >Italiano</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pl"
        >Polski</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="sq"
        >Shqip</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="vi"
        >Tiếng Việt</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="tr"
        >Türkçe</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ru"
        >Русский</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="he"
        >עברית</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ar"
        >العربيّة</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fa"
        >فارسی</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="hi"
        >हिंदी</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="bn"
        >বাংলা</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="th"
        >ภาษาไทย</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_cn"
        >中文 – 简体</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_tw"
        >中文 – 繁體</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ja"
        >日本語</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ko"
        >한국어</a>
    </li>
    
  </ul>
</devsite-language-selector>


          
            <a class="devsite-header-link devsite-top-button button gc-analytics-event "
    href="https://aistudio.google.com/apikey"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Get API key"
    
      
        target="_blank"
      
    >
  Get API key
</a>
          
            <a class="devsite-header-link devsite-top-button button gc-analytics-event "
    href="https://github.com/google-gemini/cookbook"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Cookbook"
    
      
        target="_blank"
      
    >
  Cookbook
</a>
          
            <a class="devsite-header-link devsite-top-button button gc-analytics-event "
    href="https://discuss.ai.google.dev/c/gemini-api/"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Community"
    
      
        target="_blank"
      
    >
  Community
</a>
          

        

        
          <devsite-user 
                        
                        
                          enable-profiles
                        
                        
                        id="devsite-user">
            
              
              <span class="button devsite-top-button" aria-hidden="true" visually-hidden>Sign in</span>
            
          </devsite-user>
        
        
        
      </div>
    </div>
  </div>



  <div class="devsite-collapsible-section
    ">
    <div class="devsite-header-background">
      
        
      
      
        <div class="devsite-doc-set-nav-row">
          
          
            
            
  <devsite-tabs class="lower-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Lower tabs">
      
        
          <tab  class="devsite-active">
            
    <a href="https://ai.google.dev/gemini-api/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://ai.google.dev/gemini-api/docs"
    
       track-type="nav"
       track-metadata-position="nav - docs"
       track-metadata-module="primary nav"
       aria-label="Docs, selected" 
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Docs"
         
           track-name="docs"
         
       >
    Docs
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://ai.google.dev/api"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://ai.google.dev/api"
    
       track-type="nav"
       track-metadata-position="nav - api reference"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: API reference"
         
           track-name="api reference"
         
       >
    API reference
  
    </a>
    
  
          </tab>
        
      
    </nav>

  </devsite-tabs>

          
          
        </div>
      
    </div>
  </div>

</div>



  

  
</devsite-header>
        <devsite-book-nav scrollbars >
          
            





















<div class="devsite-book-nav-filter"
     hidden>
  <span class="filter-list-icon material-icons" aria-hidden="true"></span>
  <input type="text"
         placeholder="Filter"
         
         aria-label="Type to filter"
         role="searchbox">
  
  <span class="filter-clear-button hidden"
        data-title="Clear filter"
        aria-label="Clear filter"
        role="button"
        tabindex="0"></span>
</div>

<nav class="devsite-book-nav devsite-nav nocontent" data-nosnippet
     aria-label="Side menu">
  <div class="devsite-mobile-header">
    <button type="button"
            id="devsite-close-nav"
            class="devsite-header-icon-button button-flat material-icons gc-analytics-event"
            data-category="Site-Wide Custom Events"
            data-label="Close navigation"
            aria-label="Close navigation">
    </button>
    <div class="devsite-product-name-wrapper">

  <a href="/" class="devsite-site-logo-link gc-analytics-event"
   data-category="Site-Wide Custom Events" data-label="Site logo" track-type="globalNav"
   track-name="geminiAPI" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://ai.google.dev/_static/googledevai/images/gemini-api-logo-dark-theme.svg"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg" class="devsite-site-logo" alt="Gemini API">
  </picture>
  
</a>


  
      <span class="devsite-product-name">
        
        
        <ul class="devsite-breadcrumb-list"
  >
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
      
    
  </li>
  
</ul>
      </span>
    

</div>
  </div>

  <div class="devsite-book-nav-wrapper">
    <div class="devsite-mobile-nav-top">
      
        <ul class="devsite-nav-list">
          
            <li class="devsite-nav-item">
              
  
  <a href="/gemini-api/docs"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Gemini API"
      
        track-name="gemini api"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Gemini API"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Gemini API
   </span>
    
  
  </a>
  

  
              
                <ul class="devsite-nav-responsive-tabs">
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/gemini-api/docs"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Docs"
      
        track-name="docs"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Docs"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip menu="_book">
      Docs
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/api"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: API reference"
      
        track-name="api reference"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: API reference"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      API reference
   </span>
    
  
  </a>
  

  
                    </li>
                  
                </ul>
              
            </li>
          
          
    
    
<li class="devsite-nav-item">

  
  <a href="https://aistudio.google.com/apikey"
    
       class="devsite-nav-title gc-analytics-event "
    

    
      
        target="_blank"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Get API key"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Get API key
   </span>
    
  
  </a>
  

</li>

  
    
    
<li class="devsite-nav-item">

  
  <a href="https://github.com/google-gemini/cookbook"
    
       class="devsite-nav-title gc-analytics-event "
    

    
      
        target="_blank"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Cookbook"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Cookbook
   </span>
    
  
  </a>
  

</li>

  
    
    
<li class="devsite-nav-item">

  
  <a href="https://discuss.ai.google.dev/c/gemini-api/"
    
       class="devsite-nav-title gc-analytics-event "
    

    
      
        target="_blank"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Community"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Community
   </span>
    
  
  </a>
  

</li>

  
          
        </ul>
      
    </div>
    
      <div class="devsite-mobile-nav-bottom">
        
          
          <ul class="devsite-nav-list" menu="_book">
            <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Get started</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/get-started"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/api-key"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>API keys</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/pricing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Pricing</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/coding-agents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Coding agent setup</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Models</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/models"
        class="devsite-nav-title"
      
        alt-paths=" /gemini-api/docs/models/gemini-3.1-flash-image /gemini-api/docs/models/gemini-3.1-flash-lite-image /gemini-api/docs/models/gemini-3.1-pro-preview /gemini-api/docs/models/gemini-3-pro-preview /gemini-api/docs/models/gemini-3-pro-image /gemini-api/docs/models/gemini-3.7-flash /gemini-api/docs/models/gemini-3.6-flash /gemini-api/docs/models/gemini-3.5-flash /gemini-api/docs/models/gemini-3.5-live-translate-preview /gemini-api/docs/models/gemini-3-flash-preview /gemini-api/docs/models/gemini-3.1-flash-tts-preview /gemini-api/docs/models/veo-3.1-lite-generate-preview /gemini-api/docs/models/gemini-3.1-flash-live-preview /gemini-api/docs/models/gemini-3.5-flash-lite /gemini-api/docs/models/gemini-3.1-flash-lite /gemini-api/docs/models/gemini-3.1-flash-lite-preview /gemini-api/docs/models/gemini-2.5-flash /gemini-api/docs/models/gemini-2.5-flash-preview-09-2025 /gemini-api/docs/models/gemini-2.5-flash-image /gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025 /gemini-api/docs/models/gemini-2.5-flash-preview-tts /gemini-api/docs/models/gemini-2.5-flash-lite /gemini-api/docs/models/gemini-2.5-flash-lite-preview-09-2025 /gemini-api/docs/models/gemini-2.5-pro /gemini-api/docs/models/gemini-2.5-pro-preview-tts /gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025 /gemini-api/docs/models/gemini-2.0-flash /gemini-api/docs/models/gemini-2.0-flash-lite /gemini-api/docs/models/imagen /gemini-api/docs/models/veo-3.1-generate-preview /gemini-api/docs/models/veo-2.0-generate-001 /gemini-api/docs/models/gemini-embedding-001 /gemini-api/docs/models/gemini-embedding-2 /gemini-api/docs/models/gemini-robotics-er-1.5-preview /gemini-api/docs/models/gemini-robotics-er-2-preview /gemini-api/docs/models/gemini-robotics-er-2-streaming-preview /gemini-api/docs/models/gemini-robotics-er-1.6-preview /gemini-api/docs/models/deep-research-pro-preview-12-2025 /gemini-api/docs/models/deep-research-preview-04-2026 /gemini-api/docs/models/deep-research-max-preview-04-2026 /gemini-api/docs/models/antigravity-preview-05-2026 /gemini-api/docs/models/lyria-realtime-exp /gemini-api/docs/models/lyria-3-clip-preview /gemini-api/docs/models/lyria-3-pro-preview /gemini-api/docs/models/gemini-omni-flash /gemini-api/docs/models/gemini-3.5-transcribe "><span class="devsite-nav-text" tooltip>All models</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/latest-model"
        class="devsite-nav-title"
      
        alt-paths=" /gemini-api/docs/whats-new-gemini-3.5 "><span class="devsite-nav-text" tooltip>Latest Gemini models</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/image-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Nano Banana</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/veo"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Veo</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/omni"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini Omni Flash</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/music-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Lyria 3</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/realtime-music-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Lyria RealTime</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/imagen"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Imagen</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/speech-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Text-to-speech</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/transcribe"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Transcribe</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Live</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/live-translate"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Live translate</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/embeddings"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Embeddings</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Robotics</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/robotics-overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/robotics-spatial"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Spatial reasoning</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/robotics-agentic"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Agentic vision</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/robotics-orchestration"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Task orchestration</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/robotics-streaming"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Robotics with streaming</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/robotics-video-progress"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Video understanding</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Core capabilities</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/text-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Text</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Image</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/image-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Image generation 🍌</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/image-understanding"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Image understanding</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Video</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/video"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Video overview</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/video-understanding"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Video understanding</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/document-processing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Documents</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Speech and audio</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/speech-generation"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Speech generation</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/audio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Audio understanding</span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/transcribe"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Audio transcription</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Thinking</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/thinking"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Thinking</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/thought-signatures"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Thought signatures</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/structured-output"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Structured outputs</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/function-calling"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Function calling</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/long-context"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Long context</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Agents</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/agents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/managed-agents-quickstart"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Quickstart</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/antigravity-agent"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Antigravity agent</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/custom-agents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Building managed agents</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/agent-environment"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Environments</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/agent-hooks"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Hooks</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/deep-research"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Deep Research agent</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Tools</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/tools"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/google-search"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Google Search</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/maps-grounding"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Google Maps</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/code-execution"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Code execution</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/url-context"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>URL context</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/computer-use"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Computer use</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/file-search"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>File search</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/tool-combination"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Combine tools and function calling</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Live API</span>
      </div></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/live-api"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Get started</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/get-started-sdk"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started using the GenAI SDK</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/get-started-websocket"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started using raw WebSockets</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/capabilities"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Capabilities</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/live-transcribe"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Live transcription</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/live-translate"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Live translation</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/tools"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Tool use</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/session-management"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Session management</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/live-api/ephemeral-tokens"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Ephemeral tokens</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/live-api/best-practices"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Best practices</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Optimization</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/optimization"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/batch-api"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Batch API</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/webhooks"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Webhooks</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/flex-inference"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Flex inference</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini-api/docs/priority-inference"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Priority inference</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/caching"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Context caching</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Guides</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/interactions-overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Interactions API</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/streaming"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Streaming</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/background-execution"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Background execution</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>File input</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/file-input-methods"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Input methods</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/files"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Files API</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/openai"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>OpenAI compatibility</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/media-resolution"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Media resolution</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/tokens"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Token counting</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/prompting-strategies"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Prompt engineering</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Logs and datasets</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/logs-datasets"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started with logs</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/logs-policy"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Data logging and sharing</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Safety</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/safety-settings"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Safety settings</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/safety-guidance"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Safety guidance</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Frameworks</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/langgraph-example"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>LangChain &amp; LangGraph</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/crewai-example"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>CrewAI</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/llama-index"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>LlamaIndex</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/vercel-ai-sdk-example"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Vercel AI SDK</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/temporal-example"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Temporal</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Resources</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/changelog"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Release notes</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/deprecations"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Deprecations</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/libraries"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Libraries</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Migration</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/migrate"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Migrate to Gen AI SDK</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/migrate-to-interactions"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Migrate to Interactions API</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/interactions-breaking-changes-may-2026"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Interactions breaking changes (May 2026)</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/rate-limits"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Rate limits</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/billing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Billing info</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/troubleshooting"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>API troubleshooting</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/api-errors"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>API errors</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-external"><a href="https://aistudio.google.com/status"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Status</span><span class="devsite-nav-icon material-icons"
        data-icon="external"
        data-title="External"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/partner-integration"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Partner and library integrations</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Google AI Studio</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/ai-studio-quickstart"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Quickstart</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/google-ai-plans"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Google AI plans</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-build-mode"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Vibe code in Build mode</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-fullstack"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Developing full-stack apps</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-android"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Build Android apps</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-deploying"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Deploying your app</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/aistudio-agents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Agents in AI Studio Playground</span></a></li><li class="devsite-nav-item
           devsite-nav-experimental"><a href="/gemini-api/docs/learnlm"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Try out LearnLM</span><span class="devsite-nav-icon material-icons"
        data-icon="experimental"
        data-title="Experimental!"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/troubleshoot-ai-studio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Troubleshooting</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/workspace"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Access for Workspace users</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Google Cloud Platform</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini-api/docs/migrate-to-cloud"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini Enterprise Agent Platform Gemini API</span></a></li><li class="devsite-nav-item"><a href="/gemini-api/docs/oauth"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>OAuth authentication</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Policies</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini-api/terms"
        class="devsite-nav-title"
      
        alt-paths=" /gemini-api/docs/zdr "><span class="devsite-nav-text" tooltip>Terms of service</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/available-regions"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Available regions</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/usage-policies"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Abuse monitoring</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/feedback-policies"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Feedback information</span></a></li>
          </ul>
        
        
          
    
  
        
        
          
    
  
    
  
        
      </div>
    
  </div>
</nav>
          
        </devsite-book-nav>
      
      <section id="gc-wrapper">
        <main role="main" id="main-content" class="devsite-main-content"
            
              has-book-nav
              has-sidebar
            >
          <div class="devsite-sidebar">
            <div class="devsite-sidebar-content">
                
                <devsite-toc class="devsite-nav"
                            role="navigation"
                            aria-label="On this page"
                            depth="2"
                            scrollbars
                            data-nosnippet
                  ></devsite-toc>
                <devsite-recommendations-sidebar class="nocontent devsite-nav" data-nosnippet>
                </devsite-recommendations-sidebar>
            </div>
          </div>
          <devsite-content>
            
              










<article class="devsite-article">
  
  
  
    <div class="devsite-banner devsite-banner-announcement nocontent" data-nosnippet
      
        
    background="google-blue"
  
      >
      <div class="devsite-banner-message">
        <div class="devsite-banner-message-text">
          Gemini 3.7 Flash is now available. <a href="https://aistudio.google.com/prompts/new_chat?model=gemini-3.7-flash" style="color: black;">Try it out</a>.
        </div>
      </div>
    </div>
  
  
  

  <div class="devsite-article-meta nocontent" role="navigation" data-nosnippet>
    
    
    <ul class="devsite-breadcrumb-list"
  
    aria-label="Breadcrumb">
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://ai.google.dev/"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail=""
      
    >
    
          Home
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://ai.google.dev/gemini-api"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="2"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="2"
      
        track-metadata-eventdetail="Gemini API"
      
    >
    
          Gemini API
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://ai.google.dev/gemini-api/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="3"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="3"
      
        track-metadata-eventdetail=""
      
    >
    
          Docs
        
  </a>
  
      
    
  </li>
  
</ul>
    
      
    <devsite-thumb-rating position="header">
    </devsite-thumb-rating>
  
    
    <devsite-gemini-api-switcher class="nocontent"></devsite-gemini-api-switcher>
  </div>
  
    <devsite-feedback
  position="header"
  project-name="Gemini API"
  product-id="5292923"
  bucket="documentation"
  context=""
  version="t-devsite-webserver-20260825-r00-rc00.479916215664864412"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="header"
  class="nocontent"
  data-nosnippet
  
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"
  
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
  
    <h1 class="devsite-page-title" tabindex="-1">
      Interactions API: Breaking changes migration guide (May 2026)<devsite-actions hidden data-nosnippet>
    <devsite-llm-tools></devsite-llm-tools></devsite-actions>
  
      
    </h1>
  <div class="devsite-page-title-meta"><devsite-view-release-notes></devsite-view-release-notes></div>
  

  <devsite-toc class="devsite-nav"
    depth="2"
    devsite-toc-embedded
    >
  </devsite-toc>
  
    
  <div class="devsite-article-body clearfix
  ">

  
    
    
<p>
</p>



























































<aside class="caution" style="margin: 20px 0;">
  <p><strong>Breaking changes</strong>: The changes described in this guide are
  breaking changes to the Interactions API. The legacy schema will be
  removed on <strong>June 8, 2026</strong>. Use the
  <code translate="no" dir="ltr">Api-Revision</code> request header to
  <a href="#how-to-migrate">manage your migration</a>.</p>
</aside>

<p>The <code translate="no" dir="ltr">v1beta</code> Interactions API is introducing breaking changes that restructure the
API shape to support future capabilities like mid-flight steering and
asynchronous tool calls. This page explains what&#39;s changing and provides
before-and-after code examples to help you migrate. There are two categories
of changes:</p>

<ol>
<li><a href="#steps-schema"><strong>Steps schema</strong></a>: A new <code translate="no" dir="ltr">steps</code> array replaces the
<code translate="no" dir="ltr">outputs</code> array, providing a structured timeline of each interaction turn.</li>
<li><a href="#output-format-config"><strong>Output format configuration</strong></a>: A new polymorphic
<code translate="no" dir="ltr">response_format</code> consolidates all output format controls and removes
<code translate="no" dir="ltr">response_mime_type</code>.</li>
</ol>

<p>Follow the steps in <a href="#how-to-migrate">How to migrate to the new schema</a> to
update your integration.</p>

<h2 id="steps-schema" data-text="Core change: outputs to steps" tabindex="-1">Core change: <code translate="no" dir="ltr">outputs</code> to <code translate="no" dir="ltr">steps</code></h2>

<p>The new schema replaces the <code translate="no" dir="ltr">outputs</code> array with a <code translate="no" dir="ltr">steps</code> array.</p>

<ul>
<li><strong>Legacy</strong>: Responses returned a flat <code translate="no" dir="ltr">outputs</code> array containing only the model&#39;s generated content.</li>
<li><strong>New schema</strong>: Responses return a <code translate="no" dir="ltr">steps</code> array containing structured steps with type discriminators.</li>
</ul>

<p><code translate="no" dir="ltr">POST /interactions</code> returns only output steps. <code translate="no" dir="ltr">GET /interactions/{id}</code>
returns the full step timeline, including the initial <code translate="no" dir="ltr">user_input</code> step.</p>

<h3 id="basic-unary" data-text="Basic input/output (unary)" tabindex="-1">Basic input/output (unary)</h3>

<h4 id="before_legacy" data-text="Before (legacy)" tabindex="-1">Before (legacy)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Request</span>
<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Tell me a joke."</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># Response access</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">outputs</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-o">-</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Request</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Tell me a joke.'</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-c1">// Response access</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">outputs</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-o">-</span><span class="devsite-syntax-mf">1</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="rest" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Tell me a joke."</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="reStructuredText"><code translate="no" dir="ltr">// Response
{
  "id": "int_123",
  "role": "model",
  <strong>"outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]</strong>
}
</code></pre></devsite-code></section>
</devsite-selector></div>
<h4 id="after_new_schema" data-text="After (new schema)" tabindex="-1">After (new schema)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Request</span>
<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Tell me a joke."</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># Response access (Recommended sugar)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Request</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Tell me a joke.'</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-c1">// Response access (Recommended sugar)</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code><aside class="note"><strong>Note:</strong><span> For details on SDK convenience properties (including <code translate="no" dir="ltr">.output_text</code>,
<code translate="no" dir="ltr">.output_image</code>, and <code translate="no" dir="ltr">.output_audio</code>), see
[Access outputs with SDK convenience properties][sdk-convenience]
in the overview.</span></aside>
<p>[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar</p></section>
<section><h3 id="rest_1" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Opt-in needed before May 26th</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span><strong>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Api-Revision: 2026-05-20"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span></strong>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Tell me a joke."</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="reStructuredText"><code translate="no" dir="ltr">// POST Response
{
  "id": "int_123",
  <strong>"steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]</strong>
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="function-calling" data-text="Function calling" tabindex="-1">Function calling</h3>

<p>The request structure remains unchanged, but the response replaces the flat
<code translate="no" dir="ltr">outputs</code> content with structured steps.</p>

<h4 id="before_legacy_2" data-text="Before (legacy)" tabindex="-1">Before (legacy)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Accessing function call in legacy schema</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">output</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">outputs</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">output</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Calling </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">output</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2"> with </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">output</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">arguments</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Accessing function call in legacy schema</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">outputs</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'function_call'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Calling </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb"> with </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arguments</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_2" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Response</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_001"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"requires_action"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"outputs"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"signature"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"abc123..."</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"fc_1"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"arguments"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"location"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Boston, MA"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h4 id="after_new_schema_2" data-text="After (new schema)" tabindex="-1">After (new schema)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_3" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Accessing function call in new steps schema</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Calling </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2"> with </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">arguments</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_3" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Accessing function call in new steps schema</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'function_call'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Calling </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb"> with </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arguments</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_3" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// POST Response</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_001"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"requires_action"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"summary"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"I need to check the weather in Boston..."</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"signature"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"abc123..."</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"fc_1"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"arguments"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"location"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Boston, MA"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="server-side-tools" data-text="Server-side tools" tabindex="-1">Server-side tools</h3>

<p>Server-side tools (like Google Search or Code Execution) now yield specific
step types in the <code translate="no" dir="ltr">steps</code> array. While the legacy schema returned these
operations as specific content types within the <code translate="no" dir="ltr">outputs</code> array, the new schema
moves them into the <code translate="no" dir="ltr">steps</code> array. The following examples use Google Search.</p>

<h4 id="before_legacy_3" data-text="Before (legacy)" tabindex="-1">Before (legacy)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_4" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Accessing search results in legacy schema</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">output</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">outputs</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">output</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"google_search_call"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Searched for: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">output</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">arguments</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">queries</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">output</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"google_search_result"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Found results: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">output</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">rendered_content</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_4" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Accessing search results in legacy schema</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">outputs</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'google_search_call'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Searched for: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arguments</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">queries</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'google_search_result'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Found results: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">renderedContent</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_4" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Who won the last Super Bowl?",</span>
<span class="devsite-syntax-s1">    "tools": [</span>
<span class="devsite-syntax-s1">      { "type": "google_search" }</span>
<span class="devsite-syntax-s1">    ]</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="reStructuredText"><code translate="no" dir="ltr">// Response
{
  "id": "int_456",
  <strong>"outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "&lt;div&gt;...&lt;/div&gt;",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ]</strong>,
  "status": "completed"
}
</code></pre></devsite-code></section>
</devsite-selector></div>
<h4 id="after_new_schema_3" data-text="After (new schema)" tabindex="-1">After (new schema)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_5" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Accessing search results in new steps schema</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"google_search_call"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Searched for: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">arguments</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">queries</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"google_search_result"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Found results: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">search_suggestions</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_5" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Accessing search results in new steps schema</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'google_search_call'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Searched for: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arguments</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">queries</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'google_search_result'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Found results: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">search_suggestions</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_5" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Opt-in needed before May 26th</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span><strong>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Api-Revision: 2026-05-20"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span></strong>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Who won the last Super Bowl?",</span>
<span class="devsite-syntax-s1">    "tools": [</span>
<span class="devsite-syntax-s1">      { "type": "google_search" }</span>
<span class="devsite-syntax-s1">    ]</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="reStructuredText"><code translate="no" dir="ltr">// POST Response
{
  "id": "int_456",
  <strong>"steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "&lt;div&gt;...&lt;/div&gt;"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ]</strong>,
  "status": "completed"
}
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="streaming" data-text="Streaming" tabindex="-1">Streaming</h3>

<p>Streaming exposes new event types:</p>

<h4 id="event-types" data-text="New event types" tabindex="-1">New event types</h4>

<ul>
<li><code translate="no" dir="ltr">interaction.created</code></li>
<li><code translate="no" dir="ltr">interaction.completed</code></li>
<li><code translate="no" dir="ltr">interaction.in_progress</code></li>
<li><code translate="no" dir="ltr">interaction.requires_action</code></li>
<li><code translate="no" dir="ltr">step.start</code></li>
<li><code translate="no" dir="ltr">step.delta</code></li>
<li><code translate="no" dir="ltr">step.stop</code></li>
</ul>

<h4 id="deprecated-event-types" data-text="Deprecated event types" tabindex="-1">Deprecated event types</h4>

<p>The following legacy event types are replaced by the new events listed above:</p>

<ul>
<li><code translate="no" dir="ltr">interaction.start</code> → <code translate="no" dir="ltr">interaction.created</code></li>
<li><code translate="no" dir="ltr">content.start</code> → <code translate="no" dir="ltr">step.start</code></li>
<li><code translate="no" dir="ltr">content.delta</code> → <code translate="no" dir="ltr">step.delta</code></li>
<li><code translate="no" dir="ltr">content.stop</code> → <code translate="no" dir="ltr">step.stop</code></li>
<li><code translate="no" dir="ltr">interaction.complete</code> → <code translate="no" dir="ltr">interaction.completed</code></li>
<li><code translate="no" dir="ltr">interaction.status_update</code> → replaced by <code translate="no" dir="ltr">interaction.in_progress</code>, <code translate="no" dir="ltr">interaction.requires_action</code>, etc.</li>
</ul>

<p><strong>Streaming function calls</strong>: When you use streaming with function calling,
the <code translate="no" dir="ltr">step.start</code> event delivers the function name, and <code translate="no" dir="ltr">step.delta</code> events
stream the arguments as partial JSON strings (using <code translate="no" dir="ltr">arguments_delta</code>). You
must accumulate these deltas to get the full arguments. This differs from
unary calls where you receive the complete function call object at once.</p>

<h4 id="streaming-examples" data-text="Examples" tabindex="-1">Examples</h4>

<h5 id="before_legacy_4" data-text="Before (Legacy)" tabindex="-1">Before (Legacy)</h5>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_6" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Legacy streaming used content.delta</span>
<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Explain quantum entanglement in simple terms."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">chunk</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"content.delta"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_6" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Legacy streaming used content.delta</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Explain quantum entanglement in simple terms.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chunk</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">chunk</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'content.delta'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">chunk</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">chunk</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_6" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Explain quantum entanglement in simple terms.",</span>
<span class="devsite-syntax-s1">    "stream": true</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="reStructuredText"><code translate="no" dir="ltr">// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
</code></pre></devsite-code></section>
</devsite-selector></div>
<h5 id="after_new_schema_4" data-text="After (New Schema)" tabindex="-1">After (New Schema)</h5>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_7" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Consuming stream and handling new event types</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Tell me a story."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">):</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">:</span>  <span class="devsite-syntax-c1"># CHANGED: step.delta instead of content.delta</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_7" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Consuming stream and handling new event types</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Tell me a story.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'step.delta'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// CHANGED: step.delta instead of content.delta</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_7" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-w"> </span><strong><span class="devsite-syntax-c1"># Opt-in needed before May 26th</span></strong>
<span class="devsite-syntax-w"> </span>curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">   </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">   </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Accept: text/event-stream"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">   </span><strong>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Api-Revision: 2026-05-20"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span></strong>
<span class="devsite-syntax-w">   </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">     "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">     "input": "Tell me a story.",</span>
<span class="devsite-syntax-s1">     "stream": true</span>
<span class="devsite-syntax-s1">   }'</span>
</code></pre></devsite-code><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="reStructuredText"><code translate="no" dir="ltr"> // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.7-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="stateless-history" data-text="Stateless Conversation History" tabindex="-1">Stateless Conversation History</h3>

<p>If you manage conversation history manually on the client side (stateless use
case), you must update how you string along previous turns.</p>

<ul>
<li><strong>Legacy</strong>: Developers often collected the <code translate="no" dir="ltr">outputs</code> array from responses and sent them back in the <code translate="no" dir="ltr">input</code> field on the next turn.</li>
<li><strong>New schema</strong>: You should now collect the <code translate="no" dir="ltr">steps</code> array from the response and pass it in the <code translate="no" dir="ltr">input</code> field of the next request, appending your new user turn as a <code translate="no" dir="ltr">user_input</code> step.</li>
</ul>

<h2 id="output-format-config" data-text="Output format configuration: response_format changes" tabindex="-1">Output format configuration: <code translate="no" dir="ltr">response_format</code> changes</h2>

<p>The updated API consolidates all output format controls into a unified,
polymorphic <code translate="no" dir="ltr">response_format</code> field. This centralizes output configuration at
the top level and keeps <code translate="no" dir="ltr">generation_config</code> focused on model behavior (like
temperature, top_p, and thinking).</p>

<h3 id="response-format-changes" data-text="Key changes" tabindex="-1">Key changes</h3>

<ul>
<li><strong>The API removes <code translate="no" dir="ltr">response_mime_type</code>.</strong> You now specify the MIME type
per format entry inside <code translate="no" dir="ltr">response_format</code>.</li>
<li><strong><code translate="no" dir="ltr">response_format</code> is now a polymorphic object (or array).</strong> Each
entry has a <code translate="no" dir="ltr">type</code> discriminator (<code translate="no" dir="ltr">text</code>, <code translate="no" dir="ltr">audio</code>, <code translate="no" dir="ltr">image</code>) and
type-specific fields. To request multiple output modalities, pass an
array of format entries.</li>
<li><strong><code translate="no" dir="ltr">image_config</code> moves from <code translate="no" dir="ltr">generation_config</code> to <code translate="no" dir="ltr">response_format</code>.</strong>
You now specify image output settings like <code translate="no" dir="ltr">aspect_ratio</code> and <code translate="no" dir="ltr">image_size</code>
in a <code translate="no" dir="ltr">response_format</code> entry with <code translate="no" dir="ltr">&quot;type&quot;: &quot;image&quot;</code>.</li>
</ul>

<h3 id="structured-output" data-text="Structured output (JSON)" tabindex="-1">Structured output (JSON)</h3>

<p>The new schema removes the <code translate="no" dir="ltr">response_mime_type</code> field. Instead, specify the
MIME type and JSON schema inside a <code translate="no" dir="ltr">response_format</code> object with
<code translate="no" dir="ltr">&quot;type&quot;: &quot;text&quot;</code>.</p>

<h4 id="before_legacy_5" data-text="Before (legacy)" tabindex="-1">Before (legacy)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_8" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Summarize this article."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">response_mime_type</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"application/json"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">response_format</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"properties"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"summary"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">outputs</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-o">-</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_8" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Summarize this article.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">response_mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'application/json'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">response_format</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'object'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">properties</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">summary</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'string'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">outputs</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-o">-</span><span class="devsite-syntax-mf">1</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_8" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Summarize this article.",</span>
<span class="devsite-syntax-s1">    "response_mime_type": "application/json",</span>
<span class="devsite-syntax-s1">    "response_format": {</span>
<span class="devsite-syntax-s1">      "type": "object",</span>
<span class="devsite-syntax-s1">      "properties": {</span>
<span class="devsite-syntax-s1">        "summary": { "type": "string" }</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h4 id="after_new_schema_5" data-text="After (new schema)" tabindex="-1">After (new schema)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_9" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Summarize this article."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-c1"># response_mime_type is removed — specify mime_type inside response_format</span>
    <span class="devsite-syntax-n">response_format</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"application/json"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"schema"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"properties"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"summary"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">}</span>
            <span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># Print response</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_9" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Summarize this article.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-c1">// response_mime_type is removed — specify mime_type inside response_format</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">response_format</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'application/json'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">schema</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'object'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">properties</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">summary</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'string'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-c1">// Print response</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_9" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Opt-in needed before May 26th</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span><strong>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Api-Revision: 2026-05-20"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span></strong>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Summarize this article.",</span>
<span class="devsite-syntax-s1">    "response_format": {</span>
<span class="devsite-syntax-s1">      "type": "text",</span>
<span class="devsite-syntax-s1">      "mime_type": "application/json",</span>
<span class="devsite-syntax-s1">      "schema": {</span>
<span class="devsite-syntax-s1">        "type": "object",</span>
<span class="devsite-syntax-s1">        "properties": {</span>
<span class="devsite-syntax-s1">          "summary": { "type": "string" }</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="image-config" data-text="Image configuration" tabindex="-1">Image configuration</h3>

<p>The new schema removes <code translate="no" dir="ltr">image_config</code> from <code translate="no" dir="ltr">generation_config</code>. You now specify
image output settings in a <code translate="no" dir="ltr">response_format</code> entry with <code translate="no" dir="ltr">&quot;type&quot;: &quot;image&quot;</code>.</p>

<h4 id="before_legacy_6" data-text="Before (legacy)" tabindex="-1">Before (legacy)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_10" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Generate an image of a sunset over the ocean."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">generation_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"image_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"aspect_ratio"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"1:1"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"image_size"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"1K"</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_10" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Generate an image of a sunset over the ocean.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generation_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">image_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">aspect_ratio</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'1:1'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">image_size</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'1K'</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_10" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Generate an image of a sunset over the ocean.",</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "image_config": {</span>
<span class="devsite-syntax-s1">        "aspect_ratio": "1:1",</span>
<span class="devsite-syntax-s1">        "image_size": "1K"</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h4 id="after_new_schema_6" data-text="After (new schema)" tabindex="-1">After (new schema)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_11" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Generate an image of a sunset over the ocean."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-c1"># image_config is removed from generation_config — use response_format</span>
    <span class="devsite-syntax-n">response_format</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"image"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"image/jpeg"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"aspect_ratio"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"1:1"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"image_size"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"1K"</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_11" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Generate an image of a sunset over the ocean.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-c1">// image_config is removed from generation_config — use response_format</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">response_format</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'image'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'image/jpeg'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">aspect_ratio</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'1:1'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">image_size</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'1K'</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_11" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Opt-in needed before May 26th</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span><strong>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Api-Revision: 2026-05-20"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span></strong>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Generate an image of a sunset over the ocean.",</span>
<span class="devsite-syntax-s1">    "response_format": {</span>
<span class="devsite-syntax-s1">      "type": "image",</span>
<span class="devsite-syntax-s1">      "mime_type": "image/jpeg",</span>
<span class="devsite-syntax-s1">      "aspect_ratio": "1:1",</span>
<span class="devsite-syntax-s1">      "image_size": "1K"</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="audio-config" data-text="Audio configuration" tabindex="-1">Audio configuration</h3>

<p>The new schema replaces <code translate="no" dir="ltr">response_modalities: [&quot;audio&quot;]</code> with a <code translate="no" dir="ltr">response_format</code> entry of <code translate="no" dir="ltr">&quot;type&quot;: &quot;audio&quot;</code>.</p>

<h4 id="before_legacy_7" data-text="Before (legacy)" tabindex="-1">Before (legacy)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_12" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.1-flash-tts-preview"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Say cheerfully: Have a wonderful day!"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">generation_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"speech_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
            <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"voice"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Kore"</span><span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">]</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_12" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.1-flash-tts-preview'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Say cheerfully: Have a wonderful day!'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">response_modalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'audio'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generation_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">speech_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">voice</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Kore'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_12" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.1-flash-tts-preview",</span>
<span class="devsite-syntax-s1">    "input": "Say cheerfully: Have a wonderful day!",</span>
<span class="devsite-syntax-s1">    "response_modalities": ["audio"],</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "speech_config": [</span>
<span class="devsite-syntax-s1">        { "voice": "Kore" }</span>
<span class="devsite-syntax-s1">      ]</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h4 id="after_new_schema_7" data-text="After (new schema)" tabindex="-1">After (new schema)</h4>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_13" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.1-flash-tts-preview"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Say cheerfully: Have a wonderful day!"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-c1"># response_modalities is removed — use response_format</span>
    <span class="devsite-syntax-n">response_format</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"audio"</span>
    <span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-n">generation_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"speech_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
            <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"voice"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Kore"</span><span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">]</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_13" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.1-flash-tts-preview'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Say cheerfully: Have a wonderful day!'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-c1">// response_modalities is removed — use response_format</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">response_format</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'audio'</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generation_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">speech_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">voice</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Kore'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_13" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Opt-in needed before May 26th</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Api-Revision: 2026-05-20"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.1-flash-tts-preview",</span>
<span class="devsite-syntax-s1">    "input": "Say cheerfully: Have a wonderful day!",</span>
<span class="devsite-syntax-s1">    "response_format": {</span>
<span class="devsite-syntax-s1">      "type": "audio"</span>
<span class="devsite-syntax-s1">    },</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "speech_config": [</span>
<span class="devsite-syntax-s1">        { "voice": "Kore" }</span>
<span class="devsite-syntax-s1">      ]</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>To request multiple output modalities (for example, text and audio together),
pass an array of format entries to <code translate="no" dir="ltr">response_format</code> instead of a single
object.</p>

<h2 id="how-to-migrate" data-text="How to migrate to the new schema" tabindex="-1">How to migrate to the new schema</h2>

<h3 id="sdk-users" data-text="SDK users" tabindex="-1">SDK users</h3>

<p>Upgrade to the latest SDK version (Python ≥2.0.0, JavaScript ≥2.0.0). The
SDK automatically opts you into the new schema — no code changes needed beyond
updating how you read responses (see examples above). Note that only the new
schema is supported in these SDK versions. Older SDK versions
(Python 1.x.x, JavaScript 1.x.x) will continue to work until the legacy
schema is removed on <strong>June 8, 2026</strong>.</p>

<h3 id="raw-api-users" data-text="REST API users" tabindex="-1">REST API users</h3>

<p>Add the <code translate="no" dir="ltr">Api-Revision: 2026-05-20</code> header to your requests to opt in to
the new schema now. After <strong>May 26</strong>, the new schema becomes the default for all
requests. You can temporarily opt out with <code translate="no" dir="ltr">Api-Revision: 2026-05-07</code>
until <strong>June 8</strong>, when the API permanently removes the legacy schema.</p>

<h3 id="timeline" data-text="Timeline" tabindex="-1">Timeline</h3>

<table>
<thead>
<tr>
<th>Date</th>
<th>Phase</th>
<th>SDK users</th>
<th>REST API users</th>
</tr>
</thead>

<tbody>
<tr>
<td><strong>May 7</strong></td>
<td>Opt-in</td>
<td>New SDK version available (Python ≥2.0.0, JS ≥2.0.0). Upgrade to get the new schema automatically.</td>
<td>Add <code translate="no" dir="ltr">Api-Revision: 2026-05-20</code> header to opt in. Default remains legacy.</td>
</tr>
<tr>
<td><strong>May 26</strong></td>
<td>Default flip</td>
<td>No action needed if already upgraded. Older SDKs (Python 1.x.x, JS 1.x.x) still work but return legacy responses.</td>
<td>New schema is now the default. Send <code translate="no" dir="ltr">Api-Revision: 2026-05-07</code> header to opt out.</td>
</tr>
<tr>
<td><strong>June 8</strong></td>
<td>Sunset</td>
<td>Python 1.x.x and JS 1.x.x SDK versions will break for Interactions API calls.</td>
<td>Legacy schema removed for Interactions API. <code translate="no" dir="ltr">Api-Revision</code> header ignored.</td>
</tr>
</tbody>
</table>

<aside class="note" style="margin: 20px 0;">
  <p><strong>Note</strong>: New features shipped after May 7 will only
  appear in <code translate="no" dir="ltr">steps</code> responses. Users on the legacy <code translate="no" dir="ltr">outputs</code>
  schema will not receive new capabilities until they migrate.</p>
</aside>

<h2 id="migration-checklist" data-text="Migration Checklist" tabindex="-1">Migration Checklist</h2>

<h3 id="steps_schema_steps" data-text="Steps schema (steps)" tabindex="-1">Steps schema (<code translate="no" dir="ltr">steps</code>)</h3>

<ul>
<li>Update code to read response content from the <code translate="no" dir="ltr">steps</code> array instead of <code translate="no" dir="ltr">outputs</code>. <a href="#basic-unary">See examples</a>.</li>
<li>Verify that your code handles both <code translate="no" dir="ltr">user_input</code> and <code translate="no" dir="ltr">model_output</code> step types. <a href="#basic-unary">See examples</a>.</li>
<li>(Function Calling) Update code to find <code translate="no" dir="ltr">function_call</code> steps in the <code translate="no" dir="ltr">steps</code> array. <a href="#function-calling">See examples</a>.</li>
<li>(Server-Side Tools) Update code to handle tool-specific steps (e.g., <code translate="no" dir="ltr">google_search_call</code>, <code translate="no" dir="ltr">google_search_result</code>). <a href="#server-side-tools">See examples</a>.</li>
<li>(Stateless History) Update history management to pass the <code translate="no" dir="ltr">steps</code> array in the <code translate="no" dir="ltr">input</code> field of the next request. <a href="#stateless-history">See details</a>.</li>
<li>(Streaming only) Update client to listen for new SSE event types (<code translate="no" dir="ltr">interaction.created</code>, <code translate="no" dir="ltr">step.delta</code>, etc.). <a href="#streaming">See examples</a>.</li>
</ul>

<h3 id="output_format_configuration_response_format" data-text="Output format configuration (response_format)" tabindex="-1">Output format configuration (<code translate="no" dir="ltr">response_format</code>)</h3>

<ul>
<li>Replace <code translate="no" dir="ltr">response_mime_type</code> with a <code translate="no" dir="ltr">mime_type</code> field inside <code translate="no" dir="ltr">response_format</code>. <a href="#structured-output">See examples</a>.</li>
<li>Wrap your existing <code translate="no" dir="ltr">response_format</code> JSON schema inside a <code translate="no" dir="ltr">{&quot;type&quot;: &quot;text&quot;, &quot;schema&quot;: ...}</code> object. <a href="#structured-output">See examples</a>.</li>
<li>(Image Generation) Move <code translate="no" dir="ltr">image_config</code> from <code translate="no" dir="ltr">generation_config</code> to a <code translate="no" dir="ltr">{&quot;type&quot;: &quot;image&quot;, ...}</code> entry in <code translate="no" dir="ltr">response_format</code>. <a href="#image-config">See examples</a>.</li>
<li>(Speech Generation) Replace <code translate="no" dir="ltr">response_modalities=[&quot;audio&quot;]</code> with a <code translate="no" dir="ltr">{&quot;type&quot;: &quot;audio&quot;}</code> entry in <code translate="no" dir="ltr">response_format</code>. <a href="#audio-config">See examples</a>.</li>
<li>(Multimodal) Convert <code translate="no" dir="ltr">response_format</code> from a single object to an array when requesting multiple output modalities.</li>
</ul>
<link href="https://fonts.googleapis.com/css2?family=Google+Symbols:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet" data-page-link>
  

  
</div>

  
    
    
      
    <devsite-thumb-rating position="footer">
    </devsite-thumb-rating>
  
       
         <devsite-feedback
  position="footer"
  project-name="Gemini API"
  product-id="5292923"
  bucket="documentation"
  context=""
  version="t-devsite-webserver-20260825-r00-rc00.479916215664864412"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="footer"
  class="nocontent"
  data-nosnippet
  
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"
  
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
       
    
    
  

  <div class="devsite-floating-action-buttons"></div></article>


<devsite-content-footer class="nocontent" data-nosnippet>
  <p>Except as otherwise noted, the content of this page is licensed under the <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 License</a>, and code samples are licensed under the <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a>. For details, see the <a href="https://developers.google.com/site-policies">Google Developers Site Policies</a>. Java is a registered trademark of Oracle and/or its affiliates.</p>
  <p>Last updated 2026-08-17 UTC.</p>
</devsite-content-footer>


<devsite-notification
>
</devsite-notification>


  
<div class="devsite-content-data">
  
    
    
    
  
  
    
  
</div>
            
          </devsite-content>
        </main>
        <devsite-footer-promos class="devsite-footer">
          
            
          
        </devsite-footer-promos>
        <devsite-footer-linkboxes class="devsite-footer">
          
            
<nav class="devsite-footer-linkboxes nocontent"
     aria-label="Footer links"
     data-nosnippet>
  
</nav>
          
        </devsite-footer-linkboxes>
        <devsite-footer-utility class="devsite-footer">
          
            

<div class="devsite-footer-utility nocontent" data-nosnippet>
  

  
  <nav class="devsite-footer-utility-links" aria-label="Utility links">
    
    <ul class="devsite-footer-utility-list">
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/terms"
           data-category="Site-Wide Custom Events"
           data-label="Footer Terms link"
         >
          Terms
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/privacy"
           data-category="Site-Wide Custom Events"
           data-label="Footer Privacy link"
         >
          Privacy
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 glue-cookie-notification-bar-control">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="#"
           data-category="Site-Wide Custom Events"
           data-label="Footer Manage cookies link"
         
           aria-hidden="true"
         >
          Manage cookies
        </a>
        
      </li>
      
    </ul>
    
    
<devsite-language-selector>
  <ul role="presentation">
    
    
    <li role="presentation">
      <a role="menuitem" lang="en"
        >English</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="de"
        >Deutsch</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="es_419"
        >Español – América Latina</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fr"
        >Français</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="id"
        >Indonesia</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="it"
        >Italiano</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pl"
        >Polski</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="sq"
        >Shqip</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="vi"
        >Tiếng Việt</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="tr"
        >Türkçe</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ru"
        >Русский</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="he"
        >עברית</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ar"
        >العربيّة</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fa"
        >فارسی</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="hi"
        >हिंदी</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="bn"
        >বাংলা</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="th"
        >ภาษาไทย</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_cn"
        >中文 – 简体</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_tw"
        >中文 – 繁體</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ja"
        >日本語</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ko"
        >한국어</a>
    </li>
    
  </ul>
</devsite-language-selector>

  </nav>
</div>
          
        </devsite-footer-utility>
        <devsite-panel>
          
        </devsite-panel>
        
      </section>
      </section>
    <devsite-sitemask></devsite-sitemask>
    <devsite-snackbar></devsite-snackbar>
    <devsite-tooltip ></devsite-tooltip>
    <devsite-heading-link></devsite-heading-link>
    <devsite-analytics>
      
        

      
    </devsite-analytics>
    
      <devsite-badger></devsite-badger>
    
    
    
    


    <devsite-a11y-announce></devsite-a11y-announce>
  </body>
</html>