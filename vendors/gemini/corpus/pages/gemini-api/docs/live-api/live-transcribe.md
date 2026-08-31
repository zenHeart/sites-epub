








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/live-api/live-transcribe"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/live-api/live-transcribe" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/live-api/live-transcribe" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=bn" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=fa" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=ru" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=sq" /><title>Live transcription with Gemini Live API &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Live transcription with Gemini Live API &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/live-api/live-transcribe"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
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
      Live transcription with Gemini Live API<devsite-actions hidden data-nosnippet>
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



<p>The Gemini Live API supports low-latency, real-time speech-to-text transcription using the <a href="/gemini-api/docs/models/gemini-3.5-transcribe"><code translate="no" dir="ltr">gemini-3.5-transcribe-live</code></a> model. By connecting to the Live API over WebSockets or using the Google Gen AI SDK, you can stream continuous audio input and receive incremental, real-time text transcriptions as speech occurs.</p>

<div class="quickstart">
  <a class="button button-with-icon button-primary" href="https://aistudio.google.com/live?model=gemini-3.5-transcribe-live">
    Try Live Transcription in Google AI Studio<span class="material-icons icon-after" aria-hidden="true" translate="no">mic</span>
  </a>

  <a class="button button-with-icon button-primary" href="https://github.com/google-gemini/cookbook">
    Open the Colab cookbook<span class="material-icons icon-after" aria-hidden="true" translate="no">code</span>
  </a>

  <a class="button button-with-icon button-primary" href="/gemini-api/docs/coding-agents#gemini-live-api-dev">
    Use coding agent skills<span class="material-icons icon-after" aria-hidden="true" translate="no">terminal</span>
  </a>
</div>

<p>By leveraging the Gemini Live API, developer platforms such as
<a href="https://docs.agora.io/en/ai/models/asr/gemini">Agora</a>,
<a href="https://docs.fishjam.io/tutorials/gemini-live-integration">Fishjam</a>,
<a href="https://docs.livekit.io/agents/models/stt/gemini/">LiveKit</a>,
<a href="https://docs.pipecat.ai/api-reference/server/services/stt/google">Pipecat</a>,
<a href="https://vercel.com/docs/ai-gateway/modalities/speech-to-text">Vercel</a>, and
<a href="https://visionagents.ai/integrations/stt/gemini">Vision Agents</a>
enable developers to build and deploy high-performance voice-driven interfaces
with ease. These platforms manage complex real-time media streaming
infrastructure behind the scenes, allowing developers to focus entirely on
crafting the user experience.</p>

<h2 id="live_agent_versus_live_transcription" data-text="Live agent versus live Transcription" tabindex="-1">Live agent versus live Transcription</h2>

<p>While both use the Live API bidirectional streaming connection, Live Transcription operates as a dedicated, low-latency speech recognition pipeline rather than a conversational agent.</p>

<table>
<thead>
<tr>
<th style="text-align: left">Feature</th>
<th style="text-align: left">Live Agent</th>
<th style="text-align: left">Live Transcription</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left"><strong>Primary role</strong></td>
<td style="text-align: left">Conversational assistant that listens, reasons, and speaks back.</td>
<td style="text-align: left">Real-time speech-to-text pipeline that transcribes incoming audio.</td>
</tr>
<tr>
<td style="text-align: left"><strong>Response modality</strong></td>
<td style="text-align: left">Spoken audio and text (<code translate="no" dir="ltr">response_modalities=[&quot;AUDIO&quot;]</code>).</td>
<td style="text-align: left">Streaming text transcriptions (<code translate="no" dir="ltr">response_modalities=[&quot;TEXT&quot;]</code>).</td>
</tr>
<tr>
<td style="text-align: left"><strong>Interaction style</strong></td>
<td style="text-align: left">Turn-based dialogue with pause detection and interruptions.</td>
<td style="text-align: left">Continuous stream processing as the speaker talks.</td>
</tr>
<tr>
<td style="text-align: left"><strong>Supported features</strong></td>
<td style="text-align: left">Function calling, Google Search, system instructions.</td>
<td style="text-align: left">Speech biasing (<code translate="no" dir="ltr">custom_vocabulary</code>), language detection, manual &amp; hybrid VAD, Smart transcription.</td>
</tr>
<tr>
<td style="text-align: left"><strong>Input stream</strong></td>
<td style="text-align: left">Multimodal: audio, video, images, text.</td>
<td style="text-align: left">Audio input (raw 16-bit PCM).</td>
</tr>
</tbody>
</table>

<h2 id="get_started" data-text="Get started" tabindex="-1">Get started</h2>

<p>The following examples demonstrate how to open a bidirectional streaming session with <code translate="no" dir="ltr">gemini-3.5-transcribe-live</code> and receive real-time transcriptions.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">asyncio</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-n">model</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"gemini-3.5-transcribe-live"</span>

<span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">LiveConnectConfig</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"TEXT"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">input_audio_transcription</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AudioTranscriptionConfig</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">language_codes</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[],</span>  <span class="devsite-syntax-c1"># Automatic language detection</span>
    <span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">main</span><span class="devsite-syntax-p">():</span>
    <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">aio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">live</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">connect</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">config</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Session established with Live Transcription"</span><span class="devsite-syntax-p">)</span>

        <span class="devsite-syntax-c1"># Receive transcription events</span>
        <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">response</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">receive</span><span class="devsite-syntax-p">():</span>
            <span class="devsite-syntax-n">server_content</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">server_content</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">server_content</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">server_content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">input_transcription</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Transcript:"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">server_content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">input_transcription</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">if</span> <span class="devsite-syntax-vm">__name__</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"__main__"</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">asyncio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">run</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">main</span><span class="devsite-syntax-p">())</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.5-transcribe-live'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">TEXT</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">languageCodes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[],</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-c1">// Automatic language detection</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">session</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">live</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">connect</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">callbacks</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onopen</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Connected to Live Transcription'</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onmessage</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inputTranscription</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Transcript:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inputTranscription</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onerror</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">error</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Error:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">onclose</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Connection closed:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">e</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">reason</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
<section><h3 id="websockets" data-text="WebSockets" tabindex="-1">WebSockets</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">API_KEY</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"YOUR_API_KEY"</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">MODEL_NAME</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.5-transcribe-live"</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">WS_URL</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-sb">`wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">API_KEY</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">WebSocket</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">WS_URL</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">onopen</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'WebSocket connected'</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">setup</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-sb">`models/</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">MODEL_NAME</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">generationConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'TEXT'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">languageCodes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[]</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">};</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-p">};</span>

<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">onmessage</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inputTranscription</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'Transcript:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inputTranscription</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">};</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="interim-transcriptions" data-text="Interim and finalized transcriptions" tabindex="-1">Interim and finalized transcriptions</h2>

<p>As audio streams into the Live API, the server emits two complementary transcription fields within <code translate="no" dir="ltr">server_content</code>:</p>

<ul>
<li><strong><code translate="no" dir="ltr">interim_input_transcription</code></strong>: low-latency, speculative partial hypotheses updated while the speaker is actively talking. These partial updates occur rapidly with minimal delay. Use <code translate="no" dir="ltr">interim_input_transcription</code> to render responsive live UI subtitles or preview captions.</li>
<li><strong><code translate="no" dir="ltr">input_transcription</code></strong>: the finalized transcript emitted when the speaker pauses, the turn completes, or speech is finalized. Once emitted, this text represents the model&#39;s authoritative transcription of that speech segment. In smart transcription mode, this will include the cleaned, formatted response.</li>
</ul>

<p>The following example demonstrates how to display streaming interim partials and commit final transcripts:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">def</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nf">receive_transcripts</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">session</span><span class="devsite-syntax-p">):</span>
    <span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">response</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">receive</span><span class="devsite-syntax-p">():</span>
        <span class="devsite-syntax-n">server_content</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">server_content</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-ow">not</span> <span class="devsite-syntax-n">server_content</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">continue</span>

        <span class="devsite-syntax-c1"># Real-time interim hypothesis (updates dynamically as user speaks)</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">server_content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interim_input_transcription</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-n">interim_text</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">server_content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interim_input_transcription</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\r</span><span class="devsite-syntax-s2">[Interim] </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">interim_text</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">""</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">flush</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>

        <span class="devsite-syntax-c1"># Finalized transcript (emitted on speech completion)</span>
        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">server_content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">input_transcription</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-n">final_text</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">server_content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">input_transcription</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span>
            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n</span><span class="devsite-syntax-s2">[Final] </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">final_text</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-nx">onmessage</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">message</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">return</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interimInputTranscription</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-c1">// Update live subtitle preview on screen</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">renderInterimPreview</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interimInputTranscription</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inputTranscription</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-c1">// Append final committed transcript to chat history</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">commitFinalTranscript</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inputTranscription</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">};</span>
</code></pre></devsite-code></section>
<section><h3 id="websockets_1" data-text="WebSockets" tabindex="-1">WebSockets</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">onmessage</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">event</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">serverContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interimInputTranscription</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'[Interim]:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interimInputTranscription</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-o">?</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inputTranscription</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'[Final]:'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">inputTranscription</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">};</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="sending_audio" data-text="Sending audio" tabindex="-1">Sending audio</h2>

<p>Stream audio chunks over the active connection as raw 16-bit PCM audio.</p>
<ul>
<li><strong>Audio format:</strong> Raw 16-bit PCM at 16kHz (mono, little-endian).</li>
<li><strong>Chunk size:</strong> Send audio in chunks of 100ms (1,024 to 2,048 frames).</li>
<li><p><strong>MIME type:</strong> <code translate="no" dir="ltr">audio/pcm;rate=16000</code> (or the matching sample rate).</p></li>
</ul>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Stream a raw PCM audio chunk</span>
<span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_realtime_input</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">audio</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Blob</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">data</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">audio_chunk_bytes</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"audio/pcm;rate=16000"</span>
    <span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-c1"># Signal the end of the audio stream when finished</span>
<span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_realtime_input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">audio_stream_end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Send base64-encoded PCM audio chunk</span>
<span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendRealtimeInput</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">audio</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioChunkBase64</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'audio/pcm;rate=16000'</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-c1">// Signal stream end</span>
<span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendRealtimeInput</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">audioStreamEnd</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="websockets_2" data-text="WebSockets" tabindex="-1">WebSockets</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Send base64-encoded PCM audio chunk</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">realtimeInput</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">audio</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">audioChunkBase64</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'audio/pcm;rate=16000'</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}));</span>

<span class="devsite-syntax-c1">// Signal stream end</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">realtimeInput</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">audioStreamEnd</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}));</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="transcription_features" data-text="Transcription features" tabindex="-1">Transcription features</h2>

<h3 id="automatic_language_detection" data-text="Automatic language detection" tabindex="-1">Automatic language detection</h3>

<p>By default, omitting <code translate="no" dir="ltr">language_codes</code> or setting <code translate="no" dir="ltr">language_codes=[]</code> enables automatic language identification. The model dynamically detects the spoken language across utterances, including multilingual conversations and code-switching.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_3" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">LiveConnectConfig</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"TEXT"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">input_audio_transcription</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AudioTranscriptionConfig</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">language_codes</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[],</span>
    <span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_3" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">TEXT</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">languageCodes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
</code></pre></devsite-code></section>
<section><h3 id="websockets_3" data-text="WebSockets" tabindex="-1">WebSockets</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">setup</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'models/gemini-3.5-transcribe-live'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generationConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'TEXT'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">languageCodes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="specific_language_hint" data-text="Specific language hint" tabindex="-1">Specific language hint</h3>

<p>Provide explicit BCP-47 language codes (for example, <code translate="no" dir="ltr">[&quot;es-ES&quot;]</code> for Spanish or <code translate="no" dir="ltr">[&quot;fr-FR&quot;]</code> for French) to bias recognition toward specific languages (see <a href="#supported-languages">Supported languages</a>).</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_4" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">LiveConnectConfig</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"TEXT"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">input_audio_transcription</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AudioTranscriptionConfig</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">language_codes</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"es-ES"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_4" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">TEXT</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">languageCodes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'es-ES'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
</code></pre></devsite-code></section>
<section><h3 id="websockets_4" data-text="WebSockets" tabindex="-1">WebSockets</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">setup</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'models/gemini-3.5-transcribe-live'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generationConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'TEXT'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">languageCodes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'es-ES'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="custom_vocabulary_biasing" data-text="Custom vocabulary biasing" tabindex="-1">Custom vocabulary biasing</h3>

<p>Provide a list of up to 1,000 phrases, proper nouns, brand names, or technical terms in <code translate="no" dir="ltr">custom_vocabulary</code> to bias speech recognition toward specific terminology (best results are typically achieved with up to 100 terms).</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_5" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">LiveConnectConfig</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"TEXT"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">input_audio_transcription</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AudioTranscriptionConfig</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">language_codes</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[],</span>
        <span class="devsite-syntax-n">custom_vocabulary</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"Gemini"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"Kubernetes"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"BigQuery"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_5" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">TEXT</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">languageCodes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">customVocabulary</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'Gemini'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Kubernetes'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'BigQuery'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
</code></pre></devsite-code></section>
<section><h3 id="websockets_5" data-text="WebSockets" tabindex="-1">WebSockets</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">setup</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'models/gemini-3.5-transcribe-live'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generationConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'TEXT'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">languageCodes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[],</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">customVocabulary</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'Gemini'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Kubernetes'</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'BigQuery'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="smart-transcription" data-text="Smart transcription" tabindex="-1">Smart transcription</h3>

<p>Configure transcription output formatting using the <code translate="no" dir="ltr">mode</code> parameter in <code translate="no" dir="ltr">input_audio_transcription</code>:</p>
<ul>
<li><strong><code translate="no" dir="ltr">VERBATIM</code> (default)</strong>: Produces an exact literal transcript of everything spoken, preserving raw filler words (&quot;um&quot;, &quot;uh&quot;, &quot;like&quot;), repetitions, and false starts.</li>
<li><p><strong><code translate="no" dir="ltr">SMART</code> (Smart transcription)</strong>: Cleans up and structures the transcript for readability:</p>

<ul>
<li><strong>Disfluency removal</strong>: Removes filler words, stuttering, and false starts.</li>
<li><strong>Inline self-corrections</strong>: Resolves spoken corrections naturally.</li>
<li><strong>Structured formatting</strong>: Automatically formats lists, bullet points, numbers, dates, and paragraph breaks.</li>
<li><strong>Grammar &amp; casing</strong>: Applies natural capitalization and punctuation polish.</li>
</ul></li>
</ul>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_6" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">LiveConnectConfig</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"TEXT"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">input_audio_transcription</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AudioTranscriptionConfig</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">mode</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"SMART"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_6" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">TEXT</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">mode</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'SMART'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
</code></pre></devsite-code></section>
<section><h3 id="websockets_6" data-text="WebSockets" tabindex="-1">WebSockets</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">setup</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'models/gemini-3.5-transcribe-live'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generationConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'TEXT'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mode</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'SMART'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="voice_activity_detection_vad_strategies" data-text="Voice Activity Detection (VAD) strategies" tabindex="-1">Voice Activity Detection (VAD) strategies</h2>

<h3 id="automatic_vad_default" data-text="Automatic VAD (Default)" tabindex="-1">Automatic VAD (Default)</h3>

<p>By default, server-side automatic Voice Activity Detection detects when a speaker begins and stops speaking.</p>

<h3 id="hybrid-vad" data-text="Hybrid VAD" tabindex="-1">Hybrid VAD</h3>

<p><a href="/gemini-api/docs/live-api/capabilities#hybrid-vad">Hybrid VAD</a> combines server-side automatic speech start detection with client-side speech end detection for zero-latency turn finalization:</p>

<ol>
<li><strong>Server-side automatic VAD remains enabled</strong> to detect speech beginnings accurately with prefix audio padding, preventing front-word truncation.</li>
<li><strong>Client-side VAD detects silence</strong>: When a local on-device VAD detects that the speaker has stopped talking, the client sends an <code translate="no" dir="ltr">audio_stream_end</code> signal immediately.</li>
<li><strong>Fast finalization</strong>: The server treats <code translate="no" dir="ltr">audio_stream_end</code> as an immediate turn finalization prompt, bypassing the default server-side silence wait time and returning the finalized transcript with minimal latency.</li>
<li><strong>Fallback</strong>: If the client VAD fails to trigger, the server-side VAD acts as an automatic fallback.</li>
</ol>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_7" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">LiveConnectConfig</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"TEXT"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">input_audio_transcription</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AudioTranscriptionConfig</span><span class="devsite-syntax-p">(),</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">aio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">live</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">connect</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">config</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-c1"># Stream audio chunks...</span>
    <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_realtime_input</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">audio</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Blob</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"audio/pcm;rate=16000"</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-p">)</span>

    <span class="devsite-syntax-c1"># When client-side VAD detects end of speech, send audio_stream_end:</span>
    <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_realtime_input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">audio_stream_end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_7" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">TEXT</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{},</span>
<span class="devsite-syntax-p">};</span>

<span class="devsite-syntax-c1">// Stream audio...</span>
<span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendRealtimeInput</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">audio</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chunkBase64</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'audio/pcm;rate=16000'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-c1">// When client VAD detects end of speech, send audioStreamEnd:</span>
<span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendRealtimeInput</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">audioStreamEnd</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="websockets_7" data-text="WebSockets" tabindex="-1">WebSockets</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">setup</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'models/gemini-3.5-transcribe-live'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generationConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'TEXT'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-p">));</span>

<span class="devsite-syntax-c1">// Stream audio...</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">realtimeInput</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">audio</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chunkBase64</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'audio/pcm;rate=16000'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}));</span>

<span class="devsite-syntax-c1">// When client VAD detects end of speech, send audioStreamEnd:</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">realtimeInput</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">audioStreamEnd</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}));</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="manual_vad_push-to-talk" data-text="Manual VAD (Push-to-Talk)" tabindex="-1">Manual VAD (Push-to-Talk)</h3>

<p>For walkie-talkie interfaces or push-to-talk buttons, disable automatic VAD entirely and control turn boundaries explicitly using <code translate="no" dir="ltr">activity_start</code> and <code translate="no" dir="ltr">activity_end</code>:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_8" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">config</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">LiveConnectConfig</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">response_modalities</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"TEXT"</span><span class="devsite-syntax-p">],</span>
    <span class="devsite-syntax-n">realtime_input_config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">RealtimeInputConfig</span><span class="devsite-syntax-p">(</span>
        <span class="devsite-syntax-n">automatic_activity_detection</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AutomaticActivityDetection</span><span class="devsite-syntax-p">(</span>
            <span class="devsite-syntax-n">disabled</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-kc">True</span>
        <span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-p">),</span>
    <span class="devsite-syntax-n">input_audio_transcription</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">AudioTranscriptionConfig</span><span class="devsite-syntax-p">(),</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">async</span> <span class="devsite-syntax-k">with</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">aio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">live</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">connect</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">model</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">config</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-k">as</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-c1"># Button pressed: signal speech start</span>
    <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_realtime_input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">activity_start</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">ActivityStart</span><span class="devsite-syntax-p">())</span>

    <span class="devsite-syntax-c1"># Stream audio chunks...</span>
    <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_realtime_input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">audio</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Blob</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">data</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">chunk</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"audio/pcm;rate=16000"</span><span class="devsite-syntax-p">))</span>

    <span class="devsite-syntax-c1"># Button released: signal speech end</span>
    <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">session</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_realtime_input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">activity_end</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">ActivityEnd</span><span class="devsite-syntax-p">())</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_8" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">Modality</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">TEXT</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">realtimeInputConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">automaticActivityDetection</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">disabled</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{},</span>
<span class="devsite-syntax-p">};</span>

<span class="devsite-syntax-c1">// Signal speech start</span>
<span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendRealtimeInput</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">activityStart</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-c1">// Stream audio...</span>

<span class="devsite-syntax-c1">// Signal speech end</span>
<span class="devsite-syntax-nx">session</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">sendRealtimeInput</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">activityEnd</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="websockets_8" data-text="WebSockets" tabindex="-1">WebSockets</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">setup</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'models/gemini-3.5-transcribe-live'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">generationConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'TEXT'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">realtimeInputConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">automaticActivityDetection</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">disabled</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">};</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">setupMessage</span><span class="devsite-syntax-p">));</span>

<span class="devsite-syntax-c1">// Button pressed: signal speech start</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">realtimeInput</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">activityStart</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">}));</span>

<span class="devsite-syntax-c1">// Stream audio...</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">realtimeInput</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">audio</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">chunkBase64</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'audio/pcm;rate=16000'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">}));</span>

<span class="devsite-syntax-c1">// Button released: signal speech end</span>
<span class="devsite-syntax-nx">websocket</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">send</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">realtimeInput</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">activityEnd</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">}));</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="ephemeral_tokens_in_client_applications" data-text="Ephemeral tokens in client applications" tabindex="-1">Ephemeral tokens in client applications</h2>

<p>For client-to-server applications (such as mobile or web apps streaming directly from a microphone), use <a href="/gemini-api/docs/live-api/ephemeral-tokens">ephemeral tokens</a> to avoid exposing your API key in client code.</p>

<p>Create a constrained ephemeral token on your server before initiating the client connection:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_9" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">datetime</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-n">expire_time</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">datetime</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">datetime</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">now</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">tz</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">datetime</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">timezone</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">utc</span><span class="devsite-syntax-p">)</span> <span class="devsite-syntax-o">+</span> <span class="devsite-syntax-n">datetime</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">timedelta</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">minutes</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">30</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">token</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">auth_tokens</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"uses"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"expire_time"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">expire_time</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"live_connect_constraints"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s2">"model"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"gemini-3.5-transcribe-live"</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s2">"config"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                <span class="devsite-syntax-s2">"response_modalities"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"TEXT"</span><span class="devsite-syntax-p">],</span>
                <span class="devsite-syntax-s2">"input_audio_transcription"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
                    <span class="devsite-syntax-s2">"language_codes"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[],</span>
                <span class="devsite-syntax-p">},</span>
            <span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">},</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_9" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">expireTime</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Date</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">Date</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">now</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">+</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">30</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">60</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">1000</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-nx">toISOString</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">token</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">authTokens</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">uses</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">1</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">expireTime</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">expireTime</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">liveConnectConstraints</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.5-transcribe-live'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">responseModalities</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s1">'TEXT'</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">inputAudioTranscription</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">languageCodes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[],</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="rest" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/auth_tokens"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">GEMINI_API_KEY</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "uses": 1,</span>
<span class="devsite-syntax-s1">    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",</span>
<span class="devsite-syntax-s1">    "liveConnectConstraints": {</span>
<span class="devsite-syntax-s1">      "model": "models/gemini-3.5-transcribe-live",</span>
<span class="devsite-syntax-s1">      "config": {</span>
<span class="devsite-syntax-s1">        "responseModalities": ["TEXT"],</span>
<span class="devsite-syntax-s1">        "inputAudioTranscription": {</span>
<span class="devsite-syntax-s1">          "languageCodes": []</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="supported-languages" data-text="Supported languages" tabindex="-1">Supported languages</h2>

<p>The following languages and BCP-47 language codes are supported for Gemini 3.5 Transcribe Live:</p>

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

<h2 id="parameter-reference" data-text="Parameter reference" tabindex="-1">Parameter reference</h2>

<p>Configure live transcription using fields in <code translate="no" dir="ltr">input_audio_transcription</code> and <code translate="no" dir="ltr">realtime_input_config</code>:</p>

<table>
<thead>
<tr>
<th style="text-align: left">Parameter</th>
<th style="text-align: left">Type</th>
<th style="text-align: left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">language_codes</code></td>
<td style="text-align: left">Array of strings</td>
<td style="text-align: left">BCP-47 language codes (e.g., <code translate="no" dir="ltr">[&quot;en-US&quot;]</code>). If omitted or empty (<code translate="no" dir="ltr">[]</code>), the model automatically detects the language and handles multilingual speech.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">custom_vocabulary</code></td>
<td style="text-align: left">Array of strings</td>
<td style="text-align: left">Up to 1,000 custom terms, acronyms, brand names, or proper nouns to bias speech recognition.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">mode</code></td>
<td style="text-align: left">String</td>
<td style="text-align: left">Transcription mode: <code translate="no" dir="ltr">&quot;VERBATIM&quot;</code> (default) or <code translate="no" dir="ltr">&quot;SMART&quot;</code> (Smart transcription). When set to <code translate="no" dir="ltr">&quot;SMART&quot;</code>, the model removes filler words, formats lists, and corrects disfluencies.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">automatic_activity_detection.disabled</code></td>
<td style="text-align: left">Boolean</td>
<td style="text-align: left">Set to <code translate="no" dir="ltr">true</code> to disable automatic voice activity detection and manually send <code translate="no" dir="ltr">activityStart</code> and <code translate="no" dir="ltr">activityEnd</code> signals.</td>
</tr>
</tbody>
</table>

<h3 id="server_response_fields" data-text="Server response fields" tabindex="-1">Server response fields</h3>

<table>
<thead>
<tr>
<th style="text-align: left">Field</th>
<th style="text-align: left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">server_content.interim_input_transcription</code></td>
<td style="text-align: left">Low-latency, interim partial transcription hypothesis emitted continuously while the user is actively speaking.</td>
</tr>
<tr>
<td style="text-align: left"><code translate="no" dir="ltr">server_content.input_transcription</code></td>
<td style="text-align: left">Finalized, authoritative input transcript emitted when a speech turn finishes.</td>
</tr>
</tbody>
</table>

<h2 id="limitations" data-text="Limitations" tabindex="-1">Limitations</h2>

<ul>
<li><strong>Session duration:</strong> Live transcription sessions support continuous streaming for up to 10 minutes.</li>
<li><strong>Speaker diarization:</strong> Speaker diarization is not supported in live streaming sessions. For speaker diarization, use the non-streaming <a href="/gemini-api/docs/transcribe#speaker-diarization">Audio transcription</a> endpoint.</li>
<li><strong>Word-level timestamps:</strong> Word-level timestamps are not supported over the Live API. The Live API emits utterance-level timestamps (<code translate="no" dir="ltr">interim_input_transcription</code> and <code translate="no" dir="ltr">input_transcription</code>).</li>
<li><strong>Custom vocabulary:</strong> You can provide up to 1,000 terms in <code translate="no" dir="ltr">custom_vocabulary</code>, but best results are typically achieved with up to 100 terms.</li>
<li><strong>Mode compatibility:</strong> Smart transcription (<code translate="no" dir="ltr">&quot;mode&quot;: &quot;SMART&quot;</code>) removes filler words and formats intent-aware text, but cannot be combined with word annotations.</li>
</ul>

<h2 id="whats-next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li>Read the <a href="/gemini-api/docs/transcribe">Gemini Transcribe documentation</a> for non-streaming audio files.</li>
<li>Read the <a href="/gemini-api/docs/live-api">Live API overview</a> for conversational voice agents.</li>
<li>Read the <a href="/gemini-api/docs/live-api/live-translate">Live translation guide</a> for real-time speech-to-speech translation.</li>
<li>Check the <a href="/gemini-api/docs/pricing#gemini-3.5-transcribe-live">Pricing page</a> for Live API streaming pricing.</li>
<li>Explore the <a href="/gemini-api/docs/live-api/capabilities">Live API capabilities guide</a>.</li>
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