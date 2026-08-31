








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/temporal-example"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/temporal-example" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/temporal-example" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/temporal-example?hl=sq" /><title>Durable AI agent with Gemini and Temporal &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Durable AI agent with Gemini and Temporal &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta name="description" content="Building durable AI agents with Gemini and Temporal">
  <meta property="og:description" content="Building durable AI agents with Gemini and Temporal"><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/temporal-example"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
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
      Durable AI agent with Gemini and Temporal<devsite-actions hidden data-nosnippet>
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



<p>This tutorial walks you through building a durable AI agent that uses the Gemini
API for reasoning and <a href="https://temporal.io/">Temporal</a> for durability. It uses
Temporal&#39;s built-in <a href="https://github.com/temporalio/sdk-python/tree/main/temporalio/contrib/google_genai">Gemini SDK integration</a>.</p>

<p>The agent can call tools, like looking up weather alerts or geolocating an IP
address, and will loop until it has enough information to respond.</p>

<p>What makes this different from a typical agent demo is <strong>durability</strong>. Every LLM
call and every tool invocation is persisted by Temporal. If the process crashes,
the network drops, or an API times out, Temporal automatically retries and
resumes from the last completed step. No conversation history is lost, and no
tool calls are incorrectly repeated.</p>

<h2 id="architecture" data-text="Architecture" tabindex="-1">Architecture</h2>

<p>The architecture consists of three parts:</p>

<ul>
<li><strong>Workflow:</strong> A single <code translate="no" dir="ltr">generate_content</code> call. The Gemini SDK&#39;s automatic
function calling (AFC) loop runs <em>inside</em> the Workflow, and Temporal makes
every step of it durable.</li>
<li><strong>Activities:</strong> Individual units of work that Temporal makes durable. The
Gemini API calls become Activities automatically.</li>
<li><strong>Worker:</strong> The process that executes the Workflows and Activities, and the
only place your API key lives.</li>
</ul>

<p>In this example, you will place all three of these pieces in a single file
(<code translate="no" dir="ltr">durable_agent_worker.py</code>). In a real-world implementation, you would separate
them to allow for various deployment and scalability advantages. You will supply
prompts to the agent with the Temporal CLI, so there is no client code to write.</p>

<h2 id="prerequisites" data-text="Prerequisites" tabindex="-1">Prerequisites</h2>

<p>To complete this guide, you&#39;ll need:</p>

<ul>
<li>A Gemini API key. You can create one for free in
<a href="https://aistudio.google.com/apikey">Google AI Studio</a>.</li>
<li><a href="https://www.python.org/downloads/">Python</a> version 3.10 or later.</li>
<li><a href="https://docs.astral.sh/uv/getting-started/installation/">uv</a> for dependency
management.</li>
<li>The <a href="https://docs.temporal.io/cli">Temporal CLI</a> for running a local
development server and starting Workflows.</li>
</ul>

<h2 id="setup" data-text="Setup" tabindex="-1">Setup</h2>

<p>Before you begin, ensure you have a
<a href="https://docs.temporal.io/cli#start-dev-server">Temporal development server</a>
running locally:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">temporal<span class="devsite-syntax-w"> </span>server<span class="devsite-syntax-w"> </span>start-dev</code></pre></devsite-code>
<p>Next, create a project and install the required dependencies:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">uv<span class="devsite-syntax-w"> </span>init<span class="devsite-syntax-w"> </span>durable-gemini-agent</code>
<code class="devsite-terminal" translate="no" dir="ltr"><span class="devsite-syntax-nb">cd</span><span class="devsite-syntax-w"> </span>durable-gemini-agent</code>
<code class="devsite-terminal" translate="no" dir="ltr">uv<span class="devsite-syntax-w"> </span>add<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"temporalio[google-genai]"</span><span class="devsite-syntax-w"> </span>httpx<span class="devsite-syntax-w"> </span>python-dotenv</code></pre></devsite-code>
<p>uv creates and manages the virtual environment for you, so every Python command
later in this tutorial runs through <code translate="no" dir="ltr">uv run</code>.</p>

<p>Create a <code translate="no" dir="ltr">.env</code> file in your project directory with your Gemini API key. You
can get an API key from
<a href="https://aistudio.google.com/apikey">Google AI Studio</a>.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr"><span class="devsite-syntax-nb">echo</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"GOOGLE_API_KEY=your-api-key-here"</span><span class="devsite-syntax-w"> &gt; </span>.env</code></pre></devsite-code><aside class="note"><strong>Note:</strong><span> Only the worker process needs the API key. Whatever starts the
Workflow does not require it, and neither does the Workflow itself—the real
<code translate="no" dir="ltr">genai.Client</code> is constructed on the worker and never crosses into Workflow
code, so no auth material can appear in Temporal&#39;s event history.</span></aside>
<h2 id="implementation" data-text="Implementation" tabindex="-1">Implementation</h2>

<p>The rest of this tutorial walks through <code translate="no" dir="ltr">durable_agent_worker.py</code> from top to
bottom, building up the agent piece by piece. Create the file and follow along.</p>
<aside class="note"><strong>Note:</strong><span> The <code translate="no" dir="ltr">temporalio.contrib.google_genai</code> integration is experimental. Its API
may change in future versions of the Temporal Python SDK.</span></aside>
<h3 id="imports" data-text="Imports and sandbox setup" tabindex="-1">Imports and sandbox setup</h3>

<p>Start with the imports that must be defined up-front. The
<code translate="no" dir="ltr">workflow.unsafe.imports_passed_through()</code> block tells Temporal&#39;s Workflow
sandbox to let <code translate="no" dir="ltr">httpx</code> pass through without restriction. Importing <code translate="no" dir="ltr">httpx</code>
executes <code translate="no" dir="ltr">class _CookieCompatRequest(urllib.request.Request)</code>, and the sandbox
blocks subclassing that stdlib class.</p>

<p>Your tools use <code translate="no" dir="ltr">httpx</code>, and <code translate="no" dir="ltr">activity_as_tool()</code> needs the Workflow to import
those tool functions so Gemini can derive their schemas from the signatures. So
<code translate="no" dir="ltr">httpx</code> reaches the sandbox no matter how you split the files—moving the tools
into their own module doesn&#39;t avoid it.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">workflow</span>

<span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">workflow</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">unsafe</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">imports_passed_through</span><span class="devsite-syntax-p">():</span>
    <span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">httpx</span>
</code></pre></devsite-code>
<p>You don&#39;t need to list <code translate="no" dir="ltr">google.genai</code> here. The Temporal plugin you configure
later adds it—along with <code translate="no" dir="ltr">pydantic_core</code> and <code translate="no" dir="ltr">annotated_types</code>—to the sandbox
passthrough set for you.</p>

<h3 id="system-instructions" data-text="System instructions" tabindex="-1">System instructions</h3>

<p>Next, define the agent&#39;s personality. The system instructions tell the model how
to behave. This agent is instructed to respond in haikus when no tools are
needed.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">SYSTEM_INSTRUCTIONS</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"""</span>
<span class="devsite-syntax-s2">You are a helpful agent that can use tools to help the user.</span>
<span class="devsite-syntax-s2">You will be given an input from the user and a list of tools to use.</span>
<span class="devsite-syntax-s2">You may or may not need to use the tools to satisfy the user ask.</span>
<span class="devsite-syntax-s2">If no tools are needed, respond in haikus.</span>
<span class="devsite-syntax-s2">"""</span>
</code></pre></devsite-code>
<h3 id="tool-definitions" data-text="Tool definitions" tabindex="-1">Tool definitions</h3>

<p>Now define the tools the agent can use. Each tool is an ordinary Temporal
Activity: an async function decorated with <code translate="no" dir="ltr">@activity.defn</code>, with type-annotated
parameters and a descriptive docstring. Gemini builds the function declaration
from that signature and docstring, so document each parameter in the <code translate="no" dir="ltr">Args</code>
section.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">json</span>

<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">activity</span>

<span class="devsite-syntax-n">NWS_API_BASE</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"https://api.weather.gov"</span>
<span class="devsite-syntax-n">USER_AGENT</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"weather-app/1.0"</span>

<span class="devsite-syntax-nd">@activity</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">defn</span>
<span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">get_weather_alerts</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">state</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-nb">str</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-o">-</span>&gt; <span class="devsite-syntax-nb">str</span><span class="devsite-syntax-p">:</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-sd">"""Get weather alerts for a US state.</span>

<span class="devsite-syntax-sd">    Args:</span>
<span class="devsite-syntax-sd">        state: Two-letter US state code (e.g. CA, NY)</span>
<span class="devsite-syntax-sd">    """</span>
    <span class="devsite-syntax-n">headers</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"User-Agent"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">USER_AGENT</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"Accept"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"application/geo+json"</span><span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-n">url</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">NWS_API_BASE</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">/alerts/active/area/</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">state</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>

    <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">httpx</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AsyncClient</span><span class="devsite-syntax-p">()</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">url</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">headers</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">headers</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">timeout</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mf">5.0</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">raise_for_status</span><span class="devsite-syntax-p">()</span>
        <span class="devsite-syntax-k">return</span> <span class="devsite-syntax-n">json</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">dumps</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">json</span><span class="devsite-syntax-p">())</span>
</code></pre></devsite-code>
<p>Next, define tools for IP address geolocation:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-nd">@activity</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">defn</span>
<span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">get_ip_address</span><span class="devsite-syntax-p">()</span> <span class="devsite-syntax-o">-</span>&gt; <span class="devsite-syntax-nb">str</span><span class="devsite-syntax-p">:</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-sd">"""Get the public IP address of the current machine."""</span>
    <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">httpx</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AsyncClient</span><span class="devsite-syntax-p">()</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"https://icanhazip.com"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">raise_for_status</span><span class="devsite-syntax-p">()</span>
        <span class="devsite-syntax-k">return</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">strip</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-nd">@activity</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">defn</span>
<span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">get_location_info</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">ipaddress</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-nb">str</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-o">-</span>&gt; <span class="devsite-syntax-nb">str</span><span class="devsite-syntax-p">:</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-sd">"""Get the location information for an IP address including city, state, and country.</span>

<span class="devsite-syntax-sd">    Args:</span>
<span class="devsite-syntax-sd">        ipaddress: An IP address to look up</span>
<span class="devsite-syntax-sd">    """</span>
    <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">httpx</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AsyncClient</span><span class="devsite-syntax-p">()</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"http://ip-api.com/json/</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">ipaddress</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">raise_for_status</span><span class="devsite-syntax-p">()</span>
        <span class="devsite-syntax-n">result</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">json</span><span class="devsite-syntax-p">()</span>
        <span class="devsite-syntax-k">return</span> <span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'city'</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">, </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'regionName'</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">, </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'country'</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>
</code></pre></devsite-code>
<p>That&#39;s the whole tool layer. There is no tool registry, no <code translate="no" dir="ltr">FunctionDeclaration</code>
construction, and no dispatch table—the next section wraps these Activities with
<code translate="no" dir="ltr">activity_as_tool()</code>, which passes each parameter through to the Activity
positionally. Tools with zero, one, or several parameters all work.</p>

<h3 id="agent-workflow" data-text="The agent Workflow" tabindex="-1">The agent Workflow</h3>

<p>Now you have all the pieces to finish building the agent. The <code translate="no" dir="ltr">AgentWorkflow</code>
class makes one <code translate="no" dir="ltr">generate_content</code> call. <code translate="no" dir="ltr">TemporalAsyncClient</code> is a drop-in
<code translate="no" dir="ltr">AsyncClient</code> whose every API call runs as a Temporal Activity, and
<code translate="no" dir="ltr">activity_as_tool()</code> turns each of your Activities into a Gemini tool.</p>

<p>When the model asks for a tool, the SDK&#39;s AFC loop—running inside the
Workflow—dispatches it through <code translate="no" dir="ltr">workflow.execute_activity</code>, appends the result
to the conversation, and calls the model again. That loop is the agent, and it
is durable because each step is an Activity recorded in Temporal&#39;s event
history.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">datetime</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">timedelta</span>

<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio.contrib.google_genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">TemporalAsyncClient</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">activity_as_tool</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio.workflow</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">ActivityConfig</span>

<span class="devsite-syntax-n">TOOL_CONFIG</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">ActivityConfig</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">start_to_close_timeout</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">timedelta</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">seconds</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">30</span><span class="devsite-syntax-p">))</span>

<span class="devsite-syntax-nd">@workflow</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">defn</span>
<span class="devsite-syntax-k">class</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nc">AgentWorkflow</span><span class="devsite-syntax-p">:</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-sd">"""Agent workflow that uses Gemini for LLM calls and executes tools."""</span>

    <span class="devsite-syntax-nd">@workflow</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">run</span>
    <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">run</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-bp">self</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-nb">str</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-o">-</span>&gt; <span class="devsite-syntax-nb">str</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">TemporalAsyncClient</span><span class="devsite-syntax-p">()</span>

        <span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">GenerateContentConfig</span><span class="devsite-syntax-p">(</span>
                <span class="devsite-syntax-n">system_instruction</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">SYSTEM_INSTRUCTIONS</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
                    <span class="devsite-syntax-n">activity_as_tool</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">get_weather_alerts</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">activity_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">TOOL_CONFIG</span><span class="devsite-syntax-p">),</span>
                    <span class="devsite-syntax-n">activity_as_tool</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">get_ip_address</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">activity_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">TOOL_CONFIG</span><span class="devsite-syntax-p">),</span>
                    <span class="devsite-syntax-n">activity_as_tool</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">get_location_info</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">activity_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">TOOL_CONFIG</span><span class="devsite-syntax-p">),</span>
                <span class="devsite-syntax-p">],</span>
            <span class="devsite-syntax-p">),</span>
        <span class="devsite-syntax-p">)</span>

        <span class="devsite-syntax-c1"># Leave this in place. You will un-comment it during a durability</span>
        <span class="devsite-syntax-c1"># test later on.</span>
        <span class="devsite-syntax-c1"># await workflow.sleep(timedelta(seconds=10))</span>

        <span class="devsite-syntax-k">return</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span> <span class="devsite-syntax-ow">or</span> <span class="devsite-syntax-s2">""</span>
</code></pre></devsite-code>
<p>A few things to note:</p>

<ul>
<li>Construct <code translate="no" dir="ltr">TemporalAsyncClient</code> <strong>inside</strong> the Workflow. It carries no
credentials; it only knows how to turn API calls into Activity invocations.</li>
<li><code translate="no" dir="ltr">activity_config</code> must set <code translate="no" dir="ltr">start_to_close_timeout</code> or
<code translate="no" dir="ltr">schedule_to_close_timeout</code>. Temporal requires a timeout and there is no
default for tool Activities.</li>
<li>The Gemini API Activities default to a 60-second <code translate="no" dir="ltr">start_to_close_timeout</code>.
Override it with <code translate="no" dir="ltr">TemporalAsyncClient(activity_config=...)</code> if your model
calls need longer.</li>
</ul>

<p>The agent is fully durable. If the worker crashes after several turns, Temporal
picks up exactly where it left off without re-invoking already executed LLM
calls or tool calls.</p>

<h3 id="retries" data-text="Retries" tabindex="-1">Retries</h3>

<p>Temporal owns retries, so don&#39;t enable the Gemini SDK&#39;s own retry loop. Set
retry behavior with a <code translate="no" dir="ltr">retry_policy</code> on the Activity config instead:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio.common</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">RetryPolicy</span>

<span class="devsite-syntax-n">TOOL_CONFIG</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">ActivityConfig</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">start_to_close_timeout</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">timedelta</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">seconds</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">30</span><span class="devsite-syntax-p">),</span>
    <span class="devsite-syntax-n">retry_policy</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">RetryPolicy</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">maximum_attempts</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code>
<p>API failures are also classified for you. Transient statuses (408, 429, 5xx)
stay retryable so the Activity&#39;s retry policy applies; other statuses (such as a
400 for a malformed request) are non-retryable, so the Workflow fails fast
instead of burning attempts on an error that won&#39;t resolve.</p>

<p>You can extend that classification. The integration surfaces each API failure as
an <code translate="no" dir="ltr">ApplicationError</code> whose type is the Gemini exception class name—<code translate="no" dir="ltr">ClientError</code>
for 4xx, <code translate="no" dir="ltr">ServerError</code> for 5xx—so listing a name in
<code translate="no" dir="ltr">non_retryable_error_types</code> moves it out of the transient set. For example, to
stop retrying Gemini-side outages and fail the Workflow on the first 5xx, apply
the policy to the Gemini API Activities through <code translate="no" dir="ltr">TemporalAsyncClient</code>:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio.common</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">RetryPolicy</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">TemporalAsyncClient</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">activity_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">ActivityConfig</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">start_to_close_timeout</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">timedelta</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">seconds</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">60</span><span class="devsite-syntax-p">),</span>
        <span class="devsite-syntax-n">retry_policy</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">RetryPolicy</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">maximum_attempts</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">5</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-n">non_retryable_error_types</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"ServerError"</span><span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-p">),</span>
    <span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code>
<h3 id="worker-startup" data-text="Worker startup" tabindex="-1">Worker startup</h3>

<p>Finally, wire everything together. The Temporal worker connects to the Temporal
service and acts as a scheduler for the Workflow and Activity tasks.</p>

<p>This is where the real <code translate="no" dir="ltr">genai.Client</code> is created, with your API key.
<code translate="no" dir="ltr">GoogleGenAIPlugin</code> takes that client and registers the Gemini API Activities,
installs the Pydantic data converter, and configures the Workflow sandbox.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">asyncio</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">os</span>

<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">dotenv</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">load_dotenv</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio.client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">Client</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio.contrib.google_genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">GoogleGenAIPlugin</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio.envconfig</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">ClientConfig</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">temporalio.worker</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">Worker</span>

<span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">main</span><span class="devsite-syntax-p">():</span>
    <span class="devsite-syntax-n">gemini</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">api_key</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">os</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environ</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"GOOGLE_API_KEY"</span><span class="devsite-syntax-p">])</span>
    <span class="devsite-syntax-n">plugin</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">GoogleGenAIPlugin</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">gemini</span><span class="devsite-syntax-p">)</span>

    <span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">ClientConfig</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">load_client_connect_config</span><span class="devsite-syntax-p">()</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setdefault</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"target_host"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"localhost:7233"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">Client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">connect</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">**</span><span class="devsite-syntax-n">config</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">plugins</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">plugin</span><span class="devsite-syntax-p">])</span>

    <span class="devsite-syntax-n">worker</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">Worker</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-n">task_queue</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-agent"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-n">workflows</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
            <span class="devsite-syntax-n">AgentWorkflow</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-n">activities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
            <span class="devsite-syntax-n">get_weather_alerts</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-n">get_ip_address</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-n">get_location_info</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">worker</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">run</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-k">if</span> <span class="devsite-syntax-vm">__name__</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"__main__"</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">load_dotenv</span><span class="devsite-syntax-p">()</span>
    <span class="devsite-syntax-n">asyncio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">run</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">main</span><span class="devsite-syntax-p">())</span>
</code></pre></devsite-code>
<p>The plugin removes three pieces of boilerplate you would otherwise need here:</p>

<ul>
<li>No <code translate="no" dir="ltr">data_converter=pydantic_data_converter</code>—the plugin installs the Pydantic
payload converter itself.</li>
<li>No <code translate="no" dir="ltr">activity_executor=ThreadPoolExecutor</code>—every Activity is async.</li>
<li>No Gemini Activities in the <code translate="no" dir="ltr">activities</code> list—the plugin registers them.
You only register your own tools.</li>
</ul>

<h2 id="run-agent" data-text="Run the agent" tabindex="-1">Run the agent</h2>

<p>That&#39;s the entire agent. You don&#39;t need to write a client—the Temporal CLI can
start the Workflow for you.</p>

<p>If you haven&#39;t already, start the Temporal development server:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">temporal<span class="devsite-syntax-w"> </span>server<span class="devsite-syntax-w"> </span>start-dev</code></pre></devsite-code>
<p>In a new terminal window, start the agent worker:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">uv<span class="devsite-syntax-w"> </span>run<span class="devsite-syntax-w"> </span>durable_agent_worker.py</code></pre></devsite-code>
<p>In a third terminal window, submit a query to your agent:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">temporal<span class="devsite-syntax-w"> </span>workflow<span class="devsite-syntax-w"> </span>execute<span class="devsite-syntax-w"> </span>--type<span class="devsite-syntax-w"> </span>AgentWorkflow<span class="devsite-syntax-w"> </span>--task-queue<span class="devsite-syntax-w"> </span>gemini-agent<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--input<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'"are there any weather alerts for where I am?"'</span></code></pre></devsite-code>
<p>Note the task queue: it&#39;s the same one the worker polls. Starting the Workflow
dispatches a Workflow task carrying the user prompt to that queue, which is what
initiates the agent. <code translate="no" dir="ltr">execute</code> blocks until the Workflow completes and prints the
result. If you&#39;d rather not wait, use <code translate="no" dir="ltr">temporal workflow start</code> with an explicit
<code translate="no" dir="ltr">--workflow-id</code>, then collect the result later with
<code translate="no" dir="ltr">temporal workflow result -w your-workflow-id</code>. Temporal generates the Workflow
ID for you when you omit <code translate="no" dir="ltr">--workflow-id</code>.</p>

<p><code translate="no" dir="ltr">--input</code> takes JSON, so a bare string prompt needs its own quotes inside the
shell quotes. The CLI needs no Gemini API key, and no data converter
configuration either: the Workflow&#39;s argument and return value are both plain
strings, which the default JSON payload converter handles.</p>

<p>Open the Temporal UI at
<code translate="no" dir="ltr">http://localhost:8233/namespaces/default/workflows</code> to watch the agentic loop
unfold. You&#39;ll see <code translate="no" dir="ltr">gemini_api_client_async_request</code> Activities—one per model
turn—interleaved with one Activity per tool call, each labeled with a
<code translate="no" dir="ltr">tool_call</code> summary. That interleaving <em>is</em> the AFC loop, made durable and
observable.</p>

<p>Try a few different prompts to see the agent reason and call tools. Each command
is the same as the one above with a new <code translate="no" dir="ltr">--input</code>:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">temporal<span class="devsite-syntax-w"> </span>workflow<span class="devsite-syntax-w"> </span>execute<span class="devsite-syntax-w"> </span>--type<span class="devsite-syntax-w"> </span>AgentWorkflow<span class="devsite-syntax-w"> </span>--task-queue<span class="devsite-syntax-w"> </span>gemini-agent<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--input<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'"are there any weather alerts for New York?"'</span></code>
<code class="devsite-terminal" translate="no" dir="ltr">temporal<span class="devsite-syntax-w"> </span>workflow<span class="devsite-syntax-w"> </span>execute<span class="devsite-syntax-w"> </span>--type<span class="devsite-syntax-w"> </span>AgentWorkflow<span class="devsite-syntax-w"> </span>--task-queue<span class="devsite-syntax-w"> </span>gemini-agent<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--input<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'"where am I?"'</span></code>
<code class="devsite-terminal" translate="no" dir="ltr">temporal<span class="devsite-syntax-w"> </span>workflow<span class="devsite-syntax-w"> </span>execute<span class="devsite-syntax-w"> </span>--type<span class="devsite-syntax-w"> </span>AgentWorkflow<span class="devsite-syntax-w"> </span>--task-queue<span class="devsite-syntax-w"> </span>gemini-agent<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--input<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'"what is my ip address?"'</span></code>
<code class="devsite-terminal" translate="no" dir="ltr">temporal<span class="devsite-syntax-w"> </span>workflow<span class="devsite-syntax-w"> </span>execute<span class="devsite-syntax-w"> </span>--type<span class="devsite-syntax-w"> </span>AgentWorkflow<span class="devsite-syntax-w"> </span>--task-queue<span class="devsite-syntax-w"> </span>gemini-agent<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--input<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'"tell me a joke"'</span></code></pre></devsite-code>
<p>The last prompt doesn&#39;t require any tools, so the agent responds in a haiku
based on the <code translate="no" dir="ltr">SYSTEM_INSTRUCTIONS</code>.</p>

<h2 id="test-durability" data-text="Test durability" tabindex="-1">Test durability</h2>

<p>Building on Temporal ensures your agent survives failures seamlessly. You can
test this using two distinct experiments.</p>

<h3 id="network-outage" data-text="Simulating a network outage" tabindex="-1">Simulating a network outage</h3>

<p>In this test, you&#39;ll temporarily disable your computer&#39;s internet connection,
submit a Workflow, watch Temporal automatically retry, and then restore the
network to see it recover.</p>

<ol>
<li>Disconnect your machine from the internet (for example, turn off your
Wi-Fi).</li>
<li><p>Submit a Workflow:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">temporal<span class="devsite-syntax-w"> </span>workflow<span class="devsite-syntax-w"> </span>execute<span class="devsite-syntax-w"> </span>--type<span class="devsite-syntax-w"> </span>AgentWorkflow<span class="devsite-syntax-w"> </span>--task-queue<span class="devsite-syntax-w"> </span>gemini-agent<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--input<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'"tell me a joke"'</span></code></pre></devsite-code></li>
<li><p>Check the Temporal UI (<code translate="no" dir="ltr">http://localhost:8233</code>). You will see the Gemini API
Activity failing and Temporal automatically managing the retries in the
background.</p></li>
<li><p>Reconnect to the internet.</p></li>
<li><p>The next automated retry will successfully reach the Gemini API, and your
terminal will print the final result.</p></li>
</ol>

<h3 id="worker-crash" data-text="Surviving a worker crash" tabindex="-1">Surviving a worker crash</h3>

<p>In this test, you kill the worker mid-execution and restart it. Temporal replays
the Workflow history (event sourcing) and resumes from the last completed
Activity—already-completed LLM invocations and tool calls are not repeated.</p>

<ol>
<li><p>To give yourself time to kill the worker, open <code translate="no" dir="ltr">durable_agent_worker.py</code> and
uncomment the durable timer in <code translate="no" dir="ltr">AgentWorkflow.run</code>:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">workflow</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">sleep</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">timedelta</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">seconds</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">10</span><span class="devsite-syntax-p">))</span>
</code></pre></devsite-code>
<p><code translate="no" dir="ltr">workflow.sleep</code> is a Temporal timer, not a local one. It is recorded in
history and survives the restart, which is what makes this test reliable.</p></li>
<li><p>Restart the worker:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">uv<span class="devsite-syntax-w"> </span>run<span class="devsite-syntax-w"> </span>durable_agent_worker.py</code></pre></devsite-code></li>
<li><p>Submit a query that triggers several tools:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">temporal<span class="devsite-syntax-w"> </span>workflow<span class="devsite-syntax-w"> </span>execute<span class="devsite-syntax-w"> </span>--type<span class="devsite-syntax-w"> </span>AgentWorkflow<span class="devsite-syntax-w"> </span>--task-queue<span class="devsite-syntax-w"> </span>gemini-agent<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--input<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'"are there any weather alerts where I am?"'</span></code></pre></devsite-code></li>
<li><p>Once the tool calls have completed and the timer is running, kill the worker
process (<code translate="no" dir="ltr">Ctrl-C</code> in the worker terminal, or <code translate="no" dir="ltr">kill %1</code> if running in the
background).</p></li>
<li><p>Restart the worker:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code class="devsite-terminal" translate="no" dir="ltr">uv<span class="devsite-syntax-w"> </span>run<span class="devsite-syntax-w"> </span>durable_agent_worker.py</code></pre></devsite-code></li>
</ol>

<p>Temporal replays the Workflow history. The LLM calls and tool invocations that
already completed are <strong>not</strong> re-executed—their results are instantly replayed
from history (the event log), the timer resumes, and the Workflow finishes
successfully.</p>

<h2 id="going-further" data-text="Going further" tabindex="-1">Going further</h2>

<p>The integration supports more than this tutorial covers. See the
<a href="https://github.com/temporalio/sdk-python/tree/main/temporalio/contrib/google_genai">plugin documentation</a>
for details:</p>

<ul>
<li><strong>Streaming.</strong> Use <code translate="no" dir="ltr">generate_content_stream</code> as usual. To let an external
consumer (a chat UI) observe chunks in real time while the Workflow runs
durably, set <code translate="no" dir="ltr">TemporalAsyncClient(streaming_topic=...)</code> and host a
<code translate="no" dir="ltr">WorkflowStream</code> in the Workflow.</li>
<li><strong>MCP.</strong> Register a client-side MCP server on the worker with
<code translate="no" dir="ltr">GoogleGenAIPlugin(mcp_servers={...})</code> and reference it by name in the
Workflow with <code translate="no" dir="ltr">TemporalMcpClientSession</code>. Tool discovery and calls run as
Activities against a pooled worker-side connection.</li>
<li><strong>Vertex AI.</strong> Pass <code translate="no" dir="ltr">vertexai=True</code> to both the worker-side <code translate="no" dir="ltr">genai.Client</code>
and the Workflow-side <code translate="no" dir="ltr">TemporalAsyncClient</code>, setting <code translate="no" dir="ltr">project</code> and
<code translate="no" dir="ltr">location</code> explicitly on the Workflow side so replay stays deterministic.</li>
</ul>

<h2 id="further-resources" data-text="Further resources" tabindex="-1">Further resources</h2>

<ul>
<li><a href="https://docs.temporal.io/">Temporal documentation</a></li>
<li><a href="https://docs.temporal.io/develop/python">Temporal Python SDK</a></li>
<li><a href="https://docs.temporal.io/develop/python/integrations/google-genai">Temporal Gemini SDK integration</a></li>
<li><a href="https://googleapis.github.io/python-genai/">Google GenAI SDK</a></li>
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
  <p>Last updated 2026-08-19 UTC.</p>
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