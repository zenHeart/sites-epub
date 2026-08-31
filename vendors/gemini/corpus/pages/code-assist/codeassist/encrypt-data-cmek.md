








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/images/favicons/onecloud/super_cloud.png"><link rel="canonical" href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek"><link rel="search" type="application/opensearchdescription+xml"
            title="Google Cloud Documentation" href="https://docs.cloud.google.com/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek" /><link rel="alternate" hreflang="x-default" href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek" /><link rel="alternate" hreflang="zh-Hans"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=zh-tw" /><link rel="alternate" hreflang="fr"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=de" /><link rel="alternate" hreflang="he"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=he" /><link rel="alternate" hreflang="id"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=id" /><link rel="alternate" hreflang="it"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=ko" /><link rel="alternate" hreflang="pt-BR"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=pt-br" /><link rel="alternate" hreflang="pt"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=pt" /><link rel="alternate" hreflang="es"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=es" /><link rel="alternate" hreflang="es-419"
          href="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek?hl=es-419" /><link rel="alternate" hreflang="en-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek" /><link rel="alternate" hreflang="x-default" href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek" /><link rel="alternate" hreflang="zh-Hans-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=zh-tw" /><link rel="alternate" hreflang="fr-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=fr" /><link rel="alternate" hreflang="de-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=de" /><link rel="alternate" hreflang="he-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=he" /><link rel="alternate" hreflang="id-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=id" /><link rel="alternate" hreflang="it-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=it" /><link rel="alternate" hreflang="ja-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=ja" /><link rel="alternate" hreflang="ko-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=ko" /><link rel="alternate" hreflang="pt-BR-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=pt-br" /><link rel="alternate" hreflang="pt-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=pt" /><link rel="alternate" hreflang="es-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=es" /><link rel="alternate" hreflang="es-419-cn"
          href="https://docs.cloud.google.cn/gemini/docs/codeassist/encrypt-data-cmek?hl=es-419" /><title>Encrypt data with customer-managed encryption keys &nbsp;|&nbsp; Gemini for Google Cloud &nbsp;|&nbsp; Google Cloud Documentation</title>

<meta property="og:title" content="Encrypt data with customer-managed encryption keys &nbsp;|&nbsp; Gemini for Google Cloud &nbsp;|&nbsp; Google Cloud Documentation"><meta name="description" content="Shows how to encrypt data with customer-managed encryption keys (CMEK).">
  <meta property="og:description" content="Shows how to encrypt data with customer-managed encryption keys (CMEK)."><meta property="og:url" content="https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek"><meta property="og:image" content="https://docs.cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png">
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
    
      
        referrerpolicy="no-referrer-when-downgrade"
      
        track-metadata-eventDetail="nav"
      
        track-name="console"
      
        track-metadata-position="nav"
      
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
      
        track-metadata-eventDetail="nav"
      
        track-type="freeTrial"
      
    
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
    

    
      
        referrerpolicy="no-referrer-when-downgrade"
      
        track-metadata-eventDetail="nav"
      
        track-name="console"
      
        track-metadata-position="nav"
      
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
      Encrypt data with customer-managed encryption keys<devsite-actions hidden data-nosnippet><devsite-feature-tooltip
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

  
    
    
    
    

<p>This document shows how to use customer-managed encryption keys (CMEK) to
encrypt and control data-at-rest in a cloud service through
<a href="/kms/docs">Cloud Key Management Service</a>. CMEK is integrated with
<a href="/gemini/docs/codeassist/code-customization-overview">code customization</a> for
Gemini Code Assist. Gemini Code Assist doesn&#39;t support the use
of <a href="/kms/docs/ekm">Cloud EKM</a> keys.</p>

<p>In this document, you do the following:</p>

<ul>
<li>Learn how to create a CMEK.</li>
<li>Grant permissions to the Gemini Code Assist service account.</li>
<li>Create a code repository index with a CMEK.</li>
<li>Remove access to a CMEK repository.</li>
</ul>





















  





















  






  




  




<p>By default, Gemini for Google Cloud encrypts customer content at
    rest. Gemini handles encryption for you without any
  additional actions on your part. This option is called <em>Google default encryption</em>.
  </p>

<p>If you want to control your encryption keys, then you can use customer-managed encryption keys
  (CMEKs) in <a href="/kms/docs">Cloud KMS</a> with CMEK-integrated services including
  Gemini. Using Cloud KMS keys gives you control over their protection
  level, location, rotation schedule, usage and access permissions, and cryptographic boundaries.
  Using Cloud KMS also lets
you view audit logs and control key lifecycles.
  
  Instead of Google owning and managing the symmetric
  <a href="/kms/docs/envelope-encryption#key_encryption_keys">key encryption keys (KEKs)</a> that protect your data, you control and
  manage these keys in Cloud KMS.</p>

<p>After you set up your resources with CMEKs, the experience of accessing your
  Gemini resources is similar to using Google default encryption.
  For more information about your encryption
  options, see <a href="/kms/docs/cmek">Customer-managed encryption keys (CMEK)</a>.</p>





<h2 id="before_you_begin" data-text="Before you begin" tabindex="-1">Before you begin</h2>




<ol>
<li>
















  





  
    
  
    
    <p>In the Google Cloud console, activate Cloud Shell.</p>
    <p><a
       href="https://console.cloud.google.com/?cloudshell=true"
       target="console" track-type="commonIncludes"
       track-name="consoleLink"
       track-metadata-end-goal="launchCloudShell"
       class="button button-primary">Activate Cloud Shell</a></p>
    
  

  








</li>
<li><p>In the development environment where you set up the gcloud CLI, run the
<a href="/sdk/gcloud/reference/components/update"><code translate="no" dir="ltr">gcloud components update</code> command</a>
to make sure that you have updated all installed components of the
<a href="/sdk/gcloud">gcloud CLI</a> to the latest version.</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">gcloud<span class="devsite-syntax-w"> </span>components<span class="devsite-syntax-w"> </span>update
</code></pre></devsite-code></li>
</ol>

<h2 id="create_a_cmek_and_grant_permissions" data-text="Create a CMEK and grant permissions" tabindex="-1">Create a CMEK and grant permissions</h2>

<p>To create a CMEK and grant the Gemini Code Assist service account
permissions on the key, perform the following tasks:</p>
<ol>
<li><p>In the Google Cloud project where you want to manage your keys, do the
following:</p>

<ol>
<li><p><a href="https://console.cloud.google.com/flows/enableapi?apiid=cloudkms.googleapis.com&amp;redirect=https://console.cloud.google.com/">Enable the Cloud Key Management Service API</a>.</p></li>
<li><p>Create the <a href="/kms/docs/create-key-ring">key ring</a> and
<a href="/kms/docs/create-key">key</a> directly in Cloud KMS.</p></li>
</ol></li>
<li><p>Grant the <a href="/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter">CryptoKey Encrypter/Decrypter IAM role</a>
(<code translate="no" dir="ltr">roles/cloudkms.cryptoKeyEncrypterDecrypter</code>) to the
Gemini Code Assist service account. Grant this permission on
the key that you created.</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="console" data-text=" Console " tabindex="-1"> Console </h3><ol>
<li><p>Go to <strong>Key management</strong>.</p>

<p><a href="https://console.cloud.google.com/security/kms" target="console" class="button button-primary">Go to Key management</a> </p></li>
<li><p>Select the key that you created.</p></li>
<li><p>Grant access to the Gemini Code Assist service account:</p>

<ol>
<li>Click <strong>Add principal</strong>.</li>
<li>Add the Gemini Code Assist service account. The
service account is <code translate="no" dir="ltr">service-<var translate="no">PROJECT_NUMBER</var>@gcp-sa-cloudaicompanions.iam.gserviceaccount.com</code>,
where <var translate="no">PROJECT_NUMBER</var> is the
<a href="/resource-manager/docs/creating-managing-projects#identifying_projects">project number</a>
of the Google Cloud project where
Gemini Code Assist is enabled.</li>
<li>In <strong>Select a role</strong>, select <strong>Cloud KMS</strong> &gt;
<strong>Cloud KMS CryptoKey Encrypter/Decrypter</strong>.</li>
<li>Click <strong>Save</strong>.</li>
</ol></li>
<li><p>Repeat the previous step to grant access to the account that will
create the code repository index with a CMEK.</p></li>
<li><p>Return to the <strong><a href="https://console.cloud.google.com/security/kms">Key management</a></strong>
page and select the key again.</p></li>
<li><p>Select <strong>Show info panel</strong>. You should see roles in the
<strong>Role/Member</strong> column.</p></li>
</ol></section>
<section><h3 id="gcloud-cli" data-text=" gcloud CLI " tabindex="-1"> gcloud CLI </h3><ol>
<li><p>To grant access to the Gemini Code Assist service
account, in a shell environment, use the
<a href="/sdk/gcloud/reference/projects/add-iam-policy-binding"><code translate="no" dir="ltr">kms keys add-iam-policy-binding</code>command</a>:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded><code translate="no" dir="ltr">gcloud kms keys add-iam-policy-binding <var translate="no">KEY_NAME</var> \
    --project=<var translate="no">PROJECT_ID</var> \
    --location=<var translate="no">LOCATION</var> \
    --keyring=<var translate="no">KEYRING_NAME</var> \
    --member=&#34;serviceAccount:service-<var translate="no">PROJECT_NUMBER</var>@gcp-sa-cloudaicompanion.iam.gserviceaccount.com&#34; \
    --role=&#34;roles/cloudkms.cryptoKeyEncrypterDecrypter&#34;
</code></pre></devsite-code>
<p>Replace the following:</p>

<ul>
<li><var translate="no">KEY_NAME</var>: the key name.</li>
<li><var translate="no">PROJECT_ID</var>: the ID of the project that contains the key.</li>
<li><var translate="no">LOCATION</var>: the key location.</li>
<li><var translate="no">KEYRING_NAME</var>: the key ring name.</li>
<li><var translate="no">PROJECT_NUMBER</var>: the <a href="/resource-manager/docs/creating-managing-projects#identifying_projects">project number</a>
of the Google Cloud project with
Gemini Code Assist enabled.</li>
</ul></li>
<li><p>Repeat the previous step to grant access to the account that will
create the code repository index with a CMEK.</p></li>
</ol>

<p>For more information about this command, see the
<a href="/sdk/gcloud/reference/kms/keys/add-iam-policy-binding"><code translate="no" dir="ltr">gcloud kms keys add-iam-policy-binding</code> documentation</a>.</p></section>
</devsite-selector></div></li>
</ol>
<p>You can now
<a href="#create_a_code_repository_index_with_a_cmek">create a code repository index with a CMEK</a>
using the API, and specify the key to use for encryption.</p>

<h2 id="create_a_code_repository_index_with_a_cmek" data-text="Create a code repository index with a CMEK" tabindex="-1">Create a code repository index with a CMEK</h2>

<p>To create a new repository that has CMEK protection, do one of the following:</p>
<div><devsite-selector data-ds-scope="code-sample">
<section><h3 id="gcloud-cli_1" data-text=" gcloud CLI " tabindex="-1"> gcloud CLI </h3><p>Use the <a href="/sdk/gcloud/reference/gemini/code-repository-indexes/create"><code translate="no" dir="ltr">gemini code-repository-indexes create</code> command</a>:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded><code translate="no" dir="ltr">gcloud gemini code-repository-indexes create <var translate="no">CODE_REPOSITORY_INDEX_NAME</var> \
    --location=<var translate="no">LOCATION</var> \
    --kms-key=&#34;projects/<var translate="no">KEY_PROJECT_ID</var>/locations/<var translate="no">LOCATION</var>/keyRings/<var translate="no">KEYRING_NAME</var>/cryptoKeys/<var translate="no">KEY_NAME</var>&#34;
</code></pre></devsite-code>
<p>Replace the following:</p>

<ul>
<li><var translate="no">CODE_REPOSITORY_INDEX_NAME</var>: the name of the new code repository
index that you&#39;ll create.</li>
<li><var translate="no">LOCATION</var>: the key location.</li>
<li><var translate="no">KEY_PROJECT_ID</var>: the key project ID.</li>
<li><var translate="no">KEYRING_NAME</var>: the key ring name.</li>
<li><var translate="no">KEY_NAME</var>: the key name.</li>
</ul></section>
<section><h3 id="api" data-text=" API " tabindex="-1"> API </h3><ol>
<li><p>Create a JSON file that contains the following information:</p>

<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded>
  {
    "kmsKey": "projects/<var translate="no">KEY_PROJECT_ID</var>/locations/<var translate="no">KEY_LOCATION</var>/keyRings/<var translate="no">KEYRING_NAME</var>/cryptoKeys/<var translate="no">KEY_NAME</var>"
  }
</pre></devsite-code>

<p>Replace the following:</p>

<ul>
<li><code translate="no" dir="ltr"><var translate="no">KEY_PROJECT_ID</var></code>: the key project ID</li>
<li><code translate="no" dir="ltr"><var translate="no">KEY_LOCATION</var></code>: the key location</li>
<li><code translate="no" dir="ltr"><var translate="no">KEYRING_NAME</var></code>: the key ring name</li>
<li><code translate="no" dir="ltr"><var translate="no">KEY_NAME</var></code>: the key name</li>
</ul></li>
<li><p>Use a <a href="http://curl.haxx.se/"><code translate="no" dir="ltr">cURL</code></a> command to call the
<a href="/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes/create"><code translate="no" dir="ltr">projects.locations.codeRepositoryIndexes.create</code> method</a>:</p>

<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded>curl -X POST --data-binary @<var translate="no">JSON_FILE_NAME</var> \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://cloudaicompanion.googleapis.com/v1/projects/<var translate="no">PROJECT_ID</var>/locations/<var translate="no">KEY_LOCATION</var>/codeRepositoryIndexes?codeRepositoryIndexId=<var translate="no">CODE_REPOSITORY_INDEX_NAME</var>"</pre></devsite-code>

<p>Replace the following:</p>

<ul>
<li><code translate="no" dir="ltr"><var translate="no">JSON_FILE_NAME</var></code>: the path for the
JSON file that you created in the preceding step.</li>
<li><code translate="no" dir="ltr"><var translate="no">PROJECT_ID</var></code>: the ID of the project to create
the repository in.</li>
<li><code translate="no" dir="ltr"><var translate="no">KEY_LOCATION</var></code>: the location to create the
repository in, which must match the location where the CMEK exists.</li>
<li><code translate="no" dir="ltr"><var translate="no">CODE_REPOSITORY_INDEX_NAME</var></code>: the name of the
new code repository index that you&#39;ll create. For example,
<code translate="no" dir="ltr">zg-btf-0001</code>.</li>
</ul></li>
</ol>

<p>The response returns a set of log entries.</p></section>
</devsite-selector></div>
<h2 id="remove_access_to_a_cmek_repository" data-text="Remove access to a CMEK repository" tabindex="-1">Remove access to a CMEK repository</h2>
<aside class="warning"><strong>Warning:</strong><span> If you disable the CMEK, Google Cloud removes the instance and
the service will no longer be available, even if you re-enable the key.</span></aside>
<p>There are several ways to remove access to a CMEK-encrypted repository:</p>

<ul>
<li>Revoke the Cloud KMS CryptoKey Encrypter/Decrypter
<a href="/kms/docs/reference/permissions-and-roles#predefined_roles">role</a> from the
Gemini Code Assist service account using the
<a href="/iam/docs/granting-changing-revoking-access#revoke_access">Google Cloud console</a>
or the <a href="/iam/docs/granting-changing-revoking-access#revoking-gcloud-manual">gcloud CLI</a>.</li>
<li><a href="/kms/docs/enable-disable#disable_an_enabled_key_version">Temporarily disable</a>
the CMEK.</li>
<li><a href="/kms/docs/destroy-restore#schedule_a_key_version_for_destruction_destroy_a_key_version">Permanently destroy</a>
the CMEK.</li>
</ul>

<p>We recommend that you revoke the permissions from the
Gemini Code Assist service account before disabling or destroying
a key. Changes to permissions are consistent within seconds, so you can observe
the impacts of disabling or destroying a key.</p>


  
  

  
    <devsite-hats-survey class="nocontent" data-nosnippet
      hats-id="mwETRvWii0eU5NUYprb0Y9z5GVbc"
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
  
  <ul class="devsite-footer-linkboxes-list">
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Products and pricing</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/products/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-type="footer link"track-metadata-module="footer"track-metadata-position="footer"track-name="see all products"track-metadata-eventDetail="cloud.google.com/products/"track-metadata-child_headline="products and pricing">
            
          
            See all products
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/pricing/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-position="footer"track-metadata-eventDetail="cloud.google.com/pricing/"track-type="footer link"track-name="google cloud pricing"track-metadata-module="footer"track-metadata-child_headline="products and pricing">
            
          
            Google Cloud pricing
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/marketplace/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-eventDetail="cloud.google.com/marketplace/"track-metadata-position="footer"track-name="google cloud marketplace"track-metadata-module="footer"track-type="footer link"track-metadata-child_headline="resources">
            
          
            Google Cloud Marketplace
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/contact/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-type="footer link"track-name="contact sales"track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/contact/"track-metadata-position="footer"track-metadata-child_headline="engage">
            
              
              
            
          
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
            track-metadata-child_headline="engage"track-name="google cloud community"rel="noopener"track-metadata-position="footer"track-type="footer link"track-metadata-eventDetail="www.googlecloudcommunity.com"track-metadata-module="footer"target="_blank">
            
          
            Community forums
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/support-hub/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-module="footer"track-metadata-position="footer"track-name="support"track-type="footer link"track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/support-hub/">
            
          
            Support
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//docs.cloud.google.com/release-notes"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-child_headline="resources"track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/release-notes/"track-type="footer link"track-metadata-position="footer"track-name="release notes">
            
          
            Release Notes
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//status.cloud.google.com"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-eventDetail="status.cloud.google.com"track-metadata-module="footer"track-metadata-position="footer"target="_blank"track-type="footer link"track-name="system status"track-metadata-child_headline="resources">
            
              
              
            
          
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
            track-metadata-child_headline="resources"track-type="footer link"track-name="github"track-metadata-position="footer"track-metadata-eventDetail="github.com/googlecloudPlatform/"track-metadata-module="footer">
            
          
            GitHub
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/get-started/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-module="footer"track-metadata-child_headline="resources"track-name="google cloud quickstarts"track-metadata-eventDetail="cloud.google.com/docs/get-started/"track-type="footer link"track-metadata-position="footer">
            
          
            Getting Started with Google Cloud
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/samples"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-position="footer"track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/docs/samples"track-type="footer link"track-metadata-module="footer"track-name="code samples">
            
          
            Code samples
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/architecture/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-position="footer"track-name="cloud architecture center"track-metadata-eventDetail="cloud.google.com/architecture/"track-metadata-module="footer"track-type="footer link"track-metadata-child_headline="resources">
            
          
            Cloud Architecture Center
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/learn/training/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            track-name="training"track-type="footer link"track-metadata-module="footer"track-metadata-child_headline="resources"track-metadata-position="footer"track-metadata-eventDetail="cloud.google.com/learn/training/">
            
              
              
            
          
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
            track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/blog/"track-metadata-child_headline="engage"track-type="footer link"track-name="blog"track-metadata-position="footer">
            
          
            Blog
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/events/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-child_headline="engage"track-metadata-eventDetail="cloud.google.com/events/"track-name="events"track-metadata-position="footer"track-type="footer link"track-metadata-module="footer">
            
          
            Events
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//x.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-position="footer"track-name="follow on x"track-metadata-child_headline="engage"rel="noopener"track-type="footer link"track-metadata-module="footer"track-metadata-eventDetail="x.com/googlecloud"target="_blank">
            
          
            X (Twitter)
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-name="google cloud on youtube"track-type="footer link"track-metadata-position="footer"track-metadata-eventDetail="www.youtube.com/googlecloud"track-metadata-child_headline="engage"rel="noopener"track-metadata-module="footer"target="_blank">
            
          
            Google Cloud on YouTube
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloudplatform"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            track-metadata-child_headline="engage"track-metadata-position="footer"target="_blank"rel="noopener"track-metadata-eventDetail="www.youtube.com/googlecloudplatform"track-metadata-module="footer"track-type="footer link"track-name="google cloud tech on youtube">
            
              
              
            
          
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
         
           track-metadata-position="footer"
         
           track-metadata-eventDetail="//about.google/"
         
           target="_blank"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           track-name="about google"
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
         
           track-metadata-module="utility footer"
         
           track-metadata-position="footer"
         
           track-type="footer link"
         
           track-name="privacy"
         
           target="_blank"
         
           track-metadata-eventDetail="//policies.google.com/privacy"
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
         
           track-metadata-eventDetail="//www.google.com/intl/en/policies/terms/regional.html"
         
           track-metadata-module="utility footer"
         
           target="_blank"
         
           track-type="footer link"
         
           track-metadata-position="footer"
         
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
         
           track-metadata-position="footer"
         
           track-metadata-module="utility footer"
         
           track-type="footer link"
         
           track-name="google cloud terms"
         
           track-metadata-eventDetail="//cloud.google.com/product-terms"
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
         
           track-metadata-position="footer"
         
           track-metadata-module="utility footer"
         
           track-name="Manage cookies"
         
           aria-hidden="true"
         
           track-type="footer link"
         
           track-metadata-eventDetail="#"
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
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           track-name="Our third decade of climate action: join us"
         
           track-metadata-position="footer"
         
           track-metadata-eventDetail="/sustainability/"
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
         
           track-name="subscribe"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="/newsletter/"
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