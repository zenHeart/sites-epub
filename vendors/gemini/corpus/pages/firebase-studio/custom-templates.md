








<!doctype html>
<html 
      lang="en"
      dir="ltr">
  <head>
    <meta name="google-signin-client-id" content="721724668570-nbkv1cfusk7kk4eni4pjvepaus73b13t.apps.googleusercontent.com"><meta name="google-signin-scope"
          content="profile email https://www.googleapis.com/auth/developerprofiles https://www.googleapis.com/auth/developerprofiles.award https://www.googleapis.com/auth/devprofiles.full_control.firstparty"><meta property="og:site_name" content="Firebase">
    <meta property="og:type" content="website"><meta name="theme-color" content="#a8c7fa"><meta charset="utf-8">
    <meta content="IE=Edge" http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    

    <link rel="manifest" href="/_pwa/firebase/manifest.json"
          crossorigin="use-credentials">
    <link rel="preconnect" href="//www.gstatic.com" crossorigin>
    <link rel="preconnect" href="//fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="//www.google-analytics.com" crossorigin><link rel="stylesheet" href="//fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700&display=swap">
      <link rel="stylesheet"
            href="//fonts.googleapis.com/css2?family=Material+Icons&family=Material+Symbols+Outlined&display=block"><link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/css/app.css">
      
        <link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/css/dark-theme.css" disabled>
      <link rel="shortcut icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/favicon.png">
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/touchicon-180.png"><link rel="canonical" href="https://firebase.google.com/docs/studio/custom-templates"><link rel="search" type="application/opensearchdescription+xml"
            title="Firebase" href="https://firebase.google.com/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://firebase.google.com/docs/studio/custom-templates" /><link rel="alternate" hreflang="x-default" href="https://firebase.google.com/docs/studio/custom-templates" /><link rel="alternate" hreflang="ar"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=ar" /><link rel="alternate" hreflang="bn"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=bn" /><link rel="alternate" hreflang="zh-Hans"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=zh-cn" /><link rel="alternate" hreflang="zh-Hant"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=zh-tw" /><link rel="alternate" hreflang="fa"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=fa" /><link rel="alternate" hreflang="fr"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=fr" /><link rel="alternate" hreflang="de"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=de" /><link rel="alternate" hreflang="he"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=he" /><link rel="alternate" hreflang="hi"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=hi" /><link rel="alternate" hreflang="id"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=id" /><link rel="alternate" hreflang="it"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=it" /><link rel="alternate" hreflang="ja"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=ja" /><link rel="alternate" hreflang="ko"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=ko" /><link rel="alternate" hreflang="pl"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=pl" /><link rel="alternate" hreflang="pt-BR"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=pt-br" /><link rel="alternate" hreflang="ru"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=ru" /><link rel="alternate" hreflang="es-419"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=es-419" /><link rel="alternate" hreflang="th"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=th" /><link rel="alternate" hreflang="tr"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=tr" /><link rel="alternate" hreflang="vi"
          href="https://firebase.google.com/docs/studio/custom-templates?hl=vi" /><title>Create a custom template &nbsp;|&nbsp; Firebase Studio</title>

<meta property="og:title" content="Create a custom template &nbsp;|&nbsp; Firebase Studio"><meta name="description" content="A guide to creating custom templates in Firebase Studio, including how to define the template structure, add user-configurable parameters, and test and share the template.">
  <meta property="og:description" content="A guide to creating custom templates in Firebase Studio, including how to define the template structure, add user-configurable parameters, and test and share the template."><meta property="og:url" content="https://firebase.google.com/docs/studio/custom-templates"><meta property="og:locale" content="en">
  

  

  

  

  


    </head>
  <body class="color-scheme--light"
        template="page"
        theme="firebase-icy-theme"
        type="article"
        
        appearance
        
        layout="docs"
        
        
        free-trial
        
        
          
            concierge='closed'
          
        
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
   track-name="firebase" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/lockup.svg"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/lockup.svg" class="devsite-site-logo" alt="Firebase">
  </picture>
  
</a>



</div>
        <div class="devsite-top-logo-row-middle">
          <div class="devsite-header-upper-tabs">
            
              
              
  <devsite-tabs class="upper-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Upper tabs">
      
        
          <tab class="devsite-dropdown
    
    
    
    ">
  
    <a href="https://firebase.google.com/products-build"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/products-build"
    
       track-type="nav"
       track-metadata-position="nav - build"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Build"
         
           track-name="build"
         
       >
    Build
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Build"
         track-type="nav"
         track-metadata-eventdetail="https://firebase.google.com/products-build"
         track-metadata-position="nav - build"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Build"
          
            track-name="build"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    firebase-dropdown firebase-dropdown--primary firebase-build">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Build</li>
              
              
                <li class="devsite-nav-description">Get to market quickly and securely with products that can scale globally
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products-build"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products-build"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Go to Build
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    firebase-dropdown firebase-dropdown--secondary firebase-build">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Build Products</li>
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/app-check"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/app-check"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      App Check
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/app-hosting"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/app-hosting"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      App Hosting
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/auth"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/auth"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Authentication
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/functions"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/functions"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Cloud Functions
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/storage"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/storage"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Cloud Storage
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/sql-connect"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/sql-connect"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      SQL Connect
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/extensions"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/extensions"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Extensions
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/firestore"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/firestore"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Firestore
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/hosting"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/hosting"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Hosting
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/phone-number-verification"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/phone-number-verification"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Phone Number Verification
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/realtime-database"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/realtime-database"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Realtime Database
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/firebase-ai-logic"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/firebase-ai-logic"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Firebase AI Logic
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/generative-ai"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/generative-ai"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Generative AI
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    
    
    
    ">
  
    <a href="https://firebase.google.com/products-run"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/products-run"
    
       track-type="nav"
       track-metadata-position="nav - run"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Run"
         
           track-name="run"
         
       >
    Run
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Run"
         track-type="nav"
         track-metadata-eventdetail="https://firebase.google.com/products-run"
         track-metadata-position="nav - run"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Run"
          
            track-name="run"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    firebase-dropdown firebase-dropdown--primary firebase-run">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Run</li>
              
              
                <li class="devsite-nav-description">Run your app with confidence and deliver the best experience for your users
</li>
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products-run"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products-run"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Go to Run
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    firebase-dropdown firebase-dropdown--secondary">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Run Products</li>
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/ab-testing"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/ab-testing"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      A/B Testing
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/app-distribution"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/app-distribution"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      App Distribution
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/cloud-messaging"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/cloud-messaging"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Cloud Messaging
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/crashlytics"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/crashlytics"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Crashlytics
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/analytics"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/analytics"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Google Analytics
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/in-app-messaging"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/in-app-messaging"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      In-App Messaging
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/performance"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/performance"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Performance Monitoring
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/remote-config"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/remote-config"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Remote Config
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/products/test-lab"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/products/test-lab"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="run products"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Test Lab
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab  >
            
    <a href="https://firebase.google.com/solutions"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/solutions"
    
       track-type="nav"
       track-metadata-position="nav - solutions"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Solutions"
         
           track-name="solutions"
         
       >
    Solutions
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://firebase.google.com/pricing"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/pricing"
    
       track-type="nav"
       track-metadata-position="nav - pricing"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Pricing"
         
           track-name="pricing"
         
       >
    Pricing
  
    </a>
    
  
          </tab>
        
      
        
          <tab class="devsite-dropdown
    
    devsite-active
    
    ">
  
    <a href="https://firebase.google.com/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/docs"
    
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
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Docs"
         track-type="nav"
         track-metadata-eventdetail="https://firebase.google.com/docs"
         track-metadata-position="nav - docs"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Docs"
          
            track-name="docs"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs"
                     track-metadata-position="nav - docs"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Overview
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/guides"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/guides"
                     track-metadata-position="nav - docs"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Fundamentals
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/ai"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/ai"
                     track-metadata-position="nav - docs"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      AI
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/build"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/build"
                     track-metadata-position="nav - docs"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Build
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/run"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/run"
                     track-metadata-position="nav - docs"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Run
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/reference"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/reference"
                     track-metadata-position="nav - docs"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Reference
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/samples"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/samples"
                     track-metadata-position="nav - docs"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Samples
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    
    
    
    ">
  
    <a href="https://firebase.google.com/community"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/community"
    
       track-type="nav"
       track-metadata-position="nav - community"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Community"
         
           track-name="community"
         
       >
    Community
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Community"
         track-type="nav"
         track-metadata-eventdetail="https://firebase.google.com/community"
         track-metadata-position="nav - community"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Community"
          
            track-name="community"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/community/learn"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/community/learn"
                     track-metadata-position="nav - community"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Learn
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/community/stories"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/community/stories"
                     track-metadata-position="nav - community"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Stories
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab  >
            
    <a href="https://firebase.google.com/support"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/support"
    
       track-type="nav"
       track-metadata-position="nav - support"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Support"
         
           track-name="support"
         
       >
    Support
  
    </a>
    
  
          </tab>
        
      
    </nav>

  </devsite-tabs>

            
           </div>
          
<devsite-search
    enable-signin
    enable-search
    enable-suggestions
      enable-query-completion
    
    enable-search-summaries
    project-name="Firebase Studio"
    tenant-name="Firebase"
    
    
    
    
    
    >
  <form class="devsite-search-form" action="https://firebase.google.com/s/results" method="GET">
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
    href="//firebase.blog"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Blog"
    >
  Blog
</a>
          
            <a class="devsite-header-link devsite-top-button button gc-analytics-event "
    href="//console.firebase.google.com"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Go to console"
    >
  Go to console
</a>
          

        

        
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
                  
                  
                  
                    <ul class="devsite-breadcrumb-list"
  
    aria-label="Lower header breadcrumb">
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://firebase.google.com/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Lower Header"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail="Firebase Documentation"
      
    >
    
          Documentation
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://firebase.google.com/docs/studio"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Lower Header"
      
        data-value="2"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="2"
      
        track-metadata-eventdetail="Firebase Studio"
      
    >
    
          Firebase Studio
        
  </a>
  
      
    
  </li>
  
</ul>
                </div>
                
              
              
            </div>
            
          </div>
          
        
      
      
        <div class="devsite-doc-set-nav-row">
          
          
            
            
  <devsite-tabs class="lower-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Lower tabs">
      
        
          <tab  >
            
    <a href="https://firebase.google.com/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/docs"
    
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
        
      
        
          <tab class="devsite-dropdown
    
    
    
    ">
  
    <a href="https://firebase.google.com/docs/guides"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/docs/guides"
    
       track-type="nav"
       track-metadata-position="nav - fundamentals"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Fundamentals"
         
           track-name="fundamentals"
         
       >
    Fundamentals
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Fundamentals"
         track-type="nav"
         track-metadata-eventdetail="https://firebase.google.com/docs/guides"
         track-metadata-position="nav - fundamentals"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Fundamentals"
          
            track-name="fundamentals"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/ios/setup"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/ios/setup"
                     track-metadata-position="nav - fundamentals"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Add Firebase - Apple platforms (iOS+)
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/android/setup"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/android/setup"
                     track-metadata-position="nav - fundamentals"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Add Firebase - Android
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/web/setup"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/web/setup"
                     track-metadata-position="nav - fundamentals"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Add Firebase - Web
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/flutter/setup"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/flutter/setup"
                     track-metadata-position="nav - fundamentals"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Add Firebase - Flutter
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/cpp/setup"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/cpp/setup"
                     track-metadata-position="nav - fundamentals"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Add Firebase - C++
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/unity/setup"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/unity/setup"
                     track-metadata-position="nav - fundamentals"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Add Firebase - Unity
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/admin/setup"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/admin/setup"
                     track-metadata-position="nav - fundamentals"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Add Firebase - Server environments
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/projects/learn-more"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/projects/learn-more"
                     track-metadata-position="nav - fundamentals"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Manage Firebase projects
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/libraries"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/libraries"
                     track-metadata-position="nav - fundamentals"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Supported platforms & frameworks
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    
    devsite-active
    
    ">
  
    <a href="https://firebase.google.com/docs/ai"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/docs/ai"
    
       track-type="nav"
       track-metadata-position="nav - ai"
       track-metadata-module="primary nav"
       aria-label="AI, selected" 
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: AI"
         
           track-name="ai"
         
       >
    AI
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for AI"
         track-type="nav"
         track-metadata-eventdetail="https://firebase.google.com/docs/ai"
         track-metadata-position="nav - ai"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: AI"
          
            track-name="ai"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Develop with AI assistance</li>
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/ai-assistance"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/ai-assistance"
                     track-metadata-position="nav - ai"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="develop with ai assistance"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Overview
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/ai-assistance/gemini-in-firebase"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/ai-assistance/gemini-in-firebase"
                     track-metadata-position="nav - ai"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="develop with ai assistance"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Gemini in Firebase
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Streamline development with an AI-powered assistant in Firebase interfaces and tools.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/ai-assistance/agent-skills"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/ai-assistance/agent-skills"
                     track-metadata-position="nav - ai"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="develop with ai assistance"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      AI tools, skills, & MCP
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Access agentive development tools, like our agent skills and MCP server.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/studio/migrating-project"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/studio/migrating-project"
                     track-metadata-position="nav - ai"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="develop with ai assistance"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Firebase Studio (deprecated)
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Build and ship full-stack AI-infused apps right from your browser.

                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
                <li class="devsite-nav-title" role="heading" tooltip>Build AI-powered apps</li>
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/ai-logic"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/ai-logic"
                     track-metadata-position="nav - ai"
                     track-metadata-module="tertiary nav"
                     
                       track-metadata-module_headline="build ai-powered apps"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Firebase AI Logic
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Build genAI features and securely access Gemini models directly from your mobile &amp; web apps.

                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    devsite-dropdown-full
    
    
    ">
  
    <a href="https://firebase.google.com/docs/build"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/docs/build"
    
       track-type="nav"
       track-metadata-position="nav - build"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Build"
         
           track-name="build"
         
       >
    Build
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Build"
         track-type="nav"
         track-metadata-eventdetail="https://firebase.google.com/docs/build"
         track-metadata-position="nav - build"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Build"
          
            track-name="build"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/auth"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/auth"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Authentication
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Simplify user authentication and sign-in on a secure, all-in-one identity platform.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/phone-number-verification"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/phone-number-verification"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Phone Number Verification
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Obtain the phone number of a device directly from the carrier, without SMS.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/app-check"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/app-check"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      App Check
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Protect your backend resources from abuse and unauthorized access.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/rules"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/rules"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Security Rules
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Define granular, server-enforced rules to protect your database and storage data.

                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/sql-connect"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/sql-connect"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      SQL Connect
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Build and scale your apps using a fully-managed PostgreSQL relational database service.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/firestore"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/firestore"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Firestore
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Store and sync data using a scalable NoSQL cloud database with rich data models and queryability.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/database"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/database"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Realtime Database
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Store and sync data in realtime with a NoSQL cloud database.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/storage"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/storage"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Storage
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Store and serve content like images, audio, video with a secure cloud-hosted solution.

                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/app-hosting"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/app-hosting"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      App Hosting
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Deploy your modern, full-stack web apps with server-side rendering and AI features.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/hosting"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/hosting"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Hosting
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Deploy your static and single-page web apps to a global CDN with a single command.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/functions"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/functions"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Cloud Functions
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Run backend code in response to events without provisioning or managing a server.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/extensions"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/extensions"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Extensions (deprecated)
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Deploy pre-built integrations and solutions for common tasks.

                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/emulator-suite"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/emulator-suite"
                     track-metadata-position="nav - build"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Emulator Suite
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Test your app in real-world conditions without affecting live data.

                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    
    
    
    ">
  
    <a href="https://firebase.google.com/docs/run"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/docs/run"
    
       track-type="nav"
       track-metadata-position="nav - run"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Run"
         
           track-name="run"
         
       >
    Run
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Run"
         track-type="nav"
         track-metadata-eventdetail="https://firebase.google.com/docs/run"
         track-metadata-position="nav - run"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Run"
          
            track-name="run"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/test-lab"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/test-lab"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Test Lab
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Test your Android and iOS apps on a wide range of real and virtual devices, all in the cloud.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/app-distribution"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/app-distribution"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      App Distribution
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Streamline delivery of pre-release Android and iOS apps to trusted testers.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/crashlytics"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/crashlytics"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Crashlytics
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Track, prioritize, and fix app stability issues.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/perf-mon"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/perf-mon"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Performance Monitoring
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Gain real-time insight into your app&#39;s performance and fix issues.

                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/remote-config"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/remote-config"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Remote Config
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Instantly change your app&#39;s behavior and appearance, without publishing an update.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/ab-testing"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/ab-testing"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      A/B Testing
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Test variants to make data-driven decisions about changes, features, and campaigns.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/cloud-messaging"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/cloud-messaging"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Cloud Messaging
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Send notifications and messages to your users on Android, iOS, and the Web.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/in-app-messaging"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/in-app-messaging"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      In-App Messaging
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Engage your active users with targeted, contextual messages within your app.

                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/analytics"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/analytics"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Google Analytics
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Gain insights into user behavior, and optimize your app&#39;s marketing and performance.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/admob"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/admob"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Google AdMob
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Monetize your app, gain user insights, and tailor the ad experience.

                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://firebase.google.com/docs/ads"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://firebase.google.com/docs/ads"
                     track-metadata-position="nav - run"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Google Ads
                    </div>
                    
                    <div class="devsite-nav-item-description">
                      Run smarter campaigns, find high-value users, and measure in-app conversions.

                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab  >
            
    <a href="https://firebase.google.com/docs/reference"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/docs/reference"
    
       track-type="nav"
       track-metadata-position="nav - reference"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Reference"
         
           track-name="reference"
         
       >
    Reference
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://firebase.google.com/docs/samples"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://firebase.google.com/docs/samples"
    
       track-type="nav"
       track-metadata-position="nav - samples"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Samples"
         
           track-name="samples"
         
       >
    Samples
  
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
   track-name="firebase" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/lockup.svg"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/lockup.svg" class="devsite-site-logo" alt="Firebase">
  </picture>
  
</a>


</div>
  </div>

  <div class="devsite-book-nav-wrapper">
    <div class="devsite-mobile-nav-top">
      
        <ul class="devsite-nav-list">
          
            <li class="devsite-nav-item">
              
  
  <a href="/products-build"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Build"
      
        track-name="build"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Build"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Build
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Build"
      
        track-name="build"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Build">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Build">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/products-run"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Run"
      
        track-name="run"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Run"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Run
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Run"
      
        track-name="run"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Run">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Run">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/solutions"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Solutions"
      
        track-name="solutions"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Solutions"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Solutions
   </span>
    
  
  </a>
  

  
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/pricing"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Pricing"
      
        track-name="pricing"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Pricing"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Pricing
   </span>
    
  
  </a>
  

  
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/docs"
    
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
  
    <span class="devsite-nav-text" tooltip >
      Docs
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Docs"
      
        track-name="docs"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Docs">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Docs">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
                <ul class="devsite-nav-responsive-tabs">
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/docs"
    
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
                      
  
  <a href="/docs/guides"
    
       class="devsite-nav-title gc-analytics-event
              devsite-nav-has-children
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Fundamentals"
      
        track-name="fundamentals"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Fundamentals"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Fundamentals
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          >
    </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
                devsite-lower-tab-item">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Fundamentals"
      
        track-name="fundamentals"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Fundamentals">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Fundamentals">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/docs/ai"
    
       class="devsite-nav-title gc-analytics-event
              devsite-nav-has-children
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: AI"
      
        track-name="ai"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: AI"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip menu="_book">
      AI
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="_book">
    </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
                devsite-lower-tab-item">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: AI"
      
        track-name="ai"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="AI">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="AI">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/docs/build"
    
       class="devsite-nav-title gc-analytics-event
              devsite-nav-has-children
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Build"
      
        track-name="build"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Build"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Build
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          >
    </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
                devsite-lower-tab-item">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Build"
      
        track-name="build"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Build">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Build">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/docs/run"
    
       class="devsite-nav-title gc-analytics-event
              devsite-nav-has-children
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Run"
      
        track-name="run"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Run"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Run
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          >
    </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
                devsite-lower-tab-item">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Run"
      
        track-name="run"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Run">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Run">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/docs/reference"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Reference"
      
        track-name="reference"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Reference"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Reference
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/docs/samples"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Samples"
      
        track-name="samples"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Samples"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Samples
   </span>
    
  
  </a>
  

  
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/community"
    
       class="devsite-nav-title gc-analytics-event
              devsite-nav-has-children
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Community"
      
        track-name="community"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Community"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Community
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          >
    </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Community"
      
        track-name="community"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Community">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Community">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/support"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Support"
      
        track-name="support"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Support"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Support
   </span>
    
  
  </a>
  

  
              
            </li>
          
          
    
    
<li class="devsite-nav-item">

  
  <a href="//firebase.blog"
    
       class="devsite-nav-title gc-analytics-event "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Blog"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Blog
   </span>
    
  
  </a>
  

</li>

  
    
    
<li class="devsite-nav-item">

  
  <a href="//console.firebase.google.com"
    
       class="devsite-nav-title gc-analytics-event "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Go to console"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Go to console
   </span>
    
  
  </a>
  

</li>

  
          
        </ul>
      
    </div>
    
      <div class="devsite-mobile-nav-bottom">
        
          
          <ul class="devsite-nav-list" menu="_book">
            <li class="devsite-nav-item"><a href="/docs/ai"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-divider
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Develop with AI assistance</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/docs/ai-assistance"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Develop with AI assistance</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Gemini in Firebase</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-assistance/gemini-in-firebase"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Introduction</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/gemini-in-firebase/set-up-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up Gemini in Firebase</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/gemini-in-firebase/try-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Try Gemini in the Firebase console</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>AI tools and integrations</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-assistance/agent-skills"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Firebase agent skills</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/mcp-server"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Firebase MCP server</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/build-with-ai"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Integrate Firebase services using AI assistance</span></a></li><li class="devsite-nav-item
           devsite-nav-unsupported"><a href="/docs/ai-assistance/gcli-extension"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Gemini CLI extension</span><span class="devsite-nav-icon material-icons"
        data-icon="unsupported"
        data-title="No longer supported"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/ai-studio-integration"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Google AI Studio integration</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Prompts</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/prompt-catalog"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/prompt-catalog/set-up-backend"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Set up a backend</span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/docs/ai-assistance/prompt-catalog/write-security-rules"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Write security rules</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/prompt-catalog/add-ai-features"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Add AI features</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/prompt-catalog/deploy-to-hosting"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Deploy to hosting</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-assistance/prompt-catalog/prioritize-fix-issues"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Prioritize &amp; fix issues</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion
           devsite-nav-deprecated"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Firebase Studio</span><span class="devsite-nav-icon material-icons"
        data-icon="deprecated"
        data-title="Deprecated"
        aria-hidden="true"></span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/studio/migrating-project"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Firebase Studio sunset and project migration</span></a></li><li class="devsite-nav-item"><a href="/docs/studio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Introduction</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/get-started"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/get-started-import"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started with an existing project</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/get-started-ai"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started with the App Prototyping agent</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/get-started-template"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started with a template</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/pricing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Firebase Studio pricing, quotas, and limits</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>AI assistance in Firebase Studio</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/studio/ai-assistance"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Introduction</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/try-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get assistance from Gemini</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/set-up-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configure Gemini assistance</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/prompting"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Effective prompting</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/mcp-servers"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Connect to MCP servers</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Preview, publish, and monitor</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/studio/preview-apps"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Preview web and Android apps</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/deploy-app"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Publish apps</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/monitor"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Monitor and protect web apps</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/github"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Upload your app to GitHub</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Optimize your Firebase Studio workspace</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/studio/get-started-workspace"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>About Firebase Studio workspaces</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/customize-workspace"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Customize your Firebase Studio workspace</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/firebase-projects"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Connect to a Firebase project</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/google-integrations"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Integrate with Google and Firebase services</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/custom-templates"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create custom templates</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/open-in-firebase-studio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create a shortcut to a predefined workspace</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/share-your-workspace"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Share your workspace</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/import-workspace"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Create a button to import code into Firebase Studio</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Solutions</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/studio/solution-build-with-ai"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Develop, publish, and monitor a full-stack web app</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/build-gemini-api-app"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Build an app with the Gemini API</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Troubleshoot and debug</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/studio/debug"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Debug your app</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/troubleshooting"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>FAQ and troubleshooting</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Reference</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/studio/devnix-reference"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>dev.nix Reference</span></a></li><li class="devsite-nav-item
           devsite-nav-break"></li><li class="devsite-nav-item"><a href="/docs/studio/idx-is-firebase-studio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Project IDX is now part of Firebase Studio</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/oss"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Licensed software</span></a></li><li class="devsite-nav-item"><a href="/docs/studio/connect"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Connect with us</span></a></li></ul></div></li>

  <li class="devsite-nav-item
           devsite-nav-divider
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Build AI-powered apps</span>
      </div></li>

  <li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-accordion"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Firebase AI Logic</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Introduction</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/get-started"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/models"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Models</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/ref-docs"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>SDK reference docs</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Security</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/security-checklist"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Security checklist</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/app-check"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Prevent abuse with App Check</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Core capabilities</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/generate-text"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Text</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/chat"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Chat</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Images</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/analyze-images"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Analyze images</span></a></li><li class="devsite-nav-item
           devsite-nav-preview"><a href="/docs/ai-logic/generate-images-gemini"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Generate &amp; edit images (Nano Banana)</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/imagen-models-migration"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Migrate from Imagen to Gemini</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Video</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/analyze-video"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Analyze video</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Audio</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/analyze-audio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Analyze audio</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/generate-audio"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Generate audio</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/generate-speech"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Generate speech (TTS)</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Documents (PDFs)</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/analyze-documents"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Analyze documents (PDFs)</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/generate-structured-output"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Structured output (JSON)</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/stream-responses"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Streaming responses</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Specialized capabilities</span>
      </div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Hybrid &amp; on-device inference</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/hybrid"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-experimental"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>iOS+</span><span class="devsite-nav-icon material-icons"
        data-icon="experimental"
        data-title="Experimental!"
        aria-hidden="true"></span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/hybrid/ios/get-started"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/hybrid/ios/configuration-options"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configuration options</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-experimental"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Android</span><span class="devsite-nav-icon material-icons"
        data-icon="experimental"
        data-title="Experimental!"
        aria-hidden="true"></span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/hybrid/android/get-started"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/hybrid/android/configuration-options"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configuration options</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Web</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/hybrid/web/get-started"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/hybrid/web/configuration-options"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configuration options</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/hybrid/web/generate-structured-output"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Structured output</span></a></li></ul></div></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-preview"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Real-time bidirectional streaming (Live API)</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/live-api"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/live-api/capabilities"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Capabilities</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/live-api/configuration"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Configuration options</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/live-api/sessions"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Manage sessions</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/live-api/limits-and-specs"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Limits &amp; specifications</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Provide tools to the model</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/function-calling"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Function calling</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/code-execution"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Code execution</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/url-context"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>URL context</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/grounding-google-search"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Grounding - Google Search</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/grounding-google-maps"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Grounding - Google Maps</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Control generation of responses</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/control-content-gen"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview of options</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/prompt-design"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Prompt design</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/model-parameters"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Model configuration</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/thinking"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Thinking</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/safety-settings"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Safety settings</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/system-instructions"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>System instructions</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Get ready for production</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/production-checklist"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Production checklist</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/auth-mode"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Restrict requests to authenticated users</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/change-model-name-remotely"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Change model name remotely</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/locations"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Locations</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/context-caching"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Context caching</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/pricing"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Pricing</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/quotas"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Rate limits &amp; quota</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/count-tokens"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Count tokens</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/monitoring"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Monitor costs, usage, &amp; metrics</span></a></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Solutions</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/solutions/overview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/solutions/cloud-storage"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Include large files in requests with Cloud Storage</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-preview"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Store &amp; access prompt templates on the server</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/server-prompt-templates/get-started"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/server-prompt-templates/multi-turn-interactions"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Multi-turn interactions</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/server-prompt-templates/syntax-and-examples"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Format, syntax, &amp; examples</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/server-prompt-templates/best-practices-and-considerations"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Best practices &amp; considerations</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/server-prompt-templates/manage-templates"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Manage templates</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/server-prompt-templates/versioning-with-remote-config"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Version with Remote Config</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/server-prompt-templates/template-only-mode"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Template-only mode</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/server-prompt-templates/advanced-workflows"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Advanced workflows</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/solutions/remote-config"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Dynamically update your app with Remote Config</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable
           devsite-nav-preview"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Access Gemini API via Apple&#39;s Foundation Models framework</span><span class="devsite-nav-icon material-icons"
        data-icon="preview"
        data-title="Preview"
        aria-hidden="true"></span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/apple-foundation-models-framework/get-started"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Get started</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/apple-foundation-models-framework/capabilities"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Capabilities</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/apple-foundation-models-framework/configuration"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Config options</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/apple-foundation-models-framework/tools"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Provide tools</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Additional information</span>
      </div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/input-file-requirements"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Input file types &amp; requirements</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Migration guides</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/docs/ai-logic/migrate-to-latest-sdk"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Migrate from GA &#34;Vertex AI in Firebase&#34;</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/migrate-from-preview"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Migrate from preview &#34;Vertex AI in Firebase&#34;</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/migrate-from-google-ai-client-sdks"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Migrate from &#34;Google AI client SDKs&#34;</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/docs/ai-logic/data-governance"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Data governance &amp; Responsible AI</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/cloud-audit-logging"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Cloud Audit Logging</span></a></li><li class="devsite-nav-item
           devsite-nav-break"></li><li class="devsite-nav-item"><a href="/docs/ai-logic/faq-and-troubleshooting"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>FAQ and troubleshooting</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/error-codes"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Error codes</span></a></li><li class="devsite-nav-item"><a href="/docs/ai-logic/feedback"
        class="devsite-nav-title"
      ><span class="devsite-nav-text" tooltip>Give feedback</span></a></li></ul></div></li>
          </ul>
        
        
          
    
      
      <ul class="devsite-nav-list" menu="Build"
          aria-label="Side menu" hidden>
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Build
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/products-build"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Go to Build"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Go to Build
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Build Products
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/products/app-check"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: App Check"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      App Check
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/app-hosting"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: App Hosting"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      App Hosting
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/auth"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Authentication"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Authentication
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/functions"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Cloud Functions"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Cloud Functions
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/storage"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Cloud Storage"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Cloud Storage
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/sql-connect"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: SQL Connect"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      SQL Connect
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/extensions"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Extensions"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Extensions
   </span>
    
  
  </a>
  

</li>

            
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/products/firestore"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Firestore"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Firestore
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/hosting"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Hosting"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Hosting
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/phone-number-verification"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Phone Number Verification"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Phone Number Verification
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/realtime-database"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Realtime Database"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Realtime Database
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/firebase-ai-logic"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Firebase AI Logic"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Firebase AI Logic
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/generative-ai"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Generative AI"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Generative AI
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Run"
          aria-label="Side menu" hidden>
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Run
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/products-run"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Go to Run"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Go to Run
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Run Products
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/products/ab-testing"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: A/B Testing"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      A/B Testing
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/app-distribution"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: App Distribution"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      App Distribution
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/cloud-messaging"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Cloud Messaging"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Cloud Messaging
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/crashlytics"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Crashlytics"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Crashlytics
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/analytics"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Google Analytics"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Google Analytics
   </span>
    
  
  </a>
  

</li>

            
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/products/in-app-messaging"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: In-App Messaging"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      In-App Messaging
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/performance"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Performance Monitoring"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Performance Monitoring
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/remote-config"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Remote Config"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Remote Config
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/products/test-lab"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Test Lab"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Test Lab
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
  
    
  
    
      
      <ul class="devsite-nav-list" menu="Docs"
          aria-label="Side menu" hidden>
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Overview"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Overview
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/guides"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Fundamentals"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Fundamentals
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ai"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: AI"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      AI
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/build"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Build"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Build
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/run"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Run"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Run
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/reference"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Reference"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Reference
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/samples"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Samples"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Samples
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Community"
          aria-label="Side menu" hidden>
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/community/learn"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Learn"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Learn
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/community/stories"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Stories"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Stories
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
  
        
        
          
    
  
    
      
      <ul class="devsite-nav-list" menu="Fundamentals"
          aria-label="Side menu" hidden>
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ios/setup"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Add Firebase - Apple platforms (iOS+)"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Add Firebase - Apple platforms (iOS+)
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/android/setup"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Add Firebase - Android"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Add Firebase - Android
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/web/setup"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Add Firebase - Web"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Add Firebase - Web
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/flutter/setup"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Add Firebase - Flutter"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Add Firebase - Flutter
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/cpp/setup"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Add Firebase - C++"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Add Firebase - C++
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/unity/setup"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Add Firebase - Unity"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Add Firebase - Unity
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/admin/setup"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Add Firebase - Server environments"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Add Firebase - Server environments
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/projects/learn-more"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Manage Firebase projects"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Manage Firebase projects
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/libraries"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Supported platforms &amp; frameworks"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Supported platforms &amp; frameworks
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="AI"
          aria-label="Side menu" hidden>
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Develop with AI assistance
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ai-assistance"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Overview"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Overview
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ai-assistance/gemini-in-firebase"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Gemini in Firebase"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Gemini in Firebase
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ai-assistance/agent-skills"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: AI tools, skills, &amp; MCP"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      AI tools, skills, &amp; MCP
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/studio/migrating-project"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Firebase Studio (deprecated)"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Firebase Studio (deprecated)
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
              
<li class="devsite-nav-item devsite-nav-heading">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    >
  
    <span class="devsite-nav-text" tooltip >
      Build AI-powered apps
   </span>
    
  
  </span>
  

</li>

            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ai-logic"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Firebase AI Logic"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Firebase AI Logic
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Build"
          aria-label="Side menu" hidden>
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/auth"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Authentication"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Authentication
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/phone-number-verification"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Phone Number Verification"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Phone Number Verification
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/app-check"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: App Check"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      App Check
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/rules"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Security Rules"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Security Rules
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/sql-connect"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: SQL Connect"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      SQL Connect
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/firestore"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Firestore"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Firestore
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/database"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Realtime Database"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Realtime Database
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

            
          
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/app-hosting"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: App Hosting"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      App Hosting
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/hosting"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Hosting"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Hosting
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/functions"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Cloud Functions"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Cloud Functions
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/extensions"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Extensions (deprecated)"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Extensions (deprecated)
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/emulator-suite"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Emulator Suite"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Emulator Suite
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Run"
          aria-label="Side menu" hidden>
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/test-lab"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Test Lab"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Test Lab
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/app-distribution"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: App Distribution"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      App Distribution
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/crashlytics"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Crashlytics"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Crashlytics
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/perf-mon"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Performance Monitoring"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Performance Monitoring
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/remote-config"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Remote Config"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Remote Config
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ab-testing"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: A/B Testing"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      A/B Testing
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/cloud-messaging"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Cloud Messaging"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Cloud Messaging
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/in-app-messaging"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: In-App Messaging"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      In-App Messaging
   </span>
    
  
  </a>
  

</li>

            
          
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/analytics"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Google Analytics"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Google Analytics
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/admob"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Google AdMob"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Google AdMob
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ads"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Google Ads"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Google Ads
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
  
  
  
    <div class="devsite-banner devsite-banner-announcement nocontent" data-nosnippet
      
        
    background="orange"
  
      >
      <div class="devsite-banner-message">
        <div class="devsite-banner-message-text">
          <p><strong>Firebase Studio is sunsetting on March 22, 2027.</strong> As of June 22, 2026, new workspace creation and user signup are disabled. You can continue to work in and migrate your existing workspaces to Google AI Studio or Google Antigravity. <a href="/docs/studio/migrating-project">Learn how to migrate.</a></p> <p><em>Any apps already deployed to Firebase will continue to run even after the sunset date. Also, all our <u>core Firebase products</u> (like Firestore, Authentication, App Hosting, etc.) are <u>not impacted</u> by the Firebase Studio sunset.</em></p>
        </div>
      </div>
    </div>
  
  
  

  <div class="devsite-article-meta nocontent" role="navigation" data-nosnippet>
    
    
    <ul class="devsite-breadcrumb-list"
  
    aria-label="Breadcrumb">
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://firebase.google.com/"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail="Firebase"
      
    >
    
          Firebase
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://firebase.google.com/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="2"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="2"
      
        track-metadata-eventdetail="Firebase Documentation"
      
    >
    
          Documentation
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://firebase.google.com/docs/studio"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="3"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="3"
      
        track-metadata-eventdetail="Firebase Studio"
      
    >
    
          Firebase Studio
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://firebase.google.com/docs/ai"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="4"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="4"
      
        track-metadata-eventdetail=""
      
    >
    
          AI
        
  </a>
  
      
    
  </li>
  
</ul>
    
      
    <devsite-thumb-rating position="header">
    </devsite-thumb-rating>
  
    
  </div>
  
    <devsite-feedback
  position="header"
  project-name="Firebase Studio"
  product-id="719752"
  bucket=""
  context=""
  version="t-devsite-webserver-20260825-r00-rc00.479916215390653058"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="header"
  class="nocontent"
  data-nosnippet
  
  
    project-feedback-url="https://firebase.google.com/support/contact/bugs-features/"
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/touchicon-180.png"
  
  
    project-support-url="https://firebase.google.com/support/troubleshooter/report"
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
  
    <h1 class="devsite-page-title" tabindex="-1">
      Create a custom template<devsite-actions hidden data-nosnippet><devsite-feature-tooltip
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
  <div class="devsite-page-title-meta"><devsite-view-release-notes></devsite-view-release-notes></div>
  

  <devsite-toc class="devsite-nav"
    depth="2"
    devsite-toc-embedded
    >
  </devsite-toc>
  <div class="devsite-article-body clearfix
  ">

  
    
    

























































































































































































































































































































































































































































































































































































































































































































































































































































































    























































<p><span class="notranslate">Firebase Studio</span> offers a wide range of built-in
<a href="https://studio.firebase.google.com//templates">templates</a> that include all
the files, <a href="/docs/studio/customize-workspace#system-tools">system
packages</a> (for example,
compilers), and
<a href="/docs/studio/customize-workspace#extensions">extensions</a> you need to
quickly get started with a language or framework.</p>

<p>You can also launch a <span class="notranslate">Firebase Studio</span> workspace using
<a href="https://github.com/firebase-studio/community-templates/">Community</a> templates
hosted on GitHub. For more information about launching a new
workspace from a template, see <a href="/docs/studio/get-started-workspace#create-workspace">Create a
<span class="notranslate">Firebase Studio</span> workspace</a>.</p>

<p>Most users will use the built-in templates or import projects from Git, but
for more advanced use cases, you can create your own templates:</p>

<ul>
<li><p>If you&#39;re <strong>building your own framework, library, or service</strong>, you can
let your users quickly get started with your technology without ever
leaving the browser, with the full power of a cloud-based virtual machine.</p></li>
<li><p>If you have a <strong>preferred technology stack for your projects</strong>, you can
simplify your own process for starting new projects with a custom template.</p></li>
<li><p>If you&#39;re <strong>teaching others, such as through a tutorial or codelab</strong>,
you can remove some of the initial steps for your students by
pre-configuring the starting point for your codelab as a custom
template.</p></li>
</ul>

<p>After you create and test your custom template, you can <a href="/docs/studio/open-in-firebase-studio">create a link for
it</a> to place on your website, Git
repository <code translate="no" dir="ltr">README</code> file, package detail page (for example, in NPM), or
any other place you expect your users to start using your technology.</p>
<aside class="tip"><strong>Tip:</strong><span> You can also create a link for users to create a new workspace by cloning
a Git repository. While this is less configurable than creating your own
<span class="notranslate">Firebase Studio</span> template, it requires no changes to the Git repository.
Learn more at
<a href="/docs/studio/get-started-workspace#create-workspace">Create a workspace</a>.</span></aside>
<h2 id="prerequisites" data-text="Prerequisites" tabindex="-1">Prerequisites</h2>

<p>Before you get started:</p>

<ul>
<li><p>Learn how to use the <code translate="no" dir="ltr">idx/dev.nix</code> file to
<a href="/docs/studio/customize-workspace">customize your environment</a>.</p></li>
<li><p>Get familiar with <a href="https://nix.dev/tutorials/nix-language">Nix language</a>
basics and keep the reference handy.</p></li>
</ul>

<h2 id="file-structure" data-text="Template file structure" tabindex="-1">Template file structure</h2>

<p>A <span class="notranslate">Firebase Studio</span> template is a public Git repository (or folder or
branch in a repository) that contains at least two files:</p>

<ul>
<li><p><strong><code translate="no" dir="ltr">idx-template.json</code></strong> includes the metadata for the template,
including its user-visible name, description, and parameters available
to users to configure the template. For example, you can allow your
users to choose from a number of programming languages, or example use
cases. <strong><span class="notranslate">Firebase Studio</span> uses this information to prepare the UI
shown to users when they choose to create a new workspace from your
template.</strong></p></li>
<li><p><strong><code translate="no" dir="ltr">idx-template.nix</code></strong> is a file written with the <a href="https://nix.dev/tutorials/nix-language">Nix
language</a> that contains a Bash shell
script (wrapped in a Nix function) that:</p>

<ol>
<li><p>Creates the working directory for the new workspace.</p></li>
<li><p>Sets up its environment by creating a <code translate="no" dir="ltr">.idx/dev.nix</code> file. Note
that you can also just run a project scaffolding tool like <code translate="no" dir="ltr">flutter
create</code> or <code translate="no" dir="ltr">npm init</code> in this script, or run a custom script
written in Go, Python, Node.js, or another language.</p>

<p>This file will be <strong>executed with the parameters specified by the user</strong>
when <span class="notranslate">Firebase Studio</span> loads the template.</p></li>
</ol></li>
</ul>

<p>Other files may be included alongside these two files, for use in
<code translate="no" dir="ltr">idx-template.nix</code>, in order to instantiate the template. For example, you could
include the final <code translate="no" dir="ltr">.idx/dev.nix</code> file, or even include all of the scaffolding
files right in the repository.</p>

<h2 id="create-starter-template" data-text="Create a starter template" tabindex="-1">Create a starter template</h2>

<p>To expedite template creation, we recommend that you start with one of the
following methods to create a <span class="notranslate">Firebase Studio</span> template that you can further
customize:</p>

<ul>
<li><a href="#basic-example">Turn any public GitHub repository into a template</a></li>
<li><a href="#custom-from-template">Use an official or community template as a basis for your
template</a></li>
</ul>

<h3 id="basic-example" data-text="A basic example: Turn any public GitHub repository into a template" tabindex="-1">A basic example: Turn any public GitHub repository into a template</h3>

<p>Before getting into the details of how to define your <code translate="no" dir="ltr">idx-template.json</code> and
<code translate="no" dir="ltr">idx-template.nix</code>, it&#39;s useful to see a basic example template that:</p>

<ul>
<li>Contains no user-configurable parameters.</li>
<li>Copies all the files in your template repository (except for the two
<code translate="no" dir="ltr">idx-template</code> files) into the user&#39;s workspace. There should already be a
<code translate="no" dir="ltr">.idx</code> subfolder with a <code translate="no" dir="ltr">dev.nix</code> file that defines the environment.</li>
</ul>

<p>If you add the following files to any public GitHub repository (or subfolder or
branch), this effectively turns that repository into a <span class="notranslate">Firebase Studio</span>
template.</p>

<h4 id="idx-template-json" data-text="idx-template.json" tabindex="-1"><code translate="no" dir="ltr">idx-template.json</code></h4>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hello world"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"description"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"A template for a CLI program that prints 'hello world'"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"icon"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"https://www.gstatic.com/images/branding/productlogos/studio/v1/192px.svg"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"params"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[]</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h4 id="idx-template-nix" data-text="idx-template.nix" tabindex="-1"><code translate="no" dir="ltr">idx-template.nix</code></h4>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Nix"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># No user-configurable parameters</span>
<span class="devsite-syntax-p">{</span> pkgs<span class="devsite-syntax-p">,</span> <span class="devsite-syntax-o">...</span> <span class="devsite-syntax-p">}:</span> <span class="devsite-syntax-p">{</span>
  <span class="devsite-syntax-c1"># Shell script that produces the final environment</span>
  <span class="devsite-syntax-ss">bootstrap</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s devsite-syntax-s-Multiline">''</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    # Copy the folder containing the `idx-template` files to the final</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    # project folder for the new workspace. </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-l">./.</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s devsite-syntax-s-Multiline"> inserts the directory</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    # of the checked-out Git folder containing this template.</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    cp -rf </span><span class="devsite-syntax-si">${</span><span class="devsite-syntax-l">./.</span><span class="devsite-syntax-si">}</span><span class="devsite-syntax-s devsite-syntax-s-Multiline"> "$out"</span>

<span class="devsite-syntax-s devsite-syntax-s-Multiline">    # Set some permissions</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    chmod -R +w "$out"</span>

<span class="devsite-syntax-s devsite-syntax-s-Multiline">    # Remove the template files themselves and any connection to the template's</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    # Git repository</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    rm -rf "$out/.git" "$out/idx-template".{nix,json}</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">  ''</span><span class="devsite-syntax-p">;</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code><aside class="note"><strong>Note:</strong><span> In addition to <code translate="no" dir="ltr">$out</code>, you can also obtain the new workspace ID using the
<code translate="no" dir="ltr">$WS_NAME</code> variable.</span></aside>
<p>Proceed to <a href="#customize-template">Customize your template</a> to learn about
additional changes you can make to customize your template.</p>

<h3 id="custom-from-template" data-text="Create a custom template using an official or community template" tabindex="-1">Create a custom template using an official or community template</h3>

<p>The <span class="notranslate">Firebase Studio</span> team maintains two repositories for
<span class="notranslate">Firebase Studio</span> templates:</p>

<ul>
<li><p><a href="https://github.com/firebase-studio/templates">Official templates</a>: These
are the templates you select directly from the <span class="notranslate">Firebase Studio</span>
dashboard when you create a new app.</p></li>
<li><p><a href="https://github.com/firebase-studio/community-templates">Community templates</a>:
These templates allow contributions from the open source community. To use
a community template, clone the Community templates Git repository. You can
use the full link to the template you want to use.</p>
<aside class="tip"><strong>Tip:</strong><span> To contribute back to the community by adding new templates or updating
existing templates, submit a pull request.</span></aside></li>
</ul>

<p>To create a custom template with an existing template as a basis:</p>

<ol>
<li><p>Decide which template to use as a basis for your custom template, then
clone the project.</p></li>
<li><p>Customize <code translate="no" dir="ltr">idx-template.json</code>, <code translate="no" dir="ltr">idx-template.nix</code>, and <code translate="no" dir="ltr">.idx/dev.nix</code>
as needed, starting with <a href="#bootstrap-dependencies">Customize your template</a>.</p></li>
<li><p>Check the changes into your repository.</p></li>
<li><p>Follow <a href="#create-workspace">Create a new workspace for your template</a> to
publish and test your template. If you use a nested repository, link directly
to it in your URL. For example, if you were using the community
&quot;Vanilla Vite&quot; template, you&#39;d provision and test a new workspace using the
following URL:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Bash"><code translate="no" dir="ltr">https://studio.firebase.google.com/new?template<span class="devsite-syntax-o">=</span>https://github.com/firebase-studio/community-templates/tree/main/vite-vanilla
</code></pre></devsite-code></li>
</ol>

<p>Proceed to <a href="#customize-template">Customize your template</a> to learn about
additional changes you can make to customize your template.</p>

<h2 id="customize-template" data-text="Customize your template" tabindex="-1">Customize your template</h2>

<p>Now that you&#39;ve created a basic template to build upon, you can edit the
<code translate="no" dir="ltr">idx-template.json</code>, <code translate="no" dir="ltr">idx-template.nix</code>, and <code translate="no" dir="ltr">.idx/dev.nix</code> files to match your
requirements. You might want to customize additional configurations:</p>

<ul>
<li><a href="#bootstrap-dependencies">Add system packages to your <code translate="no" dir="ltr">bootstrap</code> script</a>.</li>
<li><a href="#parameters">Add user-configurable parameters</a></li>
<li><a href="#open-files">Choose which files should open by default</a></li>
<li><a href="#custom-icon">Choose a default workspace icon</a></li>
</ul>

<h3 id="bootstrap-dependencies" data-text="Use additional system packages in your bootstrap script" tabindex="-1">Use additional system packages in your <code translate="no" dir="ltr">bootstrap</code> script</h3>

<p>The <a href="#basic-example">basic example</a> only uses basic POSIX commands to copy
files into the right place. Your template&#39;s <code translate="no" dir="ltr">bootstrap</code> script may require
additional binaries to be installed, such as <code translate="no" dir="ltr">git</code>, <code translate="no" dir="ltr">node</code>, <code translate="no" dir="ltr">python3</code>, or
others.</p>

<p>You can make additional system packages available to your bootstrap script
by specifying <code translate="no" dir="ltr">packages</code> in your <code translate="no" dir="ltr">idx-template.nix</code> file, just as you would
<a href="/docs/studio/customize-workspace#packages">customize a workspace with additional system
packages</a> by adding to the
<code translate="no" dir="ltr">packages</code> in its <code translate="no" dir="ltr">dev.nix</code> file.</p>
<aside class="note"><strong>Note:</strong><span> <code translate="no" dir="ltr">idx-template.nix</code> always uses the <code translate="no" dir="ltr">stable-23.11</code> <a href="https://search.nixos.org/packages">Nix
channel</a>.</span></aside>
<p>Here&#39;s an example of adding <code translate="no" dir="ltr">pkgs.nodejs</code>, which includes binaries like <code translate="no" dir="ltr">node</code>,
<code translate="no" dir="ltr">npx</code> and <code translate="no" dir="ltr">npm</code>:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Nix"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># idx-template.nix</span>
<span class="devsite-syntax-p">{</span>pkgs<span class="devsite-syntax-p">}:</span> <span class="devsite-syntax-p">{</span>
  <span class="devsite-syntax-ss">packages</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[</span>
    <span class="devsite-syntax-c1"># Enable "node", "npm" and "npx" in the bootstrap script below.</span>
    <span class="devsite-syntax-c1"># Note, this is NOT the list of packages available to the workspace once</span>
    <span class="devsite-syntax-c1"># it's created. Those go in .idx/dev.nix</span>
    pkgs<span class="devsite-syntax-o">.</span>nodejs
  <span class="devsite-syntax-p">];</span>

  <span class="devsite-syntax-ss">bootstrap</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s devsite-syntax-s-Multiline">''</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    mkdir "$out"</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    # We can now use "npm"</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    npm init --yes my-boot-strap@latest "$out"</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">  ''</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code><aside class="special"><strong>Important:</strong><span> Your bootstrap script <strong>cannot be interactive</strong>. If it waits for user
input, the template will fail to instantiate correctly.</span></aside>
<h3 id="parameters" data-text="Add user-configurable parameters" tabindex="-1">Add user-configurable parameters</h3>

<p>To allow users to customize the starting point for their new project, you can
either create multiple templates, or create a single template with parameters.
This is a great option if your different starting points are just different
values passed to a CLI tool (for example <code translate="no" dir="ltr">--language=js</code> versus
<code translate="no" dir="ltr">--language=ts</code>).</p>

<p>To add parameters, you&#39;ll:</p>

<ol>
<li>Describe your parameter in the <code translate="no" dir="ltr">params</code> object of your
<code translate="no" dir="ltr">idx-template.json</code> metadata file. <span class="notranslate">Firebase Studio</span> uses information
in this file to prepare the UI (such as checkboxes, drop-downs, and
text fields) shown to users of your template.</li>
<li>Update your <code translate="no" dir="ltr">idx-template.nix</code> bootstrap to use the values the user selected
while instantiating the template.</li>
</ol>

<h4 id="describe-your-parameter-json" data-text="Describe your parameter in idx-template.json" tabindex="-1">Describe your parameter in <code translate="no" dir="ltr">idx-template.json</code></h4>

<p>Here&#39;s an example of adding an <code translate="no" dir="ltr">enum</code> parameter, which <span class="notranslate">Firebase Studio</span>
shows as either a drop-down menu or radio button group, depending on the
number of options:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="JSON"><code translate="no" dir="ltr"><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Hello world"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"description"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"A hello world app"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-nt">"params"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">[</span><strong>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"id"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"language"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"name"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"Programming Language"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"type"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"enum"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"default"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"ts"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"options"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-p">{</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"js"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"JavaScript"</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-w">        </span><span class="devsite-syntax-nt">"ts"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-s2">"TypeScript"</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-p">},</span>
<span class="devsite-syntax-w">      </span><span class="devsite-syntax-nt">"required"</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kc">true</span>
<span class="devsite-syntax-w">    </span><span class="devsite-syntax-p">}</span></strong>
<span class="devsite-syntax-w">  </span><span class="devsite-syntax-p">]</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p>Since there are two values (JavaScript and TypeScript), the UI will render a
radio button group for the two options and pass either the value <code translate="no" dir="ltr">ts</code> or <code translate="no" dir="ltr">js</code> to
the <code translate="no" dir="ltr">idx-template.nix</code> script.</p>

<p>Each parameter object has the following properties:</p>

<table>
<thead>
<tr>
<th>PROPERTY</th>
<th>TYPE</th>
<th>DESCRIPTION</th>
</tr>
</thead>

<tbody>
<tr>
<td>id</td>
<td><code translate="no" dir="ltr">string</code></td>
<td>The parameter&#39;s unique ID, similar to a variable name.</td>
</tr>
<tr>
<td>name</td>
<td><code translate="no" dir="ltr">string</code></td>
<td>The display name for this parameter.</td>
</tr>
<tr>
<td>type</td>
<td><code translate="no" dir="ltr">string</code></td>
<td><p>Specifies the UI component to use for this parameter, and the data type to pass to the bootstrap script. Valid values are:</p><ul><li><code translate="no" dir="ltr">&quot;enum&quot;</code> - Shows a drop-down or radio button group, and passes a <code translate="no" dir="ltr">string</code> to the bootstrap</li><li><code translate="no" dir="ltr">&quot;boolean&quot;</code> - Shows a checkbox and passes <code translate="no" dir="ltr">true</code> or <code translate="no" dir="ltr">false</code></li><li><code translate="no" dir="ltr">&quot;text&quot;</code> - Shows a text field and passes a <code translate="no" dir="ltr">string</code></li></ul></td>
</tr>
<tr>
<td>options</td>
<td><code translate="no" dir="ltr">object</code></td>
<td>For <code translate="no" dir="ltr">enum</code> parameters, this represents the options to show users. For example if options is <code translate="no" dir="ltr">{&quot;js&quot;: &quot;JavaScript&quot;, ...}</code>, &quot;JavaScript&quot; will be shown as the option, and when selected the value of this parameter will be <code translate="no" dir="ltr">js</code>.</td>
</tr>
<tr>
<td>default</td>
<td><code translate="no" dir="ltr">string</code> or <code translate="no" dir="ltr">boolean</code></td>
<td>Sets the initial value in the UI. For <code translate="no" dir="ltr">enum</code> parameters, this must be one of the keys in <code translate="no" dir="ltr">options</code>. For <code translate="no" dir="ltr">boolean</code> parameters, this should be either <code translate="no" dir="ltr">true</code> or <code translate="no" dir="ltr">false</code>.</td>
</tr>
<tr>
<td>required</td>
<td><code translate="no" dir="ltr">boolean</code></td>
<td>Indicates that this parameter is required.</td>
</tr>
</tbody>
</table>

<h4 id="use-parameter-values-idx-template-nix" data-text="Use parameter values in idx-template.nix" tabindex="-1">Use parameter values in <code translate="no" dir="ltr">idx-template.nix</code></h4>

<p>After defining the <code translate="no" dir="ltr">params</code> object in your <code translate="no" dir="ltr">idx-template.json</code> file, you can
start customizing the bootstrap script based on the parameter values the user
chooses.</p>

<p>Following the example in the previous section, if you have a single parameter
with ID <code translate="no" dir="ltr">language</code> that&#39;s an enum with possible values <code translate="no" dir="ltr">ts</code> or <code translate="no" dir="ltr">js</code>, you can use
it like so:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="Nix"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># idx-template.nix</span>
<span class="devsite-syntax-c1"># Accept additional arguments to this template corresponding to template</span>
<span class="devsite-syntax-c1"># parameter IDs, including default values (language=ts by default in this example).</span>
<span class="devsite-syntax-p">{</span> pkgs<span class="devsite-syntax-p">,</span> <strong>language <span class="devsite-syntax-o">?</span> <span class="devsite-syntax-s2">"ts"</span></strong><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-o">...</span> <span class="devsite-syntax-p">}:</span> <span class="devsite-syntax-p">{</span>
  <span class="devsite-syntax-ss">packages</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[</span>
    pkgs<span class="devsite-syntax-o">.</span>nodejs
  <span class="devsite-syntax-p">];</span>

  <span class="devsite-syntax-ss">bootstrap</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-s devsite-syntax-s-Multiline">''</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    # We use Nix string interpolation to pass the user's chosen programming</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    # language to our script.</span>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">    npm init --yes my-boot-strap@latest "$out" -- <strong>--lang=</span><span class="devsite-syntax-si">${</span>language<span class="devsite-syntax-si">}</span></strong>
<span class="devsite-syntax-s devsite-syntax-s-Multiline">  ''</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<p>Another common pattern is to conditionally include content depending on the
value of a string. Another way to write the previous example is:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="Nix"><code translate="no" dir="ltr">npm init <span class="devsite-syntax-o">--</span>yes my-boot-strap<span class="devsite-syntax-p">@</span>latest <span class="devsite-syntax-s2">"$out"</span> <span class="devsite-syntax-o">--</span> <span class="devsite-syntax-err">\</span>
    <strong><span class="devsite-syntax-si">${</span><span class="devsite-syntax-k">if</span> <span class="devsite-syntax-ss">language</span> <span class="devsite-syntax-o">==</span> <span class="devsite-syntax-s2">"ts"</span> <span class="devsite-syntax-k">then</span> <span class="devsite-syntax-s2">"--lang=ts"</span> <span class="devsite-syntax-k">else</span> <span class="devsite-syntax-s2">"--lang=js"</span> <span class="devsite-syntax-si">}</span></strong>
</code></pre></devsite-code><aside class="special"><strong>Important:</strong><span> Remember to always produce a <code translate="no" dir="ltr">.idx/dev.nix</code> file in the <code translate="no" dir="ltr">$out</code>
directory as part of your <code translate="no" dir="ltr">bootstrap</code> script. If the generated workspace
environment needs to vary based on user-configured parameters (for example,
including different system packages, or customizing the <code translate="no" dir="ltr">onCreate</code> hook),
you can use string manipulation in Nix, or call out to a templating engine
such as <a href="https://jinja.palletsprojects.com/en/3.1.x/">jinja2</a>.</span></aside>
<h3 id="open-files" data-text="Choose which files should open by default" tabindex="-1">Choose which files should open by default</h3>

<p>It&#39;s a good idea to customize which files should be opened for editing when new
workspaces are created with your template. For example, if your template is for
a basic website, you may want to open the main HTML, JavaScript, and CSS files.</p>

<p>To customize which files should open by default, update your <code translate="no" dir="ltr">.idx/dev.nix</code> file
(<em>not</em> your <code translate="no" dir="ltr">idx-template.nix</code> file!) to include an <code translate="no" dir="ltr">onCreate</code> workspace hook
with an <code translate="no" dir="ltr">openFiles</code> attribute, like so:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy" translate="no" dir="ltr" is-upgraded syntax="Nix"><code translate="no" dir="ltr"><span class="devsite-syntax-c1"># .idx/dev.nix</span>
<span class="devsite-syntax-p">{</span>pkgs<span class="devsite-syntax-p">}:</span> <span class="devsite-syntax-p">{</span>
  <span class="devsite-syntax-o">...</span>
  <span class="devsite-syntax-ss">idx</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span>
    <span class="devsite-syntax-c1"># Workspace lifecycle hooks</span>
    <span class="devsite-syntax-ss">workspace</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span>
      <span class="devsite-syntax-c1"># Runs when a workspace is first created with this `dev.nix` file</span>
      <span class="devsite-syntax-ss">onCreate</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span>
        <span class="devsite-syntax-c1"># Open editors for the following files by default, if they exist.</span>
        <span class="devsite-syntax-c1"># The last file in the list will be focused.</span>
        default<span class="devsite-syntax-o">.</span><span class="devsite-syntax-ss">openFiles</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">[</span>
          <span class="devsite-syntax-s2">"src/index.css"</span>
          <span class="devsite-syntax-s2">"src/index.js"</span>
          <span class="devsite-syntax-s2">"src/index.html"</span>
        <span class="devsite-syntax-p">];</span>
        <span class="devsite-syntax-c1"># Include other scripts here, as needed, for example:</span>
        <span class="devsite-syntax-c1"># installDependencies = "npm install";</span>
      <span class="devsite-syntax-p">};</span>
      <span class="devsite-syntax-c1"># To run something each time the workspace is (re)started, use the `onStart` hook</span>
    <span class="devsite-syntax-p">};</span>
    <span class="devsite-syntax-c1"># Enable previews and customize configuration</span>
    <span class="devsite-syntax-ss">previews</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-p">{</span> <span class="devsite-syntax-o">...</span> <span class="devsite-syntax-p">};</span>
  <span class="devsite-syntax-p">};</span>
<span class="devsite-syntax-p">}</span>
</code></pre></devsite-code>
<h3 id="custom-icon" data-text="Choose a default workspace icon" tabindex="-1">Choose a default workspace icon</h3>

<p>You can choose the default icon for workspaces created with your template,
by placing a PNG file named <code translate="no" dir="ltr">icon.png</code> next to the <code translate="no" dir="ltr">dev.nix</code> file, inside the
<code translate="no" dir="ltr">.idx</code> directory.</p>
<aside class="note"><strong>Note:</strong><span> The <code translate="no" dir="ltr">idx-template.json</code> file also includes an optional <code translate="no" dir="ltr">icon</code> property,
which should point to a public PNG or SVG URL, when provided. This field is
not used in <span class="notranslate">Firebase Studio</span>.</span></aside>
<h2 id="create-workspace" data-text="Test your template in a new workspace" tabindex="-1">Test your template in a new workspace</h2>

<p>The simplest way to test your template end-to-end is to create a new workspace
with it. Visit the following link, replacing the example with your template&#39;s
GitHub repository URL:</p>
<div></div><devsite-code><pre class="devsite-click-to-copy devsite-code-highlight" translate="no" dir="ltr" is-upgraded syntax="Text only" syntax-guessed><code translate="no" dir="ltr">https://idx.google.com/new?template=<strong>https://github.com/my-org/my-repo</strong>
</code></pre></devsite-code>
<p>You can optionally include a branch and subfolder. All of the following are
valid, as long as they are publicly accessible:</p>

<ul>
<li><code translate="no" dir="ltr">https://github.com/my-org/my-repo/</code></li>
<li><code translate="no" dir="ltr">https://github.com/my-org/my-repo/tree/main/path/to/myidxtemplate</code></li>
<li><code translate="no" dir="ltr">https://github.com/my-org/my-repo/tree/branch</code></li>
<li><code translate="no" dir="ltr">https://github.com/my-org/my-repo/tree/branch/path/to/myidxtemplate</code></li>
</ul>

<p>This is also the URL you&#39;ll share with others so that they can use your new
template, or the URL you&#39;ll link to from your <a href="/docs/studio/open-in-firebase-studio">&quot;Open in <span class="notranslate">Firebase Studio</span>&quot;
button</a>.</p>

<hr>



<h2 id="share-template" data-text="Share your template" tabindex="-1">Share your template</h2>

<p>After you&#39;ve confirmed that your template behaves as expected, publish it to a
GitHub repository and share the same link you used when <a href="#create-workspace">creating a workspace
for testing</a>.</p>

<p>And to make it even easier for users to find your template, add an <a href="/docs/studio/open-in-firebase-studio">&quot;Open in
<span class="notranslate">Firebase Studio</span>&quot; button</a> to your
website or repository README.</p>


  

  
    <devsite-hats-survey class="nocontent" data-nosnippet
      hats-id="Eo9GZTcG10ncf3CThQj0SEgFWynR"
      listnr-id="5244646"></devsite-hats-survey>
  
</div>

  
    
      <devsite-recommendations display="in-page" hidden yield>
      </devsite-recommendations>
    
    
      
    <devsite-thumb-rating position="footer">
    </devsite-thumb-rating>
  
       
         <devsite-feedback
  position="footer"
  project-name="Firebase Studio"
  product-id="719752"
  bucket=""
  context=""
  version="t-devsite-webserver-20260825-r00-rc00.479916215390653058"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="footer"
  class="nocontent"
  data-nosnippet
  
  
    project-feedback-url="https://firebase.google.com/support/contact/bugs-features/"
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/touchicon-180.png"
  
  
    project-support-url="https://firebase.google.com/support/troubleshooter/report"
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
       
    
    
      <devsite-recommendations id="recommendations-link" yield></devsite-recommendations>
    
  

  <div class="devsite-floating-action-buttons"></div></article>


<devsite-content-footer class="nocontent" data-nosnippet>
  <p>Except as otherwise noted, the content of this page is licensed under the <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 License</a>, and code samples are licensed under the <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a>. For details, see the <a href="https://developers.google.com/site-policies">Google Developers Site Policies</a>. Java is a registered trademark of Oracle and/or its affiliates.</p>
  <p>Last updated 2026-08-24 UTC.</p>
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
    <h3 class="devsite-footer-linkbox-heading no-link">Learn</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            >
            
          
            Developer guides
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/reference/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            >
            
          
            SDK & API reference
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/samples/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            >
            
          
            Samples
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/libraries/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            >
            
          
            Libraries
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//github.com/firebase/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            >
            
              
              
            
          
            GitHub
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Stay connected</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//firebase.blog"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            >
            
          
            Check out the blog
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.reddit.com/r/Firebase"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            >
            
          
            Find us on Reddit
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//x.com/Firebase"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            >
            
          
            Follow on X
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/user/Firebase"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            >
            
          
            Subscribe on YouTube
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/community/events"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            >
            
              
              
            
          
            Attend an event
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Support</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/support/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            >
            
          
            Contact support
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//stackoverflow.com/questions/tagged/firebase"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            >
            
          
            Stack Overflow
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//groups.google.com/forum/#!forum/firebase-talk"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            >
            
          
            Google group
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/support/releases"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            >
            
          
            Release notes
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/brand-guidelines/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            >
            
          
            Brand guidelines
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/support/faq/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 6)"
            >
            
              
              
            
          
            FAQs
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
  </ul>
  
</nav>
          
        </devsite-footer-linkboxes>
        <devsite-footer-utility class="devsite-footer">
          
            

<div class="devsite-footer-utility nocontent" data-nosnippet>
  
  
  <nav class="devsite-footer-sites" aria-label="Other Google Developers websites">
    <a href="https://developers.google.com/"
       class="devsite-footer-sites-logo-link gc-analytics-event"
       data-category="Site-Wide Custom Events"
       data-label="Footer Google Developers Link">
      <picture>
        
        <source srcset="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/lockup-google-for-developers-dark-theme.svg"
                media="(prefers-color-scheme: none)"
                class="devsite-dark-theme">
        
        <img class="devsite-footer-sites-logo"
             src="https://www.gstatic.com/devrel-devsite/prod/vdc800838fb8be04a9a7685606311d18c65800504bccf261551968ac74bffd42e/firebase/images/lockup-google-for-developers.svg"
             loading="lazy"
             alt="Google Developers">
      </picture>
    </a>
    <ul class="devsite-footer-sites-list">
      
      <li class="devsite-footer-sites-item">
        <a href="//developer.android.com"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer Android Link"
         
         >
          Android
        </a>
      </li>
      
      <li class="devsite-footer-sites-item">
        <a href="//developer.chrome.com/home"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer Chrome Link"
         
         >
          Chrome
        </a>
      </li>
      
      <li class="devsite-footer-sites-item">
        <a href="//firebase.google.com"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer Firebase Link"
         
         >
          Firebase
        </a>
      </li>
      
      <li class="devsite-footer-sites-item">
        <a href="//cloud.google.com"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer Google Cloud Platform Link"
         
         >
          Google Cloud Platform
        </a>
      </li>
      
      <li class="devsite-footer-sites-item">
        <a href="//developers.google.com/products/"
           class="devsite-footer-sites-link
                  gc-analytics-event"
           data-category="Site-Wide Custom Events"
         
           data-label="Footer All products Link"
         
         >
          All products
        </a>
      </li>
      
    </ul>
  </nav>
  

  
  <nav class="devsite-footer-utility-links" aria-label="Utility links">
    
    <ul class="devsite-footer-utility-list">
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="/terms/"
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
        
          <devsite-concierge
  
  
  
    data-ai-panel
  
  
  
  >
</devsite-concierge>
        
      </section>
      </section>
    <devsite-sitemask></devsite-sitemask>
    <devsite-snackbar></devsite-snackbar>
    <devsite-tooltip ></devsite-tooltip>
    <devsite-heading-link></devsite-heading-link>
    <devsite-analytics>
      
        

      
    </devsite-analytics>
    
      <devsite-badger></devsite-badger>
    
    
    <firebase-gtm></firebase-gtm>

  <firebase-utm></firebase-utm>

<cloudx-track></cloudx-track>

  <cloudx-free-trial-eligible-store freeTrialEligible="true"></cloudx-free-trial-eligible-store>

    


    <devsite-a11y-announce></devsite-a11y-announce>
  </body>
</html>