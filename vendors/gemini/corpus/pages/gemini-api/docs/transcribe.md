








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/transcribe"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/transcribe" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/transcribe" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/transcribe?hl=sq" /><title>Audio transcription &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Audio transcription &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta name="description" content="Get started transcribing audio with the Gemini 3.5 Transcribe model in the Gemini API">
  <meta property="og:description" content="Get started transcribing audio with the Gemini 3.5 Transcribe model in the Gemini API"><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/transcribe"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
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
      Audio transcription<devsite-actions hidden data-nosnippet>
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

  
    
    
<div id="gemini-api-switcher-trigger" style="display:none;"></div>

<p>
</p>



<p>The Gemini API converts speech in audio files into text using the Gemini 3.5 Transcribe model (<code translate="no" dir="ltr">gemini-3.5-transcribe</code>). Based on Gemini&#39;s audio understanding capabilities, it delivers accurate transcription with automatic language identification, speaker diarization, word-level timestamps, and custom vocabulary hints. It also provides a <a href="#transcription-modes">smart transcription</a> mode featuring disfluency removal and smart formatting.</p>

<p>To transcribe an audio file, upload the audio and pass it to <code translate="no" dir="ltr">gemini-3.5-transcribe</code>:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">audio_file</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">files</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">upload</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">file</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"path/to/sample.mp3"</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"uri"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">uri</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">files</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">upload</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">file</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"path/to/sample.mp3"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"audio/mp3"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="rest" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># First upload the file via the Files API, then pass its URI:</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.5-transcribe",</span>
<span class="devsite-syntax-s1">    "input": [</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "audio",</span>
<span class="devsite-syntax-s1">        "uri": "YOUR_FILE_URI",</span>
<span class="devsite-syntax-s1">        "mime_type": "audio/mp3"</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ]</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div><aside class="note"><strong>Note:</strong><span> For real-time, low-latency streaming speech recognition from a microphone or live audio stream, see <a href="/gemini-api/docs/live-api/live-transcribe">Live transcription</a> using the Live API and <code translate="no" dir="ltr">gemini-3.5-transcribe-live</code>.</span></aside>
<h2 id="overview" data-text="Overview" tabindex="-1">Overview</h2>

<p>Gemini 3.5 Transcribe is optimized for speech-to-text tasks. It handles diverse accents, background noise, and multi-language conversations.</p>

<p>Key capabilities include:</p>

<ul>
<li><strong>Automatic speech recognition (ASR):</strong> Automatically detects languages across <a href="#supported-languages">85+ locales</a>. Handles intra-sentence and inter-sentential code-switching without manual configuration.</li>
<li><strong>Custom vocabulary:</strong> Biases recognition toward domain-specific terms, acronyms, and proper names by passing up to 1,000 phrases.</li>
<li><strong>Speaker diarization:</strong> Distinguishes between multiple speakers and attributes spoken segments to distinct labels.</li>
<li><strong>Word-level timestamps:</strong> Generates precise start and end time offsets for each recognized word.</li>
<li><strong>Smart transcription:</strong> Cleans up disfluencies, filler words, repetitions, and applies structured formatting.</li>
<li><strong>Formatting and normalization:</strong> Applies capitalization, punctuation, and inverse text normalization, such as converting &quot;twenty six million dollars&quot; to &quot;$26M&quot;.</li>
</ul>

<p>For general audio reasoning or question answering over audio content, use <a href="/gemini-api/docs/audio">Audio understanding</a>. For text-to-speech audio synthesis, use <a href="/gemini-api/docs/speech-generation">Text-to-speech</a>.</p>

<h2 id="language-detection" data-text="Language detection and hints" tabindex="-1">Language detection and hints</h2>

<p>By default, the model detects the spoken language automatically. It switches between languages dynamically when speakers code-switch.</p>

<p>To use automatic detection, omit <code translate="no" dir="ltr">language_codes</code> or provide an empty list:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"uri"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">uri</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">generation_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"transcription_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"language_codes"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[],</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">generation_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">transcription_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">language_codes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_1" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.5-transcribe",</span>
<span class="devsite-syntax-s1">    "input": [</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "audio",</span>
<span class="devsite-syntax-s1">        "uri": "YOUR_FILE_URI",</span>
<span class="devsite-syntax-s1">        "mime_type": "audio/mp3"</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ],</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "transcription_config": {</span>
<span class="devsite-syntax-s1">        "language_codes": []</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>If you know the language in advance, specify BCP-47 language codes in <code translate="no" dir="ltr">language_codes</code> to improve transcription accuracy (see <a href="#supported-languages">Supported languages</a>):</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">generation_config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span>
    <span class="devsite-syntax-s2">"transcription_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"language_codes"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"es-ES"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">generationConfig</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">transcription_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">language_codes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"es-ES"</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_2" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"generation_config"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"transcription_config"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"language_codes"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"es-ES"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="custom-vocabulary" data-text="Custom vocabulary" tabindex="-1">Custom vocabulary</h2>

<p>You can steer the speech model toward uncommon words, technical jargon, brand names, or proper nouns. Supply up to 1,000 terms in the <code translate="no" dir="ltr">custom_vocabulary</code> array (best results are typically achieved with up to 100 terms):</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_3" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"uri"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">uri</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">generation_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"transcription_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"custom_vocabulary"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"Gemini"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"Kubernetes"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"BigQuery"</span><span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_3" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">generation_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">transcription_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">custom_vocabulary</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"Gemini"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Kubernetes"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"BigQuery"</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_3" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.5-transcribe",</span>
<span class="devsite-syntax-s1">    "input": [</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "audio",</span>
<span class="devsite-syntax-s1">        "uri": "YOUR_FILE_URI",</span>
<span class="devsite-syntax-s1">        "mime_type": "audio/mp3"</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ],</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "transcription_config": {</span>
<span class="devsite-syntax-s1">        "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"]</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="speaker-diarization" data-text="Speaker diarization" tabindex="-1">Speaker diarization</h2>

<p>Speaker diarization identifies different voices in the recording and tags each segment with a speaker identifier like <code translate="no" dir="ltr">spk_1</code> or <code translate="no" dir="ltr">spk_2</code>. Up to 8 speakers are supported (attribution for 3 or more speakers is experimental).</p>

<p>Enable diarization by configuring <code translate="no" dir="ltr">diarization_mode</code> within <code translate="no" dir="ltr">mode</code>:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_4" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"uri"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">uri</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">generation_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"transcription_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"mode"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"verbatim"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"diarization_mode"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"speaker"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_4" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">generation_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">transcription_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mode</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"verbatim"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">diarization_mode</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"speaker"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_4" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.5-transcribe",</span>
<span class="devsite-syntax-s1">    "input": [</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "audio",</span>
<span class="devsite-syntax-s1">        "uri": "YOUR_FILE_URI",</span>
<span class="devsite-syntax-s1">        "mime_type": "audio/mp3"</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ],</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "transcription_config": {</span>
<span class="devsite-syntax-s1">        "mode": {</span>
<span class="devsite-syntax-s1">          "type": "verbatim",</span>
<span class="devsite-syntax-s1">          "diarization_mode": "speaker"</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="word-timestamps" data-text="Word-level timestamps" tabindex="-1">Word-level timestamps</h2>

<p>Word-level timestamps provide exact start and end offsets for every recognized word in the audio stream.</p>
<aside class="note"><strong>Note:</strong><span> Enabling word-level timestamps may degrade overall transcription accuracy.</span></aside>
<p>Enable timestamps by configuring <code translate="no" dir="ltr">timestamp_granularities</code> within <code translate="no" dir="ltr">mode</code>:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_5" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"uri"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">uri</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">generation_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"transcription_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"mode"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"verbatim"</span><span class="devsite-syntax-p">,</span>
                <span class="devsite-syntax-s2">"timestamp_granularities"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"word"</span><span class="devsite-syntax-p">],</span>
            <span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_5" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">generation_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">transcription_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mode</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"verbatim"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">timestamp_granularities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"word"</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_5" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.5-transcribe",</span>
<span class="devsite-syntax-s1">    "input": [</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "audio",</span>
<span class="devsite-syntax-s1">        "uri": "YOUR_FILE_URI",</span>
<span class="devsite-syntax-s1">        "mime_type": "audio/mp3"</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ],</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "transcription_config": {</span>
<span class="devsite-syntax-s1">        "mode": {</span>
<span class="devsite-syntax-s1">          "type": "verbatim",</span>
<span class="devsite-syntax-s1">          "timestamp_granularities": ["word"]</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>You can combine <code translate="no" dir="ltr">diarization_mode</code> and <code translate="no" dir="ltr">timestamp_granularities</code> in <code translate="no" dir="ltr">mode</code> to receive both speaker labels and word timestamps:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_6" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">generation_config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span>
    <span class="devsite-syntax-s2">"transcription_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"custom_vocabulary"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"Gemini"</span><span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-s2">"mode"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"verbatim"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"diarization_mode"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"speaker"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"timestamp_granularities"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"word"</span><span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_6" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">generationConfig</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">transcription_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">custom_vocabulary</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"Gemini"</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">mode</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"verbatim"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">diarization_mode</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"speaker"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">timestamp_granularities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"word"</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_6" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"generation_config"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"transcription_config"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"custom_vocabulary"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"Gemini"</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"mode"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"verbatim"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"diarization_mode"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"speaker"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"timestamp_granularities"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"word"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="transcription-modes" data-text="Transcription modes" tabindex="-1">Transcription modes</h2>

<p>Gemini 3.5 Transcribe supports two transcription modes via the <code translate="no" dir="ltr">mode</code> parameter:</p>

<ul>
<li><strong><code translate="no" dir="ltr">verbatim</code> (default)</strong>: Returns an exact word-for-word transcript of everything spoken, preserving raw filler words (&quot;um&quot;, &quot;uh&quot;, &quot;like&quot;, &quot;you know&quot;), repetitions, pauses, and false starts. Timestamps and speaker diarization are configured within this mode (<code translate="no" dir="ltr">{&quot;type&quot;: &quot;verbatim&quot;, ...}</code>).</li>
<li><strong><code translate="no" dir="ltr">smart</code> (Smart transcription)</strong>: Optimizes the transcript for reading by applying intelligent post-processing:
<ul>
<li><strong>Disfluency removal</strong>: Strips conversational filler words, stuttering, and false starts.</li>
<li><strong>Inline self-corrections</strong>: Resolves spoken corrections directly (for example, <em>&quot;Let&#39;s meet on Tuesday, actually no, Wednesday at two&quot;</em> becomes <em>&quot;Let&#39;s meet on Wednesday at 2:00 PM&quot;</em>).</li>
<li><strong>Automatic structured formatting</strong>: Automatically structures spoken thoughts into paragraphs, numbered lists, bullet points, formatted dates, currencies, and numbers.</li>
<li><strong>Grammatical cleanup</strong>: Applies natural punctuation, sentence casing, and flow.</li>
</ul></li>
</ul>

<table>
<thead>
<tr>
<th style="text-align: left">Spoken audio</th>
<th style="text-align: left"><code translate="no" dir="ltr">verbatim</code> output</th>
<th style="text-align: left"><code translate="no" dir="ltr">smart</code> (Smart transcription) output</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left">&quot;Um, so for the meeting, I think we should, uh, invite Alice and, wait no, Bob and Carol.&quot;</td>
<td style="text-align: left">&quot;Um so for the meeting I think we should uh invite Alice and wait no Bob and Carol.&quot;</td>
<td style="text-align: left">&quot;For the meeting, I think we should invite Bob and Carol.&quot;</td>
</tr>
<tr>
<td style="text-align: left">&quot;First item review budget second item finalize timeline third item send recap&quot;</td>
<td style="text-align: left">&quot;first item review budget second item finalize timeline third item send recap&quot;</td>
<td style="text-align: left">&quot;1. Review budget<br>2. Finalize timeline<br>3. Send recap&quot;</td>
</tr>
</tbody>
</table>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_7" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"uri"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">uri</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">audio_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">generation_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"transcription_config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"mode"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"smart"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_7" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.5-transcribe"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"audio"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">generation_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">transcription_config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mode</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"smart"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_7" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.5-transcribe",</span>
<span class="devsite-syntax-s1">    "input": [</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "audio",</span>
<span class="devsite-syntax-s1">        "uri": "YOUR_FILE_URI",</span>
<span class="devsite-syntax-s1">        "mime_type": "audio/mp3"</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ],</span>
<span class="devsite-syntax-s1">    "generation_config": {</span>
<span class="devsite-syntax-s1">      "transcription_config": {</span>
<span class="devsite-syntax-s1">        "mode": "smart"</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div><aside class="note"><strong>Note:</strong><span> Smart transcription (<code translate="no" dir="ltr">&quot;smart&quot;</code>) is incompatible with
<code translate="no" dir="ltr">timestamp_granularities</code> and <code translate="no" dir="ltr">diarization_mode</code>. If you need word timestamps
or speaker diarization, configure <code translate="no" dir="ltr">mode</code> with <code translate="no" dir="ltr">{&quot;type&quot;: &quot;verbatim&quot;, ...}</code>.</span></aside>
<h2 id="parsing-output" data-text="Parsing transcription output" tabindex="-1">Parsing transcription output</h2>

<p>The complete transcript text is returned in <code translate="no" dir="ltr">interaction.output_text</code>.</p>

<p>When <code translate="no" dir="ltr">timestamp_granularities</code> or <code translate="no" dir="ltr">diarization_mode</code> is enabled, the API also returns detailed word-level annotations attached to the interaction content.</p>

<p>Here is how to extract and iterate over word timestamps and speaker turns:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_8" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">extract_word_annotations</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">):</span>
    <span class="devsite-syntax-n">words</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[]</span>
    <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"steps"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-p">[])</span> <span class="devsite-syntax-ow">or</span> <span class="devsite-syntax-p">[]:</span>
        <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">content</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">step</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"content"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-p">[])</span> <span class="devsite-syntax-ow">or</span> <span class="devsite-syntax-p">[]:</span>
            <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">annotation</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"annotations"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-p">[])</span> <span class="devsite-syntax-ow">or</span> <span class="devsite-syntax-p">[]:</span>
                <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"word_info"</span><span class="devsite-syntax-p">:</span>
                    <span class="devsite-syntax-n">words</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">append</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-k">return</span> <span class="devsite-syntax-n">words</span>

<span class="devsite-syntax-n">words</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">extract_word_annotations</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">w</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">words</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">speaker</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"[</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">w</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">speaker</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">] "</span> <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">w</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"speaker"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-kc">None</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">else</span> <span class="devsite-syntax-s2">""</span>
    <span class="devsite-syntax-n">start</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">w</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"start_offset"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-n">end</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-nb">getattr</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">w</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"end_offset"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-n">timing</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"(</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">start</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2"> -&gt; </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">end</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">) "</span> <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">start</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">end</span> <span class="devsite-syntax-k">else</span> <span class="devsite-syntax-s2">""</span>
    <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">speaker</span><span class="devsite-syntax-si">}{</span><span class="devsite-syntax-n">timing</span><span class="devsite-syntax-si">}{</span><span class="devsite-syntax-n">w</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_8" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">extractWordAnnotations</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">words</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[];</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">??</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[])</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">??</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[])</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">??</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[])</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"word_info"</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">words</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">push</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">words</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">words</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">extractWordAnnotations</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">w</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">words</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">speaker</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">w</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">speaker</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-sb">`[</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">w</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">speaker</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">] `</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">timing</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">w</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">start_offset</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">w</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">end_offset</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-sb">`(</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">w</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">start_offset</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb"> -&gt; </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">w</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">end_offset</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">) `</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">speaker</span><span class="devsite-syntax-si">}${</span><span class="devsite-syntax-nx">timing</span><span class="devsite-syntax-si">}${</span><span class="devsite-syntax-nx">w</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_8" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"interactions/abc123xyz"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"completed"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"step_001"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hello world"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"annotations"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"word_info"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hello"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"speaker"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"spk_1"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"start_offset"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"0.100s"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"end_offset"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"0.450s"</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"word_info"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"world"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"speaker"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"spk_1"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"start_offset"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"0.500s"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"end_offset"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"0.850s"</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="supported-languages" data-text="Supported languages" tabindex="-1">Supported languages</h2>

<p>The following languages and BCP-47 language codes are supported for Gemini 3.5 Transcribe:</p>

<table>
<thead>
<tr>
<th style="text-align: left">Language</th>
<th style="text-align: left">BCP-47 Code</th>
<th style="text-align: left">Language</th>
<th style="text-align: left">BCP-47 Code</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left">Afrikaans</td>
<td style="text-align: left"><code translate="no" dir="ltr">af-ZA</code></td>
<td style="text-align: left">Japanese</td>
<td style="text-align: left"><code translate="no" dir="ltr">ja-JP</code></td>
</tr>
<tr>
<td style="text-align: left">Amharic</td>
<td style="text-align: left"><code translate="no" dir="ltr">am-ET</code></td>
<td style="text-align: left">Javanese</td>
<td style="text-align: left"><code translate="no" dir="ltr">jv-ID</code></td>
</tr>
<tr>
<td style="text-align: left">Arabic (Egypt)</td>
<td style="text-align: left"><code translate="no" dir="ltr">ar-EG</code></td>
<td style="text-align: left">Kabuverdianu</td>
<td style="text-align: left"><code translate="no" dir="ltr">kea-CV</code></td>
</tr>
<tr>
<td style="text-align: left">Armenian</td>
<td style="text-align: left"><code translate="no" dir="ltr">hy-AM</code></td>
<td style="text-align: left">Kannada</td>
<td style="text-align: left"><code translate="no" dir="ltr">kn-IN</code></td>
</tr>
<tr>
<td style="text-align: left">Assamese</td>
<td style="text-align: left"><code translate="no" dir="ltr">as-IN</code></td>
<td style="text-align: left">Kazakh</td>
<td style="text-align: left"><code translate="no" dir="ltr">kk-KZ</code></td>
</tr>
<tr>
<td style="text-align: left">Azerbaijani</td>
<td style="text-align: left"><code translate="no" dir="ltr">az-AZ</code></td>
<td style="text-align: left">Korean</td>
<td style="text-align: left"><code translate="no" dir="ltr">ko-KR</code></td>
</tr>
<tr>
<td style="text-align: left">Belarusian</td>
<td style="text-align: left"><code translate="no" dir="ltr">be-BY</code></td>
<td style="text-align: left">Kyrgyz</td>
<td style="text-align: left"><code translate="no" dir="ltr">ky-KG</code></td>
</tr>
<tr>
<td style="text-align: left">Bengali (Bangladesh)</td>
<td style="text-align: left"><code translate="no" dir="ltr">bn-BD</code></td>
<td style="text-align: left">Latvian</td>
<td style="text-align: left"><code translate="no" dir="ltr">lv-LV</code></td>
</tr>
<tr>
<td style="text-align: left">Bengali (India)</td>
<td style="text-align: left"><code translate="no" dir="ltr">bn-IN</code></td>
<td style="text-align: left">Lingala</td>
<td style="text-align: left"><code translate="no" dir="ltr">ln-CD</code></td>
</tr>
<tr>
<td style="text-align: left">Bosnian</td>
<td style="text-align: left"><code translate="no" dir="ltr">bs-BA</code></td>
<td style="text-align: left">Lithuanian</td>
<td style="text-align: left"><code translate="no" dir="ltr">lt-LT</code></td>
</tr>
<tr>
<td style="text-align: left">Bulgarian</td>
<td style="text-align: left"><code translate="no" dir="ltr">bg-BG</code></td>
<td style="text-align: left">Macedonian</td>
<td style="text-align: left"><code translate="no" dir="ltr">mk-MK</code></td>
</tr>
<tr>
<td style="text-align: left">Bulgarian (Aromanian)</td>
<td style="text-align: left"><code translate="no" dir="ltr">rup-BG</code></td>
<td style="text-align: left">Malay</td>
<td style="text-align: left"><code translate="no" dir="ltr">ms-MY</code></td>
</tr>
<tr>
<td style="text-align: left">Burmese</td>
<td style="text-align: left"><code translate="no" dir="ltr">my-MM</code></td>
<td style="text-align: left">Malayalam</td>
<td style="text-align: left"><code translate="no" dir="ltr">ml-IN</code></td>
</tr>
<tr>
<td style="text-align: left">Cantonese (Traditional)</td>
<td style="text-align: left"><code translate="no" dir="ltr">yue-Hant-HK</code></td>
<td style="text-align: left">Maltese</td>
<td style="text-align: left"><code translate="no" dir="ltr">mt-MT</code></td>
</tr>
<tr>
<td style="text-align: left">Catalan</td>
<td style="text-align: left"><code translate="no" dir="ltr">ca-ES</code></td>
<td style="text-align: left">Mandarin Chinese (Simplified)</td>
<td style="text-align: left"><code translate="no" dir="ltr">cmn-Hans-CN</code></td>
</tr>
<tr>
<td style="text-align: left">Cebuano</td>
<td style="text-align: left"><code translate="no" dir="ltr">ceb</code></td>
<td style="text-align: left">Marathi</td>
<td style="text-align: left"><code translate="no" dir="ltr">mr-IN</code></td>
</tr>
<tr>
<td style="text-align: left">Central Khmer</td>
<td style="text-align: left"><code translate="no" dir="ltr">km-KH</code></td>
<td style="text-align: left">Mongolian</td>
<td style="text-align: left"><code translate="no" dir="ltr">mn-MN</code></td>
</tr>
<tr>
<td style="text-align: left">Croatian</td>
<td style="text-align: left"><code translate="no" dir="ltr">hr-HR</code></td>
<td style="text-align: left">Nepali</td>
<td style="text-align: left"><code translate="no" dir="ltr">ne-NP</code></td>
</tr>
<tr>
<td style="text-align: left">Czech</td>
<td style="text-align: left"><code translate="no" dir="ltr">cs-CZ</code></td>
<td style="text-align: left">Norwegian</td>
<td style="text-align: left"><code translate="no" dir="ltr">nb-NO</code></td>
</tr>
<tr>
<td style="text-align: left">Danish</td>
<td style="text-align: left"><code translate="no" dir="ltr">da-DK</code></td>
<td style="text-align: left">Oriya</td>
<td style="text-align: left"><code translate="no" dir="ltr">or-IN</code></td>
</tr>
<tr>
<td style="text-align: left">Dutch</td>
<td style="text-align: left"><code translate="no" dir="ltr">nl-NL</code></td>
<td style="text-align: left">Polish</td>
<td style="text-align: left"><code translate="no" dir="ltr">pl-PL</code></td>
</tr>
<tr>
<td style="text-align: left">English (Great Britain)</td>
<td style="text-align: left"><code translate="no" dir="ltr">en-GB</code></td>
<td style="text-align: left">Portuguese (Brazil)</td>
<td style="text-align: left"><code translate="no" dir="ltr">pt-BR</code></td>
</tr>
<tr>
<td style="text-align: left">English (India)</td>
<td style="text-align: left"><code translate="no" dir="ltr">en-IN</code></td>
<td style="text-align: left">Portuguese (Portugal)</td>
<td style="text-align: left"><code translate="no" dir="ltr">pt-PT</code></td>
</tr>
<tr>
<td style="text-align: left">English (United States)</td>
<td style="text-align: left"><code translate="no" dir="ltr">en-US</code></td>
<td style="text-align: left">Punjabi</td>
<td style="text-align: left"><code translate="no" dir="ltr">pa-IN</code></td>
</tr>
<tr>
<td style="text-align: left">Estonian</td>
<td style="text-align: left"><code translate="no" dir="ltr">et-EE</code></td>
<td style="text-align: left">Punjabi (Gurmukhi script)</td>
<td style="text-align: left"><code translate="no" dir="ltr">pa-Guru-IN</code></td>
</tr>
<tr>
<td style="text-align: left">Farsi</td>
<td style="text-align: left"><code translate="no" dir="ltr">fa-IR</code></td>
<td style="text-align: left">Romanian</td>
<td style="text-align: left"><code translate="no" dir="ltr">ro-RO</code></td>
</tr>
<tr>
<td style="text-align: left">Filipino</td>
<td style="text-align: left"><code translate="no" dir="ltr">fil-PH</code></td>
<td style="text-align: left">Russian</td>
<td style="text-align: left"><code translate="no" dir="ltr">ru-RU</code></td>
</tr>
<tr>
<td style="text-align: left">Finnish</td>
<td style="text-align: left"><code translate="no" dir="ltr">fi-FI</code></td>
<td style="text-align: left">Serbian</td>
<td style="text-align: left"><code translate="no" dir="ltr">sr-RS</code></td>
</tr>
<tr>
<td style="text-align: left">French</td>
<td style="text-align: left"><code translate="no" dir="ltr">fr-FR</code></td>
<td style="text-align: left">Sindhi (Arabic script)</td>
<td style="text-align: left"><code translate="no" dir="ltr">sd-Arab-IN</code></td>
</tr>
<tr>
<td style="text-align: left">Galician</td>
<td style="text-align: left"><code translate="no" dir="ltr">gl-ES</code></td>
<td style="text-align: left">Slovak</td>
<td style="text-align: left"><code translate="no" dir="ltr">sk-SK</code></td>
</tr>
<tr>
<td style="text-align: left">Georgian</td>
<td style="text-align: left"><code translate="no" dir="ltr">ka-GE</code></td>
<td style="text-align: left">Slovenian</td>
<td style="text-align: left"><code translate="no" dir="ltr">sl-SI</code></td>
</tr>
<tr>
<td style="text-align: left">German</td>
<td style="text-align: left"><code translate="no" dir="ltr">de-DE</code></td>
<td style="text-align: left">Spanish (Latin America)</td>
<td style="text-align: left"><code translate="no" dir="ltr">es-419</code></td>
</tr>
<tr>
<td style="text-align: left">Greek</td>
<td style="text-align: left"><code translate="no" dir="ltr">el-GR</code></td>
<td style="text-align: left">Spanish (United States)</td>
<td style="text-align: left"><code translate="no" dir="ltr">es-US</code></td>
</tr>
<tr>
<td style="text-align: left">Gujarati</td>
<td style="text-align: left"><code translate="no" dir="ltr">gu-IN</code></td>
<td style="text-align: left">Swahili (Kenya)</td>
<td style="text-align: left"><code translate="no" dir="ltr">sw-KE</code></td>
</tr>
<tr>
<td style="text-align: left">Hausa</td>
<td style="text-align: left"><code translate="no" dir="ltr">ha-NG</code></td>
<td style="text-align: left">Swedish</td>
<td style="text-align: left"><code translate="no" dir="ltr">sv-SE</code></td>
</tr>
<tr>
<td style="text-align: left">Hebrew</td>
<td style="text-align: left"><code translate="no" dir="ltr">he-IL</code></td>
<td style="text-align: left">Tajik</td>
<td style="text-align: left"><code translate="no" dir="ltr">tg-TJ</code></td>
</tr>
<tr>
<td style="text-align: left">Hindi</td>
<td style="text-align: left"><code translate="no" dir="ltr">hi-IN</code></td>
<td style="text-align: left">Telugu</td>
<td style="text-align: left"><code translate="no" dir="ltr">te-IN</code></td>
</tr>
<tr>
<td style="text-align: left">Hungarian</td>
<td style="text-align: left"><code translate="no" dir="ltr">hu-HU</code></td>
<td style="text-align: left">Thai</td>
<td style="text-align: left"><code translate="no" dir="ltr">th-TH</code></td>
</tr>
<tr>
<td style="text-align: left">Icelandic</td>
<td style="text-align: left"><code translate="no" dir="ltr">is-IS</code></td>
<td style="text-align: left">Turkish</td>
<td style="text-align: left"><code translate="no" dir="ltr">tr-TR</code></td>
</tr>
<tr>
<td style="text-align: left">Indian English</td>
<td style="text-align: left"><code translate="no" dir="ltr">en-IN</code></td>
<td style="text-align: left">Ukrainian</td>
<td style="text-align: left"><code translate="no" dir="ltr">uk-UA</code></td>
</tr>
<tr>
<td style="text-align: left">Indonesian</td>
<td style="text-align: left"><code translate="no" dir="ltr">id-ID</code></td>
<td style="text-align: left">Uzbek</td>
<td style="text-align: left"><code translate="no" dir="ltr">uz-UZ</code></td>
</tr>
<tr>
<td style="text-align: left">Italian</td>
<td style="text-align: left"><code translate="no" dir="ltr">it-IT</code></td>
<td style="text-align: left">Vietnamese</td>
<td style="text-align: left"><code translate="no" dir="ltr">vi-VN</code></td>
</tr>
</tbody>
</table>

<h2 id="supported-formats" data-text="Supported audio formats" tabindex="-1">Supported audio formats</h2>

<p>Gemini 3.5 Transcribe supports the following audio format MIME types:</p>

<ul>
<li>WAV - <code translate="no" dir="ltr">audio/wav</code></li>
<li>MP3 - <code translate="no" dir="ltr">audio/mp3</code></li>
<li>AIFF - <code translate="no" dir="ltr">audio/aiff</code></li>
<li>AAC - <code translate="no" dir="ltr">audio/aac</code></li>
<li>OGG - <code translate="no" dir="ltr">audio/ogg</code></li>
<li>FLAC - <code translate="no" dir="ltr">audio/flac</code></li>
<li>MPEG - <code translate="no" dir="ltr">audio/mpeg</code></li>
<li>M4A - <code translate="no" dir="ltr">audio/m4a</code></li>
<li>L16 - <code translate="no" dir="ltr">audio/l16</code></li>
<li>Opus - <code translate="no" dir="ltr">audio/opus</code></li>
<li>ALAW - <code translate="no" dir="ltr">audio/alaw</code></li>
<li>MULAW - <code translate="no" dir="ltr">audio/mulaw</code></li>
<li>WebM - <code translate="no" dir="ltr">audio/webm</code></li>
</ul>

<p>For the complete list of supported MIME types and parameter schemas, see the <a href="/api/interactions-api#Resource:Content">Interactions API reference</a>.</p>

<h2 id="parameter-reference" data-text="Parameter reference" tabindex="-1">Parameter reference</h2>

<p>Configure transcription by setting fields within the <code translate="no" dir="ltr">transcription_config</code> object in <code translate="no" dir="ltr">generation_config</code>:</p>

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
<td style="text-align: left"><code translate="no" dir="ltr">language_codes</code></td>
<td style="text-align: left">Array of strings</td>
<td style="text-align: left">BCP-47 language codes (e.g., <code translate="no" dir="ltr">[&quot;en-US&quot;]</code>). If omitted or empty (<code translate="no" dir="ltr">[]</code>), the model automatically detects the language and handles code-switching.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">custom_vocabulary</code></td>
<td style="text-align: left">Array of strings</td>
<td style="text-align: left">Up to 1,000 custom terms, acronyms, or proper names to bias speech recognition.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">mode</code></td>
<td style="text-align: left">Object or String</td>
<td style="text-align: left">Transcription mode configuration. Accepts <code translate="no" dir="ltr">&quot;smart&quot;</code> or a verbatim mode object (<code translate="no" dir="ltr">{&quot;type&quot;: &quot;verbatim&quot;, ...}</code>). Defaults to verbatim transcription.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">mode.type</code></td>
<td style="text-align: left">String</td>
<td style="text-align: left"><em>(Verbatim mode only)</em> Mode identifier. Always set to <code translate="no" dir="ltr">&quot;verbatim&quot;</code>.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">mode.timestamp_granularities</code></td>
<td style="text-align: left">Array of strings</td>
<td style="text-align: left"><em>(Verbatim mode only)</em> Granularity of timestamps to return. Pass <code translate="no" dir="ltr">[&quot;word&quot;]</code> to enable word start and end offsets.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">mode.diarization_mode</code></td>
<td style="text-align: left">String</td>
<td style="text-align: left"><em>(Verbatim mode only)</em> Diarization mode. Pass <code translate="no" dir="ltr">&quot;speaker&quot;</code> to identify and label distinct speakers.</td>
</tr>
</tbody>
</table>

<h2 id="best-practices" data-text="Best practices" tabindex="-1">Best practices</h2>

<ul>
<li><strong>Provide clean audio:</strong> Ensure audio recordings have clear voice separation and avoid severe clipping.</li>
<li><strong>Provide language hints when known:</strong> If you know the audio language in advance, specify <code translate="no" dir="ltr">language_codes</code> to maximize accuracy.</li>
<li><strong>Target custom vocabulary:</strong> Include only distinct domain terms, brand names, or proper nouns in <code translate="no" dir="ltr">custom_vocabulary</code> rather than common everyday words.</li>
<li><strong>Use the Files API for large recordings:</strong> For files longer than a few seconds, upload the file using <code translate="no" dir="ltr">client.files.upload</code> and pass the returned file URI to the model.</li>
</ul>

<h2 id="limitations" data-text="Limitations" tabindex="-1">Limitations</h2>

<ul>
<li><strong>Audio duration:</strong> Standard unary requests support audio files up to 1 hour. Audio processing is limited to 30 minutes when features like speaker diarization or word-level timestamps are enabled.</li>
<li><strong>Word-level timestamps:</strong> Enabling word-level timestamps may degrade overall transcription accuracy.</li>
<li><strong>Speaker diarization:</strong> Speaker diarization supports up to 8 speakers. Speaker attribution for 3 or more speakers is experimental.</li>
<li><strong>Custom vocabulary:</strong> You can provide up to 1,000 terms in <code translate="no" dir="ltr">custom_vocabulary</code>, but best results are typically achieved with up to 100 terms.</li>
<li><strong>Mode compatibility:</strong> Smart transcription (<code translate="no" dir="ltr">&quot;smart&quot;</code>) cannot be combined with <code translate="no" dir="ltr">timestamp_granularities</code> or <code translate="no" dir="ltr">diarization_mode</code>.</li>
</ul>

<h2 id="whats-next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li>Stream real-time audio with the <a href="/gemini-api/docs/live-api/live-transcribe">Live transcription guide</a> using the Live API.</li>
<li>Explore <a href="/gemini-api/docs/audio">Audio understanding</a> to analyze, summarize, or query audio content.</li>
<li>Learn how to synthesize audio from text using <a href="/gemini-api/docs/speech-generation">Text-to-speech</a>.</li>
<li>Check the <a href="/gemini-api/docs/pricing#gemini-3.5-transcribe">Pricing page</a> for model pricing and token limits.</li>
<li>Check the <a href="/gemini-api/docs/files">Files API</a> guide for details on uploading and managing media files.</li>
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
  <p>Last updated 2026-08-28 UTC.</p>
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