








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/streaming"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/streaming" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/streaming" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/streaming?hl=sq" /><title>Streaming interactions &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Streaming interactions &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta name="description" content="Stream Interactions API responses using server-sent events (SSE)">
  <meta property="og:description" content="Stream Interactions API responses using server-sent events (SSE)"><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/streaming"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
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
      Streaming interactions<devsite-actions hidden data-nosnippet>
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



<p>When creating an Interaction, you can set <code translate="no" dir="ltr">stream: true</code> to incrementally stream the response using <a href="https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events" class="external">server-sent events</a> (SSE).</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Count from 1 to 25."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Count from 1 to 25."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDeltaData</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionResponse</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.utils.EventStream</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Count from 1 to 25."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">stream</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateInteractionResponse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">));</span>

<span class="devsite-syntax-k">try</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">EventStream&lt;InteractionSSEStreamEvent&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">events</span><span class="devsite-syntax-p">())</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionSSEStreamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">InteractionSSEEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">data</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-n">StepDeltaData</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">delta</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">ifPresent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">::</span><span class="devsite-syntax-n">print</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--no-buffer<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Count from 1 to 25.",</span>
<span class="devsite-syntax-s1">    "stream": true</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Transact-SQL" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">created</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"object"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"model"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"gemini-3.7-flash"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.created"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">status_update</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction_id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.status_update"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"signature"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought_signature"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"model_output"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"1, 2, 3, 4, 5, 6, "</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"7, 8, 9, 10, 11, 12, 13,"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-p">...</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">completed</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"completed"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"usage"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"total_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">346</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_input_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">11</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"input_tokens_by_modality"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-o">[</span><span class="devsite-syntax-n">{"modality":"text","tokens":11}</span><span class="devsite-syntax-o">]</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_cached_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_output_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">90</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_tool_use_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_thought_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">245</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"created"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"2026-05-12T18:44:51Z"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"updated"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"2026-05-12T18:44:51Z"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"service_tier"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"standard"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"object"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"model"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"gemini-3.7-flash"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.completed"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">done</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">[</span><span class="devsite-syntax-n">DONE</span><span class="devsite-syntax-o">]</span>
</code></pre></devsite-code>
<h2 id="event-types" data-text="Event types" tabindex="-1">Event types</h2>

<p>Each server-sent event includes a named <code translate="no" dir="ltr">event_type</code> and associated JSON data. The Interactions API uses a symmetric streaming model where all content—text, tool calls, thinking—flows through a consistent <strong>step-based</strong> event.</p>

<p>Each stream follows this event flow:</p>

<ol>
<li><code translate="no" dir="ltr">interaction.created</code>: The interaction is created, includes metadata (ID, model, status).</li>
<li>A series of <strong>steps</strong>, each consisting of:
<ul>
<li>A <code translate="no" dir="ltr">step.start</code> event, indicating the step type (e.g., <code translate="no" dir="ltr">model_output</code>, <code translate="no" dir="ltr">thought</code>, <code translate="no" dir="ltr">function_call</code>).</li>
<li>One or more <code translate="no" dir="ltr">step.delta</code> events with incremental data for that step.</li>
<li>A <code translate="no" dir="ltr">step.stop</code> event marking the step as complete.</li>
</ul></li>
<li>An <code translate="no" dir="ltr">interaction.completed</code> event with final <code translate="no" dir="ltr">usage</code> statistics.</li>
</ol>

<p>When you set <code translate="no" dir="ltr">stream: false</code>, the API returns a single <code translate="no" dir="ltr">interaction</code> object with a <code translate="no" dir="ltr">steps</code> array. Each element in <code translate="no" dir="ltr">steps</code> is the fully assembled version of one <code translate="no" dir="ltr">step.start</code> → <code translate="no" dir="ltr">step.delta</code>(s) → <code translate="no" dir="ltr">step.stop</code> cycle.</p>

<h3 id="event-interaction-created" data-text="interaction.created" tabindex="-1"><code translate="no" dir="ltr">interaction.created</code></h3>

<p>Sent when the interaction is first created. Contains the interaction ID, model, and initial status.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">created</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"interaction"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"object"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"interaction"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"interaction.created"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h3 id="event-interaction-status-update" data-text="interaction.status_update" tabindex="-1"><code translate="no" dir="ltr">interaction.status_update</code></h3>

<p>Signals an interaction-level status transition. May appear between steps.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">status_update</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"interaction_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"interaction.status_update"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h3 id="event-step-start" data-text="step.start" tabindex="-1"><code translate="no" dir="ltr">step.start</code></h3>

<p>Marks the beginning of a new step. Contains the step <code translate="no" dir="ltr">type</code> and <code translate="no" dir="ltr">index</code>. The step type determines which delta types to expect and how the step appears in a non-streaming response:</p>

<table>
<thead>
<tr>
<th>Step Type</th>
<th>Expected Delta Types</th>
<th>Description</th>
</tr>
</thead>

<tbody>
<tr>
<td><code translate="no" dir="ltr">model_output</code></td>
<td><code translate="no" dir="ltr">text</code>, <code translate="no" dir="ltr">image</code>, <code translate="no" dir="ltr">audio</code></td>
<td>The model&#39;s final response content.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">thought</code></td>
<td><code translate="no" dir="ltr">thought_signature</code>, <code translate="no" dir="ltr">thought_summary</code></td>
<td>Chain-of-thought reasoning. <code translate="no" dir="ltr">summary</code> is only present when <code translate="no" dir="ltr">thinking_summaries</code> is enabled.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">function_call</code></td>
<td><code translate="no" dir="ltr">arguments_delta</code></td>
<td>A request for the client to execute a function. Sets interaction status to <code translate="no" dir="ltr">requires_action</code>.</td>
</tr>
<tr>
<td>Server-side tools</td>
<td>Varies by tool</td>
<td>Tools executed by the API (e.g., <code translate="no" dir="ltr">google_search_call</code>, <code translate="no" dir="ltr">google_search_result</code>, <code translate="no" dir="ltr">code_execution_call</code>, <code translate="no" dir="ltr">code_execution_result</code>).</td>
</tr>
</tbody>
</table>

<p>See the <a href="/api/interactions-api">Interactions API reference</a> for the full list.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">start</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"model_output"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step.start"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p>For function calls, the step includes the function name, id and empty arguments <code translate="no" dir="ltr">{}</code>.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">start</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"function_call"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"un6k8t18"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"get_weather"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"arguments"</span><span class="devsite-syntax-p">:{}},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step.start"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h3 id="event-step-delta" data-text="step.delta" tabindex="-1"><code translate="no" dir="ltr">step.delta</code></h3>

<p>Incremental data for the current step. The <code translate="no" dir="ltr">delta</code> object contains a <code translate="no" dir="ltr">type</code> field that determines its shape.</p>

<p><strong>Examples:</strong></p>

<p><strong><code translate="no" dir="ltr">text</code>:</strong> Incremental text token from a <code translate="no" dir="ltr">model_output</code> step:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"Hello, my name is Phil"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step.delta"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">", and I live in Germany."</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step.delta"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p><strong><code translate="no" dir="ltr">image</code>:</strong> Base64-encoded image data from a <code translate="no" dir="ltr">model_output</code> step:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"image"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"mime_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"image/jpeg"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"data"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAoHBwgHBgoICAgLCg..."</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step.delta"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p><strong><code translate="no" dir="ltr">thought_summary</code>:</strong> Thinking summary content from a <code translate="no" dir="ltr">thought</code> step:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"thought_summary"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"I need to find the GCD..."</span><span class="devsite-syntax-p">}},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step.delta"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p><strong><code translate="no" dir="ltr">arguments_delta</code>:</strong> (Partial) JSON string for function call arguments. Must be accumulated across deltas:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"delta"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"arguments_delta"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"arguments"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"{\"location\": \"San Francisco, CA\"}"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step.delta"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p>These are some of the most common delta types. For the complete list of all delta types, see the <a href="/api/interactions-api">Interactions API reference</a>.</p>

<h3 id="event-step-stop" data-text="step.stop" tabindex="-1"><code translate="no" dir="ltr">step.stop</code></h3>

<p>Marks the end of a step. Contains the step <code translate="no" dir="ltr">index</code>.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stop</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"step.stop"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p>When using the <a href="/gemini-api/docs/antigravity-agent">Antigravity Agent</a>, the
<code translate="no" dir="ltr">step.stop</code> event may also include usage statistics:</p>

<ul>
<li><strong><code translate="no" dir="ltr">usage</code></strong>: The accumulated usage (running total) since the start of the interaction.</li>
<li><strong><code translate="no" dir="ltr">step_usage</code></strong>: The usage of this specific step.</li>
</ul>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded><code translate="no" dir="ltr">event: step.stop
data: {&#34;index&#34;: 2, &#34;event_type&#34;: &#34;step.stop&#34;, &#34;usage&#34;: {&#34;total_tokens&#34;: 4650, &#34;total_input_tokens&#34;: 3577, &#34;total_output_tokens&#34;: 305, &#34;total_cached_tokens&#34;: 0}, &#34;step_usage&#34;: {&#34;total_tokens&#34;: 303, &#34;total_input_tokens&#34;: 31, &#34;total_output_tokens&#34;: 3, &#34;total_cached_tokens&#34;: 0}}
</code></pre></devsite-code>
<h3 id="event-interaction-completed" data-text="interaction.completed" tabindex="-1"><code translate="no" dir="ltr">interaction.completed</code></h3>

<p>Sent when the interaction is finished. Contains the final interaction object with <code translate="no" dir="ltr">usage</code> statistics. In non-streaming mode, this is the top-level response object itself. Does not include <code translate="no" dir="ltr">steps</code> in the response.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">completed</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"interaction"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"v1_abc123"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"completed"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"usage"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"total_input_tokens"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">7</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"total_output_tokens"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">12</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"total_tokens"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">19</span><span class="devsite-syntax-p">}},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"interaction.completed"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h3 id="event-error" data-text="error" tabindex="-1"><code translate="no" dir="ltr">error</code></h3>

<p>Sent when an error occurs during the interaction. Contains an error object with a message and code.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">error</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"error"</span><span class="devsite-syntax-p">:{</span><span class="devsite-syntax-s">"message"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"Deadline expired before operation could complete."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"code"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"gateway_timeout"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"error"</span><span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h2 id="streaming-with-tools" data-text="Streaming with tools" tabindex="-1">Streaming with tools</h2>

<p>The Interactions API supports streaming with both client-side tools (function
calling) and server-side tools (Google Search, Code Execution, etc.) in a single
request. During streaming, tool invocations appear as typed steps in the event
stream. For function calls, the <code translate="no" dir="ltr">step.start</code> event delivers the function name,
and <code translate="no" dir="ltr">step.delta</code> events stream the arguments as JSON strings
(<code translate="no" dir="ltr">arguments_delta</code>). You must accumulate these deltas to get the full arguments.
Server-side tools like Google Search are executed automatically by the API,
producing <code translate="no" dir="ltr">google_search_call</code> and <code translate="no" dir="ltr">google_search_result</code> steps.</p>

<h3 id="streaming-with-function-calling" data-text="Streaming with function calling" tabindex="-1">Streaming with function calling</h3>

<p>To perform function calling with streaming, the client must handle a multi-turn
conversation:</p>

<ol>
<li><strong>Turn 1 (Function Request):</strong> Call <code translate="no" dir="ltr">interactions.create</code> with <code translate="no" dir="ltr">stream: true</code>
and your defined <code translate="no" dir="ltr">tools</code>. The API will stream a <code translate="no" dir="ltr">function_call</code> step. You
must accumulate the incremental argument JSON strings (<code translate="no" dir="ltr">arguments_delta</code>) from
<code translate="no" dir="ltr">step.delta</code> events until the interaction completes with the status
<code translate="no" dir="ltr">requires_action</code>.</li>
<li><strong>Turn 2 (Sending Result):</strong> Call <code translate="no" dir="ltr">interactions.create</code> again, passing the
<code translate="no" dir="ltr">previous_interaction_id</code> (matching the ID of the first interaction) and
sending a <code translate="no" dir="ltr">function_result</code> block within the <code translate="no" dir="ltr">input</code> array. This resumes the
stream, allowing the model to generate its final response.</li>
</ol>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">weather_tool</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span>
    <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"function"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-s2">"name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-s2">"description"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Get the current weather in a given location"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-s2">"parameters"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"properties"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"description"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"The city and state, e.g. San Francisco, CA"</span>
            <span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-s2">"required"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">]</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1"># Turn 1: Request function call</span>
<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">weather_tool</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What is the weather in Paris right now?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">first_interaction_id</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-kc">None</span>
<span class="devsite-syntax-n">func_call_id</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-kc">None</span>
<span class="devsite-syntax-n">func_call_name</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-kc">None</span>
<span class="devsite-syntax-n">func_args_accumulated</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">""</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"interaction.created"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">first_interaction_id</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">step</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-n">func_call_id</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span>
            <span class="devsite-syntax-n">func_call_name</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"arguments_delta"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-n">func_args_accumulated</span> <span class="devsite-syntax-o">+=</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">arguments</span>

<span class="devsite-syntax-c1"># Turn 2: Execute tool and send the result back to resume stream</span>
<span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">func_call_id</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-c1"># Execute weather_tool using accumulated arguments</span>
    <span class="devsite-syntax-n">dummy_result</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"content"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'{"weather": "Sunny and 22°C"}'</span><span class="devsite-syntax-p">}]</span>
    <span class="devsite-syntax-p">}</span>

    <span class="devsite-syntax-n">stream2</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-n">previous_interaction_id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">first_interaction_id</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"function_result"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">func_call_name</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"call_id"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">func_call_id</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"result"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">dummy_result</span>
        <span class="devsite-syntax-p">}],</span>
        <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-p">)</span>

    <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream2</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">weatherTool</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">description</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Get the current weather in a given location"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">parameters</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">properties</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">location</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">description</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"The city and state, e.g. San Francisco, CA"</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">required</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">};</span>

<span class="devsite-syntax-c1">// Turn 1: Request function call</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">weatherTool</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What is the weather in Paris right now?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">firstInteractionId</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">funcCallId</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">funcCallName</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">funcArgsAccumulated</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"interaction.created"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">firstInteractionId</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">funcCallId</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">funcCallName</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"arguments_delta"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">funcArgsAccumulated</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">+=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arguments</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1">// Turn 2: Execute tool and send the result back to resume stream</span>
<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">funcCallId</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">firstInteractionId</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">funcCallName</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">dummyResult</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{"weather": "Sunny and 22°C"}'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">};</span>

<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream2</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">previous_interaction_id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">firstInteractionId</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_result"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">funcCallName</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">call_id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">funcCallId</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">dummyResult</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream2</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_1" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDeltaData</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionResponse</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.utils.EventStream</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Count from 1 to 25."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">stream</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateInteractionResponse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">));</span>

<span class="devsite-syntax-k">try</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">EventStream&lt;InteractionSSEStreamEvent&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">events</span><span class="devsite-syntax-p">())</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionSSEStreamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">InteractionSSEEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">data</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-n">StepDeltaData</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">delta</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">ifPresent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">::</span><span class="devsite-syntax-n">print</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_1" data-text="REST" tabindex="-1">REST</h3><p><strong>Turn 1:</strong> Request function call</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--no-buffer<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "What is the weather in Paris right now?",</span>
<span class="devsite-syntax-s1">    "stream": true,</span>
<span class="devsite-syntax-s1">    "tools": [</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "function",</span>
<span class="devsite-syntax-s1">        "name": "get_weather",</span>
<span class="devsite-syntax-s1">        "description": "Get the current weather in a given location",</span>
<span class="devsite-syntax-s1">        "parameters": {</span>
<span class="devsite-syntax-s1">          "type": "object",</span>
<span class="devsite-syntax-s1">          "properties": {</span>
<span class="devsite-syntax-s1">            "location": {</span>
<span class="devsite-syntax-s1">              "type": "string",</span>
<span class="devsite-syntax-s1">              "description": "The city and state, e.g. San Francisco, CA"</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">          },</span>
<span class="devsite-syntax-s1">          "required": ["location"]</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ]</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code>
<p><strong>Turn 2:</strong> Send the function result using the <code translate="no" dir="ltr">previous_interaction_id</code> and <code translate="no" dir="ltr">call_id</code> from Turn 1</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--no-buffer<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "previous_interaction_id": "v1_ChdGUVFJYXBXVUdLVEF4TjhQ...",</span>
<span class="devsite-syntax-s1">    "stream": true,</span>
<span class="devsite-syntax-s1">    "input": [</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "function_result",</span>
<span class="devsite-syntax-s1">        "name": "get_weather",</span>
<span class="devsite-syntax-s1">        "call_id": "CALL_ID",</span>
<span class="devsite-syntax-s1">        "result": {</span>
<span class="devsite-syntax-s1">          "content": [</span>
<span class="devsite-syntax-s1">            {</span>
<span class="devsite-syntax-s1">              "type": "text",</span>
<span class="devsite-syntax-s1">              "text": "{\"weather\": \"Sunny and 22°C\"}"</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">          ]</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ]</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="streaming-with-multiple-tools" data-text="Streaming with multiple tools" tabindex="-1">Streaming with multiple tools</h3>

<p>The following example uses both a <code translate="no" dir="ltr">function</code> tool and <code translate="no" dir="ltr">google_search</code> in one request:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">tools</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[</span>
    <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"google_search"</span><span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"function"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"description"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Get the current weather in a given location"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"parameters"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"properties"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"description"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"The city and state, e.g. San Francisco, CA"</span>
                <span class="devsite-syntax-p">}</span>
            <span class="devsite-syntax-p">},</span>
            <span class="devsite-syntax-s2">"required"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">]</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">]</span>

<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">tools</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Search what is the largest mountain in Europe and what the weather is there right now?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">step</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n</span><span class="devsite-syntax-s2">--- Step </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">index</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2"> ---"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-c1"># Show details for tool steps</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"google_search_call"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"  Search ID: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"google_search_result"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"  Result for: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">call_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"  Function: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">(</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">arguments</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">)"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"google_search_call"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"  Queries: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">arguments</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"arguments_delta"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"  Args chunk: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">arguments</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"interaction.completed"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n\n</span><span class="devsite-syntax-s2">Status: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">status</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">status</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"requires_action"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Action required: provide function call results to continue."</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"google_search"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"get_weather"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">description</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Get the current weather in a given location"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">parameters</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">properties</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">location</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">description</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"The city and state, e.g. San Francisco, CA"</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">required</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"location"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">];</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Search what is the largest mountain in Europe and what the weather is there right now?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`\n--- Step </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">index</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb"> ---`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-c1">// Show details for tool steps</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"google_search_call"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`  Search ID: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"google_search_result"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`  Result for: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">call_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"function_call"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`  Function: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">(</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arguments</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">)`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"google_search_call"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`  Queries: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arguments</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">queries</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"arguments_delta"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`  Args chunk: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arguments</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"interaction.completed"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`\n\nStatus: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">status</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">status</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"requires_action"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Action required: provide function call results to continue."</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_2" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDeltaData</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionResponse</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.utils.EventStream</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Count from 1 to 25."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">stream</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateInteractionResponse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">));</span>

<span class="devsite-syntax-k">try</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">EventStream&lt;InteractionSSEStreamEvent&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">events</span><span class="devsite-syntax-p">())</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionSSEStreamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">InteractionSSEEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">data</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-n">StepDeltaData</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">delta</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">ifPresent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">::</span><span class="devsite-syntax-n">print</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_2" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--no-buffer<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "Search what is the largest mountain in Europe and what the weather is there right now?",</span>
<span class="devsite-syntax-s1">    "stream": true,</span>
<span class="devsite-syntax-s1">    "tools": [</span>
<span class="devsite-syntax-s1">      { "type": "google_search" },</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "function",</span>
<span class="devsite-syntax-s1">        "name": "get_weather",</span>
<span class="devsite-syntax-s1">        "description": "Get the current weather in a given location",</span>
<span class="devsite-syntax-s1">        "parameters": {</span>
<span class="devsite-syntax-s1">          "type": "object",</span>
<span class="devsite-syntax-s1">          "properties": {</span>
<span class="devsite-syntax-s1">            "location": {</span>
<span class="devsite-syntax-s1">              "type": "string",</span>
<span class="devsite-syntax-s1">              "description": "The city and state, e.g. San Francisco, CA"</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">          },</span>
<span class="devsite-syntax-s1">          "required": ["location"]</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ]</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Transact-SQL" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">created</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"object"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"model"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"gemini-3.7-flash"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.created"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">status_update</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction_id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.status_update"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"mkutnkgn"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"signature"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">""</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"google_search_call"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"signature"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"google_search_call"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"arguments"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"queries"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-o">[</span><span class="devsite-syntax-n">"largest mountain in Europe"</span><span class="devsite-syntax-o">]</span><span class="devsite-syntax-err">}}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"call_id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"mkutnkgn"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"signature"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">""</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"google_search_result"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"signature"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"google_search_result"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"is_error"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-k">false</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"signature"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought_signature"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"ktr5aysg"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"function_call"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"name"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"get_weather"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"arguments"</span><span class="devsite-syntax-err">:{}}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"arguments"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"{\"</span><span class="devsite-syntax-n">location</span><span class="devsite-syntax-err">\</span><span class="devsite-syntax-ss">":\"</span><span class="devsite-syntax-n">Mount</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Elbrus</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Russia</span><span class="devsite-syntax-err">\</span><span class="devsite-syntax-ss">"}"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"arguments_delta"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">completed</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"requires_action"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"usage"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"total_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">299</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_input_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">138</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"input_tokens_by_modality"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-o">[</span><span class="devsite-syntax-n">{"modality":"text","tokens":138}</span><span class="devsite-syntax-o">]</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_cached_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_output_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">20</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_tool_use_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_thought_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">141</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"created"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"2026-05-12T17:24:26Z"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"updated"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"2026-05-12T17:24:26Z"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"service_tier"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"standard"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"object"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"model"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"gemini-3.7-flash"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.completed"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">done</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">[</span><span class="devsite-syntax-n">DONE</span><span class="devsite-syntax-o">]</span>
</code></pre></devsite-code>
<h2 id="streaming-with-thinking" data-text="Streaming with thinking" tabindex="-1">Streaming with thinking</h2>

<p>When the model uses thinking, you&#39;ll receive <code translate="no" dir="ltr">thought</code> steps with two distinct delta types: <code translate="no" dir="ltr">thought_summary</code> (incremental text or image summary content), and <code translate="no" dir="ltr">thought_signature</code> (an encrypted representation of the model&#39;s internal reasoning, sent as the last delta before <code translate="no" dir="ltr">step.stop</code>). If <code translate="no" dir="ltr">thinking_summaries</code> is enabled, <code translate="no" dir="ltr">thought_summary</code> deltas stream a summary of the model&#39;s reasoning. For more details on thinking, see the <a href="/gemini-api/docs/thinking">Thinking guide</a>.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_3" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What is the greatest common divisor of 1071 and 462?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">generation_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"thinking_summaries"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"auto"</span>
    <span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n</span><span class="devsite-syntax-s2">--- Step: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2"> ---"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"thought_summary"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_3" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What is the greatest common divisor of 1071 and 462?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generation_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">thinking_summaries</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"auto"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`\n--- Step: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb"> ---`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought_summary"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_3" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDeltaData</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionResponse</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.utils.EventStream</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Count from 1 to 25."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">stream</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateInteractionResponse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">));</span>

<span class="devsite-syntax-k">try</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">EventStream&lt;InteractionSSEStreamEvent&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">events</span><span class="devsite-syntax-p">())</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionSSEStreamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">InteractionSSEEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">data</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-n">StepDeltaData</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">delta</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">ifPresent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">::</span><span class="devsite-syntax-n">print</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_3" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--no-buffer<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "What is the greatest common divisor of 1071 and 462?",</span>
<span class="devsite-syntax-s1">    "stream": true,</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "thinking_summaries": "auto"</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Carbon" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">created</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"interaction"</span><span class="devsite-syntax-p">:{</span><span class="devsite-syntax-s">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"object"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"interaction"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"model"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"interaction.created"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">status_update</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"interaction_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"interaction.status_update"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">start</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"step"</span><span class="devsite-syntax-p">:{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"thought"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"step.start"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"delta"</span><span class="devsite-syntax-p">:{</span><span class="devsite-syntax-s">"content"</span><span class="devsite-syntax-p">:{</span><span class="devsite-syntax-s">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"**Implementing Euclidean Algorithm**\n\nI've just worked through a detailed example applying the Euclidean algorithm to find the GCD of 1071 and 462, confirming its step-by-step nature. The calculations went smoothly, tracking the remainders until zero. My focus is now solidifying the implementation logic, ensuring accuracy and considering potential edge cases. I'll translate this example into code.\n\n\n"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"text"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"thought_summary"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"step.delta"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"delta"</span><span class="devsite-syntax-p">:{</span><span class="devsite-syntax-s">"signature"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"thought_signature"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"step.delta"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stop</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"step.stop"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">start</span>
<span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s">"index"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-s">"step"</span><span class="devsite-syntax-p">:{</span><span class="devsite-syntax-s">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"model_output"</span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-s">"event_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s">"step.start"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-o">...</span>
</code></pre></devsite-code>
<h2 id="streaming-with-agents" data-text="Streaming with agents" tabindex="-1">Streaming with agents</h2>

<p>The Interactions API supports agents like Deep Research. Agents use <code translate="no" dir="ltr">background=True</code> and return results asynchronously, but you can also stream agent interactions to receive progress updates and intermediate steps as they happen. For more details, see the <a href="/gemini-api/docs/background-execution">Background execution guide</a> and the <a href="/gemini-api/docs/deep-research">Deep Research guide</a>.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_4" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"deep-research-preview-04-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Research the latest advances in quantum computing."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">background</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">agent_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"deep-research"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"thinking_summaries"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"auto"</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n</span><span class="devsite-syntax-s2">--- Step: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2"> ---"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"thought_summary"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"interaction.completed"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n\n</span><span class="devsite-syntax-s2">Total Tokens: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">usage</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">total_tokens</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_4" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"deep-research-preview-04-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Research the latest advances in quantum computing."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">background</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"deep-research"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">thinking_summaries</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"auto"</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.start"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`\n--- Step: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb"> ---`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"thought_summary"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"interaction.completed"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`\n\nTotal Tokens: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">usage</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">total_tokens</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_4" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDeltaData</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionResponse</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.utils.EventStream</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Count from 1 to 25."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">stream</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateInteractionResponse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">));</span>

<span class="devsite-syntax-k">try</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">EventStream&lt;InteractionSSEStreamEvent&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">events</span><span class="devsite-syntax-p">())</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionSSEStreamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">InteractionSSEEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">data</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-n">StepDeltaData</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">delta</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">ifPresent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">::</span><span class="devsite-syntax-n">print</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_4" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--no-buffer<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "deep-research-preview-04-2026",</span>
<span class="devsite-syntax-s1">    "input": "Research the latest advances in quantum computing.",</span>
<span class="devsite-syntax-s1">    "stream": true,</span>
<span class="devsite-syntax-s1">    "background": true,</span>
<span class="devsite-syntax-s1">    "agent_config": {</span>
<span class="devsite-syntax-s1">      "type": "deep-research",</span>
<span class="devsite-syntax-s1">      "thinking_summaries": "auto"</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Transact-SQL" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">created</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"object"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"agent"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"deep-research-preview-04-2026"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.created"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">status_update</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction_id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.status_update"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"content"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"***Generating research plan***\n\nTo best answer your request, I'm starting by constructing a comprehensive research plan. This will outline the key areas I need to investigate and the strategy I'll use to connect them."</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought_summary"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-p">...</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">additional</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">thought</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">...</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"model_output"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"# The Quantum Inflection Point: Exhaustive Analysis of Hardware, Algorithms, and Market Dynamics in 2026\n\n## Executive Summary\n\n..."</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">completed</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"completed"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"usage"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"total_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1117031</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_input_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">428865</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_output_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">22294</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_thought_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">26213</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"created"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"2026-05-12T17:24:27Z"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"updated"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"2026-05-12T17:24:27Z"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"object"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"agent"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"deep-research-preview-04-2026"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.completed"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">done</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">[</span><span class="devsite-syntax-n">DONE</span><span class="devsite-syntax-o">]</span>
</code></pre></devsite-code>
<h2 id="streaming-image-generation" data-text="Streaming image generation" tabindex="-1">Streaming image generation</h2>

<p>The Interactions API supports streaming multiple output modalities simultaneously. By requesting both <code translate="no" dir="ltr">text</code> and <code translate="no" dir="ltr">image</code> in the <code translate="no" dir="ltr">response_format</code>, you can receive interleaved text and generated images in the same stream.</p>

<p>The following example uses <code translate="no" dir="ltr">gemini-3.1-flash-image</code> (Nano Banana 2) to search for information and generate a story with interleaved illustrations.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_5" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">stream</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.1-flash-image"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"google_search"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"search_types"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"web_search"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"image_search"</span><span class="devsite-syntax-p">]}],</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">response_format</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"image"</span><span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">event</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">stream</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">event_type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"image"</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n</span><span class="devsite-syntax-s2">[Image chunk: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-nb">len</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delta</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2"> bytes]"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_5" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.1-flash-image"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"google_search"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">search_types</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"web_search"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image_search"</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">response_format</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stream</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">event_type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step.delta"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stdout</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"image"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`\n[Image chunk: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">delta</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">length</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb"> bytes]`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_5" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.StepDeltaData</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextDelta</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionResponse</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.utils.EventStream</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Count from 1 to 25."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">stream</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateInteractionResponse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">));</span>

<span class="devsite-syntax-k">try</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">EventStream&lt;InteractionSSEStreamEvent&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">events</span><span class="devsite-syntax-p">())</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionSSEStreamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">events</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">InteractionSSEEvent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">streamEvent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">data</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-n">StepDeltaData</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">StepDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">event</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">delta</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">instanceof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-n">TextDelta</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">ifPresent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">::</span><span class="devsite-syntax-n">print</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_5" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--no-buffer<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.1-flash-image",</span>
<span class="devsite-syntax-s1">    "input": "Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",</span>
<span class="devsite-syntax-s1">    "stream": true,</span>
<span class="devsite-syntax-s1">    "tools": [</span>
<span class="devsite-syntax-s1">      { "type": "google_search",</span>
<span class="devsite-syntax-s1">        "search_types": ["web_search", "image_search"]</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ],</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "thinking_summaries": "auto"</span>
<span class="devsite-syntax-s1">    },</span>
<span class="devsite-syntax-s1">    "response_format": [</span>
<span class="devsite-syntax-s1">      { "type": "text" }, { "type": "image"}</span>
<span class="devsite-syntax-s1">    ]</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Transact-SQL" syntax-guessed><code translate="no" dir="ltr"><span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">created</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"object"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"model"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"gemini-3.1-flash-image"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.created"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">status_update</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction_id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"in_progress"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.status_update"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"model_output"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"Here is a short illustrated story about the Colosseum...\n\n### Part 1: The New Flavian Amphitheater\n\n..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-p">...</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">0</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"signature"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought_signature"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"model_output"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"mime_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"image/jpeg"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"data"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAoHBwgHBgoICAgLCg..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"image"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"### Part 2: The Hypogeum and the Wait\n\n..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-p">...</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"signature"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"thought_signature"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">3</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">start</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">4</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"step"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"model_output"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.start"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">4</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"mime_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"image/jpeg"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"data"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"/9j/4AAQSkZJRgABAQAAAQABAAD/..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"image"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">delta</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">4</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"delta"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"### Part 3: The Moment of Spectacle\n\n..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"text"</span><span class="devsite-syntax-err">}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.delta"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-p">...</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">stop</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"index"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">4</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"step.stop"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-n">completed</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-err">{</span><span class="devsite-syntax-ss">"interaction"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"id"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"v1_..."</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"status"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"completed"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"usage"</span><span class="devsite-syntax-err">:{</span><span class="devsite-syntax-ss">"total_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">6128</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_input_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">29</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"total_output_tokens"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-mi">6099</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"output_tokens_by_modality"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-o">[</span><span class="devsite-syntax-n">{"modality":"image","tokens":4480}</span><span class="devsite-syntax-o">]</span><span class="devsite-syntax-err">}}</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-ss">"event_type"</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-ss">"interaction.completed"</span><span class="devsite-syntax-err">}</span>

<span class="devsite-syntax-nl">event</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">done</span>
<span class="devsite-syntax-k">data</span><span class="devsite-syntax-err">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">[</span><span class="devsite-syntax-n">DONE</span><span class="devsite-syntax-o">]</span>
</code></pre></devsite-code>
<h2 id="handling-unknown-events" data-text="Handling unknown events" tabindex="-1">Handling unknown events</h2>

<p>In accordance with the API&#39;s versioning policy, new event types and delta types may be added over time. Your code should handle unknown event types gracefully—log and skip any events you don&#39;t recognize rather than throwing an error.</p>

<h2 id="whats-next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li>Learn more about the <a href="/gemini-api/docs/interactions-overview">Interactions API</a>.</li>
<li>Explore <a href="/gemini-api/docs/function-calling">Function calling</a> with tools.</li>
<li>Learn about <a href="/gemini-api/docs/thinking">Thinking</a> for enhanced reasoning.</li>
<li>Try the <a href="/gemini-api/docs/deep-research">Deep Research agent</a> for long-running tasks.</li>
<li>See the <a href="/api/interactions-api">Interactions API reference</a> for all event types and delta types.</li>
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