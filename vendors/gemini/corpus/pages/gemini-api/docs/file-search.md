








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/file-search"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/file-search" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/file-search" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/file-search?hl=sq" /><title>File search &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="File search &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta name="description" content="Get started building RAG solutions with the File Search tool in the Gemini API">
  <meta property="og:description" content="Get started building RAG solutions with the File Search tool in the Gemini API"><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/file-search"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
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
      File search<devsite-actions hidden data-nosnippet>
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



<p>The Gemini API enables Retrieval Augmented Generation (&quot;RAG&quot;) through the File
Search tool. File Search imports, chunks, and indexes your data to
enable fast retrieval of relevant information based on a provided prompt. This
retrieved information is then used as context for the model, allowing it to
provide more accurate and relevant answers. File search is also able to
provide multimodal capabilities with text embeddings supported by
<code translate="no" dir="ltr">gemini-embedding-001</code>, and image/multimodal embedding supported by <code translate="no" dir="ltr">gemini-embedding-2</code>.</p>
<aside class="note"><strong>Note:</strong><span> Audio and video formats are not currently supported.</span></aside>
<p>File storage and embedding generation at query time is free, and you&#39;ll only pay
for creating embeddings when you first index your files and the normal Gemini
model input / output tokens cost. This new billing paradigm makes the File
Search Tool both easier and more cost-effective to build and scale with. See
<a href="#pricing">pricing</a> section for details.</p>

<h2 id="upload" data-text="Directly upload to File Search store" tabindex="-1">Directly upload to File Search store</h2>

<p>This example shows how to directly upload a file to the
<a href="/api/file-search/file-search-stores#method:-media.uploadtofilesearchstore">file search store</a>:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">time</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">file_search_store</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s1">'display_name'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'your-fileSearchStore-name'</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s1">'embedding_model'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'models/gemini-embedding-2'</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">operation</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">upload_to_file_search_store</span><span class="devsite-syntax-p">(</span>
  <span class="devsite-syntax-n">file</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'sample.txt'</span><span class="devsite-syntax-p">,</span>
  <span class="devsite-syntax-n">file_search_store_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span>
  <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
      <span class="devsite-syntax-s1">'display_name'</span> <span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'display-file-name'</span><span class="devsite-syntax-p">,</span>
  <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">while</span> <span class="devsite-syntax-ow">not</span> <span class="devsite-syntax-n">operation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">done</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">time</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">sleep</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">5</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-n">operation</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">operations</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">operation</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Can you tell me about [insert question]"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"file_search_store_names"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">]</span>
    <span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">content_block</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
                <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                    <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-se">\n</span><span class="devsite-syntax-s2">Sources:"</span><span class="devsite-syntax-p">)</span>
                    <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">annotation</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                        <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"file_citation"</span><span class="devsite-syntax-p">:</span>
                            <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"  - </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">source</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">run</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">displayName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'your-fileSearchStore-name'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">embeddingModel</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'models/gemini-embedding-2'</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uploadToFileSearchStore</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">file</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'file.txt'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">fileSearchStoreName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">displayName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'file-name'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">while</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Promise</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setTimeout</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">5000</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">operations</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">get</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Can you tell me about [insert question]"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">file_search_store_names</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'model_output'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"\nSources:"</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'file_citation'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`  - </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">file_name</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">source</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">run</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
<section><h3 id="java" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># 1. Create a File Search store</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">      "displayName": "your-file-search-store-name",</span>
<span class="devsite-syntax-s1">      "embeddingModel": "models/gemini-embedding-2"</span>
<span class="devsite-syntax-s1">    }'</span><span class="devsite-syntax-w"> &gt; </span>store_res.json

<span class="devsite-syntax-nv">FILE_SEARCH_STORE_NAME</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>jq<span class="devsite-syntax-w"> </span>-r<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">".name"</span><span class="devsite-syntax-w"> </span>store_res.json<span class="devsite-syntax-k">)</span>

<span class="devsite-syntax-c1"># 2. Upload directly to File Search store using resumable upload</span>
<span class="devsite-syntax-nv">NUM_BYTES</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>wc<span class="devsite-syntax-w"> </span>-c<span class="devsite-syntax-w"> &lt; </span><span class="devsite-syntax-s2">"sample.txt"</span><span class="devsite-syntax-k">)</span>
curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/upload/v1beta/fileSearchStores/</span><span class="devsite-syntax-nv">$FILE_SEARCH_STORE_NAME</span><span class="devsite-syntax-s2">:uploadToFileSearchStore?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-D<span class="devsite-syntax-w"> </span>upload-header.tmp<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Protocol: resumable"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Command: start"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Header-Content-Length: </span><span class="devsite-syntax-nv">$NUM_BYTES</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Header-Content-Type: text/plain"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{"displayName": "sample.txt"}'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null

<span class="devsite-syntax-nv">upload_url</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>grep<span class="devsite-syntax-w"> </span>-i<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-upload-url: "</span><span class="devsite-syntax-w"> </span>upload-header.tmp<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>cut<span class="devsite-syntax-w"> </span>-d<span class="devsite-syntax-s2">" "</span><span class="devsite-syntax-w"> </span>-f2<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>tr<span class="devsite-syntax-w"> </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"\r"</span><span class="devsite-syntax-k">)</span>
rm<span class="devsite-syntax-w"> </span>upload-header.tmp

curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">upload_url</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Length: </span><span class="devsite-syntax-nv">$NUM_BYTES</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Offset: 0"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Command: upload, finalize"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--data-binary<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@sample.txt"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null<span class="devsite-syntax-w"> &gt; </span>upload_response.json

cat<span class="devsite-syntax-w"> </span>upload_response.json

<span class="devsite-syntax-c1"># 3. Query using the File Search store</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">      "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">      "input": "Can you tell me about [insert question]",</span>
<span class="devsite-syntax-s1">      "tools": [{</span>
<span class="devsite-syntax-s1">        "type": "file_search",</span>
<span class="devsite-syntax-s1">        "file_search_store_names": ["'</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-nv">$FILE_SEARCH_STORE_NAME</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-s1">'"]</span>
<span class="devsite-syntax-s1">      }]</span>
<span class="devsite-syntax-s1">    }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>Check the API reference for <a href="/api/file-search/file-search-stores#method:-media.uploadtofilesearchstore"><code translate="no" dir="ltr">uploadToFileSearchStore</code></a> for more information.</p>

<h2 id="importing-files" data-text="Importing files" tabindex="-1">Importing files</h2>

<p>Alternatively, you can upload an existing file and <a href="/api/file-search/file-search-stores#method:-filesearchstores.importfile">import it to your file search store</a>:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">time</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">sample_file</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">files</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">upload</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">file</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'sample.txt'</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s1">'display_name'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'display_file_name'</span><span class="devsite-syntax-p">})</span>

<span class="devsite-syntax-n">file_search_store</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s1">'display_name'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'your-fileSearchStore-name'</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s1">'embedding_model'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'models/gemini-embedding-2'</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">operation</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">import_file</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">file_search_store_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">file_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">sample_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">while</span> <span class="devsite-syntax-ow">not</span> <span class="devsite-syntax-n">operation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">done</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">time</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">sleep</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">5</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-n">operation</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">operations</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">operation</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Can you tell me about [insert question]"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"file_search_store_names"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">]</span>
    <span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">content_block</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">run</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">sampleFile</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">files</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">upload</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">file</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'sample.txt'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">displayName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'file-name'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">displayName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'your-fileSearchStore-name'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">embeddingModel</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'models/gemini-embedding-2'</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">importFile</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">fileSearchStoreName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">fileName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">sampleFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">while</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Promise</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setTimeout</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">5000</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">operations</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">get</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Can you tell me about [insert question]"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">file_search_store_names</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'model_output'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">run</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
<section><h3 id="java_1" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_1" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># 1. Upload file using the Files API</span>
<span class="devsite-syntax-nv">NUM_BYTES</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>wc<span class="devsite-syntax-w"> </span>-c<span class="devsite-syntax-w"> &lt; </span><span class="devsite-syntax-s2">"sample.txt"</span><span class="devsite-syntax-k">)</span>
curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/upload/v1beta/files?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-D<span class="devsite-syntax-w"> </span>upload-header.tmp<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Protocol: resumable"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Command: start"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Header-Content-Length: </span><span class="devsite-syntax-nv">$NUM_BYTES</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Header-Content-Type: text/plain"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{"file": {"displayName": "sample.txt"}}'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null

<span class="devsite-syntax-nv">upload_url</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>grep<span class="devsite-syntax-w"> </span>-i<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-upload-url: "</span><span class="devsite-syntax-w"> </span>upload-header.tmp<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>cut<span class="devsite-syntax-w"> </span>-d<span class="devsite-syntax-s2">" "</span><span class="devsite-syntax-w"> </span>-f2<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>tr<span class="devsite-syntax-w"> </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"\r"</span><span class="devsite-syntax-k">)</span>
rm<span class="devsite-syntax-w"> </span>upload-header.tmp

curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">upload_url</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Length: </span><span class="devsite-syntax-nv">$NUM_BYTES</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Offset: 0"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Command: upload, finalize"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--data-binary<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@sample.txt"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null<span class="devsite-syntax-w"> &gt; </span>file_info.json

<span class="devsite-syntax-nv">FILE_NAME</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>jq<span class="devsite-syntax-w"> </span>-r<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">".file.name"</span><span class="devsite-syntax-w"> </span>file_info.json<span class="devsite-syntax-k">)</span>

<span class="devsite-syntax-c1"># 2. Create a File Search store</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">      "displayName": "your-file-search-store-name",</span>
<span class="devsite-syntax-s1">      "embeddingModel": "models/gemini-embedding-2"</span>
<span class="devsite-syntax-s1">    }'</span><span class="devsite-syntax-w"> &gt; </span>store_res.json

<span class="devsite-syntax-nv">FILE_SEARCH_STORE_NAME</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>jq<span class="devsite-syntax-w"> </span>-r<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">".name"</span><span class="devsite-syntax-w"> </span>store_res.json<span class="devsite-syntax-k">)</span>

<span class="devsite-syntax-c1"># 3. Import the file into the File Search store</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores/</span><span class="devsite-syntax-nv">$FILE_SEARCH_STORE_NAME</span><span class="devsite-syntax-s2">:importFile?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{"fileName": "'</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-nv">$FILE_NAME</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-s1">'"}'</span>

<span class="devsite-syntax-c1"># 4. Query using the File Search store</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">      "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">      "input": "Can you tell me about [insert question]",</span>
<span class="devsite-syntax-s1">      "tools": [{</span>
<span class="devsite-syntax-s1">        "type": "file_search",</span>
<span class="devsite-syntax-s1">        "file_search_store_names": ["'</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-nv">$FILE_SEARCH_STORE_NAME</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-s1">'"]</span>
<span class="devsite-syntax-s1">      }]</span>
<span class="devsite-syntax-s1">    }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>Check the API reference for <a href="/api/file-search/file-search-stores#method:-filesearchstores.importfile"><code translate="no" dir="ltr">importFile</code></a> for more information.</p>

<h2 id="chunking_configuration" data-text="Chunking configuration" tabindex="-1">Chunking configuration</h2>

<p>When you import a file into a File Search store, it&#39;s automatically broken down
into chunks, embedded, indexed, and uploaded to your File Search store. If you
need more control over the chunking strategy, you can specify a
<a href="/api/file-search/file-search-stores#request-body_5"><code translate="no" dir="ltr">chunking_config</code></a> setting
to set a maximum number of tokens per chunk and maximum number of overlapping
tokens.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">time</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">operation</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">upload_to_file_search_store</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">file_search_store_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">file</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'sample.txt'</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s1">'chunking_config'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
          <span class="devsite-syntax-s1">'white_space_config'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">{</span>
            <span class="devsite-syntax-s1">'max_tokens_per_chunk'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-mi">200</span><span class="devsite-syntax-p">,</span>
            <span class="devsite-syntax-s1">'max_overlap_tokens'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-mi">20</span>
          <span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">while</span> <span class="devsite-syntax-ow">not</span> <span class="devsite-syntax-n">operation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">done</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-n">time</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">sleep</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">5</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-n">operation</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">operations</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">operation</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Custom chunking complete."</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uploadToFileSearchStore</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">file</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'file.txt'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">fileSearchStoreName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">displayName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'file-name'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">chunkingConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">whiteSpaceConfig</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">maxTokensPerChunk</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">200</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">maxOverlapTokens</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">20</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">while</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-o">!</span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">done</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">Promise</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">setTimeout</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">resolve</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">5000</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">operations</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">get</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"Custom chunking complete."</span><span class="devsite-syntax-p">);</span>
</code></pre></devsite-code></section>
<section><h3 id="java_2" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_2" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-nv">NUM_BYTES</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>wc<span class="devsite-syntax-w"> </span>-c<span class="devsite-syntax-w"> &lt; </span><span class="devsite-syntax-s2">"sample.txt"</span><span class="devsite-syntax-k">)</span>
curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/upload/v1beta/fileSearchStores/</span><span class="devsite-syntax-nv">$FILE_SEARCH_STORE_NAME</span><span class="devsite-syntax-s2">:uploadToFileSearchStore?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-D<span class="devsite-syntax-w"> </span>upload-header.tmp<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Protocol: resumable"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Command: start"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Header-Content-Length: </span><span class="devsite-syntax-nv">$NUM_BYTES</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Header-Content-Type: text/plain"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">      "displayName": "sample.txt",</span>
<span class="devsite-syntax-s1">      "chunkingConfig": {</span>
<span class="devsite-syntax-s1">        "whiteSpaceConfig": {</span>
<span class="devsite-syntax-s1">          "maxTokensPerChunk": 200,</span>
<span class="devsite-syntax-s1">          "maxOverlapTokens": 20</span>
<span class="devsite-syntax-s1">        }</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null

<span class="devsite-syntax-nv">upload_url</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>grep<span class="devsite-syntax-w"> </span>-i<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-upload-url: "</span><span class="devsite-syntax-w"> </span>upload-header.tmp<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>cut<span class="devsite-syntax-w"> </span>-d<span class="devsite-syntax-s2">" "</span><span class="devsite-syntax-w"> </span>-f2<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>tr<span class="devsite-syntax-w"> </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"\r"</span><span class="devsite-syntax-k">)</span>
rm<span class="devsite-syntax-w"> </span>upload-header.tmp

curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">upload_url</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Length: </span><span class="devsite-syntax-nv">$NUM_BYTES</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Offset: 0"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Command: upload, finalize"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>--data-binary<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@sample.txt"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null<span class="devsite-syntax-w"> &gt; </span>upload_response.json

cat<span class="devsite-syntax-w"> </span>upload_response.json
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>To use your File Search store, pass it as a tool to the <code translate="no" dir="ltr">interactions.create</code>
method, as shown in the <a href="#upload">Upload</a> and <a href="#importing-files">Import</a> examples.</p>

<h2 id="how-it-works" data-text="How it works" tabindex="-1">How it works</h2>

<p>File Search uses a technique called semantic search to find information relevant
to the user prompt. Unlike standard keyword-based search, semantic search
understands the meaning and context of your query.</p>

<p>When you import a file, it&#39;s converted into numerical representations called
<a href="/gemini-api/docs/embeddings">embeddings</a>, which capture the semantic meaning of
the uploaded content. These embeddings are stored in a specialized File Search database.
When you make a query, it&#39;s also converted into an embedding. Then the system
performs a File Search to find the most similar and relevant document chunks
from the File Search store.</p>

<p>There is no Time To Live (TTL) for embeddings;
they persist until manually deleted, or when the model is deprecated. Files,
however, are deleted after 48 hours.</p>

<p>Here&#39;s a breakdown of the process for using the File Search
<code translate="no" dir="ltr">uploadToFileSearchStore</code> API:</p>

<ol>
<li><p><strong>Create a File Search store</strong>: A File Search store contains the processed
data from your files. It&#39;s the persistent container for the embeddings that the
semantic search will operate on.</p></li>
<li><p><strong>Upload a file and import into a File Search store</strong>: Simultaneously upload
a file and import the results into your File Search store. This creates a
temporary <code translate="no" dir="ltr">File</code> object, which is a reference to your raw document. That data is
then chunked, converted into File Search embeddings, and indexed. The <code translate="no" dir="ltr">File</code>
object gets deleted after 48 hours, while the data imported into the File Search
store will be stored indefinitely until you choose to delete it.</p></li>
<li><p><strong>Query with File Search</strong>: Finally, you use the <code translate="no" dir="ltr">FileSearch</code> tool in a
<code translate="no" dir="ltr">generateContent</code> call. In the tool configuration, you specify a
<code translate="no" dir="ltr">FileSearchRetrievalResource</code>, which points to the <code translate="no" dir="ltr">FileSearchStore</code> you want to
search. This tells the model to perform a semantic search on that specific
File Search store to find relevant information to ground its response.</p></li>
</ol>

<figure>
  <img src="/static/gemini-api/docs/images/File-search.png" alt="The indexing and querying process of File Search" class="screenshot">
  <figcaption>The indexing and querying process of File Search</figcaption>
</figure>

<p>In this diagram, the dotted line from <em>Documents</em> to <em>Embedding model</em>
(using <a href="/gemini-api/docs/embeddings"><code translate="no" dir="ltr">gemini-embedding-001</code></a>)
represents the <code translate="no" dir="ltr">uploadToFileSearchStore</code> API (bypassing <em>File storage</em>).
Otherwise, using the <a href="/gemini-api/docs/files">Files API</a> to separately create
and then import files moves the indexing process from <em>Documents</em> to
<em>File storage</em> and then to <em>Embedding model</em>.</p>

<h2 id="file-search-stores" data-text="File Search stores" tabindex="-1">File Search stores</h2>

<p>A File Search store is a container for your document embeddings. While raw files
uploaded through the File API are deleted after 48 hours, the data imported into
a File Search store is stored indefinitely until you manually delete it. You can
create multiple File Search stores to organize your documents. The
<code translate="no" dir="ltr">FileSearchStore</code> API lets you create, list, get, and delete to manage your file
search stores. File Search store names are globally scoped.</p>

<p>Here are some examples of how to manage your File Search stores:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_3" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">file_search_store</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s1">'display_name'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'myfilesearchstore123'</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s1">'embedding_model'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'models/gemini-embedding-2'</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">store</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">list</span><span class="devsite-syntax-p">():</span>
    <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">store</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">my_file_search_store</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delete</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s1">'force'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">})</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_3" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">displayName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'myfilesearchstore123'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">embeddingModel</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'models/gemini-embedding-2'</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">list</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">store</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">store</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">myFileSearchStore</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">get</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-ow">delete</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">force</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="java_3" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_3" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">GEMINI_API_KEY</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'</span>

curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">GEMINI_API_KEY</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>

curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">GEMINI_API_KEY</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>

curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>DELETE<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">GEMINI_API_KEY</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="file-search-documents" data-text="File Search documents" tabindex="-1">File Search documents</h2>

<p>You can manage individual documents in your file stores with the
<a href="/api/file-search/documents">File Search Documents</a> API to <code translate="no" dir="ltr">list</code> each document
in a file search store, <code translate="no" dir="ltr">get</code> information about a document, and <code translate="no" dir="ltr">delete</code> a
document by name.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_4" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">document_in_store</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">documents</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">list</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">parent</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'fileSearchStores/myfilesearchstore123'</span><span class="devsite-syntax-p">):</span>
  <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">document_in_store</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">file_search_document</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">documents</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'fileSearchStores/myfilesearchstore123/documents/sampletxt123'</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">file_search_document</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">documents</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">delete</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'fileSearchStores/myfilesearchstore123/documents/sampletxt123'</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s1">'force'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-kc">True</span><span class="devsite-syntax-p">})</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_4" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">documents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">documents</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">list</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">parent</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'fileSearchStores/myfilesearchstore123'</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">doc</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">documents</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">doc</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchDocument</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">documents</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">get</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'fileSearchStores/myfilesearchstore123/documents/sampletxt123'</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">documents</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-ow">delete</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'fileSearchStores/myfilesearchstore123/documents/sampletxt123'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">force</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="java_4" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_4" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents?key=</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">GEMINI_API_KEY</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>

curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">GEMINI_API_KEY</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>

curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>DELETE<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">GEMINI_API_KEY</span><span class="devsite-syntax-si">}</span>&amp;<span class="devsite-syntax-s2">force=true"</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="metadata" data-text="File metadata" tabindex="-1">File metadata</h2>

<p>You can add custom metadata to your files to help filter them or provide
additional context. Metadata is a set of key-value pairs.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_5" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">op</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">import_file</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">file_search_store_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">file_name</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">sample_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s1">'custom_metadata'</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span>
            <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"key"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"author"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"string_value"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Robert Graves"</span><span class="devsite-syntax-p">},</span>
            <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"key"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"year"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"numeric_value"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-mi">1934</span><span class="devsite-syntax-p">}</span>
        <span class="devsite-syntax-p">]</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_5" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">let</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">operation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">importFile</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">fileSearchStoreName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">fileName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">sampleFile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">customMetadata</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">key</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"author"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">stringValue</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Robert Graves"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">key</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"year"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">numericValue</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">1934</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="java_5" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>This is useful when you have multiple documents in a File Search store and want
to search only a subset of them.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_6" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Tell me about the book 'I, Claudius'"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"file_search_store_names"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">],</span>
        <span class="devsite-syntax-s2">"metadata_filter"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s1">'author="Robert Graves"'</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">content_block</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_6" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Tell me about the book 'I, Claudius'"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">file_search_store_names</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">metadata_filter</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'author="Robert Graves"'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'model_output'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_6" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_5" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Content-Type: application/json'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">            "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],</span>
<span class="devsite-syntax-s1">            "tools": [{</span>
<span class="devsite-syntax-s1">                "type": "file_search",</span>
<span class="devsite-syntax-s1">                "file_search_store_names": ["'</span><span class="devsite-syntax-nv">$STORE_NAME</span><span class="devsite-syntax-s1">'"],</span>
<span class="devsite-syntax-s1">                "metadata_filter": "author = \"Robert Graves\""</span>
<span class="devsite-syntax-s1">            }]</span>
<span class="devsite-syntax-s1">        }'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null<span class="devsite-syntax-w"> &gt; </span>response.json

cat<span class="devsite-syntax-w"> </span>response.json
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>Guidance on implementing list filter syntax for <code translate="no" dir="ltr">metadata_filter</code> can be found
at <a href="https://google.aip.dev/160">google.aip.dev/160</a></p>

<h2 id="multimodal-file-search" data-text="Multimodal File Search" tabindex="-1">Multimodal File Search</h2>

<p>Multimodal File Search lets you to natively embed and search through images,
enabling rich, multimodal RAG applications.</p>

<h3 id="configure_the_embedding_model" data-text="Configure the embedding model" tabindex="-1">Configure the embedding model</h3>

<p>When you create a <code translate="no" dir="ltr">FileSearchStore</code>, you must override the default text-only
embedding model to use a multimodal model. Use <code translate="no" dir="ltr">models/gemini-embedding-2</code> to
process both text and images.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_7" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">store</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"display_name"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"Multimodal Catalog"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"embedding_model"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"models/gemini-embedding-2"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_7" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">displayName</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Multimodal Catalog"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">embeddingModel</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"models/gemini-embedding-2"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="java_7" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_6" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=</span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">      "display_name": "Multimodal Catalog",</span>
<span class="devsite-syntax-s1">      "embedding_model": "models/gemini-embedding-2"</span>
<span class="devsite-syntax-s1">    }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="upload-images" data-text="Upload images" tabindex="-1">Upload images</h3>

<p>After you create the store with a multimodal embedding model, you can upload
image files directly using the same upload APIs described in
<a href="#upload">Directly upload to File Search store</a> or <a href="#importing-files">Importing files</a>.</p>

<p><strong>Image file requirements:</strong></p>

<ul>
<li>Image files must be at most 4K x 4K pixels in resolution.</li>
<li>Supported formats are PNG, JPEG.</li>
</ul>

<h2 id="citations" data-text="Citations" tabindex="-1">Citations</h2>

<p>When you use File Search, the model&#39;s response may include citations that
specify which parts of your uploaded documents were used to generate the
answer. This helps with fact-checking and verification.</p>

<p>You can access citation information through the <code translate="no" dir="ltr">annotations</code> attribute inside the <code translate="no" dir="ltr">model_output</code> step&#39;s <code translate="no" dir="ltr">content</code> blocks of the response.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_8" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s1">'model_output'</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">content</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s1">'text'</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_8" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'model_output'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">stringify</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">null</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">2</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_8" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_7" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"annotations"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"file_citation"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"file_name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"sample.txt"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"source"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p>For detailed information on the structure of the citations, see the
<a href="/api/interactions-api#Resource:FileCitation">API reference for Interactions</a>.</p>

<h3 id="page-numbers" data-text="Page numbers" tabindex="-1">Page numbers</h3>

<p>When you use File Search with documents that have pages (such as PDFs), the
model&#39;s response may include the page number where the information was found.
You can access this information through the <code translate="no" dir="ltr">page_number</code> attribute of a
<code translate="no" dir="ltr">file_citation</code> annotation.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_9" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">content</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">annotation</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"file_citation"</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">page_number</span><span class="devsite-syntax-p">:</span>
                        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Cited Page: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">page_number</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_9" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'model_output'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">block</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">block</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">block</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">block</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'file_citation'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">pageNumber</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Cited Page: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">pageNumber</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_9" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_8" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"annotations"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"file_citation"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"file_name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"document.pdf"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"page_number"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">1</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"source"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="media-citations" data-text="Media citations" tabindex="-1">Media citations</h3>

<p>When the model references an image chunk during generation, the API returns an
annotation of type <code translate="no" dir="ltr">file_citation</code> in the annotations that includes a <code translate="no" dir="ltr">media_id</code>. You can use this
ID to download the exact image chunk the model referenced. This <code translate="no" dir="ltr">media_id</code> is
persistent across multiple search calls, which lets you reliably retrieve
the same image or cache it using the ID.</p>

<p>The following snippet is an example REST response step:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"annotations"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"file_citation"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"file_name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"product_image"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"media_id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"fileSearchStores/my-store-123/media/BlobId-456"</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p>The following code snippets demonstrate how to retrieve the <code translate="no" dir="ltr">media_id</code> and
download the media:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_10" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">content</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"text"</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">annotation</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">content</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"file_citation"</span> <span class="devsite-syntax-ow">and</span> <span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">media_id</span><span class="devsite-syntax-p">:</span>
                        <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sa">f</span><span class="devsite-syntax-s2">"Cited Media ID: </span><span class="devsite-syntax-si">{</span><span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">media_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-p">)</span>
                        <span class="devsite-syntax-n">blob_content</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">file_search_stores</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">download_media</span><span class="devsite-syntax-p">(</span>
                            <span class="devsite-syntax-n">media_id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">media_id</span>
                        <span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_10" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'model_output'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">block</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">block</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">block</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">block</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'file_citation'</span><span class="devsite-syntax-w"> &amp;&amp; </span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mediaId</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-sb">`Cited Media ID: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mediaId</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-sb">`</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">blobContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fileSearchStores</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">downloadMedia</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mediaId</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_10" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_9" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>GET<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="custom-metadata-grounding" data-text="Custom metadata" tabindex="-1">Custom metadata</h2>

<p>If you have added custom metadata to your files, you can access it in the
annotations of the model&#39;s response. This is useful for passing
additional context (like URLs, page numbers, or authors) from your source
documents to your application logic. Each citation annotation of type <code translate="no" dir="ltr">file_citation</code>
contains this custom metadata.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_11" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Tell me about [insert question]"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"file_search_store_names"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">]</span>
    <span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">step</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">steps</span><span class="devsite-syntax-p">:</span>
    <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">type</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">:</span>
        <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">content_block</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">step</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span><span class="devsite-syntax-p">:</span>
            <span class="devsite-syntax-k">if</span> <span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                <span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">annotation</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">content_block</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">annotations</span><span class="devsite-syntax-p">:</span>
                    <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">annotation</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_11" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Tell me about [insert question]"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">file_search_store_names</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}]</span>
<span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">steps</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">===</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'model_output'</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">step</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">content</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">contentBlock</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">annotations</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">forEach</span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">annotation</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
<section><h3 id="java_11" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_10" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"steps"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"model_output"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"content"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"text"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-nt">"annotations"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"file_name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"source"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"..."</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-nt">"custom_metadata"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-nt">"key"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"author"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-nt">"string_value"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Robert Graves"</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-nt">"key"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"year"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                  </span><span class="devsite-syntax-nt">"numeric_value"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mi">1934</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">              </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">          </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="structured-output" data-text="Structured output" tabindex="-1">Structured output</h2>

<p>Starting with Gemini 3 models, you can combine file search tool with
<a href="/gemini-api/docs/structured-output">structured outputs</a>.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_12" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">pydantic</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">BaseModel</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">Field</span>

<span class="devsite-syntax-k">class</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nc">Money</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">BaseModel</span><span class="devsite-syntax-p">):</span>
    <span class="devsite-syntax-n">amount</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-nb">str</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">Field</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">description</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"The numerical part of the amount."</span><span class="devsite-syntax-p">)</span>
    <span class="devsite-syntax-n">currency</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-nb">str</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">Field</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">description</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"The currency of amount."</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"What is the minimum hourly wage in Tokyo right now?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">tools</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"file_search_store_names"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-p">[</span><span class="devsite-syntax-n">file_search_store</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">]</span>
    <span class="devsite-syntax-p">}],</span>
    <span class="devsite-syntax-n">response_format</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"application/json"</span><span class="devsite-syntax-p">,</span>
        <span class="devsite-syntax-s2">"schema"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">Money</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">model_json_schema</span><span class="devsite-syntax-p">()</span>
    <span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-n">result</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">Money</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">model_validate_json</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_12" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">z</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"zod"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">moneyJsonSchema</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"object"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">properties</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">amount</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">description</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"The numerical part of the amount."</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">currency</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"string"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">description</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"The currency of amount."</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">required</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"amount"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"currency"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">};</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">moneySchema</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">z</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">fromJSONSchema</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">moneyJsonSchema</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">run</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"What is the minimum hourly wage in Tokyo right now?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">tools</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"file_search"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">file_search_store_names</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-nx">fileSearchStore</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}],</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">response_format</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'text'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'application/json'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nx">schema</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">moneyJsonSchema</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">moneySchema</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">JSON</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">parse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">));</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">run</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
<section><h3 id="java_12" data-text="Java" tabindex="-1">Java</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Java"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.Client</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Content</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.CreateModelInteraction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.DocumentContentMimeType</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Interaction</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.InteractionsInput</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.Model</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.interactions.TextContent</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">com.google.genai.gaos.models.operations.CreateInteractionRequestBody</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.Arrays</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">java.util.List</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-n">Client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">TextContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">text</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"Summarize this document."</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>
<span class="devsite-syntax-n">Content</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">DocumentContent</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">uri</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gs://cloud-samples-data/generative-ai/pdf/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">mimeType</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">DocumentContentMimeType</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">APPLICATION_PDF</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">List&lt;Content&gt;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">Arrays</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">asList</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">textContent</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">docContent</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">CreateModelInteraction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">builder</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">model</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">Model</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"gemini-3.7-flash"</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">input</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">InteractionsInput</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">ofContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">contents</span><span class="devsite-syntax-p">))</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">build</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">Interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-n">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">create</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">CreateInteractionRequestBody</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">of</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">params</span><span class="devsite-syntax-p">)).</span><span class="devsite-syntax-na">interaction</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">get</span><span class="devsite-syntax-p">();</span>

<span class="devsite-syntax-n">System</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">out</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-na">outputText</span><span class="devsite-syntax-p">().</span><span class="devsite-syntax-na">orElse</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">));</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_11" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Content-Type: application/json'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": "What is the minimum hourly wage in Tokyo right now?",</span>
<span class="devsite-syntax-s1">    "tools": [{</span>
<span class="devsite-syntax-s1">      "type": "file_search",</span>
<span class="devsite-syntax-s1">      "file_search_store_names": ["$FILE_SEARCH_STORE_NAME"]</span>
<span class="devsite-syntax-s1">    }],</span>
<span class="devsite-syntax-s1">    "response_format": {</span>
<span class="devsite-syntax-s1">      "type": "text",</span>
<span class="devsite-syntax-s1">      "mime_type": "application/json",</span>
<span class="devsite-syntax-s1">      "schema": {</span>
<span class="devsite-syntax-s1">        "type": "object",</span>
<span class="devsite-syntax-s1">        "properties": {</span>
<span class="devsite-syntax-s1">          "amount": {"type": "string", "description": "The numerical part of the amount."},</span>
<span class="devsite-syntax-s1">          "currency": {"type": "string", "description": "The currency of amount."}</span>
<span class="devsite-syntax-s1">        },</span>
<span class="devsite-syntax-s1">        "required": ["amount", "currency"]</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    }</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="supported-models" data-text="Supported models" tabindex="-1">Supported models</h2>

<p>The following models support File Search:</p>

<table>
<thead>
<tr>
<th>Model</th>
<th style="text-align: center">File Search</th>
</tr>
</thead>

<tbody>
<tr>
<td><a href="/gemini-api/docs/models/gemini-3.7-flash">Gemini 3.7 Flash</a></td>
<td style="text-align: center">✔️</td>
</tr>
<tr>
<td><a href="/gemini-api/docs/models/gemini-3.6-flash">Gemini 3.6 Flash</a></td>
<td style="text-align: center">✔️</td>
</tr>
<tr>
<td><a href="/gemini-api/docs/models/gemini-3.5-flash-lite">Gemini 3.5 Flash-Lite</a></td>
<td style="text-align: center">✔️</td>
</tr>
<tr>
<td><a href="/gemini-api/docs/models/gemini-3.5-flash">Gemini 3.5 Flash</a></td>
<td style="text-align: center">✔️</td>
</tr>
<tr>
<td><a href="/gemini-api/docs/models/gemini-3.1-pro-preview">Gemini 3.1 Pro Preview</a></td>
<td style="text-align: center">✔️</td>
</tr>
<tr>
<td><a href="/gemini-api/docs/models/gemini-3.1-flash-lite">Gemini 3.1 Flash-Lite</a></td>
<td style="text-align: center">✔️</td>
</tr>
<tr>
<td><a href="/gemini-api/docs/models/gemini-3-flash-preview">Gemini 3 Flash Preview</a></td>
<td style="text-align: center">✔️</td>
</tr>
</tbody>
</table>

<h2 id="supported-files" data-text="Supported file types" tabindex="-1">Supported file types</h2>

<p>File Search supports a wide range of file formats, listed in the following
sections.</p>

<h3 id="application" data-text="Application file types" tabindex="-1">Application file types</h3>

<ul>
<li><code translate="no" dir="ltr">application/dart</code></li>
<li><code translate="no" dir="ltr">application/ecmascript</code></li>
<li><code translate="no" dir="ltr">application/json</code></li>
<li><code translate="no" dir="ltr">application/ms-java</code></li>
<li><code translate="no" dir="ltr">application/msword</code></li>
<li><code translate="no" dir="ltr">application/pdf</code></li>
<li><code translate="no" dir="ltr">application/sql</code></li>
<li><code translate="no" dir="ltr">application/typescript</code></li>
<li><code translate="no" dir="ltr">application/vnd.curl</code></li>
<li><code translate="no" dir="ltr">application/vnd.dart</code></li>
<li><code translate="no" dir="ltr">application/vnd.ibm.secure-container</code></li>
<li><code translate="no" dir="ltr">application/vnd.jupyter</code></li>
<li><code translate="no" dir="ltr">application/vnd.ms-excel</code></li>
<li><code translate="no" dir="ltr">application/vnd.oasis.opendocument.text</code></li>
<li><code translate="no" dir="ltr">application/vnd.openxmlformats-officedocument.presentationml.presentation</code></li>
<li><code translate="no" dir="ltr">application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</code></li>
<li><code translate="no" dir="ltr">application/vnd.openxmlformats-officedocument.wordprocessingml.document</code></li>
<li><code translate="no" dir="ltr">application/vnd.openxmlformats-officedocument.wordprocessingml.template</code></li>
<li><code translate="no" dir="ltr">application/x-csh</code></li>
<li><code translate="no" dir="ltr">application/x-hwp</code></li>
<li><code translate="no" dir="ltr">application/x-hwp-v5</code></li>
<li><code translate="no" dir="ltr">application/x-latex</code></li>
<li><code translate="no" dir="ltr">application/x-php</code></li>
<li><code translate="no" dir="ltr">application/x-powershell</code></li>
<li><code translate="no" dir="ltr">application/x-sh</code></li>
<li><code translate="no" dir="ltr">application/x-shellscript</code></li>
<li><code translate="no" dir="ltr">application/x-tex</code></li>
<li><code translate="no" dir="ltr">application/x-zsh</code></li>
<li><code translate="no" dir="ltr">application/xml</code></li>
<li><code translate="no" dir="ltr">application/zip</code></li>
</ul>

<h3 id="text" data-text="Text file types" tabindex="-1">Text file types</h3>

<ul>
<li><code translate="no" dir="ltr">text/1d-interleaved-parityfec</code></li>
<li><code translate="no" dir="ltr">text/RED</code></li>
<li><code translate="no" dir="ltr">text/SGML</code></li>
<li><code translate="no" dir="ltr">text/cache-manifest</code></li>
<li><code translate="no" dir="ltr">text/calendar</code></li>
<li><code translate="no" dir="ltr">text/cql</code></li>
<li><code translate="no" dir="ltr">text/cql-extension</code></li>
<li><code translate="no" dir="ltr">text/cql-identifier</code></li>
<li><code translate="no" dir="ltr">text/css</code></li>
<li><code translate="no" dir="ltr">text/csv</code></li>
<li><code translate="no" dir="ltr">text/csv-schema</code></li>
<li><code translate="no" dir="ltr">text/dns</code></li>
<li><code translate="no" dir="ltr">text/encaprtp</code></li>
<li><code translate="no" dir="ltr">text/enriched</code></li>
<li><code translate="no" dir="ltr">text/example</code></li>
<li><code translate="no" dir="ltr">text/fhirpath</code></li>
<li><code translate="no" dir="ltr">text/flexfec</code></li>
<li><code translate="no" dir="ltr">text/fwdred</code></li>
<li><code translate="no" dir="ltr">text/gff3</code></li>
<li><code translate="no" dir="ltr">text/grammar-ref-list</code></li>
<li><code translate="no" dir="ltr">text/hl7v2</code></li>
<li><code translate="no" dir="ltr">text/html</code></li>
<li><code translate="no" dir="ltr">text/javascript</code></li>
<li><code translate="no" dir="ltr">text/jcr-cnd</code></li>
<li><code translate="no" dir="ltr">text/jsx</code></li>
<li><code translate="no" dir="ltr">text/markdown</code></li>
<li><code translate="no" dir="ltr">text/mizar</code></li>
<li><code translate="no" dir="ltr">text/n3</code></li>
<li><code translate="no" dir="ltr">text/parameters</code></li>
<li><code translate="no" dir="ltr">text/parityfec</code></li>
<li><code translate="no" dir="ltr">text/php</code></li>
<li><code translate="no" dir="ltr">text/plain</code></li>
<li><code translate="no" dir="ltr">text/provenance-notation</code></li>
<li><code translate="no" dir="ltr">text/prs.fallenstein.rst</code></li>
<li><code translate="no" dir="ltr">text/prs.lines.tag</code></li>
<li><code translate="no" dir="ltr">text/prs.prop.logic</code></li>
<li><code translate="no" dir="ltr">text/raptorfec</code></li>
<li><code translate="no" dir="ltr">text/rfc822-headers</code></li>
<li><code translate="no" dir="ltr">text/rtf</code></li>
<li><code translate="no" dir="ltr">text/rtp-enc-aescm128</code></li>
<li><code translate="no" dir="ltr">text/rtploopback</code></li>
<li><code translate="no" dir="ltr">text/rtx</code></li>
<li><code translate="no" dir="ltr">text/sgml</code></li>
<li><code translate="no" dir="ltr">text/shaclc</code></li>
<li><code translate="no" dir="ltr">text/shex</code></li>
<li><code translate="no" dir="ltr">text/spdx</code></li>
<li><code translate="no" dir="ltr">text/strings</code></li>
<li><code translate="no" dir="ltr">text/t140</code></li>
<li><code translate="no" dir="ltr">text/tab-separated-values</code></li>
<li><code translate="no" dir="ltr">text/texmacs</code></li>
<li><code translate="no" dir="ltr">text/troff</code></li>
<li><code translate="no" dir="ltr">text/tsv</code></li>
<li><code translate="no" dir="ltr">text/tsx</code></li>
<li><code translate="no" dir="ltr">text/turtle</code></li>
<li><code translate="no" dir="ltr">text/ulpfec</code></li>
<li><code translate="no" dir="ltr">text/uri-list</code></li>
<li><code translate="no" dir="ltr">text/vcard</code></li>
<li><code translate="no" dir="ltr">text/vnd.DMClientScript</code></li>
<li><code translate="no" dir="ltr">text/vnd.IPTC.NITF</code></li>
<li><code translate="no" dir="ltr">text/vnd.IPTC.NewsML</code></li>
<li><code translate="no" dir="ltr">text/vnd.a</code></li>
<li><code translate="no" dir="ltr">text/vnd.abc</code></li>
<li><code translate="no" dir="ltr">text/vnd.ascii-art</code></li>
<li><code translate="no" dir="ltr">text/vnd.curl</code></li>
<li><code translate="no" dir="ltr">text/vnd.debian.copyright</code></li>
<li><code translate="no" dir="ltr">text/vnd.dvb.subtitle</code></li>
<li><code translate="no" dir="ltr">text/vnd.esmertec.theme-descriptor</code></li>
<li><code translate="no" dir="ltr">text/vnd.exchangeable</code></li>
<li><code translate="no" dir="ltr">text/vnd.familysearch.gedcom</code></li>
<li><code translate="no" dir="ltr">text/vnd.ficlab.flt</code></li>
<li><code translate="no" dir="ltr">text/vnd.fly</code></li>
<li><code translate="no" dir="ltr">text/vnd.fmi.flexstor</code></li>
<li><code translate="no" dir="ltr">text/vnd.gml</code></li>
<li><code translate="no" dir="ltr">text/vnd.graphviz</code></li>
<li><code translate="no" dir="ltr">text/vnd.hans</code></li>
<li><code translate="no" dir="ltr">text/vnd.hgl</code></li>
<li><code translate="no" dir="ltr">text/vnd.in3d.3dml</code></li>
<li><code translate="no" dir="ltr">text/vnd.in3d.spot</code></li>
<li><code translate="no" dir="ltr">text/vnd.latex-z</code></li>
<li><code translate="no" dir="ltr">text/vnd.motorola.reflex</code></li>
<li><code translate="no" dir="ltr">text/vnd.ms-mediapackage</code></li>
<li><code translate="no" dir="ltr">text/vnd.net2phone.commcenter.command</code></li>
<li><code translate="no" dir="ltr">text/vnd.radisys.msml-basic-layout</code></li>
<li><code translate="no" dir="ltr">text/vnd.senx.warpscript</code></li>
<li><code translate="no" dir="ltr">text/vnd.sosi</code></li>
<li><code translate="no" dir="ltr">text/vnd.sun.j2me.app-descriptor</code></li>
<li><code translate="no" dir="ltr">text/vnd.trolltech.linguist</code></li>
<li><code translate="no" dir="ltr">text/vnd.wap.si</code></li>
<li><code translate="no" dir="ltr">text/vnd.wap.sl</code></li>
<li><code translate="no" dir="ltr">text/vnd.wap.wml</code></li>
<li><code translate="no" dir="ltr">text/vnd.wap.wmlscript</code></li>
<li><code translate="no" dir="ltr">text/vtt</code></li>
<li><code translate="no" dir="ltr">text/wgsl</code></li>
<li><code translate="no" dir="ltr">text/x-asm</code></li>
<li><code translate="no" dir="ltr">text/x-bibtex</code></li>
<li><code translate="no" dir="ltr">text/x-boo</code></li>
<li><code translate="no" dir="ltr">text/x-c</code></li>
<li><code translate="no" dir="ltr">text/x-c++hdr</code></li>
<li><code translate="no" dir="ltr">text/x-c++src</code></li>
<li><code translate="no" dir="ltr">text/x-cassandra</code></li>
<li><code translate="no" dir="ltr">text/x-chdr</code></li>
<li><code translate="no" dir="ltr">text/x-coffeescript</code></li>
<li><code translate="no" dir="ltr">text/x-component</code></li>
<li><code translate="no" dir="ltr">text/x-csh</code></li>
<li><code translate="no" dir="ltr">text/x-csharp</code></li>
<li><code translate="no" dir="ltr">text/x-csrc</code></li>
<li><code translate="no" dir="ltr">text/x-cuda</code></li>
<li><code translate="no" dir="ltr">text/x-d</code></li>
<li><code translate="no" dir="ltr">text/x-diff</code></li>
<li><code translate="no" dir="ltr">text/x-dsrc</code></li>
<li><code translate="no" dir="ltr">text/x-emacs-lisp</code></li>
<li><code translate="no" dir="ltr">text/x-erlang</code></li>
<li><code translate="no" dir="ltr">text/x-gff3</code></li>
<li><code translate="no" dir="ltr">text/x-go</code></li>
<li><code translate="no" dir="ltr">text/x-haskell</code></li>
<li><code translate="no" dir="ltr">text/x-java</code></li>
<li><code translate="no" dir="ltr">text/x-java-properties</code></li>
<li><code translate="no" dir="ltr">text/x-java-source</code></li>
<li><code translate="no" dir="ltr">text/x-kotlin</code></li>
<li><code translate="no" dir="ltr">text/x-lilypond</code></li>
<li><code translate="no" dir="ltr">text/x-lisp</code></li>
<li><code translate="no" dir="ltr">text/x-literate-haskell</code></li>
<li><code translate="no" dir="ltr">text/x-lua</code></li>
<li><code translate="no" dir="ltr">text/x-moc</code></li>
<li><code translate="no" dir="ltr">text/x-objcsrc</code></li>
<li><code translate="no" dir="ltr">text/x-pascal</code></li>
<li><code translate="no" dir="ltr">text/x-pcs-gcd</code></li>
<li><code translate="no" dir="ltr">text/x-perl</code></li>
<li><code translate="no" dir="ltr">text/x-perl-script</code></li>
<li><code translate="no" dir="ltr">text/x-python</code></li>
<li><code translate="no" dir="ltr">text/x-python-script</code></li>
<li><code translate="no" dir="ltr">text/x-r-markdown</code></li>
<li><code translate="no" dir="ltr">text/x-rsrc</code></li>
<li><code translate="no" dir="ltr">text/x-rst</code></li>
<li><code translate="no" dir="ltr">text/x-ruby-script</code></li>
<li><code translate="no" dir="ltr">text/x-rust</code></li>
<li><code translate="no" dir="ltr">text/x-sass</code></li>
<li><code translate="no" dir="ltr">text/x-scala</code></li>
<li><code translate="no" dir="ltr">text/x-scheme</code></li>
<li><code translate="no" dir="ltr">text/x-script.python</code></li>
<li><code translate="no" dir="ltr">text/x-scss</code></li>
<li><code translate="no" dir="ltr">text/x-setext</code></li>
<li><code translate="no" dir="ltr">text/x-sfv</code></li>
<li><code translate="no" dir="ltr">text/x-sh</code></li>
<li><code translate="no" dir="ltr">text/x-siesta</code></li>
<li><code translate="no" dir="ltr">text/x-sos</code></li>
<li><code translate="no" dir="ltr">text/x-sql</code></li>
<li><code translate="no" dir="ltr">text/x-swift</code></li>
<li><code translate="no" dir="ltr">text/x-tcl</code></li>
<li><code translate="no" dir="ltr">text/x-tex</code></li>
<li><code translate="no" dir="ltr">text/x-vbasic</code></li>
<li><code translate="no" dir="ltr">text/x-vcalendar</code></li>
<li><code translate="no" dir="ltr">text/xml</code></li>
<li><code translate="no" dir="ltr">text/xml-dtd</code></li>
<li><code translate="no" dir="ltr">text/xml-external-parsed-entity</code></li>
<li><code translate="no" dir="ltr">text/yaml</code></li>
</ul>

<h2 id="limitations" data-text="Limitations" tabindex="-1">Limitations</h2>

<ul>
<li><strong>Live API:</strong> File Search is not supported in the
<a href="/gemini-api/docs/live">Live API</a>.</li>
<li><strong>Tool incompatibility:</strong> Built-in grounding tools cannot be combined with one another;
for example, File Search cannot be used simultaneously with <a href="/gemini-api/docs/google-search">Grounding with Google Search</a> or
<a href="/gemini-api/docs/url-context">URL Context</a> in the same request.</li>
</ul>

<h3 id="rate-limits" data-text="Rate limits" tabindex="-1">Rate limits</h3>

<p>The File Search API has the following limits to enforce service stability:</p>

<ul>
<li><strong>Maximum file size / per document limit</strong>: 100 MB</li>
<li><strong>Total size of project File Search stores</strong> (based on user tier):
<ul>
<li><strong>Free</strong>: 1 GB</li>
<li><strong>Tier 1</strong>: 10 GB</li>
<li><strong>Tier 2</strong>: 100 GB</li>
<li><strong>Tier 3</strong>: 1 TB</li>
</ul></li>
<li><strong>Recommendation</strong>: Limit the size of each File Search store to under 20 GB to ensure optimal retrieval latencies.</li>
</ul>
<aside class="note"><strong>Note:</strong><span> The limit on File Search store size is computed on the backend, based on
the size of your input plus the embeddings generated and stored with it. This
is typically approximately 3 times the size of your input data.</span></aside>
<h2 id="pricing" data-text="Pricing" tabindex="-1">Pricing</h2>

<ul>
<li>You are charged for embeddings at indexing time based on existing
<a href="/gemini-api/docs/pricing#gemini-embedding-2">embeddings pricing</a>.</li>
<li>Storage is free of charge.</li>
<li>Query time embeddings are free of charge.</li>
<li>Retrieved document tokens are charged as regular
<a href="/gemini-api/docs/tokens">context tokens</a>.</li>
</ul>

<h2 id="whats_next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li>Visit the API reference for <a href="/api/file-search/file-search-stores">File Search Stores</a> and File Search <a href="/api/file-search/documents">Documents</a>.</li>
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