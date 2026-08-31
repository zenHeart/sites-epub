








<!doctype html>
<html 
      lang="en"
      dir="ltr">
  <head>
    <meta name="google-signin-client-id" content="721724668570-nbkv1cfusk7kk4eni4pjvepaus73b13t.apps.googleusercontent.com"><meta name="google-signin-scope"
          content="profile email https://www.googleapis.com/auth/developerprofiles https://www.googleapis.com/auth/developerprofiles.award https://www.googleapis.com/auth/devprofiles.full_control.firstparty"><meta property="og:site_name" content="Google Cloud Documentation">
    <meta property="og:type" content="website"><meta name="theme-color" content="#1a73e8"><meta charset="utf-8">
    <meta content="IE=Edge" http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    

    <link rel="manifest" href="/_pwa/clouddocs/manifest.json"
          crossorigin="use-credentials">
    <link rel="preconnect" href="//www.gstatic.com" crossorigin>
    <link rel="preconnect" href="//fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="//www.google-analytics.com" crossorigin><link rel="stylesheet" href="//fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700&display=swap">
      <link rel="stylesheet"
            href="//fonts.googleapis.com/css2?family=Material+Icons&family=Material+Symbols+Outlined&display=block"><link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/css/app.css">
      
        <link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/css/dark-theme.css" disabled>
      <link rel="shortcut icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/images/favicons/onecloud/favicon.ico">
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/images/favicons/onecloud/super_cloud.png"><link rel="canonical" href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini"><link rel="search" type="application/opensearchdescription+xml"
            title="Google Cloud Documentation" href="https://docs.cloud.google.com/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini" /><link rel="alternate" hreflang="x-default" href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini" /><link rel="alternate" hreflang="zh-Hans"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=zh-tw" /><link rel="alternate" hreflang="fr"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=de" /><link rel="alternate" hreflang="he"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=he" /><link rel="alternate" hreflang="id"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=id" /><link rel="alternate" hreflang="it"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=ko" /><link rel="alternate" hreflang="pt-BR"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=pt-br" /><link rel="alternate" hreflang="pt"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=pt" /><link rel="alternate" hreflang="es"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=es" /><link rel="alternate" hreflang="es-419"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini?hl=es-419" /><link rel="alternate" hreflang="en-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini" /><link rel="alternate" hreflang="x-default" href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini" /><link rel="alternate" hreflang="zh-Hans-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=zh-tw" /><link rel="alternate" hreflang="fr-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=fr" /><link rel="alternate" hreflang="de-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=de" /><link rel="alternate" hreflang="he-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=he" /><link rel="alternate" hreflang="id-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=id" /><link rel="alternate" hreflang="it-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=it" /><link rel="alternate" hreflang="ja-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=ja" /><link rel="alternate" hreflang="ko-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=ko" /><link rel="alternate" hreflang="pt-BR-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=pt-br" /><link rel="alternate" hreflang="pt-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=pt" /><link rel="alternate" hreflang="es-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=es" /><link rel="alternate" hreflang="es-419-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/write-code-gemini?hl=es-419" /><title>Code with Gemini Code Assist Standard and Enterprise &nbsp;|&nbsp; Gemini for Google Cloud &nbsp;|&nbsp; Google Cloud Documentation</title>

<meta property="og:title" content="Code with Gemini Code Assist Standard and Enterprise &nbsp;|&nbsp; Gemini for Google Cloud &nbsp;|&nbsp; Google Cloud Documentation"><meta name="description" content="How to use Gemini Code Assist in an IDE">
  <meta property="og:description" content="How to use Gemini Code Assist in an IDE"><meta property="og:url" content="https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini"><meta property="og:image" content="https://docs.cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630"><meta property="og:locale" content="en"><meta name="twitter:card" content="summary_large_image">
  
    
    



































    

    
    

    
    
    

    
    
    
    
    



  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined&display=block" rel="stylesheet" data-page-link><link href="https://fonts.googleapis.com/css2?family=Google+Symbols&display=block" rel="stylesheet" data-page-link>

    </head>
  <body class="color-scheme--light"
        template="page"
        theme="clouddocs-theme"
        type="article"
        
        appearance
        
        layout="docs"
        
        
        free-trial
        
        
        display-toc
        pending>
  
    <devsite-progress type="indeterminate" id="app-progress"></devsite-progress>
  
  
    <a href="#main-content" class="skip-link button">
      
      Skip to main content
    </a>
    <section class="devsite-wrapper">
      <devsite-cookie-notification-bar></devsite-cookie-notification-bar>
        <cloudx-track userCountry="US"></cloudx-track>

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
   track-name="googleCloudDocumentation" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/images/lockup_dark_theme.svg"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/images/lockup_full_color.svg" class="devsite-site-logo" alt="Google Cloud Documentation">
  </picture>
  
</a>



</div>
        <div class="devsite-top-logo-row-middle">
          <div class="devsite-header-upper-tabs">
            
              
              
  <devsite-tabs class="upper-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Upper tabs">
      
        
          <tab class="devsite-dropdown
    
    devsite-active
    devsite-clickable
    ">
  
    <a href="https://docs.cloud.google.com/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/docs"
    
       track-type="nav"
       track-metadata-position="nav - docs-home"
       track-metadata-module="primary nav"
       aria-label="Technology areas, selected" 
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Technology areas"
         
           track-name="docs-home"
         
           track-link-column-type="single-column"
         
       >
    Technology areas
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Technology areas"
         track-type="nav"
         track-metadata-eventdetail="https://docs.cloud.google.com/docs"
         track-metadata-position="nav - docs-home"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Technology areas"
          
            track-name="docs-home"
          
            track-link-column-type="single-column"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
        <button class="devsite-tabs-close-button material-icons button-flat gc-analytics-event"
                data-category="Site-Wide Custom Events"
                data-label="Close dropdown menu"
                aria-label="Close dropdown menu"
                track-type="nav"
                track-name="close"
                track-metadata-eventdetail="#"
                track-metadata-position="nav - docs-home"
                track-metadata-module="tertiary nav">close</button>
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/ai-ml"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/ai-ml"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      AI and ML
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/application-development"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/application-development"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Application development
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/application-hosting"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/application-hosting"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Application hosting
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/compute-area"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/compute-area"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Compute
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/data"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/data"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Data analytics and pipelines
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/databases"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/databases"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Databases
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/dhm-cloud"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/dhm-cloud"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Distributed, hybrid, and multicloud
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/industry"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/industry"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Industry solutions
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/migration"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/migration"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Migration
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/networking"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/networking"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Networking
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/observability"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/observability"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Observability and monitoring
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/security"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/security"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Security
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/storage"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/storage"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Storage
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    
    
    devsite-clickable
    ">
  
    <a href="https://docs.cloud.google.com/docs/cross-product-overviews"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/docs/cross-product-overviews"
    
       track-type="nav"
       track-metadata-position="nav - crossproduct"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Cross-product tools"
         
           track-name="crossproduct"
         
           track-link-column-type="single-column"
         
       >
    Cross-product tools
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Cross-product tools"
         track-type="nav"
         track-metadata-eventdetail="https://docs.cloud.google.com/docs/cross-product-overviews"
         track-metadata-position="nav - crossproduct"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Cross-product tools"
          
            track-name="crossproduct"
          
            track-link-column-type="single-column"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
        <button class="devsite-tabs-close-button material-icons button-flat gc-analytics-event"
                data-category="Site-Wide Custom Events"
                data-label="Close dropdown menu"
                aria-label="Close dropdown menu"
                track-type="nav"
                track-name="close"
                track-metadata-eventdetail="#"
                track-metadata-position="nav - crossproduct"
                track-metadata-module="tertiary nav">close</button>
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/access-resources"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/access-resources"
                     track-metadata-position="nav - crossproduct"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Access and resources management
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/costs-usage"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/costs-usage"
                     track-metadata-position="nav - crossproduct"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Costs and usage management
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/iac"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/iac"
                     track-metadata-position="nav - crossproduct"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Infrastructure as code
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/devtools"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/devtools"
                     track-metadata-position="nav - crossproduct"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      SDK, languages, frameworks, and tools
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
    </nav>

  </devsite-tabs>

            
           </div>
          
<devsite-search
    enable-signin
    enable-search
    enable-suggestions
      
    
    enable-search-summaries
    project-name="Gemini for Google Cloud"
    tenant-name="Google Cloud Documentation"
    project-scope="/gemini/docs"
    url-scoped="https://docs.cloud.google.com/s/results/gemini/docs"
    
    
    
    >
  <form class="devsite-search-form" action="https://docs.cloud.google.com/s/results" method="GET">
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

        

  

  
    <a class="devsite-header-link devsite-top-button button gc-analytics-event button-with-icon"
    href="//console.cloud.google.com/"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Console"
    
      
        track-metadata-position="nav"
      
        track-name="console"
      
        referrerpolicy="no-referrer-when-downgrade"
      
        track-metadata-eventDetail="nav"
      
        track-type="globalNav"
      
    >
  Console
</a>
  

  

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
      <a role="menuitem" lang="es"
        >Español</a>
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
      <a role="menuitem" lang="pt"
        >Português</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="he"
        >עברית</a>
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




        
          <devsite-user 
                        
                        
                          enable-profiles
                        
                        
                          fp-auth
                        
                        id="devsite-user">
            
              
              <span class="button devsite-top-button" aria-hidden="true" visually-hidden>Sign in</span>
            
          </devsite-user>
        
        
        
      </div>
    </div>
  </div>



  <div class="devsite-collapsible-section
    ">
    <div class="devsite-header-background">
      
        
          <div class="devsite-product-id-row"
           >
            <div class="devsite-product-description-row">
              
                
                <div class="devsite-product-id">
                  
                    
  
  <a href="https://docs.cloud.google.com/gemini/docs">
    
  <div class="devsite-product-logo-container"
       
       
       
    size="medium"
  >
  
    <picture>
      
      <source class="devsite-dark-theme"
              media="(prefers-color-scheme: dark)"
              srcset=" /_static/clouddocs/images/icons/products/gemini-white.svg"
              sizes="64px">
      
      <img class="devsite-product-logo"
           alt=""
           src="https://docs.cloud.google.com/_static/clouddocs/images/icons/products/gemini-color.svg"
           srcset=" /_static/clouddocs/images/icons/products/gemini-color.svg"
           sizes="64px"
           loading="lazy"
           >
    </picture>
  
  </div>
  
  </a>
  

                  
                  
                  
                    <ul class="devsite-breadcrumb-list"
  >
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://docs.cloud.google.com/gemini/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Lower Header"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail="Gemini for Google Cloud"
      
    >
    
          Gemini for Google Cloud
        
  </a>
  
      
    
  </li>
  
</ul>
                </div>
                
              
              
            </div>
            
              <div class="devsite-product-button-row">
  

  
  <a href="//console.cloud.google.com/freetrial"
  
    class="cloud-free-trial-button button button-primary
      "
    
    
      
        referrerpolicy="no-referrer-when-downgrade"
      
        track-metadata-position="nav"
      
        track-name="gcpCta"
      
        track-type="freeTrial"
      
        track-metadata-eventDetail="nav"
      
    
    >Start free</a>

</div>
            
          </div>
          
        
      
      
        <div class="devsite-doc-set-nav-row">
          
          
            
            
  <devsite-tabs class="lower-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Lower tabs">
      
        
          <tab  >
            
    <a href="https://docs.cloud.google.com/gemini/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/gemini/docs"
    
       track-type="nav"
       track-metadata-position="nav - overview"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Overview"
         
           track-name="overview"
         
       >
    Overview
  
    </a>
    
  
          </tab>
        
      
        
          <tab  class="devsite-active">
            
    <a href="https://docs.cloud.google.com/gemini/docs/overview"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/gemini/docs/overview"
    
       track-type="nav"
       track-metadata-position="nav - guides"
       track-metadata-module="primary nav"
       aria-label="Guides, selected" 
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Guides"
         
           track-name="guides"
         
       >
    Guides
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://docs.cloud.google.com/gemini/docs/api-and-reference"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/gemini/docs/api-and-reference"
    
       track-type="nav"
       track-metadata-position="nav - api and references"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: API and references"
         
           track-name="api and references"
         
       >
    API and references
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://docs.cloud.google.com/gemini/docs/resources"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/gemini/docs/resources"
    
       track-type="nav"
       track-metadata-position="nav - resources"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Resources"
         
           track-name="resources"
         
       >
    Resources
  
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
     >
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
   track-name="googleCloudDocumentation" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/images/lockup_dark_theme.svg"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/images/lockup_full_color.svg" class="devsite-site-logo" alt="Google Cloud Documentation">
  </picture>
  
</a>


</div>
  </div>

  <div class="devsite-book-nav-wrapper">
    <div class="devsite-mobile-nav-top">
      
        <ul class="devsite-nav-list">
          
            <li class="devsite-nav-item">
              
  
  <a href="/docs"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Technology areas"
      
        track-name="docs-home"
      
        track-link-column-type="single-column"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Technology areas"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Technology areas
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Technology areas"
      
        track-name="docs-home"
      
        track-link-column-type="single-column"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Technology areas">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Technology areas">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
                <ul class="devsite-nav-responsive-tabs">
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/gemini/docs"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Overview"
      
        track-name="overview"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Overview"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Overview
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/gemini/docs/overview"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Guides"
      
        track-name="guides"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Guides"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip menu="_book">
      Guides
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/gemini/docs/api-and-reference"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: API and references"
      
        track-name="api and references"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: API and references"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      API and references
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/gemini/docs/resources"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Resources"
      
        track-name="resources"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Resources"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Resources
   </span>
    
  
  </a>
  

  
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/docs/cross-product-overviews"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Cross-product tools"
      
        track-name="crossproduct"
      
        track-link-column-type="single-column"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Cross-product tools"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Cross-product tools
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Cross-product tools"
      
        track-name="crossproduct"
      
        track-link-column-type="single-column"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Cross-product tools">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Cross-product tools">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
            </li>
          
          
    
    
<li class="devsite-nav-item">

  
  <a href="//console.cloud.google.com/"
    
       class="devsite-nav-title gc-analytics-event button-with-icon"
    

    
      
        track-metadata-position="nav"
      
        track-name="console"
      
        referrerpolicy="no-referrer-when-downgrade"
      
        track-metadata-eventDetail="nav"
      
        track-type="globalNav"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Console"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Console
   </span>
    
  
  </a>
  

</li>

  
          
        </ul>
      
    </div>
    
      <div class="devsite-mobile-nav-bottom">
        
          
          <ul class="devsite-nav-list" menu="_book">
            <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Discover</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Product overview</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Product offerings</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Gemini Code Assist</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/security-privacy-compliance"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Security and privacy overview</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/gemini-cli"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini CLI</span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini/docs/codeassist/gemini-3"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini 3 with Gemini Code Assist</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/supported-languages"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Supported languages, IDEs, and interfaces</span></a></li></ul></div></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/discover/works"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>How Gemini works</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/discover/data-governance"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>How Gemini uses your data</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/discover/responsible-ai"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Responsible AI</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/discover/certifications"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Certifications and security</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Release notes</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini/docs/release-notes"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini for Google Cloud release notes</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/release-notes"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini Code Assist release notes</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/turn-off-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Turn off Gemini for Google Cloud products</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Get started</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/codeassist/set-up-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up Gemini Code Assist</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/discover/write-prompts"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Write better prompts</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Gemini Code Assist</span>
      </div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Configure Gemini Code Assist</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini/docs/admin-settings"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini Code Assist administrator settings</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/configure-release-channels"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure Gemini Code Assist release channels</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/keyboard-shortcuts"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Keyboard shortcuts</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/create-aiexclude-file"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Exclude files from Gemini Code Assist use</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/configure-local-codebase-awareness"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure local codebase awareness</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/configure-logging"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure Gemini Code Assist logging</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/admin"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Add or change Gemini Code Assist subscriptions</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Gemini Code Assist licenses</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/request-license"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Request a Gemini Code Assist license</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/manage-licenses"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Manage Gemini Code Assist licenses</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/cross-org-license-usage"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Prevent cross-organization license usage</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/use-pre-release-features-gemini-code-assist"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use pre-release features in Gemini Code Assist for VS Code</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/configure-vpc-service-controls"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure VPC Service Controls</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/network-access"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Control Network Access with User Domain Restrictions</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/codeassist/generate-metrics"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Generate Code Assist metrics</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Code with Gemini Code Assist</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/code-overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Code features overview</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/write-code-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Code with Gemini Code Assist</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Chat with Gemini Code Assist</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/chat-overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Chat features overview</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/use-gemini-code-assist-chat"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use the Gemini Code Assist chat</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/chat-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Chat with Gemini Code Assist</span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini/docs/codeassist/agent-mode"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Agent mode overview</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/gemini/docs/codeassist/use-agentic-chat-pair-programmer"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use the Gemini Code Assist agent mode</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Code customization</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/code-customization-overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Code customization overview</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/code-customization"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure code customization</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/use-code-customization"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use code customization</span></a></li><li class="devsite-nav-item"><a href="/gemini/docs/codeassist/encrypt-data-cmek"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Encrypt data with customer-managed encryption keys</span></a></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/codeassist/turn-off"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Turn off Code Assist</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Review code in GitHub</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/code-review/review-repo-code"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Review GitHub code with Gemini Code Assist</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/code-review/set-up-code-assist-github"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up Gemini Code Assist for GitHub</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/code-review/use-code-assist-github"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Use Gemini Code Assist for GitHub</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/code-review/customize-repo-review"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Customize Gemini Code Assist behavior in GitHub</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/code-review/style-guide"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Code review style guide</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Observability</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/codeassist/monitor-gemini-code-assist"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Monitor Gemini Code Assist usage</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/log-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>View Gemini Code Assist logs</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/audit-logging"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini for Google Cloud audit logging</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/codeassist/business-audit-logging"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Business AI Code audit logging</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Troubleshoot</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/support/troubleshoot-setup"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Troubleshoot Gemini issues</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/support/troubleshoot-code-assist"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Troubleshoot access to Gemini Code Assist features</span></a></li>

  <li class="devsite-nav-item"><a href="/gemini/docs/support/feedback"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Provide feedback</span></a></li>
          </ul>
        
        
          
    
      
      <ul class="devsite-nav-list" menu="Technology areas"
          aria-label="Side menu" hidden>
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ai-ml"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: AI and ML"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      AI and ML
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/application-development"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Application development"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Application development
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/application-hosting"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Application hosting"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Application hosting
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/compute-area"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Compute"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Compute
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/data"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Data analytics and pipelines"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Data analytics and pipelines
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/databases"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Databases"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Databases
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/dhm-cloud"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Distributed, hybrid, and multicloud"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Distributed, hybrid, and multicloud
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/industry"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Industry solutions"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Industry solutions
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/migration"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Migration"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Migration
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/networking"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Networking"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Networking
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/observability"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Observability and monitoring"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Observability and monitoring
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/security"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Security"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Security
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/storage"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Storage"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Storage
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Cross-product tools"
          aria-label="Side menu" hidden>
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/access-resources"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Access and resources management"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Access and resources management
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/costs-usage"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Costs and usage management"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Costs and usage management
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/iac"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Infrastructure as code"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Infrastructure as code
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/devtools"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: SDK, languages, frameworks, and tools"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      SDK, languages, frameworks, and tools
   </span>
    
  
  </a>
  

</li>

            
          
        
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
  
  
  
  
  

  <div class="devsite-article-meta nocontent" role="navigation" data-nosnippet>
    
    
    <ul class="devsite-breadcrumb-list"
  
    aria-label="Breadcrumb">
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://docs.cloud.google.com/"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail="Google Cloud Documentation"
      
    >
    
          Home
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://docs.cloud.google.com/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="2"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="2"
      
        track-metadata-eventdetail="Documentation"
      
    >
    
          Documentation
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://docs.cloud.google.com/docs/ai-ml"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="3"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="3"
      
        track-metadata-eventdetail="AI and ML"
      
    >
    
          AI and ML
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://docs.cloud.google.com/gemini/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="4"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="4"
      
        track-metadata-eventdetail="Gemini for Google Cloud"
      
    >
    
          Gemini for Google Cloud
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://docs.cloud.google.com/gemini/docs/overview"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="5"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="5"
      
        track-metadata-eventdetail=""
      
    >
    
          Guides
        
  </a>
  
      
    
  </li>
  
</ul>
    
      
    <devsite-thumb-rating position="header">
    </devsite-thumb-rating>
  
    
  </div>
  
    <devsite-feedback
  position="header"
  project-name="Gemini for Google Cloud"
  product-id="5041938"
  bucket="Documentation"
  context=""
  version="t-devsite-webserver-20260825-r00-rc00.479916215390653058"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="header"
  class="nocontent"
  data-nosnippet
  
  
  
    
      project-icon="https://docs.cloud.google.com/_static/clouddocs/images/icons/products/gemini-color.svg"
    
  
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
  
    <h1 class="devsite-page-title" tabindex="-1">
      Code with Gemini Code Assist Standard and Enterprise<devsite-actions hidden data-nosnippet><devsite-feature-tooltip
      ack-key="AckCollectionsBookmarkTooltipDismiss"
      analytics-category="Site-Wide Custom Events"
      analytics-action-show="Callout Profile displayed"
      analytics-action-close="Callout Profile dismissed"
      analytics-label="Create Collection Callout"
      class="devsite-page-bookmark-tooltip nocontent"
      data-nosnippet
      dismiss-button="true"
      id="devsite-collections-dropdown"
      
      dismiss-button-text="Dismiss"

      
      close-button-text="Got it">

    
    
      <devsite-bookmark></devsite-bookmark>
    

    <span slot="popout-heading">
      
      Stay organized with collections
    </span>
    <span slot="popout-contents">
      
      Save and categorize content based on your preferences.
    </span>
  </devsite-feature-tooltip>
    <devsite-llm-tools></devsite-llm-tools></devsite-actions>
  
      
    </h1>
  

  <devsite-toc class="devsite-nav"
    depth="2"
    devsite-toc-embedded
    >
  </devsite-toc>
  
    
  <div class="devsite-article-body clearfix
  ">

  
    
    
    
    
<aside class="note"><strong>Note:</strong><span> We have unified our tools into a single, multi-agent platform called
Antigravity, with Antigravity CLI now available. Starting June 18, 2026,
Gemini Code Assist IDE Extensions and Gemini CLI
stopped serving requests for the Gemini Code Assist for
individuals, Google AI Pro, and Google AI Ultra tiers. Affected users
should migrate to Antigravity and Antigravity CLI. To learn more, see the
<a href="https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals">deprecation page</a>.</span></aside>
<p></p>

<p>This document describes how you can use <a href="/gemini/docs/codeassist/overview">Gemini Code Assist</a>,
an AI-powered collaborator in your IDE, to help you do the following in VS Code
or IntelliJ and other <a href="/gemini/docs/codeassist/supported-languages#supported_ides">supported JetBrains IDEs</a>:</p>

<ul>
<li>Generate code for your project with code transformation.</li>
<li>Receive code completions while you&#39;re coding.</li>
<li>Use smart actions.</li>
</ul>

<p>If you&#39;re using <a href="/gemini/docs/codeassist/overview#editions-overview">Gemini Code Assist Enterprise</a>, you
can use <a href="/gemini/docs/codeassist/code-customization-overview">Code customization</a>,
which lets you get code suggestions based on your organization&#39;s private
codebase directly from Gemini Code Assist Enterprise. Learn
<a href="/gemini/docs/codeassist/code-customization">how to configure code customization</a>.</p>

<p>This document is intended for developers of all skill levels. It assumes you
have working knowledge of VS Code or IntelliJ and other supported JetBrains
IDEs, and are familiar with Google Cloud. If you prefer, you can also
explore Gemini Code Assist in
<a href="/code/docs/shell/write-code-gemini">Cloud Shell Editor</a>,
<a href="/workstations/docs/write-code-gemini">Cloud Workstations</a>,
and <a href="https://developer.android.com/studio/gemini/overview">Android Studio</a>.</p>
<aside class="note"><strong>Note:</strong><span> The behaviour of code generation, completion, and transformation are
non-deterministic when used simultaneously with other plugins that either
implement the same shortcuts and/or use the same platform API to process these
actions.</span></aside>
<h2 id="before_you_begin" data-text="Before you begin" tabindex="-1">Before you begin</h2>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code" data-text=" VS Code " tabindex="-1"> VS Code </h3><ol>
<li><p><a href="/gemini/docs/codeassist/set-up-gemini">Set up Gemini Code Assist Standard or Enterprise</a>,
 if you haven&#39;t already.</p></li>
<li><p>Before testing Gemini Code Assist capabilities in your
code file, make sure your file&#39;s coding language is supported. For more
information on supported coding languages, see
<a href="/gemini/docs/codeassist/supported-languages#coding-languages">Supported coding languages</a>.</p></li>
<li><p>If you prefer to use your IDE behind a proxy, see
<a href="https://code.visualstudio.com/docs/setup/network">Network Connections in Visual Studio Code</a>.</p></li>
</ol></section>
<section><h3 id="intellij" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><ol>
<li><p><a href="/gemini/docs/codeassist/set-up-gemini">Set up Gemini Code Assist Standard or Enterprise</a>,
 if you haven&#39;t already.</p></li>
<li><p>Before testing Gemini Code Assist capabilities in your
code file, make sure your file&#39;s coding language is supported. For more
information on supported coding languages, see
<a href="/gemini/docs/codeassist/supported-languages#coding-languages">Supported coding languages</a>.</p></li>
<li><p>If you prefer to use your IDE behind a proxy, see
<a href="https://www.jetbrains.com/help/idea/settings-http-proxy.html">HTTP Proxy</a>.</p></li>
</ol></section>
</devsite-selector></div>
<h2 id="generate_code_with_prompts" data-text="Generate code with prompts" tabindex="-1">Generate code with prompts</h2>

<p>The following sections show you how to use Gemini Code Assist to
generate code with the example prompt <code translate="no" dir="ltr">Function to create a Cloud Storage
bucket</code> inside your code file. You can also select a part of your code and then
prompt Gemini Code Assist for help through the chat feature, and
receive and accept or reject code suggestions while you code.</p>

<h3 id="prompt_with_code_transformation" data-text="Prompt Gemini Code Assist with code transformation" tabindex="-1">Prompt Gemini Code Assist with code transformation</h3>

<p>Code transformation allows you to use commands or natural language prompts in
the Quick Pick menu to request modifications to your code, and provides you with
a diff view to show pending changes to your code. To prompt
Gemini Code Assist with code transformation, follow these steps:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_1" data-text=" VS Code " tabindex="-1"> VS Code </h3><ol>
<li><p>In your code file, on a new line, press <kbd>Control+I</kbd> (for Windows
and Linux) or <kbd>Command+I</kbd> (for macOS) to open the
<strong>Gemini Code Assist Quick Pick</strong> menu.</p></li>
<li><p>In the menu, using the <code translate="no" dir="ltr">/generate</code> command, enter <code translate="no" dir="ltr">/generate function to
create a Cloud Storage bucket</code> and then press <kbd>Enter</kbd> (for Windows
and Linux) or <kbd>Return</kbd> (for macOS).</p>

<p><img src="/static/code/docs/vscode/images/gemini-code-assist-generate-command.png" alt="Gemini Code Assist generates code with the /generate command." class="screenshot"> </p>

<p>Gemini Code Assist generates the code based on your prompt
in a diff view.</p>

<p><img src="/static/code/docs/vscode/images/gemini-code-assist-diff-view.png" alt="Gemini Code Assist opens a diff view to show generated code." class="screenshot"> </p></li>
<li><p>Optional: To accept these changes, click <strong>Accept</strong>.</p></li>
</ol></section>
<section><h3 id="intellij_1" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><ol>
<li><p>In your code file, on a new line, press <kbd>Alt+\</kbd> (for Windows and
Linux) or <kbd>Cmd+\</kbd> (for macOS) to open the <strong>Gemini Code Assist
Quick Pick</strong> menu.</p></li>
<li><p>In the menu, using the <code translate="no" dir="ltr">/generate</code> command, enter <code translate="no" dir="ltr">/generate function to
create a Cloud Storage bucket</code> and then press <kbd>Enter</kbd> (for
Windows and Linux) or <kbd>Return</kbd> (for macOS).</p>

<p><img src="/static/gemini/images/cloud-transformation-generate-function-gca-intellij.png" alt="Code transformation generate function in IntelliJ Gemini Code Assist" class="screenshot"> </p>

<p>Gemini Code Assist generates the code based on your prompt
in a diff view.</p>

<p><img src="/static/gemini/images/cloud-transformation-diff-view-gca-intellij.png" alt="Code transformation diff view in IntelliJ Gemini Code Assist" class="screenshot"> </p></li>
<li><p>Optional: To accept these changes, click <strong>Accept Changes</strong>.</p>

<p>You can use the following code transformation commands in your IDE:</p>

<ul>
<li><code translate="no" dir="ltr">/fix</code>: Fix issues or errors in your code. Example: <code translate="no" dir="ltr">/fix potential
NullPointerExceptions in my code</code>.</li>
<li><code translate="no" dir="ltr">/generate</code>: Generate code. Example: <code translate="no" dir="ltr">/generate a function to get the
current time</code>.</li>
<li><code translate="no" dir="ltr">/doc</code>: Add documentation to your code. Example: <code translate="no" dir="ltr">/doc this function</code>.</li>
<li><code translate="no" dir="ltr">/simplify</code>: Simplify your code. Example: <code translate="no" dir="ltr">/simplify if statement in
this code</code>.</li>
</ul></li>
</ol></section>
</devsite-selector></div>
<h3 id="prompt_in_a_code_file_with_a_comment" data-text="Prompt Gemini Code Assist in a code file with a comment" tabindex="-1">Prompt Gemini Code Assist in a code file with a comment</h3>

<p>If you prefer, you can also prompt Gemini Code Assist in your
code file with a comment by following these steps:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_2" data-text=" VS Code " tabindex="-1"> VS Code </h3><ol>
<li><p>On a new line, enter the comment <code translate="no" dir="ltr">Function to create a Cloud Storage
bucket</code>, and then press <kbd>Enter</kbd> (for Windows and Linux) or
<kbd>Return</kbd> (for macOS).</p></li>
<li><p>To generate code, press <kbd>Control+Enter</kbd> (for Windows and Linux)
or <kbd>Control+Return</kbd> (for macOS).</p>

<p>Next to your prompt text in your code file,
Gemini Code Assist generates the code in the form of ghost
text.</p></li>
<li><p>Optional: To accept the generated code, press <kbd>Tab</kbd>.</p></li>
</ol></section>
<section><h3 id="intellij_2" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><ol>
<li><p>In your code file, on a new line, enter the comment <code translate="no" dir="ltr">Function to create a
Cloud Storage bucket</code>.</p></li>
<li><p>To generate code, press <kbd>Alt+G</kbd> (for Windows and Linux) or
<kbd>Option+G</kbd> (for macOS). Alternatively, you can right-click next
to the comment and select <strong>Generate Code</strong>.</p>

<p>Gemini Code Assist generates the code below your comment in
the form of ghost text.</p></li>
<li><p>Optional: To accept the generated code, press <kbd>Tab</kbd>.</p></li>
</ol></section>
</devsite-selector></div>
<h3 id="optional_change_keyboard_shortcut_for_generating_code" data-text="Optional: Change keyboard shortcut for generating code" tabindex="-1">Optional: Change keyboard shortcut for generating code</h3>

<p>If the default keyboard shortcut for generating code isn&#39;t working as outlined
in the previous section, you can
<a href="/gemini/docs/codeassist/keyboard-shortcuts#edit_keyboard_shortcuts">change the keyboard shortcut</a>.</p>

<h2 id="get_code_completions" data-text="Get code completions" tabindex="-1">Get code completions</h2>

<p>While you write code, Gemini Code Assist makes inline code
suggestions, also known as <em>code completions</em>, that you can either accept or
ignore. To get code completions, follow these steps:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_3" data-text=" VS Code " tabindex="-1"> VS Code </h3><ol>
<li><p>In your code file, on a new line, start writing a function. For example,
if you&#39;re in a Python file, write <code translate="no" dir="ltr">def</code>.</p>

<p>Gemini Code Assist suggests code in the form of ghost text.</p></li>
<li><p>To accept the code suggestion from Gemini Code Assist,
press <kbd>Tab</kbd>. Otherwise, to ignore the suggestion, press
<kbd>Esc</kbd> or continue writing your code.</p></li>
</ol></section>
<section><h3 id="intellij_3" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><ol>
<li><p>In your code file, on a new line, start writing a function. For example,
if you&#39;re in a Python file, write <code translate="no" dir="ltr">def</code>.</p>

<p>Gemini Code Assist suggests code in the form of an inline
suggestion.</p></li>
<li><p>To accept the code suggestion from Gemini Code Assist,
press <kbd>Tab</kbd>. Otherwise, to ignore the suggestion, press
<kbd>Esc</kbd> or continue writing your code.</p></li>
<li><p>Optional: If you prefer to use a different shortcut key to accept the
inline suggestion, hold your pointer over the inline suggestion and click the
<strong>Tab</strong> dropdown that appears. Then, select your preferred shortcut or click
<strong>Custom</strong> to enter your own shortcut.</p>

<p><img src="/static/code/docs/intellij/images/gemini-code-assist-change-inline-completion-shortcut.png" alt="Gemini provides a dropdown menu to change your shortcut to accept an inline suggestion." class="screenshot"> </p></li>
</ol></section>
</devsite-selector></div>
<h3 id="optional_disable_code_completion" data-text="Optional: Disable code completion" tabindex="-1">Optional: Disable code completion</h3>

<p>Code completion is enabled by default. If you want to disable code completion,
follow these steps:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_4" data-text=" VS Code " tabindex="-1"> VS Code </h3><ol>
<li><p>In your IDE, click <strong>Code</strong> (for macOS) or <strong>File</strong> (for Windows and
Linux), and then navigate to <strong>Preferences</strong> <span aria-label="and then">></span> <strong>Settings</strong>.</p></li>
<li><p>On the <strong>User</strong> tab of the <strong>Settings</strong> dialog, navigate to <strong>Extensions</strong>
<span aria-label="and then">></span> <strong>Gemini Code Assist</strong>.</p></li>
<li><p>Scroll until you find the <strong>Geminicodeassist &gt; Inline Suggestions: Enable Auto</strong>
list, and then select <strong>Off</strong>.</p>

<p>This turns off the inline suggestions. You can still press
<kbd>Control+Enter</kbd> (for Windows and Linux) or
<kbd>Control+Return</kbd> (for macOS) to manually trigger inline
suggestions.</p></li>
</ol></section>
<section><h3 id="intellij_4" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><p>In the status bar of your IDE, click
<span class="google-symbols" translate="no">spark</span> <strong>Gemini Code
Assist: Active</strong> and select <strong>Enable AI Code Completion</strong>.</p>

<p><img src="/static/code/docs/intellij/images/gemini-code-assist-code-completion.png" alt="Gemini Code Completion button in IntelliJ status bar." class="screenshot"> </p>

<p>This disables the code completion setting, and
Gemini Code Assist no longer makes inline suggestions until
you enable the setting again.</p></section>
</devsite-selector></div>
<h2 id="use_next_edit_predictions" data-text="Use Next Edit Predictions" tabindex="-1">Use Next Edit Predictions</h2>

<aside class="preview"><b>Preview</b>

<p>This product or feature is in preview. Products and features that are
in preview are available "as is".</p>

</aside>

<p>While code completion only suggests changes at your cursor in a code file, Next
Edit Predictions provide predicted code suggestions throughout the file, even in
locations away from the cursor.</p>

<p>You can enable Next Edit Predictions in the settings of your IDE.</p>

<p>To use Next Edit Predictions in your IDE, follow these steps:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_5" data-text=" VS Code " tabindex="-1"> VS Code </h3><p>To begin using Next Edit Predictions, enable the setting:</p>

<ol>
<li><p>Navigate to <span class="google-symbols">settings</span> <strong>Manage</strong>
<span aria-label="and then">></span> <strong>Settings</strong>.</p></li>
<li><p>In the <strong>User</strong> tab of the settings window, navigate to <strong>Extensions</strong>
<span aria-label="and then">></span> <strong>Gemini Code Assist</strong>.</p></li>
<li><p>Scroll until you find <strong>Geminicodeassist &gt; Inline Suggestions: Next Edit
Predictions</strong>.</p></li>
<li><p>Select the checkbox to enable Next Edit Predictions in VS Code.</p></li>
</ol>

<p>Now that you&#39;ve enabled the setting, you can start using Next Edit Predictions
in a code file by performing these steps:</p>

<ol>
<li><p>In your code file, start writing code. Next Edit Predictions appear when
you pause or stop typing.</p>

<p class="screenshot"><img src="/static/gemini/images/vscode-next-edits-triggererd.png" alt="User triggers the Next Edit Predictions in VS Code Gemini Code Assist."> </p></li>
<li><p>Press <kbd>Tab</kbd> to accept the provided Next Edit suggestion.</p>

<p class="screenshot"><img src="/static/gemini/images/vscode-next-edits-entered.png" alt="User enters the Next Edit Prediction in VS Code Gemini Code Assist."> </p></li>
<li><p>If you want to accept the next suggestion, press <kbd>Tab</kbd> again. A
further suggestion may appear and the process can again be repeated.
Otherwise, press <kbd>Esc</kbd> to dismiss, or continue typing to ignore the
suggestion.</p>

<p>When you press <kbd>Tab</kbd> to enter the suggestion, you can hold your
pointer over the suggestion to see the other suggestions, if applicable.
If there are multiple suggestions, you can click the left and right arrows
to cycle through the other suggestions.</p>

<p class="screenshot"><img src="/static/gemini/images/vscode-next-edits-available.png" alt="Available Next Edit Predictions in VS Code Gemini Code Assist."> </p>

<p>Whenever you press <kbd>Esc</kbd> to dismiss the suggestion,
Gemini Code Assist stops suggesting Next Edit Predictions
for that specific code block. You continue to receive suggestions when you
move to another section of your code.</p>
<aside class="note"><strong>Note:</strong><span> Gemini Code Assist only provides Next Edit
Predictions in the file that you&#39;re currently in.
Gemini Code Assist doesn&#39;t provide Next Edit Predictions in
other files.</span></aside></li>
</ol></section>
<section><h3 id="intellij_5" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><p>To begin using Next Edit Predictions, enable the setting:</p>

<ol>
<li><p>Navigate to <strong>File</strong> <span aria-label="and then">></span> <strong>Settings</strong> <span aria-label="and then">></span> <strong>Tools</strong>
<span aria-label="and then">></span> <strong>Gemini</strong>.</p></li>
<li><p>In the <strong>Completion</strong> section, select the <strong>Next Edit Predictions</strong>
checkbox to enable the feature.</p></li>
</ol>

<p>Now that you&#39;ve enabled the setting, you can start using Next Edit Predictions
in a code file by performing these steps:</p>

<ol>
<li><p>In your code file, start writing code. Next Edit Predictions appear when
you pause or stop typing.</p>

<p class="screenshot"><img src="/static/gemini/images/intellij-next-edits-triggererd.png" alt="User triggers the Next Edit Predictions in IntelliJ Gemini Code Assist."> </p></li>
<li><p>Press <kbd>Tab</kbd> to accept the provided Next Edit suggestion.</p>

<p class="screenshot"><img src="/static/gemini/images/intellij-next-edits-entered.png" alt="User enters the Next Edit Prediction in IntelliJ Gemini Code Assist."> </p></li>
<li><p>If you want to accept the next suggestion, press <kbd>Tab</kbd> again. A
further suggestion may appear and the process can again be repeated.
Otherwise, press <kbd>Esc</kbd> to dismiss, or continue typing to ignore the
suggestion.</p>

<p>Whenever you press <kbd>Esc</kbd> to dismiss the suggestion,
Gemini Code Assist stops suggesting Next Edit Predictions
for that specific code block. You continue to receive suggestions when you
move to another section of your code.</p>
<aside class="note"><strong>Note:</strong><span> Gemini Code Assist only provides Next Edit
Predictions in the file that you&#39;re currently in.
Gemini Code Assist doesn&#39;t provide Next Edit Predictions
that would impact code in other files.</span></aside></li>
</ol></section>
</devsite-selector></div>
<h2 id="finish-changes" data-text="Finish changes in a file" tabindex="-1">Finish changes in a file</h2>

<p>Gemini Code Assist can generate code suggestion to complete your
file&#39;s pseudocode, #TODOs, and half-written code.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_6" data-text=" VS Code " tabindex="-1"> VS Code </h3><ol>
<li><p>In your code file, start writing code until the <code translate="no" dir="ltr">Alt+F</code> or <code translate="no" dir="ltr">Opt+F</code>  hint
appears.</p></li>
<li><p>To generate suggested code, press the keyboard shortcut provided
by the hint, or right-click in the file and select
<strong>Gemini Code Assist</strong> <span aria-label="and then">></span> <strong>Finish changes</strong>.</p>

<p>You can dismiss the hint or cancel the code generation process by
pressing <code translate="no" dir="ltr">Esc</code>.</p></li>
<li><p>Once Gemini Code Assist finishes generating suggested
code, you can click <strong>Accept</strong>, which applies the suggested code to your
file, or you can click <strong>Decline</strong>, which leaves your original code
unchanged.</p></li>
</ol></section>
<section><h3 id="intellij_6" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><ol>
<li><p>Check that there are portions of your focused file that have code in need
of completion, such as pseudocode or #TODOs.</p></li>
<li><p>In the file window, right-click <span aria-label="and then">></span> <strong>Gemini</strong> <span aria-label="and then">></span>
<strong>Finish changes</strong>. Alternatively, you can
<a href="/gemini/docs/codeassist/keyboard-shortcuts#code-shortcuts">use the finish changes keyboard shortcut</a>.</p>

<p>Gemini Code Assist generates code suggestions to finish
the incomplete portions of your code.</p></li>
<li><p>For each code suggestion, click 
<span class="google-symbols">check_small</span> <strong>Accept</strong> or
<span class="google-symbols">undo</span> <strong>Reject</strong>.</p>

<p>Alternatively, the option to <strong>Accept all</strong> or <strong>Reject all</strong> is
available at the top of the file.</p></li>
</ol></section>
</devsite-selector></div>
<h2 id="get_more_relevant_suggestions_with_remote_repository_context" data-text="Get more relevant suggestions with remote repository context" tabindex="-1">Get more relevant suggestions with remote repository context</h2>

<p>You can get more contextually aware and relevant code suggestions by directing
Gemini Code Assist to focus on specific remote repositories.
This is useful when your task centers on a specific set of microservices,
libraries, or modules.</p>

<h3 id="before_you_begin_2" data-text="Before you begin" tabindex="-1">Before you begin</h3>

<p>Before you use a remote repository as context, you must first
<a href="/gemini/docs/codeassist/code-customization">index and configure it for code customization</a>.</p>

<h3 id="use_a_remote_repository_as_context" data-text="Use a remote repository as context" tabindex="-1">Use a remote repository as context</h3>

<p>To direct Gemini Code Assist to use one or more repositories
as the primary context for your prompts:</p>

<ol>
<li>In your IDE&#39;s chat, start your prompt with the <kbd>@</kbd> symbol.
A list of your available indexed remote repositories appears.</li>
<li>Select the repository (or repositories) you want to use for context from
the list. You can also start typing the repository name to filter the list.</li>
<li>After selecting the repositories, write the rest of your prompt.</li>
</ol>

<p>Gemini Code Assist then prioritizes the selected repositories
when generating a response.</p>

<h3 id="example_prompts" data-text="Example prompts" tabindex="-1">Example prompts</h3>

<p>This section includes examples of how you can get more relevant suggestions with
remote repository context.</p>

<ul>
<li>Understand a repository
<ul>
<li><code translate="no" dir="ltr">@REPOSITORY_NAME What is the overall structure of this repository?</code></li>
<li><code translate="no" dir="ltr">@REPOSITORY_NAME I&#39;m a new team member. Can you give me an overview of
this repository&#39;s purpose and key modules?</code></li>
</ul></li>
<li>Generate and modify code
<ul>
<li><code translate="no" dir="ltr">@REPOSITORY_NAME Implement an authentication function similar to the one
in this repository.</code></li>
<li><code translate="no" dir="ltr">@REPOSITORY_NAME Refactor the following code to follow the conventions in
the selected repository.</code></li>
<li><code translate="no" dir="ltr">Use the library-x in @REPOSITORY_A_NAME-A and implement the function-x</code></li>
</ul></li>
<li>Test
<ul>
<li><code translate="no" dir="ltr">@UNIT_TEST_FILE_NAME Generate unit tests for module-x based on the examples
in the selected file.</code></li>
</ul></li>
</ul>

<p>By using remote repositories as a focused source of context, you can get more
accurate and relevant suggestions from Gemini Code Assist, which
can help you code faster and more efficiently.</p>

<h2 id="use_smart_actions" data-text="Use smart actions" tabindex="-1">Use smart actions</h2>

<p>To help you be more productive while minimizing context switching,
Gemini Code Assist provides AI-powered smart actions directly in
your code editor. When you select your code in your code editor, you can view
and select from a list of actions relevant to your context.</p>

<p>To use smart actions in your code, follow these steps:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_7" data-text=" VS Code " tabindex="-1"> VS Code </h3><ol>
<li><p>In your code file, select a block of code.</p></li>
<li><p>Next to the selected code block, click
<span class="google-symbols" translate="no">lightbulb</span> <strong>Show Code
Actions</strong>.</p>

<p class="screenshot"><img src="/static/code/docs/vscode/images/duet-ai-vsc-code-actions.png" alt="Smart actions lightbulb icon appears after selecting a block of code in VS Code."> </p></li>
<li><p>Select an action such as <strong>Generate unit tests</strong>.</p>

<p>Gemini Code Assist generates a response that&#39;s based on the
action you selected.</p></li>
</ol></section>
<section><h3 id="intellij_7" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><ol>
<li><p>In your code file, select a line or block of code.</p></li>
<li><p>Right-click the selected code and select a smart action, like
<strong>Generate unit tests</strong>.</p>

<p>Selecting the smart action will automatically prompt
Gemini Code Assist to generate a response to the prompt in
the <strong>Gemini Code Assist</strong> tool window.</p></li>
</ol></section>
</devsite-selector></div>
<h2 id="use_code_transformation_quick_fix" data-text="Use code transformation quick fix" tabindex="-1">Use code transformation quick fix</h2>

<p>If there&#39;s an error in your code, Gemini Code Assist gives you
the option to apply a <em>quick fix</em> to the error with code transformation.</p>

<p>To apply a quick fix in your code file, follow these steps:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_8" data-text=" VS Code " tabindex="-1"> VS Code </h3><ol>
<li><p>In your code file, hold your pointer over the squiggly error line and
select <strong>Quick Fix</strong>, and then select <strong>/fix</strong>.</p>

<p><img src="/static/code/docs/vscode/images/code-transformation-quick-fix.png" alt="Code transformation quick fix in the IDE." class="screenshot"> </p></li>
<li><p>When the quick fix is applied, a diff view appears. To accept these
changes, click <strong>Accept</strong>.</p></li>
</ol></section>
<section><h3 id="intellij_8" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><ol>
<li><p>In your code file, click the red error bulb icon, which indicates an error
in your code, and select <strong>Fix with Gemini</strong>.</p>

<p><img src="/static/gemini/images/code-transformation-quick-fix-gca-intellij.png" alt="Code transformation option to fix with Gemini in the IDE." class="screenshot"> </p></li>
<li><p>When the fix is applied, a diff view appears. To accept these changes,
click <strong>Accept</strong>.</p></li>
</ol></section>
</devsite-selector></div>
<h2 id="exclude_files_from_local_context" data-text="Exclude files from local context" tabindex="-1">Exclude files from local context</h2>

<p>If files are specified in a <code translate="no" dir="ltr">.aiexclude</code> or <code translate="no" dir="ltr">.gitignore</code> file,
Gemini Code Assist by default excludes them from local use in the
context for code completion, code generation, code transformation, and chat.</p>

<p>To learn how to exclude files from local use, see
<a href="/gemini/docs/codeassist/create-aiexclude-file">Exclude files from Gemini Code Assist use</a>.</p>

<h2 id="disable_code_suggestions_that_match_cited_sources" data-text="Disable code suggestions that match cited sources" tabindex="-1">Disable code suggestions that match cited sources</h2>

<p>Gemini Code Assist provides citation information when it directly
quotes at length from another source, such as existing open source code. For
more information, see
<a href="/gemini/docs/discover/works">How and when Gemini cites sources</a>.</p>

<p>To prevent code that matches cited sources from being suggested to you, do the
following:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_9" data-text="VS Code" tabindex="-1">VS Code</h3><ol>
<li><p>In the activity bar of your IDE, click <strong>Manage</strong> <span aria-label="and then">></span> <strong>Settings</strong>.</p></li>
<li><p>In the <strong>User</strong> tab of the settings window, navigate to <strong>Extensions</strong>
<span aria-label="and then">></span> <strong>Gemini Code Assist</strong>.</p></li>
<li><p>Scroll until you find <strong>Geminicodeassist &gt; Recitation: Max Cited Length</strong>.</p></li>
<li><p>Set the value to <code translate="no" dir="ltr">0</code>.</p></li>
</ol>

<p>Gemini Code Assist no longer suggests code to you that matches
cited sources.</p></section>
<section><h3 id="intellij_9" data-text="IntelliJ" tabindex="-1">IntelliJ</h3><ol>
<li><p>In the status bar of your IDE, click
<span class="google-symbols" translate="no">spark</span>
<strong>Gemini Code Assist: Active</strong> and select then select
<strong>Configure Gemini</strong>.</p></li>
<li><p>Expand the <strong>Advanced settings</strong> section, and then select
<strong>Block selections that match external cited sources</strong>.</p></li>
<li><p>Click <strong>OK</strong>.</p></li>
</ol>

<p>Gemini Code Assist no longer suggests code to you that matches
cited sources.</p></section>
</devsite-selector></div>
<h2 id="known-issues" data-text="Known issues" tabindex="-1">Known issues</h2>

<p>This section outlines the known issues of Gemini Code Assist:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="vs-code_10" data-text=" VS Code " tabindex="-1"> VS Code </h3><ul>
<li><p><strong>Chat responses may be truncated when they include an updated version of a
large open file</strong></p>

<p>To work around this issue, select a smaller section of code and include an
additional directive in the chat prompt, such as <code translate="no" dir="ltr">only output the selected
code.</code></p></li>
<li><p><strong>Vim: Cannot accept or dismiss code generation suggestions unless in
insert mode</strong></p>

<p>When using the Vim plugin in normal mode, you can&#39;t accept or dismiss code
suggestions.</p>

<p>To work around this issue, press <kbd>i</kbd> to enter insert mode, and
then press <kbd>Tab</kbd> to accept the suggestion.</p></li>
<li><p><strong>Vim: Inconsistent behavior when pressing <kbd>Esc</kbd> to dismiss
suggestions</strong></p>

<p>When you press <kbd>Esc</kbd>, both the IDE and
Gemini Code Assist suggestions are dismissed. This behavior
is different from the non-Vim behavior where pressing <kbd>Esc</kbd>
re-triggers Gemini Code Assist.</p></li>
<li><p><strong>Sign-in attempts keep timing out</strong></p>

<p>If your sign-in attempts keep timing out, try adding the
<code translate="no" dir="ltr">cloudcode.beta.forceOobLogin</code> setting to your <code translate="no" dir="ltr">settings.json</code> file:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nt">"cloudcode.beta.forceOobLogin"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span>
</code></pre></devsite-code></li>
<li><p><strong>License recitation warnings don&#39;t persist across sessions</strong></p>

<p>If license recitation warnings don&#39;t persist across sessions, refer to the
persistent logs:</p>

<ol>
<li><p>Click <strong>View</strong> <span aria-label="and then">></span> <strong>Output</strong>.</p></li>
<li><p>Select <strong>Gemini Code Assist - Citations</strong>.</p></li>
</ol></li>
<li><p><strong>Connectivity issues in the Gemini Code Assist output
window</strong></p>

<p>If you see a connection error or other connectivity problems in the
Gemini Code Assist output window, try the following:</p>

<ul>
<li><p>Configure your firewall to allow access to <code translate="no" dir="ltr">oauth2.googleapis.com</code> and
<code translate="no" dir="ltr">cloudaicompanion.googleapis.com</code>.</p></li>
<li><p>Configure your firewall to allow communication over HTTP/2, which gRPC
uses.</p></li>
</ul>

<p>You can use the <code translate="no" dir="ltr">grpc-health-probe</code> tool to test connectivity. A
successful check results in the following output:</p>

<p><code translate="no" dir="ltr">$ grpc-health-probe -addr cloudaicompanion.googleapis.com:443 -tls
error: this server does not implement the grpc health protocol
(grpc.health.v1.Health): GRPC target method can&#39;t be resolved</code></p>

<p>An unsuccessful check results in the following output:</p>

<p><code translate="no" dir="ltr">timeout: failed to connect service &quot;cloudaicompanion.googleapis.com:443&quot; within 1s</code></p>

<p>To obtain more details, run the following before <code translate="no" dir="ltr">grpc-health-probe</code>:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded><code translate="no" dir="ltr">export GRPC_GO_LOG_SEVERITY_LEVEL=info
</code></pre></devsite-code></li>
</ul>

</section>
<section><h3 id="intellij_10" data-text=" IntelliJ " tabindex="-1"> IntelliJ </h3><p>There are no known issues for Gemini Code Assist for IntelliJ
and other supported JetBrains IDEs.</p></section>
</devsite-selector></div>
<h2 id="leave_feedback" data-text="Leave feedback" tabindex="-1">Leave feedback</h2>

<p>To leave feedback of your experience, see
<a href="/gemini/docs/support/feedback">Provide Gemini Code Assist feedback</a>.</p>

<h2 id="whats_next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li>Learn how to <a href="/gemini/docs/discover/write-prompts">write better prompts</a>.</li>
<li>Learn <a href="/gemini/docs/discover/data-governance">how Gemini Code Assist uses your data</a>.</li>
<li>Learn about <a href="https://cloud.google.com/products/gemini/pricing">Gemini Code Assist pricing</a>.</li>
<li>Learn more about <a href="https://cloud.google.com/compliance">Google Cloud compliance</a>.</li>
</ul>


  <link href="https://fonts.googleapis.com/css2?family=Google+Symbols" rel="stylesheet" data-page-link>
  

  
    <devsite-hats-survey class="nocontent" data-nosnippet
      hats-id="Nd7nTix2o0eU5NUYprb0ThtUc5jf"
      listnr-id="83405"></devsite-hats-survey>
  

  
</div>

  
    
    
      
    <devsite-thumb-rating position="footer">
    </devsite-thumb-rating>
  
       
         <devsite-feedback
  position="footer"
  project-name="Gemini for Google Cloud"
  product-id="5041938"
  bucket="Documentation"
  context=""
  version="t-devsite-webserver-20260825-r00-rc00.479916215390653058"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="footer"
  class="nocontent"
  data-nosnippet
  
  
  
    
      project-icon="https://docs.cloud.google.com/_static/clouddocs/images/icons/products/gemini-color.svg"
    
  
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
       
    
    
  

  <div class="devsite-floating-action-buttons"></div></article>


<devsite-content-footer class="nocontent" data-nosnippet>
  <p>Except as otherwise noted, the content of this page is licensed under the <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 License</a>, and code samples are licensed under the <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a>. For details, see the <a href="https://developers.google.com/site-policies">Google Developers Site Policies</a>. Java is a registered trademark of Oracle and/or its affiliates.</p>
  <p>Last updated 2026-08-27 UTC.</p>
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
  
  <ul class="devsite-footer-linkboxes-list">
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Products and pricing</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/products/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-metadata-position="footer"track-metadata-child_headline="products and pricing"track-type="footer link"track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/products/"track-name="see all products">
            
          
            See all products
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/pricing/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-type="footer link"track-metadata-eventDetail="cloud.google.com/pricing/"track-name="google cloud pricing"track-metadata-position="footer"track-metadata-child_headline="products and pricing"track-metadata-module="footer">
            
          
            Google Cloud pricing
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/marketplace/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-child_headline="resources"track-metadata-module="footer"track-name="google cloud marketplace"track-metadata-eventDetail="cloud.google.com/marketplace/"track-type="footer link"track-metadata-position="footer">
            
          
            Google Cloud Marketplace
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/contact/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-child_headline="engage"track-metadata-position="footer"track-type="footer link"track-name="contact sales"track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/contact/">
            
              
              
            
          
            Contact sales
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Support</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//discuss.google.dev/c/google-cloud/14/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-type="footer link"target="_blank"track-name="google cloud community"track-metadata-eventDetail="www.googlecloudcommunity.com"track-metadata-position="footer"track-metadata-module="footer"track-metadata-child_headline="engage"rel="noopener">
            
          
            Community forums
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/support-hub/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-type="footer link"track-metadata-child_headline="resources"track-metadata-module="footer"track-metadata-position="footer"track-name="support"track-metadata-eventDetail="cloud.google.com/support-hub/">
            
          
            Support
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//docs.cloud.google.com/release-notes"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-type="footer link"track-name="release notes"track-metadata-module="footer"track-metadata-position="footer"track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/release-notes/">
            
          
            Release Notes
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//status.cloud.google.com"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-module="footer"track-metadata-child_headline="resources"track-name="system status"track-metadata-position="footer"track-type="footer link"target="_blank"track-metadata-eventDetail="status.cloud.google.com">
            
              
              
            
          
            System status
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Resources</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//github.com/googlecloudPlatform/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-type="footer link"track-metadata-eventDetail="github.com/googlecloudPlatform/"track-name="github"track-metadata-module="footer"track-metadata-position="footer"track-metadata-child_headline="resources">
            
          
            GitHub
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/get-started/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-module="footer"track-metadata-position="footer"track-type="footer link"track-metadata-child_headline="resources"track-name="google cloud quickstarts"track-metadata-eventDetail="cloud.google.com/docs/get-started/">
            
          
            Getting Started with Google Cloud
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/samples"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-child_headline="resources"track-name="code samples"track-metadata-position="footer"track-type="footer link"track-metadata-eventDetail="cloud.google.com/docs/samples"track-metadata-module="footer">
            
          
            Code samples
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/architecture/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-module="footer"track-type="footer link"track-name="cloud architecture center"track-metadata-eventDetail="cloud.google.com/architecture/"track-metadata-child_headline="resources"track-metadata-position="footer">
            
          
            Cloud Architecture Center
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/learn/training/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            track-type="footer link"track-name="training"track-metadata-position="footer"track-metadata-module="footer"track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/learn/training/">
            
              
              
            
          
            Training and Certification
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Engage</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/blog/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-name="blog"track-type="footer link"track-metadata-module="footer"track-metadata-position="footer"track-metadata-child_headline="engage"track-metadata-eventDetail="cloud.google.com/blog/">
            
          
            Blog
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/events/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-eventDetail="cloud.google.com/events/"track-metadata-position="footer"track-type="footer link"track-metadata-child_headline="engage"track-name="events"track-metadata-module="footer">
            
          
            Events
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//x.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-position="footer"track-metadata-eventDetail="x.com/googlecloud"track-type="footer link"track-metadata-child_headline="engage"target="_blank"rel="noopener"track-name="follow on x"track-metadata-module="footer">
            
          
            X (Twitter)
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            rel="noopener"track-metadata-module="footer"track-name="google cloud on youtube"target="_blank"track-metadata-child_headline="engage"track-type="footer link"track-metadata-eventDetail="www.youtube.com/googlecloud"track-metadata-position="footer">
            
          
            Google Cloud on YouTube
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloudplatform"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            rel="noopener"track-metadata-position="footer"target="_blank"track-name="google cloud tech on youtube"track-metadata-module="footer"track-type="footer link"track-metadata-child_headline="engage"track-metadata-eventDetail="www.youtube.com/googlecloudplatform">
            
              
              
            
          
            Google Cloud Tech on YouTube
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
  </ul>
  
</nav>
          
        </devsite-footer-linkboxes>
        <devsite-footer-utility class="devsite-footer">
          
            

<div class="devsite-footer-utility nocontent" data-nosnippet>
  

  
  <nav class="devsite-footer-utility-links" aria-label="Utility links">
    
    <ul class="devsite-footer-utility-list">
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//about.google/"
           data-category="Site-Wide Custom Events"
           data-label="Footer About Google link"
         
           track-name="about google"
         
           target="_blank"
         
           track-type="footer link"
         
           track-metadata-position="footer"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="//about.google/"
         >
          About Google
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-privacy-link">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/privacy"
           data-category="Site-Wide Custom Events"
           data-label="Footer Privacy link"
         
           target="_blank"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="//policies.google.com/privacy"
         
           track-type="footer link"
         
           track-name="privacy"
         
           track-metadata-position="footer"
         >
          Privacy
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/terms?hl=en"
           data-category="Site-Wide Custom Events"
           data-label="Footer Site terms link"
         
           target="_blank"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="//www.google.com/intl/en/policies/terms/regional.html"
         
           track-metadata-position="footer"
         
           track-type="footer link"
         
           track-name="site terms"
         >
          Site terms
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//cloud.google.com/product-terms"
           data-category="Site-Wide Custom Events"
           data-label="Footer Google Cloud terms link"
         
           track-metadata-eventDetail="//cloud.google.com/product-terms"
         
           track-metadata-module="utility footer"
         
           track-name="google cloud terms"
         
           track-metadata-position="footer"
         
           track-type="footer link"
         >
          Google Cloud terms
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 glue-cookie-notification-bar-control">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="#"
           data-category="Site-Wide Custom Events"
           data-label="Footer Manage cookies link"
         
           aria-hidden="true"
         
           track-metadata-position="footer"
         
           track-metadata-eventDetail="#"
         
           track-name="Manage cookies"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         >
          Manage cookies
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-carbon-button">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//cloud.google.com/sustainability"
           data-category="Site-Wide Custom Events"
           data-label="Footer Our third decade of climate action: join us link"
         
           track-metadata-module="utility footer"
         
           track-name="Our third decade of climate action: join us"
         
           track-metadata-position="footer"
         
           track-metadata-eventDetail="/sustainability/"
         
           track-type="footer link"
         >
          Our third decade of climate action: join us
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-utility-button">
        
        <span class="devsite-footer-utility-description">Sign up for the Google Cloud newsletter</span>
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//cloud.google.com/newsletter/"
           data-category="Site-Wide Custom Events"
           data-label="Footer Subscribe link"
         
           track-metadata-position="footer"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="/newsletter/"
         
           track-name="subscribe"
         >
          Subscribe
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
      <a role="menuitem" lang="es"
        >Español</a>
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
      <a role="menuitem" lang="pt"
        >Português</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="he"
        >עברית</a>
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
    
    
    
<cloudx-user></cloudx-user>




  
    <cloudx-free-trial-eligible-store freeTrialEligible="true"></cloudx-free-trial-eligible-store>
  

    


    <devsite-a11y-announce></devsite-a11y-announce>
  </body>
</html>