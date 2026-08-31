








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/live-api/tools"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/live-api/tools" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/live-api/tools?hl=sq" /><title>Tool use with Live API &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Tool use with Live API &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/live-api/tools"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
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
      Tool use with Live API<devsite-actions hidden data-nosnippet>
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

<p>
</p>
































<p>Tool use allows Live API to go beyond just conversation by enabling it to
perform actions in the real-world and pull in external context while maintaining
a real time connection.
You can define tools such as <a href="/gemini-api/docs/function-calling">Function calling</a>
 and <a href="/gemini-api/docs/grounding">Google Search</a> with the Live API.</p>

<h2 id="tools-overview" data-text="Overview of supported tools" tabindex="-1">Overview of supported tools</h2>

<p>Here&#39;s a brief overview of the available tools for Live API models:</p>

<table class="pricing-table" style="width: 100%; table-layout: fixed;">
  <colgroup>
    <col class="paid-tier" width="20%">
    <col width="40%">
    <col class="paid-tier" width="40%">
  </colgroup>
  <thead>
    <tr>
      <th scope="col">Tool</th>
      <th scope="col">Gemini 3.1 Flash Live Preview</th>
      <th scope="col">Gemini 2.5 Flash Live Preview</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Search</b></td>
      <td><span class="gemini-api-supported">Supported</span></td>
      <td><span class="gemini-api-supported">Supported</span></td>
    </tr>
    <tr>
      <td><b>Function calling</b></td>
      <td><span class="gemini-api-supported">Supported</span> (synchronous only)</td>
      <td><span class="gemini-api-supported">Supported</span> (synchronous and <a href="#async-function-calling">asynchronous</a>)</td>
    </tr>
    <tr>
      <td><b>Google Maps</b></td>
      <td><span class="gemini-api-not-supported">Not supported</span></td>
      <td><span class="gemini-api-not-supported">Not supported</span></td>
    </tr>
    <tr>
      <td><b>Code execution</b></td>
      <td><span class="gemini-api-not-supported">Not supported</span></td>
      <td><span class="gemini-api-not-supported">Not supported</span></td>
    </tr>
    <tr>
      <td><b>URL context</b></td>
      <td><span class="gemini-api-not-supported">Not supported</span></td>
      <td><span class="gemini-api-not-supported">Not supported</span></td>
    </tr>
  </tbody>
</table>

<h2 id="function-calling" data-text="Function calling" tabindex="-1">Function calling</h2>

<p>Live API supports function calling, just like regular content generation
requests. Function calling lets the Live API interact with external data and
programs, greatly increasing what your applications can accomplish.</p>

<p>You can define function declarations as part of the session configuration.
After receiving tool calls, the client should respond with a list of
<code translate="no" dir="ltr">FunctionResponse</code> objects using the <code translate="no" dir="ltr">session.send_tool_response</code> method.</p>

<p>See the <a href="/gemini-api/docs/function-calling">Function calling tutorial</a> to learn
more.</p>
<aside class="note"><strong>Note:</strong><span> Unlike the <code translate="no" dir="ltr">generateContent</code> API, the Live API
doesn&#39;t support automatic tool response handling. You must handle tool responses
manually in your client code.</span></aside><div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text=" Python " tabindex="-1"> Python </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">asyncio</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">wave</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">model</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"gemini-3.1-flash-live-preview"</span>

<span class="devsite-syntax-c1"># Simple function definitions</span>
<span class="devsite-syntax-n">turn_on_the_lights</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"turn_on_the_lights"</span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-n">turn_off_the_lights</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"turn_off_the_lights"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-n">tools</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[{</span><span class="devsite-syntax-s2">"function_declarations"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">turn_on_the_lights</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">turn_off_the_lights</span><span class="devsite-syntax-p">]}]</span>
<span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"response_modalities"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"AUDIO"</span><span class="devsite-syntax-p">],</span> <span class="devsite-syntax-s2">"tools"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">main</span><span class="devsite-syntax-p">():</span>
    <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">aio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">live</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">connect</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">config</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">prompt</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"Turn on the lights please"</span>
        <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_client_content</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">turns</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"parts"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[{</span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">}]})</span>

        <span class="devsite-syntax-n">wf</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">wave</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">open</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"audio.wav"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"wb"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setnchannels</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setsampwidth</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setframerate</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">24000</span><span class="devsite-syntax-p">)</span>  <span class="devsite-syntax-c1"># Output is 24kHz</span>

        <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">response</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">receive</span><span class="devsite-syntax-p">():</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">data</span> <span class="devsite-syntax-ow">is</span> <span class="devsite-syntax-ow">not</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">writeframes</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">)</span>
            <span class="devsite-syntax-k">elif</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">tool_call</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"The tool was called"</span><span class="devsite-syntax-p">)</span>
                <span class="devsite-syntax-n">function_responses</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[]</span>
                <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">fc</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">tool_call</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">function_calls</span><span class="devsite-syntax-p">:</span>
                    <span class="devsite-syntax-n">function_response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">FunctionResponse</span><span class="devsite-syntax-p">(</span>
                        <span class="devsite-syntax-nb">id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">fc</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span><span class="devsite-syntax-p">,</span>
                        <span class="devsite-syntax-n">name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">fc</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span>
                        <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span> <span class="devsite-syntax-s2">"result"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"ok"</span> <span class="devsite-syntax-p">}</span> <span class="devsite-syntax-c1"># simple, hard-coded function response</span>
                    <span class="devsite-syntax-p">)</span>
                    <span class="devsite-syntax-n">function_responses</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">append</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">function_response</span><span class="devsite-syntax-p">)</span>

                <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_tool_response</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">function_responses</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">function_responses</span><span class="devsite-syntax-p">)</span>

        <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">close</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-k">if</span> <span class="devsite-syntax-vm">__name__</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"__main__"</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">asyncio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">run</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">main</span><span class="devsite-syntax-p">())</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript" data-text=" JavaScript " tabindex="-1"> JavaScript </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">as</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"node:fs"</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">pkg</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'wavefile'</span><span class="devsite-syntax-p">;</span><span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// npm install wavefile</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">WaveFile</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">pkg</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.1-flash-live-preview'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-c1">// Simple function definitions</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn_on_the_lights</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"turn_on_the_lights"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-c1">// , description: '...', parameters: { ... }</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn_off_the_lights</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"turn_off_the_lights"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">functionDeclarations</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">turn_on_the_lights</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn_off_the_lights</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">AUDIO</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">live</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">responseQueue</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[];</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">waitMessage</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">false</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">undefined</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">while</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">responseQueue</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">shift</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Promise</span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setTimeout</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">100</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">handleTurn</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[];</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">false</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">while</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">waitMessage</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">push</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">turnComplete</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">toolCall</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">session</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">live</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">connect</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">callbacks</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onopen</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Opened'</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onmessage</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">responseQueue</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">push</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onerror</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Error:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onclose</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Close:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">reason</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">inputTurns</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Turn on the lights please'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendClientContent</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">inputTurns</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">handleTurn</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">toolCall</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'A tool was called'</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">functionResponses</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[];</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fc</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">toolCall</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">functionCalls</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">functionResponses</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">push</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fc</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fc</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"ok"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-c1">// simple, hard-coded function response</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Sending tool response...\n'</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendToolResponse</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">functionResponses</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">functionResponses</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// Check again for new messages</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">handleTurn</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// Combine audio data strings and save as wave file</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">combinedAudio</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">reduce</span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-nx">acc</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'base64'</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">intArray</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Int16Array</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">byteOffset</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">byteLength</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">/</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Int16Array</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">BYTES_PER_ELEMENT</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">acc</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">concat</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">Array</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">intArray</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">acc</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[]);</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioBuffer</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Int16Array</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">combinedAudio</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">wf</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">WaveFile</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">wf</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fromScratch</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mf">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">24000</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'16'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioBuffer</span><span class="devsite-syntax-p">);</span><span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// output is 24kHz</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">writeFileSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'audio.wav'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">wf</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">toBuffer</span><span class="devsite-syntax-p">());</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">close</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">live</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-k">catch</span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">error</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'got error'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>From a single prompt, the model can generate multiple function calls and the
code necessary to chain their outputs. This code executes in a sandbox
environment, generating subsequent <a href="/api/live#bidigeneratecontenttoolcall">BidiGenerateContentToolCall</a> messages.</p>

<h2 id="async-function-calling" data-text="Asynchronous function calling" tabindex="-1">Asynchronous function calling</h2>

<p>Function calling executes sequentially by default, meaning execution pauses
until the results of each function call are available. This ensures sequential
processing, which means you won&#39;t be able to continue interacting with the model
while the functions are being run.</p>
<aside class="note"><strong>Note:</strong><span> Asynchronous function calling is not yet supported in Gemini 3.1 Flash Live. The model will not start responding until you&#39;ve sent the tool response.</span></aside>
<p>If you don&#39;t want to block the conversation, you can tell the model to run the
functions asynchronously. To do so, you first need to add a <code translate="no" dir="ltr">behavior</code> to the
function definitions:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text=" Python " tabindex="-1"> Python </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Non-blocking function definitions</span>
<span class="devsite-syntax-n">turn_on_the_lights</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"turn_on_the_lights"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"behavior"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"NON_BLOCKING"</span><span class="devsite-syntax-p">}</span> <span class="devsite-syntax-c1"># turn_on_the_lights will run asynchronously</span>
<span class="devsite-syntax-n">turn_off_the_lights</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"turn_off_the_lights"</span><span class="devsite-syntax-p">}</span> <span class="devsite-syntax-c1"># turn_off_the_lights will still pause all interactions with the model</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text=" JavaScript " tabindex="-1"> JavaScript </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Behavior</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-c1">// Non-blocking function definitions</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn_on_the_lights</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"turn_on_the_lights"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">behavior</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Behavior</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">NON_BLOCKING</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1">// Blocking function definitions</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn_off_the_lights</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"turn_off_the_lights"</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">functionDeclarations</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">turn_on_the_lights</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn_off_the_lights</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p><code translate="no" dir="ltr">NON-BLOCKING</code> ensures the function runs asynchronously while you can
continue interacting with the model.</p>

<p>Then you need to tell the model how to behave when it receives the
<code translate="no" dir="ltr">FunctionResponse</code> using the <code translate="no" dir="ltr">scheduling</code> parameter. It can either:</p>
<ul>
<li>Interrupt what it&#39;s doing and tell you about the response it got right away
(<code translate="no" dir="ltr">scheduling=&quot;INTERRUPT&quot;</code>),</li>
<li>Wait until it&#39;s finished with what it&#39;s currently doing
(<code translate="no" dir="ltr">scheduling=&quot;WHEN_IDLE&quot;</code>),</li>
<li><p>Or do nothing and use that knowledge later on in the discussion
(<code translate="no" dir="ltr">scheduling=&quot;SILENT&quot;</code>)</p></li>
</ul>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text=" Python " tabindex="-1"> Python </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># for a non-blocking function definition, apply scheduling in the function response:</span>
  <span class="devsite-syntax-n">function_response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">FunctionResponse</span><span class="devsite-syntax-p">(</span>
      <span class="devsite-syntax-nb">id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">fc</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">id</span><span class="devsite-syntax-p">,</span>
      <span class="devsite-syntax-n">name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">fc</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span>
      <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
          <span class="devsite-syntax-s2">"result"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"ok"</span><span class="devsite-syntax-p">,</span>
          <span class="devsite-syntax-s2">"scheduling"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"INTERRUPT"</span> <span class="devsite-syntax-c1"># Can also be WHEN_IDLE or SILENT</span>
      <span class="devsite-syntax-p">}</span>
  <span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text=" JavaScript " tabindex="-1"> JavaScript </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Behavior</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">FunctionResponseScheduling</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-c1">// for a non-blocking function definition, apply scheduling in the function response:</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">functionResponse</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fc</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">id</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fc</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"ok"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">scheduling</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">FunctionResponseScheduling</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">INTERRUPT</span><span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// Can also be WHEN_IDLE or SILENT</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="google-search" data-text="Grounding with Google Search" tabindex="-1">Grounding with Google Search</h2>

<p>You can enable Grounding with Google Search as part of the session
configuration. This increases the Live API&#39;s accuracy and prevents
hallucinations. See the <a href="/gemini-api/docs/grounding">Grounding tutorial</a> to
learn more.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_3" data-text="Python " tabindex="-1">Python </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">asyncio</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">wave</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">model</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"gemini-3.1-flash-live-preview"</span>

<span class="devsite-syntax-n">tools</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[{</span><span class="devsite-syntax-s1">'google_search'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{}}]</span>
<span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"response_modalities"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"AUDIO"</span><span class="devsite-syntax-p">],</span> <span class="devsite-syntax-s2">"tools"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">main</span><span class="devsite-syntax-p">():</span>
    <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">aio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">live</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">connect</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">config</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-n">prompt</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"When did the last Brazil vs. Argentina soccer match happen?"</span>
        <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_client_content</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">turns</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"parts"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[{</span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">}]})</span>

        <span class="devsite-syntax-n">wf</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">wave</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">open</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"audio.wav"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"wb"</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setnchannels</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setsampwidth</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">2</span><span class="devsite-syntax-p">)</span>
        <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">setframerate</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">24000</span><span class="devsite-syntax-p">)</span>  <span class="devsite-syntax-c1"># Output is 24kHz</span>

        <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">chunk</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">receive</span><span class="devsite-syntax-p">():</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">server_content</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">data</span> <span class="devsite-syntax-ow">is</span> <span class="devsite-syntax-ow">not</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">:</span>
                    <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">writeframes</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-p">)</span>

                <span class="devsite-syntax-c1"># The model might generate and execute Python code to use Search</span>
                <span class="devsite-syntax-n">model_turn</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">server_content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">model_turn</span>
                <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">model_turn</span><span class="devsite-syntax-p">:</span>
                    <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">part</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">model_turn</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">parts</span><span class="devsite-syntax-p">:</span>
                        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">executable_code</span> <span class="devsite-syntax-ow">is</span> <span class="devsite-syntax-ow">not</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">:</span>
                            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">executable_code</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">code</span><span class="devsite-syntax-p">)</span>

                        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">code_execution_result</span> <span class="devsite-syntax-ow">is</span> <span class="devsite-syntax-ow">not</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">:</span>
                            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">part</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">code_execution_result</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output</span><span class="devsite-syntax-p">)</span>

        <span class="devsite-syntax-n">wf</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">close</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-k">if</span> <span class="devsite-syntax-vm">__name__</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"__main__"</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">asyncio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">run</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">main</span><span class="devsite-syntax-p">())</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_3" data-text=" JavaScript " tabindex="-1"> JavaScript </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">as</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"node:fs"</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">pkg</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'wavefile'</span><span class="devsite-syntax-p">;</span><span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// npm install wavefile</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">WaveFile</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">pkg</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.1-flash-live-preview'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">googleSearch</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">AUDIO</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">live</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">responseQueue</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[];</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">waitMessage</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">false</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">undefined</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">while</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">responseQueue</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">shift</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Promise</span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setTimeout</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">100</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">handleTurn</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[];</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">false</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">while</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">waitMessage</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">push</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">turnComplete</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">toolCall</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">session</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">live</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">connect</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">callbacks</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onopen</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Opened'</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onmessage</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">responseQueue</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">push</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onerror</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Error:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onclose</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Close:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">reason</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">inputTurns</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'When did the last Brazil vs. Argentina soccer match happen?'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendClientContent</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">inputTurns</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">handleTurn</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">combinedData</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">''</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turns</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">modelTurn</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">modelTurn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">modelTurn</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parts</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">executableCode</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'executableCode: %s\n'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">executableCode</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">code</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">codeExecutionResult</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">debug</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'codeExecutionResult: %s\n'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">codeExecutionResult</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">else</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inlineData</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-ow">typeof</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inlineData</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'string'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">combinedData</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">+=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">atob</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">part</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inlineData</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// Convert the base64-encoded string of bytes into a Buffer.</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">combinedData</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'binary'</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// The buffer contains raw bytes. For 16-bit audio, we need to interpret every 2 bytes as a single sample.</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">intArray</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Int16Array</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">byteOffset</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">byteLength</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">/</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Int16Array</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">BYTES_PER_ELEMENT</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">wf</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">WaveFile</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-c1">// The API returns 16-bit PCM audio at a 24kHz sample rate.</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">wf</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fromScratch</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mf">1</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">24000</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'16'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">intArray</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">writeFileSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'audio.wav'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">wf</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">toBuffer</span><span class="devsite-syntax-p">());</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">close</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">live</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-k">catch</span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">error</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'got error'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="combine-tools" data-text="Combining multiple tools" tabindex="-1">Combining multiple tools</h2>

<p>You can combine multiple tools within the Live API,
increasing your application&#39;s capabilities even more:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_4" data-text=" Python " tabindex="-1"> Python </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">prompt</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"""</span>
<span class="devsite-syntax-s2">Hey, I need you to do two things for me.</span>

<span class="devsite-syntax-s2">1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?</span>
<span class="devsite-syntax-s2">2. Then turn on the lights</span>

<span class="devsite-syntax-s2">Thanks!</span>
<span class="devsite-syntax-s2">"""</span>

<span class="devsite-syntax-n">tools</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[</span>
    <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"google_search"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{}},</span>
    <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"function_declarations"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">turn_on_the_lights</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">turn_off_the_lights</span><span class="devsite-syntax-p">]},</span>
<span class="devsite-syntax-p">]</span>

<span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"response_modalities"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"AUDIO"</span><span class="devsite-syntax-p">],</span> <span class="devsite-syntax-s2">"tools"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1"># ... remaining model call</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_4" data-text=" JavaScript " tabindex="-1"> JavaScript </h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-sb">`Hey, I need you to do two things for me.</span>

<span class="devsite-syntax-sb">1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?</span>
<span class="devsite-syntax-sb">2. Then turn on the lights</span>

<span class="devsite-syntax-sb">Thanks!</span>
<span class="devsite-syntax-sb">`</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">googleSearch</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">functionDeclarations</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">turn_on_the_lights</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">turn_off_the_lights</span><span class="devsite-syntax-p">]</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">]</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">AUDIO</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">tools</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-c1">// ... remaining model call</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="whats-next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li>Check out more examples of using tools with the Live API in the
<a href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb">Tool use cookbook</a>.</li>
<li>Get the full story on features and configurations from the
<a href="/gemini-api/docs/live-guide">Live API Capabilities guide</a>.</li>
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
  <p>Last updated 2026-06-01 UTC.</p>
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