








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/agent-environment"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/agent-environment" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/agent-environment" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/agent-environment?hl=sq" /><title>Environments in managed agents &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Environments in managed agents &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta name="description" content="Learn about persistent execution environments for managed agents in the Gemini API, including pre-installed software, snapshots, and configuration options.">
  <meta property="og:description" content="Learn about persistent execution environments for managed agents in the Gemini API, including pre-installed software, snapshots, and configuration options."><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/agent-environment"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
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
      Environments in managed agents<devsite-actions hidden data-nosnippet>
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



<p>Environments are managed Linux sandboxes that give agents an isolated place to
execute code and persist files. They are decoupled from interaction context, so you can reuse the same environment across multiple interactions or start fresh at any time.</p>

<p>The following example demonstrates how to create an interaction with a fresh
remote environment and retrieve its ID:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Environment ID: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environment_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Environment ID: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environment_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": "Install pandas and matplotlib, verify the imports, and print the versions.",</span>
<span class="devsite-syntax-s1">    "environment": "remote"</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="the-environment-parameter" data-text="The environment parameter" tabindex="-1">The <code translate="no" dir="ltr">environment</code> parameter</h2>

<p>The <code translate="no" dir="ltr">environment</code> parameter accepts three forms:</p>

<table>
<thead>
<tr>
<th style="text-align: left">Form</th>
<th style="text-align: left">Example</th>
<th style="text-align: left">When to use</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">&quot;remote&quot;</code></td>
<td style="text-align: left"><code translate="no" dir="ltr">environment=&quot;remote&quot;</code></td>
<td style="text-align: left">Provision a fresh sandbox.</td>
</tr>
<tr>
<td style="text-align: left">Environment ID</td>
<td style="text-align: left"><code translate="no" dir="ltr">environment=&quot;env_abc123&quot;</code></td>
<td style="text-align: left">Reuse an existing sandbox with all its files and packages.</td>
</tr>
<tr>
<td style="text-align: left">Config object</td>
<td style="text-align: left"><code translate="no" dir="ltr">environment={...}</code></td>
<td style="text-align: left">Provision a new sandbox with sources, network rules, or both.</td>
</tr>
</tbody>
</table>

<p>The following examples demonstrate the three ways of using the <code translate="no" dir="ltr">environment</code>
parameter.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-c1"># Fresh sandbox</span>
<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Write a hello world script."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># Reuse an existing sandbox</span>
<span class="devsite-syntax-n">interaction_2</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Modify the script to accept a name argument."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environment_id</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">previous_interaction_id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># New sandbox with sources</span>
<span class="devsite-syntax-n">interaction_3</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"List all files and summarize the project."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"sources"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
            <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"repository"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"source"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"https://github.com/octocat/Spoon-Knife"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"target"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"/workspace/spoon-knife"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-c1">// Fresh sandbox</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Write a hello world script."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-c1">// Reuse an existing sandbox</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction2</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Modify the script to accept a name argument."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environment_id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">previous_interaction_id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-c1">// New sandbox with sources</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction3</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"List all files and summarize the project."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">sources</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"repository"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">source</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://github.com/octocat/Spoon-Knife"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">target</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"/workspace/spoon-knife"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_1" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_1" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Fresh sandbox</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": [{"type": "text", "text": "Write a hello world script."}],</span>
<span class="devsite-syntax-s1">    "environment": "remote"</span>
<span class="devsite-syntax-s1">}'</span>

<span class="devsite-syntax-c1"># Reuse an existing sandbox (replace $ENV_ID and $INTERACTION_ID with values from the previous response)</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"{</span>
<span class="devsite-syntax-s2">    \"agent\": \"antigravity-preview-05-2026\",</span>
<span class="devsite-syntax-s2">    \"input\": [{\"type\": \"text\", \"text\": \"Modify the script to accept a name argument.\"}],</span>
<span class="devsite-syntax-s2">    \"environment\": \"</span><span class="devsite-syntax-nv">$ENV_ID</span><span class="devsite-syntax-s2">\",</span>
<span class="devsite-syntax-s2">    \"previous_interaction_id\": \"</span><span class="devsite-syntax-nv">$INTERACTION_ID</span><span class="devsite-syntax-s2">\"</span>
<span class="devsite-syntax-s2">}"</span>

<span class="devsite-syntax-c1"># New sandbox with sources</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": [{"type": "text", "text": "List all files and summarize the project."}],</span>
<span class="devsite-syntax-s1">    "environment": {</span>
<span class="devsite-syntax-s1">        "type": "remote",</span>
<span class="devsite-syntax-s1">        "sources": [</span>
<span class="devsite-syntax-s1">            {</span>
<span class="devsite-syntax-s1">                "type": "repository",</span>
<span class="devsite-syntax-s1">                "source": "https://github.com/octocat/Spoon-Knife",</span>
<span class="devsite-syntax-s1">                "target": "/workspace/spoon-knife"</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">        ]</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="configure-an-environment" data-text="Configure an environment" tabindex="-1">Configure an environment</h2>

<p>One way to set up an environment is to tell the agent what you need installed.
It handles dependency resolution and troubleshooting. Once the environment is
ready, save the <code translate="no" dir="ltr">environment_id</code> and reuse it.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># Reuse the configured environment</span>
<span class="devsite-syntax-n">interaction_2</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environment_id</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">previous_interaction_id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># Reuse the configured environment</span>
<span class="devsite-syntax-n">interaction_3</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Using the tools in /workspace/tools, list the files."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environment_id</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">previous_interaction_id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">interaction_2</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction2</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environment_id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">previous_interaction_id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction3</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Using the tools in /workspace/tools, list the files."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environment_id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">previous_interaction_id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction2</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_2" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_2" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Create interaction</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",</span>
<span class="devsite-syntax-s1">    "environment": "remote"</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="mount_from_a_source" data-text="Mount from a source" tabindex="-1">Mount from a source</h3>

<p>If you know exactly what files the agent needs, mount them in a single call
instead of iterating. The <code translate="no" dir="ltr">environment</code> config object accepts a <code translate="no" dir="ltr">sources</code> array
with three types:</p>

<table>
<thead>
<tr>
<th style="text-align: left">Source type</th>
<th style="text-align: left"><code translate="no" dir="ltr">type</code> value</th>
<th style="text-align: left">Description</th>
<th style="text-align: left">Limit</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left">Git repository</td>
<td style="text-align: left"><code translate="no" dir="ltr">repository</code></td>
<td style="text-align: left">Clones a repository from a URL into the sandbox at <code translate="no" dir="ltr">target</code>.</td>
<td style="text-align: left">500 MB</td>
</tr>
<tr>
<td style="text-align: left">Cloud Storage</td>
<td style="text-align: left"><code translate="no" dir="ltr">gcs</code></td>
<td style="text-align: left">Copies a file or directory from Cloud Storage into the sandbox at <code translate="no" dir="ltr">target</code>.</td>
<td style="text-align: left">2 GB</td>
</tr>
<tr>
<td style="text-align: left">Inline content</td>
<td style="text-align: left"><code translate="no" dir="ltr">inline</code></td>
<td style="text-align: left">Writes raw text content to a file in the sandbox at <code translate="no" dir="ltr">target</code>.</td>
<td style="text-align: left">1 MB per file, 2 MB total</td>
</tr>
</tbody>
</table>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_3" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"List all files under /workspace and describe what you find."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"sources"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
            <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"repository"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"source"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"https://github.com/octocat/Spoon-Knife"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"target"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"/workspace/spoon-knife"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-p">},</span>
            <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"gcs"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"source"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"gs://cloud-samples-data/bigquery/us-states/"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"target"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"/workspace/gcs-data"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-p">},</span>
            <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"inline"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"content"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"# Project Notes</span><span class="devsite-syntax-se">\n\n</span><span class="devsite-syntax-s2">- Analyze state population data</span><span class="devsite-syntax-se">\n</span><span class="devsite-syntax-s2">- Create visualizations</span><span class="devsite-syntax-se">\n</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"target"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"/workspace/notes/readme.md"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_3" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"List all files under /workspace and describe what you find."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">sources</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"repository"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">source</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://github.com/octocat/Spoon-Knife"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">target</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"/workspace/spoon-knife"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gcs"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">source</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gs://cloud-samples-data/bigquery/us-states/"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">target</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"/workspace/gcs-data"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"inline"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"# Project Notes\n\n- Analyze state population data\n- Create visualizations\n"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">target</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"/workspace/notes/readme.md"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_3" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_3" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Create interaction with sources</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": "List all files under /workspace and describe what you find.",</span>
<span class="devsite-syntax-s1">    "environment": {</span>
<span class="devsite-syntax-s1">        "type": "remote",</span>
<span class="devsite-syntax-s1">        "sources": [</span>
<span class="devsite-syntax-s1">            {</span>
<span class="devsite-syntax-s1">                "type": "repository",</span>
<span class="devsite-syntax-s1">                "source": "https://github.com/octocat/Spoon-Knife",</span>
<span class="devsite-syntax-s1">                "target": "/workspace/spoon-knife"</span>
<span class="devsite-syntax-s1">            },</span>
<span class="devsite-syntax-s1">            {</span>
<span class="devsite-syntax-s1">                "type": "gcs",</span>
<span class="devsite-syntax-s1">                "source": "gs://cloud-samples-data/bigquery/us-states/",</span>
<span class="devsite-syntax-s1">                "target": "/workspace/gcs-data"</span>
<span class="devsite-syntax-s1">            },</span>
<span class="devsite-syntax-s1">            {</span>
<span class="devsite-syntax-s1">                "type": "inline",</span>
<span class="devsite-syntax-s1">                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",</span>
<span class="devsite-syntax-s1">                "target": "/workspace/notes/readme.md"</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">        ]</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>You can combine both approaches: mount known sources declaratively, then iterate
with follow-up interactions to install packages or run setup scripts. You can&#39;t
set root (<code translate="no" dir="ltr">/</code>) as target when adding a custom source, you must always specify a
sub-directory.</p>

<h3 id="hooks" data-text="Hooks" tabindex="-1">Hooks</h3>

<p>You can also mount a <code translate="no" dir="ltr">.agents/hooks.json</code> configuration file and custom interception scripts into the sandbox to enforce security guardrails or run automated validations whenever tools execute. For schema definitions and code examples, see <a href="/gemini-api/docs/agent-hooks">Hooks</a>.</p>

<h3 id="private-sources" data-text="Private sources" tabindex="-1">Private sources</h3>

<p>You can also download from private GitHub repositories or private Cloud
Storage buckets by adding the credentials in the network configuration:</p>

<p>For <strong>private Git repositories</strong>, use <code translate="no" dir="ltr">Basic</code> authentication with your
<a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">GitHub Personal Access Token
(PAT)</a>.
Encode the token using <code translate="no" dir="ltr">x-oauth-basic</code> as the username:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-nb">echo</span><span class="devsite-syntax-w"> </span>-n<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-oauth-basic:ghp_YourPATHere"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>base64
</code></pre></devsite-code><div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_4" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Run the test for my backend app and fix any issue."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"sources"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
            <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"repository"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"source"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"https://github.com/your-org/backend"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"target"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"/backend-app"</span>
            <span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-s2">"network"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"allowlist"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
                <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"github.com"</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"transform"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                        <span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Basic YOUR_BASE64_TOKEN"</span>
                    <span class="devsite-syntax-p">}</span>
                <span class="devsite-syntax-p">},</span>
                <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"*"</span>
                <span class="devsite-syntax-p">}</span>
            <span class="devsite-syntax-p">]</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_4" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Run the test for my backend app and fix any issue."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">sources</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"repository"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">source</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://github.com/your-org/backend"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">target</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"/backend-app"</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">network</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">allowlist</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"github.com"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">transform</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Basic YOUR_BASE64_TOKEN"</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"*"</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="java_4" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_4" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": "Run the test for my backend app and fix any issue.",</span>
<span class="devsite-syntax-s1">    "environment": {</span>
<span class="devsite-syntax-s1">        "type": "remote",</span>
<span class="devsite-syntax-s1">        "sources": [</span>
<span class="devsite-syntax-s1">            {</span>
<span class="devsite-syntax-s1">                "type": "repository",</span>
<span class="devsite-syntax-s1">                "source": "https://github.com/your-org/backend",</span>
<span class="devsite-syntax-s1">                "target": "/backend-app"</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">        ],</span>
<span class="devsite-syntax-s1">        "network": {</span>
<span class="devsite-syntax-s1">            "allowlist": [</span>
<span class="devsite-syntax-s1">                {</span>
<span class="devsite-syntax-s1">                    "domain": "github.com",</span>
<span class="devsite-syntax-s1">                    "transform": {</span>
<span class="devsite-syntax-s1">                        "Authorization": "Basic YOUR_BASE64_TOKEN"</span>
<span class="devsite-syntax-s1">                    }</span>
<span class="devsite-syntax-s1">                },</span>
<span class="devsite-syntax-s1">                {</span>
<span class="devsite-syntax-s1">                    "domain": "*"</span>
<span class="devsite-syntax-s1">                }</span>
<span class="devsite-syntax-s1">            ]</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>For <strong>private Cloud Storage buckets</strong>, use a standard OAuth 2.0 Bearer token:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">gcloud<span class="devsite-syntax-w"> </span>auth<span class="devsite-syntax-w"> </span>print-access-token
</code></pre></devsite-code><div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_5" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Analyze the discrepancies across the data in workspace"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"sources"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
            <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"gcs"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"source"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"gs://my-private-bucket/data"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"target"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"/workspace"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-s2">"network"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"allowlist"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
                <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"*.googleapis.com"</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"transform"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                        <span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Bearer YOUR_GCS_TOKEN"</span>
                    <span class="devsite-syntax-p">}</span>
                <span class="devsite-syntax-p">},</span>
                <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"*"</span>
                <span class="devsite-syntax-p">}</span>
            <span class="devsite-syntax-p">]</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_5" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Analyze the discrepancies across the data in workspace"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">sources</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gcs"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">source</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gs://my-private-bucket/data"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">target</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"/workspace"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">network</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">allowlist</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"storage.googleapis.com"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">transform</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Bearer YOUR_GCS_TOKEN"</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"*"</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="java_5" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_5" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": "Analyze the discrepancies across the data in workspace",</span>
<span class="devsite-syntax-s1">    "environment": {</span>
<span class="devsite-syntax-s1">        "type": "remote",</span>
<span class="devsite-syntax-s1">        "sources": [</span>
<span class="devsite-syntax-s1">            {</span>
<span class="devsite-syntax-s1">                "type": "gcs",</span>
<span class="devsite-syntax-s1">                "source": "gs://my-private-bucket/data",</span>
<span class="devsite-syntax-s1">                "target": "/workspace"</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">        ],</span>
<span class="devsite-syntax-s1">        "network": {</span>
<span class="devsite-syntax-s1">            "allowlist": [</span>
<span class="devsite-syntax-s1">                {</span>
<span class="devsite-syntax-s1">                    "domain": "storage.googleapis.com",</span>
<span class="devsite-syntax-s1">                    "transform": {</span>
<span class="devsite-syntax-s1">                        "Authorization": "Bearer YOUR_GCS_TOKEN"</span>
<span class="devsite-syntax-s1">                    }</span>
<span class="devsite-syntax-s1">                },</span>
<span class="devsite-syntax-s1">                {</span>
<span class="devsite-syntax-s1">                    "domain": "*"</span>
<span class="devsite-syntax-s1">                }</span>
<span class="devsite-syntax-s1">            ]</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="pre-installed-software" data-text="Pre-installed software" tabindex="-1">Pre-installed software</h2>

<p>The sandbox runs on Ubuntu and comes with runtimes and common packages
pre-installed. The agent can install additional packages at runtime using <code translate="no" dir="ltr">pip
install</code> or <code translate="no" dir="ltr">npm install</code>. Packages installed during an interaction persist when
you reuse the same <code translate="no" dir="ltr">environment_id</code>.</p>

<table>
<thead>
<tr>
<th style="text-align: left">Category</th>
<th style="text-align: left">Pre-installed packages</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left"><strong>UNIX tools</strong></td>
<td style="text-align: left"><code translate="no" dir="ltr">curl</code>, <code translate="no" dir="ltr">wget</code>, <code translate="no" dir="ltr">git</code>, <code translate="no" dir="ltr">rsync</code>, <code translate="no" dir="ltr">unzip</code>, <code translate="no" dir="ltr">ripgrep</code>, <code translate="no" dir="ltr">fd-find</code>, <code translate="no" dir="ltr">gawk</code>, <code translate="no" dir="ltr">bc</code>, <code translate="no" dir="ltr">tree</code>, <code translate="no" dir="ltr">which</code>, <code translate="no" dir="ltr">lsof</code>, <code translate="no" dir="ltr">htop</code>, <code translate="no" dir="ltr">jq</code>, <code translate="no" dir="ltr">iproute2</code>, <code translate="no" dir="ltr">procps</code>, <code translate="no" dir="ltr">gcloud CLI</code></td>
</tr>
<tr>
<td style="text-align: left"><strong>Python 3.12</strong></td>
<td style="text-align: left"><code translate="no" dir="ltr">numpy</code>, <code translate="no" dir="ltr">pandas</code>, <code translate="no" dir="ltr">requests</code>, <code translate="no" dir="ltr">google-genai</code>, <code translate="no" dir="ltr">beautifulsoup4</code>, <code translate="no" dir="ltr">pyyaml</code>, <code translate="no" dir="ltr">ast-grep-cli</code></td>
</tr>
<tr>
<td style="text-align: left"><strong>Node.js 22</strong></td>
<td style="text-align: left"><code translate="no" dir="ltr">create-next-app</code>, <code translate="no" dir="ltr">create-vite</code>, <code translate="no" dir="ltr">typescript</code></td>
</tr>
</tbody>
</table>

<h2 id="network-configuration" data-text="Network configuration" tabindex="-1">Network configuration</h2>

<p>By default, environments have unrestricted outbound network access. Use the
<code translate="no" dir="ltr">network</code> field to restrict outbound traffic to specific domains. Each rule
specifies a <code translate="no" dir="ltr">domain</code> and an optional <code translate="no" dir="ltr">transform</code> object to inject headers into
matching requests. These headers can be unique per interaction, and you can update them for the same environment.</p>

<table>
<thead>
<tr>
<th style="text-align: left">Field</th>
<th style="text-align: left">Type</th>
<th style="text-align: left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">domain</code></td>
<td style="text-align: left"><code translate="no" dir="ltr">string</code></td>
<td style="text-align: left">Domain to match. Use an exact hostname or <code translate="no" dir="ltr">*</code> for all domains.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">transform</code></td>
<td style="text-align: left"><code translate="no" dir="ltr">object</code></td>
<td style="text-align: left">Object containing flat key-value pairs representing headers to inject into matching requests, e.g. <code translate="no" dir="ltr">{&quot;Authorization&quot;: &quot;Bearer ...&quot;}</code>.</td>
</tr>
</tbody>
</table>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_6" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Fetch the latest issues from the GitHub API for my-org/my-repo."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"network"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"allowlist"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
                <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"api.github.com"</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"transform"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                        <span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Bearer ghp_your_github_token"</span>
                    <span class="devsite-syntax-p">},</span>
                <span class="devsite-syntax-p">},</span>
                <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"pypi.org"</span><span class="devsite-syntax-p">},</span>
                <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"*"</span><span class="devsite-syntax-p">},</span>
            <span class="devsite-syntax-p">]</span>
        <span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_6" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Fetch the latest issues from the GitHub API for my-org/my-repo."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">network</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">allowlist</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"api.github.com"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">transform</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Bearer ghp_your_github_token"</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"pypi.org"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"*"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_6" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_6" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": [{"type": "text", "text": "Fetch the latest issues from the GitHub API for my-org/my-repo."}],</span>
<span class="devsite-syntax-s1">    "environment": {</span>
<span class="devsite-syntax-s1">        "type": "remote",</span>
<span class="devsite-syntax-s1">        "network": {</span>
<span class="devsite-syntax-s1">            "allowlist": [</span>
<span class="devsite-syntax-s1">                {</span>
<span class="devsite-syntax-s1">                    "domain": "api.github.com",</span>
<span class="devsite-syntax-s1">                    "transform": {</span>
<span class="devsite-syntax-s1">                        "Authorization": "Bearer ghp_your_github_token"</span>
<span class="devsite-syntax-s1">                    }</span>
<span class="devsite-syntax-s1">                },</span>
<span class="devsite-syntax-s1">                {"domain": "pypi.org"},</span>
<span class="devsite-syntax-s1">                {"domain": "*"}</span>
<span class="devsite-syntax-s1">            ]</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>When an allowlist is set, only requests to explicitly listed domains are
permitted. You can use wildcards to match subdomains (e.g., <code translate="no" dir="ltr">{&quot;domain&quot;:
&quot;*.example.com&quot;}</code>), but note that this does not match the root domain
<code translate="no" dir="ltr">example.com</code>, which must be added separately. To permit all other traffic, such
as routing unlisted domains without injected headers, add <code translate="no" dir="ltr">{&quot;domain&quot;: &quot;*&quot;}</code> as a
catch-all entry.</p>

<h3 id="credentials" data-text="Credentials" tabindex="-1">Credentials</h3>

<p>You can add credentials for your agent to use by adding header transformations. The credentials are
injected in the respective HTTP headers by an egress proxy, they are never
exposed inside the sandbox as environment variables or files.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_7" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">subprocess</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-c1"># Fetch a short-lived access token from your local gcloud CLI</span>
<span class="devsite-syntax-n">gcloud_token</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">subprocess</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">check_output</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"gcloud"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"auth"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"print-access-token"</span><span class="devsite-syntax-p">],</span> <span class="devsite-syntax-n">text</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span>
<span class="devsite-syntax-p">)</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">strip</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"List the files in gs://my-bucket/reports/ using the GCS JSON API."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"network"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"allowlist"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
                <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"storage.googleapis.com"</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"transform"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                        <span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Bearer </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">gcloud_token</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>
                    <span class="devsite-syntax-p">},</span>
                <span class="devsite-syntax-p">}</span>
            <span class="devsite-syntax-p">]</span>
        <span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_7" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">execSync</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"child_process"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">gcloudToken</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">execSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"gcloud auth print-access-token"</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-nx">toString</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-nx">trim</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"List the files in gs://my-bucket/reports/ using the GCS JSON API."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">network</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">allowlist</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"storage.googleapis.com"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">transform</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-sb">`Bearer </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">gcloudToken</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_7" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_7" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": "List the files in gs://my-bucket/reports/ using the GCS JSON API.",</span>
<span class="devsite-syntax-s1">    "environment": {</span>
<span class="devsite-syntax-s1">        "type": "remote",</span>
<span class="devsite-syntax-s1">        "network": {</span>
<span class="devsite-syntax-s1">            "allowlist": [</span>
<span class="devsite-syntax-s1">                {</span>
<span class="devsite-syntax-s1">                    "domain": "storage.googleapis.com",</span>
<span class="devsite-syntax-s1">                    "transform": {</span>
<span class="devsite-syntax-s1">                        "Authorization": "Bearer &lt;YOUR_GCLOUD_TOKEN&gt;"</span>
<span class="devsite-syntax-s1">                    }</span>
<span class="devsite-syntax-s1">                }</span>
<span class="devsite-syntax-s1">            ]</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="disable_network_access" data-text="Disable network access" tabindex="-1">Disable network access</h3>

<p>To block all outbound network access, set <code translate="no" dir="ltr">network</code> to <code translate="no" dir="ltr">disabled</code>:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_8" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Analyze the local files only."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"network"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"disabled"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_8" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Analyze the local files only."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">network</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"disabled"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_8" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_8" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": "Analyze the local files only.",</span>
<span class="devsite-syntax-s1">    "environment": {</span>
<span class="devsite-syntax-s1">        "type": "remote",</span>
<span class="devsite-syntax-s1">        "network": "disabled"</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="refresh-credentials" data-text="Refresh credentials" tabindex="-1">Refresh credentials</h3>

<p>Credentials such as access tokens and short-lived API keys expire.
You can refresh them by passing the existing <code translate="no" dir="ltr">environment_id</code> together with a
new <code translate="no" dir="ltr">network</code> configuration on the next interaction. The new network rules
fully replace the previous ones, while the environment&#39;s file system state
(installed packages, files, repositories) is preserved.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_9" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-c1"># First interaction: use an initial token</span>
<span class="devsite-syntax-n">first</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"List the files in gs://my-bucket/reports/ using the GCS JSON API."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"network"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"allowlist"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
                <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"storage.googleapis.com"</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"transform"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                        <span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Bearer INITIAL_TOKEN"</span>
                    <span class="devsite-syntax-p">},</span>
                <span class="devsite-syntax-p">}</span>
            <span class="devsite-syntax-p">]</span>
        <span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># Later: refresh the token on the same environment</span>
<span class="devsite-syntax-n">result</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Now download the file reports/q1.csv from the same bucket."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"environment_id"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">first</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environment_id</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"network"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"allowlist"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
                <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"domain"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"storage.googleapis.com"</span><span class="devsite-syntax-p">,</span>
                    <span class="devsite-syntax-s2">"transform"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                        <span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Bearer REFRESHED_TOKEN"</span>
                    <span class="devsite-syntax-p">},</span>
                <span class="devsite-syntax-p">}</span>
            <span class="devsite-syntax-p">]</span>
        <span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_9" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-c1">// First interaction: use an initial token</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">first</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"List the files in gs://my-bucket/reports/ using the GCS JSON API."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">network</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">allowlist</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"storage.googleapis.com"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">transform</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Bearer INITIAL_TOKEN"</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-c1">// Later: refresh the token on the same environment</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Now download the file reports/q1.csv from the same bucket."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">environment_id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">first</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environment_id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">network</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">allowlist</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">domain</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"storage.googleapis.com"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-nx">transform</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                        </span><span class="devsite-syntax-s2">"Authorization"</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Bearer REFRESHED_TOKEN"</span>
<span class="devsite-syntax-w">                    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_9" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_9" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Use the environment_id from a previous interaction</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": "Now download the file reports/q1.csv from the same bucket.",</span>
<span class="devsite-syntax-s1">    "environment": {</span>
<span class="devsite-syntax-s1">        "type": "remote",</span>
<span class="devsite-syntax-s1">        "environment_id": "&lt;ENVIRONMENT_ID_FROM_PREVIOUS_INTERACTION&gt;",</span>
<span class="devsite-syntax-s1">        "network": {</span>
<span class="devsite-syntax-s1">            "allowlist": [</span>
<span class="devsite-syntax-s1">                {</span>
<span class="devsite-syntax-s1">                    "domain": "storage.googleapis.com",</span>
<span class="devsite-syntax-s1">                    "transform": {</span>
<span class="devsite-syntax-s1">                        "Authorization": "Bearer REFRESHED_TOKEN"</span>
<span class="devsite-syntax-s1">                    }</span>
<span class="devsite-syntax-s1">                }</span>
<span class="devsite-syntax-s1">            ]</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="environment-lifecycle" data-text="Environment lifecycle" tabindex="-1">Environment lifecycle</h2>

<p>Environments follow this lifecycle:</p>

<table>
<thead>
<tr>
<th style="text-align: left">State</th>
<th style="text-align: left">Behavior</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left"><strong>Created</strong></td>
<td style="text-align: left">Provisioned when an interaction specifies <code translate="no" dir="ltr">environment: &quot;remote&quot;</code> or a config object.</td>
</tr>
<tr>
<td style="text-align: left"><strong>Active</strong></td>
<td style="text-align: left">Running while an interaction is in progress.</td>
</tr>
<tr>
<td style="text-align: left"><strong>Idle</strong></td>
<td style="text-align: left">Auto-snapshot and stopped after 15 minutes of inactivity.</td>
</tr>
<tr>
<td style="text-align: left"><strong>Offline</strong></td>
<td style="text-align: left">Retained for 7 days since last active. Can be resumed by passing its ID.</td>
</tr>
<tr>
<td style="text-align: left"><strong>Deleted</strong></td>
<td style="text-align: left">Removed from the system automatically after 7-day TTL retention expires or upon manual deletion.</td>
</tr>
</tbody>
</table>

<h2 id="environments-api" data-text="Environments API" tabindex="-1">Environments API</h2>

<p>You can use the Environments API to programmatically manage sandbox sessions.
Enumerating environments lets you discover active session IDs and recover state
if a client connection terminates during a long-running task. You can also
inspect session metadata and explicitly delete environments when workflows
conclude rather than waiting for automatic TTL expiration.</p>

<h3 id="list_environments" data-text="List environments" tabindex="-1">List environments</h3>

<p>List active environments belonging to your project. Use pagination parameters
to control the response batch size.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_10" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">env</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environments</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">list</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">page_size</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">10</span><span class="devsite-syntax-p">):</span>
    <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Environment ID: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">env</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environment_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">, Type: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">env</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_10" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environments</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">list</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">pageSize</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">10</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">env</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environments</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Environment ID: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">env</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environment_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">, Type: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">env</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_10" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_10" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>GET<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/environments?pageSize=10"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>The response looks similar to the following:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"environments"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"environment_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"140128b2a13c12c00a5a0d8cf7af9469"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"environment_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"362b738275a1d74af6f1c62bc050da73"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"next_page_token"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Cj...5aE="</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h3 id="get_an_environment" data-text="Get an environment" tabindex="-1">Get an environment</h3>

<p>Retrieve metadata and configuration details for a specific environment by its
resource name.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_11" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">env</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environments</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"environments/YOUR_ENVIRONMENT_ID"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Environment ID: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">env</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environment_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">, Type: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">env</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_11" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">env</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environments</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">get</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"environments/YOUR_ENVIRONMENT_ID"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Environment ID: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">env</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environment_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">, Type: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">env</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_11" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_11" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>GET<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>The response looks similar to the following:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"environment_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"140128b2a13c12c00a5a0d8cf7af9469"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"sources"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"repository"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"source"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://github.com/octocat/Spoon-Knife"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"target"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"/workspace/spoon-knife"</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"network"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"allowlist"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"domain"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"api.github.com"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"domain"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"github.com"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h3 id="delete_an_environment" data-text="Delete an environment" tabindex="-1">Delete an environment</h3>

<p>Explicitly terminate and delete an environment to clean up sandbox resources
when your tasks or pipelines finish.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_12" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environments</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delete</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"environments/YOUR_ENVIRONMENT_ID"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_12" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environments</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-ow">delete</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"environments/YOUR_ENVIRONMENT_ID"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="java_12" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_12" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>DELETE<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="download_files_from_the_environment" data-text="Download files from the environment" tabindex="-1">Download files from the environment</h2>

<p>The agent creates files inside the sandbox during execution. You can download the full environment snapshot as a tar file using the Files API:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_13" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">os</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">requests</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">tarfile</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">agent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Write a file environments_test.txt with content 'Environments' inside the sandbox."</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">environment</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">env_id</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environment_id</span>
<span class="devsite-syntax-n">api_key</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">os</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">environ</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"GEMINI_API_KEY"</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">requests</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/files/environment-</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">env_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">:download"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">params</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"alt"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"media"</span><span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-n">headers</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"x-goog-api-key"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">api_key</span><span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-n">allow_redirects</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">with</span> <span class="devsite-syntax-nb">open</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"snapshot_env.tar"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"wb"</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">f</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">f</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">write</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">os</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">makedirs</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"extracted_env_snapshot"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">exist_ok</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">tarfile</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">open</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"snapshot_env.tar"</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">tar</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">tar</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">extractall</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">path</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"extracted_env_snapshot"</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">os</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">listdir</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"extracted_env_snapshot"</span><span class="devsite-syntax-p">))</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_13" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">execSync</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"child_process"</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">as</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"fs"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">agent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Write a file environments_test.txt with content 'Environments' inside the sandbox."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">environment</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"remote"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">envId</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">environment_id</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">apiKey</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">env</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">GEMINI_API_KEY</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">||</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">url</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-sb">`https://generativelanguage.googleapis.com/v1beta/files/environment-</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">envId</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">:download?alt=media`</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fetch</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">url</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">headers</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-s2">"x-goog-api-key"</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">apiKey</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">ok</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">throw</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ne">Error</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Failed to download file: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">statusText</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arrayBuffer</span><span class="devsite-syntax-p">());</span>
<span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">writeFileSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"snapshot_env.tar"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">existsSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"extracted_env_snapshot"</span><span class="devsite-syntax-p">))</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mkdirSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"extracted_env_snapshot"</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-nx">execSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"tar -xf snapshot_env.tar -C extracted_env_snapshot"</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">readdirSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"extracted_env_snapshot"</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="java_13" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.AgentOption</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateAgentInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">agent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">AgentOption</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"antigravity-preview-05-2026"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Install pandas and matplotlib, verify the imports, and print the versions."</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">environment</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateAgentInteractionEnvironment</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"remote"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_13" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "agent": "antigravity-preview-05-2026",</span>
<span class="devsite-syntax-s1">    "input": "Write a file environments_test.txt with content '</span><span class="devsite-syntax-se">\'</span><span class="devsite-syntax-s1">'Environments'</span><span class="devsite-syntax-se">\'</span><span class="devsite-syntax-s1">' inside the sandbox.",</span>
<span class="devsite-syntax-s1">    "environment": "remote"</span>
<span class="devsite-syntax-s1">}'</span>
<span class="devsite-syntax-c1"># Step 2: Download snapshot (reusing environment ID from Step 1)</span>
<span class="devsite-syntax-c1"># curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \</span>
<span class="devsite-syntax-c1">#   -H "x-goog-api-key: $API_KEY" \</span>
<span class="devsite-syntax-c1">#   -o snapshot.tar</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="pricing-resources" data-text="Pricing &amp; resources" tabindex="-1">Pricing &amp; resources</h2>

<p>Each environment runs with fixed resource allocations:</p>

<table>
<thead>
<tr>
<th style="text-align: left">Resource</th>
<th style="text-align: left">Value</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left"><strong>CPU</strong></td>
<td style="text-align: left">4 cores</td>
</tr>
<tr>
<td style="text-align: left"><strong>Memory</strong></td>
<td style="text-align: left">16 GB</td>
</tr>
</tbody>
</table>

<p>Environment compute (CPU, memory, sandbox execution) is <strong>not billed</strong> during
the preview period. See
<a href="/gemini-api/docs/pricing#pricing-for-agents">Pricing</a> for
agent token costs.</p>

<h2 id="limitations" data-text="Limitations" tabindex="-1">Limitations</h2>

<ul>
<li><strong>Preview status:</strong> Environments and managed agents are in preview. Features and schemas may change.</li>
<li><strong>Inline source size:</strong> Inline sources are limited to 1 MB per file, and 2 MB total across all files.</li>
<li><strong>Source size</strong>: Git repositories are limited to 500 MB and Cloud Storage repositories to 2 GB.</li>
<li><strong>Environment startup:</strong> Provisioning a new environment takes up to ~5 seconds. Large source repositories may increase this time.</li>
<li><strong>Environment expiration:</strong> Inactive offline environments are retained for 7
days before expiring using automatic TTL cleanup. Passing an expired or
invalid environment ID returns a <code translate="no" dir="ltr">404 Not Found</code> error.</li>
<li><strong>File support:</strong> The agent is currently constrained to reading text and image files. Binary file support is not yet available.</li>
<li><strong>No mounting from root:</strong> You can&#39;t set root (<code translate="no" dir="ltr">/</code>) as target when adding a custom source, you must always specify a sub-directory.</li>
</ul>

<h2 id="whats-next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li><a href="/gemini-api/docs/agents">Agents Overview</a>: Learn about the core concepts of managed agents.</li>
<li><a href="/gemini-api/docs/managed-agents-quickstart">Quickstart</a>: Start building with multi-turn conversations and streaming.</li>
<li><a href="/gemini-api/docs/antigravity-agent">Antigravity Agent</a>: Explore capabilities, tools, model selection, and pricing for the default agent.</li>
<li><a href="/gemini-api/docs/custom-agents">Building Custom Agents</a>: Define your own agents using <code translate="no" dir="ltr">AGENTS.md</code> and <code translate="no" dir="ltr">SKILL.md</code>.</li>
<li><a href="/gemini-api/docs/agent-hooks">Hooks</a>: Enforce security guardrails and run side-effect validations inside the sandbox.</li>
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