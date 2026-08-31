





<!DOCTYPE html>
<html class="no-js glue-flexbox  keyword-blog" lang="en-us" data-locale="en-us" data-version="pr20260820-1820">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <title>Gemini 2.5 Native Audio upgrade, plus text-to-speech model updates</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=1.0, minimum-scale=1.0" />
        <meta name="optimize_experiments" content="[]">

        
  




<!--Article Specific Metadata-->
<meta name="description" content="An upgraded Gemini 2.5 Native Audio model across Google products and live speech translation in the Google Translate app."/>
<meta name="keywords" content="None"/>
<meta name="article-author" content="Bibo Xu, Tara Sainath"/>
<meta name="robots" content="max-image-preview:large">

<!--Open Graph Metadata-->
<meta property="og:type" content="article" />
<meta property="og:title" content="Improved Gemini audio models for powerful voice interactions"/>

<meta property="og:description" content="An upgraded Gemini 2.5 Native Audio model across Google products and live speech translation in the Google Translate app." />
<meta property="og:image" content="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio-flash__keyword_meta__dark.width-1300.png" />
<meta property="og:site_name" content="Google" />
<meta property="og:url" content="https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/" />
<meta property="article:publisher" content="https://www.facebook.com/Google/" />
<meta property="article:published_time" content="2025-12-12" />

<!--Twitter Card Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:url" content="https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/" />
<meta name="twitter:title" content="Improved Gemini audio models for powerful voice interactions"/>
<meta name="twitter:description" content="An upgraded Gemini 2.5 Native Audio model across Google products and live speech translation in the Google Translate app." />
<meta name="twitter:image:src" content="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio-flash__keyword_meta__dark.width-1300.png" />
<meta name="twitter:site" content="@google" />







        
  <meta name="page" content="82933" />
  <meta name="locale" content="en-us" />
  <meta name="published_time" content="2025-12-12T17:00:00+00:00" />
  <meta name="content_type" content="blogv2.articlepage" />
  <meta name="tags" content="Gemini models" />
  <meta name="authors" content="Bibo Xu,Tara Sainath" />



        
        

        
        
  
  
  




        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        


        
        
        <link class="deferred-stylesheet" rel="preload" type="text/css" href="/static/keyword/css/blog/index.min.css?version=pr20260820-1820" as="style">
<noscript>
  <link rel="stylesheet" href="/static/keyword/css/blog/index.min.css?version=pr20260820-1820">
</noscript>

        <link class="deferred-stylesheet" rel="preload" type="text/css" href="https://fonts.googleapis.com/css?family=Google+Sans:400,500,600,700|Google+Sans+Flex:400,500|Product+Sans:400&amp;display=swap&amp;lang=en" as="style">
<noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Google+Sans:400,500,600,700|Google+Sans+Flex:400,500|Product+Sans:400&amp;display=swap&amp;lang=en">
</noscript>

        <link class="deferred-stylesheet" rel="preload" type="text/css" href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css" as="style">
<noscript>
  <link rel="stylesheet" href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css">
</noscript>


        
        
        

	
        

        
  
            
        
  
  <link rel="stylesheet" type="text/css" href="/static/keyword/css/print/index.min.css?version=pr20260820-1820" media="print" />


        

<link rel="canonical" href="https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"/>

<link href="/favicon.ico" rel="icon">
<link href="/static/blogv2/images/apple-touch-icon.png?version=pr20260820-1820" rel="apple-touch-icon">



        <meta property="gtm-tag" content="GTM-TRV24V">



        <!-- https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API -->


      </head>

    <body class="template-articlepage keyword-blog">
        
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TRV24V" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>


        


<div class="data-layer-init-data" data-ga4-analytics='
  {
    "event": "dataLayer_initialized",
    
      "page_name": "Gemini 2.5 Native Audio upgrade, plus text\u002Dto\u002Dspeech model updates",
    
    "experiments": "undefined",
    "locale": "en-us",
    "page_type": "blogv2 | article page",
    "primary_tag": "topics - gemini models",
    "secondary_tags": "undefined",
    
      "landing_page_tags": "undefined",
    
    
      "article_name": "Improved Gemini audio models for powerful voice interactions",
      "author_name": "Bibo Xu, Tara Sainath",
    
    "publish_date": "2025-12-12|17:00",
    "hero_media": "image",
    
      "special_hero": "undefined",
    
    "days_since_published": "261",
    
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#h-burger"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-clear"></use>
</svg>

        </button>
        <!-- Logo -->
        
        
          <a href="/" class="uni-nav__logo" aria-label="Google News Home" title="News from Google">
            <svg
  aria-label="Google"
  
  
  
  
  
  role="img"
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#news-from-google-logo"></use>
</svg>

            <!-- SuperG Logo -->
            <img class="uni-nav__logo--super-g" src="/static/blogv2/images/super-g-aurora.svg?version=pr20260820-1820" alt="Google" width="30" height="30">
          </a>
        
        
          <p class="uni-nav-article__article-title font-body-m">Improved Gemini audio models for powerful voice interactions</p>
        
      </div>
      

<div id="mobile-menu-overlay" class="uni-nav-mobile__wrapper" aria-hidden="true">
  <nav
    data-analytics-module='{
        "module_name":"main nav",
        "section_header": "Mobile menu"
     }'
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
</svg>

        Back
      </button>
    </section>
    <section class="uni-nav-mobile__section uni-nav-mobile__section--intro">
      <h3 class="uni-nav-mobile__section-title font-h3">Innovation &amp; AI</h3>
      
      
        <uni-cta class="uni-nav-mobile__see-all-cta" href="/innovation-and-ai/" emphasis="medium" icon-id-right="arrow-forward">
          
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
</svg>

        Back
      </button>
    </section>
    <section class="uni-nav-mobile__section uni-nav-mobile__section--intro">
      <h3 class="uni-nav-mobile__section-title font-h3">Products &amp; platforms</h3>
      
      
        <uni-cta class="uni-nav-mobile__see-all-cta" href="/products-and-platforms/" emphasis="medium" icon-id-right="arrow-forward">
          
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
                    Chromebooks
                    
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
</svg>

        Back
      </button>
    </section>
    <section class="uni-nav-mobile__section uni-nav-mobile__section--intro">
      <h3 class="uni-nav-mobile__section-title font-h3">Company news</h3>
      
      
        <uni-cta class="uni-nav-mobile__see-all-cta" href="/company-news/" emphasis="medium" icon-id-right="arrow-forward">
          
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
                          Chromebooks 
                        </a>
                      
                    </li>
                   
                    <li class="uni-nav-desktop__subitem">
                      <a href="/products-and-platforms/devices/" class="uni-nav-link uni-nav-link--see-all font-body-xl" title="See all Devices articles">See all <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow-forward"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#arrow_outward"></use>
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
  <div class="uni-article-progress-bar__title uni-article-progress-bar__ellipsis">Improved Gemini audio models for powerful voice interactions</div>
  <div class="uni-article-progress-bar__social"
    data-analytics-module='{
      "module_name": "Progress Bar",
      "section_header": "Improved Gemini audio models for powerful voice interactions"
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-share"></use>
</svg>

    <div class="uni-social-share__button">Share</div>
  </a>
  <div class="uni-social-share__dialog uni-social-share__content " aria-labelledby="social-share-icon">
    


<a aria-label="Share on X"
    class="article-share__link-text uni-click-tracker"
    href="https://twitter.com/intent/tweet?text=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions%20%40google&url=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
    target="_blank"
    data-ga4-method="twitter">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-x"></use>
</svg>

  <div class="article-share__title">x.com</div>
</a>

<a aria-label="Share on Facebook"
    class="article-share__link-text uni-click-tracker"
    href="https://www.facebook.com/sharer/sharer.php?caption=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions&u=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
    target="_blank"
    data-ga4-method="facebook">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-facebook"></use>
</svg>

  <div class="article-share__title">Facebook</div>
</a>

<a aria-label="Share on LinkedIn"
    class="article-share__link-text uni-click-tracker"
    href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/&title=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions"
    target="_blank"
    data-ga4-method="linkedin">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-linkedin"></use>
</svg>

  <div class="article-share__title">LinkedIn</div>
</a>

<a aria-label="Share with Email"
    class="article-share__link-text uni-click-tracker article-share__email"
    
      href="mailto:?subject=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions&body=Check out this article on the Keyword:%0A%0AImproved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions%0A%0AAn upgraded Gemini 2.5 Native Audio model across Google products and live speech translation in the Google Translate app.%0A%0Ahttps://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
    
    target="_blank"
    data-ga4-method="email">
  <svg
  
  class="h-c-icon h-c-icon--social h-c-icon--30px"
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 30 30"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-mail"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-link"></use>
</svg>

    <div class="copy-link__title">Copy link</div>
  </button>
  <div class="copy-link__dialog copy-link__content" uni-options='{"copyTextButton": "COPIED TO CLIPBOARD"}' aria-hidden="true" tabindex="-1">
    <input class="h-c-copy copy-link__url" value="https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/" id="copy-link" readonly="readonly" type="text"/>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-more-vert"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#language"></use>
</svg>

            


  <div data-component="uni-lang-picker" class="uni-lang-picker">
    <select
      name="language-picker"
      class="uni-lang-picker__select font-ctas uni-lang-picker--inside-menu"
      aria-label="Change Region">
      
      <option
        label="Global (English)"
        value="https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
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
        label="Malaysia (Melayu)"
        value="https://blog.google/intl/ms-my/"
        lang="ms-my"
        class="uni-lang-picker__option"
        >
        Malaysia (Melayu)
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#expand_more"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#photo-library"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#rss-feed"></use>
</svg>
RSS feed</a>
        </li>
      </ul>
    </div>
  </div>

  <!-- Share Dropdown Menu -->
  
  <div class="uni-share-dropdown" data-component="uni-share-dropdown" data-analytics-module='{
         "module_name": "Progress Bar",
         "section_header": "Improved Gemini audio models for powerful voice interactions"
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#share"></use>
</svg>

    </button>
    <div id="header-share-dropdown" class="uni-share-dropdown__menu " aria-hidden="true">
  <div class="uni-share-dropdown__menu-inner">
    <ul class="uni-share-dropdown__menu-link-list uni-social-share">
      


<li>
  <a aria-label="Share on X"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://twitter.com/intent/tweet?text=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions%20%40google&url=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
      target="_blank"
      data-ga4-method="twitter">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-x"></use>
</svg>

    <span>x.com</span>
  </a>
</li>

<li>
  <a aria-label="Share on Facebook"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.facebook.com/sharer/sharer.php?caption=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions&u=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
      target="_blank"
      data-ga4-method="facebook">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-facebook"></use>
</svg>

    <span>Facebook</span>
  </a>
</li>

<li>
  <a aria-label="Share on LinkedIn"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/&title=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions"
      target="_blank"
      data-ga4-method="linkedin">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-linkedin"></use>
</svg>

    <span>LinkedIn</span>
  </a>
</li>

<li>
  <a aria-label="Share with Email"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      
        href="mailto:?subject=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions&body=Check out this article on the Keyword:%0A%0AImproved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions%0A%0AAn upgraded Gemini 2.5 Native Audio model across Google products and live speech translation in the Google Translate app.%0A%0Ahttps://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
      
      target="_blank"
      data-ga4-method="email">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-mail"></use>
</svg>

    <span>Mail</span>
  </a>
</li>

<li data-component="uni-copy-popup-component">
  <button aria-label="Copy link"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker uni-copy-share"
      data-ga4-analytics-share-copy-link
      data-ga4-method="Copy link"
      data-copy-text="https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-link"></use>
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

    









<section class="uni-article-hero uni-article-hero--neutral"
  data-analytics-module='{
    "module_name": "Hero Menu",
    "section_header": "Improved Gemini audio models for powerful voice interactions"
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#uni-icon-chevron-right"></use>
</svg>

    </button>
    <div class="uni-breadcrumb__focusable uni-breadcrumb__focusable--start"></div>
    <nav aria-label="Breadcrumb" class="breadcrumb uni-breadcrumb__scrollable">
      <span class="uni-breadcrumb__label">Breadcrumb</span>
      <ol data-analytics-module='{
        "module_name": "breadcrumbs",
        "section_header": "Improved Gemini audio models for powerful voice interactions"
      }'>
      
        <li>
        
          <a href="https://blog.google/"
            class="uni-breadcrumb__button uni-breadcrumb__button--homepage font-body-s"
            title="The Keyword"
            aria-label="The Keyword"
            

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "The Keyword"
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#uni-icon-chevron-right"></use>
</svg>

          
            <a href="https://blog.google/products-and-platforms/"
              class="uni-breadcrumb__button font-body-s"
              

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "Products \u0026 Platforms"
}'
>
                Products &amp; Platforms
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#uni-icon-chevron-right"></use>
</svg>

          
            <a href="https://blog.google/products-and-platforms/products/"
              class="uni-breadcrumb__button font-body-s"
              

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "Products"
}'
>
                Products
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#uni-icon-chevron-right"></use>
</svg>

          
            <a href="https://blog.google/products-and-platforms/products/gemini/"
              class="uni-breadcrumb__button font-body-s"
              

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "Gemini"
}'
>
                Gemini
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#uni-icon-chevron-right"></use>
</svg>

    </button>
  </uni-breadcrumbs>


          </div>
        
      </div>
      
      <div class="uni-grid uni-article-hero__content-grid">
        <div class="uni-grid__col--span-4 uni-grid__col--span-12-tablet uni-grid__col--span-8-desktop uni-grid__col--start-3-desktop uni-article-hero__main-content">
          <h1 class="uni-article-hero__title font-h1">Improved Gemini audio models for powerful voice interactions</h1>

          <div class="uni-article-hero__meta-wrapper">
            <div class="uni-article-hero__meta-header">
              
              <div class="uni-article-hero__meta-aside">
                
                
                
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
      href="https://twitter.com/intent/tweet?text=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions%20%40google&url=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
      target="_blank"
      data-ga4-method="twitter">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-x"></use>
</svg>

    <span>x.com</span>
  </a>
</li>

<li>
  <a aria-label="Share on Facebook"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.facebook.com/sharer/sharer.php?caption=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions&u=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
      target="_blank"
      data-ga4-method="facebook">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-facebook"></use>
</svg>

    <span>Facebook</span>
  </a>
</li>

<li>
  <a aria-label="Share on LinkedIn"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/&title=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions"
      target="_blank"
      data-ga4-method="linkedin">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-linkedin"></use>
</svg>

    <span>LinkedIn</span>
  </a>
</li>

<li>
  <a aria-label="Share with Email"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      
        href="mailto:?subject=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions&body=Check out this article on the Keyword:%0A%0AImproved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions%0A%0AAn upgraded Gemini 2.5 Native Audio model across Google products and live speech translation in the Google Translate app.%0A%0Ahttps://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
      
      target="_blank"
      data-ga4-method="email">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-mail"></use>
</svg>

    <span>Mail</span>
  </a>
</li>

<li data-component="uni-copy-popup-component">
  <button aria-label="Copy link"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker uni-copy-share"
      data-ga4-analytics-share-copy-link
      data-ga4-method="Copy link"
      data-copy-text="https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-link"></use>
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

          
          <div class="uni-article-hero__authors-actions">
            <div class="uni-article-hero__authors-wrapper">
              
                

<div class="uni-article-hero__authors uni-grid">
  
    
    <div class="uni-article-hero__author">
      <div class="uni-article-hero__author-info">
        
            <p class="uni-article-hero__author-name font-author-name">Bibo Xu</p>
            
              
                <p class="uni-article-hero__author-title font-author-info">Director of Product Management</p>
              
            
        
      </div>
    </div>
  
    
    <div class="uni-article-hero__author">
      <div class="uni-article-hero__author-info">
        
            <p class="uni-article-hero__author-name font-author-name">Tara Sainath</p>
            
              
                <p class="uni-article-hero__author-title font-author-info">Distinguished Research Scientist</p>
              
            
        
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
      href="https://twitter.com/intent/tweet?text=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions%20%40google&url=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
      target="_blank"
      data-ga4-method="twitter">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-x"></use>
</svg>

    <span>x.com</span>
  </a>
</li>

<li>
  <a aria-label="Share on Facebook"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.facebook.com/sharer/sharer.php?caption=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions&u=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
      target="_blank"
      data-ga4-method="facebook">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-facebook"></use>
</svg>

    <span>Facebook</span>
  </a>
</li>

<li>
  <a aria-label="Share on LinkedIn"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/&title=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions"
      target="_blank"
      data-ga4-method="linkedin">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-linkedin"></use>
</svg>

    <span>LinkedIn</span>
  </a>
</li>

<li>
  <a aria-label="Share with Email"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker"
      
        href="mailto:?subject=Improved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions&body=Check out this article on the Keyword:%0A%0AImproved%20Gemini%20audio%20models%20for%20powerful%20voice%20interactions%0A%0AAn upgraded Gemini 2.5 Native Audio model across Google products and live speech translation in the Google Translate app.%0A%0Ahttps://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
      
      target="_blank"
      data-ga4-method="email">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-mail"></use>
</svg>

    <span>Mail</span>
  </a>
</li>

<li data-component="uni-copy-popup-component">
  <button aria-label="Copy link"
      class="uni-share-dropdown__menu-link font-ctas uni-click-tracker uni-copy-share"
      data-ga4-analytics-share-copy-link
      data-ga4-method="Copy link"
      data-copy-text="https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/">
    <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#social-link"></use>
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
            alt="Gemini Audio text logo"
            class="uni-article-hero__image uni-progressive-image--blur"
            data-component="uni-progressive-image"
            fetchpriority="high"
            src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio-flash__keyword_heade.width-200.format-webp.webp"
            
              data-sizes="(max-width: 1023px) 100vw, (max-width: 1440px) 95vw, 1408px"
              data-srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio-flash__keyword_heade.width-450.format-webp.webp 450w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio-flash__keyword_heade.width-900.format-webp.webp 900w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio-flash__keyword_head.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio-flash__keyword_head.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio-flash__keyword_head.width-2200.format-webp.webp 2200w"
            
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
      "section_header": "Improved Gemini audio models for powerful voice interactions"
     }'
     data-tts-audios='[
      
        {"voice_name": "Umbriel",
        "voice_source": "https://storage.googleapis.com/gweb-uniblog-publish-prod/media/tts_audio_82933_umbriel_2025_12_19_19_02_55.wav",
        "mimetype": "audio/x-wav"},
      
        {"voice_name": "Gacrux",
        "voice_source": "https://storage.googleapis.com/gweb-uniblog-publish-prod/media/tts_audio_82933_gacrux_2025_12_19_19_04_03.wav",
        "mimetype": "audio/x-wav"}
      ]'>
  <audio
    class="audio-player-tts__player"
    title="Improved Gemini audio models for powerful voice interactions">
      <source
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/media/tts_audio_82933_umbriel_2025_12_19_19_02_55.wav"
        type="audio/x-wav" />
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#play-gd"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#ttf-info"></use>
</svg>

        </span>
      </div>
      <button class="audio-player-tts__pause" aria-label="Pause article audio description">
        <svg
  
  class="audio-player-tts__icon-play"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#play-gd"></use>
</svg>

        <svg
  
  class="audio-player-tts__icon-pause audio-player-tts__icon-pause--hidden"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#pause-gd"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#ttf-settings"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#tts-voice"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#tts-chevron"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#tts-speed"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#tts-chevron"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#tts-chevron"></use>
</svg>
 <span>Voice</span></button>
          </div>
          <div class="audio-player-tts__settings--speeds uni-cta-text">
            <button class="audio-player-tts__settings-back" aria-label="Click to go back"><svg
  
  class="icon tts-chevron"
  
  
  
  
  
  
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#tts-chevron"></use>
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


        
          
            


<div class="uni-ai-summary "
  data-component="uni-ai-generated-summary"
  data-analytics-module='{
    "event": "module_impression",
    "module_name": "ai_summary",
    "section_header": "Improved Gemini audio models for powerful voice interactions"
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#summarize-gd"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
</svg>

        </span>
      </span>
    </button>

    <div id="uni-ai-summary-dropdown" class="uni-ai-summary__dropdown" aria-hidden="true">
      <div class="uni-ai-summary__dropdown-inner">
        
          <div class="uni-ai-summary__summary active" data-summary-id="ai_summary_1">
            <div class="uni-ai-summary__copy font-h6">
              <p>Google enhanced Gemini 2.5 Flash Native Audio for better live voice agents. Expect sharper function calling, robust instruction following and smoother conversations. Try live speech translation in the Google Translate app beta, rolling out now on Android in the US Mexico and India.</p>
            </div>
            <small class="uni-ai-summary__legal font-body-xs">
              Summaries were generated by Google AI. Generative AI is experimental.
            </small>
          </div>
        
          <div class="uni-ai-summary__summary " data-summary-id="ai_summary_2">
            <div class="uni-ai-summary__copy font-h6">
              <ul>
<li>"Improved Gemini audio models for powerful voice interactions" enhance live agents and translation.</li>
<li>Gemini 2.5 Flash Native Audio now has sharper function calling and better instruction following.</li>
<li>The update allows for smoother conversations by retrieving context from previous turns.</li>
<li>Live speech translation in Google Translate preserves intonation and handles 70+ languages.</li>
<li>You can start building voice agents today with Gemini 2.5 Flash Native Audio on Vertex AI.</li>
</ul>
            </div>
            <small class="uni-ai-summary__legal font-body-xs">
              Summaries were generated by Google AI. Generative AI is experimental.
            </small>
          </div>
        
          <div class="uni-ai-summary__summary " data-summary-id="ai_summary_3">
            <div class="uni-ai-summary__copy font-h6">
              <p>Google made its Gemini AI better at understanding and speaking in conversations. It can now understand instructions better, have smoother conversations, and translate languages in real time. This means AI can help businesses with customer service and people can understand each other better, even if they speak different languages. You can even try out the live translation feature in the Google Translate app.</p>
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
              <button class="uni-ai-summary__chip-btn font-body-s" aria-label="General summary" data-summary-id="ai_summary_1" aria-pressed="true">
                
                  <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#summarize_auto"></use>
</svg>

                
                <span class="uni-ai-summary__chip-text" aria-hidden="true">
                  General summary
                </span>
              </button>
            </li>
            
            <li>
              <button class="uni-ai-summary__chip-btn font-body-s" aria-label="Bullet points" data-summary-id="ai_summary_2" >
                
                  <svg
  
  
  
  
  
  
  role="presentation"
  aria-hidden="true"
  
  
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#format_list_bulleted"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#text_snippet"></use>
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
      
        
        
        <div class="uni-content uni-blog-article-container article-container__content
                    "
            data-reading-time="true"
            data-component="uni-article-body">

          
          
<!--article text-->

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Improved Gemini audio models for powerful voice interactions"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="61bfj">Earlier this week, we introduced greater control over audio generation with an upgrade to our <a href="https://blog.google/technology/developers/gemini-2-5-text-to-speech">Gemini 2.5 Pro and Flash Text-to-Speech models</a>.</p><p data-block-key="12cio">But generating expressive speech is only one side of the conversation. Today, we’re releasing an updated Gemini 2.5 Flash Native Audio for live voice agents. This update improves the model’s ability to handle complex workflows, navigate user instructions, and hold natural conversations.</p><p data-block-key="o2mg">Gemini 2.5 Flash Native Audio is now available across Google products including <a href="https://aistudio.google.com/prompts/new_chat?model=gemini-2.5-flash-native-audio-preview-12-2025">Google AI Studio</a>, <a href="https://cloud.google.com/blog/products/ai-machine-learning/gemini-live-api-available-on-vertex-ai">Vertex AI</a>, and has also started rolling out in <a href="https://gemini.google/overview/gemini-live/">Gemini Live</a> and <a href="https://blog.google/products/search/live-audio-gemini-model-update/">Search Live</a>, bringing the naturalness of native audio to Search Live for the first time. This means you can more effectively brainstorm live with Gemini, get real-time help in Search Live, or build the next generation of enterprise-ready customer service agents.</p><p data-block-key="abqf7">Beyond powering helpful agents, native audio unlocks new possibilities for global communication. We’re introducing live speech translation, a capability that enables streaming speech-to-speech translation for headphones. It preserves the speaker’s intonation, pacing and pitch. This beta experience is rolling out in the <a href="https://blog.google/products/search/gemini-capabilities-translation-upgrades/">Google Translate app</a> starting today.</p><h2 data-block-key="12h0r">Live Voice Agents</h2></div>
  </uni-article-paragraph>
</section>

  

  
    
  
    



<uni-youtube-player-article
  index="2"
  page-title="Improved Gemini audio models for powerful voice interactions"
  thumbnail-alt="Video introducing the updated Gemini 2.5 Flash Native Audio"
  
  subtitle="Gemini 2.5 Flash Native Audio is now enabling a wide spectrum of conversational experiences."
  
  video-id="5eA5aZpVYbs"
  video-type="video"
  
  
  >
</uni-youtube-player-article>










  


  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Improved Gemini audio models for powerful voice interactions"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="61bfj">To enable the breadth of use cases across surfaces and products, we have improved Gemini 2.5 Native Audio in three key areas:</p><ul><li data-block-key="2mflj"><b>Sharper function calling:</b> We’ve improved the model's reliability when triggering external functions. It can now more accurately identify when to fetch real-time information during a conversation and seamlessly weave that data back into the audio response, without breaking the flow. On <a href="https://github.com/zai-org/ComplexFuncBench?tab=readme-ov-file#citatio">ComplexFuncBench Audio</a>, an eval that captures multi-step function calling with various constraints, Gemini 2.5 Native Audio leads with a score of 71.5%.</li><li data-block-key="f7bio"><b>Robust instruction following:</b> The model is now better at handling complex instructions resulting in higher user satisfaction on content completeness. With a 90% adherence rate to developer instructions (up from 84%), it delivers more reliable outputs.</li><li data-block-key="bp5l4"><b>Smoother conversations:</b> We’ve achieved significant gains in multi-turn conversation quality. Gemini 2.5 Flash Native Audio is able to retrieve context from previous turns more effectively, creating more cohesive conversations.</li></ul></div>
  </uni-article-paragraph>
</section>

  

  
    





  
  
  
  
  

























<section class="uni-page uni-grid uni-inline-image-section" data-component="uni-inline-image">
  <uni-inline-image
    class="uni-inline-image uni-inline-image--full"
    alignment="full"
    alt-text="updated Gemini 2.5 Flash Native Audio’s performance against previous versions and industry competitors"
    external-image=""
    or-mp4-video-title=""
    or-mp4-video-url=""
    section-header="Improved Gemini audio models for powerful voice interactions"
    
    
    
    
    
      autoplay="true"
    
  >
    
      <div slot="caption-slot">
        <div class="rich-text"><p data-block-key="m27h1">The updated Gemini 2.5 Flash Native Audio’s performance against previous versions and industry competitors on <a href="https://github.com/zai-org/ComplexFuncBench?tab=readme-ov-file#citatio">ComplexFuncBench</a></p></div>
      </div>
    

    
      <div slot="image-slot">
        <img
          alt="updated Gemini 2.5 Flash Native Audio’s performance against previous versions and industry competitors"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-audio_blog_light_blue_16x9_v1_25-12-12_1.gif"
          
            loading="lazy"
            sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
            srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-audio_blog_light_blue_16x9_v1_25-12-12_1.gif 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-audio_blog_light_blue_16x9_v1_25-12-12_1.gif 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-audio_blog_light_blue_16x9_v1_25-12-12_1.gif 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-audio_blog_light_blue_16x9_v1_25-12-12_1.gif 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-audio_blog_light_blue_16x9_v1_25-12-12_1.gif 2000w"
          
        >
      </div>
    
  </uni-inline-image>
</section>

  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Improved Gemini audio models for powerful voice interactions"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h3 data-block-key="61bfj">What customers are saying</h3><p data-block-key="c8rur"><a href="https://cloud.google.com/blog/products/ai-machine-learning/gemini-live-api-available-on-vertex-ai">Google Cloud customers</a> are already using Gemini’s native audio capabilities to drive real business results, from mortgage processing to customer calls.</p><ul><li data-block-key="f9d5j"><i>“Users often forget they’re talking to AI within a minute of using Sidekick, and in some cases have thanked the bot after a long chat…New Live API AI capabilities offered through Gemini [2.5 Flash Native Audio] empower our merchants to win.”</i> – David Wurtz, VP of Product, Shopify</li><li data-block-key="cpoqr"><i>"By integrating the Gemini 2.5 Flash Native Audio model…we've significantly enhanced Mia's capabilities since launching in May 2025. This powerful combination has enabled us to generate over 14,000 loans for our broker partners.</i>" – Jason Bressler, Chief Technology Officer, United Wholesale Mortgage (UWM)</li><li data-block-key="5gvgc"><i>“Working with the Gemini 2.5 Flash Native Audio model through Vertex AI allows Newo.ai AI Receptionists to achieve unmatched conversational intelligence ... .They can identify the main speaker even in noisy settings, switch languages mid-conversation, and sound remarkably natural and emotionally expressive.”</i> – David Yang, Co-founder, Newo.ai</li></ul><h2 data-block-key="7lcen">Live Speech Translation</h2><p data-block-key="9k6cr">Gemini now natively supports new live speech-to-speech translation capabilities designed to handle both continuous listening and two-way conversation.</p><p data-block-key="38f3">With continuous listening, Gemini automatically translates speech in multiple languages into a single target language. This allows you to put headphones in and hear the world around you in your language.</p><p data-block-key="eq38s">For two-way conversation, Gemini’s live speech translation handles translation between two languages in real-time, automatically switching the output language based on who is speaking. For example, if you speak English and want to chat with a Hindi speaker, you’ll hear English translations in real-time in your headphones, while your phone broadcasts Hindi when you’re done speaking.</p><p data-block-key="86q6c">Gemini’s live speech translation has a number of key capabilities that help in the real world:</p><ul><li data-block-key="2afoq"><b>Language coverage</b>: Translates speech in over 70 languages and 2000 language pairs by combining Gemini model’s world knowledge and multilingual capabilities with its native audio capabilities</li><li data-block-key="di844"><b>Style transfer:</b> Captures the nuance of human speech, preserving the speaker’s intonation, pacing and pitch so the translation sounds natural.</li><li data-block-key="bdrko"><b>Multilingual input:</b> Understands multiple languages simultaneously in a single session, helping you follow multilingual conversations without needing to fiddle around with language settings.</li><li data-block-key="alfj9"><b>Auto detection:</b> Identifies the spoken language and begins translation, so you don’t even need to know what language is being spoken to start translating.</li><li data-block-key="4j5i0"><b>Noise robustness</b>: Filters out ambient noise so you can converse comfortably even in loud, outdoor environments.</li></ul></div>
  </uni-article-paragraph>
</section>

  

  
    
  
    



<uni-youtube-player-article
  index="6"
  page-title="Improved Gemini audio models for powerful voice interactions"
  thumbnail-alt="Video demo of Gemini&#x27;s live speech-to-speech translation capabilities"
  
  
  
  video-id="xdPIwgDriTg"
  video-type="video"
  
  
  >
</uni-youtube-player-article>










  


  

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Improved Gemini audio models for powerful voice interactions"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="61bfj">Starting today, you can try it in a new beta experience in the Google Translate app for <a href="https://blog.google/products/search/gemini-capabilities-translation-upgrades/">real-time translation in your headphones</a> by connecting them to your device and tapping “Live translate.” This experience is rolling out to all Android devices in the US, Mexico and India with support for iOS and more regions coming soon.</p><p data-block-key="nu4n">Based on feedback, we will continue to iterate on this experience and bring it to more Google products including the Gemini API in 2026.</p><h2 data-block-key="6eoc0">Get started today</h2><p data-block-key="d1rrs">Start building voice agents today with Gemini 2.5 Flash Native Audio, now generally available on <a href="https://cloud.google.com/blog/products/ai-machine-learning/gemini-live-api-available-on-vertex-ai">Vertex AI</a> and as preview in <a href="https://ai.google.dev/gemini-api/docs/live">the Gemini API</a>. Try it out in <a href="https://ai.dev/prompts/new_chat?model=gemini-2.5-flash-native-audio-preview-12-2025">Google AI Studio</a>.</p><p data-block-key="2c94r">Gemini 2.5 Flash and 2.5 Pro text-to-speech models are also available via the Gemini API in Google AI Studio. Get started with the <a href="https://ai.google.dev/gemini-api/docs/speech-generation">speech generation docs</a>, explore the <a href="https://ai.google.dev/gemini-api/docs/speech-generation#prompting-guide">prompting guide</a>, or check out the <a href="https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb">Gemini API Cookbook</a> to get started.</p></div>
  </uni-article-paragraph>
</section>

  


          
          

          
            


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
    "section_header": "Improved Gemini audio models for powerful voice interactions"
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
  href="https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/"
  class="uni-article-card"
  aria-label="Developer tools - Gemini Omni 1.1 Flash lets you build with more control - By Anish Nangia& Alisa Fortin - Aug 27, 2026"
  data-index="1"
  data-target="card"
  data-primaryTag="products - developer tools"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "Gemini Omni 1.1 Flash lets you build with more control",
    "link_url":  "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source_content": "Related stories",
    "related_index": "1",
    "related_article_tag": "products - developer tools",
    "article_name": "Gemini Omni 1.1 Flash lets you build with more control",
    "author_name": "Anish Nangia, Alisa Fortin",
    "content_type": "blogv2 | article page"
  }'
  data-theme-color="green"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["6-sided-cookie", "8-leaf-clover", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Omni_1-1_Flash_hero.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Omni_1-1_Flash_hero.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Omni_1-1_Flash_hero.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        Gemini Omni 1.1 Flash lets you build with more control
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Anish Nangia
          
            & 
            Alisa Fortin
          
        </span>
      
    </div>
  </div>
</a>

        
          




<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/"
  class="uni-article-card"
  aria-label="Gemini models - Intelligent transcription with Gemini 3.5 Transcribe - By Diego Melendo Casado& Luke Leonhard - Aug 26, 2026"
  data-index="2"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "Intelligent transcription with Gemini 3.5 Transcribe",
    "link_url":  "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source_content": "Related stories",
    "related_index": "2",
    "related_article_tag": "topics - gemini models",
    "article_name": "Intelligent transcription with Gemini 3.5 Transcribe",
    "author_name": "Diego Melendo Casado, Luke Leonhard",
    "content_type": "blogv2 | article page"
  }'
  data-theme-color="blue"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-sided-cookie", "bun", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_3-5_transcribe.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_3-5_transcribe.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_3-5_transcribe.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        Intelligent transcription with Gemini 3.5 Transcribe
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Diego Melendo Casado
          
            & 
            Luke Leonhard
          
        </span>
      
    </div>
  </div>
</a>

        
          




<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/what-full-stack-development-means/"
  class="uni-article-card"
  aria-label="Gemini models - What does “full\u002Dstack” AI actually mean? - By Lindsey Lanquist - Aug 21, 2026"
  data-index="3"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "What does “full\u002Dstack” AI actually mean?",
    "link_url":  "https://blog.google/innovation-and-ai/models-and-research/gemini-models/what-full-stack-development-means/",
    "source_content": "Related stories",
    "related_index": "3",
    "related_article_tag": "topics - gemini models",
    "article_name": "What does “full\u002Dstack” AI actually mean?",
    "author_name": "Lindsey Lanquist",
    "content_type": "blogv2 | Short Post"
  }'
  data-theme-color="blue"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-sided-cookie", "bun", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/thumbnail_BfIj9lP.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/thumbnail_BfIj9lP.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/thumbnail_BfIj9lP.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        What does “full-stack” AI actually mean?
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
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/"
  class="uni-article-card"
  aria-label="Gemini models - Introducing Gemini 3.7 Flash - By Tulsee Doshi - Aug 13, 2026"
  data-index="4"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "Introducing Gemini 3.7 Flash",
    "link_url":  "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "source_content": "Related stories",
    "related_index": "4",
    "related_article_tag": "topics - gemini models",
    "article_name": "Introducing Gemini 3.7 Flash",
    "author_name": "Tulsee Doshi",
    "content_type": "blogv2 | article page"
  }'
  data-theme-color="blue"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-sided-cookie", "bun", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-7-flash.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-7-flash.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-7-flash.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        Introducing Gemini 3.7 Flash
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Tulsee Doshi
          
        </span>
      
    </div>
  </div>
</a>

        
          




<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-experts-roundtable/"
  class="uni-article-card"
  aria-label="Gemini models - Omni experts share what excites them most about the model. - By Lindsey Lanquist - Aug 13, 2026"
  data-index="5"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "Omni experts share what excites them most about the model.",
    "link_url":  "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-experts-roundtable/",
    "source_content": "Related stories",
    "related_index": "5",
    "related_article_tag": "topics - gemini models",
    "article_name": "Omni experts share what excites them most about the model.",
    "author_name": "Lindsey Lanquist",
    "content_type": "blogv2 | Short Post"
  }'
  data-theme-color="neutral"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["4-sided-cookie", "bun", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Omni_experts_social.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Omni_experts_social.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Omni_experts_social.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        Omni experts share what excites them most about the model.
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
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-builders/"
  class="uni-article-card"
  aria-label="Gemini models - See what 5 builders are making with Gemini Omni - By Lindsey Lanquist - Aug 07, 2026"
  data-index="6"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "See what 5 builders are making with Gemini Omni",
    "link_url":  "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-builders/",
    "source_content": "Related stories",
    "related_index": "6",
    "related_article_tag": "topics - gemini models",
    "article_name": "See what 5 builders are making with Gemini Omni",
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
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Omni_hero.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Omni_hero.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Omni_hero.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        See what 5 builders are making with Gemini Omni
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
    "section_header": "Improved Gemini audio models for powerful voice interactions"
  }'>
  <section class="uni-footer__logo">
    <a href="https://www.google.com" aria-label="The Google logo">
      <svg
  
  
  
  
  
  
  
  aria-hidden="true"
  
  viewBox="0 0 396 130"
  
  
>
  <use
    xmlns:xlink="http://www.w3.org/1999/xlink"
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#google-logo"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#expand_more"></use>
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
        value="https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/"
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
        label="Malaysia (Melayu)"
        value="https://blog.google/intl/ms-my/"
        lang="ms-my"
        class="uni-lang-picker__option"
        >
        Malaysia (Melayu)
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#expand_more"></use>
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
              { "url": "/static/blogv2/js/csp/gtm.js?version=pr20260820-1820",
                "options": {
                  "async": false,
                  "defer": true
                }
              },
              { "url": "/static/keyword/js/all/index.js?version=pr20260820-1820",
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
