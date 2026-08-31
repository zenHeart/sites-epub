








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
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/clouddocs/images/favicons/onecloud/super_cloud.png"><link rel="canonical" href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github"><link rel="search" type="application/opensearchdescription+xml"
            title="Google Cloud Documentation" href="https://docs.cloud.google.com/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github" /><link rel="alternate" hreflang="x-default" href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github" /><link rel="alternate" hreflang="zh-Hans"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=zh-tw" /><link rel="alternate" hreflang="fr"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=de" /><link rel="alternate" hreflang="he"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=he" /><link rel="alternate" hreflang="id"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=id" /><link rel="alternate" hreflang="it"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=ko" /><link rel="alternate" hreflang="pt-BR"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=pt-br" /><link rel="alternate" hreflang="es-419"
          href="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github?hl=es-419" /><link rel="alternate" hreflang="en-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github" /><link rel="alternate" hreflang="x-default" href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github" /><link rel="alternate" hreflang="zh-Hans-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=zh-tw" /><link rel="alternate" hreflang="fr-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=fr" /><link rel="alternate" hreflang="de-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=de" /><link rel="alternate" hreflang="he-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=he" /><link rel="alternate" hreflang="id-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=id" /><link rel="alternate" hreflang="it-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=it" /><link rel="alternate" hreflang="ja-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=ja" /><link rel="alternate" hreflang="ko-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=ko" /><link rel="alternate" hreflang="pt-BR-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=pt-br" /><link rel="alternate" hreflang="es-419-cn"
          href="https://docs.cloud.google.cn/gemini/docs/code-review/use-code-assist-github?hl=es-419" /><title>Use Gemini Code Assist on GitHub &nbsp;|&nbsp; Gemini for Google Cloud &nbsp;|&nbsp; Google Cloud Documentation</title>

<meta property="og:title" content="Use Gemini Code Assist on GitHub &nbsp;|&nbsp; Gemini for Google Cloud &nbsp;|&nbsp; Google Cloud Documentation"><meta name="description" content="Review pull requests using Gemini Code Assist.">
  <meta property="og:description" content="Review pull requests using Gemini Code Assist."><meta property="og:url" content="https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github"><meta property="og:image" content="https://docs.cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png">
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
    
      
        track-type="globalNav"
      
        track-metadata-position="nav"
      
        referrerpolicy="no-referrer-when-downgrade"
      
        track-metadata-eventDetail="nav"
      
        track-name="console"
      
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
    
    
      
        track-type="freeTrial"
      
        track-metadata-position="nav"
      
        track-name="gcpCta"
      
        referrerpolicy="no-referrer-when-downgrade"
      
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
    

    
      
        track-type="globalNav"
      
        track-metadata-position="nav"
      
        referrerpolicy="no-referrer-when-downgrade"
      
        track-metadata-eventDetail="nav"
      
        track-name="console"
      
    
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
      Use Gemini Code Assist on GitHub<devsite-actions hidden data-nosnippet><devsite-feature-tooltip
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

  
    
    
    
    

<p>This page shows you how to use
<a href="/gemini/docs/code-review/review-repo-code">Gemini Code Assist on GitHub</a>.</p>

<h2 id="before-you-begin" data-text="Before you begin" tabindex="-1">Before you begin</h2>

<p>To complete the tasks in this page, make sure you have
<a href="/gemini/docs/code-review/set-up-code-assist-github">set up Gemini Code Assist on GitHub</a>.</p>

<h2 id="get-pull-request-summary-and-feedback" data-text="Get pull request summary and feedback" tabindex="-1">Get pull request summary and feedback</h2>

<p>To get an initial review for a pull request from
Gemini Code Assist, create a new pull request.</p>

<p>When you open the new pull request, Gemini Code Assist provides
an initial review. After the review is ready,
<code translate="no" dir="ltr">gemini-code-assist[bot]</code> is automatically added as a reviewer to the pull
request. Gemini Code Assist adds an issue comment in the
<strong>Conversation</strong> tab of the pull request with its feedback and proceeds to add
comments about modified portions of the code.</p>

<p>Review comments contain the following information:</p>

<ul>
<li>Severity of the issue, given as Critical, High, Medium, and Low</li>
<li>Feedback on the issue</li>
<li>Code suggestion that can be committed directly from GitHub</li>
<li>References to a <a href="/gemini/docs/code-review/style-guide">user-provided style guide</a></li>
</ul>

<p>Gemini Code Assist does not add comments that have a <em>severity</em>
less than the minimum severity threshold that is
<a href="/gemini/docs/code-review/customize-repo-review">set for the repository</a>.</p>

<h2 id="manually-invoke-gemini-code-assist" data-text="Manually invoke Gemini Code Assist" tabindex="-1">Manually invoke Gemini Code Assist</h2>

<p>Gemini Code Assist listens to comments from any pull request
contributor, and decides whether it should respond.</p>

<p>To manually invoke Gemini Code Assist, you can use the
following commands in the main comments page on the pull request as an issue
comment.</p>

<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>

<tbody>
<tr>
<td><code translate="no" dir="ltr">/gemini summary</code></td>
<td>Posts a summary of the changes in the pull request</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">/gemini review</code></td>
<td>Posts a code review of the changes in the pull request</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">/gemini</code></td>
<td>Manually invokes Gemini Code Assist in comments</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">/gemini help</code></td>
<td>Overview of the available commands</td>
</tr>
</tbody>
</table>

<h2 id="manage-gemini-code-settings" data-text="Manage the Gemini Code Assist settings" tabindex="-1">Manage the Gemini Code Assist settings</h2>

<p>Anyone with permissions to modify GitHub App settings for the
organization can manage the Gemini Code Assist app settings. You can
review the permissions provided to the Gemini Code Assist app, manage
repository access, and uninstall the Gemini Code Assist app.</p>

<p>To modify the settings, follow these steps:</p>

<ol>
<li>On GitHub, click your profile photo and then click <strong>Settings</strong>.</li>
<li>In the <strong>Integrations</strong> section, click <strong>Applications</strong>.
A list of GitHub Apps is displayed.</li>
<li>Beside Gemini Code Assist, click <strong>Configure</strong>.</li>
</ol>

<h2 id="troubleshooting" data-text="Troubleshooting" tabindex="-1">Troubleshooting</h2>

<p>If you&#39;re not receiving responses from Gemini Code Assist, it
might be because the Google Cloud project that you used during setup isn&#39;t
connected to a valid billing account. You should
<a href="/billing/docs/how-to/verify-billing-enabled">verify the billing status of your project</a>
and, if necessary, connect your project to a valid billing account.</p>

<p>Note that Developer Connect has a large
<a href="/developer-connect/pricing">free tier</a>, and there are no charges for using
Gemini Code Assist on GitHub during Preview. While a
valid billing account is required, it only accrues charges when usage goes over
the free tier limits.</p>

<h2 id="whats_next" data-text="What's next" tabindex="-1">What's next</h2>

<ul>
<li>Learn more about <a href="/gemini/docs/code-review/review-repo-code">Gemini Code Assist on GitHub</a>.</li>
<li><a href="/gemini/docs/code-review/set-up-code-assist-github">Set up Gemini Code Assist on GitHub</a>.</li>
<li>Learn how to
<a href="/gemini/docs/code-review/customize-repo-review">customize Gemini Code Assist on GitHub behavior</a>.</li>
</ul>


  
  

  
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
            track-metadata-module="footer"track-name="see all products"track-metadata-child_headline="products and pricing"track-type="footer link"track-metadata-position="footer"track-metadata-eventDetail="cloud.google.com/products/">
            
          
            See all products
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/pricing/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-name="google cloud pricing"track-metadata-eventDetail="cloud.google.com/pricing/"track-metadata-child_headline="products and pricing"track-metadata-position="footer"track-metadata-module="footer"track-type="footer link">
            
          
            Google Cloud pricing
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/marketplace/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/marketplace/"track-name="google cloud marketplace"track-metadata-position="footer"track-type="footer link"track-metadata-child_headline="resources">
            
          
            Google Cloud Marketplace
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/contact/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-child_headline="engage"track-name="contact sales"track-metadata-module="footer"track-type="footer link"track-metadata-position="footer"track-metadata-eventDetail="cloud.google.com/contact/">
            
              
              
            
          
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
            track-metadata-eventDetail="www.googlecloudcommunity.com"track-metadata-child_headline="engage"rel="noopener"track-type="footer link"track-metadata-position="footer"track-name="google cloud community"target="_blank"track-metadata-module="footer">
            
          
            Community forums
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/support-hub/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-type="footer link"track-metadata-eventDetail="cloud.google.com/support-hub/"track-metadata-position="footer"track-metadata-child_headline="resources"track-metadata-module="footer"track-name="support">
            
          
            Support
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//docs.cloud.google.com/release-notes"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-type="footer link"track-metadata-module="footer"track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/release-notes/"track-name="release notes"track-metadata-position="footer">
            
          
            Release Notes
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//status.cloud.google.com"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-position="footer"target="_blank"track-type="footer link"track-metadata-child_headline="resources"track-metadata-module="footer"track-name="system status"track-metadata-eventDetail="status.cloud.google.com">
            
              
              
            
          
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
            track-metadata-eventDetail="github.com/googlecloudPlatform/"track-name="github"track-metadata-module="footer"track-metadata-child_headline="resources"track-metadata-position="footer"track-type="footer link">
            
          
            GitHub
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/get-started/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-child_headline="resources"track-name="google cloud quickstarts"track-metadata-eventDetail="cloud.google.com/docs/get-started/"track-type="footer link"track-metadata-position="footer"track-metadata-module="footer">
            
          
            Getting Started with Google Cloud
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/samples"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-module="footer"track-name="code samples"track-metadata-eventDetail="cloud.google.com/docs/samples"track-metadata-position="footer"track-metadata-child_headline="resources"track-type="footer link">
            
          
            Code samples
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/architecture/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-name="cloud architecture center"track-metadata-position="footer"track-type="footer link"track-metadata-child_headline="resources"track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/architecture/">
            
          
            Cloud Architecture Center
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/learn/training/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            track-type="footer link"track-metadata-position="footer"track-metadata-child_headline="resources"track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/learn/training/"track-name="training">
            
              
              
            
          
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
            track-metadata-position="footer"track-metadata-child_headline="engage"track-type="footer link"track-name="blog"track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/blog/">
            
          
            Blog
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/events/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-type="footer link"track-metadata-eventDetail="cloud.google.com/events/"track-metadata-child_headline="engage"track-metadata-position="footer"track-name="events"track-metadata-module="footer">
            
          
            Events
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//x.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-eventDetail="x.com/googlecloud"track-type="footer link"track-metadata-module="footer"track-metadata-position="footer"track-metadata-child_headline="engage"rel="noopener"target="_blank"track-name="follow on x">
            
          
            X (Twitter)
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-type="footer link"track-metadata-position="footer"track-metadata-child_headline="engage"track-metadata-eventDetail="www.youtube.com/googlecloud"rel="noopener"track-name="google cloud on youtube"track-metadata-module="footer"target="_blank">
            
          
            Google Cloud on YouTube
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloudplatform"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            target="_blank"rel="noopener"track-metadata-position="footer"track-metadata-eventDetail="www.youtube.com/googlecloudplatform"track-name="google cloud tech on youtube"track-type="footer link"track-metadata-module="footer"track-metadata-child_headline="engage">
            
              
              
            
          
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
         
           track-metadata-module="utility footer"
         
           track-name="about google"
         
           track-metadata-eventDetail="//about.google/"
         
           target="_blank"
         
           track-metadata-position="footer"
         
           track-type="footer link"
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
         
           track-name="privacy"
         
           track-metadata-module="utility footer"
         
           track-metadata-position="footer"
         
           target="_blank"
         
           track-type="footer link"
         
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
         
           track-metadata-position="footer"
         
           track-name="site terms"
         
           target="_blank"
         
           track-metadata-module="utility footer"
         
           track-type="footer link"
         
           track-metadata-eventDetail="//www.google.com/intl/en/policies/terms/regional.html"
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
         
           aria-hidden="true"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="#"
         
           track-type="footer link"
         
           track-name="Manage cookies"
         
           track-metadata-position="footer"
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
         
           track-metadata-position="footer"
         
           track-type="footer link"
         
           track-metadata-eventDetail="/sustainability/"
         
           track-metadata-module="utility footer"
         
           track-name="Our third decade of climate action: join us"
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
         
           track-name="subscribe"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="/newsletter/"
         
           track-metadata-position="footer"
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