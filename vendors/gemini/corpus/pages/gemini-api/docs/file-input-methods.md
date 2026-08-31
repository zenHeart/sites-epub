








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/googledevai/images/touchicon-180-new.png"><link rel="canonical" href="https://ai.google.dev/gemini-api/docs/file-input-methods"><link rel="search" type="application/opensearchdescription+xml"
            title="Google AI for Developers" href="https://ai.google.dev/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods" /><link rel="alternate" hreflang="x-default" href="https://ai.google.dev/gemini-api/docs/file-input-methods" /><link rel="alternate" hreflang="ar"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de" /><link rel="alternate" hreflang="he"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=id" /><link rel="alternate" hreflang="it"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi" /><link rel="alternate" hreflang="sq"
          href="https://ai.google.dev/gemini-api/docs/file-input-methods?hl=sq" /><title>File input methods &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers</title>

<meta property="og:title" content="File input methods &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers"><meta name="description" content="Get started building with Gemini&amp;#39;s multimodal capabilities in the Gemini API">
  <meta property="og:description" content="Get started building with Gemini&amp;#39;s multimodal capabilities in the Gemini API"><meta property="og:url" content="https://ai.google.dev/gemini-api/docs/file-input-methods"><meta property="og:image" content="https://ai.google.dev/static/site-assets/images/vision.png">
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
      File input methods<devsite-actions hidden data-nosnippet>
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



























































<p>This guide explains the different ways you can include media files such as
images, audio, video, and documents when making requests to the Gemini API.
The new methods are supported in all of the Gemini API endpoints, including
Batch, Interactions and Live API.
Choosing the right method depends on the size of your file, where your data is
stored, and how frequently you plan to use the file.</p>

<p>The simplest way to include a file as your input is to read a local file and
include it in a prompt. The following example shows how to read a local PDF
file. PDFs are limited to 50MB for this method. See the
<a href="#method-comparison">Input method comparison table</a> for a complete list of file
input types and limits.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">pathlib</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">base64</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">filepath</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">pathlib</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Path</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'my_local_file.pdf'</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">prompt</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"Summarize this document"</span>
<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"data"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">base64</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">b64encode</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">filepath</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">read_bytes</span><span class="devsite-syntax-p">())</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">decode</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'utf-8'</span><span class="devsite-syntax-p">),</span> <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"application/pdf"</span><span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">*</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">as</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'node:fs'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Summarize this document"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">filePath</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'my_local_file.pdf'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fs</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">readFileSync</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">filePath</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-nx">toString</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"base64"</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"application/pdf"</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
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
<section><h3 id="rest" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># Encode the local file to base64</span>
<span class="devsite-syntax-nv">B64_CONTENT</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>base64<span class="devsite-syntax-w"> </span>-w<span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">0</span><span class="devsite-syntax-w"> </span>my_local_file.pdf<span class="devsite-syntax-k">)</span>

curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Content-Type: application/json'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">    "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">    "input": [</span>
<span class="devsite-syntax-s1">      {"type": "text", "text": "Summarize this document"},</span>
<span class="devsite-syntax-s1">      {</span>
<span class="devsite-syntax-s1">        "type": "document",</span>
<span class="devsite-syntax-s1">        "data": "'</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">B64_CONTENT</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s1">'",</span>
<span class="devsite-syntax-s1">        "mime_type": "application/pdf"</span>
<span class="devsite-syntax-s1">      }</span>
<span class="devsite-syntax-s1">    ]</span>
<span class="devsite-syntax-s1">  }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="method-comparison" data-text="Input method comparison" tabindex="-1">Input method comparison</h2>

<p>The following table compares each input method with file limits and best use
cases. Note that the file size limit may vary depending on the file type and
model or tokenizer used to process the file.</p>

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Best for</th>
      <th>Max file size</th>
      <th>Persistence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Inline data</b></td>
      <td>Quick testing, small files, real-time applications.</td>
      <td>100 MB per request or payload <br> (<b>50 MB for PDFs</b>)</td>
      <td>None (sent with every request)</td>
    </tr>
    <tr>
      <td><b>File API upload</b></td>
      <td>Large files, files used multiple times.</td>
      <td>2 GB per file, <br> up to 20GB per project</td>
      <td>48 Hours</td>
    </tr>
    <tr>
      <td><b>File API GCS URI registration</b></td>
      <td>Large files already in Google Cloud Storage, files used multiple times.</td>
      <td>2 GB per file, no overall storage limits</td>
      <td>None (fetched per request). One time registration can give access for up to 30 days.</td>
    </tr>
    <tr>
      <td><b>External URLs</b></td>
      <td>Public data or data in cloud buckets (AWS, Azure, GCS) without re-uploading.</td>
      <td>100 MB per request/payload</td>
      <td>None (fetched per request)</td>
    </tr>
  </tbody>
</table>

<h2 id="inline-data" data-text="Inline data" tabindex="-1">Inline data</h2>

<p>For smaller files (under 100MB, or 50MB for PDFs), you can pass the data
directly in the request payload. This is the simplest method for quick tests or
applications handling real-time, transient data. You can provide data as
base64 encoded strings or by reading local files directly.</p>

<p>For an example of reading from a local file, see the example at the beginning of
this page.</p>

<h3 id="fetch-from-a-url" data-text="Fetch from a URL" tabindex="-1">Fetch from a URL</h3>

<p>You can also fetch a file from a URL, convert it to bytes, and include it in the
input.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_1" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>
<span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">httpx</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">doc_url</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"</span>
<span class="devsite-syntax-n">doc_data</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">httpx</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">get</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">doc_url</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">content</span>

<span class="devsite-syntax-n">prompt</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"Summarize this document"</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"data"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">base64</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">b64encode</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">doc_data</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">decode</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'utf-8'</span><span class="devsite-syntax-p">),</span> <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"application/pdf"</span><span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_1" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">docUrl</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf'</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Summarize this document"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">pdfResp</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">fetch</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">docUrl</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">then</span><span class="devsite-syntax-p">((</span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span>&gt;<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">response</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">arrayBuffer</span><span class="devsite-syntax-p">());</span>

<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">data</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">Buffer</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">pdfResp</span><span class="devsite-syntax-p">).</span><span class="devsite-syntax-nx">toString</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s2">"base64"</span><span class="devsite-syntax-p">),</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"application/pdf"</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
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
<section><h3 id="rest_1" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-nv">DOC_URL</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"</span>
<span class="devsite-syntax-nv">PROMPT</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"Summarize this document"</span>
<span class="devsite-syntax-nv">DISPLAY_NAME</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"base64_pdf"</span>

<span class="devsite-syntax-c1"># Download the PDF</span>
wget<span class="devsite-syntax-w"> </span>-O<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">DISPLAY_NAME</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">.pdf"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">DOC_URL</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>

<span class="devsite-syntax-c1"># Check for FreeBSD base64 and set flags accordingly</span>
<span class="devsite-syntax-k">if</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">[[</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-k">$(</span>base64<span class="devsite-syntax-w"> </span>--version<span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2&gt;&amp;1</span><span class="devsite-syntax-k">)</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span>*<span class="devsite-syntax-s2">"FreeBSD"</span>*<span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">]]</span><span class="devsite-syntax-p">;</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">then</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nv">B64FLAGS</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"--input"</span>
<span class="devsite-syntax-k">else</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nv">B64FLAGS</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"-w0"</span>
<span class="devsite-syntax-k">fi</span>

<span class="devsite-syntax-c1"># Base64 encode the PDF</span>
<span class="devsite-syntax-nv">ENCODED_PDF</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>base64<span class="devsite-syntax-w"> </span><span class="devsite-syntax-nv">$B64FLAGS</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">DISPLAY_NAME</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">.pdf"</span><span class="devsite-syntax-k">)</span>

<span class="devsite-syntax-c1"># Create JSON payload file</span>
cat<span class="devsite-syntax-w"> </span>&lt;&lt;EOF<span class="devsite-syntax-w"> &gt; </span>payload.json
<span class="devsite-syntax-o">{</span>
<span class="devsite-syntax-s2">"model"</span>:<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span>,
<span class="devsite-syntax-s2">"input"</span>:<span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">[</span>
<span class="devsite-syntax-o">{</span><span class="devsite-syntax-s2">"type"</span>:<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"document"</span>,<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"data"</span>:<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">ENCODED_PDF</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>,<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"mime_type"</span>:<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"application/pdf"</span><span class="devsite-syntax-o">}</span>,
<span class="devsite-syntax-o">{</span><span class="devsite-syntax-s2">"type"</span>:<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span>,<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span>:<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">PROMPT</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-o">}</span>
<span class="devsite-syntax-o">]</span>
<span class="devsite-syntax-o">}</span>
EOF

<span class="devsite-syntax-c1"># Generate content using interactions</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Content-Type: application/json'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span>@payload.json<span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null<span class="devsite-syntax-w"> &gt; </span>response.json

cat<span class="devsite-syntax-w"> </span>response.json
<span class="devsite-syntax-nb">echo</span>

jq<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">".outputs[] | select(.type == \"text\") | .text"</span><span class="devsite-syntax-w"> </span>response.json
</code></pre></devsite-code></section>
</devsite-selector></div>
<h2 id="file-api" data-text="Gemini File API" tabindex="-1">Gemini File API</h2>

<p>The File API is designed for larger files (up to 2GB) or files you intend to
use in multiple requests.</p>

<h3 id="standard-file-upload" data-text="Standard file upload" tabindex="-1">Standard file upload</h3>

<p>Upload a local file to the Gemini API. Files uploaded this way are stored
temporarily (48 hours) and processed for efficient retrieval by the model.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_2" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">doc_file</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">files</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">upload</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">file</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"path/to/your/sample.pdf"</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-n">prompt</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"Summarize this document"</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"uri"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">doc_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">uri</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">doc_file</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_2" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>
<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Summarize this document"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">filePath</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"path/to/your/sample.pdf"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">myfile</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">files</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">upload</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">file</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">filePath</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">config</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"application/pdf"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">myfile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">myfile</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
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
<section><h3 id="rest_2" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-nv">FILE_PATH</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"path/to/sample.pdf"</span>
<span class="devsite-syntax-nv">MIME_TYPE</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>file<span class="devsite-syntax-w"> </span>-b<span class="devsite-syntax-w"> </span>--mime-type<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">FILE_PATH</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-k">)</span>
<span class="devsite-syntax-nv">NUM_BYTES</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>wc<span class="devsite-syntax-w"> </span>-c<span class="devsite-syntax-w"> &lt; </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">FILE_PATH</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-k">)</span>
<span class="devsite-syntax-nv">DISPLAY_NAME</span><span class="devsite-syntax-o">=</span>DOCUMENT

<span class="devsite-syntax-nv">tmp_header_file</span><span class="devsite-syntax-o">=</span>upload-header.tmp

<span class="devsite-syntax-c1"># Initial resumable request defining metadata.</span>
curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/upload/v1beta/files"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-D<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">tmp_header_file</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Protocol: resumable"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Command: start"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Header-Content-Length: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">NUM_BYTES</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Header-Content-Type: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">MIME_TYPE</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Type: application/json"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"{'file': {'display_name': '</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">DISPLAY_NAME</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">'}}"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null

<span class="devsite-syntax-nv">upload_url</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>grep<span class="devsite-syntax-w"> </span>-i<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-upload-url: "</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">tmp_header_file</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>cut<span class="devsite-syntax-w"> </span>-d<span class="devsite-syntax-s2">" "</span><span class="devsite-syntax-w"> </span>-f2<span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">|</span><span class="devsite-syntax-w"> </span>tr<span class="devsite-syntax-w"> </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"\r"</span><span class="devsite-syntax-k">)</span>
rm<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">tmp_header_file</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span>

<span class="devsite-syntax-c1"># Upload the actual bytes.</span>
curl<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">upload_url</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Content-Length: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">NUM_BYTES</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Offset: 0"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"X-Goog-Upload-Command: upload, finalize"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--data-binary<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">FILE_PATH</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-m">2</span>&gt;<span class="devsite-syntax-w"> </span>/dev/null<span class="devsite-syntax-w"> &gt; </span>file_info.json

<span class="devsite-syntax-nv">file_uri</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>jq<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">".file.uri"</span><span class="devsite-syntax-w"> </span>file_info.json<span class="devsite-syntax-k">)</span>

<span class="devsite-syntax-c1"># Now use in an interaction</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-api-key: </span><span class="devsite-syntax-nv">$GEMINI_API_KEY</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Content-Type: application/json'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">      "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">      "input": [</span>
<span class="devsite-syntax-s1">        {"type": "text", "text": "Summarize this document"},</span>
<span class="devsite-syntax-s1">        {"type": "document", "uri": '</span><span class="devsite-syntax-nv">$file_uri</span><span class="devsite-syntax-s1">', "mime_type": "'</span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">MIME_TYPE</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s1">'"}</span>
<span class="devsite-syntax-s1">      ]</span>
<span class="devsite-syntax-s1">    }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="registration" data-text="Register Google Cloud Storage files" tabindex="-1">Register Google Cloud Storage files</h3>

<p>If your data is already in Google Cloud Storage, you don&#39;t need to
download and re-upload it. You can register it directly with the File API.</p>
<ol>
<li><p>Grant <strong>Service Agent</strong> access to each bucket</p>

<ol>
<li><p>Enable the Gemini API in your Google Cloud project.</p></li>
<li><p>Create the Service Agent:</p>

<p><code translate="no" dir="ltr">gcloud beta services identity create --service=generativelanguage.googleapis.com --project=&lt;your_project&gt;</code></p></li>
<li><p><strong>Grant the Gemini API Service Agent permissions</strong> to read your storage
buckets.</p>

<p>The user needs to assign the <code translate="no" dir="ltr">Storage Object Viewer</code>
<a href="https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectViewer">IAM role</a>
to this service agent on the specific storage buckets they intend to use.</p></li>
</ol>

<p>This access doesn&#39;t expire by default, but can be changed at any time. You can
also use the
<a href="https://cloud.google.com/iam/docs/write-policy-client-libraries">Google Cloud Storage IAM SDK</a>
commands to grant permissions.</p></li>
<li><p>Authenticate your service</p>

<p><strong>Prerequisites</strong></p>

<ul>
<li>Enable API</li>
<li>Create a service account or agent with appropriate permissions.</li>
</ul>

<p>You first need to authenticate as the service that has storage object viewer
permissions. How this happens depends on the environment in which your file
management code will be running.</p>

<p><strong>Outside of Google Cloud</strong></p>

<p>If your code is running from outside of Google Cloud, such as your desktop,
download the account credentials from the Google Cloud Console with the
following steps:</p>

<ol>
<li>Browse to the <a href="https://console.cloud.google.com/iam-admin/serviceaccounts">Service Account console</a></li>
<li>Select the relevant service account</li>
<li>Select the <strong>Keys</strong> tab and choose <strong>Add key, Create new key</strong></li>
<li>Choose the <strong>JSON</strong> key type, and note where the file was downloaded to on
your machine.</li>
</ol>

<p>For more details, see the official Google Cloud documentation on
<a href="https://docs.cloud.google.com/iam/docs/keys-create-delete">service account key management</a>.</p>

<p>Then use the following commands to authenticate. These commands assume your
service account file is in the current directory, named
<code translate="no" dir="ltr">service-account.json</code>.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_3" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.oauth2.service_account</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">Credentials</span>

<span class="devsite-syntax-n">GCS_READ_SCOPES</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[</span>
  <span class="devsite-syntax-s1">'https://www.googleapis.com/auth/devstorage.read_only'</span><span class="devsite-syntax-p">,</span>
  <span class="devsite-syntax-s1">'https://www.googleapis.com/auth/cloud-platform'</span>
<span class="devsite-syntax-p">]</span>

<span class="devsite-syntax-n">SERVICE_ACCOUNT_FILE</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s1">'service-account.json'</span>

<span class="devsite-syntax-n">credentials</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">Credentials</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">from_service_account_file</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">SERVICE_ACCOUNT_FILE</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">scopes</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">GCS_READ_SCOPES</span>
<span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_3" data-text="Javascript" tabindex="-1">Javascript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleAuth</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">require</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'google-auth-library'</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GCS_READ_SCOPES</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-s1">'https://www.googleapis.com/auth/devstorage.read_only'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-s1">'https://www.googleapis.com/auth/cloud-platform'</span>
<span class="devsite-syntax-p">];</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">SERVICE_ACCOUNT_FILE</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'service-account.json'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">auth</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleAuth</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">keyFile</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">SERVICE_ACCOUNT_FILE</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">scopes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GCS_READ_SCOPES</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
<section><h3 id="cli" data-text="CLI" tabindex="-1">CLI</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">gcloud<span class="devsite-syntax-w"> </span>auth<span class="devsite-syntax-w"> </span>application-default<span class="devsite-syntax-w"> </span>login<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--client-id-file<span class="devsite-syntax-o">=</span>service-account.json<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">  </span>--scopes<span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<p><strong>On Google Cloud</strong></p>

<p>If you are running directly in Google Cloud, for example by using <a href="https://cloud.google.com/functions">Cloud
Run functions</a> or a
<a href="https://cloud.google.com/products/compute">Compute Engine instance</a>, you will
have implicit credentials but will need to re-authenticate to grant the
appropriate scopes.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_4" data-text="Python" tabindex="-1">Python</h3><p>This code expects that the service is running in an environment where
<a href="https://docs.cloud.google.com/docs/authentication/application-default-credentials">Application Default Credentials</a>
can be obtained automatically, such as Cloud Run or Compute Engine.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google.auth</span>

<span class="devsite-syntax-n">GCS_READ_SCOPES</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[</span>
  <span class="devsite-syntax-s1">'https://www.googleapis.com/auth/devstorage.read_only'</span><span class="devsite-syntax-p">,</span>
  <span class="devsite-syntax-s1">'https://www.googleapis.com/auth/cloud-platform'</span>
<span class="devsite-syntax-p">]</span>

<span class="devsite-syntax-n">credentials</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">project</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">google</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">auth</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">default</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">scopes</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">GCS_READ_SCOPES</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_4" data-text="JavaScript" tabindex="-1">JavaScript</h3><p>This code expects that the service is running in an environment where
<a href="https://docs.cloud.google.com/docs/authentication/application-default-credentials">Application Default Credentials</a>
can be obtained automatically, such as Cloud Run or Compute Engine.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleAuth</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">require</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'google-auth-library'</span><span class="devsite-syntax-p">);</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">auth</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleAuth</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">scopes</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-s1">'https://www.googleapis.com/auth/devstorage.read_only'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-s1">'https://www.googleapis.com/auth/cloud-platform'</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">});</span>
</code></pre></devsite-code></section>
</devsite-selector></div></li>
</ol><div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="java_3" data-text="Java" tabindex="-1">Java</h3><code translate="no" dir="ltr">java
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text(&quot;Summarize this document.&quot;).build();
Content docContent =
    DocumentContent.builder()
        .uri(&quot;gs://cloud-samples-data/generative-ai/pdf/sample.pdf&quot;)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();

List&lt;Content&gt; contents = Arrays.asList(textContent, docContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of(&quot;gemini-3.7-flash&quot;))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(&quot;&quot;));</code><div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="cli_1" data-text="CLI" tabindex="-1">CLI</h3><p>This is an interactive command. For services like Compute Engine you can attach scopes to
the running service at the config level. See the <a href="https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using">user-managed service
docs</a>
for an example.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">gcloud<span class="devsite-syntax-w"> </span>auth<span class="devsite-syntax-w"> </span>application-default<span class="devsite-syntax-w"> </span>login<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
--scopes<span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"</span>
</code></pre></devsite-code></section>
</devsite-selector></div></section>
</devsite-selector></div><ol>
<li>File registration (Files API)

Use the Files API to register files and produce a Files API path that can
directly be used in the Gemini API.<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_5" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">credentials</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-n">credentials</span><span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-n">registered_gcs_files</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">files</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">register_files</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">uris</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"gs://my_bucket/some_object.pdf"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"gs://bucket2/object2.txt"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-n">prompt</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"Summarize this file."</span>

<span class="devsite-syntax-k">for</span> <span class="devsite-syntax-n">f</span> <span class="devsite-syntax-ow">in</span> <span class="devsite-syntax-n">registered_gcs_files</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">files</span><span class="devsite-syntax-p">:</span>
  <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">f</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">name</span><span class="devsite-syntax-p">)</span>
  <span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
      <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">},</span>
      <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"uri"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">f</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">uri</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">f</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">mime_type</span><span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">],</span>
  <span class="devsite-syntax-p">)</span>
  <span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_5" data-text="JavaScript" tabindex="-1">JavaScript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"@google/genai"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">auth</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">auth</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">registeredGcsFiles</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">files</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">registerFiles</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">uris</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><span class="devsite-syntax-s2">"gs://my_bucket/some_object.pdf"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gs://bucket2/object2.txt"</span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">    </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Summarize this file."</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-w">    </span><span class="devsite-syntax-k">for</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">file</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">of</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">registeredGcsFiles</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">files</span><span class="devsite-syntax-p">)</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">file</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">name</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">ai</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">prompt</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">                </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">file</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">file</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">mimeType</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">            </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
</devsite-selector></div></li>
</ol><div><devsite-selector data-ds-scope="code-sample">
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
</code></pre></devsite-code><div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="cli_2" data-text="CLI" tabindex="-1">CLI</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr"><span class="devsite-syntax-nv">access_token</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>gcloud<span class="devsite-syntax-w"> </span>auth<span class="devsite-syntax-w"> </span>application-default<span class="devsite-syntax-w"> </span>print-access-token<span class="devsite-syntax-k">)</span>
<span class="devsite-syntax-nv">project_id</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-k">$(</span>gcloud<span class="devsite-syntax-w"> </span>config<span class="devsite-syntax-w"> </span>get-value<span class="devsite-syntax-w"> </span>project<span class="devsite-syntax-k">)</span>
curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span>https://generativelanguage.googleapis.com/v1beta/files:register<span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Content-Type: application/json'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Authorization: Bearer </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">access_token</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"x-goog-user-project: </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-nv">project_id</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s2">"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">    </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'</span>
</code></pre></devsite-code></section>
</devsite-selector></div></section>
</devsite-selector></div>
<h2 id="external-urls" data-text="External HTTP / Signed URLs" tabindex="-1">External HTTP / Signed URLs</h2>

<p>You can pass publicly accessible HTTPS URLs or pre-signed URLs directly in your
request. The Gemini API will fetch the content securely during processing.
This is ideal for files up to 100MB that you don&#39;t want to re-upload.</p>
<aside class="note"><strong>Note:</strong><span> Gemini 2.0 family of models are not supported</span></aside><div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="python_6" data-text="Python" tabindex="-1">Python</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Python"><code translate="no" dir="ltr"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">uri</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"</span>
<span class="devsite-syntax-n">prompt</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s2">"Summarize this file"</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">()</span>

<span class="devsite-syntax-n">interaction</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">interactions</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s2">"gemini-3.7-flash"</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-nb">input</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">[</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"uri"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">uri</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"mime_type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"application/pdf"</span><span class="devsite-syntax-p">},</span>
        <span class="devsite-syntax-p">{</span><span class="devsite-syntax-s2">"type"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">:</span> <span class="devsite-syntax-n">prompt</span><span class="devsite-syntax-p">}</span>
    <span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">interaction</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">output_text</span><span class="devsite-syntax-p">)</span>
</code></pre></devsite-code></section>
<section><h3 id="javascript_6" data-text="Javascript" tabindex="-1">Javascript</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JavaScript"><code translate="no" dir="ltr"><span class="devsite-syntax-k">import</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kr">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'@google/genai'</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-ow">new</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">GoogleGenAI</span><span class="devsite-syntax-p">({});</span>

<span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"</span><span class="devsite-syntax-p">;</span>

<span class="devsite-syntax-k">async</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kd">function</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">()</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-kd">const</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-k">await</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">client</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">interactions</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">create</span><span class="devsite-syntax-p">({</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">model</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'gemini-3.7-flash'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-nx">input</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"document"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">uri</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">mime_type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"application/pdf"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">type</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"text"</span><span class="devsite-syntax-p">,</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nx">text</span><span class="devsite-syntax-o">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"summarize this file"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">}</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">});</span>

<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nx">console</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">log</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-nx">interaction</span><span class="devsite-syntax-p">.</span><span class="devsite-syntax-nx">output_text</span><span class="devsite-syntax-p">);</span>
<span class="devsite-syntax-p">}</span>

<span class="devsite-syntax-nx">main</span><span class="devsite-syntax-p">();</span>
</code></pre></devsite-code></section>
<section><h3 id="rest_3" data-text="REST" tabindex="-1">REST</h3><div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">curl<span class="devsite-syntax-w"> </span>-X<span class="devsite-syntax-w"> </span>POST<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://generativelanguage.googleapis.com/v1beta/interactions"</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">      </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'x-goog-api-key: $GEMINI_API_KEY'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">      </span>-H<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'Content-Type: application/json'</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-se">\</span>
<span class="devsite-syntax-w">      </span>-d<span class="devsite-syntax-w"> </span><span class="devsite-syntax-s1">'{</span>
<span class="devsite-syntax-s1">          "model": "gemini-3.7-flash",</span>
<span class="devsite-syntax-s1">          "input": [</span>
<span class="devsite-syntax-s1">            {"type": "text", "text": "Summarize this pdf"},</span>
<span class="devsite-syntax-s1">            {</span>
<span class="devsite-syntax-s1">              "type": "document",</span>
<span class="devsite-syntax-s1">              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",</span>
<span class="devsite-syntax-s1">              "mime_type": "application/pdf"</span>
<span class="devsite-syntax-s1">            }</span>
<span class="devsite-syntax-s1">          ]</span>
<span class="devsite-syntax-s1">        }'</span>
</code></pre></devsite-code></section>
</devsite-selector></div>
<h3 id="accessibility" data-text="Accessibility" tabindex="-1">Accessibility</h3>

<p>Verify that the URLs you provide don&#39;t lead to pages that require a login or
are behind a paywall. For private databases, ensure you create a signed URL
with the correct access permissions and expiry.</p>

<h3 id="safety-checks" data-text="Safety checks" tabindex="-1">Safety checks</h3>

<p>The system performs a content moderation check on the URL to confirm they meet
safety and policy standards. If the URL fails this check, you will get an
<code translate="no" dir="ltr">url_retrieval_status</code> of <code translate="no" dir="ltr">URL_RETRIEVAL_STATUS_UNSAFE</code>.</p>

<h3 id="supported-content-types" data-text="Supported content types" tabindex="-1">Supported content types</h3>

<p>This list of supported file types and limitations is intended as initial
guidance and is not comprehensive. The effective
set of supported types is subject to change and can vary based on the specific
model and tokenizer version in use. Unsupported types will result in an error.
Additionally, content retrieval for these file types
only supports publicly accessible URLs.</p>

<h4 id="text_file_types" data-text="Text file types" tabindex="-1">Text file types</h4>

<ul>
<li><code translate="no" dir="ltr">text/html</code></li>
<li><code translate="no" dir="ltr">text/css</code></li>
<li><code translate="no" dir="ltr">text/plain</code></li>
<li><code translate="no" dir="ltr">text/xml</code></li>
<li><code translate="no" dir="ltr">text/csv</code></li>
<li><code translate="no" dir="ltr">text/rtf</code></li>
<li><code translate="no" dir="ltr">text/javascript</code></li>
</ul>

<h4 id="application_file_types" data-text="Application file types" tabindex="-1">Application file types</h4>

<ul>
<li><code translate="no" dir="ltr">application/json</code></li>
<li><code translate="no" dir="ltr">application/pdf</code></li>
</ul>

<h4 id="image_file_types" data-text="Image file types" tabindex="-1">Image file types</h4>

<ul>
<li><code translate="no" dir="ltr">image/bmp</code></li>
<li><code translate="no" dir="ltr">image/jpeg</code></li>
<li><code translate="no" dir="ltr">image/png</code></li>
<li><code translate="no" dir="ltr">image/webp</code></li>
</ul>

<h4 id="video_file_types" data-text="Video file types" tabindex="-1">Video file types</h4>

<ul>
<li><code translate="no" dir="ltr">video/mp4</code></li>
<li><code translate="no" dir="ltr">video/mpeg</code></li>
<li><code translate="no" dir="ltr">video/quicktime</code></li>
<li><code translate="no" dir="ltr">video/avi</code></li>
<li><code translate="no" dir="ltr">video/x-flv</code></li>
<li><code translate="no" dir="ltr">video/mpg</code></li>
<li><code translate="no" dir="ltr">video/webm</code></li>
<li><code translate="no" dir="ltr">video/wmv</code></li>
<li><code translate="no" dir="ltr">video/3gpp</code></li>
</ul>

<h2 id="best-practices" data-text="Best practices" tabindex="-1">Best practices</h2>

<ul>
<li><strong>Choose the right method:</strong> Use inline data for small, transient files.
Use the File API for larger or frequently used files. Use external URLs
for data already hosted online.</li>
<li><strong>Specify MIME Types:</strong> Always provide the correct MIME type for the file
data to ensure proper processing.</li>
<li><strong>Handle Errors:</strong> Implement error handling in your code to manage
potential issues like network failures, file access problems, or API
errors.</li>
</ul>

<h2 id="limitations" data-text="Limitations" tabindex="-1">Limitations</h2>

<ul>
<li>File size limits vary by method (see <a href="#method-comparison">comparison table</a>)
and file type.</li>
<li>Inline data increases request payload size.</li>
<li>File API uploads are temporary and expire after 48 hours.</li>
<li>External URL fetching is limited to 100MB per payload and supports specific
content types.</li>
</ul>

<h2 id="whats-next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li>Try writing your own multimodal prompts using
<a href="http://aistudio.google.com/">Google AI Studio</a>.</li>
<li>For information on including files in your prompts, see the
<a href="/gemini-api/docs/vision">Vision</a>,
<a href="/gemini-api/docs/audio">Audio</a>, and
<a href="/gemini-api/docs/document-processing">Document processing</a>
guides.</li>
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