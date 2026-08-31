








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/api/environments"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/api/environments" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/api/environments" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/api/environments?hl=bn" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/api/environments?hl=fa" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/api/environments?hl=ru" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/api/environments?hl=sq" /><title>Gemini Environments API &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Gemini Environments API &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta property="og:url" content="https://ai.google.dev/api/environments"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675"><meta property="og:locale" content="en"><meta name="twitter:card" content="summary_large_image">
  







<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&amp;family=Roboto+Mono:wght@400;500&amp;display=swap" rel="stylesheet" data-page-link>

    </head>
  <body class="gemini-api docs color-scheme--light"
        template="page"
        theme="googledevai-theme"
        type="reference"
        
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
      
        
          <tab  >
            
    <a href="https://ai.google.dev/gemini-api/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://ai.google.dev/gemini-api/docs"
    
       track-type="nav"
       track-metadata-position="nav - docs"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Docs"
         
           track-name="docs"
         
       >
    Docs
  
    </a>
    
  
          </tab>
        
      
        
          <tab  class="devsite-active">
            
    <a href="https://ai.google.dev/api"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://ai.google.dev/api"
    
       track-type="nav"
       track-metadata-position="nav - api reference"
       track-metadata-module="primary nav"
       aria-label="API reference, selected" 
       
         
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
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Docs"
      
        track-name="docs"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Docs"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Docs
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/api"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: API reference"
      
        track-name="api reference"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: API reference"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip menu="_book">
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
            <li class="devsite-nav-item"><a href="/api"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini-api/docs/api-versions"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>API versions</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Core APIs</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/api/interactions-api"
        class="devsite-nav-title"
      
        alt-paths=" /api/interactions-api-v1 "><span class="devsite-nav-text" tooltip>Interactions API</span></a></li>

  <li class="devsite-nav-item"><a href="/api/generate-content"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>GenerateContent</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Real time APIs</span>
      </div></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/api/live"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Live API</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-preview"><a href="/api/live_music"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Live Music API</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Platform APIs</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/api/models"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Model API</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-beta"><a href="/api/agents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Agents</span><span class="devsite-nav-icon material-icons"
        data-icon="beta"
        data-title="Beta"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-beta"><a href="/api/webhooks"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Webhooks</span><span class="devsite-nav-icon material-icons"
        data-icon="beta"
        data-title="Beta"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-beta"><a href="/api/triggers"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Triggers</span><span class="devsite-nav-icon material-icons"
        data-icon="beta"
        data-title="Beta"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-beta"><a href="/api/environments"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Environments</span><span class="devsite-nav-icon material-icons"
        data-icon="beta"
        data-title="Beta"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item"><a href="/api/batch-api"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Batch API</span></a></li>

  <li class="devsite-nav-item"><a href="/api/files"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Files API</span></a></li>

  <li class="devsite-nav-item"><a href="/api/tokens"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Tokens</span></a></li>

  <li class="devsite-nav-item"><a href="/api/caching"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Caching</span></a></li>

  <li class="devsite-nav-item"><a href="/api/embeddings"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Embeddings</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>File Search API</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/api/file-search/file-search-stores"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>File search stores</span></a></li><li class="devsite-nav-item"><a href="/api/file-search/documents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Documents</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/api/all-methods"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>All methods</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>SDK references</span>
      </div></li>

  <li class="devsite-nav-item
           devsite-nav-external"><a href="https://googleapis.github.io/python-genai/"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Python</span><span class="devsite-nav-icon material-icons"
        data-icon="external"
        data-title="External"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-external"><a href="https://pkg.go.dev/google.golang.org/genai"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Go</span><span class="devsite-nav-icon material-icons"
        data-icon="external"
        data-title="External"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-external"><a href="https://googleapis.github.io/js-genai/"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>TypeScript</span><span class="devsite-nav-icon material-icons"
        data-icon="external"
        data-title="External"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-external"><a href="https://googleapis.github.io/java-genai/javadoc/"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Java</span><span class="devsite-nav-icon material-icons"
        data-icon="external"
        data-title="External"
        aria-hidden="true"></span></a></li>

  <li class="devsite-nav-item
           devsite-nav-external"><a href="https://googleapis.github.io/dotnet-genai/"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>C#</span><span class="devsite-nav-icon material-icons"
        data-icon="external"
        data-title="External"
        aria-hidden="true"></span></a></li>
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
    
    
    
      
        
  <a href="https://ai.google.dev/api"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="3"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="3"
      
        track-metadata-eventdetail=""
      
    >
    
          API reference
        
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
      Gemini Environments API<devsite-actions hidden data-nosnippet>
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

  
    
    
<p>Environments provide isolated execution contexts for running agent code, tools, and services securely.</p>
<div class="markdown-actions" style="margin-top: 16px; margin-bottom: 24px;">
<a class="md-button" href="/static/api/environments.md.txt" target="_blank">View as markdown</a>
<a class="md-button" href="/static/api/interactions.openapi.json" target="_blank">View the OpenAPI Spec</a>
</div>
<aside class="note">
<p>This API is in Beta. Endpoints are under <code translate="no" dir="ltr">/v1beta/</code>.</p>
</aside>

<div class="prototype" itemscope="" itemtype="http://developers.google.com/ReferenceObject">
<h2 id="CreateEnvironment" data-text="CreateEnvironment" tabindex="-1">CreateEnvironment</h2>
<div>
<span class="endpoint">
<span class="http-method post">
                post
            </span>
</span>
<span class="endpoint-url" style="font-size: 16px; color: var(--devsite-code-color);">
            https://generativelanguage.googleapis.com/v1beta/environments
        </span>
</div>
<section id="description">
<p>Creates an environment.</p>
</section>
<section class="prototype">
<ul class="toc">
<li><a href="#CreateEnvironment.request_body">Request body</a></li> <li><a href="#CreateEnvironment.response">Response</a></li>
</ul>
<div class="column-container request-section" style="margin-top: 48px;">
<div class="reference">
<section id="CreateEnvironment.request_body">
<h3 id="request-body" data-text="Request body" tabindex="-1">Request body</h3>
<p>The request body contains data with the following structure:</p>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">network</span>
<span class="field-type">EnvironmentNetworkEgressAllowlist or enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>Network configuration for the environment.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">Outbound networking configuration for the sandbox. Accepts an object with an 'allowlist' array to restrict traffic, or the string 'disabled' to turn off all network access. Omit entirely to allow all outbound traffic with no header injection.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="possible-types" data-text="Possible Types" tabindex="-1">Possible Types</h4>
<details class="subtype-details">
<summary class="subtype-summary">
<span style="font-weight: 500;">object</span>
</summary>
<div class="subtype-content">
<p>Outbound networking configuration for the sandbox. When specified, restricts which external domains the sandbox can reach. Omit entirely to allow all outbound traffic with no header injection.</p>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">allowlist</span>
<span class="field-type">array (AllowlistEntry)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>List of allowed outbound domains. Only requests to listed domains are permitted. Use [{'domain': '*'}] to allow all domains while still injecting headers on specific ones.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">A single domain allowlist rule with optional header injection.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">domain</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Domain to allow outbound requests to. Supports wildcards (e.g. '*.googleapis.com'). Use '*' to allow all domains.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">transform</span>
<span class="field-type">array (object) or object</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Headers to inject on all outbound requests matching this domain. Accepts a single dict or a list of dicts. The egress proxy injects these automatically.</p>
</div>
</div>
</div>
</div>
</section>
</div>
</details>
</div>
</details>
<details class="subtype-details">
<summary class="subtype-summary">
<span style="font-weight: 500;">string</span>
</summary>
<div class="subtype-content">
<p>Turns all network off.</p>
</div>
</details>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="possible-values" data-text="Possible values" tabindex="-1">Possible values</h4>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">disabled</code>
<p style="margin-left: 16px; font-size: 13px; color: var(--devsite-text-secondary);">Turns all network off.</p> </li>
</ul>
</div>
</div>
</section>
</div>
</details>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">sources</span>
<span class="field-type">array (Source)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>Sources to be mounted into the environment.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">A source to be mounted into the environment.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields_1" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">content</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>The inline content if `type` is `INLINE`.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">encoding</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Optional encoding for inline content (e.g. `base64`).</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">source</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>The source of the environment.
For Cloud Storage, this is the Cloud Storage path.
For GitHub, this is the GitHub path.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">target</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Where the source should appear in the environment.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">type</span>
<span class="field-type">enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>No description provided.</p>
<p style="margin-top: 8px; font-weight: 500; font-size: 13px; color: var(--devsite-text-secondary);">Possible
            values:</p>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">gcs</code>
<p style="margin-left: 16px; font-size: 13px;">A Cloud Storage bucket.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">inline</code>
<p style="margin-left: 16px; font-size: 13px;">Inline content.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">repository</code>
<p style="margin-left: 16px; font-size: 13px;">A generic repository. The protocol prefix in the source URL
identifies the provider (e.g., github://, gcs://).</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">skill_registry</code>
<p style="margin-left: 16px; font-size: 13px;">A skill resource from the Skill Registry Service.
Skill: projects/{project}/locations/{location}/skills/{skill}
SkillRevision:
projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}
Support mounting all skills under a project:
projects/{project}/locations/{location}/skills.</p> </li>
</ul>
</div>
</div>
</div>
</div>
</section>
</div>
</details>
</section>
<section id="CreateEnvironment.response">
<h3 id="response" data-text="Response" tabindex="-1">Response</h3>
<p>If successful, the response body contains data with the following structure:</p>
<div class="field-entry">
<div class="signature">
<span class="field-name">created</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The time at which the environment was created in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">file_count</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The number of files in the environment, output only.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">id</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Required. Output only. The ID of the environment.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">last_accessed</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The time at which the environment was last accessed in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).</p>
</div>
</div>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">network</span>
<span class="field-type">EnvironmentNetworkEgressAllowlist or enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>Network configuration for the environment.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">Outbound networking configuration for the sandbox. Accepts an object with an 'allowlist' array to restrict traffic, or the string 'disabled' to turn off all network access. Omit entirely to allow all outbound traffic with no header injection.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="possible-types_1" data-text="Possible Types" tabindex="-1">Possible Types</h4>
<details class="subtype-details">
<summary class="subtype-summary">
<span style="font-weight: 500;">object</span>
</summary>
<div class="subtype-content">
<p>Outbound networking configuration for the sandbox. When specified, restricts which external domains the sandbox can reach. Omit entirely to allow all outbound traffic with no header injection.</p>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">allowlist</span>
<span class="field-type">array (AllowlistEntry)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>List of allowed outbound domains. Only requests to listed domains are permitted. Use [{'domain': '*'}] to allow all domains while still injecting headers on specific ones.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">A single domain allowlist rule with optional header injection.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields_2" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">domain</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Domain to allow outbound requests to. Supports wildcards (e.g. '*.googleapis.com'). Use '*' to allow all domains.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">transform</span>
<span class="field-type">array (object) or object</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Headers to inject on all outbound requests matching this domain. Accepts a single dict or a list of dicts. The egress proxy injects these automatically.</p>
</div>
</div>
</div>
</div>
</section>
</div>
</details>
</div>
</details>
<details class="subtype-details">
<summary class="subtype-summary">
<span style="font-weight: 500;">string</span>
</summary>
<div class="subtype-content">
<p>Turns all network off.</p>
</div>
</details>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="possible-values_1" data-text="Possible values" tabindex="-1">Possible values</h4>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">disabled</code>
<p style="margin-left: 16px; font-size: 13px; color: var(--devsite-text-secondary);">Turns all network off.</p> </li>
</ul>
</div>
</div>
</section>
</div>
</details>
<div class="field-entry">
<div class="signature">
<span class="field-name">size_bytes</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The total size of the environment files in bytes, output only.</p>
</div>
</div>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">sources</span>
<span class="field-type">array (Source)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>Sources to be mounted into the environment.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">A source to be mounted into the environment.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields_3" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">content</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>The inline content if `type` is `INLINE`.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">encoding</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Optional encoding for inline content (e.g. `base64`).</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">source</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>The source of the environment.
For Cloud Storage, this is the Cloud Storage path.
For GitHub, this is the GitHub path.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">target</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Where the source should appear in the environment.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">type</span>
<span class="field-type">enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>No description provided.</p>
<p style="margin-top: 8px; font-weight: 500; font-size: 13px; color: var(--devsite-text-secondary);">Possible
            values:</p>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">gcs</code>
<p style="margin-left: 16px; font-size: 13px;">A Cloud Storage bucket.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">inline</code>
<p style="margin-left: 16px; font-size: 13px;">Inline content.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">repository</code>
<p style="margin-left: 16px; font-size: 13px;">A generic repository. The protocol prefix in the source URL
identifies the provider (e.g., github://, gcs://).</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">skill_registry</code>
<p style="margin-left: 16px; font-size: 13px;">A skill resource from the Skill Registry Service.
Skill: projects/{project}/locations/{location}/skills/{skill}
SkillRevision:
projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}
Support mounting all skills under a project:
projects/{project}/locations/{location}/skills.</p> </li>
</ul>
</div>
</div>
</div>
</div>
</section>
</div>
</details>
<div class="field-entry">
<div class="signature">
<span class="field-name">status</span>
<span class="field-type">enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The status of the environment container.</p>
<p style="margin-top: 8px; font-weight: 500; font-size: 13px; color: var(--devsite-text-secondary);">Possible
            values:</p>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">active</code>
<p style="margin-left: 16px; font-size: 13px;">Output only. The status of the environment container.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">expired</code>
<p style="margin-left: 16px; font-size: 13px;">Output only. The status of the environment container.</p> </li>
</ul>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">updated</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The time at which the environment was last updated in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).</p>
</div>
</div>
</section>
</div>
<div class="second-column">
<div class="examples">
<devsite-selector>
<section>
<h3 id="CreateEnvironment-default" data-text="Example" tabindex="-1">Example</h3>
<div class="example-content">
                                <devsite-iframe><iframe src="https://ai.google.dev/frame/api/environments_4db5aa95680895b0c2d2a38b7b70f91e1896f734439bdf141586b0dd5a233e37.frame" class="framebox inherit-locale " allow="clipboard-write https://googledevai-dot-devsite-v2-prod-3p.appspot.com" allowfullscreen is-upgraded></iframe></devsite-iframe>
                                <h4 style="margin-top: 24px; margin-bottom: 8px; font-size: 14px; font-weight: 500; color: var(--devsite-text-secondary); text-transform: uppercase;" id="example-response" data-text="                                     Example Response" tabindex="-1">
                                    Example Response</h4>
<div></div><devsite-code><pre class="devsite-click-to-copy" dir="ltr" translate="no" is-upgraded syntax="JSON"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"created"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"file_count"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"last_accessed"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"network"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"allowlist"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"domain"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"github.com"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"transform"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"Authorization"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Bearer your-token"</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"domain"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"*.googleapis.com"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"size_bytes"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"sources"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"encoding"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"source"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"target"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gcs"</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"active"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"updated"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span>
<span class="devsite-syntax-p">}</span></pre></devsite-code>
</div>
</section>
</devsite-selector>
</div>
</div>
</div>
</section>
</div>
<div class="prototype" itemscope="" itemtype="http://developers.google.com/ReferenceObject">
<h2 id="ListEnvironments" data-text="ListEnvironments" tabindex="-1">ListEnvironments</h2>
<div>
<span class="endpoint">
<span class="http-method get">
                get
            </span>
</span>
<span class="endpoint-url" style="font-size: 16px; color: var(--devsite-code-color);">
            https://generativelanguage.googleapis.com/v1beta/environments
        </span>
</div>
<section id="description">
<p>Lists environments.</p>
</section>
<section class="prototype">
<ul class="toc">
<li><a href="#ListEnvironments.PATH_PARAMETERS">Path / Query parameters</a></li> <li><a href="#ListEnvironments.response">Response</a></li>
</ul>
<div class="column-container request-section" style="margin-top: 48px;">
<div class="reference">
<section id="ListEnvironments.PATH_PARAMETERS">
<h3 id="path-query-parameters" data-text="Path / Query Parameters" tabindex="-1">Path / Query Parameters</h3>
<div class="field-entry">
<div class="signature">
<span class="field-name">page_size</span>
<span class="field-type">integer</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Optional. Maximum number of environments to return.\nIf unspecified, defaults to 50. Maximum is 1000.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">page_token</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Optional. Pagination token.</p>
</div>
</div>
</section>
<section id="ListEnvironments.response">
<h3 id="response_1" data-text="Response" tabindex="-1">Response</h3>
<p>If successful, the response body contains data with the following structure:</p>
<div class="field-entry">
<div class="signature">
<span class="field-name">environments</span>
<span class="field-type">array (<a href="#Resource:Environment">Environment</a>)</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Environments belonging to the provided project.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">next_page_token</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Pagination token.</p>
</div>
</div>
</section>
</div>
<div class="second-column">
<div class="examples">
<devsite-selector>
<section>
<h3 id="ListEnvironments-default" data-text="Example" tabindex="-1">Example</h3>
<div class="example-content">
                                <devsite-iframe><iframe src="https://ai.google.dev/frame/api/environments_f99ca789ee1cf8366fc8bedb853b49cc7ba47903992f0f2b6fa04567f7c4de34.frame" class="framebox inherit-locale " allow="clipboard-write https://googledevai-dot-devsite-v2-prod-3p.appspot.com" allowfullscreen is-upgraded></iframe></devsite-iframe>
                                <h4 style="margin-top: 24px; margin-bottom: 8px; font-size: 14px; font-weight: 500; color: var(--devsite-text-secondary); text-transform: uppercase;" id="example-response_1" data-text="                                     Example Response" tabindex="-1">
                                    Example Response</h4>
<div></div><devsite-code><pre class="devsite-click-to-copy" dir="ltr" translate="no" is-upgraded syntax="JSON"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"environments"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"created"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"file_count"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"last_accessed"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"network"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"allowlist"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"domain"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"github.com"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"transform"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nt">"Authorization"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Bearer your-token"</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"domain"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"*.googleapis.com"</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"size_bytes"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"sources"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"encoding"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"source"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"target"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gcs"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"active"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"updated"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"next_page_token"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span>
<span class="devsite-syntax-p">}</span></pre></devsite-code>
</div>
</section>
</devsite-selector>
</div>
</div>
</div>
</section>
</div>
<div class="prototype" itemscope="" itemtype="http://developers.google.com/ReferenceObject">
<h2 id="GetEnvironmentFiles" data-text="GetEnvironmentFiles" tabindex="-1">GetEnvironmentFiles</h2>
<div>
<span class="endpoint">
<span class="http-method get">
                get
            </span>
</span>
<span class="endpoint-url" style="font-size: 16px; color: var(--devsite-code-color);">
            https://generativelanguage.googleapis.com/v1beta/environments/{environment}/files/{path}
        </span>
</div>
<section id="description">
<p>Retrieves a file or directory from an environment's snapshot.</p>
</section>
<section class="prototype">
<ul class="toc">
<li><a href="#GetEnvironmentFiles.PATH_PARAMETERS">Path / Query parameters</a></li> <li><a href="#GetEnvironmentFiles.response">Response</a></li>
</ul>
<div class="column-container request-section" style="margin-top: 48px;">
<div class="reference">
<section id="GetEnvironmentFiles.PATH_PARAMETERS">
<h3 id="path-query-parameters_1" data-text="Path / Query Parameters" tabindex="-1">Path / Query Parameters</h3>
<div class="field-entry">
<div class="signature">
<span class="field-name">page_size</span>
<span class="field-type">integer</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Optional. Maximum number of entries to return per page (for directory listing).</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">page_token</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Optional. Pagination token for directory listing.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">recursive</span>
<span class="field-type">boolean</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Optional. If true and the path is a directory, recursively lists all files.</p>
</div>
</div>
</section>
<section id="GetEnvironmentFiles.response">
<h3 id="response_2" data-text="Response" tabindex="-1">Response</h3>
<p>If successful, the response body contains data with the following structure:</p>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">files</span>
<span class="field-type">array (EnvironmentFile)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>If the requested path is a directory, this contains its contents.
If the requested path is a file, this contains a single entry with the
file's metadata.
If alt=media was specified, this is empty (content is served via `blob`).</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">Metadata for a file or directory within an environment.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields_4" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">created</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The creation time of the file/directory.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">mime_type</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The MIME type of the file (e.g., "text/python", "image/png").
Empty for directories.
NOLINT</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">modified</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The modification time of the file/directory.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">name</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The name of the file or directory (e.g., "main.py" or "src").</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">path</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The full relative path within the environment
(e.g., "workspace/src/main.py").</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">size_bytes</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The size of the file/directory in bytes.
NOLINT</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">type</span>
<span class="field-type">enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The type of the entry.</p>
<p style="margin-top: 8px; font-weight: 500; font-size: 13px; color: var(--devsite-text-secondary);">Possible
            values:</p>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">file</code>
<p style="margin-left: 16px; font-size: 13px;">A regular file.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">directory</code>
<p style="margin-left: 16px; font-size: 13px;">A directory.</p> </li>
</ul>
</div>
</div>
</div>
</div>
</section>
</div>
</details>
<div class="field-entry">
<div class="signature">
<span class="field-name">next_page_token</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Pagination token for directory listing.
NOLINT</p>
</div>
</div>
</section>
</div>
<div class="second-column">
<div class="examples">
<devsite-selector>
<section>
<h3 id="GetEnvironmentFiles-default" data-text="Example" tabindex="-1">Example</h3>
<div class="example-content">
                                <devsite-iframe><iframe src="https://ai.google.dev/frame/api/environments_d255bff6cdeb0572e4256132b9f447d05aabd5fdd852cb90caaa8d15dd9df716.frame" class="framebox inherit-locale " allow="clipboard-write https://googledevai-dot-devsite-v2-prod-3p.appspot.com" allowfullscreen is-upgraded></iframe></devsite-iframe>
                                <h4 style="margin-top: 24px; margin-bottom: 8px; font-size: 14px; font-weight: 500; color: var(--devsite-text-secondary); text-transform: uppercase;" id="example-response_2" data-text="                                     Example Response" tabindex="-1">
                                    Example Response</h4>
<div></div><devsite-code><pre class="devsite-click-to-copy" dir="ltr" translate="no" is-upgraded syntax="JSON"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"files"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"created"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"mime_type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"modified"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"path"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"size_bytes"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"file"</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"next_page_token"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span>
<span class="devsite-syntax-p">}</span></pre></devsite-code>
</div>
</section>
</devsite-selector>
</div>
</div>
</div>
</section>
</div>
<div class="prototype" itemscope="" itemtype="http://developers.google.com/ReferenceObject">
<h2 id="GetEnvironment" data-text="GetEnvironment" tabindex="-1">GetEnvironment</h2>
<div>
<span class="endpoint">
<span class="http-method get">
                get
            </span>
</span>
<span class="endpoint-url" style="font-size: 16px; color: var(--devsite-code-color);">
            https://generativelanguage.googleapis.com/v1beta/environments/{id}
        </span>
</div>
<section id="description">
<p>Gets an environment.</p>
</section>
<section class="prototype">
<ul class="toc">
<li><a href="#GetEnvironment.response">Response</a></li>
</ul>
<div class="column-container request-section" style="margin-top: 48px;">
<div class="reference">
<section id="GetEnvironment.response">
<h3 id="response_3" data-text="Response" tabindex="-1">Response</h3>
<p>If successful, the response body contains data with the following structure:</p>
<div class="field-entry">
<div class="signature">
<span class="field-name">created</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The time at which the environment was created in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">file_count</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The number of files in the environment, output only.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">id</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Required. Output only. The ID of the environment.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">last_accessed</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The time at which the environment was last accessed in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).</p>
</div>
</div>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">network</span>
<span class="field-type">EnvironmentNetworkEgressAllowlist or enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>Network configuration for the environment.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">Outbound networking configuration for the sandbox. Accepts an object with an 'allowlist' array to restrict traffic, or the string 'disabled' to turn off all network access. Omit entirely to allow all outbound traffic with no header injection.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="possible-types_2" data-text="Possible Types" tabindex="-1">Possible Types</h4>
<details class="subtype-details">
<summary class="subtype-summary">
<span style="font-weight: 500;">object</span>
</summary>
<div class="subtype-content">
<p>Outbound networking configuration for the sandbox. When specified, restricts which external domains the sandbox can reach. Omit entirely to allow all outbound traffic with no header injection.</p>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">allowlist</span>
<span class="field-type">array (AllowlistEntry)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>List of allowed outbound domains. Only requests to listed domains are permitted. Use [{'domain': '*'}] to allow all domains while still injecting headers on specific ones.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">A single domain allowlist rule with optional header injection.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields_5" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">domain</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Domain to allow outbound requests to. Supports wildcards (e.g. '*.googleapis.com'). Use '*' to allow all domains.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">transform</span>
<span class="field-type">array (object) or object</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Headers to inject on all outbound requests matching this domain. Accepts a single dict or a list of dicts. The egress proxy injects these automatically.</p>
</div>
</div>
</div>
</div>
</section>
</div>
</details>
</div>
</details>
<details class="subtype-details">
<summary class="subtype-summary">
<span style="font-weight: 500;">string</span>
</summary>
<div class="subtype-content">
<p>Turns all network off.</p>
</div>
</details>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="possible-values_2" data-text="Possible values" tabindex="-1">Possible values</h4>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">disabled</code>
<p style="margin-left: 16px; font-size: 13px; color: var(--devsite-text-secondary);">Turns all network off.</p> </li>
</ul>
</div>
</div>
</section>
</div>
</details>
<div class="field-entry">
<div class="signature">
<span class="field-name">size_bytes</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The total size of the environment files in bytes, output only.</p>
</div>
</div>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">sources</span>
<span class="field-type">array (Source)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>Sources to be mounted into the environment.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">A source to be mounted into the environment.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields_6" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">content</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>The inline content if `type` is `INLINE`.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">encoding</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Optional encoding for inline content (e.g. `base64`).</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">source</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>The source of the environment.
For Cloud Storage, this is the Cloud Storage path.
For GitHub, this is the GitHub path.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">target</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Where the source should appear in the environment.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">type</span>
<span class="field-type">enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>No description provided.</p>
<p style="margin-top: 8px; font-weight: 500; font-size: 13px; color: var(--devsite-text-secondary);">Possible
            values:</p>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">gcs</code>
<p style="margin-left: 16px; font-size: 13px;">A Cloud Storage bucket.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">inline</code>
<p style="margin-left: 16px; font-size: 13px;">Inline content.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">repository</code>
<p style="margin-left: 16px; font-size: 13px;">A generic repository. The protocol prefix in the source URL
identifies the provider (e.g., github://, gcs://).</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">skill_registry</code>
<p style="margin-left: 16px; font-size: 13px;">A skill resource from the Skill Registry Service.
Skill: projects/{project}/locations/{location}/skills/{skill}
SkillRevision:
projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}
Support mounting all skills under a project:
projects/{project}/locations/{location}/skills.</p> </li>
</ul>
</div>
</div>
</div>
</div>
</section>
</div>
</details>
<div class="field-entry">
<div class="signature">
<span class="field-name">status</span>
<span class="field-type">enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The status of the environment container.</p>
<p style="margin-top: 8px; font-weight: 500; font-size: 13px; color: var(--devsite-text-secondary);">Possible
            values:</p>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">active</code>
<p style="margin-left: 16px; font-size: 13px;">Output only. The status of the environment container.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">expired</code>
<p style="margin-left: 16px; font-size: 13px;">Output only. The status of the environment container.</p> </li>
</ul>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">updated</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The time at which the environment was last updated in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).</p>
</div>
</div>
</section>
</div>
<div class="second-column">
<div class="examples">
<devsite-selector>
<section>
<h3 id="GetEnvironment-default" data-text="Example" tabindex="-1">Example</h3>
<div class="example-content">
                                <devsite-iframe><iframe src="https://ai.google.dev/frame/api/environments_4dd66d0b956fefd22cef277e4f527f086b0fdebc56af7f366f7682686c962ef1.frame" class="framebox inherit-locale " allow="clipboard-write https://googledevai-dot-devsite-v2-prod-3p.appspot.com" allowfullscreen is-upgraded></iframe></devsite-iframe>
                                <h4 style="margin-top: 24px; margin-bottom: 8px; font-size: 14px; font-weight: 500; color: var(--devsite-text-secondary); text-transform: uppercase;" id="example-response_3" data-text="                                     Example Response" tabindex="-1">
                                    Example Response</h4>
<div></div><devsite-code><pre class="devsite-click-to-copy" dir="ltr" translate="no" is-upgraded syntax="JSON"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"created"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"file_count"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"last_accessed"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"network"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nt">"allowlist"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"domain"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"github.com"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"transform"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nt">"Authorization"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Bearer your-token"</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"domain"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"*.googleapis.com"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"size_bytes"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"sources"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"encoding"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"source"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"target"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gcs"</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"status"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"active"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"updated"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span>
<span class="devsite-syntax-p">}</span></pre></devsite-code>
</div>
</section>
</devsite-selector>
</div>
</div>
</div>
</section>
</div>
<div class="prototype" itemscope="" itemtype="http://developers.google.com/ReferenceObject">
<h2 id="DeleteEnvironment" data-text="DeleteEnvironment" tabindex="-1">DeleteEnvironment</h2>
<div>
<span class="endpoint">
<span class="http-method delete">
                delete
            </span>
</span>
<span class="endpoint-url" style="font-size: 16px; color: var(--devsite-code-color);">
            https://generativelanguage.googleapis.com/v1beta/environments/{id}
        </span>
</div>
<section id="description">
<p>Deletes an environment.</p>
</section>
<section class="prototype">
<ul class="toc">
<li><a href="#DeleteEnvironment.response">Response</a></li>
</ul>
<div class="column-container request-section" style="margin-top: 48px;">
<div class="reference">
<section id="DeleteEnvironment.response">
<h3 id="response_4" data-text="Response" tabindex="-1">Response</h3>
<p>If successful, the response is empty.</p>
</section>
</div>
<div class="second-column">
<div class="examples">
<devsite-selector>
<section>
<h3 id="DeleteEnvironment-default" data-text="Example" tabindex="-1">Example</h3>
<div class="example-content">
                                <devsite-iframe><iframe src="https://ai.google.dev/frame/api/environments_8066560a4d8fa671d2db58f8803356422b6b9d9d69a521d7990c1d963958ce10.frame" class="framebox inherit-locale " allow="clipboard-write https://googledevai-dot-devsite-v2-prod-3p.appspot.com" allowfullscreen is-upgraded></iframe></devsite-iframe>
                            </div>
</section>
</devsite-selector>
</div>
</div>
</div>
</section>
</div>
<h2 id="resources" style="margin-top: 64px;" data-text="Resources" tabindex="-1">Resources</h2>
<div itemscope="" itemtype="http://developers.google.com/ReferenceObject">
<h3 id="Resource:Environment" data-text="Environment" tabindex="-1">Environment</h3>
<section class="prototype">
<div class="column-container">
<div class="reference">
<p>An execution environment for an agent.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields_7" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">created</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The time at which the environment was created in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">file_count</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The number of files in the environment, output only.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">id</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Required. Output only. The ID of the environment.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">last_accessed</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The time at which the environment was last accessed in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).</p>
</div>
</div>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">network</span>
<span class="field-type">EnvironmentNetworkEgressAllowlist or enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>Network configuration for the environment.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">Outbound networking configuration for the sandbox. Accepts an object with an 'allowlist' array to restrict traffic, or the string 'disabled' to turn off all network access. Omit entirely to allow all outbound traffic with no header injection.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="possible-types_3" data-text="Possible Types" tabindex="-1">Possible Types</h4>
<details class="subtype-details">
<summary class="subtype-summary">
<span style="font-weight: 500;">object</span>
</summary>
<div class="subtype-content">
<p>Outbound networking configuration for the sandbox. When specified, restricts which external domains the sandbox can reach. Omit entirely to allow all outbound traffic with no header injection.</p>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">allowlist</span>
<span class="field-type">array (AllowlistEntry)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>List of allowed outbound domains. Only requests to listed domains are permitted. Use [{'domain': '*'}] to allow all domains while still injecting headers on specific ones.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">A single domain allowlist rule with optional header injection.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields_8" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">domain</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Domain to allow outbound requests to. Supports wildcards (e.g. '*.googleapis.com'). Use '*' to allow all domains.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">transform</span>
<span class="field-type">array (object) or object</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Headers to inject on all outbound requests matching this domain. Accepts a single dict or a list of dicts. The egress proxy injects these automatically.</p>
</div>
</div>
</div>
</div>
</section>
</div>
</details>
</div>
</details>
<details class="subtype-details">
<summary class="subtype-summary">
<span style="font-weight: 500;">string</span>
</summary>
<div class="subtype-content">
<p>Turns all network off.</p>
</div>
</details>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="possible-values_3" data-text="Possible values" tabindex="-1">Possible values</h4>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">disabled</code>
<p style="margin-left: 16px; font-size: 13px; color: var(--devsite-text-secondary);">Turns all network off.</p> </li>
</ul>
</div>
</div>
</section>
</div>
</details>
<div class="field-entry">
<div class="signature">
<span class="field-name">size_bytes</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The total size of the environment files in bytes, output only.</p>
</div>
</div>
<details class="field-entry inline-details">
<summary class="signature">
<span class="expander-icon"></span>
<span class="field-name">sources</span>
<span class="field-type">array (Source)</span>
<span class="field-nessesity optional"> (optional)</span> </summary>
<div class="field-description">
<p>Sources to be mounted into the environment.</p>
<section class="prototype" style="padding-left: 16px;">
<div class="column-container">
<div class="reference">
<p style="display: none;">A source to be mounted into the environment.</p>
<h4 style="margin-top: 16px; margin-bottom: 8px; font-size: 14px; font-weight: 500;" id="fields_9" data-text="Fields" tabindex="-1">Fields</h4>
<div class="field-entry">
<div class="signature">
<span class="field-name">content</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>The inline content if `type` is `INLINE`.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">encoding</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Optional encoding for inline content (e.g. `base64`).</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">source</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>The source of the environment.
For Cloud Storage, this is the Cloud Storage path.
For GitHub, this is the GitHub path.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">target</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Where the source should appear in the environment.</p>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">type</span>
<span class="field-type">enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>No description provided.</p>
<p style="margin-top: 8px; font-weight: 500; font-size: 13px; color: var(--devsite-text-secondary);">Possible
            values:</p>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">gcs</code>
<p style="margin-left: 16px; font-size: 13px;">A Cloud Storage bucket.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">inline</code>
<p style="margin-left: 16px; font-size: 13px;">Inline content.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">repository</code>
<p style="margin-left: 16px; font-size: 13px;">A generic repository. The protocol prefix in the source URL
identifies the provider (e.g., github://, gcs://).</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">skill_registry</code>
<p style="margin-left: 16px; font-size: 13px;">A skill resource from the Skill Registry Service.
Skill: projects/{project}/locations/{location}/skills/{skill}
SkillRevision:
projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}
Support mounting all skills under a project:
projects/{project}/locations/{location}/skills.</p> </li>
</ul>
</div>
</div>
</div>
</div>
</section>
</div>
</details>
<div class="field-entry">
<div class="signature">
<span class="field-name">status</span>
<span class="field-type">enum (string)</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The status of the environment container.</p>
<p style="margin-top: 8px; font-weight: 500; font-size: 13px; color: var(--devsite-text-secondary);">Possible
            values:</p>
<ul style="margin: 4px 0 0 0; padding-left: 20px; list-style-type: disc;">
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">active</code>
<p style="margin-left: 16px; font-size: 13px;">Output only. The status of the environment container.</p> </li>
<li style="margin-bottom: 4px;">
<code style="font-size: 13px;" translate="no" dir="ltr">expired</code>
<p style="margin-left: 16px; font-size: 13px;">Output only. The status of the environment container.</p> </li>
</ul>
</div>
</div>
<div class="field-entry">
<div class="signature">
<span class="field-name">updated</span>
<span class="field-type">string</span>
<span class="field-nessesity optional"> (optional)</span> </div>
<div class="field-description">
<p>Output only. The time at which the environment was last updated in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).</p>
</div>
</div>
</div>
<div class="second-column">
</div>
</div>
</section>
</div>
  

  
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