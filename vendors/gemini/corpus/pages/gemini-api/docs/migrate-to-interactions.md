








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=sq" /><title>Migrating to the Interactions API &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Migrating to the Interactions API &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta name="description" content="Guide for migrating from generateContent to the Interactions API.">
  <meta property="og:description" content="Guide for migrating from generateContent to the Interactions API."><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/migrate-to-interactions"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
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
      Migrating to the Interactions API<devsite-actions hidden data-nosnippet>
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



























































<p>This guide helps you migrate from the <code translate="no" dir="ltr">generateContent</code> API to the Interactions API.</p>

<p>The Interactions API is our simplest and best way to build with Gemini models and agents. While <code translate="no" dir="ltr">generateContent</code> remains fully supported, we recommend the Interactions API for all new development.</p>

<aside class="note">
  <p><strong>Automate this migration with a coding agent.</strong> If you use
  a coding agent that supports skills (like Gemini CLI or Jules), install the
  <a href="/gemini-api/docs/coding-agents#gemini-interactions-api">Gemini
  Interactions API skill</a> and run:</p>
  <div></div><devsite-code><pre translate="no" dir="ltr" is-upgraded>/gemini-interactions-api migrate my app to the interactions api</pre></devsite-code>
  <p>The skill applies the API changes described in this guide.</p>
</aside>

<h3 id="why_migrate" data-text="Why migrate?" tabindex="-1">Why migrate?</h3>

<p>The Interactions API is our simplest and best way to build with Gemini models and agents:</p>

<ul>
<li><strong>Server-side history management</strong>: Simplified multi-turn flows via <code translate="no" dir="ltr">previous_interaction_id</code>. The server enables state by default (<code translate="no" dir="ltr">store=true</code>), but you can opt into stateless behavior by setting <code translate="no" dir="ltr">store=false</code>.</li>
<li><strong>Observable execution steps</strong>: Typed steps make it easy to debug complex flows and render UI for intermediate events (like thoughts or search widgets).</li>
<li><strong>Tool use and agentic workflows</strong>: Native support for multi-step tool use, orchestration, and complex reasoning flows through typed execution steps.</li>
<li><strong>Long-running and background tasks</strong>: Supports offloading time-intensive operations like Deep Think and Deep Research to background processes using <code translate="no" dir="ltr">background=true</code>.</li>
</ul>

<h2 id="basic-input-output" data-text="Basic input/output" tabindex="-1">Basic input/output</h2>

<p>This section shows how to migrate a simple text generation request.</p>

<h3 id="before_generatecontent" data-text="Before (generateContent)" tabindex="-1">Before (<code translate="no" dir="ltr">generateContent</code>)</h3>

<p>The <code translate="no" dir="ltr">generateContent</code> API is stateless and returns the response directly. The response structure wraps the output in a list of <code translate="no" dir="ltr">candidates</code>, each containing <code translate="no" dir="ltr">content</code> with a list of <code translate="no" dir="ltr">parts</code> to parse.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Tell me a joke."</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Tell me a joke."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"contents"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Tell me a joke."</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"candidates"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Why did the chicken cross the road? To get to the other side!"</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"finishReason"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"STOP"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</strong>,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"usageMetadata"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"promptTokenCount"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">4</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"candidatesTokenCount"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">12</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"totalTokenCount"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">16</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>The Interactions API returns a stored interaction resource with a <code translate="no" dir="ltr">steps</code>
timeline. While you can inspect the <code translate="no" dir="ltr">steps</code> array manually to find intermediate
events, the Google GenAI SDKs provide convenience properties
directly on the returned <code translate="no" dir="ltr">Interaction</code> object to access the final output.</p>

<p>The most common convenience property is <strong><code translate="no" dir="ltr">.output_text</code></strong> (String), which
automatically extracts and joins consecutive <code translate="no" dir="ltr">TextContent</code> blocks at the
end of the model&#39;s response. While this works perfectly for simple responses,
it does not include earlier text blocks separated by non-text content (such
as thoughts, images, audio, or tool calls). For complex or interleaved
multimodal responses, you must manually iterate over <code translate="no" dir="ltr">steps</code> instead.</p>
<aside class="note"><strong>Note:</strong><span> For details on other SDK convenience properties (including <code translate="no" dir="ltr">.output_image</code>
and <code translate="no" dir="ltr">.output_audio</code>), see
<a href="/gemini-api/docs/interactions-overview#sdk-sugar">Access outputs with SDK convenience properties</a>
in the overview.</span></aside><div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Tell me a joke."</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Tell me a joke.'</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_1" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_1" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta2/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"input"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Tell me a joke."</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_123"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"completed"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"user_input"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Tell me a joke."</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Why did the chicken cross the road?"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="multi-turn-conversations" data-text="Multi-turn conversations" tabindex="-1">Multi-turn conversations</h2>

<p>The Interactions API stores interactions by default, enabling server-side state management for multi-turn conversations.</p>

<h3 id="before_generatecontent_2" data-text="Before (generateContent)" tabindex="-1">Before (<code translate="no" dir="ltr">generateContent</code>)</h3>

<p>In <code translate="no" dir="ltr">generateContent</code>, you must manually manage conversation history using the <code translate="no" dir="ltr">contents</code> array or a client-side chat helper.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text="Python" tabindex="-1">Python</h3><p><strong>Using the chat helper (recommended)</strong></p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">chat</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">chats</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-n">response1</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">chat</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_message</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Hi, my name is Phil."</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response1</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">response2</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">chat</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_message</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"What is my name?"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response2</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code>
<p><strong>Manually managing history</strong></p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Content</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">role</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"user"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">parts</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">from_text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Hi, my name is Phil."</span><span class="devsite-syntax-p">)]</span>
        <span class="devsite-syntax-p">),</span>
        <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Content</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">role</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"model"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-n">parts</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">from_text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Hi Phil, how can I help you?"</span><span class="devsite-syntax-p">)],</span>
        <span class="devsite-syntax-p">),</span>
        <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Content</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">role</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"user"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">parts</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">from_text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What is my name?"</span><span class="devsite-syntax-p">)]</span>
        <span class="devsite-syntax-p">),</span>
    <span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text="JavaScript" tabindex="-1">JavaScript</h3><p><strong>Using the chat helper (recommended)</strong></p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chat</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">chats</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-2.5-flash-lite'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chat</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendMessage</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Hi, my name is Phil.'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chat</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendMessage</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'What is my name?'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_2" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code>
<p><strong>Manually managing history</strong></p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-2.5-flash-lite'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">role</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'user'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Hi, my name is Phil.'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">role</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'model'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Hi Phil, how can I help you?'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">role</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'user'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'What is my name?'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_2" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">(</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">he</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">seco</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">turn</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">requires</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">se</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">di</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">g</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">he</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">e</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-err">ire</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">his</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">ory)</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"contents"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"user"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hi, my name is Phil."</span><span class="devsite-syntax-p">}]},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hi Phil, how can I help you?"</span><span class="devsite-syntax-p">}]},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"user"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What is my name?"</span><span class="devsite-syntax-p">}]}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"candidates"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Your name is Phil."</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"finishReason"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"STOP"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="after_interactions_api" data-text="After (Interactions API)" tabindex="-1">After (Interactions API)</h3>

<p>The Interactions API manages state on the server. You continue a conversation by referencing the <code translate="no" dir="ltr">previous_interaction_id</code>.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_3" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction1</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Hi, my name is Phil."</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Response 1:"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">interaction1</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">interaction2</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">previous_interaction_id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">interaction1</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What is my name?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Response 2:"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">interaction2</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_3" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Hi, my name is Phil.'</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Response 1:"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">previous_interaction_id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'What is my name?'</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Response 2:"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_3" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_3" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Firs</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta2/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"input"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hi, my name is Phil."</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Seco</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">(usi</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">g</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">ID</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">fr</span><span class="devsite-syntax-err">om</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">f</span><span class="devsite-syntax-err">irs</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">respo</span><span class="devsite-syntax-kc">nse</span><span class="devsite-syntax-err">)</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta2/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"previous_interaction_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_123"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"input"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What is my name?"</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">o</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Seco</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_123"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"user_input"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hi, my name is Phil."</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hello Phil! How can I help you today?"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"user_input"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What is my name?"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Your name is Phil."</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="multimodal-inputs" data-text="Multimodal inputs" tabindex="-1">Multimodal inputs</h2>

<p>Both APIs support multimodal inputs (text, images, video, etc.).</p>

<h3 id="before_generatecontent_3" data-text="Before (generateContent)" tabindex="-1">Before (<code translate="no" dir="ltr">generateContent</code>)</h3>

<p>In <code translate="no" dir="ltr">generateContent</code>, you pass a list of <code translate="no" dir="ltr">parts</code> within the <code translate="no" dir="ltr">contents</code> array. The response returns output in the <code translate="no" dir="ltr">parts</code> of the first candidate.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_4" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-k">with</span> <span class="devsite-syntax-nb">open</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"sample.jpg"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"rb"</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">f</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">image_bytes</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">f</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">read</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">from_bytes</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">image_bytes</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"image/jpeg"</span><span class="devsite-syntax-p">),</span>
        <span class="devsite-syntax-s2">"Describe this image."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_4" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">as</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'fs'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">imageBytes</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">readFileSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'sample.jpg'</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-nx">toString</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'base64'</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-2.5-flash-lite'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">inlineData</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">imageBytes</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'image/jpeg'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-s1">'Describe this image.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_4" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_4" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"contents"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"inlineData"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nt">"mimeType"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image/jpeg"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nt">"data"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Describe this image."</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"candidates"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"This is a picture of a beautiful sunset."</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="after_interactions_api_2" data-text="After (Interactions API)" tabindex="-1">After (Interactions API)</h3>

<p>In the Interactions API, you pass an array to the <code translate="no" dir="ltr">input</code> field. You retrieve output content by finding the <code translate="no" dir="ltr">model_output</code> step in the timeline.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_5" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">base64</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-k">with</span> <span class="devsite-syntax-nb">open</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"sample.jpg"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"rb"</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">f</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">image_bytes</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">f</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">read</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-n">image_b64</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">base64</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">b64encode</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">image_bytes</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">decode</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"utf-8"</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"image"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"image/jpeg"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"data"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">image_b64</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Describe this image."</span><span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_5" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">as</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'fs'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">imageBytes</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">readFileSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'sample.jpg'</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-nx">toString</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'base64'</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'image'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'image/jpeg'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">imageBytes</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Describe this image.'</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_5" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_5" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta2/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"input"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"mime_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image/jpeg"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"data"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Describe this image."</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_multimodal"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"user_input"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"mime_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image/jpeg"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"data"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Describe this image."</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"This is a picture of a beautiful sunset over the mountains."</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="structured_output" data-text="Structured output" tabindex="-1">Structured output</h2>

<p>To make the model return JSON matching a specific schema, configure the response format.</p>

<h3 id="before_generatecontent_4" data-text="Before (generateContent)" tabindex="-1">Before (<code translate="no" dir="ltr">generateContent</code>)</h3>

<p>In <code translate="no" dir="ltr">generateContent</code>, you configure output format using the <code translate="no" dir="ltr">response_mime_type</code> and <code translate="no" dir="ltr">response_schema</code> fields nested inside the <code translate="no" dir="ltr">config</code> (or <code translate="no" dir="ltr">generationConfig</code>) object.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_6" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">pydantic</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">BaseModel</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-k">class</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nc">Recipe</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">BaseModel</span><span class="devsite-syntax-p">):</span>
    <span class="devsite-syntax-n">recipe_name</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-nb">str</span>
    <span class="devsite-syntax-n">ingredients</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-nb">list</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nb">str</span><span class="devsite-syntax-p">]</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Give me a recipe for chocolate chip cookies."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">GenerateContentConfig</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">response_mime_type</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"application/json"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-n">response_schema</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">Recipe</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_6" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-2.5-flash-lite'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Give me a recipe for chocolate chip cookies.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">responseMimeType</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'application/json'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">responseSchema</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Type</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">OBJECT</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">properties</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">recipe_name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Type</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">STRING</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">ingredients</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Type</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">ARRAY</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">items</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Type</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">STRING</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">required</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'recipe_name'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'ingredients'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_6" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_6" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"contents"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Give me a recipe for chocolate chip cookies."</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"generationConfig"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"responseMimeType"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"application/json"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"responseSchema"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"OBJECT"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"properties"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"recipe_name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"STRING"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"ingredients"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"ARRAY"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nt">"items"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"STRING"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"required"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"recipe_name"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"ingredients"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"candidates"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="after_interactions_api_3" data-text="After (Interactions API)" tabindex="-1">After (Interactions API)</h3>

<p>In the Interactions API, output format controls move to a top-level <code translate="no" dir="ltr">response_format</code> array.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_7" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">pydantic</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">BaseModel</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-k">class</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nc">Recipe</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">BaseModel</span><span class="devsite-syntax-p">):</span>
    <span class="devsite-syntax-n">recipe_name</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-nb">str</span>
    <span class="devsite-syntax-n">ingredients</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-nb">list</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nb">str</span><span class="devsite-syntax-p">]</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Give me a recipe for chocolate chip cookies."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">response_format</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"application/json"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"schema"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">Recipe</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">model_json_schema</span><span class="devsite-syntax-p">(),</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_7" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Give me a recipe for chocolate chip cookies.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">response_format</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'application/json'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">schema</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'object'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">properties</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">recipe_name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'string'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">ingredients</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'array'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-nx">items</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'string'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">required</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'recipe_name'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'ingredients'</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_7" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_7" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta2/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"input"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Give me a recipe for chocolate chip cookies."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"response_format"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"mime_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"application/json"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"schema"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"OBJECT"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"properties"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nt">"recipe_name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"STRING"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nt">"ingredients"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"ARRAY"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-nt">"items"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"STRING"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"required"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"recipe_name"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"ingredients"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_structured"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"user_input"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Give me a recipe for chocolate chip cookies."</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="multimodal_generation" data-text="Multimodal generation" tabindex="-1">Multimodal generation</h2>

<p>When generating content in modalities beyond text (such as images or audio), the primary difference is how the response structures the generated media.</p>

<h3 id="before_generatecontent_5" data-text="Before (generateContent)" tabindex="-1">Before (<code translate="no" dir="ltr">generateContent</code>)</h3>

<p>In <code translate="no" dir="ltr">generateContent</code>, the response returns generated media directly in the <code translate="no" dir="ltr">parts</code> of the candidate, typically as base64 data in <code translate="no" dir="ltr">inlineData</code>.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">tru</span><span class="devsite-syntax-err">c</span><span class="devsite-syntax-kc">ture</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">co</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">cep</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"candidates"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Here is your generated image:"</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"inlineData"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"mimeType"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image/jpeg"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"data"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"...base64..."</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h3 id="after_interactions_api_4" data-text="After (Interactions API)" tabindex="-1">After (Interactions API)</h3>

<p>In the Interactions API, generated media appears as distinct items within the <code translate="no" dir="ltr">content</code> array of a <code translate="no" dir="ltr">model_output</code> step in the timeline, maintaining the chronological flow of the interaction.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">tru</span><span class="devsite-syntax-err">c</span><span class="devsite-syntax-kc">ture</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">co</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">cep</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_123"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Here is your generated image:"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"mime_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image/jpeg"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"data"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"...base64..."</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-c1">// Or a reference URL in future</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p>This keeps the response parsing consistent with how inputs and text outputs are handled—everything is a step in the timeline.</p>

<h2 id="server-side_tools" data-text="Server-side tools" tabindex="-1">Server-side tools</h2>

<p>Gemini supports built-in server-side tools like Google Search grounding. The primary difference is how the response represents tool execution.</p>

<h3 id="before_generatecontent_6" data-text="Before (generateContent)" tabindex="-1">Before (<code translate="no" dir="ltr">generateContent</code>)</h3>

<p>In <code translate="no" dir="ltr">generateContent</code>, server-side tools are largely opaque. You enable the tool and get a final answer with a separate <code translate="no" dir="ltr">groundingMetadata</code> object. Crucially, citations are not inline; <code translate="no" dir="ltr">groundingSupports</code> use character indices to map text segments back to web sources in <code translate="no" dir="ltr">groundingChunks</code>.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_8" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Who won Euro 2024?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">GenerateContentConfig</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-s2">"google_search"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{}}]</span>
    <span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">metadata</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">grounding_metadata</span>
<span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">metadata</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">search_entry_point</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Search Entry Point: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">metadata</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">search_entry_point</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">rendered_content</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">support</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">metadata</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">grounding_supports</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Citation: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">support</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">segment</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_8" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-2.5-flash-lite'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Who won Euro 2024?'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">google_search</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">metadata</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">groundingMetadata</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">metadata</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">searchEntryPoint</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Search Entry Point: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">metadata</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">searchEntryPoint</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">renderedContent</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">support</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">metadata</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">groundingSupports</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Citation: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">support</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">segment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_8" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_8" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"contents"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Who won Euro 2024?"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"tools"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"googleSearchRetrieval"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"candidates"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"groundingMetadata"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"webSearchQueries"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-s2">"UEFA Euro 2024 winner"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-s2">"who won euro 2024"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"searchEntryPoint"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"renderedContent"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"&lt;!-- HTML and CSS for the search widget --&gt;"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"groundingChunks"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"web"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"uri"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://vertexaisearch.cloud.google.com....."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"title"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"aljazeera.com"</span><span class="devsite-syntax-p">}},</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"web"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"uri"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://vertexaisearch.cloud.google.com....."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"title"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"uefa.com"</span><span class="devsite-syntax-p">}}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"groundingSupports"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"segment"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"startIndex"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"endIndex"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">85</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Spain won Euro 2024, defeatin..."</span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"groundingChunkIndices"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"segment"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"startIndex"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">86</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"endIndex"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">210</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"This victory marks Spain's..."</span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"groundingChunkIndices"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="after_interactions_api_5" data-text="After (Interactions API)" tabindex="-1">After (Interactions API)</h3>

<p>In the Interactions API, server-side tools provide full timeline transparency. The API records the call and result as distinct execution <code translate="no" dir="ltr">steps</code> (<code translate="no" dir="ltr">google_search_call</code> and <code translate="no" dir="ltr">google_search_result</code>), exposing exactly what data the model retrieved.</p>

<p>Furthermore, the API returns citations <strong>inline</strong>. Instead of mapping indices from a separate metadata object, the text item within the <code translate="no" dir="ltr">model_output</code> step contains its own <code translate="no" dir="ltr">annotations</code> array linking directly to the source.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_9" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Who won Euro 2024?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"google_search"</span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"google_search_result"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Search Suggestions: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">search_suggestions</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Answer: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">anno</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Citation: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">anno</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">title</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2"> (</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">anno</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">uri</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">)"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_9" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Who won Euro 2024?'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'google_search'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'google_search_result'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Search Suggestions: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">search_suggestions</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'model_output'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Answer: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">anno</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Citation: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">anno</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">title</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb"> (</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">anno</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">)`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_9" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_9" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta2/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"input"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Who won Euro 2024?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"tools"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"google_search"</span><span class="devsite-syntax-p">}]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">(showi</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">g</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">grou</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">di</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">g)</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_grounded"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"user_input"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Who won Euro 2024?"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"google_search_call"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"UEFA Euro 2024 winner"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"google_search_result"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Spain won Euro 2024..."</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Spain won Euro 2024, defeating England 2-1."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"annotations"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"start_index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"end_index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">42</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"uri"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://vertexaisearch..."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"title"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"aljazeera.com"</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="function_calling" data-text="Function calling" tabindex="-1">Function calling</h2>

<p>The structure of function calls and results has also changed to fit the Steps schema.</p>

<h3 id="before_generatecontent_7" data-text="Before (generateContent)" tabindex="-1">Before (<code translate="no" dir="ltr">generateContent</code>)</h3>

<p>In <code translate="no" dir="ltr">generateContent</code>, the response returns function calls within the candidates.*   {Python}</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-err">```</span><span class="devsite-syntax-n">python</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">GenerateContentConfig</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">weather_tool</span><span class="devsite-syntax-p">]),</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">function_call</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">parts</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">function_call</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Requested tool: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">function_call</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">result</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"52°F and rain"</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Content</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">role</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"user"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-n">parts</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
                <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">from_text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">)</span>
            <span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-p">),</span>
        <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Content</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">role</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"user"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-n">parts</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
                <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">from_function_response</span><span class="devsite-syntax-p">(</span>
                    <span class="devsite-syntax-n">name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">function_call</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"result"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">result</span><span class="devsite-syntax-p">},</span>
                <span class="devsite-syntax-p">)</span>
            <span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-p">),</span>
    <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">GenerateContentConfig</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">weather_tool</span><span class="devsite-syntax-p">]),</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-err">```</span>
</code></pre></devsite-code><div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="javascript_10" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-2.5-flash-lite'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">weatherTool</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">functionCall</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">functionCall</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Requested tool: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">functionCall</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"52°F and rain"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-2.5-flash-lite'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">role</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'user'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">role</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'user'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">functionResponse</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">functionCall</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">weatherTool</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_10" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_10" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"contents"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What is the weather like in Boston, MA?"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"tools"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"functionDeclarations"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"description"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Get the current weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"parameters"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"OBJECT"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"properties"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nt">"location"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"STRING"</span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"required"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"candidates"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"functionCall"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"args"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"location"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Boston, MA"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"role"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"finishReason"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"STOP"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="after_interactions_api_6" data-text="After (Interactions API)" tabindex="-1">After (Interactions API)</h3>

<p>Tool calls and results are now distinct steps in the timeline.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_10" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">weather_tool</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span>
    <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"function"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-s2">"name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-s2">"description"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Gets weather"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-s2">"parameters"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"properties"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">weather_tool</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Executing </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2"> for </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">arguments</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>

        <span class="devsite-syntax-n">result</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"52°F and rain"</span>

        <span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-n">previous_interaction_id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
                <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"function_result"</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"call_id"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"result"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">result</span><span class="devsite-syntax-p">}],</span>
                <span class="devsite-syntax-p">}</span>
            <span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_11" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">weatherTool</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">description</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Get weather for a location"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">parameters</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">properties</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">location</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">required</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">};</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">weatherTool</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'function_call'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Executing </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb"> for </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arguments</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-w">        </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"52°F and rain"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-w">        </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">nextInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">previous_interaction_id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'function_result'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">call_id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">nextInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_11" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_11" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">I</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">i</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">ial</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta2/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"input"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"tools"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"description"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Get weather for a location"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parameters"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"properties"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"location"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"required"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">(requires</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">ac</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">io</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">)</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_001"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"requires_action"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"user_input"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"waiting"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"fc_1"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"arguments"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"location"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Boston, MA"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Submi</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Tool</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Resul</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta2/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"previous_interaction_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_001"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"input"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_result"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"call_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"fc_1"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"result"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"52°F with rain"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Fi</span><span class="devsite-syntax-kc">nal</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span>
<span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_002"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"completed"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><strong><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_result"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"call_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"fc_1"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"result"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"52°F with rain"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"It's 52°F with rain in Boston."</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span></strong>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="streaming" data-text="Streaming" tabindex="-1">Streaming</h2>

<p>A key difference in streaming is that the Interactions API uses the same endpoint with <code translate="no" dir="ltr">&quot;stream&quot;: true</code> in the request body, whereas the <code translate="no" dir="ltr">generateContent</code> API required calling a dedicated endpoint (<code translate="no" dir="ltr">:streamGenerateContent</code>).</p>

<p>Additionally, streaming events now use specialized types to monitor the interaction lifecycle and track execution steps along the timeline.</p>

<h3 id="before_generatecontentstream" data-text="Before (generateContentStream)" tabindex="-1">Before (<code translate="no" dir="ltr">generateContentStream</code>)</h3>

<p>With <code translate="no" dir="ltr">generateContent</code>, you consume a stream of response chunks.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_11" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content_stream</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Tell me a story"</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">chunk</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_12" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">responseStream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContentStream</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-2.5-flash-lite'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Tell me a story'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chunk</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">responseStream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">chunk</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_12" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_12" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:streamGenerateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"contents"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Tell me a story"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">trea</span><span class="devsite-syntax-err">m</span>
<strong><span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">co</span><span class="devsite-syntax-kc">ntent</span><span class="devsite-syntax-err">.s</span><span class="devsite-syntax-kc">tart</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"content.start"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought"</span><span class="devsite-syntax-p">}}</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">co</span><span class="devsite-syntax-kc">ntent</span><span class="devsite-syntax-err">.del</span><span class="devsite-syntax-kc">ta</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"content.delta"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought_summary"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"User wants an explanation."</span><span class="devsite-syntax-p">}}</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">co</span><span class="devsite-syntax-kc">ntent</span><span class="devsite-syntax-err">.s</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">op</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"content.stop"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">co</span><span class="devsite-syntax-kc">ntent</span><span class="devsite-syntax-err">.s</span><span class="devsite-syntax-kc">tart</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"content.start"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">}}</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">co</span><span class="devsite-syntax-kc">ntent</span><span class="devsite-syntax-err">.del</span><span class="devsite-syntax-kc">ta</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"content.delta"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hello"</span><span class="devsite-syntax-p">}}</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">co</span><span class="devsite-syntax-kc">ntent</span><span class="devsite-syntax-err">.s</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">op</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"content.stop"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">}</span></strong>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="after_interactions_api_7" data-text="After (Interactions API)" tabindex="-1">After (Interactions API)</h3>

<p>In the Interactions API, streaming uses Server-Sent Events (SSE) and specialized delta types to represent execution steps as they happen.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_12" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Tell me a story"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">):</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"interaction.completed"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n\n</span><span class="devsite-syntax-s2">--- Stream Finished ---"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_13" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Tell me a story'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'step.delta'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'interaction.completed'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'\n\n--- Stream Finished ---'</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_13" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_13" data-text="REST" tabindex="-1">REST</h3><p># Example SSE stream output
<strong>event: interaction.created
data: {&quot;type&quot;: &quot;interaction.created&quot;, &quot;interaction&quot;: {&quot;id&quot;: &quot;int_xyz&quot;, &quot;status&quot;: &quot;created&quot;}}
event: interaction.in_progress
data: {&quot;type&quot;: &quot;interaction.in_progress&quot;, &quot;interaction&quot;: {&quot;id&quot;: &quot;int_xyz&quot;, &quot;status&quot;: &quot;in_progress&quot;}}
event: step.start
data: {&quot;type&quot;: &quot;step.start&quot;, &quot;index&quot;: 0, &quot;step&quot;: {&quot;type&quot;: &quot;thought&quot;}}
event: step.delta
data: {&quot;type&quot;: &quot;step.delta&quot;, &quot;index&quot;: 0, &quot;delta&quot;: {&quot;type&quot;: &quot;thought&quot;, &quot;text&quot;: &quot;User wants an explanation.&quot;}}
event: step.stop
data: {&quot;type&quot;: &quot;step.stop&quot;, &quot;index&quot;: 0, &quot;status&quot;: &quot;done&quot;}
event: step.start
data: {&quot;type&quot;: &quot;step.start&quot;, &quot;index&quot;: 1, &quot;step&quot;: {&quot;type&quot;: &quot;model_output&quot;}}
event: step.delta
data: {&quot;type&quot;: &quot;step.delta&quot;, &quot;index&quot;: 1, &quot;delta&quot;: {&quot;type&quot;: &quot;text&quot;, &quot;text&quot;: &quot;Hello&quot;}}
event: step.stop
data: {&quot;type&quot;: &quot;step.stop&quot;, &quot;index&quot;: 1, &quot;status&quot;: &quot;done&quot;}
event: interaction.completed
data: {&quot;type&quot;: &quot;interaction.completed&quot;, &quot;interaction&quot;: {&quot;id&quot;: &quot;int_xyz&quot;, &quot;status&quot;: &quot;completed&quot;, &quot;usage&quot;: {&quot;prompt_tokens&quot;: 10, &quot;completion_tokens&quot;: 5, &quot;total_tokens&quot;: 15}}}</strong>
```</p></section>
</devsite-selector></div>
<h3 id="streaming_tools_and_function_calls" data-text="Streaming tools and function calls" tabindex="-1">Streaming tools and function calls</h3>

<p>The way tools behave in the stream has shifted significantly from <code translate="no" dir="ltr">generateContent</code> to provide more granular control and visibility.</p>

<h4 id="before_generatecontent_8" data-text="Before (generateContent)" tabindex="-1">Before (<code translate="no" dir="ltr">generateContent</code>)</h4>

<p>With <code translate="no" dir="ltr">generateContent</code>, streaming function calls arrived complete in a single chunk. You could not see the arguments being generated in real-time, so the handler simply checked for a complete <code translate="no" dir="ltr">functionCall</code> object.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_13" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content_stream</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-2.5-flash-lite"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">GenerateContentConfig</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">weather_tool</span><span class="devsite-syntax-p">]),</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">chunk</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-c1"># Function calls arrived complete — no partial arguments</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">parts</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">function_call</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">fc</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">parts</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">function_call</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Call: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">fc</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">(</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">fc</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">args</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">)"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_14" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">generateContentStream</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-2.5-flash-lite'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">weatherTool</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chunk</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chunk</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">candidates</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">].</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-mf">0</span><span class="devsite-syntax-p">];</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">functionCall</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Call: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">functionCall</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">(</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">functionCall</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">args</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">)`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_14" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_14" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:streamGenerateContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"contents"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What is the weather in Boston?"</span><span class="devsite-syntax-p">}]}],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"tools"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"functionDeclarations"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"parameters"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"OBJECT"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"properties"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"location"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"STRING"</span><span class="devsite-syntax-p">}}}}]}]</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">trea</span><span class="devsite-syntax-err">m</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">—</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">fun</span><span class="devsite-syntax-err">c</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">io</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">call</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">arrives</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">comple</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">i</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">o</span><span class="devsite-syntax-kc">ne</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">chu</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">k</span>
<strong><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"candidates"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"parts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"functionCall"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"args"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"location"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Boston, MA"</span><span class="devsite-syntax-p">}}}]}}]}</span></strong>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h4 id="after_interactions_api_8" data-text="After (Interactions API)" tabindex="-1">After (Interactions API)</h4>

<p>The Interactions API streams function call arguments character-by-character as <code translate="no" dir="ltr">arguments</code> events. The entire tool lifecycle — thought, call, result, and output — plays out as a series of distinct steps.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_14" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">get_weather_tool</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.start"</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Calling: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"arguments"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"  args: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">partial_arguments</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">):</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"interaction.completed"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n</span><span class="devsite-syntax-s2">--- Done ---"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_15" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What's the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">getWeatherTool</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'step.start'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'function_call'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Calling: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'step.delta'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'arguments'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">partial_arguments</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`  args: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">partial_arguments</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'interaction.completed'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'\n--- Done ---'</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_15" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Explain how AI works in a few words"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_15" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Reques</span><span class="devsite-syntax-kc">t</span>
<span class="devsite-syntax-err">curl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">X</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">POST</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta2/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">H</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: $GEMINI_API_KEY"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">\</span>
<span class="devsite-syntax-mi">-</span><span class="devsite-syntax-err">d</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">'</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><strong><span class="devsite-syntax-nt">"input"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What is the weather in Boston?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"tools"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"parameters"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"properties"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"location"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">}}}}],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"stream"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span></strong>
<span class="devsite-syntax-p">}</span><span class="devsite-syntax-err">'</span>

<span class="devsite-syntax-err">#</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">Respo</span><span class="devsite-syntax-kc">nse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">trea</span><span class="devsite-syntax-err">m</span>
<span class="devsite-syntax-c1">// Interaction created</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">i</span><span class="devsite-syntax-kc">ntera</span><span class="devsite-syntax-err">c</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">io</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">.crea</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">d</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"interaction.created"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"interaction"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_xyz"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"created"</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">i</span><span class="devsite-syntax-kc">ntera</span><span class="devsite-syntax-err">c</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">io</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">.i</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">_progress</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"interaction.in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"interaction"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_xyz"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"in_progress"</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-c1">// ── Step 0: Thought ──────────────────────────────────</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">tart</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"step"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought"</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.del</span><span class="devsite-syntax-kc">ta</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"The user wants weather data for Boston. I'll call the get_weather tool."</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">op</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.stop"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1">// ── Step 1: Function Call (arguments streamed) ───────</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">tart</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"step"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"fc_1"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.del</span><span class="devsite-syntax-kc">ta</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"arguments"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"partial_arguments"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"{\"location\": \"Boston, MA\"}"</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">op</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.stop"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"waiting"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1">// The interaction pauses — the model needs the tool result before continuing.</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">i</span><span class="devsite-syntax-kc">ntera</span><span class="devsite-syntax-err">c</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">io</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">.requires_ac</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">io</span><span class="devsite-syntax-kc">n</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"interaction.requires_action"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"interaction"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_xyz"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"requires_action"</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-c1">// ── (Client submits the tool result) ──────────────────</span>
<span class="devsite-syntax-c1">// The client calls interactions.create with the function_result as input</span>
<span class="devsite-syntax-c1">// and the previous interaction's ID, then resumes consuming the stream.</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">i</span><span class="devsite-syntax-kc">ntera</span><span class="devsite-syntax-err">c</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">io</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">.i</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">_progress</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"interaction.in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"interaction"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_xyz"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"in_progress"</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-c1">// ── Step 2: Function Result (echoed back, no deltas) ─</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">tart</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"step"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_result"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"call_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"fc_1"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"result"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"52°F, rain"</span><span class="devsite-syntax-p">}]}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">op</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.stop"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1">// ── Step 3: Thought ──────────────────────────────────</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">tart</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"step"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought"</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.del</span><span class="devsite-syntax-kc">ta</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Got weather data. Composing the final response."</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">op</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.stop"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1">// ── Step 4: Model Output (text streamed) ─────────────</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">tart</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">4</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"step"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.del</span><span class="devsite-syntax-kc">ta</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">4</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"It's currently 52°F and rainy in Boston."</span><span class="devsite-syntax-p">}}</span>

<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">s</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">p.s</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">op</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.stop"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">4</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"done"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1">// ── Interaction complete ─────────────────────────────</span>
<span class="devsite-syntax-err">eve</span><span class="devsite-syntax-kc">nt</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">i</span><span class="devsite-syntax-kc">ntera</span><span class="devsite-syntax-err">c</span><span class="devsite-syntax-kc">t</span><span class="devsite-syntax-err">io</span><span class="devsite-syntax-kc">n</span><span class="devsite-syntax-err">.comple</span><span class="devsite-syntax-kc">te</span><span class="devsite-syntax-err">d</span>
<span class="devsite-syntax-err">da</span><span class="devsite-syntax-kc">ta</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"interaction.completed"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"interaction"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"int_xyz"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"completed"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"usage"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nt">"prompt_tokens"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">256</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"completion_tokens"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">128</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"total_tokens"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">384</span><span class="devsite-syntax-p">}}}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
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
  <p>Last updated 2026-08-26 UTC.</p>
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