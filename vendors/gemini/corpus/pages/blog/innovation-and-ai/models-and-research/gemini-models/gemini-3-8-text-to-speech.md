





<!DOCTYPE html>
<html class="no-js glue-flexbox  keyword-blog" lang="en-us" data-locale="en-us" data-version="pr20261008-1701">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <title>Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=1.0, minimum-scale=1.0" />
        <meta name="optimize_experiments" content="[]">

        
  




<!--Article Specific Metadata-->
<meta name="description" content="Gemini 3.8 Flash-Lite TTS and Gemini 3.8 Flash TTS are our most expressive audio models yet."/>
<meta name="keywords" content="None"/>
<meta name="article-author" content="Leland Rechis, Alan Cowen"/>
<meta name="robots" content="max-image-preview:large">

<!--Open Graph Metadata-->
<meta property="og:type" content="article" />
<meta property="og:title" content="Gemini 3.8 text-to-speech says hello"/>

<meta property="og:description" content="Gemini 3.8 Flash-Lite TTS and Gemini 3.8 Flash TTS are our most expressive audio models yet." />
<meta property="og:image" content="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__keyword__metacard__light.width-1300.png" />
<meta property="og:site_name" content="Google" />
<meta property="og:url" content="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/" />
<meta property="article:publisher" content="https://www.facebook.com/Google/" />
<meta property="article:published_time" content="2026-09-23" />

<!--Twitter Card Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:url" content="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/" />
<meta name="twitter:title" content="Gemini 3.8 text-to-speech says hello"/>
<meta name="twitter:description" content="Gemini 3.8 Flash-Lite TTS and Gemini 3.8 Flash TTS are our most expressive audio models yet." />
<meta name="twitter:image:src" content="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__keyword__metacard__light.width-1300.png" />
<meta name="twitter:site" content="@google" />







        
  <meta name="page" content="86315" />
  <meta name="locale" content="en-us" />
  <meta name="published_time" content="2026-09-23T15:15:00+00:00" />
  <meta name="content_type" content="blogv2.articlepage" />
  <meta name="tags" content="Gemini models" />
  <meta name="authors" content="Leland Rechis,Alan Cowen" />



        
        

        
        
  
  
  




        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        


        
        
        <link class="deferred-stylesheet" rel="preload" type="text/css" href="/static/keyword/css/blog/index.min.css?version=pr20261008-1701" as="style">
<noscript>
  <link rel="stylesheet" href="/static/keyword/css/blog/index.min.css?version=pr20261008-1701">
</noscript>

        <link class="deferred-stylesheet" rel="preload" type="text/css" href="https://fonts.googleapis.com/css?family=Google+Sans:400,500,600,700|Google+Sans+Flex:400,500|Product+Sans:400&amp;display=swap&amp;lang=en" as="style">
<noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Google+Sans:400,500,600,700|Google+Sans+Flex:400,500|Product+Sans:400&amp;display=swap&amp;lang=en">
</noscript>

        <link class="deferred-stylesheet" rel="preload" type="text/css" href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css" as="style">
<noscript>
  <link rel="stylesheet" href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css">
</noscript>


        
        
        

	
        

        
  
            
        
  
  <link rel="stylesheet" type="text/css" href="/static/keyword/css/print/index.min.css?version=pr20261008-1701" media="print" />


        

<link rel="canonical" href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"/>

<link rel="icon" type="image/x-icon" href="/static/blogv2/images/favicon.ico?version=pr20261008-1701">
<link href="/static/blogv2/images/apple-touch-icon.png?version=pr20261008-1701" rel="apple-touch-icon">



        <meta property="gtm-tag" content="GTM-TRV24V">



        <!-- https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API -->


      </head>

    <body class="template-articlepage keyword-blog">
        
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TRV24V" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>


        


<div class="data-layer-init-data" data-ga4-analytics='
  {
    "event": "dataLayer_initialized",
    
      "page_name": "Gemini 3.8 Flash TTS and Gemini 3.8 Flash\u002DLite TTS",
    
    "experiments": "undefined",
    "locale": "en-us",
    "page_type": "blogv2 | article page",
    "primary_tag": "topics - gemini models",
    "secondary_tags": "undefined",
    
      "landing_page_tags": "undefined",
    
    
      "article_name": "Gemini 3.8 text\u002Dto\u002Dspeech says hello",
      "author_name": "Leland Rechis, Alan Cowen",
    
    "publish_date": "2026-09-23|15:15",
    "hero_media": "image",
    
      "special_hero": "undefined",
    
    "days_since_published": "15",
    
      "content_category": "Topics - Gemini models",
    
    "word_count": "long 600+",
    "has_audio": "no",
    "has_video": "yes"
  }'>
</div>

        

        <svg class="uni-svg-defs" width="0" height="0" style="position:absolute; width:0; height:0; overflow:hidden;" aria-hidden="true">
  <defs>
    <mask id="uni-spark-4c-mask" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="14" height="14">
      <path d="M6.99902 0.507812C7.13501 0.507851 7.25382 0.600537 7.28711 0.732422C7.38892 1.13635 7.52126 1.53079 7.68652 1.91406C8.11701 2.91409 8.70808 3.78913 9.45801 4.53906C10.2083 5.28897 11.083 5.88007 12.083 6.31055C12.4665 6.47572 12.86 6.60818 13.2637 6.70996C13.3957 6.74316 13.4893 6.86193 13.4893 6.99805C13.4892 7.13413 13.3957 7.25294 13.2637 7.28613C12.8599 7.38792 12.4661 7.52037 12.083 7.68555C11.083 8.11603 10.2079 8.70709 9.45801 9.45703C8.70807 10.2073 8.11701 11.082 7.68652 12.082C7.52135 12.4655 7.3889 12.859 7.28711 13.2627C7.25392 13.3947 7.13511 13.4882 6.99902 13.4883C6.86291 13.4883 6.74414 13.3948 6.71094 13.2627C6.60915 12.859 6.47669 12.4651 6.31152 12.082C5.88105 11.082 5.29031 10.207 4.54004 9.45703C3.78974 8.7071 2.91507 8.11603 1.91504 7.68555C1.5314 7.52029 1.13733 7.38795 0.733398 7.28613C0.60151 7.25284 0.508825 7.13404 0.508789 6.99805C0.508789 6.86204 0.601504 6.74327 0.733398 6.70996C1.13732 6.60815 1.53177 6.47581 1.91504 6.31055C2.91509 5.88006 3.7901 5.289 4.54004 4.53906C5.28998 3.78912 5.88104 2.91411 6.31152 1.91406C6.47678 1.53043 6.60913 1.13635 6.71094 0.732422C6.74425 0.600531 6.86302 0.507812 6.99902 0.507812Z" fill="black"/>
      <path d="M6.99902 0.507812C7.13501 0.507851 7.25382 0.600537 7.28711 0.732422C7.38892 1.13635 7.52126 1.53079 7.68652 1.91406C8.11701 2.91409 8.70808 3.78913 9.45801 4.53906C10.2083 5.28897 11.083 5.88007 12.083 6.31055C12.4665 6.47572 12.86 6.60818 13.2637 6.70996C13.3957 6.74316 13.4893 6.86193 13.4893 6.99805C13.4892 7.13413 13.3957 7.25294 13.2637 7.28613C12.8599 7.38792 12.4661 7.52037 12.083 7.68555C11.083 8.11603 10.2079 8.70709 9.45801 9.45703C8.70807 10.2073 8.11701 11.082 7.68652 12.082C7.52135 12.4655 7.3889 12.859 7.28711 13.2627C7.25392 13.3947 7.13511 13.4882 6.99902 13.4883C6.86291 13.4883 6.74414 13.3948 6.71094 13.2627C6.60915 12.859 6.47669 12.4651 6.31152 12.082C5.88105 11.082 5.29031 10.207 4.54004 9.45703C3.78974 8.7071 2.91507 8.11603 1.91504 7.68555C1.5314 7.52029 1.13733 7.38795 0.733398 7.28613C0.60151 7.25284 0.508825 7.13404 0.508789 6.99805C0.508789 6.86204 0.601504 6.74327 0.733398 6.70996C1.13732 6.60815 1.53177 6.47581 1.91504 6.31055C2.91509 5.88006 3.7901 5.289 4.54004 4.53906C5.28998 3.78912 5.88104 2.91411 6.31152 1.91406C6.47678 1.53043 6.60913 1.13635 6.71094 0.732422C6.74425 0.600531 6.86302 0.507812 6.99902 0.507812Z" fill="url(#uni-spark-4c-paint0)"/>
    </mask>

    <filter id="uni-spark-4c-filter0" x="-3.45662" y="3.13713" width="7.85561" height="8.6437" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="0.49198" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter1" x="-2.49131" y="-7.546" width="16.9748" height="17.1389" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="2.37847" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter2" x="-3.64737" y="2.89364" width="15.8924" height="18.1854" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="2.02193" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter3" x="-3.64737" y="2.89364" width="15.8924" height="18.1854" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="2.02193" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter4" x="-3.46085" y="3.60068" width="15.9481" height="16.3026" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="2.02193" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter5" x="6.47649" y="-1.80378" width="15.0246" height="14.7521" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="1.92142" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter6" x="-6.27061" y="-0.0870199" width="10.8225" height="10.9162" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="1.06109" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter7" x="-7.22718" y="-2.76331" width="15.6663" height="15.7922" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="1.7508" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter8" x="2.131" y="-0.684428" width="15.7771" height="15.5095" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="1.5551" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter9" x="0.30029" y="0.402829" width="7.26466" height="7.47559" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="0.769289" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter10" x="2.82374" y="0.247572" width="8.97556" height="7.63767" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="0.84887" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter11" x="-2.59673" y="-5.75298" width="14.1729" height="13.8614" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="1.17532" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <filter id="uni-spark-4c-filter12" x="-2.32435" y="4.70006" width="11.1008" height="10.3147" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="1.45466" result="effect1_foregroundBlur_17771_12257"/>
    </filter>
    <linearGradient id="uni-spark-4c-paint0" x1="4.19868" y1="9.1928" x2="10.9405" y2="3.50884" gradientUnits="userSpaceOnUse">
      <stop stop-color="#3C90FF"/>
      <stop offset="0.27" stop-color="#3C90FF"/>
      <stop offset="0.776981" stop-color="#969DFF"/>
      <stop offset="1" stop-color="#BD99FE"/>
    </linearGradient>
    <linearGradient id="uni-spark-4c-paint1" x1="4.89424" y1="0" x2="4.89424" y2="9.04247" gradientUnits="userSpaceOnUse">
      <stop offset="0.75" stop-color="#3186FF"/>
      <stop offset="1" stop-color="#00A5B7"/>
    </linearGradient>
    <linearGradient id="uni-spark-4c-paint2" x1="3.93267" y1="1.43467" x2="3.93267" y2="6.84622" gradientUnits="userSpaceOnUse">
      <stop offset="0.120192" stop-color="#FF5A59"/>
      <stop offset="0.899038" stop-color="#FEC700"/>
    </linearGradient>
    <linearGradient id="uni-spark-4c-paint3" x1="6.23948" y1="3.71631" x2="7.60016" y2="5.28663" gradientUnits="userSpaceOnUse">
      <stop offset="0.321566" stop-color="#FE85DF"/>
      <stop offset="0.602767" stop-color="#9378FF"/>
      <stop offset="0.910378" stop-color="#3186FF"/>
    </linearGradient>
    <linearGradient id="uni-spark-4c-paint4" x1="6.68578" y1="2.5527" x2="-0.540806" y2="3.55631" gradientUnits="userSpaceOnUse">
      <stop offset="0.600962" stop-color="#FC413D"/>
      <stop offset="1" stop-color="#FF6B2B"/>
    </linearGradient>
    <linearGradient id="uni-spark-4c-paint5" x1="2.88101" y1="9.07635" x2="4.57563" y2="7.56988" gradientUnits="userSpaceOnUse">
      <stop offset="0.192308" stop-color="#FFE921"/>
      <stop offset="0.8125" stop-color="#88DE42"/>
    </linearGradient>
    <radialGradient id="gd-uni-icon-noteboooklm" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(5.7 24) rotate(-61.472) scale(19.0241 13.1919)">
      <stop stop-color="#4197E9"/>
      <stop offset="1" stop-color="#47EA93"/>
    </radialGradient>
  </defs>
</svg>


        



        
          
          


<div class="uni-nav__content-pusher"></div>
<header
  class="uni-nav redesign-patch uni-page--fullbleed uni-nav-article"
  data-content-type="blogv2 | article page"
  data-component="uni-header">
  <div class="uni-page">
    <nav class="uni-nav__container">
      
      <div class="uni-nav__jump-to-content-wrapper">
        <uni-cta href="#jump-content" class="uni-nav__jump-to-content" emphasis="medium">
          Skip to main content
        </uni-cta>
      </div>
      <div class="uni-nav__left" data-analytics-module='{
          "module_name": "main nav",
          "section_header": "News from Google"
        }'>
        <!-- Mobile Menu Toggle -->
        <button class="uni-nav__menu-btn uni-nav__menu-btn--open" aria-label="Open Menu" aria-expanded="false">
          <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#h-burger"></use>
</svg>

        </button>
        <button class="uni-nav__menu-btn uni-nav__menu-btn--close" aria-label="Close Menu"
          aria-expanded="false">
          <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-clear"></use>
</svg>

        </button>
        <!-- Logo -->
        
        
          <a href="/" class="uni-nav__logo" aria-label="News from Google" title="News from Google">
            <svg
  
  
  
  
  
  
  role="img"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#news-from-google-logo"></use>
</svg>

            <!-- SuperG Logo -->
            <img class="uni-nav__logo--super-g" src="/static/blogv2/images/super-g-aurora.svg?version=pr20261008-1701" alt="" width="30" height="30" aria-hidden="true">
          </a>
        
        
          <p class="uni-nav-article__article-title font-body-m">Gemini 3.8 text-to-speech says hello</p>
        
      </div>
      

<div id="mobile-menu-overlay" class="uni-nav-mobile__wrapper" aria-hidden="true"
  data-analytics-module='{
      "module_name":"main nav",
      "section_header": "Mobile menu"
   }'>
  <nav
    class="uni-nav-mobile"
    aria-modal="true">
    <div class="uni-nav-mobile__container">
      <section class="uni-nav-mobile__section">
        <ul class="uni-nav-mobile__link-list">
          
            
            <li class="uni-nav-mobile__link-list-item">
              <button
                class="uni-nav-link uni-nav-link--full-width uni-nav-link--main-menu uni-nav-link--has-subnav font-body-xl"
                aria-expanded="false"
                aria-controls="mobile-subnav-1">
                Innovation &amp; AI
                <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

              </button>
            </li>
            
          
            
            <li class="uni-nav-mobile__link-list-item">
              <button
                class="uni-nav-link uni-nav-link--full-width uni-nav-link--main-menu uni-nav-link--has-subnav font-body-xl"
                aria-expanded="false"
                aria-controls="mobile-subnav-2">
                Products &amp; platforms
                <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

              </button>
            </li>
            
          
            
            <li class="uni-nav-mobile__link-list-item">
              <button
                class="uni-nav-link uni-nav-link--full-width uni-nav-link--main-menu uni-nav-link--has-subnav font-body-xl"
                aria-expanded="false"
                aria-controls="mobile-subnav-3">
                Company news
                <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

              </button>
            </li>
            
          
            
              <li class="uni-nav-mobile__link-list-item">
                <a href="/feed" class="uni-nav-link uni-nav-link--full-width uni-nav-link--main-menu font-body-xl">Feed</a>
              </li>
            
          
        </ul>
      </section>
      
        
          
          <section class="uni-nav-mobile__section">
            <uni-cta class="uni-nav__subscribe" href="/newsletter-subscribe/" emphasis="high"><span>Newsletter</span></uni-cta>
          </section>
        
      
      <div class="uni-nav-mobile__shape-container">
        <div class="uni-nav-mobile__shape" data-shape="pill"></div>
      </div>
    </div>
  </nav>
  
    
      

<div id="mobile-subnav-1" class="uni-nav-mobile-subnav" aria-hidden="true">
  <div class="uni-nav-mobile-subnav__container">
    <section class="uni-nav-mobile-subnav__header uni-nav-mobile__section uni-nav-mobile__section--divider">
      <button type="button" class="uni-nav-link uni-nav-mobile-subnav__back-btn font-body-xl" aria-label="Back">
        <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

        Back
      </button>
    </section>
    <section class="uni-nav-mobile__section uni-nav-mobile__section--intro">
      <h3 class="uni-nav-mobile__section-title font-h3">Innovation &amp; AI</h3>
      
      
        <uni-cta class="uni-nav-mobile__see-all-cta" href="/innovation-and-ai/" emphasis="medium" icon-id-right="arrow-forward" additional-class="uni-nav-link--subitem-cta">
          
            See all in Innovation &amp; AI
          
        </uni-cta>
      
    </section>

    <section class="uni-nav-mobile__section">
      <ul class="uni-nav-mobile__link-list">
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-1-1">
              Models &amp; Research
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-1-1">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/models-and-research/google-deepmind/"
                    data-navigation="models-research">
                    Google DeepMind
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/models-and-research/google-research/"
                    data-navigation="models-research">
                    Google Research
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/models-and-research/google-labs/"
                    data-navigation="models-research">
                    Google Labs
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/models-and-research/gemini-models/"
                    data-navigation="models-research">
                    Gemini models
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/models-and-research/quantum-computing/"
                    data-navigation="models-research">
                    Quantum computing
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/innovation-and-ai/models-and-research/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Models &amp; Research">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-1-2">
              Products
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-1-2">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/technology/developers-tools/"
                    data-navigation="products">
                    Developer tools
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/products/gemini-app/"
                    data-navigation="products">
                    Gemini app
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/products/gemini-notebook/"
                    data-navigation="products">
                    Gemini Notebook
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/innovation-and-ai/products/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Products">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-1-3">
              Infrastructure &amp; cloud
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-1-3">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/infrastructure-and-cloud/global-network/"
                    data-navigation="infrastructure-cloud">
                    Global network
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/infrastructure-and-cloud/google-cloud/"
                    data-navigation="infrastructure-cloud">
                    Google Cloud
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/innovation-and-ai/infrastructure-and-cloud/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Infrastructure &amp; cloud">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-1-4">
              Technology
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-1-4">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/technology/safety-security/"
                    data-navigation="technology">
                    Safety &amp; Security
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/technology/health/"
                    data-navigation="technology">
                    Health
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/innovation-and-ai/technology/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Technology">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
      </ul>
    </section>
    
      <hr class="uni-nav-mobile__divider"></hr>
      <section class="uni-nav-mobile__section">
        <p class="font-h6 uni-nav-mobile__section-title--small">Learn more:</p>
        <ul class="uni-nav-mobile__link-list">
        
          <li class="uni-nav-mobile__link-list-item">
            <a href="https://deepmind.google/blog/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
              Google DeepMind blog
              <span class="uni-nav-link--learn-more-icon"><svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>
</span>
            </a>
          </li>
        
          <li class="uni-nav-mobile__link-list-item">
            <a href="https://research.google/blog/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
              Google Research blog
              <span class="uni-nav-link--learn-more-icon"><svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>
</span>
            </a>
          </li>
        
          <li class="uni-nav-mobile__link-list-item">
            <a href="https://developers.googleblog.com/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
              Google Developers blog
              <span class="uni-nav-link--learn-more-icon"><svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>
</span>
            </a>
          </li>
        
          <li class="uni-nav-mobile__link-list-item">
            <a href="https://cloud.google.com/blog" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
              Google Cloud blog
              <span class="uni-nav-link--learn-more-icon"><svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>
</span>
            </a>
          </li>
        
        </ul>
      </section>
    
  </div>
  <div class="uni-nav-mobile__shape-container uni-nav-mobile__shape-container--subnav">
    <div class="uni-nav-mobile__shape uni-nav-mobile__shape--4-sided-cookie" data-shape="4-sided-cookie"></div>
  </div>
</div>

    
  
    
      

<div id="mobile-subnav-2" class="uni-nav-mobile-subnav" aria-hidden="true">
  <div class="uni-nav-mobile-subnav__container">
    <section class="uni-nav-mobile-subnav__header uni-nav-mobile__section uni-nav-mobile__section--divider">
      <button type="button" class="uni-nav-link uni-nav-mobile-subnav__back-btn font-body-xl" aria-label="Back">
        <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

        Back
      </button>
    </section>
    <section class="uni-nav-mobile__section uni-nav-mobile__section--intro">
      <h3 class="uni-nav-mobile__section-title font-h3">Products &amp; platforms</h3>
      
      
        <uni-cta class="uni-nav-mobile__see-all-cta" href="/products-and-platforms/" emphasis="medium" icon-id-right="arrow-forward" additional-class="uni-nav-link--subitem-cta">
          
            See all in Products &amp; platforms
          
        </uni-cta>
      
    </section>

    <section class="uni-nav-mobile__section">
      <ul class="uni-nav-mobile__link-list">
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-2-1">
              Products
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-2-1">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/products/search/"
                    data-navigation="products">
                    Search
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/products/maps/"
                    data-navigation="products">
                    Maps
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/products/chrome/"
                    data-navigation="products">
                    Chrome
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/products/google-health/"
                    data-navigation="products">
                    Google Health
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/products/workspace/"
                    data-navigation="products">
                    Google Workspace
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/products/education/"
                    data-navigation="products">
                    Learning &amp; Education
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/products/shopping/"
                    data-navigation="products">
                    Shopping
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/products-and-platforms/products/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Products">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-2-2">
              Platforms
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-2-2">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/platforms/android/"
                    data-navigation="platforms">
                    Android
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/platforms/google-play/"
                    data-navigation="platforms">
                    Google Play
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/platforms/wear-os/"
                    data-navigation="platforms">
                    Wear OS
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/products-and-platforms/platforms/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Platforms">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-2-3">
              Devices
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-2-3">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/devices/pixel/"
                    data-navigation="devices">
                    Pixel
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/devices/google-nest/"
                    data-navigation="devices">
                    Google Nest
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/devices/fitbit/"
                    data-navigation="devices">
                    Fitbit
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/devices/chromebooks/"
                    data-navigation="devices">
                    Chromebook
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/products-and-platforms/devices/googlebook/"
                    data-navigation="devices">
                    Googlebook
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/products-and-platforms/devices/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Devices">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
      </ul>
    </section>
    
      <hr class="uni-nav-mobile__divider"></hr>
      <section class="uni-nav-mobile__section">
        <p class="font-h6 uni-nav-mobile__section-title--small">Learn more:</p>
        <ul class="uni-nav-mobile__link-list">
        
          <li class="uni-nav-mobile__link-list-item">
            <a href="https://blog.google/products/ads-commerce/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
              Google Ads &amp; Commerce blog
              <span class="uni-nav-link--learn-more-icon"><svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>
</span>
            </a>
          </li>
        
          <li class="uni-nav-mobile__link-list-item">
            <a href="https://blog.google/waze/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
              Waze blog
              <span class="uni-nav-link--learn-more-icon"><svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>
</span>
            </a>
          </li>
        
        </ul>
      </section>
    
  </div>
  <div class="uni-nav-mobile__shape-container uni-nav-mobile__shape-container--subnav">
    <div class="uni-nav-mobile__shape uni-nav-mobile__shape--8-leaf-clover" data-shape="8-leaf-clover"></div>
  </div>
</div>

    
  
    
      

<div id="mobile-subnav-3" class="uni-nav-mobile-subnav" aria-hidden="true">
  <div class="uni-nav-mobile-subnav__container">
    <section class="uni-nav-mobile-subnav__header uni-nav-mobile__section uni-nav-mobile__section--divider">
      <button type="button" class="uni-nav-link uni-nav-mobile-subnav__back-btn font-body-xl" aria-label="Back">
        <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

        Back
      </button>
    </section>
    <section class="uni-nav-mobile__section uni-nav-mobile__section--intro">
      <h3 class="uni-nav-mobile__section-title font-h3">Company news</h3>
      
      
        <uni-cta class="uni-nav-mobile__see-all-cta" href="/company-news/" emphasis="medium" icon-id-right="arrow-forward" additional-class="uni-nav-link--subitem-cta">
          
            See all in Company news
          
        </uni-cta>
      
    </section>

    <section class="uni-nav-mobile__section">
      <ul class="uni-nav-mobile__link-list">
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-3-1">
              Outreach &amp; initiatives
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-3-1">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/company-news/outreach-and-initiatives/creating-opportunity/"
                    data-navigation="outreach-initiatives">
                    Creating opportunity
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/technology/safety-security/"
                    data-navigation="outreach-initiatives">
                    Safety &amp; security
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/company-news/outreach-and-initiatives/google-org/"
                    data-navigation="outreach-initiatives">
                    Google.org
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/company-news/outreach-and-initiatives/public-policy/"
                    data-navigation="outreach-initiatives">
                    Public policy
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/company-news/outreach-and-initiatives/sustainability/"
                    data-navigation="outreach-initiatives">
                    Sustainability
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/innovation-and-ai/technology/health/"
                    data-navigation="outreach-initiatives">
                    Health
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/company-news/outreach-and-initiatives/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Outreach &amp; initiatives">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-3-2">
              Leadership
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-3-2">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/authors/sundar-pichai/"
                    data-navigation="leadership">
                    Sundar Pichai, CEO
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/authors/"
                    data-navigation="leadership">
                    More authors
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/authors/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Leadership">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
        <li class="uni-nav-mobile__link-list-item has-submenu">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--full-width uni-nav-mobile-subnav__sublist-trigger font-body-xl" aria-controls="mobile-subnav-sublist-3-3">
              Inside Google
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            <ul class="uni-nav-mobile-subnav__sublist" aria-hidden="true" id="mobile-subnav-sublist-3-3">
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/company-news/inside-google/around-the-globe/"
                    data-navigation="inside-google">
                    Around the globe
                    
                  </a>
                </li>
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  
                  <a class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--full-width font-body-m"
                    href="/company-news/inside-google/life-at-google/"
                    data-navigation="inside-google">
                    Life at Google
                    
                  </a>
                </li>
              
              
                <li class="uni-nav-mobile-subnav__sublist-item">
                  <a href="/company-news/inside-google/"
                    class="uni-nav-link uni-nav-link--sublist-mobile uni-nav-link--sublist font-body-m"
                    data-navigation="Inside Google">
                    See all
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>

                  </a>
                </li>
              
            </ul>
          
        </li>
      
      </ul>
    </section>
    
      <hr class="uni-nav-mobile__divider"></hr>
      <section class="uni-nav-mobile__section">
        <p class="font-h6 uni-nav-mobile__section-title--small">Learn more:</p>
        <ul class="uni-nav-mobile__link-list">
        
          <li class="uni-nav-mobile__link-list-item">
            <a href="https://blog.google/security/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
              Google Security blog
              <span class="uni-nav-link--learn-more-icon"><svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>
</span>
            </a>
          </li>
        
        </ul>
      </section>
    
  </div>
  <div class="uni-nav-mobile__shape-container uni-nav-mobile__shape-container--subnav">
    <div class="uni-nav-mobile__shape uni-nav-mobile__shape--4-leaf-clover" data-shape="4-leaf-clover"></div>
  </div>
</div>

    
  
    
  
</div>


      <div class="uni-nav__primary" data-analytics-module='{
          "module_name":"main nav",
          "section_header": "Desktop menu"
      }'>
        <ul class="uni-nav__list">
        
          <li class="uni-nav__item">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--desktop uni-nav-link--dropdown font-body-s" aria-expanded="false" aria-controls="desktop-nav-1" aria-haspopup="true">
              Innovation &amp; AI
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            

<div class="uni-nav-desktop uni-page--fullbleed" id="desktop-nav-1" role="region" aria-label="Innovation &amp; AI submenu" aria-hidden="true">
  <div class="uni-page">
    <div class="uni-nav-desktop__container uni-grid">
      <div class="uni-nav-desktop__header">
        <h3 class="uni-nav-desktop__title font-h3">Innovation &amp; AI</h3>
        
        
          <uni-cta class="uni-nav-desktop__see-all-cta" href="/innovation-and-ai/" emphasis="medium" icon-id-right="arrow-forward" additional-class="uni-nav-link--subitem-cta">
            
              See all in Innovation &amp; AI
            
          </uni-cta>
        
      </div>

      <div class="uni-nav-desktop__content">
        <ul class="uni-nav-desktop__list">
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-innovation-ai-1">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-innovation-ai-1">Models &amp; Research</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/models-and-research/google-deepmind/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Google DeepMind 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/models-and-research/google-research/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Google Research 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/models-and-research/google-labs/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Google Labs 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/models-and-research/gemini-models/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Gemini models 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/models-and-research/quantum-computing/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Quantum computing 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/innovation-and-ai/models-and-research/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Models &amp; Research articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-innovation-ai-2">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-innovation-ai-2">Products</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/technology/developers-tools/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Developer tools 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/products/gemini-app/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Gemini app 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/products/gemini-notebook/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Gemini Notebook 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/innovation-and-ai/products/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Products articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-innovation-ai-3">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-innovation-ai-3">Infrastructure &amp; cloud</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/infrastructure-and-cloud/global-network/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Global network 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/infrastructure-and-cloud/google-cloud/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Google Cloud 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/innovation-and-ai/infrastructure-and-cloud/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Infrastructure &amp; cloud articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-innovation-ai-4">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-innovation-ai-4">Technology</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/technology/safety-security/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Safety &amp; Security 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/technology/health/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Health 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/innovation-and-ai/technology/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Technology articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
        </ul>
      </div>

      
        <div class="uni-nav-desktop__footer">
          
            <p class="font-h6 uni-nav-desktop__list-title--learn-more uni-nav-mobile__section-title--small">
              Learn more:
            </p>
            <div class="uni-nav-desktop__learn-more-links">
              
                <a href="https://deepmind.google/blog/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
                  <span>Google DeepMind blog</span>
                  <span class="uni-nav-link--learn-more-icon">
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>

                  </span>
                </a>
              
                <a href="https://research.google/blog/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
                  <span>Google Research blog</span>
                  <span class="uni-nav-link--learn-more-icon">
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>

                  </span>
                </a>
              
                <a href="https://developers.googleblog.com/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
                  <span>Google Developers blog</span>
                  <span class="uni-nav-link--learn-more-icon">
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>

                  </span>
                </a>
              
                <a href="https://cloud.google.com/blog" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
                  <span>Google Cloud blog</span>
                  <span class="uni-nav-link--learn-more-icon">
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>

                  </span>
                </a>
              
            </div>
          
        </div>
      
    </div>
  </div>
  
    <div class="uni-nav-desktop__shape-container">
      <div class="uni-nav-desktop__shape uni-nav-desktop__shape--4-sided-cookie" data-shape="4-sided-cookie"></div>
    </div>
  
</div>

          
          </li>
        
          <li class="uni-nav__item">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--desktop uni-nav-link--dropdown font-body-s" aria-expanded="false" aria-controls="desktop-nav-2" aria-haspopup="true">
              Products &amp; platforms
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            

<div class="uni-nav-desktop uni-page--fullbleed" id="desktop-nav-2" role="region" aria-label="Products &amp; platforms submenu" aria-hidden="true">
  <div class="uni-page">
    <div class="uni-nav-desktop__container uni-grid">
      <div class="uni-nav-desktop__header">
        <h3 class="uni-nav-desktop__title font-h3">Products &amp; platforms</h3>
        
        
          <uni-cta class="uni-nav-desktop__see-all-cta" href="/products-and-platforms/" emphasis="medium" icon-id-right="arrow-forward" additional-class="uni-nav-link--subitem-cta">
            
              See all in Products &amp; platforms
            
          </uni-cta>
        
      </div>

      <div class="uni-nav-desktop__content">
        <ul class="uni-nav-desktop__list">
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-products-platforms-1">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-products-platforms-1">Products</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/products/search/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Search 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/products/maps/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Maps 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/products/chrome/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Chrome 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/products/google-health/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Google Health 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/products/workspace/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Google Workspace 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/products/education/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Learning &amp; Education 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/products/shopping/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Shopping 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/products-and-platforms/products/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Products articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-products-platforms-2">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-products-platforms-2">Platforms</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/platforms/android/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Android 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/platforms/google-play/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Google Play 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/platforms/wear-os/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Wear OS 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/products-and-platforms/platforms/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Platforms articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-products-platforms-3">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-products-platforms-3">Devices</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/devices/pixel/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Pixel 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/devices/google-nest/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Google Nest 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/devices/fitbit/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Fitbit 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/devices/chromebooks/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Chromebook 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/products-and-platforms/devices/googlebook/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Googlebook 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/products-and-platforms/devices/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Devices articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
        </ul>
      </div>

      
        <div class="uni-nav-desktop__footer">
          
            <p class="font-h6 uni-nav-desktop__list-title--learn-more uni-nav-mobile__section-title--small">
              Learn more:
            </p>
            <div class="uni-nav-desktop__learn-more-links">
              
                <a href="https://blog.google/products/ads-commerce/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
                  <span>Google Ads &amp; Commerce blog</span>
                  <span class="uni-nav-link--learn-more-icon">
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>

                  </span>
                </a>
              
                <a href="https://blog.google/waze/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
                  <span>Waze blog</span>
                  <span class="uni-nav-link--learn-more-icon">
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>

                  </span>
                </a>
              
            </div>
          
        </div>
      
    </div>
  </div>
  
    <div class="uni-nav-desktop__shape-container">
      <div class="uni-nav-desktop__shape uni-nav-desktop__shape--8-leaf-clover" data-shape="8-leaf-clover"></div>
    </div>
  
</div>

          
          </li>
        
          <li class="uni-nav__item">
          
            <button class="uni-nav-link uni-nav-link--expand uni-nav-link--desktop uni-nav-link--dropdown font-body-s" aria-expanded="false" aria-controls="desktop-nav-3" aria-haspopup="true">
              Company news
              <svg
  
  
  
  
  
  
  role="presentation"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

            </button>
            

<div class="uni-nav-desktop uni-page--fullbleed" id="desktop-nav-3" role="region" aria-label="Company news submenu" aria-hidden="true">
  <div class="uni-page">
    <div class="uni-nav-desktop__container uni-grid">
      <div class="uni-nav-desktop__header">
        <h3 class="uni-nav-desktop__title font-h3">Company news</h3>
        
        
          <uni-cta class="uni-nav-desktop__see-all-cta" href="/company-news/" emphasis="medium" icon-id-right="arrow-forward" additional-class="uni-nav-link--subitem-cta">
            
              See all in Company news
            
          </uni-cta>
        
      </div>

      <div class="uni-nav-desktop__content">
        <ul class="uni-nav-desktop__list">
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-company-news-1">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-company-news-1">Outreach &amp; initiatives</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/company-news/outreach-and-initiatives/creating-opportunity/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Creating opportunity 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/technology/safety-security/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Safety &amp; security 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/company-news/outreach-and-initiatives/google-org/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Google.org 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/company-news/outreach-and-initiatives/public-policy/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Public policy 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/company-news/outreach-and-initiatives/sustainability/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Sustainability 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/innovation-and-ai/technology/health/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Health 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/company-news/outreach-and-initiatives/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Outreach &amp; initiatives articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-company-news-2">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-company-news-2">Leadership</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/authors/sundar-pichai/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Sundar Pichai, CEO 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/authors/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          More authors 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/authors/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Leadership articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="uni-nav-desktop__item" role="group" aria-labelledby="desktop-nav-group-company-news-3">
              <p class="font-h6 uni-nav-desktop__list-title uni-nav-mobile__section-title--small" id="desktop-nav-group-company-news-3">Inside Google</p>

              
                <ul class="uni-nav-desktop__sublist">
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/company-news/inside-google/around-the-globe/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Around the globe 
                        </a>
                      
                    </li>
                  
                    <li class="uni-nav-desktop__subitem">
                      
                        
                        <a href="/company-news/inside-google/life-at-google/" class="uni-nav-link uni-nav-link--sublist uni-nav-link--full-width font-body-xl">
                          Life at Google 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/company-news/inside-google/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Inside Google articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow-forward"></use>
</svg>
</a>
                    </li>
                  
                </ul>
              
            </li>
          
        </ul>
      </div>

      
        <div class="uni-nav-desktop__footer">
          
            <p class="font-h6 uni-nav-desktop__list-title--learn-more uni-nav-mobile__section-title--small">
              Learn more:
            </p>
            <div class="uni-nav-desktop__learn-more-links">
              
                <a href="https://blog.google/security/" class="uni-nav-link uni-nav-link--learn-more font-body-xl">
                  <span>Google Security blog</span>
                  <span class="uni-nav-link--learn-more-icon">
                    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#arrow_outward"></use>
</svg>

                  </span>
                </a>
              
            </div>
          
        </div>
      
    </div>
  </div>
  
    <div class="uni-nav-desktop__shape-container">
      <div class="uni-nav-desktop__shape uni-nav-desktop__shape--4-leaf-clover" data-shape="4-leaf-clover"></div>
    </div>
  
</div>

          
          </li>
        
          <li class="uni-nav__item">
          
            <a href="/feed" class="uni-nav-link uni-nav-link--desktop font-body-s">
              Feed
            </a>
          
          </li>
        
        </ul>
      </div>

      
        


<div class="uni-article-progress-bar slide-up" data-component="uni-progress-bar" role="none">
  <div class="uni-article-progress-bar__title uni-article-progress-bar__ellipsis">Gemini 3.8 text-to-speech says hello</div>
  <div class="uni-article-progress-bar__social"
    data-analytics-module='{
      "module_name": "Progress Bar",
      "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
    }'
  >
    


<div class ="uni-social-share " data-component="uni-social-share-dropdown">
  <a class="uni-social-share__trigger" role="button" tabindex="0" aria-label="Share" aria-expanded="false">
    
    <svg
  
  class="h-c-icon h-c-icon--color-text"
  
  
  
  
  
  aria-hidden="true"
  title="Share"
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-share"></use>
</svg>

    <div class="uni-social-share__button">Share</div>
  </a>
  <div class="uni-social-share__dialog uni-social-share__content " aria-labelledby="social-share-icon">
    


<a aria-label="Share on X"
    class="article-share__link-text uni-click-tracker"
    href="https://twitter.com/intent/tweet?text=Gemini%203.8%20text-to-speech%20says%20hello%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
    target="_blank"
    data-ga4-method="twitter">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-x"></use>
</svg>

  <div class="article-share__title">x.com</div>
</a>

<a aria-label="Share on Facebook"
    class="article-share__link-text uni-click-tracker"
    href="https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.8%20text-to-speech%20says%20hello&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
    target="_blank"
    data-ga4-method="facebook">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-facebook"></use>
</svg>

  <div class="article-share__title">Facebook</div>
</a>

<a aria-label="Share on LinkedIn"
    class="article-share__link-text uni-click-tracker"
    href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/&title=Gemini%203.8%20text-to-speech%20says%20hello"
    target="_blank"
    data-ga4-method="linkedin">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-linkedin"></use>
</svg>

  <div class="article-share__title">LinkedIn</div>
</a>

<a aria-label="Share with Email"
    class="article-share__link-text uni-click-tracker article-share__email"
    
      href="mailto:?subject=Gemini%203.8%20text-to-speech%20says%20hello&body=Check out this article on the Keyword:%0A%0AGemini%203.8%20text-to-speech%20says%20hello%0A%0AGemini 3.8 Flash-Lite TTS and Gemini 3.8 Flash TTS are our most expressive audio models yet.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
    
    target="_blank"
    data-ga4-method="email">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-mail"></use>
</svg>

  <div class="article-share__title">Mail</div>
</a>

    


<div class="copy-link uni-copy-share uni-click-tracker"
  data-component="uni-copy-popup-component"
  data-ga4-analytics-share-copy-link
  data-ga4-method="Copy link">
  
  <button class="copy-link__trigger copy-link__trigger-text"
    data-ga4-method="Copy link"
    title="Copy link">
    <svg
  
  class="h-c-icon h-c-icon--color-text"
  
  
  
  
  role="presentation"
  
  title="Copy link"
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-link"></use>
</svg>

    <div class="copy-link__title">Copy link</div>
  </button>
  <div class="copy-link__dialog copy-link__content" uni-options='{"copyTextButton": "Copied"}' aria-hidden="true" tabindex="-1">
    <input class="h-c-copy copy-link__url" value="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/" id="copy-link" readonly="readonly" type="text"/>
    <div class="copy-link__copy-message" role="status"></div>
  </div>
</div>

  </div>
</div>

  </div>
  <div class="uni-article-progress-bar__indicator hide-progress-bar"></div>
</div>

      

      <div class="uni-nav__actions">
        
























<uni-search-bar
  class="uni-search-bar"
  search-placeholder=""
  onboarding-text=""
  
  >
  <div slot="suggested-searches-slot">
    []
  </div>
</uni-search-bar>

        


<div class="uni-nav__item">
  <button
    type="button"
    class="uni-nav__action-btn uni-nav__action-btn--kebab uni-nav-link--dropdown"
    title='Secondary menu'
    aria-expanded="false"
    aria-haspopup="menu"
    aria-controls="header-kebab-dropdown"
    aria-label="Secondary menu"
    data-analytics-module='{
      "module_name": "main nav",
      "section_header": "Secondary menu"
    }'>
    <!-- Kebab Icon (3 vertical dots) -->
    <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-more-vert"></use>
</svg>

  </button>

  <!-- Kebab Dropdown Menu -->
  <div id="header-kebab-dropdown" class="uni-nav__dropdown-menu" aria-hidden="true"
    data-analytics-module='{
      "module_name": "main nav",
      "section_header": "Secondary menu"
    }'>
    <div class="uni-nav__dropdown-menu-inner">
      <span class="font-body-xs">Preferences</span>
      <ul class="uni-nav__dropdown-menu-link-list">
        <li>
          <div class="uni-nav__dropdown-menu-link uni-nav__dropdown-menu-link--select font-ctas" data-component="uni-lang-picker">
            <svg
  
  class="uni-lang-picker__world-icon"
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#language"></use>
</svg>

            


  <div data-component="uni-lang-picker" class="uni-lang-picker">
    <select
      name="language-picker"
      class="uni-lang-picker__select font-ctas uni-lang-picker--inside-menu"
      aria-label="Change Region">
      
      <option
        label="Global (English)"
        value="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
        lang="en-us"
        class="uni-lang-picker__option"
        
          selected="selected"
          data-selected-index="0"
        >
        Global (English)
      </option>
      
      <option
        label="Africa (English)"
        value="https://blog.google/intl/en-africa/"
        lang="en-africa"
        class="uni-lang-picker__option"
        >
        Africa (English)
      </option>
      
      <option
        label="Australia (English)"
        value="https://blog.google/intl/en-au/"
        lang="en-au"
        class="uni-lang-picker__option"
        >
        Australia (English)
      </option>
      
      <option
        label="Brasil (Português)"
        value="https://blog.google/intl/pt-br/"
        lang="pt-br"
        class="uni-lang-picker__option"
        >
        Brasil (Português)
      </option>
      
      <option
        label="Canada (English)"
        value="https://blog.google/intl/en-ca/"
        lang="en-ca"
        class="uni-lang-picker__option"
        >
        Canada (English)
      </option>
      
      <option
        label="Canada (Français)"
        value="https://blog.google/intl/fr-ca/"
        lang="fr-ca"
        class="uni-lang-picker__option"
        >
        Canada (Français)
      </option>
      
      <option
        label="Česko (Čeština)"
        value="https://blog.google/intl/cs-cz/"
        lang="cs-cz"
        class="uni-lang-picker__option"
        >
        Česko (Čeština)
      </option>
      
      <option
        label="Deutschland (Deutsch)"
        value="https://blog.google/intl/de-de/"
        lang="de-de"
        class="uni-lang-picker__option"
        >
        Deutschland (Deutsch)
      </option>
      
      <option
        label="España (Español)"
        value="https://blog.google/intl/es-es/"
        lang="es-es"
        class="uni-lang-picker__option"
        >
        España (Español)
      </option>
      
      <option
        label="France (Français)"
        value="https://blog.google/intl/fr-fr/"
        lang="fr-fr"
        class="uni-lang-picker__option"
        >
        France (Français)
      </option>
      
      <option
        label="Greece (Ελληνικά)"
        value="https://blog.google/intl/el-gr/"
        lang="el-gr"
        class="uni-lang-picker__option"
        >
        Greece (Ελληνικά)
      </option>
      
      <option
        label="India (English)"
        value="https://blog.google/intl/en-in/"
        lang="en-in"
        class="uni-lang-picker__option"
        >
        India (English)
      </option>
      
      <option
        label="Indonesia (Bahasa Indonesia)"
        value="https://blog.google/intl/id-id/"
        lang="id-id"
        class="uni-lang-picker__option"
        >
        Indonesia (Bahasa Indonesia)
      </option>
      
      <option
        label="Ireland (English)"
        value="https://blog.google/intl/en-ie/"
        lang="en-ie"
        class="uni-lang-picker__option"
        >
        Ireland (English)
      </option>
      
      <option
        label="Italia (Italiano)"
        value="https://blog.google/intl/it-it/"
        lang="it-it"
        class="uni-lang-picker__option"
        >
        Italia (Italiano)
      </option>
      
      <option
        label="日本 (日本語)"
        value="https://blog.google/intl/ja-jp/"
        lang="ja-jp"
        class="uni-lang-picker__option"
        >
        日本 (日本語)
      </option>
      
      <option
        label="대한민국 (한국어)"
        value="https://blog.google/intl/ko-kr/"
        lang="ko-kr"
        class="uni-lang-picker__option"
        >
        대한민국 (한국어)
      </option>
      
      <option
        label="Latinoamérica (Español)"
        value="https://blog.google/intl/es-419/"
        lang="es-419"
        class="uni-lang-picker__option"
        >
        Latinoamérica (Español)
      </option>
      
      <option
        label="Malaysia (English)"
        value="https://blog.google/intl/en-my/"
        lang="en-my"
        class="uni-lang-picker__option"
        >
        Malaysia (English)
      </option>
      
      <option
        label="الشرق الأوسط وشمال أفريقيا (اللغة العربية)"
        value="https://blog.google/intl/ar-mena/"
        lang="ar-mena"
        class="uni-lang-picker__option"
        >
        الشرق الأوسط وشمال أفريقيا (اللغة العربية)
      </option>
      
      <option
        label="MENA (English)"
        value="https://blog.google/intl/en-mena/"
        lang="en-mena"
        class="uni-lang-picker__option"
        >
        MENA (English)
      </option>
      
      <option
        label="Nederlands (Nederland)"
        value="https://blog.google/intl/nl-nl/"
        lang="nl-nl"
        class="uni-lang-picker__option"
        >
        Nederlands (Nederland)
      </option>
      
      <option
        label="New Zealand (English)"
        value="https://blog.google/intl/en-nz/"
        lang="en-nz"
        class="uni-lang-picker__option"
        >
        New Zealand (English)
      </option>
      
      <option
        label="Polska (Polski)"
        value="https://blog.google/intl/pl-pl/"
        lang="pl-pl"
        class="uni-lang-picker__option"
        >
        Polska (Polski)
      </option>
      
      <option
        label="Portugal (Português)"
        value="https://blog.google/intl/pt-pt/"
        lang="pt-pt"
        class="uni-lang-picker__option"
        >
        Portugal (Português)
      </option>
      
      <option
        label="România (Română)"
        value="https://blog.google/intl/ro-ro/"
        lang="ro-ro"
        class="uni-lang-picker__option"
        >
        România (Română)
      </option>
      
      <option
        label="Sverige (Svenska)"
        value="https://blog.google/intl/sv-se/"
        lang="sv-se"
        class="uni-lang-picker__option"
        >
        Sverige (Svenska)
      </option>
      
      <option
        label="ประเทศไทย (ไทย)"
        value="https://blog.google/intl/th-th/"
        lang="th-th"
        class="uni-lang-picker__option"
        >
        ประเทศไทย (ไทย)
      </option>
      
      <option
        label="Türkiye (Türkçe)"
        value="https://blog.google/intl/tr-tr/"
        lang="tr-tr"
        class="uni-lang-picker__option"
        >
        Türkiye (Türkçe)
      </option>
      
      <option
        label="台灣 (中文)"
        value="https://blog.google/intl/zh-tw/"
        lang="zh-tw"
        class="uni-lang-picker__option"
        >
        台灣 (中文)
      </option>
      
    </select>
    <span class="uni-lang-picker__chevron">
      <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#expand_more"></use>
</svg>

    </span>
  </div>

          </div>
        </li>
      </ul>
      <span class="font-body-xs">Links</span>
      <ul class="uni-nav__dropdown-menu-link-list">
        <li>
          
            <a class="uni-nav__dropdown-menu-link font-ctas" href="/image-library/"
              title="Images"><svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#photo-library"></use>
</svg>
Images</a>
          
        </li>
        <li>
          <a
            href="/rss/"
            class="uni-nav__dropdown-menu-link font-ctas">
              <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#rss-feed"></use>
</svg>
RSS feed</a>
        </li>
      </ul>
    </div>
  </div>

  <!-- Share Dropdown Menu -->
  
  <div class="uni-share-dropdown" data-component="uni-share-dropdown" data-analytics-module='{
         "module_name": "Progress Bar",
         "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
       }'>
    <button
      aria-label="Share"
      aria-expanded="false"
      aria-haspopup="menu"
      aria-controls="header-share-dropdown"
      data-ga4-analytics-share-dropdown-click
      class="uni-share-dropdown__trigger uni-nav__action-btn uni-nav__action-btn--share">
      <!-- Share Icon -->
      <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#share"></use>
</svg>

    </button>
    <div id="header-share-dropdown" class="uni-share-dropdown__menu " aria-hidden="true">
  <div class="uni-share-dropdown__menu-inner">
    <ul class="uni-share-dropdown__menu-link-list uni-social-share">
      


<li>
  <a aria-label="Share on X"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://twitter.com/intent/tweet?text=Gemini%203.8%20text-to-speech%20says%20hello%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
      target="_blank"
      data-ga4-method="twitter">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-x"></use>
</svg>

    <span>x.com</span>
  </a>
</li>

<li>
  <a aria-label="Share on Facebook"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.8%20text-to-speech%20says%20hello&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
      target="_blank"
      data-ga4-method="facebook">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-facebook"></use>
</svg>

    <span>Facebook</span>
  </a>
</li>

<li>
  <a aria-label="Share on LinkedIn"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/&title=Gemini%203.8%20text-to-speech%20says%20hello"
      target="_blank"
      data-ga4-method="linkedin">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-linkedin"></use>
</svg>

    <span>LinkedIn</span>
  </a>
</li>

<li>
  <a aria-label="Share with Email"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      
        href="mailto:?subject=Gemini%203.8%20text-to-speech%20says%20hello&body=Check out this article on the Keyword:%0A%0AGemini%203.8%20text-to-speech%20says%20hello%0A%0AGemini 3.8 Flash-Lite TTS and Gemini 3.8 Flash TTS are our most expressive audio models yet.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
      
      target="_blank"
      data-ga4-method="email">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-mail"></use>
</svg>

    <span>Mail</span>
  </a>
</li>

<li data-component="uni-copy-popup-component">
  <button aria-label="Copy link"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker uni-copy-share"
      data-ga4-analytics-share-copy-link
      data-ga4-method="Copy link"
      data-copy-text="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-link"></use>
</svg>

    <span>Copy link</span>
  </button>
  <div class="uni-share-dropdown__copy-toast" uni-options='{"copyTextButton": "Copied"}' aria-hidden="true" tabindex="-1">
    <span class="uni-share-dropdown__copy-toast-message font-body-xs" role="status"></span>
  </div>
</li>

    </ul>
  </div>
</div>

  </div>
  
</div>

        
          
            
            <uni-cta class="uni-nav__subscribe" emphasis="high"><span>Newsletter</span></uni-cta>
          
        
      </div>
    </nav>
  </div>
  
    <div class="uni-nav__progress-bar" role="progressbar" aria-valuemin="0" aria-valuemax="100"></div>
  
</header>

        

        <main id="jump-content" class="site-content" tabindex="-1">
            
    
    

    <article class="uni-article-wrapper">

    









<section class="uni-article-hero uni-article-hero--blue"
  data-analytics-module='{
    "module_name": "Hero Menu",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>

  <div class="uni-page--fullbleed uni-article-hero__container">
    
    <div class="uni-page">
      <div class="uni-grid uni-article-hero__header">
        
          <div class="uni-grid__col--span-4 uni-grid__col--span-12-tablet uni-grid__col--start-3-desktop uni-grid__col--span-8-desktop uni-article-hero__breadcrumb">
            


    









  <uni-breadcrumbs class="uni-breadcrumb__container uni-grid__col--span-4 uni-grid__col--span-8-tablet uni-grid__col--start-3-tablet">
    <button class="uni-breadcrumb__prev-btn hide" aria-label="Previous">
      <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#uni-icon-chevron-right"></use>
</svg>

    </button>
    <div class="uni-breadcrumb__focusable uni-breadcrumb__focusable--start"></div>
    <nav aria-label="Breadcrumb" class="breadcrumb uni-breadcrumb__scrollable">
      <span class="uni-breadcrumb__label">Breadcrumb</span>
      <ol data-analytics-module='{
        "module_name": "breadcrumbs",
        "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
      }'>
      
        <li>
        
          <a href="https://blog.google/"
            class="uni-breadcrumb__button uni-breadcrumb__button--homepage font-body-s"
            title="News from Google"
            aria-label="News from Google"
            

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "News from Google"
}'
>
            Home
          </a>
        
        </li>
      
        <li>
        
        <svg
  
  class="uni-breadcrumb__chevron"
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#uni-icon-chevron-right"></use>
</svg>

          
            <a href="https://blog.google/innovation-and-ai/"
              class="uni-breadcrumb__button font-body-s"
              

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "Innovation \u0026 AI"
}'
>
                Innovation &amp; AI
            </a>
          
        
        </li>
      
        <li>
        
        <svg
  
  class="uni-breadcrumb__chevron"
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#uni-icon-chevron-right"></use>
</svg>

          
            <a href="https://blog.google/innovation-and-ai/models-and-research/"
              class="uni-breadcrumb__button font-body-s"
              

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "Models \u0026 research"
}'
>
                Models &amp; research
            </a>
          
        
        </li>
      
        <li>
        
        <svg
  
  class="uni-breadcrumb__chevron"
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#uni-icon-chevron-right"></use>
</svg>

          
            <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/"
              class="uni-breadcrumb__button font-body-s"
              

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "Gemini Models"
}'
>
                Gemini Models
            </a>
          
        
        </li>
      
      
      
      </ol>
    </nav>
    <div class="uni-breadcrumb__focusable uni-breadcrumb__focusable--end"></div>
    <button class="uni-breadcrumb__next-btn hide" aria-label="Next">
      <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#uni-icon-chevron-right"></use>
</svg>

    </button>
  </uni-breadcrumbs>


          </div>
        
      </div>
      
      <div class="uni-grid uni-article-hero__content-grid">
        <div class="uni-grid__col--span-4 uni-grid__col--span-12-tablet uni-grid__col--span-8-desktop uni-grid__col--start-3-desktop uni-article-hero__main-content">
          <h1 class="uni-article-hero__title font-h1">Gemini 3.8 text-to-speech says hello</h1>

          <div class="uni-article-hero__meta-wrapper">
            <div class="uni-article-hero__meta-header">
              
              <div class="uni-article-hero__meta-aside">
                
                  <p class="uni-article-hero__date font-body-s">Sep 23, 2026</p>
                
                
                  <span class="uni-article-hero__meta-aside-divider font-body-s">|</span>
                
                
                  <uni-reading-time class="uni-article-hero__reading-time font-body-s"></uni-reading-time>
                
              </div>
              <!-- Share Dropdown Menu -->
              <div class="uni-share-dropdown uni-article-hero__meta-aside-share" data-component="uni-share-dropdown">
                <uni-cta
                  emphasis="low"
                  aria-label="Share"
                  aria-expanded="false"
                  aria-haspopup="menu"
                  aria-controls="article-hero-share-dropdown-1"
                  icon-id-right="share"
                  data-ga4-analytics-share-dropdown-click
                  class="uni-share-dropdown__trigger">
                </uni-cta>
                <div id="article-hero-share-dropdown-1" class="uni-share-dropdown__menu " aria-hidden="true">
  <div class="uni-share-dropdown__menu-inner">
    <ul class="uni-share-dropdown__menu-link-list uni-social-share">
      


<li>
  <a aria-label="Share on X"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://twitter.com/intent/tweet?text=Gemini%203.8%20text-to-speech%20says%20hello%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
      target="_blank"
      data-ga4-method="twitter">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-x"></use>
</svg>

    <span>x.com</span>
  </a>
</li>

<li>
  <a aria-label="Share on Facebook"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.8%20text-to-speech%20says%20hello&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
      target="_blank"
      data-ga4-method="facebook">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-facebook"></use>
</svg>

    <span>Facebook</span>
  </a>
</li>

<li>
  <a aria-label="Share on LinkedIn"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/&title=Gemini%203.8%20text-to-speech%20says%20hello"
      target="_blank"
      data-ga4-method="linkedin">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-linkedin"></use>
</svg>

    <span>LinkedIn</span>
  </a>
</li>

<li>
  <a aria-label="Share with Email"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      
        href="mailto:?subject=Gemini%203.8%20text-to-speech%20says%20hello&body=Check out this article on the Keyword:%0A%0AGemini%203.8%20text-to-speech%20says%20hello%0A%0AGemini 3.8 Flash-Lite TTS and Gemini 3.8 Flash TTS are our most expressive audio models yet.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
      
      target="_blank"
      data-ga4-method="email">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-mail"></use>
</svg>

    <span>Mail</span>
  </a>
</li>

<li data-component="uni-copy-popup-component">
  <button aria-label="Copy link"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker uni-copy-share"
      data-ga4-analytics-share-copy-link
      data-ga4-method="Copy link"
      data-copy-text="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-link"></use>
</svg>

    <span>Copy link</span>
  </button>
  <div class="uni-share-dropdown__copy-toast" uni-options='{"copyTextButton": "Copied"}' aria-hidden="true" tabindex="-1">
    <span class="uni-share-dropdown__copy-toast-message font-body-xs" role="status"></span>
  </div>
</li>

    </ul>
  </div>
</div>

              </div>
            </div>


            
            
              <p class="uni-article-hero__abstract font-body-xl">
                Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS are our most expressive audio generation models yet. Generate custom character voices and direct scene dialogue across Google AI Studio, Gemini API, Gemini Enterprise, Gemini Notebook, and Google Vids.
              </p>
            
          </div>

          <hr class="uni-article-hero__divider">

          
          <div class="uni-article-hero__authors-actions">
            <div class="uni-article-hero__authors-wrapper">
              
                

<div class="uni-article-hero__authors uni-grid">
  
    
    <div class="uni-article-hero__author">
      <div class="uni-article-hero__author-info">
        
            <p class="uni-article-hero__author-name font-author-name">Leland Rechis</p>
            
              
                <p class="uni-article-hero__author-title font-author-info">Group Product Manager</p>
              
            
        
      </div>
    </div>
  
    
    <div class="uni-article-hero__author">
      <div class="uni-article-hero__author-info">
        
            <p class="uni-article-hero__author-name font-author-name">Alan Cowen</p>
            
              
                <p class="uni-article-hero__author-title font-author-info">Director, Research Science, on Behalf of the Gemini Audio Team</p>
              
            
        
      </div>
    </div>
  
</div>

              
            </div>

            <div class="uni-article-hero__actions-wrapper">
              <!-- Share Dropdown Menu -->
              <div class="uni-share-dropdown uni-article-hero__actions-share" data-component="uni-share-dropdown">
                <uni-cta
                  emphasis="low"
                  aria-label="Share"
                  aria-expanded="false"
                  aria-haspopup="menu"
                  aria-controls="article-hero-share-dropdown-2"
                  icon-id-left="share"
                  data-ga4-analytics-share-dropdown-click
                  class="uni-share-dropdown__trigger">
                  Share
                </uni-cta>
                <div id="article-hero-share-dropdown-2" class="uni-share-dropdown__menu " aria-hidden="true">
  <div class="uni-share-dropdown__menu-inner">
    <ul class="uni-share-dropdown__menu-link-list uni-social-share">
      


<li>
  <a aria-label="Share on X"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://twitter.com/intent/tweet?text=Gemini%203.8%20text-to-speech%20says%20hello%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
      target="_blank"
      data-ga4-method="twitter">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-x"></use>
</svg>

    <span>x.com</span>
  </a>
</li>

<li>
  <a aria-label="Share on Facebook"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.8%20text-to-speech%20says%20hello&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
      target="_blank"
      data-ga4-method="facebook">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-facebook"></use>
</svg>

    <span>Facebook</span>
  </a>
</li>

<li>
  <a aria-label="Share on LinkedIn"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/&title=Gemini%203.8%20text-to-speech%20says%20hello"
      target="_blank"
      data-ga4-method="linkedin">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-linkedin"></use>
</svg>

    <span>LinkedIn</span>
  </a>
</li>

<li>
  <a aria-label="Share with Email"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      
        href="mailto:?subject=Gemini%203.8%20text-to-speech%20says%20hello&body=Check out this article on the Keyword:%0A%0AGemini%203.8%20text-to-speech%20says%20hello%0A%0AGemini 3.8 Flash-Lite TTS and Gemini 3.8 Flash TTS are our most expressive audio models yet.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
      
      target="_blank"
      data-ga4-method="email">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-mail"></use>
</svg>

    <span>Mail</span>
  </a>
</li>

<li data-component="uni-copy-popup-component">
  <button aria-label="Copy link"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker uni-copy-share"
      data-ga4-analytics-share-copy-link
      data-ga4-method="Copy link"
      data-copy-text="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#social-link"></use>
</svg>

    <span>Copy link</span>
  </button>
  <div class="uni-share-dropdown__copy-toast" uni-options='{"copyTextButton": "Copied"}' aria-hidden="true" tabindex="-1">
    <span class="uni-share-dropdown__copy-toast-message font-body-xs" role="status"></span>
  </div>
</li>

    </ul>
  </div>
</div>

              </div>
            </div>
          </div>
          <hr class="uni-article-hero__divider">
        </div>
      </div>
    </div>

    
    <div class="uni-article-hero__media-slot">
      
        










  
    <div class="uni-article-hero__image-container">
      <div class="uni-article-hero__aspect-ratio">
        <div class="uni-article-hero__image-wrapper">
          <img
            alt="a text card image reading &quot;Introducing Gemini 3.8 Flash TTS and 3.8 Flash-Lite TTS&quot;"
            class="uni-article-hero__image uni-progressive-image--blur"
            data-component="uni-progressive-image"
            fetchpriority="high"
            src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__keyword__metacard__.width-200.format-webp.webp"
            
              data-sizes="(max-width: 1023px) 100vw, (max-width: 1440px) 95vw, 1408px"
              data-srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__keyword__metacard__.width-450.format-webp.webp 450w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__keyword__metacard__.width-900.format-webp.webp 900w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__keyword__metacard_.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__keyword__metacard_.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__keyword__metacard_.width-2200.format-webp.webp 2200w"
            
            >
        </div>
      </div>
      
    </div>
  





      
    </div>
  </div>
</section>

    <div class="uni-page uni-grid article-container__ai-box-container">
      <div class="article-container__ai-box uni-grid__col--layout-6">
        
        
          
            


<div class="uni-ai-summary "
  data-component="uni-ai-generated-summary"
  data-analytics-module='{
    "event": "module_impression",
    "module_name": "ai_summary",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
>
  <div class="uni-ai-summary__btn-container">
    <button class="uni-ai-summary__btn font-ctas" aria-expanded="false" aria-controls="uni-ai-summary-dropdown">
      <span class="uni-ai-summary__icon-wrapper">
        <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#summarize-gd"></use>
</svg>

      </span>
      <span class="uni-ai-summary__btn-text font-ctas">
        Read AI-generated summary
        <span class="uni-ai-summary__icon-wrapper uni-ai-summary__icon-wrapper--chevron">
          <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#mi-expand"></use>
</svg>

        </span>
      </span>
    </button>

    <div id="uni-ai-summary-dropdown" class="uni-ai-summary__dropdown" aria-hidden="true">
      <div class="uni-ai-summary__dropdown-inner">
        
          <div class="uni-ai-summary__summary active" data-summary-id="ai_summary_2">
            <div class="uni-ai-summary__copy font-h6">
              <ul>
<li>Check out "Gemini 3.8 text-to-speech says hello" to see how our new models work.</li>
<li>Create custom voices from scratch or replicate existing ones with simple natural language prompts.</li>
<li>Direct your audio line-by-line to control pacing, emotion, and even realistic conversational sounds.</li>
<li>Use these models for high-quality audiobooks, podcasts, or real-time voice agents at scale.</li>
<li>We’ve included built-in safety tools like watermarking to keep your generated audio secure.</li>
</ul>
            </div>
            <small class="uni-ai-summary__legal font-body-xs">
              Summaries were generated by Google AI. Generative AI is experimental.
            </small>
          </div>
        
          <div class="uni-ai-summary__summary " data-summary-id="ai_summary_3">
            <div class="uni-ai-summary__copy font-h6">
              <p>Google just launched new AI tools that let you create and customize realistic voices from scratch. You can direct these voices to sound exactly how you want, from their accent to their emotional tone. It’s perfect for making audiobooks, games, or podcasts that sound like real people talking. Plus, they added safety features to make sure these voices are used responsibly.</p>
            </div>
            <small class="uni-ai-summary__legal font-body-xs">
              Summaries were generated by Google AI. Generative AI is experimental.
            </small>
          </div>
        

        
        <div class="uni-ai-summary__explore">
          <h4 class="uni-ai-summary__explore-title font-h6">
            Explore other styles:
          </h4>
          <ul class="uni-ai-summary__chips">
            
            <li>
              <button class="uni-ai-summary__chip-btn font-body-s" aria-label="Bullet points" data-summary-id="ai_summary_2" aria-pressed="true">
                
                  <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#format_list_bulleted"></use>
</svg>

                
                <span class="uni-ai-summary__chip-text" aria-hidden="true">
                  Bullet points
                </span>
              </button>
            </li>
            
            <li>
              <button class="uni-ai-summary__chip-btn font-body-s" aria-label="Basic explainer" data-summary-id="ai_summary_3" >
                
                  <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#text_snippet"></use>
</svg>

                
                <span class="uni-ai-summary__chip-text" aria-hidden="true">
                  Basic explainer
                </span>
              </button>
            </li>
            
          </ul>
        </div>
        
      </div>
    </div>
  </div>
</div>

          
        
      </div>
    </div>
    
    <section class="uni-container article-container">
      
        
        
        <div class="uni-content uni-blog-article-container article-container__content"
            data-reading-time="true"
            data-component="uni-article-body">

          
          
<!--article text-->

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="sl809">Today, we’re introducing two new text-to-speech models to the Gemini family, transforming voice generation from static presets into a dynamic creative studio. These models enable creators, developers, and enterprises to create richer, more expressive audio experiences, while enabling improved user experiences in products like <a href="https://notebook.google.com/">Gemini Notebook</a> and<a href="http://vids.new/"> Google Vids</a>.</p><ul><li data-block-key="9eru5"><b>Gemini 3.8 Flash TTS:</b> Built for deep creative direction and character design. Create entirely new voices from scratch using natural language prompts to bring characters to life across gaming, immersive audiobooks, podcasts, and interactive media. Direct every performance line by line with granular control over acting cues, pacing, dialect shifts, and backchanneling.</li><li data-block-key="e855d"><b>Gemini 3.8 Flash-Lite TTS:</b> Built for high-volume, cost-efficient scale. Optimized for high-volume dubbing, audio content creation, and expressive voice agents with fine-grained control over tone, pacing, and expressive nuance.</li></ul><p data-block-key="ca5gi">These models complement our fast-growing Gemini Audio family, following <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/">3.5 Live Translate</a>, <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">3.5 Transcribe</a>, <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">3.8 Live, and 3.8 Live Extended Thinking</a>.</p><h2 data-block-key="4tcsr">Create and customize your own voices</h2></div>
  </uni-article-paragraph>
</section>

  

  
    
  
    



<uni-youtube-player-article
  index="2"
  page-title="Gemini 3.8 text-to-speech says hello"
  thumbnail-alt="a YouTube video showing how to create your own voices with Gemini 3.8 text-to-speech"
  
  
  
  video-id="FL6mI_Br-mc"
  video-type="video"
  
  
  >
</uni-youtube-player-article>










  


  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="sl809">Scale up from 30 original voices to an infinite library. Whether you need an entirely original character voice or a consistent brand ambassador, our 3.8 Flash TTS model powers a full vocal studio. This enables you to create and use expressive, natural-sounding voices for every moment, while empowering developers and enterprises to easily build custom audio experiences.</p><ul><li data-block-key="1unoa"><b>Generative voice design:</b> With Gemini 3.8 Flash TTS, create bespoke voices from scratch by customizing role, accent and voice characteristics across more than 100 languages and dialects using natural language prompting — whether you're bringing a dramatic, fire-breathing dragon to life or crafting a charismatic narrator with a distinct regional cadence.</li></ul></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header="Hear how Gemini 3.8 Flash TTS generates a high-energy DJ voice from Melbourne."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/AudioWaveform-Blue_HighEnergyDJ.mp4"
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="Video recording of a generated voice playing, showcasing a high-energy radio DJ with a distinct Melbourne, Australian accent."
  video-title="Blue High Energy DJ"
  
  
    
  
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="nh9zu">Hear how Gemini 3.8 Flash TTS generates a high-energy DJ voice from Melbourne.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header="Hear how Gemini 3.8 Flash TTS generates a super-tinny, monotone robot voice."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/AudioWaveform-Blue_MonotoneRobot.mp4"
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="Video recording of a generated voice playing, showcasing a heavily stylized, super-tinny and monotone metallic robot voice."
  video-title="Blue Monotone robot"
  
  
    
  
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="n3uni">Hear how Gemini 3.8 Flash TTS generates a super-tinny, monotone robot voice.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="2"
  accordion-header="Hear how Gemini 3.8 Flash TTS brings a Japanese dragon to life."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/AudioWaveform-Blue_JapaneseDragon.mp4"
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="Video recording of a generated voice playing, showcasing a dramatic, deep voice of a Japanese dragon."
  video-title="Blue Japanese Dragon audiowave"
  
  
    
  
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="uovbo">Hear how Gemini 3.8 Flash TTS brings a Japanese dragon to life.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
    </uni-media-carousel-viewport>

    <div slot="controls">
      <div class="uni-media-carousel__controls-container">
        <uni-carousel-controls class="uni-media-carousel__controls"></uni-carousel-controls>
      </div>
    </div>
  </uni-media-carousel>
</section>
  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><ul><li data-block-key="sl809"><b>Expansive voice library:</b> Access 2,000+ production-ready voices with broad language coverage — including regional varieties like Mexican Spanish, Quebec French, and Scots English.</li><li data-block-key="3o88r"><b>Voice replication:</b> Recreate consistent vocal profiles from just a 30-second audio sample of your voice or a voice you have the rights to use, backed by built-in consent verification, SynthID watermarking, and C2PA credentials to protect both developers and their vocal talent.</li><li data-block-key="6vf6t"><b>Save and scale:</b> Save and manage the custom voices you designed to ensure consistent performance and minimal drift across ongoing projects.</li><li data-block-key="brtqf"><b>Voice remixing:</b> Coming soon, pick a voice from our voice library and fine-tune timbre, pitch, pace, and accent. Use prompts to dial in characteristics (e.g. “add subtle Southern US accent” or “soften the delivery”).</li></ul><h2 data-block-key="75bm2">Direct the performance, line by line</h2><p data-block-key="7h8p6">Once you've selected your voices, both TTS models give you precise control over how each line is delivered.</p><ul><li data-block-key="6q9k2"><b>Direct performance line by line:</b> Write your own stage directions or let Gemini steer delivery with natural script cues — from a calm customer service agent to a whispered suspense scene.</li></ul></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header="Hear how Gemini 3.8 Flash TTS enables natural, highly expressive conversations for interactive voice agents."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/AudioWaveform-Blue_SingleSpeakerCES_Teleprompter.mp4"
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="Video recording of a digital script playing with generated voice, showcasing a highly natural customer service voice agent in conversation."
  video-title="blue single speaker audiowave"
  
  
    
  
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="iwplw">Hear how Gemini 3.8 Flash TTS enables natural, highly expressive conversations for interactive voice agents.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header="Watch and hear how Gemini 3.8 Flash TTS uses granular script control to build a deeply engaging, immersive audio experience."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/AudioWaveform-Blue_DramaticScreenplay_Teleprompter.mp4"
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="Video recording of a teleprompter-style script playing with generated voice, showcasing expressive audio output with natural pauses, whispers."
  video-title="audiowave blue dramatic Screenplay"
  
  
    
  
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="0s9hj">Watch and hear how Gemini 3.8 Flash TTS uses granular script control to build a deeply engaging, immersive audio experience.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
    </uni-media-carousel-viewport>

    <div slot="controls">
      <div class="uni-media-carousel__controls-container">
        <uni-carousel-controls class="uni-media-carousel__controls"></uni-carousel-controls>
      </div>
    </div>
  </uni-media-carousel>
</section>
  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><ul><li data-block-key="sl809"><b>Long-form generation:</b> Maintain high voice quality, natural pacing, and character timbre across hours of continuous audio with minimal speaker drift — ideal for podcasts and audiobooks.</li><li data-block-key="9f0e6"><b>Native two-speaker scene staging:</b> Direct multi-turn conversations seamlessly from a single script —whether for a podcast or dramatic storytelling—while keeping both voices distinctly separated with natural conversational turn-taking.</li><li data-block-key="85j94"><b>Scripted vocal bursts &amp; backchanneling:</b> Add realistic conversational texture using non verbal cues (like &lt;laughs&gt;, &lt;sigh&gt;, &lt;gasp&gt; and active-listening interjections (like |mhm| or|yeah|) for precise comedic timing and reaction beats.</li></ul></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header="See how Gemini 3.8 Flash TTS turns natural language prompts into bespoke vocal personas from scratch."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/TTSfinalCompressed.mp4"
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="A screen recording of a creator using Gemini 3.8 Flash TTS to design custom character voices in a video game intro scene."
  video-title="TTS Final Compressed Video Game"
  
  
    
  
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="tgkxn"><i>See how Gemini 3.8 Flash TTS turns natural language prompts into bespoke vocal personas from scratch.</i></p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header="Watch how Gemini 3.8 Flash TTS enables creators to design custom scenes to bring animated dialogue to life."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Detective_Short_WithEndCard_V2.mp4"
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="Screen recording of a creator designing custom voices"
  video-title="Detective Short"
  
  
    
  
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="rmhb6"><i>Watch how Gemini 3.8 Flash TTS enables creators to design custom scenes to bring animated dialogue to life.</i></p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="2"
  accordion-header="See how Gemini 3.8 Flash TTS turns scripts into fully performed dialogue scenes, letting creators direct vocal delivery, and natural turn-taking."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/TableRead_Blog_V1.mp4"
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="Video showing how Gemini 3.8 TTS turns scripts into fully performed dialogue scenes"
  video-title="table read blog"
  
  
    
  
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="atfz3"><i>See how Gemini 3.8 Flash TTS turns scripts into fully performed dialogue scenes, letting creators direct vocal delivery, and natural turn-taking.</i></p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
    </uni-media-carousel-viewport>

    <div slot="controls">
      <div class="uni-media-carousel__controls-container">
        <uni-carousel-controls class="uni-media-carousel__controls"></uni-carousel-controls>
      </div>
    </div>
  </uni-media-carousel>
</section>
  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="sl809">Get expressive high-quality speech generation built for global scale</h2><p data-block-key="6f4us">Gemini 3.8 Flash TTS delivers leading voice customization capabilities, securing the #1 overall spot on <a href="https://www.hume.ai/rw-voice-eq">Hume AI’s</a> Voice Design Benchmark (71.4) and also leading in accent modeling (60.8).</p><p data-block-key="7va56">Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS enable truly expressive performances without sacrificing reliability, also securing the #1 and #2 spots respectively on Hume AI’s Overall Quality Index. The model shows major improvements on a wide range of use cases such as long-form content and dual-speaker screenplay control compared to Gemini 3.1 Flash TTS.</p><p data-block-key="dlj5b">In blind human preference evaluations on <a href="https://voicearena.com/tts-leaderboard/us-english)">Voice Arena</a>, Gemini 3.8 Flash and Flash-Lite TTS secure top positions amongst competitors in key global languages, including Japanese, Brazilian Portuguese, Vietnamese, Modern Standard Arabic (MSA), Mexican Spanish and Hindi. With support for over 100 languages, these models empower creators, developers, and enterprises to build high-quality, multilingual voice experiences worldwide.</p></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="An evaluation showing text-to-speech quality benchmark Hume AI"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="An evaluation showing text-to-speech quality benchmark Hume AI"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/blog-gemini-3.8-flash-tts__evals_.width-100.format-webp_21WnKg9.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/blog-gemini-3.8-flash-tts__evals_.width-500.format-webp_Qb513FS.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/blog-gemini-3.8-flash-tts__evals.width-1000.format-webp_hBIZaRI.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="an evaluation chart showing text to speech voice design leaderboard Hume AI"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="an evaluation chart showing text to speech voice design leaderboard Hume AI"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/blog-gemini-3.8-flash-tts__evals_.width-100.format-webp_tbi15co.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/blog-gemini-3.8-flash-tts__evals_.width-500.format-webp_8W8j811.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/blog-gemini-3.8-flash-tts__evals.width-1000.format-webp_3X4R0xy.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="2"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="an evaluation chart showing text to speech leaderboard for Voice Arena"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="an evaluation chart showing text to speech leaderboard for Voice Arena"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/blog-gemini-3.8-flash-tts__evals_.width-100.format-webp_47W1vK6.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/blog-gemini-3.8-flash-tts__evals_.width-500.format-webp_InRpLyH.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/blog-gemini-3.8-flash-tts__evals.width-1000.format-webp_UFC28T9.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
    </uni-media-carousel-viewport>

    <div slot="controls">
      <div class="uni-media-carousel__controls-container">
        <uni-carousel-controls class="uni-media-carousel__controls"></uni-carousel-controls>
      </div>
    </div>
  </uni-media-carousel>
</section>
  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="sl809">Build with trust, consent, and transparency</h2><p data-block-key="5e3h">We built our voice creation and replication capabilities with strict safeguards to help protect voice talent, respect identity, and ensure content transparency. For voice replication our system leverages consent verification: users must provide a verbal consent recording from the voice owner that matches the reference speaker before a voice can be created.</p><p data-block-key="ansrm">More broadly, every audio clip generated by our Gemini Audio models is watermarked with<a href="https://deepmind.google/models/synthid/"> SynthID</a>. This imperceptible watermark is woven directly into the audio output, ensuring AI-generated speech remains detectable to help prevent misinformation. For more details on our approach to safety and responsibility, review the <a href="https://deepmind.google/models/model-cards/gemini-3-8-audio/">model card</a>.</p><h2 data-block-key="bj4kd">Try our new Google AI Studio audio playground</h2><p data-block-key="trp4">Starting today, developers can experience these new<a href="https://aistudio.google.com/docs/speech-generation"> speech generation</a> capabilities in<a href="https://aistudio.google.com/generate-speech?model=gemini-3.8-flash-tts"> Google AI Studio</a>. Built like a voice design workspace, you can prompt entirely new vocal identities from scratch or replicate your own voice

<a class="superscript"
    data-ga4-analytics-superscript-click
    data-tooltip-content-id="footnote-content-1"
    data-target="inline text"
    href="#footnote-1"
    id="footnote-source-1"
    aria-label="Jump to link reference 1"><sup>1</sup></a>
, then bring them directly into a dual-speaker screenplay editor to direct line-by-line delivery.</p></div>
  </uni-article-paragraph>
</section>

  

  
    





























<section class="uni-page uni-grid uni-inline-image-section" data-component="uni-inline-image">
  <uni-inline-image
    class="uni-inline-image uni-inline-image--full"
    alignment="full"
    alt-text="A screen recording of a user demonstrates the voice replication workflow in the Google AI Studio interface."
    external-image=""
    or-mp4-video-title="AIS voice replication"
    or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/ais-voice-replication_1.mp4"
    section-header="Gemini 3.8 text-to-speech says hello"
    
      poster-image-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/wagtailvideo-sksqctrn_thumb.jpg"
    
    
    
      
    
    
    
    
  >
    
      <div slot="caption-slot">
        <div class="rich-text"><p data-block-key="hg083">Try voice replication in Google AI Studio.</p></div>
      </div>
    

    
  </uni-inline-image>
</section>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="z5c3v">Deploy high-performance voice interfaces with ease</h2><p data-block-key="5tik7">By using the Gemini API, developer platforms such as <a href="http://docs.agora.io/en/ai/models/tts/gemini">Agora</a>, <a href="https://docs.livekit.io/agents/models/tts/gemini/">LiveKit</a>, <a href="https://docs.pipecat.ai/api-reference/server/services/tts/google#geminittsservice">Pipecat</a>, <a href="https://vercel.com/docs/ai-gateway/modalities/text-to-speech">Vercel</a> enable developers to build and deploy high-performance speech generation experiences with ease.</p><p data-block-key="9to4n">We’re partnering with companies like Figma, HeyGen, Linguana, Wondercraft, 99.co, and Ollang, who are integrating our latest TTS models to help accelerate global dubbing, localize media with nuanced regional accents, and power conversational voice agents at scale.</p></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="a quote from Darius Cheung, CEO and Co-Founder of 99 Group"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="a quote from Darius Cheung, CEO and Co-Founder of 99 Group"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-99-grou.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-99-grou.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-99-gro.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="a quote from Mason Adams, Developer Evangelist, Agora"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="a quote from Mason Adams, Developer Evangelist, Agora"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-agora__.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-agora__.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-agora_.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="2"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="a quote from Jonathan Gur-Zeev, Director of Product, Figma Weave"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="a quote from Jonathan Gur-Zeev, Director of Product, Figma Weave"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-figma-w.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-figma-w.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-figma-.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="3"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="a quote from Bin Liu, VP of Engineering for Hygen"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="a quote from Bin Liu, VP of Engineering for Hygen"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-heygen_.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-heygen_.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-heygen.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="4"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="a quote card from Luke Pane, Developer, katsuyo"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="a quote card from Luke Pane, Developer, katsuyo"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-katsuyo.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-katsuyo.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-katsuy.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="5"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="quote from Ritwik Baranwal, Associate Director AI/ML of kuku."
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="quote from Ritwik Baranwal, Associate Director AI/ML of kuku."
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-kuku-FM.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-kuku-FM.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-kuku-F.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="6"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="a quote from Oded Shafran, Co-Founder &amp; CTO of linguana"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="a quote from Oded Shafran, Co-Founder &amp; CTO of linguana"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-linguan.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-linguan.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-lingua.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="7"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="Aziz Ulak, CTO &amp; Co-founder, Ollang"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="Aziz Ulak, CTO &amp; Co-founder, Ollang"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-olang__.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-olang__.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-olang_.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="8"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="a quote from Phil Marshall, Founder and CEO of Spoken"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="a quote from Phil Marshall, Founder and CEO of Spoken"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-spoken_.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-spoken_.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-spoken.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="9"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="quote from Zina Rahman, Co-Founder and CEO, Transforms.AI"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="quote from Zina Rahman, Co-Founder and CEO, Transforms.AI"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-transit.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-transit.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-transi.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="10"
  accordion-header=""
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.8 text-to-speech says hello"
  alt-text="quote from Mei Ki Yiu, CTO of Wondercraft"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="quote from Mei Ki Yiu, CTO of Wondercraft"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-wonderc.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-wonderc.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio__testimonial-wonder.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
</uni-media-carousel-slide>

      
    </uni-media-carousel-viewport>

    <div slot="controls">
      <div class="uni-media-carousel__controls-container">
        <uni-carousel-controls class="uni-media-carousel__controls"></uni-carousel-controls>
      </div>
    </div>
  </uni-media-carousel>
</section>
  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="sl809">Start using our latest Gemini Audio models:</h2><p data-block-key="enfp1">Gemini 3.8 Flash TTS is rolling out starting today:</p><ul><li data-block-key="2rq5m"><b>For developers</b>: In the <a href="https://aistudio.google.com/docs/speech-generation">Gemini API</a> and <a href="https://aistudio.google.com/generate-speech?model=gemini-3.8-flash-tts">Google AI Studio</a></li><li data-block-key="4gpf6"><b>For enterprises</b>: Coming soon via API in <a href="https://docs.cloud.google.com/gemini-enterprise-agent-platform">Gemini Enterprise</a></li><li data-block-key="6qt2t"><b>For everyone</b>: In <a href="https://notebook.google.com/">Gemini Notebook</a>.</li></ul><p data-block-key="8msmr">Gemini 3.8 Flash-Lite TTS is rolling out starting today:</p><ul><li data-block-key="cpdma"><b>For developers</b>: In the <a href="https://aistudio.google.com/docs/speech-generation">Gemini API</a> and <a href="https://aistudio.google.com/generate-speech?model=gemini-3.8-flash-lite-tts">Google AI Studio</a></li><li data-block-key="c663k"><b>For enterprises</b>: Coming soon via API in <a href="https://docs.cloud.google.com/gemini-enterprise-agent-platform">Gemini Enterprise</a></li><li data-block-key="17fbe"><b>For everyone</b>: In <a href="http://vids.new/">Google Vids</a></li></ul></div>
  </uni-article-paragraph>
</section>

  

  
    
















<uni-portal portal-id="article-newsletter-portal">


<section
  class="
    uni-article-newsletter
    
      uni-article-newsletter--bottom
      uni-article-newsletter--neutral
    
  "
  data-component="uni-article-newsletter"
  data-analytics-module='{
    "module_name": "Newsletter",
    "section_header": "Get the latest news from Google in your inbox"
  }'
>
  <div class="uni-page">
    <div class="uni-grid">
      
      <div class="uni-article-newsletter__background uni-grid__col--span-4 uni-grid__col--span-12-tablet uni-grid__col--span-6-desktop uni-grid__col--start-7-desktop" aria-hidden="true">

        
        <div
          class="
            uni-article-newsletter__shape
            
              uni-article-newsletter__shape--pill
            
          "
          aria-hidden="true"
        ></div>
      </div>
      <div class="uni-article-newsletter__inner uni-grid__col--span-12 uni-grid__col--span-6-desktop uni-grid__col--start-1">

        <div class="uni-article-newsletter__form-group">
          <h2 class="uni-article-newsletter__title font-h3">
            Get the latest news from Google in your inbox
          </h2>
          <p class="uni-article-newsletter__description font-body-m">
            Sign up for our newsletters with product updates, event information, special offers, and more.
          </p>

          <div class="uni-article-newsletter__form-container">
            <div class="uni-article-newsletter__input-group">
              <uni-newsletter-form
                class="uni-landing-newsletter-form"
                action="https://services.google.com/fb/submissions/thekeywordnewsletterprodv2/"
                method="POST"
                content-type="blogv2 | article page"
                cta-override=""
                data-error-icon-url="/static/blogv2/images/alert_error_form.svg"
              >
              </uni-newsletter-form>
            </div>
          </div>

          




<div class="uni-landing-newsletter-success is-hidden">
  <div class="uni-landing-newsletter-success__message">
    <div class="uni-landing-newsletter-success__logo">
      <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#check-circle"></use>
</svg>

    </div>
    <div class="uni-landing-newsletter-success__text">
      <p class="font-body-s">Done. Just one step more.</p>
      <p
        class="uni-landing-newsletter-success__text-confirm font-body-xs"
        id="subscribe_success_label"
        tabindex="-1"
        role="text">
        Check your inbox to confirm your subscription.
      </p>
    </div>
  </div>
  <p class="uni-landing-newsletter-success__final-text font-body-s">
    You can also subscribe with a <button class="uni-landing-newsletter-success__different-email uni-anchor">different email address</button>.
  </p>
</div>


          <p class="uni-article-newsletter__info font-caption">
            Your information will be used in accordance with <a href="https://policies.google.com/privacy" target="_blank" class="uni-anchor">Google's privacy policy.</a> You may opt out at any time.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>


</uni-portal>


  


          
          

          
            


<div
  class="
    uni-blog-article-tags
    article-tags
    uni-page
    uni-grid
    
  "
  data-component="uni-article-tags"
  data-analytics-module='{
    "module_name": "Article Tags",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <div class="uni-grid__col--layout-8">
    <div class="uni-blog-article-tags__wrapper">
      <span class="uni-blog-article-tags__label font-h4">Posted in:</span>
    </div>
    <nav class="uni-blog-article-tags__container uni-click-tracker">
      <ul class="uni-blog-article-tags__tags-list">
        
        
          
          
          
            <li class="uni-blog-article-tags__tags-item">
              

  <a class="uni-blog-article-tags__tags-value font-body-s uni-blog-article-tags__theme-blue uni-blog-article-tags__link-active"
     href="https://blog.google/products-and-platforms/products/gemini/"
     

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "Gemini models"
}'
>
    Gemini models
  </a>


            </li>
          
        

        

        
        
          
          
          
        

        
      </ul>
    </nav>
  </div>
</div>

          
        </div>
      
    </section>
  </article>
  



  








  <uni-footnotes
    
      layout="article"
    
    >
    <div class="uni-footnotes__slot" slot="footnotes-slot">
      
        <div id="footnote-1"
          class="uni-footnotes__text">
          <a class="uni-footnotes__index font-body-m"
            title="Jump up"
            href="#footnote-source-1"
            aria-label="Jump up to link reference 1"
            data-ga4-analytics-superscript-click
            data-target="footer">
            <span>1</span>
          </a>
          <div><div class="rich-text"><p data-block-key="sat0e">Voice replication through AI Studio is not available in Illinois, Texas, EEA, UK, Switzerland, and India.</p></div></div>
        </div>
      
    </div>
  </uni-footnotes>



  

  
    









<uni-related-articles class="uni-related-articles kw-speakable-hidden ga4-carousel"
  data-analytics-module='{
    "module_name": "Article Footer Related Stories",
    "section_header": "Related stories"
  }'
  data-shape-context-provider
>
  <div class="uni-page">
    <div class="uni-grid">
      <h2 class="uni-grid__col--span-12 uni-related-articles__header font-h3">
        Related stories
      </h2>
    </div>
  </div>

  <div class="uni-page--fullbleed">
    <uni-carousel>
      <scrollable-cards-panel-viewport slot="viewport" class="uni-related-articles__viewport" step="1">
        
          








<a
  href="https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/"
  class="uni-article-card"
  aria-label="
    
      
      AI - 
    
    The latest AI news we announced in September 2026
    
    
      - By Blog Team
    
    
      - Oct 02, 2026
    
  "
  data-index="1"
  data-target="card"
  data-primaryTag="topics - ai"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "The latest AI news we announced in September 2026",
  "link_url": "https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/",
  "source_content": "Related stories",
  "related_index": "1",
  "related_article_tag": "topics - ai",
  "article_name": "The latest AI news we announced in September 2026",
  "author_name": "Blog Team",
  "content_type": "blogv2 | article page"
}'

  
  data-theme-color="purple"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["12-sided-cookie", "4-sided-cookie", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/September_AI_Recap_he.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/September_AI_Recap_he.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/September_AI_Recap_he.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
    loading="lazy"
  
  />




      
    </div>
  </div>

  <div class="uni-article-card__content">
    <div class="uni-article-card__text">
      
      <span
        class="uni-article-card__eyebrow font-eyebrow"
        data-target="eyebrow">
        
          AI
        
      </span>
      
      <h3
        class="uni-article-card__title font-h5"
        data-target="title">
        The latest AI news we announced in September 2026
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Blog Team
          
        </span>
      
    </div>
  </div>
</a>


        
          








<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/"
  class="uni-article-card"
  aria-label="
    
      
      Gemini models - 
    
    Gemini 4 Argon: our next era of frontier intelligence
    
    
      - By Koray Kavukcuoglu
    
    
      - Sep 30, 2026
    
  "
  data-index="2"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Gemini 4 Argon: our next era of frontier intelligence",
  "link_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
  "source_content": "Related stories",
  "related_index": "2",
  "related_article_tag": "topics - gemini models",
  "article_name": "Gemini 4 Argon: our next era of frontier intelligence",
  "author_name": "Koray Kavukcuoglu",
  "content_type": "blogv2 | article page"
}'

  
  data-theme-color="blue"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-sided-cookie", "bun", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/g4_30-09-26_key-art_b.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/g4_30-09-26_key-art_b.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/g4_30-09-26_key-art_b.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
    loading="lazy"
  
  />




      
    </div>
  </div>

  <div class="uni-article-card__content">
    <div class="uni-article-card__text">
      
      <span
        class="uni-article-card__eyebrow font-eyebrow"
        data-target="eyebrow">
        
          Gemini models
        
      </span>
      
      <h3
        class="uni-article-card__title font-h5"
        data-target="title">
        Gemini 4 Argon: our next era of frontier intelligence
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Koray Kavukcuoglu
          
        </span>
      
    </div>
  </div>
</a>


        
          








<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-flash-developers/"
  class="uni-article-card"
  aria-label="
    
      
      Gemini models - 
    
    See what 4 builders are making with Gemini 3.8 Flash
    
    
      - By Lindsey Lanquist
    
    
      - Sep 28, 2026
    
  "
  data-index="3"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "See what 4 builders are making with Gemini 3.8 Flash",
  "link_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-flash-developers/",
  "source_content": "Related stories",
  "related_index": "3",
  "related_article_tag": "topics - gemini models",
  "article_name": "See what 4 builders are making with Gemini 3.8 Flash",
  "author_name": "Lindsey Lanquist",
  "content_type": "blogv2 | article page"
}'

  
  data-theme-color="blue"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-sided-cookie", "bun", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Builders_Gemini_3.8_F.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Builders_Gemini_3.8_F.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Builders_Gemini_3.8_F.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
    loading="lazy"
  
  />




      
    </div>
  </div>

  <div class="uni-article-card__content">
    <div class="uni-article-card__text">
      
      <span
        class="uni-article-card__eyebrow font-eyebrow"
        data-target="eyebrow">
        
          Gemini models
        
      </span>
      
      <h3
        class="uni-article-card__title font-h5"
        data-target="title">
        See what 4 builders are making with Gemini 3.8 Flash
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Lindsey Lanquist
          
        </span>
      
    </div>
  </div>
</a>


        
          








<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/"
  class="uni-article-card"
  aria-label="
    
      
      Gemini models - 
    
    Introducing Gemini 3.8 Live with Live Avatar
    
    
      - By Shuo-yiin Chang& CJ Zheng
    
    
      - Sep 24, 2026
    
  "
  data-index="4"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Introducing Gemini 3.8 Live with Live Avatar",
  "link_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/",
  "source_content": "Related stories",
  "related_index": "4",
  "related_article_tag": "topics - gemini models",
  "article_name": "Introducing Gemini 3.8 Live with Live Avatar",
  "author_name": "Shuo\u002Dyiin Chang, CJ Zheng",
  "content_type": "blogv2 | article page"
}'

  
  data-theme-color="blue"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-sided-cookie", "bun", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Slide_16_9_-_37.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Slide_16_9_-_37.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Slide_16_9_-_37.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
    loading="lazy"
  
  />




      
    </div>
  </div>

  <div class="uni-article-card__content">
    <div class="uni-article-card__text">
      
      <span
        class="uni-article-card__eyebrow font-eyebrow"
        data-target="eyebrow">
        
          Gemini models
        
      </span>
      
      <h3
        class="uni-article-card__title font-h5"
        data-target="title">
        Introducing Gemini 3.8 Live with Live Avatar
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Shuo-yiin Chang
          
            & 
            CJ Zheng
          
        </span>
      
    </div>
  </div>
</a>


        
          








<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/"
  class="uni-article-card"
  aria-label="
    
      
      Gemini models - 
    
    Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking
    
    
      - By Tom Ouyang& Malini Jaganathan
    
    
      - Sep 15, 2026
    
  "
  data-index="5"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking",
  "link_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
  "source_content": "Related stories",
  "related_index": "5",
  "related_article_tag": "topics - gemini models",
  "article_name": "Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking",
  "author_name": "Tom Ouyang, Malini Jaganathan",
  "content_type": "blogv2 | article page"
}'

  
  data-theme-color="blue"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-sided-cookie", "bun", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_3-8_live___key.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_3-8_live___key.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_3-8_live___key.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
    loading="lazy"
  
  />




      
    </div>
  </div>

  <div class="uni-article-card__content">
    <div class="uni-article-card__text">
      
      <span
        class="uni-article-card__eyebrow font-eyebrow"
        data-target="eyebrow">
        
          Gemini models
        
      </span>
      
      <h3
        class="uni-article-card__title font-h5"
        data-target="title">
        Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Tom Ouyang
          
            & 
            Malini Jaganathan
          
        </span>
      
    </div>
  </div>
</a>


        
          








<a
  href="https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/"
  class="uni-article-card"
  aria-label="
    
      
      Safety &amp; Security - 
    
    Proactive cyber defense for governments and enterprises
    
    
      - By Four Flynn
    
    
      - Sep 02, 2026
    
  "
  data-index="6"
  data-target="card"
  data-primaryTag="topics - safety &amp; security"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Proactive cyber defense for governments and enterprises",
  "link_url": "https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/",
  "source_content": "Related stories",
  "related_index": "6",
  "related_article_tag": "topics - safety &amp; security",
  "article_name": "Proactive cyber defense for governments and enterprises",
  "author_name": "Four Flynn",
  "content_type": "blogv2 | article page"
}'

  
  data-theme-color="yellow"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-leaf-clover", "circle", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-8__fairwind-.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-8__fairwind-.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-8__fairwind-.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
    loading="lazy"
  
  />




      
    </div>
  </div>

  <div class="uni-article-card__content">
    <div class="uni-article-card__text">
      
      <span
        class="uni-article-card__eyebrow font-eyebrow"
        data-target="eyebrow">
        
          Safety &amp; Security
        
      </span>
      
      <h3
        class="uni-article-card__title font-h5"
        data-target="title">
        Proactive cyber defense for governments and enterprises
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Four Flynn
          
        </span>
      
    </div>
  </div>
</a>


        
      </scrollable-cards-panel-viewport>

      <div slot="controls" class="uni-page">
        <div class="uni-grid">
          <div class="uni-grid__col--span-4 uni-grid__col--span-6-tablet uni-grid__col--span-4-mobile">
            <uni-carousel-controls class="uni-related-articles__controls"></uni-carousel-controls>
          </div>
        </div>
      </div>
    </uni-carousel>
  <div>
</uni-related-articles>

  

        </main>

        

          
            
          
        
        <uni-portal destination portal-id="article-newsletter-portal"></uni-portal>
        










  
  
  
  


<footer
  class="uni-footer redesign-patch"
  id="footer-standard"
  data-component="uni-footer-component"
  data-analytics-module='{
    "module_name": "footer",
    "section_header": "Gemini 3.8 text\u002Dto\u002Dspeech says hello"
  }'>
  <section class="uni-footer__logo">
    <a href="https://www.google.com" aria-label="The Google logo">
      <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 396 130"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#google-logo"></use>
</svg>

    </a>
  </section>
  <ul class="uni-footer__main-links">
    <li class="uni-footer__links-item">
      
      <uni-cta emphasis="low" href="https://policies.google.com/privacy">
        Privacy
      </uni-cta>
    </li>
    <li class="uni-footer__links-item">
      
      <uni-cta emphasis="low" href="https://policies.google.com/terms">
        Terms
      </uni-cta>
    </li>
    <li class="uni-footer__links-item">
      
      <uni-cta emphasis="low" href="https://support.google.com">
        Help
      </uni-cta>
    </li>
    <li class="uni-footer__links-item">
      

<div
  class="uni-dropdown font-ctas"
  data-component="uni-dropdown">
  <select
    name="more-of-google-dropdown"
    id="more-of-google-dropdown-select"
    class="uni-dropdown__select"
    aria-label="More of Google">
    
    <option
      value="https://about.google/"
      label="More of Google"
      class="uni-dropdown__option">
      More of Google
    </option>
    
    <option
      value="https://about.google/products/"
      label="Google Products"
      class="uni-dropdown__option">
      Google Products
    </option>
    
    <option
      value="/about/"
      label="About the Blog"
      class="uni-dropdown__option">
      About the Blog
    </option>
    
  </select>
  <span class="uni-dropdown__chevron">
    <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#expand_more"></use>
</svg>

  </span>
</div>

    </li>
    <li class="uni-footer__links-item">
      


  <div data-component="uni-lang-picker" class="uni-lang-picker">
    <select
      name="language-picker"
      class="uni-lang-picker__select font-ctas"
      aria-label="Change Region">
      
      <option
        label="Global (English)"
        value="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/"
        lang="en-us"
        class="uni-lang-picker__option"
        
          selected="selected"
          data-selected-index="0"
        >
        Global (English)
      </option>
      
      <option
        label="Africa (English)"
        value="https://blog.google/intl/en-africa/"
        lang="en-africa"
        class="uni-lang-picker__option"
        >
        Africa (English)
      </option>
      
      <option
        label="Australia (English)"
        value="https://blog.google/intl/en-au/"
        lang="en-au"
        class="uni-lang-picker__option"
        >
        Australia (English)
      </option>
      
      <option
        label="Brasil (Português)"
        value="https://blog.google/intl/pt-br/"
        lang="pt-br"
        class="uni-lang-picker__option"
        >
        Brasil (Português)
      </option>
      
      <option
        label="Canada (English)"
        value="https://blog.google/intl/en-ca/"
        lang="en-ca"
        class="uni-lang-picker__option"
        >
        Canada (English)
      </option>
      
      <option
        label="Canada (Français)"
        value="https://blog.google/intl/fr-ca/"
        lang="fr-ca"
        class="uni-lang-picker__option"
        >
        Canada (Français)
      </option>
      
      <option
        label="Česko (Čeština)"
        value="https://blog.google/intl/cs-cz/"
        lang="cs-cz"
        class="uni-lang-picker__option"
        >
        Česko (Čeština)
      </option>
      
      <option
        label="Deutschland (Deutsch)"
        value="https://blog.google/intl/de-de/"
        lang="de-de"
        class="uni-lang-picker__option"
        >
        Deutschland (Deutsch)
      </option>
      
      <option
        label="España (Español)"
        value="https://blog.google/intl/es-es/"
        lang="es-es"
        class="uni-lang-picker__option"
        >
        España (Español)
      </option>
      
      <option
        label="France (Français)"
        value="https://blog.google/intl/fr-fr/"
        lang="fr-fr"
        class="uni-lang-picker__option"
        >
        France (Français)
      </option>
      
      <option
        label="Greece (Ελληνικά)"
        value="https://blog.google/intl/el-gr/"
        lang="el-gr"
        class="uni-lang-picker__option"
        >
        Greece (Ελληνικά)
      </option>
      
      <option
        label="India (English)"
        value="https://blog.google/intl/en-in/"
        lang="en-in"
        class="uni-lang-picker__option"
        >
        India (English)
      </option>
      
      <option
        label="Indonesia (Bahasa Indonesia)"
        value="https://blog.google/intl/id-id/"
        lang="id-id"
        class="uni-lang-picker__option"
        >
        Indonesia (Bahasa Indonesia)
      </option>
      
      <option
        label="Ireland (English)"
        value="https://blog.google/intl/en-ie/"
        lang="en-ie"
        class="uni-lang-picker__option"
        >
        Ireland (English)
      </option>
      
      <option
        label="Italia (Italiano)"
        value="https://blog.google/intl/it-it/"
        lang="it-it"
        class="uni-lang-picker__option"
        >
        Italia (Italiano)
      </option>
      
      <option
        label="日本 (日本語)"
        value="https://blog.google/intl/ja-jp/"
        lang="ja-jp"
        class="uni-lang-picker__option"
        >
        日本 (日本語)
      </option>
      
      <option
        label="대한민국 (한국어)"
        value="https://blog.google/intl/ko-kr/"
        lang="ko-kr"
        class="uni-lang-picker__option"
        >
        대한민국 (한국어)
      </option>
      
      <option
        label="Latinoamérica (Español)"
        value="https://blog.google/intl/es-419/"
        lang="es-419"
        class="uni-lang-picker__option"
        >
        Latinoamérica (Español)
      </option>
      
      <option
        label="Malaysia (English)"
        value="https://blog.google/intl/en-my/"
        lang="en-my"
        class="uni-lang-picker__option"
        >
        Malaysia (English)
      </option>
      
      <option
        label="الشرق الأوسط وشمال أفريقيا (اللغة العربية)"
        value="https://blog.google/intl/ar-mena/"
        lang="ar-mena"
        class="uni-lang-picker__option"
        >
        الشرق الأوسط وشمال أفريقيا (اللغة العربية)
      </option>
      
      <option
        label="MENA (English)"
        value="https://blog.google/intl/en-mena/"
        lang="en-mena"
        class="uni-lang-picker__option"
        >
        MENA (English)
      </option>
      
      <option
        label="Nederlands (Nederland)"
        value="https://blog.google/intl/nl-nl/"
        lang="nl-nl"
        class="uni-lang-picker__option"
        >
        Nederlands (Nederland)
      </option>
      
      <option
        label="New Zealand (English)"
        value="https://blog.google/intl/en-nz/"
        lang="en-nz"
        class="uni-lang-picker__option"
        >
        New Zealand (English)
      </option>
      
      <option
        label="Polska (Polski)"
        value="https://blog.google/intl/pl-pl/"
        lang="pl-pl"
        class="uni-lang-picker__option"
        >
        Polska (Polski)
      </option>
      
      <option
        label="Portugal (Português)"
        value="https://blog.google/intl/pt-pt/"
        lang="pt-pt"
        class="uni-lang-picker__option"
        >
        Portugal (Português)
      </option>
      
      <option
        label="România (Română)"
        value="https://blog.google/intl/ro-ro/"
        lang="ro-ro"
        class="uni-lang-picker__option"
        >
        România (Română)
      </option>
      
      <option
        label="Sverige (Svenska)"
        value="https://blog.google/intl/sv-se/"
        lang="sv-se"
        class="uni-lang-picker__option"
        >
        Sverige (Svenska)
      </option>
      
      <option
        label="ประเทศไทย (ไทย)"
        value="https://blog.google/intl/th-th/"
        lang="th-th"
        class="uni-lang-picker__option"
        >
        ประเทศไทย (ไทย)
      </option>
      
      <option
        label="Türkiye (Türkçe)"
        value="https://blog.google/intl/tr-tr/"
        lang="tr-tr"
        class="uni-lang-picker__option"
        >
        Türkiye (Türkçe)
      </option>
      
      <option
        label="台灣 (中文)"
        value="https://blog.google/intl/zh-tw/"
        lang="zh-tw"
        class="uni-lang-picker__option"
        >
        台灣 (中文)
      </option>
      
    </select>
    <span class="uni-lang-picker__chevron">
      <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261008-1701#expand_more"></use>
</svg>

    </span>
  </div>

    </li>
  </ul>

    <ul class="uni-footer__social-networks">
      
        
        <li class="uni-footer__social-item">
          <uni-cta
            emphasis="low"
            aria-label="Instagram"
            href="https://www.instagram.com/google/"
            icon-id-left="social-instagram" />
        </li>
      
      
        
          
          <li class="uni-footer__social-item">
            <uni-cta
              emphasis="low"
              aria-label="x.com"
              href="https://twitter.com/google"
              icon-id-left="social-x" />
          </li>
        
      
       
        
        <li class="uni-footer__social-item">
          <uni-cta
            emphasis="low"
            aria-label="YouTube"
            href="https://www.youtube.com/google"
            icon-id-left="social-youtube" />
        </li>
      
      
        
          
          <li class="uni-footer__social-item">
            <uni-cta
              emphasis="low"
              aria-label="Facebook"
              href="https://www.facebook.com/Google"
              icon-id-left="social-facebook" />
          </li>
        
       
      
          
        <li class="uni-footer__social-item">
          <uni-cta
            emphasis="low"
            aria-label="LinkedIn"
            href="https://www.linkedin.com/company/google"
            icon-id-left="social-linkedin" />
        </li>
       
      
    </ul>
  
</footer>
        
        

        
        <div id="base-scripts" data-scripts='[
              { "url": "/static/blogv2/js/csp/gtm.js?version=pr20261008-1701",
                "options": {
                  "async": false,
                  "defer": true
                }
              },
              { "url": "/static/keyword/js/all/index.js?version=pr20261008-1701",
                "options": {
                  "async": false,
                  "defer": false
                }
              },
              {
                "url": "https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.js",
                "options": {
                  "async": false,
                  "defer": true
                },
                "attributes": {
                  "data-glue-cookie-notification-bar-category": "2B",
                  "data-glue-cookie-notification-bar-site-id": "blog.google"
                }
              }
            ]'></div>
        <div class="extra-scripts">
          
        
        <div async data-src="https://cdn.ampproject.org/amp-story-player-v0.js" data-id="amp-cdn"></div>
      
        </div>

        

    </body>
</html>
