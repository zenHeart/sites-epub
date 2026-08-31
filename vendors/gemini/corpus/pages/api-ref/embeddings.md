








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/api/embeddings"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/api/embeddings" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/api/embeddings" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/api/embeddings?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/api/embeddings?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/api/embeddings?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/api/embeddings?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/api/embeddings?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/api/embeddings?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/api/embeddings?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/api/embeddings?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/api/embeddings?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/api/embeddings?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/api/embeddings?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/api/embeddings?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/api/embeddings?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/api/embeddings?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/api/embeddings?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/api/embeddings?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/api/embeddings?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/api/embeddings?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/api/embeddings?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/api/embeddings?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/api/embeddings?hl=sq" /><title>Embeddings &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="Embeddings &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta property="og:url" content="https://ai.google.dev/api/embeddings"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675"><meta property="og:locale" content="en"><meta name="twitter:card" content="summary_large_image">
  








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
      Embeddings<devsite-actions hidden data-nosnippet>
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

  
    
    <p>Embeddings are a numerical representation of text input that open up a number of unique use cases, such as clustering, similarity measurement and information retrieval. For an introduction, check out the <a href="https://ai.google.dev/gemini-api/docs/embeddings">Embeddings guide</a>.</p>
<p> Unlike generative AI models that create new content, the Gemini Embedding model is only intended to transform the format of your input data into a numerical representation. While Google is responsible for providing an embedding model that transforms the format of your input data to the numerical-format requested, users retain full responsibility for the data they input and the resulting embeddings. By using the Gemini Embedding model you confirm that you have the necessary rights to any content that you upload. Do not generate content that infringes on others' intellectual property or privacy rights. Your use of this service is subject to our <a href="https://policies.google.com/terms/generative-ai/use-policy">Prohibited Use Policy</a> and <a href="https://ai.google.dev/gemini-api/terms">Google's Terms of Service</a>.</p>
<div itemscope="" itemtype="http://developers.google.com/ReferenceObject"><h2 id="method:-models.embedcontent" data-text="Method: models.embedContent" tabindex="-1">Method: models.embedContent</h2><a name="v1beta.models.embedContent"></a>
<meta content="embedContent" itemprop="name"/>
<meta content="/api/rest/v1beta/models/embedContent" itemprop="path"/>
<section class="prototype" id="/api/rest/v1beta/models/embedContent">
<ul class="toc">
<li><a href="#body.HTTP_TEMPLATE">Endpoint</a></li><li><a href="#body.PATH_PARAMETERS">Path parameters</a></li><li><a href="#body.request_body">Request body</a>
<ul>
<li><a href="#body.request_body.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li><li><a href="#body.response_body">Response body</a></li><li><a href="#body.aspect">Authorization scopes</a></li><li><a href="#body.codeSnippets">Example request</a>
<ul>
<li><a href="#body.codeSnippets.group">Basic</a></li>
</ul>
</li>
</ul>
<section id="google.ai.generativelanguage.v1beta.GenerativeService.EmbedContent">
</section>
<section id="description">
<p>Generates a text embedding vector from the input <code translate="no" dir="ltr">Content</code> using the specified <a href="https://ai.google.dev/gemini-api/docs/models/gemini#text-embedding">Gemini Embedding model</a>.</p>
</section>
<div class="column-container">
<div class="reference">
<section id="body.HTTP_TEMPLATE">
<h3 id="endpoint" data-text="Endpoint" tabindex="-1">Endpoint</h3>
<span class="endpoint">
<span class="http-method">
                post
              </span>
<span class="endpoint-url">
<code translate="no" dir="ltr">https:<wbr/>/<wbr/>/generativelanguage.googleapis.com<wbr/>/v1beta<wbr/>/{model=models<wbr/>/*}:embedContent</code>
</span>
</span>
<br/>
<span>

</span>
</section>
<section id="body.PATH_PARAMETERS">
<h3 id="path-parameters" data-text="Path parameters" tabindex="-1">Path parameters</h3>
<section id="body.PATH_PARAMETERS.model">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">model</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Required. The model's resource name. This serves as an ID for the Model to use.</p><p>This name should match a model name returned by the <code translate="no" dir="ltr">models.list</code> method.</p><p>Format: <code translate="no" dir="ltr">models/{model}</code> It takes the form <code translate="no" dir="ltr">models/{model}</code>.</p>
</div>
</div>
</section>
</section>
<section id="body.request_body">
<h3 id="request-body" data-text="Request body" tabindex="-1">Request body</h3>
<p>The request body contains data with the following structure:</p>
<section id="body.request_body.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="body.request_body.FIELDS.content">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">content</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/generate-content#v1beta.Content">Content</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Required. The content to embed. Only the <code translate="no" dir="ltr">parts.text</code> fields will be counted.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.task_type">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">taskType<br/><b>(deprecated)</b></code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">enum (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.TaskType">TaskType</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Optional. Deprecated: Please use EmbedContentConfig.task_type instead. Optional task type for which the embeddings will be used. Not supported on earlier models (<code translate="no" dir="ltr">models/embedding-001</code>).</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.title">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">title<br/><b>(deprecated)</b></code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Optional. Deprecated: Please use EmbedContentConfig.title instead. An optional title for the text. Only applicable when TaskType is <code translate="no" dir="ltr">RETRIEVAL_DOCUMENT</code>.</p><p>Note: Specifying a <code translate="no" dir="ltr">title</code> for <code translate="no" dir="ltr">RETRIEVAL_DOCUMENT</code> provides better quality embeddings for retrieval.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.output_dimensionality">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">outputDimensionality<br/><b>(deprecated)</b></code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">integer</code>
</span>
</div>
<div class="field-description">
<p>Optional. Deprecated: Please use EmbedContentConfig.output_dimensionality instead. Optional reduced dimension for the output embedding. If set, excessive values in the output embedding are truncated from the end. Supported by newer models since 2024 only. You cannot set this value if using the earlier model (<code translate="no" dir="ltr">models/embedding-001</code>).</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.embed_content_config">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">embedContentConfig</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.EmbedContentConfig">EmbedContentConfig</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Optional. Configuration for the models.embedContent request.</p>
</div>
</div>
</section>
</section>
</section>
</div>
<div class="second-column">
<h3 id="example-request" data-text="Example request" tabindex="-1">Example request</h3>
<devsite-selector>
<section>
<h3 id="embed_content-PYTHON" track-metadata-position="embed_content" track-metadata-region-tag="embed_content" data-text="Python" tabindex="-1">Python</h3>
              






  
  














  



<div class="github-docwidget-gitinclude-code">

  
    
  
  











  









  




  



  <div></div><devsite-code><pre suppresswarning="suppresswarning" translate="no" class="devsite-click-to-copy" track-metadata-position="google-gemini/api-examples/python/embed.py/HEAD/embed_content" data-code-snippet="true" data-github-includecode-link="https://github.com/google-gemini/api-examples/blob/HEAD/python/embed.py" track-metadata-snippet-file-url="https://github.com/google-gemini/api-examples/blob/HEAD/python/embed.py" language="PYTHON" data-github-path="google-gemini/api-examples/python/embed.py" data-git-revision="HEAD" data-region-tag="embed_content" track-metadata-region-tag="embed_content" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-n">text</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"Hello World!"</span>
<span class="devsite-syntax-n">result</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">embed_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-embedding-001"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">EmbedContentConfig</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">output_dimensionality</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">10</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">embeddings</span><span class="devsite-syntax-p">)</span><div class="devsite-github-link nocode no-select nocontent"><a target="_top" href="https://github.com/google-gemini/api-examples/blob/51979868abf95d062a149b62af92854b2a24f005/python/embed.py#L22-L32" class="gc-analytics-event" data-category="github_link" data-label="google-gemini/api-examples/python/embed.py#embed_content" data-code-snippet="true" data-git-revision="HEAD" data-github-path="google-gemini/api-examples/python/embed.py" data-indented-block="" data-regexp="" data-region-tag="embed_content"><span class="devsite-syntax-n">embed</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">py</span></a></div></code></pre></devsite-code>
</div>



























            </section>
<section>
<h3 id="embed_content-JAVASCRIPT" track-metadata-position="embed_content" track-metadata-region-tag="embed_content" data-text="Node.js" tabindex="-1">Node.js</h3>
              






  
  














  



<div class="github-docwidget-gitinclude-code">

  
    
  
  











  









  




  



  <div></div><devsite-code><pre suppresswarning="suppresswarning" translate="no" class="devsite-click-to-copy" track-metadata-position="google-gemini/api-examples/javascript/embed.js/HEAD/embed_content" data-code-snippet="true" data-github-includecode-link="https://github.com/google-gemini/api-examples/blob/HEAD/javascript/embed.js" track-metadata-snippet-file-url="https://github.com/google-gemini/api-examples/blob/HEAD/javascript/embed.js" language="JAVASCRIPT" data-github-path="google-gemini/api-examples/javascript/embed.js" data-git-revision="HEAD" data-region-tag="embed_content" track-metadata-region-tag="embed_content" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Make sure to include the following import:</span>
<span class="devsite-syntax-c1">// import {GoogleGenAI} from '@google/genai';</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">apiKey</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">env</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">GEMINI_API_KEY</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hello World!"</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">embedContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-embedding-001"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">outputDimensionality</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">10</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">embeddings</span><span class="devsite-syntax-p">);</span><div class="devsite-github-link nocode no-select nocontent"><a target="_top" href="https://github.com/google-gemini/api-examples/blob/51979868abf95d062a149b62af92854b2a24f005/javascript/embed.js#L22-L31" class="gc-analytics-event" data-category="github_link" data-label="google-gemini/api-examples/javascript/embed.js#embed_content" data-code-snippet="true" data-git-revision="HEAD" data-github-path="google-gemini/api-examples/javascript/embed.js" data-indented-block="" data-regexp="" data-region-tag="embed_content"><span class="devsite-syntax-nx">embed</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">js</span></a></div></code></pre></devsite-code>
</div>



























            </section>
<section>
<h3 id="embed_content-GO" track-metadata-position="embed_content" track-metadata-region-tag="embed_content" data-text="Go" tabindex="-1">Go</h3>
              






  
  














  



<div class="github-docwidget-gitinclude-code">

  
    
  
  











  









  




  



  <div></div><devsite-code><pre suppresswarning="suppresswarning" translate="no" class="devsite-click-to-copy" track-metadata-position="google-gemini/api-examples/go/embed.go/HEAD/embed_content" data-code-snippet="true" data-github-includecode-link="https://github.com/google-gemini/api-examples/blob/HEAD/go/embed.go" track-metadata-snippet-file-url="https://github.com/google-gemini/api-examples/blob/HEAD/go/embed.go" language="GO" data-github-path="google-gemini/api-examples/go/embed.go" data-git-revision="HEAD" data-region-tag="embed_content" track-metadata-region-tag="embed_content" dir="ltr" is-upgraded syntax="Go"><code translate="no" dir="ltr"><span class="devsite-syntax-nx">ctx</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">context</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Background</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">NewClient</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">ctx</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span>&amp;<span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">ClientConfig</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">APIKey</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">os</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Getenv</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"GEMINI_API_KEY"</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">Backend</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">BackendGeminiAPI</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">})</span>
<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">!=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">nil</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Fatal</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">text</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"Hello World!"</span>
<span class="devsite-syntax-nx">outputDim</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">int32</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">10</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[]</span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Content</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">NewContentFromText</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">RoleUser</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">EmbedContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">ctx</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"gemini-embedding-001"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span>&amp;<span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">EmbedContentConfig</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">		</span><span class="devsite-syntax-nx">OutputDimensionality</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span>&amp;<span class="devsite-syntax-nx">outputDim</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">})</span>
<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">!=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">nil</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Fatal</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">embeddings</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">json</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">MarshalIndent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Embeddings</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"  "</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">!=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">nil</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Fatal</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-nx">fmt</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">string</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">embeddings</span><span class="devsite-syntax-p">))</span><div class="devsite-github-link nocode no-select nocontent"><a target="_top" href="https://github.com/google-gemini/api-examples/blob/51979868abf95d062a149b62af92854b2a24f005/go/embed.go#L15-L41" class="gc-analytics-event" data-category="github_link" data-label="google-gemini/api-examples/go/embed.go#embed_content" data-code-snippet="true" data-git-revision="HEAD" data-github-path="google-gemini/api-examples/go/embed.go" data-indented-block="" data-regexp="" data-region-tag="embed_content"><span class="devsite-syntax-nx">embed</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">go</span></a></div></code></pre></devsite-code>
</div>



























            </section>
<section>
<h3 id="embed_content-SHELL" track-metadata-position="embed_content" track-metadata-region-tag="embed_content" data-text="Shell" tabindex="-1">Shell</h3>
              






  
  














  



<div class="github-docwidget-gitinclude-code">

  
    
  
  











  









  




  



  <div></div><devsite-code><pre suppresswarning="suppresswarning" translate="no" class="devsite-click-to-copy" track-metadata-position="google-gemini/api-examples/rest/embed.sh/HEAD/embed_content" data-code-snippet="true" data-github-includecode-link="https://github.com/google-gemini/api-examples/blob/HEAD/rest/embed.sh" track-metadata-snippet-file-url="https://github.com/google-gemini/api-examples/blob/HEAD/rest/embed.sh" language="SHELL" data-github-path="google-gemini/api-examples/rest/embed.sh" data-git-revision="HEAD" data-region-tag="embed_content" track-metadata-region-tag="embed_content" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Content-Type: application/json'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{"model": "models/gemini-embedding-001",</span>
<span class="devsite-syntax-s1">     "content": {</span>
<span class="devsite-syntax-s1">     "parts":[{</span>
<span class="devsite-syntax-s1">     "text": "What is the meaning of life?"}]}</span>
<span class="devsite-syntax-s1">    }'</span><div class="devsite-github-link nocode no-select nocontent"><a target="_top" href="https://github.com/google-gemini/api-examples/blob/51979868abf95d062a149b62af92854b2a24f005/rest/embed.sh#L4-L12" class="gc-analytics-event" data-category="github_link" data-label="google-gemini/api-examples/rest/embed.sh#embed_content" data-code-snippet="true" data-git-revision="HEAD" data-github-path="google-gemini/api-examples/rest/embed.sh" data-indented-block="" data-regexp="" data-region-tag="embed_content">embed.sh</a></div></code></pre></devsite-code>
</div>



























            </section>
</devsite-selector>
</div>
</div>
<div class="column-container">
<div class="reference">
<section id="body.response_body">
<h3 id="response-body" data-text="Response body" tabindex="-1">Response body</h3>
<p>If successful, the response body contains an instance of <code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.EmbedContentResponse">EmbedContentResponse</a></code>.</p>
</section>
</div>
</div>
</section>
</div><div itemscope="" itemtype="http://developers.google.com/ReferenceObject"><h2 id="method:-models.batchembedcontents" data-text="Method: models.batchEmbedContents" tabindex="-1">Method: models.batchEmbedContents</h2><a name="v1beta.models.batchEmbedContents"></a>
<meta content="batchEmbedContents" itemprop="name"/>
<meta content="/api/rest/v1beta/models/batchEmbedContents" itemprop="path"/>
<section class="prototype" id="/api/rest/v1beta/models/batchEmbedContents">
<ul class="toc">
<li><a href="#body.HTTP_TEMPLATE">Endpoint</a></li><li><a href="#body.PATH_PARAMETERS">Path parameters</a></li><li><a href="#body.request_body">Request body</a>
<ul>
<li><a href="#body.request_body.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li><li><a href="#body.response_body">Response body</a>
<ul>
<li><a href="#body.BatchEmbedContentsResponse.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li><li><a href="#body.aspect">Authorization scopes</a></li><li><a href="#body.codeSnippets">Example request</a>
<ul>
<li><a href="#body.codeSnippets.group">Basic</a></li>
</ul>
</li>
</ul>
<section id="google.ai.generativelanguage.v1beta.GenerativeService.BatchEmbedContents">
</section>
<section id="description">
<p>Generates multiple embedding vectors from the input <code translate="no" dir="ltr">Content</code> which consists of a batch of strings represented as <code translate="no" dir="ltr">EmbedContentRequest</code> objects.</p>
</section>
<div class="column-container">
<div class="reference">
<section id="body.HTTP_TEMPLATE">
<h3 id="endpoint_1" data-text="Endpoint" tabindex="-1">Endpoint</h3>
<span class="endpoint">
<span class="http-method">
                post
              </span>
<span class="endpoint-url">
<code translate="no" dir="ltr">https:<wbr/>/<wbr/>/generativelanguage.googleapis.com<wbr/>/v1beta<wbr/>/{model=models<wbr/>/*}:batchEmbedContents</code>
</span>
</span>
<br/>
<span>

</span>
</section>
<section id="body.PATH_PARAMETERS">
<h3 id="path-parameters_1" data-text="Path parameters" tabindex="-1">Path parameters</h3>
<section id="body.PATH_PARAMETERS.model">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">model</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Required. The model's resource name. This serves as an ID for the Model to use.</p><p>This name should match a model name returned by the <code translate="no" dir="ltr">models.list</code> method.</p><p>Format: <code translate="no" dir="ltr">models/{model}</code> It takes the form <code translate="no" dir="ltr">models/{model}</code>.</p>
</div>
</div>
</section>
</section>
<section id="body.request_body">
<h3 id="request-body_1" data-text="Request body" tabindex="-1">Request body</h3>
<p>The request body contains data with the following structure:</p>
<section id="body.request_body.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="body.request_body.FIELDS.requests">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">requests[]</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/batch-api#EmbedContentRequest">EmbedContentRequest</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Required. Embed requests for the batch. The model in each of these requests must match the model specified <code translate="no" dir="ltr">BatchEmbedContentsRequest.model</code>.</p>
</div>
</div>
</section>
</section>
</section>
</div>
<div class="second-column">
<h3 id="example-request_1" data-text="Example request" tabindex="-1">Example request</h3>
<devsite-selector>
<section>
<h3 id="batch_embed_contents-PYTHON" track-metadata-position="batch_embed_contents" track-metadata-region-tag="batch_embed_contents" data-text="Python" tabindex="-1">Python</h3>
              






  
  














  



<div class="github-docwidget-gitinclude-code">

  
    
  
  











  









  




  



  <div></div><devsite-code><pre suppresswarning="suppresswarning" translate="no" class="devsite-click-to-copy" track-metadata-position="google-gemini/api-examples/python/embed.py/HEAD/batch_embed_contents" data-code-snippet="true" data-github-includecode-link="https://github.com/google-gemini/api-examples/blob/HEAD/python/embed.py" track-metadata-snippet-file-url="https://github.com/google-gemini/api-examples/blob/HEAD/python/embed.py" language="PYTHON" data-github-path="google-gemini/api-examples/python/embed.py" data-git-revision="HEAD" data-region-tag="batch_embed_contents" track-metadata-region-tag="batch_embed_contents" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.genai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">types</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-n">texts</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[</span>
    <span class="devsite-syntax-s2">"What is the meaning of life?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-s2">"How much wood would a woodchuck chuck?"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-s2">"How does the brain work?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-n">result</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">embed_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-embedding-001"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">texts</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">config</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">types</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">EmbedContentConfig</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">output_dimensionality</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-mi">10</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">result</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">embeddings</span><span class="devsite-syntax-p">)</span><div class="devsite-github-link nocode no-select nocontent"><a target="_top" href="https://github.com/google-gemini/api-examples/blob/51979868abf95d062a149b62af92854b2a24f005/python/embed.py#L37-L51" class="gc-analytics-event" data-category="github_link" data-label="google-gemini/api-examples/python/embed.py#batch_embed_contents" data-code-snippet="true" data-git-revision="HEAD" data-github-path="google-gemini/api-examples/python/embed.py" data-indented-block="" data-regexp="" data-region-tag="batch_embed_contents"><span class="devsite-syntax-n">embed</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">py</span></a></div></code></pre></devsite-code>
</div>



























            </section>
<section>
<h3 id="batch_embed_contents-JAVASCRIPT" track-metadata-position="batch_embed_contents" track-metadata-region-tag="batch_embed_contents" data-text="Node.js" tabindex="-1">Node.js</h3>
              






  
  














  



<div class="github-docwidget-gitinclude-code">

  
    
  
  











  









  




  



  <div></div><devsite-code><pre suppresswarning="suppresswarning" translate="no" class="devsite-click-to-copy" track-metadata-position="google-gemini/api-examples/javascript/embed.js/HEAD/batch_embed_contents" data-code-snippet="true" data-github-includecode-link="https://github.com/google-gemini/api-examples/blob/HEAD/javascript/embed.js" track-metadata-snippet-file-url="https://github.com/google-gemini/api-examples/blob/HEAD/javascript/embed.js" language="JAVASCRIPT" data-github-path="google-gemini/api-examples/javascript/embed.js" data-git-revision="HEAD" data-region-tag="batch_embed_contents" track-metadata-region-tag="batch_embed_contents" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-c1">// Make sure to include the following import:</span>
<span class="devsite-syntax-c1">// import {GoogleGenAI} from '@google/genai';</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">apiKey</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">process</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">env</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">GEMINI_API_KEY</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">texts</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-s2">"What is the meaning of life?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-s2">"How much wood would a woodchuck chuck?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-s2">"How does the brain work?"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">];</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">embedContent</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-embedding-001"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">texts</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">outputDimensionality</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-mf">10</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">embeddings</span><span class="devsite-syntax-p">);</span><div class="devsite-github-link nocode no-select nocontent"><a target="_top" href="https://github.com/google-gemini/api-examples/blob/51979868abf95d062a149b62af92854b2a24f005/javascript/embed.js#L38-L51" class="gc-analytics-event" data-category="github_link" data-label="google-gemini/api-examples/javascript/embed.js#batch_embed_contents" data-code-snippet="true" data-git-revision="HEAD" data-github-path="google-gemini/api-examples/javascript/embed.js" data-indented-block="" data-regexp="" data-region-tag="batch_embed_contents"><span class="devsite-syntax-nx">embed</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">js</span></a></div></code></pre></devsite-code>
</div>



























            </section>
<section>
<h3 id="batch_embed_contents-GO" track-metadata-position="batch_embed_contents" track-metadata-region-tag="batch_embed_contents" data-text="Go" tabindex="-1">Go</h3>
              






  
  














  



<div class="github-docwidget-gitinclude-code">

  
    
  
  











  









  




  



  <div></div><devsite-code><pre suppresswarning="suppresswarning" translate="no" class="devsite-click-to-copy" track-metadata-position="google-gemini/api-examples/go/embed.go/HEAD/batch_embed_contents" data-code-snippet="true" data-github-includecode-link="https://github.com/google-gemini/api-examples/blob/HEAD/go/embed.go" track-metadata-snippet-file-url="https://github.com/google-gemini/api-examples/blob/HEAD/go/embed.go" language="GO" data-github-path="google-gemini/api-examples/go/embed.go" data-git-revision="HEAD" data-region-tag="batch_embed_contents" track-metadata-region-tag="batch_embed_contents" dir="ltr" is-upgraded syntax="Go"><code translate="no" dir="ltr"><span class="devsite-syntax-nx">ctx</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">context</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Background</span><span class="devsite-syntax-p">()</span>
<span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">NewClient</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">ctx</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span>&amp;<span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">ClientConfig</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">APIKey</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">os</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Getenv</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"GEMINI_API_KEY"</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">Backend</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">BackendGeminiAPI</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">})</span>
<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">!=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">nil</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Fatal</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[]</span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Content</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">NewContentFromText</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"What is the meaning of life?"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">RoleUser</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">NewContentFromText</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"How much wood would a woodchuck chuck?"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">RoleUser</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">NewContentFromText</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s">"How does the brain work?"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">RoleUser</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">outputDim</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nb">int32</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-mi">10</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Models</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">EmbedContent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">ctx</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"gemini-embedding-001"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">contents</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span>&amp;<span class="devsite-syntax-nx">genai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">EmbedContentConfig</span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">OutputDimensionality</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span>&amp;<span class="devsite-syntax-nx">outputDim</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">})</span>
<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">!=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">nil</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Fatal</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">embeddings</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">:=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">json</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">MarshalIndent</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">result</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Embeddings</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">""</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s">"  "</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">!=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">nil</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">	</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Fatal</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">err</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-nx">fmt</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">Println</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nb">string</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">embeddings</span><span class="devsite-syntax-p">))</span><div class="devsite-github-link nocode no-select nocontent"><a target="_top" href="https://github.com/google-gemini/api-examples/blob/51979868abf95d062a149b62af92854b2a24f005/go/embed.go#L48-L75" class="gc-analytics-event" data-category="github_link" data-label="google-gemini/api-examples/go/embed.go#batch_embed_contents" data-code-snippet="true" data-git-revision="HEAD" data-github-path="google-gemini/api-examples/go/embed.go" data-indented-block="" data-regexp="" data-region-tag="batch_embed_contents"><span class="devsite-syntax-nx">embed</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-k">go</span></a></div></code></pre></devsite-code>
</div>



























            </section>
<section>
<h3 id="batch_embed_contents-SHELL" track-metadata-position="batch_embed_contents" track-metadata-region-tag="batch_embed_contents" data-text="Shell" tabindex="-1">Shell</h3>
              






  
  














  



<div class="github-docwidget-gitinclude-code">

  
    
  
  











  









  




  



  <div></div><devsite-code><pre suppresswarning="suppresswarning" translate="no" class="devsite-click-to-copy" track-metadata-position="google-gemini/api-examples/rest/embed.sh/HEAD/batch_embed_contents" data-code-snippet="true" data-github-includecode-link="https://github.com/google-gemini/api-examples/blob/HEAD/rest/embed.sh" track-metadata-snippet-file-url="https://github.com/google-gemini/api-examples/blob/HEAD/rest/embed.sh" language="SHELL" data-github-path="google-gemini/api-examples/rest/embed.sh" data-git-revision="HEAD" data-region-tag="batch_embed_contents" track-metadata-region-tag="batch_embed_contents" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Content-Type: application/json'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{"requests": [{</span>
<span class="devsite-syntax-s1">      "model": "models/gemini-embedding-001",</span>
<span class="devsite-syntax-s1">      "content": {</span>
<span class="devsite-syntax-s1">      "parts":[{</span>
<span class="devsite-syntax-s1">        "text": "What is the meaning of life?"}]}, },</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">      "model": "models/gemini-embedding-001",</span>
<span class="devsite-syntax-s1">      "content": {</span>
<span class="devsite-syntax-s1">      "parts":[{</span>
<span class="devsite-syntax-s1">        "text": "How much wood would a woodchuck chuck?"}]}, },</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">      "model": "models/gemini-embedding-001",</span>
<span class="devsite-syntax-s1">      "content": {</span>
<span class="devsite-syntax-s1">      "parts":[{</span>
<span class="devsite-syntax-s1">        "text": "How does the brain work?"}]}, }, ]}'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>grep<span class="devsite-syntax-w"> </span>-C<span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">5</span><span class="devsite-syntax-w"> </span>values<div class="devsite-github-link nocode no-select nocontent"><a target="_top" href="https://github.com/google-gemini/api-examples/blob/51979868abf95d062a149b62af92854b2a24f005/rest/embed.sh#L16-L34" class="gc-analytics-event" data-category="github_link" data-label="google-gemini/api-examples/rest/embed.sh#batch_embed_contents" data-code-snippet="true" data-git-revision="HEAD" data-github-path="google-gemini/api-examples/rest/embed.sh" data-indented-block="" data-regexp="" data-region-tag="batch_embed_contents">embed.sh</a></div></code></pre></devsite-code>
</div>



























            </section>
</devsite-selector>
</div>
</div>
<div class="column-container">
<div class="reference">
<section id="body.response_body">
<h3 id="response-body_1" data-text="Response body" tabindex="-1">Response body</h3>
<section id="body.BatchEmbedContentsResponse.description">
<p>The response to a <code translate="no" dir="ltr">BatchEmbedContentsRequest</code>.</p>
<p>If successful, the response body contains data with the following structure:</p>
</section>
<section id="body.BatchEmbedContentsResponse.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="body.BatchEmbedContentsResponse.FIELDS.embeddings">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">embeddings[]</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.ContentEmbedding">ContentEmbedding</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The embeddings for each request, in the same order as provided in the batch request.</p>
</div>
</div>
</section>
<section id="body.BatchEmbedContentsResponse.FIELDS.usage_metadata">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">usageMetadata</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.EmbeddingUsageMetadata">EmbeddingUsageMetadata</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The usage metadata for the request.</p>
</div>
</div>
</section>
</section>
</section>
</div>
<div class="second-column">
<section id="body.BatchEmbedContentsResponse.SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"embeddings"</span><span class="pun">: </span><span class="pun">[</span>
    <span class="pun">{</span>
      <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.ContentEmbedding">ContentEmbedding</a></code>)</span>
    <span class="pun">}</span>
  <span class="pun">]</span><span class="pun">,</span>
  <span class="str">"usageMetadata"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.EmbeddingUsageMetadata">EmbeddingUsageMetadata</a></code>)</span>
  <span class="pun">}</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
</section>
</div><div itemscope="" itemtype="http://developers.google.com/ReferenceObject"><h2 id="method:-models.asyncbatchembedcontent" data-text="Method: models.asyncBatchEmbedContent" tabindex="-1">Method: models.asyncBatchEmbedContent</h2><a name="v1beta.models.asyncBatchEmbedContent"></a>
<meta content="asyncBatchEmbedContent" itemprop="name"/>
<meta content="/api/rest/v1beta/models/asyncBatchEmbedContent" itemprop="path"/>
<section class="prototype" id="/api/rest/v1beta/models/asyncBatchEmbedContent">
<ul class="toc">
<li><a href="#body.HTTP_TEMPLATE">Endpoint</a></li><li><a href="#body.PATH_PARAMETERS">Path parameters</a></li><li><a href="#body.request_body">Request body</a>
<ul>
<li><a href="#body.request_body.SCHEMA_REPRESENTATION">JSON representation</a>
<ul>
<li><a href="#body.request_body.SCHEMA_REPRESENTATION.batch.SCHEMA_REPRESENTATION">JSON representation</a></li><li><a href="#body.request_body.SCHEMA_REPRESENTATION.batch.SCHEMA_REPRESENTATION_1">JSON representation</a></li><li><a href="#body.request_body.SCHEMA_REPRESENTATION.batch.SCHEMA_REPRESENTATION_2">JSON representation</a></li>
</ul>
</li>
</ul>
</li><li><a href="#body.response_body">Response body</a></li><li><a href="#body.aspect">Authorization scopes</a></li>
</ul>
<section id="google.ai.generativelanguage.v1beta.BatchService.AsyncBatchEmbedContent">
</section>
<section id="description">
<p>Enqueues a batch of <code translate="no" dir="ltr">models.embedContent</code> requests for batch processing. We have a <code translate="no" dir="ltr">models.batchEmbedContents</code> handler in <code translate="no" dir="ltr">GenerativeService</code>, but it was synchronized. So we name this one to be <code translate="no" dir="ltr">Async</code> to avoid confusion.</p>
</section>
<div class="column-container">
<div class="reference">
<section id="body.HTTP_TEMPLATE">
<h3 id="endpoint_2" data-text="Endpoint" tabindex="-1">Endpoint</h3>
<span class="endpoint">
<span class="http-method">
                post
              </span>
<span class="endpoint-url">
<code translate="no" dir="ltr">https:<wbr/>/<wbr/>/generativelanguage.googleapis.com<wbr/>/v1beta<wbr/>/{batch.model=models<wbr/>/*}:asyncBatchEmbedContent</code>
</span>
</span>
<br/>
<span>

</span>
</section>
<section id="body.PATH_PARAMETERS">
<h3 id="path-parameters_2" data-text="Path parameters" tabindex="-1">Path parameters</h3>
<section id="body.PATH_PARAMETERS.model">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.model</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Required. The name of the <code translate="no" dir="ltr">Model</code> to use for generating the completion.</p><p>Format: <code translate="no" dir="ltr">models/{model}</code>. It takes the form <code translate="no" dir="ltr">models/{model}</code>.</p>
</div>
</div>
</section>
</section>
<section id="body.request_body">
<h3 id="request-body_2" data-text="Request body" tabindex="-1">Request body</h3>
<p>The request body contains data with the following structure:</p>
<section id="body.request_body.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="body.request_body.FIELDS.name">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.name</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Output only. Identifier. Resource name of the batch.</p><p>Format: <code translate="no" dir="ltr">batches/{batchId}</code>.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.display_name">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.displayName</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Required. The user-defined name of this batch.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.input_config">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.inputConfig</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InputEmbedContentConfig">InputEmbedContentConfig</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Required. Input configuration of the instances on which batch processing are performed.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.output">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.output</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#EmbedContentBatchOutput">EmbedContentBatchOutput</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The output of the batch request.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.create_time">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.createTime</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<code translate="no" dir="ltr"><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp">Timestamp</a></code> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The time at which the batch was created.</p><p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.end_time">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.endTime</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<code translate="no" dir="ltr"><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp">Timestamp</a></code> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The time at which the batch processing completed.</p><p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.update_time">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.updateTime</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<code translate="no" dir="ltr"><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp">Timestamp</a></code> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The time at which the batch was last updated.</p><p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.batch_stats">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.batchStats</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#EmbedContentBatchStats">EmbedContentBatchStats</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. Stats about the batch.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.state">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.state</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">enum (<code translate="no" dir="ltr"><a href="/api/batch-api#v1beta.BatchState">BatchState</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The state of the batch.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.priority">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.priority</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<a href="https://developers.google.com/discovery/v1/type-format">int64</a> format)</code>
</span>
</div>
<div class="field-description">
<p>Optional. The priority of the batch. Batches with a higher priority value will be processed before batches with a lower priority value. Negative values are allowed. Default is 0.</p>
</div>
</div>
</section>
<section id="body.request_body.FIELDS.uris">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batch.webhookConfig.uris[]</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Optional. If set, these webhook URIs will be used for webhook events instead of the registered webhooks.</p>
</div>
</div>
</section>
</section>
</section>
</div>
</div>
<div class="column-container">
<div class="reference">
<section id="body.response_body">
<h3 id="response-body_2" data-text="Response body" tabindex="-1">Response body</h3>
<p>If successful, the response body contains an instance of <code translate="no" dir="ltr"><a href="/api/batch-api#Operation">Operation</a></code>.</p>
</section>
</div>
</div>
</section>
</div><div itemscope="" itemtype="http://developers.google.com/ReferenceObject"><h2 id="embedcontentresponse" data-text="EmbedContentResponse" tabindex="-1">EmbedContentResponse</h2><a name="v1beta.EmbedContentResponse"></a>
<meta content="EmbedContentResponse" itemprop="name"/>
<meta content="/api/rest/v1beta/EmbedContentResponse" itemprop="path"/>
<section class="prototype" id="/api/rest/v1beta/EmbedContentResponse">
<ul class="toc">
<li><a href="#SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
<div class="column-container">
<div class="reference">
<section id="description">
<p>The response to an <code translate="no" dir="ltr">EmbedContentRequest</code>.</p>
</section>
<section id="FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="FIELDS.embedding">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">embedding</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.ContentEmbedding">ContentEmbedding</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The embedding generated from the input content.</p>
</div>
</div>
</section>
<section id="FIELDS.usage_metadata">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">usageMetadata</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.EmbeddingUsageMetadata">EmbeddingUsageMetadata</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The usage metadata for the request.</p>
</div>
</div>
</section>
</section>
</div>
<div class="second-column">
<section id="SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"embedding"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.ContentEmbedding">ContentEmbedding</a></code>)</span>
  <span class="pun">}</span><span class="pun">,</span>
  <span class="str">"usageMetadata"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.EmbeddingUsageMetadata">EmbeddingUsageMetadata</a></code>)</span>
  <span class="pun">}</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
</section>
</div><div itemscope="" itemtype="http://developers.google.com/ReferenceObject"><h2 id="contentembedding" data-text="ContentEmbedding" tabindex="-1">ContentEmbedding</h2><a name="v1beta.ContentEmbedding"></a>
<meta content="ContentEmbedding" itemprop="name"/>
<meta content="/api/rest/v1beta/ContentEmbedding" itemprop="path"/>
<section class="prototype" id="/api/rest/v1beta/ContentEmbedding">
<ul class="toc">
<li><a href="#SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
<div class="column-container">
<div class="reference">
<section id="description">
<p>A list of floats representing an embedding.</p>
</section>
<section id="FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="FIELDS.values">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">values[]</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">number</code>
</span>
</div>
<div class="field-description">
<p>The embedding values. This is for 3P users only and will not be populated for 1P calls.</p>
</div>
</div>
</section>
<section id="FIELDS.shape">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">shape[]</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">integer</code>
</span>
</div>
<div class="field-description">
<p>This field stores the soft tokens tensor frame shape (e.g. [1, 1, 256, 2048]).</p>
</div>
</div>
</section>
</section>
</div>
<div class="second-column">
<section id="SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"values"</span><span class="pun">: </span><span class="pun">[</span>
    <span class="kwd">number</span>
  <span class="pun">]</span><span class="pun">,</span>
  <span class="str">"shape"</span><span class="pun">: </span><span class="pun">[</span>
    <span class="kwd">integer</span>
  <span class="pun">]</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
</section>
</div><div itemscope="" itemtype="http://developers.google.com/ReferenceObject"><h2 id="tasktype" data-text="TaskType" tabindex="-1">TaskType</h2><a name="v1beta.TaskType"></a>
<meta content="TaskType" itemprop="name"/>
<meta content="/api/rest/v1beta/TaskType" itemprop="path"/>
<section id="/api/rest/v1beta/TaskType">
<section id="description">
<p>Type of task for which the embedding will be used.</p>
</section>
<section id="ENUM_VALUES">
<table class="constants responsive fixed" id="ENUM_VALUES-table">
<colgroup>
<col width="25%"/>
<col/>
</colgroup>
<thead>
<tr>
<th colspan="2">Enums</th>
</tr>
</thead>
<tbody>
<tr id="ENUM_VALUES.TASK_TYPE_UNSPECIFIED">
<td><code class="apitype" translate="no" dir="ltr">TASK_TYPE_UNSPECIFIED</code></td>
<td>Unset value, which will default to one of the other enum values.</td>
</tr>
<tr id="ENUM_VALUES.RETRIEVAL_QUERY">
<td><code class="apitype" translate="no" dir="ltr">RETRIEVAL_QUERY</code></td>
<td>Specifies the given text is a query in a search/retrieval setting.</td>
</tr>
<tr id="ENUM_VALUES.RETRIEVAL_DOCUMENT">
<td><code class="apitype" translate="no" dir="ltr">RETRIEVAL_DOCUMENT</code></td>
<td>Specifies the given text is a document from the corpus being searched.</td>
</tr>
<tr id="ENUM_VALUES.SEMANTIC_SIMILARITY">
<td><code class="apitype" translate="no" dir="ltr">SEMANTIC_SIMILARITY</code></td>
<td>Specifies the given text will be used for STS.</td>
</tr>
<tr id="ENUM_VALUES.CLASSIFICATION">
<td><code class="apitype" translate="no" dir="ltr">CLASSIFICATION</code></td>
<td>Specifies that the given text will be classified.</td>
</tr>
<tr id="ENUM_VALUES.CLUSTERING">
<td><code class="apitype" translate="no" dir="ltr">CLUSTERING</code></td>
<td>Specifies that the embeddings will be used for clustering.</td>
</tr>
<tr id="ENUM_VALUES.QUESTION_ANSWERING">
<td><code class="apitype" translate="no" dir="ltr">QUESTION_ANSWERING</code></td>
<td>Specifies that the given text will be used for question answering.</td>
</tr>
<tr id="ENUM_VALUES.FACT_VERIFICATION">
<td><code class="apitype" translate="no" dir="ltr">FACT_VERIFICATION</code></td>
<td>Specifies that the given text will be used for fact verification.</td>
</tr>
<tr id="ENUM_VALUES.CODE_RETRIEVAL_QUERY">
<td><code class="apitype" translate="no" dir="ltr">CODE_RETRIEVAL_QUERY</code></td>
<td>Specifies that the given text will be used for code retrieval.</td>
</tr>
</tbody>
</table>
</section>
</section>
</div><div itemscope="" itemtype="http://developers.google.com/ReferenceObject"><h2 id="embedcontentbatch" data-text="EmbedContentBatch" tabindex="-1">EmbedContentBatch</h2><a name="v1beta.EmbedContentBatch"></a>
<meta content="EmbedContentBatch" itemprop="name"/>
<meta content="/api/rest/v1beta/EmbedContentBatch" itemprop="path"/>
<section class="prototype" id="/api/rest/v1beta/EmbedContentBatch">
<ul class="toc">
<li><a href="#SCHEMA_REPRESENTATION">JSON representation</a></li><li><a href="#InputEmbedContentConfig">InputEmbedContentConfig</a>
<ul>
<li><a href="#InputEmbedContentConfig.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li><li><a href="#InlinedEmbedContentRequests">InlinedEmbedContentRequests</a>
<ul>
<li><a href="#InlinedEmbedContentRequests.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li><li><a href="#InlinedEmbedContentRequest">InlinedEmbedContentRequest</a>
<ul>
<li><a href="#InlinedEmbedContentRequest.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li><li><a href="#EmbedContentBatchOutput">EmbedContentBatchOutput</a>
<ul>
<li><a href="#EmbedContentBatchOutput.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li><li><a href="#InlinedEmbedContentResponses">InlinedEmbedContentResponses</a>
<ul>
<li><a href="#InlinedEmbedContentResponses.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li><li><a href="#InlinedEmbedContentResponse">InlinedEmbedContentResponse</a>
<ul>
<li><a href="#InlinedEmbedContentResponse.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li><li><a href="#EmbedContentBatchStats">EmbedContentBatchStats</a>
<ul>
<li><a href="#EmbedContentBatchStats.SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
</li>
</ul>
<div class="column-container">
<div class="reference">
<section id="description">
<p>A resource representing a batch of <code translate="no" dir="ltr">EmbedContent</code> requests.</p>
</section>
<section id="FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="FIELDS.model">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">model</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Required. The name of the <code translate="no" dir="ltr">Model</code> to use for generating the completion.</p><p>Format: <code translate="no" dir="ltr">models/{model}</code>.</p>
</div>
</div>
</section>
<section id="FIELDS.name">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">name</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Output only. Identifier. Resource name of the batch.</p><p>Format: <code translate="no" dir="ltr">batches/{batchId}</code>.</p>
</div>
</div>
</section>
<section id="FIELDS.display_name">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">displayName</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Required. The user-defined name of this batch.</p>
</div>
</div>
</section>
<section id="FIELDS.input_config">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">inputConfig</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InputEmbedContentConfig">InputEmbedContentConfig</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Required. Input configuration of the instances on which batch processing are performed.</p>
</div>
</div>
</section>
<section id="FIELDS.output">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">output</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#EmbedContentBatchOutput">EmbedContentBatchOutput</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The output of the batch request.</p>
</div>
</div>
</section>
<section id="FIELDS.create_time">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">createTime</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<code translate="no" dir="ltr"><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp">Timestamp</a></code> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The time at which the batch was created.</p><p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p>
</div>
</div>
</section>
<section id="FIELDS.end_time">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">endTime</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<code translate="no" dir="ltr"><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp">Timestamp</a></code> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The time at which the batch processing completed.</p><p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p>
</div>
</div>
</section>
<section id="FIELDS.update_time">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">updateTime</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<code translate="no" dir="ltr"><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp">Timestamp</a></code> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The time at which the batch was last updated.</p><p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p>
</div>
</div>
</section>
<section id="FIELDS.batch_stats">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">batchStats</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#EmbedContentBatchStats">EmbedContentBatchStats</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. Stats about the batch.</p>
</div>
</div>
</section>
<section id="FIELDS.state">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">state</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">enum (<code translate="no" dir="ltr"><a href="/api/batch-api#v1beta.BatchState">BatchState</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The state of the batch.</p>
</div>
</div>
</section>
<section id="FIELDS.priority">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">priority</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<a href="https://developers.google.com/discovery/v1/type-format">int64</a> format)</code>
</span>
</div>
<div class="field-description">
<p>Optional. The priority of the batch. Batches with a higher priority value will be processed before batches with a lower priority value. Negative values are allowed. Default is 0.</p>
</div>
</div>
</section>
</section>
</div>
<div class="second-column">
<section id="SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"model"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"name"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"displayName"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"inputConfig"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InputEmbedContentConfig">InputEmbedContentConfig</a></code>)</span>
  <span class="pun">}</span><span class="pun">,</span>
  <span class="str">"output"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#EmbedContentBatchOutput">EmbedContentBatchOutput</a></code>)</span>
  <span class="pun">}</span><span class="pun">,</span>
  <span class="str">"createTime"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"endTime"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"updateTime"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"batchStats"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#EmbedContentBatchStats">EmbedContentBatchStats</a></code>)</span>
  <span class="pun">}</span><span class="pun">,</span>
  <span class="str">"state"</span><span class="pun">: </span><span class="kwd">enum (<code translate="no" dir="ltr"><a href="/api/batch-api#v1beta.BatchState">BatchState</a></code>)</span><span class="pun">,</span>
  <span class="str">"priority"</span><span class="pun">: </span><span class="kwd">string</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
<h2 id="InputEmbedContentConfig" data-text="InputEmbedContentConfig" tabindex="-1">InputEmbedContentConfig</h2>
<div class="column-container">
<div class="reference">
<section id="InputEmbedContentConfig.description">
<p>Configures the input to the batch request.</p>
</section>
<section id="InputEmbedContentConfig.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<div class="field-entry union-type">
<div class="signature">
<tr class="alt" id="InputEmbedContentConfig.FIELDS.source">
<span class="field-name">
<td><code translate="no" dir="ltr">source</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">Union type</code>
</span>
</tr>
<div class="union-type-preamble">
<div>Required. The source of the input. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:</div>
<section id="InputEmbedContentConfig.FIELDS.file_name">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">fileName</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>The name of the <code translate="no" dir="ltr">File</code> containing the input requests.</p>
</div>
</div>
</section>
<section id="InputEmbedContentConfig.FIELDS.requests">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">requests</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InlinedEmbedContentRequests">InlinedEmbedContentRequests</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>The requests to be processed in the batch.</p>
</div>
</div>
</section>
<div>End of mutually exclusive fields.</div>
</div>
</div>
</div>
</section>
</div>
<div class="second-column">
<section id="InputEmbedContentConfig.SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>

  <span class="com">// source</span>
  <span class="str">"fileName"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"requests"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InlinedEmbedContentRequests">InlinedEmbedContentRequests</a></code>)</span>
  <span class="pun">}</span>
  <span class="com">// Union type</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
<h2 id="InlinedEmbedContentRequests" data-text="InlinedEmbedContentRequests" tabindex="-1">InlinedEmbedContentRequests</h2>
<div class="column-container">
<div class="reference">
<section id="InlinedEmbedContentRequests.description">
<p>The requests to be processed in the batch if provided as part of the batch creation request.</p>
</section>
<section id="InlinedEmbedContentRequests.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="InlinedEmbedContentRequests.FIELDS.requests">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">requests[]</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InlinedEmbedContentRequest">InlinedEmbedContentRequest</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Required. The requests to be processed in the batch.</p>
</div>
</div>
</section>
</section>
</div>
<div class="second-column">
<section id="InlinedEmbedContentRequests.SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"requests"</span><span class="pun">: </span><span class="pun">[</span>
    <span class="pun">{</span>
      <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InlinedEmbedContentRequest">InlinedEmbedContentRequest</a></code>)</span>
    <span class="pun">}</span>
  <span class="pun">]</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
<h2 id="InlinedEmbedContentRequest" data-text="InlinedEmbedContentRequest" tabindex="-1">InlinedEmbedContentRequest</h2>
<div class="column-container">
<div class="reference">
<section id="InlinedEmbedContentRequest.description">
<p>The request to be processed in the batch.</p>
</section>
<section id="InlinedEmbedContentRequest.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="InlinedEmbedContentRequest.FIELDS.request">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">request</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/batch-api#EmbedContentRequest">EmbedContentRequest</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Required. The request to be processed in the batch.</p>
</div>
</div>
</section>
<section id="InlinedEmbedContentRequest.FIELDS.metadata">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">metadata</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#struct">Struct</a></code> format)</code>
</span>
</div>
<div class="field-description">
<p>Optional. The metadata to be associated with the request.</p>
</div>
</div>
</section>
</section>
</div>
<div class="second-column">
<section id="InlinedEmbedContentRequest.SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"request"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/batch-api#EmbedContentRequest">EmbedContentRequest</a></code>)</span>
  <span class="pun">}</span><span class="pun">,</span>
  <span class="str">"metadata"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object</span>
  <span class="pun">}</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
<h2 id="EmbedContentBatchOutput" data-text="EmbedContentBatchOutput" tabindex="-1">EmbedContentBatchOutput</h2>
<div class="column-container">
<div class="reference">
<section id="EmbedContentBatchOutput.description">
<p>The output of a batch request. This is returned in the <code translate="no" dir="ltr">AsyncBatchEmbedContentResponse</code> or the <code translate="no" dir="ltr">EmbedContentBatch.output</code> field.</p>
</section>
<section id="EmbedContentBatchOutput.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<div class="field-entry union-type">
<div class="signature">
<tr class="alt" id="EmbedContentBatchOutput.FIELDS.output">
<span class="field-name">
<td><code translate="no" dir="ltr">output</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">Union type</code>
</span>
</tr>
<div class="union-type-preamble">
<div>The output of the batch request. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:</div>
<section id="EmbedContentBatchOutput.FIELDS.responses_file">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">responsesFile</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Output only. The file ID of the file containing the responses. The file will be a JSONL file with a single response per line. The responses will be <code translate="no" dir="ltr">EmbedContentResponse</code> messages formatted as JSON. The responses will be written in the same order as the input requests.</p>
</div>
</div>
</section>
<section id="EmbedContentBatchOutput.FIELDS.inlined_responses">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">inlinedResponses</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InlinedEmbedContentResponses">InlinedEmbedContentResponses</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The responses to the requests in the batch. Returned when the batch was built using inlined requests. The responses will be in the same order as the input requests.</p>
</div>
</div>
</section>
<div>End of mutually exclusive fields.</div>
</div>
</div>
</div>
</section>
</div>
<div class="second-column">
<section id="EmbedContentBatchOutput.SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>

  <span class="com">// output</span>
  <span class="str">"responsesFile"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"inlinedResponses"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InlinedEmbedContentResponses">InlinedEmbedContentResponses</a></code>)</span>
  <span class="pun">}</span>
  <span class="com">// Union type</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
<h2 id="InlinedEmbedContentResponses" data-text="InlinedEmbedContentResponses" tabindex="-1">InlinedEmbedContentResponses</h2>
<div class="column-container">
<div class="reference">
<section id="InlinedEmbedContentResponses.description">
<p>The responses to the requests in the batch.</p>
</section>
<section id="InlinedEmbedContentResponses.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="InlinedEmbedContentResponses.FIELDS.inlined_responses">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">inlinedResponses[]</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InlinedEmbedContentResponse">InlinedEmbedContentResponse</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The responses to the requests in the batch.</p>
</div>
</div>
</section>
</section>
</div>
<div class="second-column">
<section id="InlinedEmbedContentResponses.SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"inlinedResponses"</span><span class="pun">: </span><span class="pun">[</span>
    <span class="pun">{</span>
      <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#InlinedEmbedContentResponse">InlinedEmbedContentResponse</a></code>)</span>
    <span class="pun">}</span>
  <span class="pun">]</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
<h2 id="InlinedEmbedContentResponse" data-text="InlinedEmbedContentResponse" tabindex="-1">InlinedEmbedContentResponse</h2>
<div class="column-container">
<div class="reference">
<section id="InlinedEmbedContentResponse.description">
<p>The response to a single request in the batch.</p>
</section>
<section id="InlinedEmbedContentResponse.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="InlinedEmbedContentResponse.FIELDS.metadata">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">metadata</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#struct">Struct</a></code> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The metadata associated with the request.</p>
</div>
</div>
</section>
<div class="field-entry union-type">
<div class="signature">
<tr class="alt" id="InlinedEmbedContentResponse.FIELDS.output">
<span class="field-name">
<td><code translate="no" dir="ltr">output</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">Union type</code>
</span>
</tr>
<div class="union-type-preamble">
<div>The output of the request. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:</div>
<section id="InlinedEmbedContentResponse.FIELDS.error">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">error</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/files#v1beta.Status">Status</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The error encountered while processing the request.</p>
</div>
</div>
</section>
<section id="InlinedEmbedContentResponse.FIELDS.response">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">response</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.EmbedContentResponse">EmbedContentResponse</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The response to the request.</p>
</div>
</div>
</section>
<div>End of mutually exclusive fields.</div>
</div>
</div>
</div>
</section>
</div>
<div class="second-column">
<section id="InlinedEmbedContentResponse.SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"metadata"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object</span>
  <span class="pun">}</span><span class="pun">,</span>

  <span class="com">// output</span>
  <span class="str">"error"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/files#v1beta.Status">Status</a></code>)</span>
  <span class="pun">}</span><span class="pun">,</span>
  <span class="str">"response"</span><span class="pun">: </span><span class="pun">{</span>
    <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.EmbedContentResponse">EmbedContentResponse</a></code>)</span>
  <span class="pun">}</span>
  <span class="com">// Union type</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
<h2 id="EmbedContentBatchStats" data-text="EmbedContentBatchStats" tabindex="-1">EmbedContentBatchStats</h2>
<div class="column-container">
<div class="reference">
<section id="EmbedContentBatchStats.description">
<p>Stats about the batch.</p>
</section>
<section id="EmbedContentBatchStats.FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="EmbedContentBatchStats.FIELDS.request_count">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">requestCount</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<a href="https://developers.google.com/discovery/v1/type-format">int64</a> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The number of requests in the batch.</p>
</div>
</div>
</section>
<section id="EmbedContentBatchStats.FIELDS.successful_request_count">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">successfulRequestCount</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<a href="https://developers.google.com/discovery/v1/type-format">int64</a> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The number of requests that were successfully processed.</p>
</div>
</div>
</section>
<section id="EmbedContentBatchStats.FIELDS.failed_request_count">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">failedRequestCount</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<a href="https://developers.google.com/discovery/v1/type-format">int64</a> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The number of requests that failed to be processed.</p>
</div>
</div>
</section>
<section id="EmbedContentBatchStats.FIELDS.pending_request_count">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">pendingRequestCount</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string (<a href="https://developers.google.com/discovery/v1/type-format">int64</a> format)</code>
</span>
</div>
<div class="field-description">
<p>Output only. The number of requests that are still pending processing.</p>
</div>
</div>
</section>
</section>
</div>
<div class="second-column">
<section id="EmbedContentBatchStats.SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"requestCount"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"successfulRequestCount"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"failedRequestCount"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"pendingRequestCount"</span><span class="pun">: </span><span class="kwd">string</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
</section>
</div><div itemscope="" itemtype="http://developers.google.com/ReferenceObject"><h2 id="embedcontentconfig" data-text="EmbedContentConfig" tabindex="-1">EmbedContentConfig</h2><a name="v1beta.EmbedContentConfig"></a>
<meta content="EmbedContentConfig" itemprop="name"/>
<meta content="/api/rest/v1beta/EmbedContentConfig" itemprop="path"/>
<section class="prototype" id="/api/rest/v1beta/EmbedContentConfig">
<ul class="toc">
<li><a href="#SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
<div class="column-container">
<div class="reference">
<section id="description">
<p>Configurations for the EmbedContent request.</p>
</section>
<section id="FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="FIELDS.title">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">title</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">string</code>
</span>
</div>
<div class="field-description">
<p>Optional. The title for the text.</p>
</div>
</div>
</section>
<section id="FIELDS.task_type">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">taskType</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">enum (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.TaskType">TaskType</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Optional. The task type of the embedding.</p>
</div>
</div>
</section>
<section id="FIELDS.auto_truncate">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">autoTruncate</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">boolean</code>
</span>
</div>
<div class="field-description">
<p>Optional. Whether to silently truncate the input content if it's longer than the maximum sequence length.</p>
</div>
</div>
</section>
<section id="FIELDS.output_dimensionality">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">outputDimensionality</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">integer</code>
</span>
</div>
<div class="field-description">
<p>Optional. Reduced dimension for the output embedding. If set, excessive values in the output embedding are truncated from the end.</p>
</div>
</div>
</section>
<section id="FIELDS.document_ocr">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">documentOcr</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">boolean</code>
</span>
</div>
<div class="field-description">
<p>Optional. Whether to enable OCR for document content.</p>
</div>
</div>
</section>
<section id="FIELDS.audio_track_extraction">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">audioTrackExtraction</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">boolean</code>
</span>
</div>
<div class="field-description">
<p>Optional. Whether to extract audio from video content.</p>
</div>
</div>
</section>
</section>
</div>
<div class="second-column">
<section id="SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"title"</span><span class="pun">: </span><span class="kwd">string</span><span class="pun">,</span>
  <span class="str">"taskType"</span><span class="pun">: </span><span class="kwd">enum (<code translate="no" dir="ltr"><a href="/api/embeddings#v1beta.TaskType">TaskType</a></code>)</span><span class="pun">,</span>
  <span class="str">"autoTruncate"</span><span class="pun">: </span><span class="kwd">boolean</span><span class="pun">,</span>
  <span class="str">"outputDimensionality"</span><span class="pun">: </span><span class="kwd">integer</span><span class="pun">,</span>
  <span class="str">"documentOcr"</span><span class="pun">: </span><span class="kwd">boolean</span><span class="pun">,</span>
  <span class="str">"audioTrackExtraction"</span><span class="pun">: </span><span class="kwd">boolean</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
</div>
</div>
</section>
</div><div itemscope="" itemtype="http://developers.google.com/ReferenceObject"><h2 id="embeddingusagemetadata" data-text="EmbeddingUsageMetadata" tabindex="-1">EmbeddingUsageMetadata</h2><a name="v1beta.EmbeddingUsageMetadata"></a>
<meta content="EmbeddingUsageMetadata" itemprop="name"/>
<meta content="/api/rest/v1beta/EmbeddingUsageMetadata" itemprop="path"/>
<section class="prototype" id="/api/rest/v1beta/EmbeddingUsageMetadata">
<ul class="toc">
<li><a href="#SCHEMA_REPRESENTATION">JSON representation</a></li>
</ul>
<div class="column-container">
<div class="reference">
<section id="description">
<p>Metadata on the usage of the embedding request.</p>
</section>
<section id="FIELDS">
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<section id="FIELDS.prompt_token_count">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">promptTokenCount</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">integer</code>
</span>
</div>
<div class="field-description">
<p>Output only. Number of tokens in the prompt.</p>
</div>
</div>
</section>
<section id="FIELDS.prompt_token_details">
<div class="field-entry">
<div class="signature">
<span class="field-name">
<td><code translate="no" dir="ltr">promptTokenDetails[]</code></td>
</span>
<span class="field-type">
<code translate="no" dir="ltr">object (<code translate="no" dir="ltr"><a href="/api/generate-content#v1beta.ModalityTokenCount">ModalityTokenCount</a></code>)</code>
</span>
</div>
<div class="field-description">
<p>Output only. List of modalities that were processed in the request input.</p>
</div>
</div>
</section>
</section>
</div>
<div class="second-column">
<section id="SCHEMA_REPRESENTATION">
<table class="properties responsive fixed">
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin:0;padding:0;"><div></div><devsite-code><pre style="border: 0;margin: 0;" translate="no" dir="ltr" is-upgraded><span class="pun">{</span>
  <span class="str">"promptTokenCount"</span><span class="pun">: </span><span class="kwd">integer</span><span class="pun">,</span>
  <span class="str">"promptTokenDetails"</span><span class="pun">: </span><span class="pun">[</span>
    <span class="pun">{</span>
      <span class="kwd">object (<code translate="no" dir="ltr"><a href="/api/generate-content#v1beta.ModalityTokenCount">ModalityTokenCount</a></code>)</span>
    <span class="pun">}</span>
  <span class="pun">]</span>
<span class="pun">}</span></pre></devsite-code></td>
</tr>
</tbody>
</table>
</section>
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