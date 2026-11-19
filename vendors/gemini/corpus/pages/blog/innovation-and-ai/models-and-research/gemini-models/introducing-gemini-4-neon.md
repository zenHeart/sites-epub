






<!DOCTYPE html>
<html class="no-js glue-flexbox  keyword-blog" lang="en-us" data-locale="en-us" data-version="pr20261117-1738">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <title>Introducing Gemini 4 Neon</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=1.0, minimum-scale=1.0" />
        <meta name="optimize_experiments" content="[]">

        
  




<!--Article Specific Metadata-->
<meta name="description" content="Google introduces Gemini 4 Neon, delivering frontier-level intelligence for complex coding and analysis at a lower cost. See what&#x27;s new."/>
<meta name="keywords" content="None"/>
<meta name="article-author" content="Koray Kavukcuoglu"/>
<meta name="robots" content="max-image-preview:large">

<!--Open Graph Metadata-->
<meta property="og:type" content="article" />
<meta property="og:title" content="Introducing Gemini 4 Neon"/>

<meta property="og:description" content="Today, we’re introducing Gemini 4 Neon" />
<meta property="og:image" content="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__blog-header__sm.width-1300.png" />
<meta property="og:site_name" content="Google" />
<meta property="og:url" content="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/" />
<meta property="article:publisher" content="https://www.facebook.com/Google/" />
<meta property="article:published_time" content="2026-11-18" />

<!--Twitter Card Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:url" content="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/" />
<meta name="twitter:title" content="Introducing Gemini 4 Neon"/>
<meta name="twitter:description" content="Today, we’re introducing Gemini 4 Neon" />
<meta name="twitter:image:src" content="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__blog-header__sm.width-1300.png" />
<meta name="twitter:site" content="@google" />







        
  <meta name="page" content="87021" />
  <meta name="locale" content="en-us" />
  <meta name="published_time" content="2026-11-18T21:00:00+00:00" />
  <meta name="content_type" content="blogv2.articlepage" />
  <meta name="tags" content="Gemini models" />
  <meta name="authors" content="Koray Kavukcuoglu" />



        
        

        
        
  
  
  




        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        


        
        
        <link class="deferred-stylesheet" rel="preload" type="text/css" href="/static/keyword/css/blog/index.min.css?version=pr20261117-1738" as="style">
<noscript>
  <link rel="stylesheet" href="/static/keyword/css/blog/index.min.css?version=pr20261117-1738">
</noscript>

        <link class="deferred-stylesheet" rel="preload" type="text/css" href="https://fonts.googleapis.com/css?family=Google+Sans:400,500,600,700|Google+Sans+Flex:400,500,700|Product+Sans:400&amp;display=swap&amp;lang=en" as="style">
<noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Google+Sans:400,500,600,700|Google+Sans+Flex:400,500,700|Product+Sans:400&amp;display=swap&amp;lang=en">
</noscript>

        <link class="deferred-stylesheet" rel="preload" type="text/css" href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css" as="style">
<noscript>
  <link rel="stylesheet" href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css">
</noscript>


        
        
        

	
        

        
  
            
        
  
  <link rel="stylesheet" type="text/css" href="/static/keyword/css/print/index.min.css?version=pr20261117-1738" media="print" />


        

<link rel="canonical" href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"/>

<link rel="icon" type="image/x-icon" href="/static/blogv2/images/favicon.ico?version=pr20261117-1738">
<link href="/static/blogv2/images/apple-touch-icon.png?version=pr20261117-1738" rel="apple-touch-icon">


  <link rel="alternate" hreflang="x-default" href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">

  <link rel="alternate" hreflang="en-us" href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">

  <link rel="alternate" hreflang="ko-kr" href="https://blog.google/intl/ko-kr/company-news/technology/introducing-gemini-4-neon-kr/">

  <link rel="alternate" hreflang="ja-jp" href="https://blog.google/intl/ja-jp/company-news/technology/introducing-gemini-4-neon/">


        <meta property="gtm-tag" content="GTM-TRV24V">



        <!-- https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API -->


      </head>

    <body class="template-articlepage keyword-blog">
        
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TRV24V" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>


        


<div class="data-layer-init-data" data-ga4-analytics='
  {
    "event": "dataLayer_initialized",
    
      "page_name": "Introducing Gemini 4 Neon",
    
    "experiments": "undefined",
    "locale": "en-us",
    "page_type": "blogv2 | article page",
    "primary_tag": "topics - gemini models",
    "secondary_tags": "undefined",
    
      "landing_page_tags": "undefined",
    
    
      "article_name": "Introducing Gemini 4 Neon",
      "author_name": "Koray Kavukcuoglu",
    
    "publish_date": "2026-11-18|21:00",
    "hero_media": "image",
    
      "special_hero": "undefined",
    
    "days_since_published": "undefined",
    
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#h-burger"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-clear"></use>
</svg>

        </button>
        <!-- Logo -->
        
        
          <a href="/" class="uni-nav__logo" aria-label="News from Google" title="News from Google">
            <svg
  
  
  
  
  
  
  role="img"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#news-from-google-logo"></use>
</svg>

            <!-- SuperG Logo -->
            <img class="uni-nav__logo--super-g" src="/static/blogv2/images/super-g-aurora.svg?version=pr20261117-1738" alt="" width="30" height="30" aria-hidden="true">
          </a>
        
        
          <p class="uni-nav-article__article-title font-body-m">Introducing Gemini 4 Neon</p>
        
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#arrow_outward"></use>
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
  <div class="uni-article-progress-bar__title uni-article-progress-bar__ellipsis">Introducing Gemini 4 Neon</div>
  <div class="uni-article-progress-bar__social"
    data-analytics-module='{
      "module_name": "Progress Bar",
      "section_header": "Introducing Gemini 4 Neon"
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-share"></use>
</svg>

    <div class="uni-social-share__button">Share</div>
  </a>
  <div class="uni-social-share__dialog uni-social-share__content " aria-labelledby="social-share-icon">
    


<a aria-label="Share on X"
    class="article-share__link-text uni-click-tracker"
    href="https://twitter.com/intent/tweet?text=Introducing%20Gemini%204%20Neon%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
    target="_blank"
    data-ga4-method="twitter">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-x"></use>
</svg>

  <div class="article-share__title">x.com</div>
</a>

<a aria-label="Share on Facebook"
    class="article-share__link-text uni-click-tracker"
    href="https://www.facebook.com/sharer/sharer.php?caption=Introducing%20Gemini%204%20Neon&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
    target="_blank"
    data-ga4-method="facebook">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-facebook"></use>
</svg>

  <div class="article-share__title">Facebook</div>
</a>

<a aria-label="Share on LinkedIn"
    class="article-share__link-text uni-click-tracker"
    href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/&title=Introducing%20Gemini%204%20Neon"
    target="_blank"
    data-ga4-method="linkedin">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-linkedin"></use>
</svg>

  <div class="article-share__title">LinkedIn</div>
</a>

<a aria-label="Share with Email"
    class="article-share__link-text uni-click-tracker article-share__email"
    
      href="mailto:?subject=Introducing%20Gemini%204%20Neon&body=Check out this article on the Keyword:%0A%0AIntroducing%20Gemini%204%20Neon%0A%0AToday, we’re introducing Gemini 4 Neon%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
    
    target="_blank"
    data-ga4-method="email">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-mail"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-link"></use>
</svg>

    <div class="copy-link__title">Copy link</div>
  </button>
  <div class="copy-link__dialog copy-link__content" uni-options='{"copyTextButton": "Copied"}' aria-hidden="true" tabindex="-1">
    <input class="h-c-copy copy-link__url" value="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/" id="copy-link" readonly="readonly" type="text"/>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-more-vert"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#language"></use>
</svg>

            


  <div data-component="uni-lang-picker" class="uni-lang-picker">
    <select
      name="language-picker"
      class="uni-lang-picker__select font-ctas uni-lang-picker--inside-menu"
      aria-label="Change Region">
      
      <option
        label="Global (English)"
        value="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
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
        value="https://blog.google/intl/ja-jp/company-news/technology/introducing-gemini-4-neon/"
        lang="ja-jp"
        class="uni-lang-picker__option"
        >
        日本 (日本語)
      </option>
      
      <option
        label="대한민국 (한국어)"
        value="https://blog.google/intl/ko-kr/company-news/technology/introducing-gemini-4-neon-kr/"
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#expand_more"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#photo-library"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#rss-feed"></use>
</svg>
RSS feed</a>
        </li>
      </ul>
    </div>
  </div>

  <!-- Share Dropdown Menu -->
  
  <div class="uni-share-dropdown" data-component="uni-share-dropdown" data-analytics-module='{
         "module_name": "Progress Bar",
         "section_header": "Introducing Gemini 4 Neon"
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#share"></use>
</svg>

    </button>
    <div id="header-share-dropdown" class="uni-share-dropdown__menu " aria-hidden="true">
  <div class="uni-share-dropdown__menu-inner">
    <ul class="uni-share-dropdown__menu-link-list uni-social-share">
      


<li>
  <a aria-label="Share on X"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://twitter.com/intent/tweet?text=Introducing%20Gemini%204%20Neon%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
      target="_blank"
      data-ga4-method="twitter">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-x"></use>
</svg>

    <span>x.com</span>
  </a>
</li>

<li>
  <a aria-label="Share on Facebook"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.facebook.com/sharer/sharer.php?caption=Introducing%20Gemini%204%20Neon&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
      target="_blank"
      data-ga4-method="facebook">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-facebook"></use>
</svg>

    <span>Facebook</span>
  </a>
</li>

<li>
  <a aria-label="Share on LinkedIn"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/&title=Introducing%20Gemini%204%20Neon"
      target="_blank"
      data-ga4-method="linkedin">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-linkedin"></use>
</svg>

    <span>LinkedIn</span>
  </a>
</li>

<li>
  <a aria-label="Share with Email"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      
        href="mailto:?subject=Introducing%20Gemini%204%20Neon&body=Check out this article on the Keyword:%0A%0AIntroducing%20Gemini%204%20Neon%0A%0AToday, we’re introducing Gemini 4 Neon%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
      
      target="_blank"
      data-ga4-method="email">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-mail"></use>
</svg>

    <span>Mail</span>
  </a>
</li>

<li data-component="uni-copy-popup-component">
  <button aria-label="Copy link"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker uni-copy-share"
      data-ga4-analytics-share-copy-link
      data-ga4-method="Copy link"
      data-copy-text="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-link"></use>
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
    "section_header": "Introducing Gemini 4 Neon"
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#uni-icon-chevron-right"></use>
</svg>

    </button>
    <div class="uni-breadcrumb__focusable uni-breadcrumb__focusable--start"></div>
    <nav aria-label="Breadcrumb" class="breadcrumb uni-breadcrumb__scrollable">
      <span class="uni-breadcrumb__label">Breadcrumb</span>
      <ol data-analytics-module='{
        "module_name": "breadcrumbs",
        "section_header": "Introducing Gemini 4 Neon"
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#uni-icon-chevron-right"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#uni-icon-chevron-right"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#uni-icon-chevron-right"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#uni-icon-chevron-right"></use>
</svg>

    </button>
  </uni-breadcrumbs>


          </div>
        
      </div>
      
      <div class="uni-grid uni-article-hero__content-grid">
        <div class="uni-grid__col--span-4 uni-grid__col--span-12-tablet uni-grid__col--span-8-desktop uni-grid__col--start-3-desktop uni-article-hero__main-content">
          <h1 class="uni-article-hero__title font-h1">Introducing Gemini 4 Neon</h1>

          <div class="uni-article-hero__meta-wrapper">
            <div class="uni-article-hero__meta-header">
              
              <div class="uni-article-hero__meta-aside">
                
                  <p class="uni-article-hero__date font-body-s">Nov 18, 2026</p>
                
                
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
      href="https://twitter.com/intent/tweet?text=Introducing%20Gemini%204%20Neon%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
      target="_blank"
      data-ga4-method="twitter">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-x"></use>
</svg>

    <span>x.com</span>
  </a>
</li>

<li>
  <a aria-label="Share on Facebook"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.facebook.com/sharer/sharer.php?caption=Introducing%20Gemini%204%20Neon&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
      target="_blank"
      data-ga4-method="facebook">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-facebook"></use>
</svg>

    <span>Facebook</span>
  </a>
</li>

<li>
  <a aria-label="Share on LinkedIn"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/&title=Introducing%20Gemini%204%20Neon"
      target="_blank"
      data-ga4-method="linkedin">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-linkedin"></use>
</svg>

    <span>LinkedIn</span>
  </a>
</li>

<li>
  <a aria-label="Share with Email"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      
        href="mailto:?subject=Introducing%20Gemini%204%20Neon&body=Check out this article on the Keyword:%0A%0AIntroducing%20Gemini%204%20Neon%0A%0AToday, we’re introducing Gemini 4 Neon%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
      
      target="_blank"
      data-ga4-method="email">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-mail"></use>
</svg>

    <span>Mail</span>
  </a>
</li>

<li data-component="uni-copy-popup-component">
  <button aria-label="Copy link"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker uni-copy-share"
      data-ga4-analytics-share-copy-link
      data-ga4-method="Copy link"
      data-copy-text="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-link"></use>
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
                Bringing frontier-level intelligence with fast end-to-end task completion  across complex software engineering, knowledge work, and science workflows.
              </p>
            
          </div>

          <hr class="uni-article-hero__divider">

          
          <div class="uni-article-hero__authors-actions">
            <div class="uni-article-hero__authors-wrapper">
              
                

<div class="uni-article-hero__authors uni-grid">
  
    
    <div class="uni-article-hero__author uni-article-hero__author--one-author">
      <div class="uni-article-hero__author-info">
        
          
          <a href="https://blog.google/authors/koray-kavukcuoglu/" class="uni-article-hero__author-link">
        
            <p class="uni-article-hero__author-name font-author-name">Koray Kavukcuoglu</p>
            
              
                <p class="uni-article-hero__author-title font-author-info">SVP, Google DeepMind and Chief AI Architect, Google</p>
              
            
        
          </a>
        
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
      href="https://twitter.com/intent/tweet?text=Introducing%20Gemini%204%20Neon%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
      target="_blank"
      data-ga4-method="twitter">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-x"></use>
</svg>

    <span>x.com</span>
  </a>
</li>

<li>
  <a aria-label="Share on Facebook"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.facebook.com/sharer/sharer.php?caption=Introducing%20Gemini%204%20Neon&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
      target="_blank"
      data-ga4-method="facebook">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-facebook"></use>
</svg>

    <span>Facebook</span>
  </a>
</li>

<li>
  <a aria-label="Share on LinkedIn"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/&title=Introducing%20Gemini%204%20Neon"
      target="_blank"
      data-ga4-method="linkedin">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-linkedin"></use>
</svg>

    <span>LinkedIn</span>
  </a>
</li>

<li>
  <a aria-label="Share with Email"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      
        href="mailto:?subject=Introducing%20Gemini%204%20Neon&body=Check out this article on the Keyword:%0A%0AIntroducing%20Gemini%204%20Neon%0A%0AToday, we’re introducing Gemini 4 Neon%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
      
      target="_blank"
      data-ga4-method="email">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-mail"></use>
</svg>

    <span>Mail</span>
  </a>
</li>

<li data-component="uni-copy-popup-component">
  <button aria-label="Copy link"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker uni-copy-share"
      data-ga4-analytics-share-copy-link
      data-ga4-method="Copy link"
      data-copy-text="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#social-link"></use>
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
            alt="hero image for Gemini 4 Neon"
            class="uni-article-hero__image uni-progressive-image--blur"
            data-component="uni-progressive-image"
            fetchpriority="high"
            src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__blog-header__sm.width-200.format-webp.webp"
            
              data-sizes="(max-width: 1023px) 100vw, (max-width: 1440px) 95vw, 1408px"
              data-srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__blog-header__sm.width-450.format-webp.webp 450w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__blog-header__sm.width-900.format-webp.webp 900w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__blog-header__sm.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__blog-header__sm.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__blog-header__sm.width-2200.format-webp.webp 2200w"
            
            >
        </div>
      </div>
      
    </div>
  





      
    </div>
  </div>
</section>

    <div class="uni-page uni-grid article-container__ai-box-container">
      <div class="article-container__ai-box uni-grid__col--layout-6">
        
  



















<!-- Workaround for Safari: Safari fails to resolve linear gradients defined in external SVG sprites when referenced via <use>. Inlining them here makes them available in the DOM for the page. -->
<svg width="0" height="0" style="position: absolute;" aria-hidden="true">
  <defs>
    <linearGradient id="paint0_linear_7609_9483" x1="7.46937" y1="15.5133" x2="18.3261" y2="6.3599" gradientUnits="userSpaceOnUse">
      <stop stop-color="#346BF1"/>
      <stop offset="0.371606" stop-color="#3186FF"/>
      <stop offset="0.776981" stop-color="#4FA0FF"/>
    </linearGradient>
    <linearGradient id="paint0_linear_7609_3755" x1="7.46937" y1="15.5133" x2="18.3261" y2="6.3599" gradientUnits="userSpaceOnUse">
      <stop stop-color="#346BF1"/>
      <stop offset="0.371606" stop-color="#3186FF"/>
      <stop offset="0.776981" stop-color="#4FA0FF"/>
    </linearGradient>
    <linearGradient id="paint0_linear_7609_9494" x1="-0.439716" y1="13.1229" x2="23.5291" y2="7.60707" gradientUnits="userSpaceOnUse">
      <stop stop-color="#3186FF"/>
      <stop offset="0.45" stop-color="#346BF1"/>
      <stop offset="0.95" stop-color="#4FA0FF"/>
    </linearGradient>
  </defs>
</svg>

<div class="audio-player-tts"
     data-component="uni-audio-player-tts"
     uni-l10n='{
       "stop": "Pause article audio description",
       "play": "Play article audio description",
       "progress": "Current audio progress minutes with seconds: [[progress]]",
       "duration": "Duration of the audio minutes with seconds: [[duration]]",
       "settings": "Click for settings",
       "timeText": "[[duration]] minutes"
     }'
     data-analytics-module='{
      "module_name": "Audio TTS",
      "section_header": "Introducing Gemini 4 Neon"
     }'
     data-tts-audios='[
      
        {"voice_name": "Umbriel",
        "voice_source": "https://storage.googleapis.com/gweb-uniblog-publish-prod/media/tts_audio_87021_umbriel_2026_11_18_23_01_11.mp3",
        "mimetype": "audio/mpeg"},
      
        {"voice_name": "Gacrux",
        "voice_source": "https://storage.googleapis.com/gweb-uniblog-publish-prod/media/tts_audio_87021_gacrux_2026_11_18_23_01_23.mp3",
        "mimetype": "audio/mpeg"}
      ]'>
  <audio
    class="audio-player-tts__player"
    title="Introducing Gemini 4 Neon">
      <source
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/media/tts_audio_87021_umbriel_2026_11_18_23_01_11.mp3"
        type="audio/mpeg" />
      <p>Your browser does not support the audio element.</p>
  </audio>
  <div class="audio-player-tts__container"  aria-label="">
    <div class="audio-player-tts__content">
      <button class="audio-player-tts__preview-play" aria-label="Play article audio description">
        <svg
  
  class="audio-player-tts__play-icon"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#play-gd"></use>
</svg>

      </button>
      <div class="audio-player-tts__text-content">
        <span class="audio-player-tts__text-content--title font-ctas">
          Listen to article
        </span>
        <div class="audio-player-tts__duration font-caption">[[duration]] minutes</div>
        <span class="audio-player-tts__disclaimer" tabindex="0" role="tooltip" aria-label="This content is generated by Google AI. Generative AI is experimental">
          <div class="audio-player-tts__disclaimer--copy font-body-s">This content is generated by Google AI. Generative AI is experimental</div>
          <svg
  
  class="audio-player-tts__disclaimer--icon"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#ttf-info"></use>
</svg>

        </span>
      </div>
      <button class="audio-player-tts__pause" aria-label="Pause article audio description">
        <svg
  
  class="audio-player-tts__icon-play"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#play-gd"></use>
</svg>

        <svg
  
  class="audio-player-tts__icon-pause audio-player-tts__icon-pause--hidden"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#pause-gd"></use>
</svg>

      </button>
      <div class="audio-player-tts__console">
        <div class="audio-player-tts__time-bar">
          <span class="audio-player-tts__current-time font-body-s"></span>
          <div class="audio-player-tts__timeline-slider-container">
            <input type="range" class="timeline__slider" max="100" value="0" step="5" aria-valuetext="Audio Slider" aria-label="Audio Slider" tabindex="0" role="slider">
          </div>
          <span class="audio-player-tts__duration-time font-body-s"></span>
        </div>
        <button class="audio-player-tts__audio-settings" aria-label="Click for settings">
          <svg
  
  class="icon audio-player-tts__audio-settings--icon"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#ttf-settings"></use>
</svg>

        </button>
        <div class="audio-player-tts__settings-container">
          <div class="audio-player-tts__settings--main uni-cta-text">
            <button class="audio-player-tts__settings--current-voice" aria-label="Click to change voice">
              <span class="audio-player-tts__settings--current-voice-info">
                <svg
  
  class="audio-player-tts__settings--current-voice-icon"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#tts-voice"></use>
</svg>

                <span>Voice</span>
              </span>
              <span class="audio-player-tts__settings--current-voice-next">
                <span class="audio-player-tts__settings--current-voice-text font-body-s" ></span>
                <svg
  
  class="icon tts-chevron"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#tts-chevron"></use>
</svg>

              </span>
            </button>
            <button class="audio-player-tts__settings--current-speed" aria-label="Click to change speed">
              <span class="audio-player-tts__settings--current-speed-info">
                  <svg
  
  class="audio-player-tts__settings--current-speed-icon"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#tts-speed"></use>
</svg>

                  <span>Speed</span>
                </span>
                <span class="audio-player-tts__settings--current-speed-next">
                  <span class="audio-player-tts__settings--current-speed-text font-body-s"></span>
                  <svg
  
  class="icon tts-chevron"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#tts-chevron"></use>
</svg>

                </span>
            </button>
          </div>
          <div class="audio-player-tts__settings--voices uni-cta-text">
            <button class="audio-player-tts__settings-back" aria-label="Click to go back"><svg
  
  class="icon tts-chevron"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#tts-chevron"></use>
</svg>
 <span>Voice</span></button>
          </div>
          <div class="audio-player-tts__settings--speeds uni-cta-text">
            <button class="audio-player-tts__settings-back" aria-label="Click to go back"><svg
  
  class="icon tts-chevron"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#tts-chevron"></use>
</svg>
 <span>Speed</span></button>
            <button class="audio-player-tts__settings-option" data-speed="0.75" aria-label="speed 0.75X"><span>0.75X</span></button>
            <button class="audio-player-tts__settings-option audio-player-tts__settings-option--selected" data-speed="1" aria-label="speed 1X"><span>1X</span></button>
            <button class="audio-player-tts__settings-option" data-speed="1.5" aria-label="speed 1.5X"><span>1.5X</span></button>
            <button class="audio-player-tts__settings-option" data-speed="2" aria-label="speed 2X"><span>2X</span></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>


        
          
        
      </div>
    </div>
    
    <section class="uni-container article-container">
      
        
          <div class="article-sidebar article-sidebar--desktop" data-component="uni-article-sidebar">
            
              
              

<div class="uni-page uni-grid uni-article-jumplinks__layout">
  <uni-article-jumplinks
    class="uni-article-jumplinks uni-grid__col--span-12 uni-grid__col--span-2-desktop"
    heading="In this article"
    data-analytics-module='{
      "module_name": "Article Jumplinks",
      "section_header": "Introducing Gemini 4 Neon"
    }'>
    <details class="uni-article-jumplinks__wrapper" open>
      <summary class="uni-article-jumplinks__toggle font-eyebrow">
        <span>In this article</span>
        <svg
  
  class="icon"
  
  
  height="24"
  
  role="presentation"
  aria-hidden="true"
  
  
  width="24"
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#mi-expand"></use>
</svg>

      </summary>
      <hr
        class="uni-article-jumplinks__divider"
        aria-hidden="true"
        role="presentation" />
      <nav aria-label="In this article">
        <ul class="uni-article-jumplinks__list">
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#gemini-4-neon"
              data-component="uni-article-jumplink">
              Gemini 4 Neon is available
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#delivers"
              data-component="uni-article-jumplink">
              Delivers across enterprise, analytical, and scientific work
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#production-ready-code"
              data-component="uni-article-jumplink">
              Built for production-ready code
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#efficiency"
              data-component="uni-article-jumplink">
              Brings efficiency and control to production-grade workflows
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#cyber-defense"
              data-component="uni-article-jumplink">
              Built for fast, efficient, frontier-level cyber defense
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#safe-dependable-execution"
              data-component="uni-article-jumplink">
              Designed for safe, dependable execution
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#analysis"
              data-component="uni-article-jumplink">
              Built for deeper analysis
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#building-gemini-4-neon"
              data-component="uni-article-jumplink">
              Start building with Gemini 4 Neon today
            </a>
          </li>
          
        </ul>
      </nav>
    </details>
  </uni-article-jumplinks>
</div>

            
            
              
            
          </div>
        
        
        <div class="uni-content uni-blog-article-container article-container__content"
            data-reading-time="true"
            data-component="uni-article-body">

          
          
<!--article text-->

  
    <div class="uni-page uni-grid">
  <section
    id="gemini-4-neon"
    aria-label="Gemini 4 Neon is available"
    class="
      uni-article-jumplinks__section
      uni-grid__col--layout-6
      
      "
    
    tabindex="-1">
    
  </section>
</div>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="039sd">Today, we’re introducing Gemini 4 Neon — bringing frontier-level intelligence with fast end-to-end task completion across complex software engineering, knowledge work, and science workflows.</p><p data-block-key="2a44q">Neon ranks ahead of comparable models and #3 overall with a score of 61 on the <a href="https://artificialanalysis.ai/">Artificial Analysis Intelligence Index</a> at its xhigh thinking level, landing just behind larger, slower models. On the <a href="https://www.vals.ai/benchmarks/vals_index">Vals Index</a>, Neon ranks #2 and lands on the Pareto frontier. Beyond just pushing on raw model capability, we’re continuing to make our models better to work with, Neon ranks #2 on steerability (adapting cleanly to mid-task user corrections) on the new <a href="https://arena.ai/leaderboard/agent?utm_source=social&amp;utm_medium=x&amp;utm_campaign=lbreboot&amp;utm_content=announcement">Agent Arena Index</a>. Neon also excels at multi-step instruction following and builds on our ongoing progress to curb fabrication, recording our lowest fabrication rate yet in internal Google Antigravity testing.</p><p data-block-key="fphaa">The model is priced at $3 per million input tokens ($0.15 per million cached input tokens, a 95% discount) and $15 per million output tokens, with a 1 million-token context window.</p><p data-block-key="7fegl">Gemini 4 Neon is rolling out today in the Gemini API in <a href="https://aistudio.google.com/prompts/new_chat?model=gemini-4-neon">Google AI Studio</a>, <a href="https://cloud.google.com/gemini-enterprise">Gemini for business</a> (via API and model dropdown), for paid Google AI Pro and Ultra subscribers in <a href="https://antigravity.google/">Google Antigravity</a>, and for Pro and Ultra subscribers in the <a href="http://gemini.google/">Gemini app</a>.</p></div>
  </uni-article-paragraph>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="delivers"
    aria-label="Delivers across enterprise, analytical, and scientific work"
    class="
      uni-article-jumplinks__section
      uni-grid__col--layout-6
      
      "
    
    tabindex="-1">
    
  </section>
</div>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="a8po7">Delivers across enterprise, analytical, and scientific work</h2><p data-block-key="oret">Enterprise work lives in spreadsheets, PDFs, charts, audio, and video. Neon can synthesize across all of these inputs in a single 1 million-token context window and turns inputs into structured deliverables. Independent evaluations rank Neon as one of the top models and on benchmarks like the <a href="https://www.vals.ai/benchmarks/vals_index">Vals Index</a>, it ranks #2 (70.9%), and reaches #1 on both the <a href="https://www.vals.ai/benchmarks/legal_research">Legal Research Bench</a> and <a href="https://www.vals.ai/benchmarks/tax_agent_bench">Tax Agent Bench</a>.</p><p data-block-key="delvn">Neon also shows strong wins across categories on <a href="https://surgehq.ai/benchmarks">Surge AI</a>, ranking #1 on most benchmarks across finance, accounting, spreadsheet modeling, and complex constraint following. It also scores 73.5% on Chartography for reading dense professional charts and performs on par with leading models on<a href="https://agents-last-exam.org/leaderboard"> Agents' Last Exam v1.1</a> (75.8%). It achieves #1 overall on both Zapier’s <a href="https://zapier.com/benchmarks">AutomationBench</a> (56.3%) and <a href="https://andonlabs.com/evals/vending-bench-2">Andon Labs' Vending-Bench 2</a> ($16,843), a long-horizon simulation of running a business. Finally, it debuts #2 globally with a score of 1336 on <a href="https://arena.ai/leaderboard/agent">Arena's new Agent Arena Index</a> across 4,200+ real-world agent sessions.</p><p data-block-key="9psru">On scientific and mathematical reasoning, spanning quantitative analysis, mathematics, and technical research problems, Neon is best in class on<a href="https://www.terminal-bench-science.ai/"> Terminal-Bench Science</a> (70.5%), <a href="https://arxiv.org/abs/2604.06802">RiemannBench</a> (84.0%), and <a href="https://lastexam.ai/blog/hle-diamond">HLE-Diamond</a> (71.3%).</p></div>
  </uni-article-paragraph>
</section>

  

  
    





  
  
  
  
  

























<section class="uni-page uni-grid uni-inline-image-section" data-component="uni-inline-image">
  <uni-inline-image
    class="uni-inline-image uni-inline-image--full"
    alignment="full"
    alt-text="a benchmark table"
    external-image=""
    or-mp4-video-title=""
    or-mp4-video-url=""
    section-header="Introducing Gemini 4 Neon"
    
    
    
    
    
    
      autoplay="true"
    
  >
    

    
      <div slot="image-slot">
        <img
          alt="a benchmark table"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_table.width-1200.format-webp.webp"
          
            loading="lazy"
            sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
            srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_table.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_table.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_table.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_table.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_table.width-2000.format-webp.webp 2000w"
          
        >
      </div>
    
  </uni-inline-image>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Introducing Gemini 4 Neon"
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
    







<uni-quote-media-carousel
  data-analytics-module='{
    "module_name": "Media Carousel/Block Quote",
    "section_header": "Introducing Gemini 4 Neon"
  }'
  quote="Gemini 4 Neon helps turn scattered information into clear, grounded answers. It delivers a compelling balance of quality, cost, and speed to day-to-day workplace tasks. In our early evaluations, it matched or exceeded Gemini 4 Carbon on overall quality at 3x the speed and 60% of the cost. We’re excited to bring these capabilities to Glean customers tackling multi-step work that demands accuracy, detail, and speed."
  
    author-name="Thai Tran"
  
  
    author-title="AI Product Lead, Glean"
  
>
</uni-quote-media-carousel>

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
    







<uni-quote-media-carousel
  data-analytics-module='{
    "module_name": "Media Carousel/Block Quote",
    "section_header": "Introducing Gemini 4 Neon"
  }'
  quote="Across our evaluations, we observed Gemini 4 Neon performing at the top of the leaderboard on our Medical Index and internal life sciences benchmark, while maintaining strong cost-efficiency and meaningful speed."
  
    author-name="Brandon Valafar"
  
  
    author-title="Strategic AI Lead, Micro1"
  
>
</uni-quote-media-carousel>

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
    







<uni-quote-media-carousel
  data-analytics-module='{
    "module_name": "Media Carousel/Block Quote",
    "section_header": "Introducing Gemini 4 Neon"
  }'
  quote="Neon is significantly more thorough and careful than other Gemini models we have tested. Neon does well on exploring large code bases and getting an understanding of complex architectures quickly. In our cyber evals, Neon was able to find several subtle vulnerabilities other models missed while using a fraction of the tokens. We think Neon is a very good model for cost-efficient exploration and research tasks."
  
    author-name="Karina Nguyen"
  
  
    author-title="Founder, Thoughtful Lab"
  
>
</uni-quote-media-carousel>

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
    







<uni-quote-media-carousel
  data-analytics-module='{
    "module_name": "Media Carousel/Block Quote",
    "section_header": "Introducing Gemini 4 Neon"
  }'
  quote="A novice researcher runs whatever experiment you give it. A great researcher keeps asking why. Gemini 4 Neon is the first model that feels like the latter. It keeps exploring: hunting for new data and imagining new signals to extract to train better models. It&#x27;s the first model we&#x27;ve seen that pushes itself to do better without a human watching: instead of giving up in the face of bad results, Neon redesigns its modeling strategies to achieve better results."
  
    author-name="Trenton Chang"
  
  
    author-title="Chief Scientist, Quadrillion"
  
>
</uni-quote-media-carousel>

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
    







<uni-quote-media-carousel
  data-analytics-module='{
    "module_name": "Media Carousel/Block Quote",
    "section_header": "Introducing Gemini 4 Neon"
  }'
  quote="Gemini 4 Neon is an INCREDIBLE partner in ML engineering, data engineering, experiment management, and architecture design. It takes feedback, is thorough, tests hypotheses, understands prior art, and generally makes the process of AI model development easier."
  
    author-name="Andrew Carr"
  
  
    author-title="Chief Scientist and Co-Founder, Cartwheel"
  
>
</uni-quote-media-carousel>

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
  

  
    <div class="uni-page uni-grid">
  <section
    id="production-ready-code"
    aria-label="Built for production-ready code"
    class="
      uni-article-jumplinks__section
      uni-grid__col--layout-6
      
      "
    
    tabindex="-1">
    
  </section>
</div>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="cnuug">Built for production-ready code</h2></div>
  </uni-article-paragraph>
</section>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="a8po7">Engineered for long-running agent workflows, Neon sustains performance through complex, tool-heavy tasks end-to-end — whether running standalone or acting as a fast, high-judgment Orchestrator directing parallel Hydrogen subagents in Google Antigravity. It cuts down on redundant file reads, shares progress as it works, and handles context compaction reliably in long sessions.</p><p data-block-key="dn9c8">Across core developer and researcher workflows, Neon achieves frontier performance and is competitive with the leading models in its class, ranking #1 overall on the <a href="https://artificialanalysis.ai/agents/coding-agents#coding-agents-index">Artificial Analysis Coding Agent Index</a> (58.6), with a score of 65.2% on <a href="https://www.tbench.ai/">Terminal-Bench 4.1</a> and<a href="https://cognition.com/blog/frontier-code-2.0"> 46.2% (at its default high setting) on FrontierCode 2.0</a>. For production-ready code, Neon handles multi-file debugging and refactoring across repositories with targeted, surgical edits. On SWE-sweep, it already leads on the mini-SWE harness (12.8%) and more than triples to a state-of-the-art 39.0% in Google Antigravity showing what the Antigravity harness unlocks.</p></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Introducing Gemini 4 Neon"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header="Driving Blender MCP in Google Antigravity, Gemini 4 Neon used /swarm to build a photorealistic 3D lab bench visualizing the model names with elemental accuracy pairing Bunsen flames for Gemini 4 Carbon and Gemini 4 Hydrogen with high-voltage gas discharge tubes for Gemini 4 Argon and Neon."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Introducing Gemini 4 Neon"
    }'
    index="1"
    thumbnail-alt="A YouTube video with Gemini 4 Neon building a photorealistic 3D lab"
    video-id="xW3OcKd1G5E"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="twfa4">Driving Blender MCP in Google Antigravity, Gemini 4 Neon used /swarm to build a photorealistic 3D lab bench visualizing the model names with elemental accuracy pairing Bunsen flames for Gemini 4 Carbon and Gemini 4 Hydrogen with high-voltage gas discharge tubes for Gemini 4 Argon and Neon.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header="In Google Antigravity, Gemini 4 Neon wrote a first-person WebGL2 freeride ski simulator from scratch on real Mont Blanc and Chamonix elevation terrain — combining 10,200 lines of custom shaders, 120 Hz ski physics across six alpine lines, dynamic carved tracks, slab avalanches, and spatial Web Audio with zero pre-made assets."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Introducing Gemini 4 Neon"
    }'
    index="2"
    thumbnail-alt="A YouTube video featuring Gemini 4 Neon"
    video-id="xhG-jNObuz4"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="dwq7b">In Google Antigravity, Gemini 4 Neon wrote a first-person WebGL2 freeride ski simulator from scratch on real Mont Blanc and Chamonix elevation terrain — combining 10,200 lines of custom shaders, 120 Hz ski physics across six alpine lines, dynamic carved tracks, slab avalanches, and spatial Web Audio with zero pre-made assets.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="2"
  accordion-header="Using /swarm in Google Antigravity, Gemini 4 Neon pulled archival photos to recreate Alan Turing’s 1936 study at King’s College, Cambridge in interactive 3D — from King’s Chapel outside to Room X.8 inside, complete with a working Universal Turing Machine running on his desk."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Introducing Gemini 4 Neon"
    }'
    index="3"
    thumbnail-alt="A YouTube video featuring Gemini 4 Neon recreating Alan Turing&#x27;s 1936 study"
    video-id="KgLLa4WhMSo"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="jxp6m">Using /swarm in Google Antigravity, Gemini 4 Neon pulled archival photos to recreate Alan Turing’s 1936 study at King’s College, Cambridge in interactive 3D — from King’s Chapel outside to Room X.8 inside, complete with a working Universal Turing Machine running on his desk.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="3"
  accordion-header="In Google Antigravity, a Gemini 4 Neon agent swarm turned a single image into a 100,000-cell Google Sheet with zero embedded images and zero Apps Script — using over 500,000 live spreadsheet formulas to run edge detection, map 3D depth, and relight the scene across six interactive modes."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Introducing Gemini 4 Neon"
    }'
    index="4"
    thumbnail-alt="A YouTube video featuring Gemini 4 Neon turning a single image into a Google sheet"
    video-id="vPsBbuz9IbE"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="jxp6m">In Google Antigravity, a Gemini 4 Neon agent swarm turned a single image into a 100,000-cell Google Sheet with zero embedded images and zero Apps Script — using over 500,000 live spreadsheet formulas to run edge detection, map 3D depth, and relight the scene across six interactive modes.</p></div>
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
  

  
    <div class="uni-page uni-grid">
  <section
    id="efficiency"
    aria-label="Brings efficiency and control to production-grade workflows"
    class="
      uni-article-jumplinks__section
      uni-grid__col--layout-6
      
      "
    
    tabindex="-1">
    
  </section>
</div>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="g0alw">Brings efficiency and control to production-grade workflows</h2><p data-block-key="872sd">We’re refining thinking levels with each new model release to give teams finer control and a smoother progression from one tier to the next. Neon’s four levels scale steadily, letting teams dial intelligence and token spend to what each workload needs.</p><p data-block-key="2mbsa">Neon delivers high performance at a lower cost per task across third-party benchmarks. At its default high thinking level, it pairs a high Artificial Analysis Intelligence Index score with a 32% lower cost per task than Carbon. It also sits on the Pareto frontier on both the Vals index and Agent Arena at high, with roughly 50% to 80% lower cost per task than top competing frontier models. xhigh thinking adds deeper, multi-step reasoning for the hardest engineering, analytical, and scientific workloads. Neon shows its highest intelligence score here, while still costing 36%+ less per task than competing models at their highest setting.</p></div>
  </uni-article-paragraph>
</section>

  

  
    





  
  
  
  
  

























<section class="uni-page uni-grid uni-inline-image-section" data-component="uni-inline-image">
  <uni-inline-image
    class="uni-inline-image uni-inline-image--full"
    alignment="full"
    alt-text="a chart showing AA Index v5.01 cost per task"
    external-image=""
    or-mp4-video-title=""
    or-mp4-video-url=""
    section-header="Introducing Gemini 4 Neon"
    
    
    
    
    
    
      autoplay="true"
    
  >
    

    
      <div slot="image-slot">
        <img
          alt="a chart showing AA Index v5.01 cost per task"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon__benchmarks__aa-in.width-1200.format-webp.webp"
          
            loading="lazy"
            sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
            srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon__benchmarks__aa-ind.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon__benchmarks__aa-ind.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon__benchmarks__aa-in.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon__benchmarks__aa-in.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon__benchmarks__aa-in.width-2000.format-webp.webp 2000w"
          
        >
      </div>
    
  </uni-inline-image>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="cyber-defense"
    aria-label="Built for fast, efficient, frontier-level cyber defense"
    class="
      uni-article-jumplinks__section
      uni-grid__col--layout-6
      
      "
    
    tabindex="-1">
    
  </section>
</div>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="a8po7">Built for fast, efficient, frontier-level cyber defense</h2><p data-block-key="d105m">As agentic coding scales, generating secure code from the start is critical. Gemini 4 Neon for cyber produces more secure code than Carbon across all easy, medium, and hard challenges on <a href="https://baxbench.com/autobaxbuilder/">AutoBaxBench</a>, achieving state-of-the-art on the hard tier (76%).</p><p data-block-key="fvd46">Securing systems also means proactively finding flaws before attackers do. Penetration testing has served as a cornerstone of enterprise cybersecurity. On <a href="https://agentcyberrange.io/">WebExploitBench v1.2</a>, Neon is state-of-the-art (51.26%) at half the cost of competing large models.</p><p data-block-key="2nspu">To fortify existing code, Neon for cyber delivers frontier-level performance across the code hardening lifecycle — vulnerability finding, validating, and patching — all while being faster and more cost efficient than large frontier models.</p><ul><li data-block-key="9khl8"><b>Finding code vulnerabilities:</b> Neon achieves state-of-the-art performance on <a href="https://sec-bench.github.io/">SEC-bench Pro</a> (90.5%), while costing roughly half as much per challenge.</li><li data-block-key="f2vk0"><b>Validating risk through exploitation:</b> To prioritize which vulnerabilities to remediate, defenders rely on models to check which vulnerabilities are exploitable. On ExploitGym, it achieves frontier-level performance using half the tokens of Carbon.</li><li data-block-key="9of67"><b>Patching vulnerabilities:</b> Fixing the root cause of vulnerabilities is a critical step in the cybersecurity defense lifecycle. Neon reaches 70.7% on Collinear’s<a href="https://cwe-bench.com/v2"> CWE-bench v2</a>, driving a 3.4% uplift over Carbon.</li></ul></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Introducing Gemini 4 Neon"
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
    "section_header": "Introducing Gemini 4 Neon"
  }'
  or-mp4-video-url=""
  section-header="Introducing Gemini 4 Neon"
  alt-text="Autobaxbench chart"
  video-title=""
  
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="Autobaxbench chart"
        loading="lazy"
        
          sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
          srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_autobax_bench.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_autobax_bench.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_autobax_bench.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_autobax_bench.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_autobax_bench.width-2000.format-webp.webp 2000w"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_autobax_bench.width-1200.format-webp.webp"
        
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
    "section_header": "Introducing Gemini 4 Neon"
  }'
  or-mp4-video-url=""
  section-header="Introducing Gemini 4 Neon"
  alt-text="webexploitbench chart"
  video-title=""
  
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="webexploitbench chart"
        loading="lazy"
        
          sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
          srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_webexploitbench.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_webexploitbench.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_webexploitbench.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_webexploitbench.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_webexploitbench.width-2000.format-webp.webp 2000w"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_webexploitbench.width-1200.format-webp.webp"
        
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
    "section_header": "Introducing Gemini 4 Neon"
  }'
  or-mp4-video-url=""
  section-header="Introducing Gemini 4 Neon"
  alt-text="sacbenchpro chart"
  video-title=""
  
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="sacbenchpro chart"
        loading="lazy"
        
          sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
          srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__benchmark__secbenc.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__benchmark__secbenc.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__benchmark__secben.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__benchmark__secben.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__benchmark__secben.width-2000.format-webp.webp 2000w"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__benchmark__secben.width-1200.format-webp.webp"
        
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
    "section_header": "Introducing Gemini 4 Neon"
  }'
  or-mp4-video-url=""
  section-header="Introducing Gemini 4 Neon"
  alt-text="exploitgym benchmark chart"
  video-title=""
  
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="exploitgym benchmark chart"
        loading="lazy"
        
          sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
          srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_exploitgym.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_exploitgym.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_exploitgym.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_exploitgym.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_exploitgym.width-2000.format-webp.webp 2000w"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_exploitgym.width-1200.format-webp.webp"
        
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
    "section_header": "Introducing Gemini 4 Neon"
  }'
  or-mp4-video-url=""
  section-header="Introducing Gemini 4 Neon"
  alt-text="CWE bench v2 chart"
  video-title=""
  
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="CWE bench v2 chart"
        loading="lazy"
        
          sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
          srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_cwe.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_cwe.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_cwe.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_cwe.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_cwe.width-2000.format-webp.webp 2000w"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_cwe.width-1200.format-webp.webp"
        
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
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="a8po7">Gemini 4 Neon for cyber is rolling out to trusted defenders in the coming days as part of the <a href="https://deepmind.google/fairwind-program/">Fairwind Program</a>.</p></div>
  </uni-article-paragraph>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="safe-dependable-execution"
    aria-label="Designed for safe, dependable execution"
    class="
      uni-article-jumplinks__section
      uni-grid__col--layout-6
      
      "
    
    tabindex="-1">
    
  </section>
</div>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="a8po7">Designed for safe, dependable execution</h2><p data-block-key="adl9r">Gemini 4 Neon builds on improvements from our <a href="https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/">Gemini 4 safety and security stack</a>— maintaining Gemini 4 Carbon-level protections against severe misuse and prompt injection while advancing further on model alignment and agentic behavior. For a model meant to carry demanding, long-running work in production, we concentrated on:</p><ul><li data-block-key="fa6h0"><b>Mitigating frontier misuse safety risks:</b> Because Neon brings frontier-level capabilities to a faster, lower-cost model, we paired it with strong real-time safeguards against cyber and biosecurity misuse comparable to our Carbon protections, while declining far less legitimate work in these areas, refusing for instance just 1.98% of tasks on Terminal-Bench 4.0 and 0% on Terminal-Bench-Science.<br/><br/></li><li data-block-key="c18gp"><b>Advancing alignment and disciplined model behavior:</b> In internal coding use, alert rates from our chain-of-thought and action misalignment monitor remained below the already low baselines set by Carbon, suggesting improved alignment propensity for Neon — and that same monitor is deployed to protect Neon across external surfaces. Neon is trained to complete multi-step work without cutting corners, fabricating results, or overstepping user boundaries — continuing to improve the balance between following through on requests and staying within scope. It matched Carbon with 0.0% cheating on Terminal-Bench 4.0 and took shortcuts on just 2.45% of tasks on our coding cheating evaluation (the lowest rate of any Gemini 4 model). It also achieved a 0.09% misaligned action rate on our agentic safety suite and a 99.2% pass rate on our agent honesty evaluation.<br/><br/> On our agentic behavior evaluation, Neon builds on Carbon’s strong baseline by further reducing under-service by 43%–56% and overreach by 15%–35% across different effort levels.<br/><br/></li><li data-block-key="e12gu"><b>Protecting users from indirect prompt injection attacks:</b> On Gray Swan's IPI benchmark, Neon is more resilient than other models in its class when malicious instructions are planted in the web pages, emails, documents, or code it accesses. We found that with real-time safeguards at its highest thinking level, Neon resisted every attack within this Gray Swan benchmark, matching the 0.0% attack success rate reached only by other Gemini models.</li></ul></div>
  </uni-article-paragraph>
</section>

  

  
    





  
  
  
  
  

























<section class="uni-page uni-grid uni-inline-image-section" data-component="uni-inline-image">
  <uni-inline-image
    class="uni-inline-image uni-inline-image--full"
    alignment="full"
    alt-text="grey swan chart"
    external-image=""
    or-mp4-video-title=""
    or-mp4-video-url=""
    section-header="Introducing Gemini 4 Neon"
    
    
    
    
    
    
      autoplay="true"
    
  >
    

    
      <div slot="image-slot">
        <img
          alt="grey swan chart"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_grey_swan.width-1200.format-webp.webp"
          
            loading="lazy"
            sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
            srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_grey_swan.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_grey_swan.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_grey_swan.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_grey_swan.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_neon_grey_swan.width-2000.format-webp.webp 2000w"
          
        >
      </div>
    
  </uni-inline-image>
</section>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="f5fdt">For more details, see the <a href="https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf">Gemini 4 Neon model card</a>.</p></div>
  </uni-article-paragraph>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="analysis"
    aria-label="Built for deeper analysis"
    class="
      uni-article-jumplinks__section
      uni-grid__col--layout-6
      
      "
    
    tabindex="-1">
    
  </section>
</div>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="a8po7">Built for deeper analysis</h2><p data-block-key="dj9rp">In the Gemini app, Gemini 4 Neon excels at work that requires frontier-level reasoning and fast responses.</p><ul><li data-block-key="6otns"><b>Higher-quality writing and knowledge work:</b> Neon writes clearly, with well-structured responses and a natural, direct tone. It reads uploads like spreadsheets, PDFs, and photos more precisely, turns dense material into helpful reports and summaries, and pulls in relevant details from Google apps like Gmail and Docs.</li><li data-block-key="fscuv"><b>Reliable research and analysis:</b> Neon frequently incorporates details from sources across the web to keep responses current for fast-moving topics like comparing pricing across vendors before a major purchase or pulling together a complex brief with the latest market data.</li><li data-block-key="54skd"><b>Faster help for tougher tasks:</b> Tasks in Gemini can now run on Neon, working through complex, multi-step jobs more quickly and efficiently than with larger models. Get more done while stretching usage limits further when handing off tedious to-dos, like analyzing billing statements to spot why a utility charge spiked or cross-checking multiple receipts and documents to negotiate a refund.</li></ul></div>
  </uni-article-paragraph>
</section>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="xopc1">Where Neon sits in the Gemini 4 family</h2><p data-block-key="4849j">Neon is built for complex coding, analytical reasoning, and production-grade enterprise workflows. While Carbon tackles your hardest, long-horizon projects and Hydrogen handles fast everyday execution, Neon balances depth and efficiency. Neon delivers frontier-level reasoning for complex, high-frequency workflows faster and more cost efficiently.</p></div>
  </uni-article-paragraph>
</section>

  

  
    





  
  
  
  
  

























<section class="uni-page uni-grid uni-inline-image-section" data-component="uni-inline-image">
  <uni-inline-image
    class="uni-inline-image uni-inline-image--full"
    alignment="full"
    alt-text="A chart showing Gemini 4 models"
    external-image=""
    or-mp4-video-title=""
    or-mp4-video-url=""
    section-header="Introducing Gemini 4 Neon"
    
    
    
    
    
    
      autoplay="true"
    
  >
    

    
      <div slot="image-slot">
        <img
          alt="A chart showing Gemini 4 models"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__comparison-graphi.width-1200.format-webp.webp"
          
            loading="lazy"
            sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
            srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__comparison-graphic.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__comparison-graphic.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__comparison-graphi.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__comparison-graphi.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-neon__comparison-graphi.width-2000.format-webp.webp 2000w"
          
        >
      </div>
    
  </uni-inline-image>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="building-gemini-4-neon"
    aria-label="Start building with Gemini 4 Neon today"
    class="
      uni-article-jumplinks__section
      uni-grid__col--layout-6
      
      "
    
    tabindex="-1">
    
  </section>
</div>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="a8po7">Start building with Gemini 4 Neon today</h2><p data-block-key="6v25p">Gemini 4 Neon begins rolling out today:</p><ul><li data-block-key="2g451"><b>For developers:</b> Build with the Gemini API paid tier in <a href="https://aistudio.google.com/prompts/new_chat?model=gemini-4-neon">Google AI Studio</a> and <a href="https://developer.android.com/studio">Android Studio</a>, if you’re a paid Google AI Pro or Ultra subscriber, you can try Neon in <a href="https://antigravity.google/">Google Antigravity</a> and all Pro and Ultra subscribers can try it in AI Studio.</li><li data-block-key="52tqh"><b>For enterprises:</b> Use Gemini 4 Neon in <a href="https://cloud.google.com/gemini-enterprise">Gemini for business</a> (via the API or model drop-down) and Google Antigravity.</li><li data-block-key="96tdu"><b>For consumers:</b> If you’re a Google AI Pro or Ultra subscriber, you can select Gemini 4 Neon from the model drop-down in the <a href="http://gemini.google.com/">Gemini app</a>.</li><li data-block-key="5sljc"><b>For cybersecurity defenders:</b> Eligible<a href="https://deepmind.google/fairwind-program/"> Fairwind Program</a> members will begin receiving access over the next few days. To request access to the Fairwind Program, contact your Cloud account team.</li></ul></div>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#check-circle"></use>
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
    "section_header": "Introducing Gemini 4 Neon"
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
  





  
    


  
    <section class="uni-page uni-grid article-about-author redesign-patch"
      data-component="uni-article-about-author"
      data-analytics-module='{
        "module_name": "About the Author",
        "section_header": "About the Author"
      }'>
      <div class="article-about-author__content uni-grid__col--layout-8 uni-grid__col--layout-md-12">
        <h2 class="article-about-author__section--title font-h4">
          About the Author
        </h2>
        <div class="article-about-author__section--wrapper">
          
          
          
          
          
          <div class="article-about-author__wrapper">
            
            <div class="article-about-author__left-container">
              
                
    <figure class="article-about-author__photo">
        <picture>
            


    

    
        <source media="(max-width: 480px) and (max-resolution: 1.5dppx)"
                sizes="600px"
                srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/koray.width-600.format-webp.webp 600w">
    
        <source media="(max-width: 1024px) and (max-resolution: 1.5dppx)"
                sizes="600px"
                srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/koray.width-600.format-webp.webp 600w">
    
        <source media="(max-resolution: 1.5dppx)"
                sizes="480px"
                srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/koray.width-480.format-webp.webp 480w">
    
        <source media="(min-resolution: 1.5dppx)"
                sizes="600px"
                srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/koray.width-600.format-webp.webp 600w">
    

    <img src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/koray.width-600.format-webp.webp"

         
            alt="Koray Kavukcuoglu"
         

         sizes="(max-width: 480px) 600px, (max-width: 1024px) 600px,  480px,  600px"
         srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/koray.width-600.format-webp.webp 600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/koray.width-600.format-webp.webp 600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/koray.width-480.format-webp.webp 480w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/koray.width-600.format-webp.webp 600w"
         data-target="image"
         
          loading="lazy"
         
         >
    


        </picture>
    </figure>


              
            </div>
            
            <div class="article-about-author__right-container">
              
              <header class="article-about-author__header">
                <div class="article-about-author__title">
                  
                    <h3 class="font-title-1">
                  
                    Koray Kavukcuoglu
                  </h3>
                  
                    <h4 class="font-body-m">
                      SVP, Google DeepMind and Chief AI Architect, Google
                    </h4>
                  
                </div>
                <ul class="article-about-author__socials">
                  
                  
                </ul>
              </header>
              
              <p class="article-about-author__profile font-body-m"
                >
                Koray is one of the world&#x27;s foremost experts in artificial intelligence. As the SVP of Google DeepMind, he leads the development of Google DeepMind’s state-of-the art generative AI models and their integration into Google’s products at scale. Prior to his current role, he was VP of Research at Google DeepMind, where he founded the deep learning team and his team pioneered major research breakthroughs such as DQN (Deep Q-Network) and WaveNet.
              </p>
              
              
                
                <uni-cta
                  href=https://blog.google/authors/koray-kavukcuoglu/
                  aria-label="Read more from Koray Kavukcuoglu, SVP, Google DeepMind and Chief AI Architect, Google"
                  emphasis="low"
                  icon-id-right="arrow-forward"
                  additional-class="article-about-author__cta"
                  
                  data-ga4-analytics-cta-click='{
  "event": "cta_click",
  "link_text": "Read more from Koray Kavukcuoglu"
}'

                  

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "Read more from Koray Kavukcuoglu"
}'

                  data-ga4-analytics-perspective-author-click='{
  "link_text": "Read more from Koray Kavukcuoglu",
  "link_url": "https://blog.google/authors/koray-kavukcuoglu/"
}'
>
                  
                    Read more from Koray Kavukcuoglu
                  
                </uni-cta>
              
              
            </div>
          </div>
          <hr class="article-about-author__separator" aria-hidden="true">
          
        </div>
      </div>
    </section>
  


  

  
    









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
  href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/"
  class="uni-article-card"
  aria-label="
    
      
      Google DeepMind - 
    
    Genie 4 is now available
    
    
      - By Diego Rivas& Pavan Kumar
    
    
      - Nov 18, 2026
    
  "
  data-index="1"
  data-target="card"
  data-primaryTag="topics - google deepmind"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Genie 4 is now available",
  "link_url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/",
  "source_content": "Related stories",
  "related_index": "1",
  "related_article_tag": "topics - google deepmind",
  "article_name": "Genie 4 is now available",
  "author_name": "Diego Rivas, Pavan Kumar",
  "content_type": "blogv2 | article page"
}'

  
  data-theme-color="purple"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["12-sided-cookie", "4-sided-cookie", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/resized_ProjectGenie_.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/resized_ProjectGenie_.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/resized_ProjectGenie_.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
    loading="lazy"
  
  />




      
    </div>
  </div>

  <div class="uni-article-card__content">
    <div class="uni-article-card__text">
      
      <span
        class="uni-article-card__eyebrow font-eyebrow"
        data-target="eyebrow">
        
          Google DeepMind
        
      </span>
      
      <h3
        class="uni-article-card__title font-h5"
        data-target="title">
        Genie 4 is now available
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Diego Rivas
          
            & 
            Pavan Kumar
          
        </span>
      
    </div>
  </div>
</a>


        
          








<a
  href="https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/"
  class="uni-article-card"
  aria-label="
    
      
      Search - 
    
    Google Search gets a major upgrade with Gemini 4 Hydrogen
    
    
      - By Robby Stein
    
    
      - Nov 12, 2026
    
  "
  data-index="2"
  data-target="card"
  data-primaryTag="products - search"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Google Search gets a major upgrade with Gemini 4 Hydrogen",
  "link_url": "https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/",
  "source_content": "Related stories",
  "related_index": "2",
  "related_article_tag": "products - search",
  "article_name": "Google Search gets a major upgrade with Gemini 4 Hydrogen",
  "author_name": "Robby Stein",
  "content_type": "blogv2 | article page"
}'

  
  data-theme-color="aquamarine"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["8-leaf-clover", "ghost-ish", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/HydrogenUI_socialshar.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/HydrogenUI_socialshar.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/HydrogenUI_socialshar.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
    loading="lazy"
  
  />




      
    </div>
  </div>

  <div class="uni-article-card__content">
    <div class="uni-article-card__text">
      
      <span
        class="uni-article-card__eyebrow font-eyebrow"
        data-target="eyebrow">
        
          Search
        
      </span>
      
      <h3
        class="uni-article-card__title font-h5"
        data-target="title">
        Google Search gets a major upgrade with Gemini 4 Hydrogen
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Robby Stein
          
        </span>
      
    </div>
  </div>
</a>


        
          








<a
  href="https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-hydrogen/"
  class="uni-article-card"
  aria-label="
    
      
      Developer tools - 
    
    Gemini 4 Hydrogen: everyday coding and agentic workflows for developers
    
    
    
      - Nov 12, 2026
    
  "
  data-index="3"
  data-target="card"
  data-primaryTag="products - developer tools"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Gemini 4 Hydrogen: everyday coding and agentic workflows for developers",
  "link_url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-hydrogen/",
  "source_content": "Related stories",
  "related_index": "3",
  "related_article_tag": "products - developer tools",
  "article_name": "Gemini 4 Hydrogen: everyday coding and agentic workflows for developers",
  "author_name": "",
  "content_type": "blogv2 | Short Post"
}'

  
  data-theme-color="green"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["6-sided-cookie", "8-leaf-clover", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Hydrogen_socialshare.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Hydrogen_socialshare.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Hydrogen_socialshare.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
    loading="lazy"
  
  />




      
    </div>
  </div>

  <div class="uni-article-card__content">
    <div class="uni-article-card__text">
      
      <span
        class="uni-article-card__eyebrow font-eyebrow"
        data-target="eyebrow">
        
          Developer tools
        
      </span>
      
      <h3
        class="uni-article-card__title font-h5"
        data-target="title">
        Gemini 4 Hydrogen: everyday coding and agentic workflows for developers
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
    </div>
  </div>
</a>


        
          








<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/"
  class="uni-article-card"
  aria-label="
    
      
      Gemini models - 
    
    Introducing Gemini 4 Hydrogen
    
    
      - By Koray Kavukcuoglu
    
    
      - Nov 12, 2026
    
  "
  data-index="4"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Introducing Gemini 4 Hydrogen",
  "link_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/",
  "source_content": "Related stories",
  "related_index": "4",
  "related_article_tag": "topics - gemini models",
  "article_name": "Introducing Gemini 4 Hydrogen",
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
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-element-hydr.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-element-hydr.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-4-element-hydr.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        Introducing Gemini 4 Hydrogen
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
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/"
  class="uni-article-card"
  aria-label="
    
      
      Gemini models - 
    
    Introducing the Multimodal Knowledge Agent benchmark
    
    
      - By Rohan Doshi& Ben Caine
    
    
      - Nov 10, 2026
    
  "
  data-index="5"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Introducing the Multimodal Knowledge Agent benchmark",
  "link_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/",
  "source_content": "Related stories",
  "related_index": "5",
  "related_article_tag": "topics - gemini models",
  "article_name": "Introducing the Multimodal Knowledge Agent benchmark",
  "author_name": "Rohan Doshi, Ben Caine",
  "content_type": "blogv2 | article page"
}'

  
  data-theme-color="blue"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-sided-cookie", "bun", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/01_Hero_MKA_Benchmark.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/01_Hero_MKA_Benchmark.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/01_Hero_MKA_Benchmark.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        Introducing the Multimodal Knowledge Agent benchmark
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Rohan Doshi
          
            & 
            Ben Caine
          
        </span>
      
    </div>
  </div>
</a>


        
          








<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/"
  class="uni-article-card"
  aria-label="
    
      
      Gemini models - 
    
    Gemini 4 Carbon is now available
    
    
      - By Koray Kavukcuoglu
    
    
      - Nov 10, 2026
    
  "
  data-index="6"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  
    






data-ga4-analytics-footer-lead-click='{
  "link_text": "Gemini 4 Carbon is now available",
  "link_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/",
  "source_content": "Related stories",
  "related_index": "6",
  "related_article_tag": "topics - gemini models",
  "article_name": "Gemini 4 Carbon is now available",
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
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_carbon_key_a.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_carbon_key_a.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_carbon_key_a.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        Gemini 4 Carbon is now available
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
    "section_header": "Introducing Gemini 4 Neon"
  }'>
  <section class="uni-footer__logo">
    <a href="https://www.google.com" aria-label="The Google logo">
      <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 396 130"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#google-logo"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#expand_more"></use>
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
        value="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
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
        value="https://blog.google/intl/ja-jp/company-news/technology/introducing-gemini-4-neon/"
        lang="ja-jp"
        class="uni-lang-picker__option"
        >
        日本 (日本語)
      </option>
      
      <option
        label="대한민국 (한국어)"
        value="https://blog.google/intl/ko-kr/company-news/technology/introducing-gemini-4-neon-kr/"
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
    href="/static/blogv2/images/icons.svg?version=pr20261117-1738#expand_more"></use>
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
              { "url": "/static/blogv2/js/csp/gtm.js?version=pr20261117-1738",
                "options": {
                  "async": false,
                  "defer": true
                }
              },
              { "url": "/static/keyword/js/all/index.js?version=pr20261117-1738",
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
