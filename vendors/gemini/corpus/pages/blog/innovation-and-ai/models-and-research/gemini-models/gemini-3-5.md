





<!DOCTYPE html>
<html class="no-js glue-flexbox  keyword-blog" lang="en-us" data-locale="en-us" data-version="pr20260820-1820">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <title>Gemini 3.5: frontier intelligence with action</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=1.0, minimum-scale=1.0" />
        <meta name="optimize_experiments" content="[]">

        
  




<!--Article Specific Metadata-->
<meta name="description" content="At Google I/O we released Gemini 3.5, our latest series of models combining frontier intelligence with action."/>
<meta name="keywords" content="None"/>
<meta name="article-author" content="Koray Kavukcuoglu, Jeff Dean, Oriol Vinyals, Noam Shazeer"/>
<meta name="robots" content="max-image-preview:large">

<!--Open Graph Metadata-->
<meta property="og:type" content="article" />
<meta property="og:title" content="Gemini 3.5: frontier intelligence with action"/>

<meta property="og:description" content="At Google I/O we released Gemini 3.5, our latest series of models combining frontier intelligence with action." />
<meta property="og:image" content="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-5__keywordstatement__metacard__light.width-1300.png" />
<meta property="og:site_name" content="Google" />
<meta property="og:url" content="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/" />
<meta property="article:publisher" content="https://www.facebook.com/Google/" />
<meta property="article:published_time" content="2026-05-19" />

<!--Twitter Card Metadata-->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:url" content="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/" />
<meta name="twitter:title" content="Gemini 3.5: frontier intelligence with action"/>
<meta name="twitter:description" content="At Google I/O we released Gemini 3.5, our latest series of models combining frontier intelligence with action." />
<meta name="twitter:image:src" content="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-5__keywordstatement__metacard__light.width-1300.png" />
<meta name="twitter:site" content="@google" />







        
  <meta name="page" content="84653" />
  <meta name="locale" content="en-us" />
  <meta name="published_time" content="2026-05-19T17:45:00+00:00" />
  <meta name="content_type" content="blogv2.articlepage" />
  <meta name="tags" content="AI,Gemini models" />
  <meta name="authors" content="Koray Kavukcuoglu,Jeff Dean,Oriol Vinyals,Noam Shazeer" />



        
        

        
        
  
  
  




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


        

<link rel="canonical" href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"/>

<link href="/favicon.ico" rel="icon">
<link href="/static/blogv2/images/apple-touch-icon.png?version=pr20260820-1820" rel="apple-touch-icon">


  <link rel="alternate" hreflang="x-default" href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">

  <link rel="alternate" hreflang="en-us" href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">

  <link rel="alternate" hreflang="fr-ca" href="https://blog.google/intl/fr-ca/produits/explorez-obtenez-des-reponses/gemini-3-5/">

  <link rel="alternate" hreflang="pt-br" href="https://blog.google/intl/pt-br/gemini-3-5/">

  <link rel="alternate" hreflang="es" href="https://blog.google/intl/es-419/actualizaciones-de-producto/gemini-3-5/">

  <link rel="alternate" hreflang="fr-fr" href="https://blog.google/intl/fr-fr/nouveautes-produits/io-gemini-3-5/">

  <link rel="alternate" hreflang="en-ng" href="https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/">

  <link rel="alternate" hreflang="pl-pl" href="https://blog.google/intl/pl-pl/nowosci-produktowe/sztuczna-inteligencja/gemini-3-5/">

  <link rel="alternate" hreflang="ja-jp" href="https://blog.google/intl/ja-jp/company-news/technology/gemini-3-5/">

  <link rel="alternate" hreflang="zh-hant" href="https://blog.google/intl/zh-tw/products/explore-get-answers/gemini-3-5/">


        <meta property="gtm-tag" content="GTM-TRV24V">



        <!-- https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API -->


      </head>

    <body class="template-articlepage keyword-blog">
        
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TRV24V" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>


        


<div class="data-layer-init-data" data-ga4-analytics='
  {
    "event": "dataLayer_initialized",
    
      "page_name": "Gemini 3.5: frontier intelligence with action",
    
    "experiments": "undefined",
    "locale": "en-us",
    "page_type": "blogv2 | article page",
    "primary_tag": "topics - gemini models",
    "secondary_tags": "AI",
    
      "landing_page_tags": "topics - ai",
    
    
      "article_name": "Gemini 3.5: frontier intelligence with action",
      "author_name": "Koray Kavukcuoglu, Jeff Dean, Oriol Vinyals, Noam Shazeer",
    
    "publish_date": "2026-05-19|17:45",
    "hero_media": "image",
    
      "special_hero": "undefined",
    
    "days_since_published": "103",
    
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
        
        
          <p class="uni-nav-article__article-title font-body-m">Gemini 3.5: frontier intelligence with action</p>
        
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
  <div class="uni-article-progress-bar__title uni-article-progress-bar__ellipsis">Gemini 3.5: frontier intelligence with action</div>
  <div class="uni-article-progress-bar__social"
    data-analytics-module='{
      "module_name": "Progress Bar",
      "section_header": "Gemini 3.5: frontier intelligence with action"
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
    href="https://twitter.com/intent/tweet?text=Gemini%203.5%3A%20frontier%20intelligence%20with%20action%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
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
    href="https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.5%3A%20frontier%20intelligence%20with%20action&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
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
    href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/&title=Gemini%203.5%3A%20frontier%20intelligence%20with%20action"
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
    
      href="mailto:?subject=Gemini%203.5%3A%20frontier%20intelligence%20with%20action&body=Check out this article on the Keyword:%0A%0AGemini%203.5%3A%20frontier%20intelligence%20with%20action%0A%0AAt Google I/O we released Gemini 3.5, our latest series of models combining frontier intelligence with action.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
    
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
    <input class="h-c-copy copy-link__url" value="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/" id="copy-link" readonly="readonly" type="text"/>
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
        value="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
        lang="en-us"
        class="uni-lang-picker__option"
        
          selected="selected"
          data-selected-index="0"
        >
        Global (English)
      </option>
      
      <option
        label="Africa (English)"
        value="https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/"
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
        value="https://blog.google/intl/pt-br/gemini-3-5/"
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
        value="https://blog.google/intl/fr-ca/produits/explorez-obtenez-des-reponses/gemini-3-5/"
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
        value="https://blog.google/intl/fr-fr/nouveautes-produits/io-gemini-3-5/"
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
        value="https://blog.google/intl/ja-jp/company-news/technology/gemini-3-5/"
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
        value="https://blog.google/intl/es-419/actualizaciones-de-producto/gemini-3-5/"
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
        value="https://blog.google/intl/pl-pl/nowosci-produktowe/sztuczna-inteligencja/gemini-3-5/"
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
        value="https://blog.google/intl/zh-tw/products/explore-get-answers/gemini-3-5/"
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
         "section_header": "Gemini 3.5: frontier intelligence with action"
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
      href="https://twitter.com/intent/tweet?text=Gemini%203.5%3A%20frontier%20intelligence%20with%20action%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
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
      href="https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.5%3A%20frontier%20intelligence%20with%20action&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
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
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/&title=Gemini%203.5%3A%20frontier%20intelligence%20with%20action"
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
      
        href="mailto:?subject=Gemini%203.5%3A%20frontier%20intelligence%20with%20action&body=Check out this article on the Keyword:%0A%0AGemini%203.5%3A%20frontier%20intelligence%20with%20action%0A%0AAt Google I/O we released Gemini 3.5, our latest series of models combining frontier intelligence with action.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
      
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
      data-copy-text="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
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
        "section_header": "Gemini 3.5: frontier intelligence with action"
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#uni-icon-chevron-right"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#uni-icon-chevron-right"></use>
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#uni-icon-chevron-right"></use>
</svg>

    </button>
  </uni-breadcrumbs>


          </div>
        
      </div>
      
      <div class="uni-grid uni-article-hero__content-grid">
        <div class="uni-grid__col--span-4 uni-grid__col--span-12-tablet uni-grid__col--span-8-desktop uni-grid__col--start-3-desktop uni-article-hero__main-content">
          <h1 class="uni-article-hero__title font-h1">Gemini 3.5: frontier intelligence with action</h1>

          <div class="uni-article-hero__meta-wrapper">
            <div class="uni-article-hero__meta-header">
              
              <div class="uni-article-hero__meta-aside">
                
                  <p class="uni-article-hero__date font-body-s">May 19, 2026</p>
                
                
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
      href="https://twitter.com/intent/tweet?text=Gemini%203.5%3A%20frontier%20intelligence%20with%20action%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
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
      href="https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.5%3A%20frontier%20intelligence%20with%20action&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
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
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/&title=Gemini%203.5%3A%20frontier%20intelligence%20with%20action"
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
      
        href="mailto:?subject=Gemini%203.5%3A%20frontier%20intelligence%20with%20action&body=Check out this article on the Keyword:%0A%0AGemini%203.5%3A%20frontier%20intelligence%20with%20action%0A%0AAt Google I/O we released Gemini 3.5, our latest series of models combining frontier intelligence with action.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
      
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
      data-copy-text="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">
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


            
            
              <p class="uni-article-hero__abstract font-body-xl">
                Gemini 3.5 is built to help you execute complex, agentic workflows.
              </p>
            
          </div>

          <hr class="uni-article-hero__divider">

          
          <div class="uni-article-hero__authors-actions">
            <div class="uni-article-hero__authors-wrapper">
              
                

<div class="uni-article-hero__authors uni-grid">
  
    
    <div class="uni-article-hero__author">
      <div class="uni-article-hero__author-info">
        
          
          <a href="https://blog.google/authors/koray-kavukcuoglu/" class="uni-article-hero__author-link">
        
            <p class="uni-article-hero__author-name font-author-name">Koray Kavukcuoglu</p>
            
              
                <p class="uni-article-hero__author-title font-author-info">CTO, Google DeepMind and Chief AI Architect, Google</p>
              
            
        
          </a>
        
      </div>
    </div>
  
    
    <div class="uni-article-hero__author">
      <div class="uni-article-hero__author-info">
        
          
          <a href="https://blog.google/authors/jeff-dean/" class="uni-article-hero__author-link">
        
            <p class="uni-article-hero__author-name font-author-name">Jeff Dean</p>
            
              
                <p class="uni-article-hero__author-title font-author-info">Chief Scientist, Google DeepMind and Google Research</p>
              
            
        
          </a>
        
      </div>
    </div>
  
    
    <div class="uni-article-hero__author">
      <div class="uni-article-hero__author-info">
        
            <p class="uni-article-hero__author-name font-author-name">Oriol Vinyals</p>
            
              
                <p class="uni-article-hero__author-title font-author-info">Vice President, Google DeepMind</p>
              
            
        
      </div>
    </div>
  
    
    <div class="uni-article-hero__author">
      <div class="uni-article-hero__author-info">
        
            <p class="uni-article-hero__author-name font-author-name">Noam Shazeer</p>
            
              
                <p class="uni-article-hero__author-title font-author-info">Vice President, Google DeepMind</p>
              
            
        
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
      href="https://twitter.com/intent/tweet?text=Gemini%203.5%3A%20frontier%20intelligence%20with%20action%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
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
      href="https://www.facebook.com/sharer/sharer.php?caption=Gemini%203.5%3A%20frontier%20intelligence%20with%20action&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
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
      href="https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/&title=Gemini%203.5%3A%20frontier%20intelligence%20with%20action"
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
      
        href="mailto:?subject=Gemini%203.5%3A%20frontier%20intelligence%20with%20action&body=Check out this article on the Keyword:%0A%0AGemini%203.5%3A%20frontier%20intelligence%20with%20action%0A%0AAt Google I/O we released Gemini 3.5, our latest series of models combining frontier intelligence with action.%0A%0Ahttps://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
      
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
      data-copy-text="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">
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
            alt="Gemini 3.5 text and multi-colored star icon on an abstract blue background."
            class="uni-article-hero__image uni-progressive-image--blur"
            data-component="uni-progressive-image"
            fetchpriority="high"
            src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-5__keyword__blog-header_.width-200.format-webp.webp"
            
              data-sizes="(max-width: 1023px) 100vw, (max-width: 1440px) 95vw, 1408px"
              data-srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-5__keyword__blog-header_.width-450.format-webp.webp 450w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-5__keyword__blog-header_.width-900.format-webp.webp 900w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-5__keyword__blog-header.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-5__keyword__blog-header.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3-5__keyword__blog-header.width-2200.format-webp.webp 2200w"
            
            >
        </div>
      </div>
      
    </div>
  





      
    </div>
  </div>
</section>

    <div class="uni-page uni-grid article-container__ai-box-container">
      <div class="article-container__ai-box uni-grid__col--layout-6">
        
        
          
        
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
      "section_header": "Gemini 3.5: frontier intelligence with action"
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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#mi-expand"></use>
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
              href="#gemini-3-5-flash"
              data-component="uni-article-jumplink">
              Gemini 3.5 Flash
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#frontier-intelligence"
              data-component="uni-article-jumplink">
              Frontier intelligence, exceptional speed
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#agentic-tasks"
              data-component="uni-article-jumplink">
              Agentic tasks at scale
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#richer-graphics"
              data-component="uni-article-jumplink">
              Richer graphics
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#real-world"
              data-component="uni-article-jumplink">
              Real-world impact
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#personal-agents"
              data-component="uni-article-jumplink">
              Personal AI agents
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#frontier-safeguards"
              data-component="uni-article-jumplink">
              Built with Frontier safeguards
            </a>
          </li>
          
          <li class="uni-article-jumplinks__item">
            <a
              class="uni-article-jumplinks__anchor font-body-s"
              href="#available-today"
              data-component="uni-article-jumplink">
              Available today
            </a>
          </li>
          
        </ul>
      </nav>
    </details>
  </uni-article-jumplinks>
</div>

            
            
              
            
          </div>
        
        
        <div class="uni-content uni-blog-article-container article-container__content
                    "
            data-reading-time="true"
            data-component="uni-article-body">

          
          
<!--article text-->

  
    

<section
  class="uni-page uni-grid uni-article-paragraph"
  data-analytics-module='{
    "module_name": "Paragraph",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="6kaby">Today, we’re introducing Gemini 3.5, our latest family of models combining frontier intelligence with action. This represents a major leap forward in building more capable, intelligent agents. We’re kicking off the series by releasing 3.5 Flash. It delivers frontier performance for agents and coding, excelling at complex long-horizon tasks that deliver real-world utility.</p><p data-block-key="crnm6">3.5 Flash is available today to billions of people globally:</p><ul><li data-block-key="7tqk3">For everyone via the Gemini app and AI Mode in <a href="https://blog.google/products-and-platforms/products/search/search-io-2026">Google Search</a></li><li data-block-key="c8uvb">For developers in our agent-first development platform Google Antigravity and Gemini API in Google AI Studio and Android Studio</li><li data-block-key="ftd63">For enterprises in Gemini Enterprise Agent Platform and Gemini Enterprise.</li></ul><p data-block-key="dqekg">We’re also hard at work on 3.5 Pro. It's already being used internally, and we look forward to rolling it out next month.</p></div>
  </uni-article-paragraph>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="gemini-3-5-flash"
    aria-label="Gemini 3.5 Flash"
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="6kaby">3.5 Flash: frontier performance for agents and coding</h2><p data-block-key="7pevi">Gemini 3.5 Flash delivers intelligence that rivals large flagship models on multiple dimensions, at the speeds you have come to expect from the Flash series. It’s our strongest agentic and coding model yet, outperforming Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 (76.2%), GDPval-AA (1656 Elo) and MCP Atlas (83.6%), and leading in multimodal understanding (84.2% on CharXiv Reasoning). When looking at output tokens per second, it is 4 times faster than other frontier models.</p></div>
  </uni-article-paragraph>
</section>

  

  
    





  
  
  
  
  

























<section class="uni-page uni-grid uni-inline-image-section" data-component="uni-inline-image">
  <uni-inline-image
    class="uni-inline-image uni-inline-image--full"
    alignment="full"
    alt-text="Performance comparison table of Gemini, Claude, and GPT models across various benchmarks, highlighting Gemini 3.5 Flash."
    external-image=""
    or-mp4-video-title=""
    or-mp4-video-url=""
    section-header="Gemini 3.5: frontier intelligence with action"
    
    
    
      external-link="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-3-5__benchmarks__light.gif"
    
    
    
      autoplay="true"
    
  >
    

    
      <div slot="image-slot">
        <img
          alt="Performance comparison table of Gemini, Claude, and GPT models across various benchmarks, highlighting Gemini 3.5 Flash."
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-3-5__benchmarks__light.gif"
          
            loading="lazy"
            sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
            srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-3-5__benchmarks__light.gif 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-3-5__benchmarks__light.gif 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-3-5__benchmarks__light.gif 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-3-5__benchmarks__light.gif 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini-3-5__benchmarks__light.gif 2000w"
          
        >
      </div>
    
  </uni-inline-image>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="frontier-intelligence"
    aria-label="Frontier intelligence, exceptional speed"
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="6kaby">Landing in the top-right quadrant of the Artificial Analysis index, 3.5 Flash delivers frontier-level intelligence at exceptional speed — proving you no longer have to trade quality for latency.</p></div>
  </uni-article-paragraph>
</section>

  

  
    





  
  
  
  
  

























<section class="uni-page uni-grid uni-inline-image-section" data-component="uni-inline-image">
  <uni-inline-image
    class="uni-inline-image uni-inline-image--full"
    alignment="full"
    alt-text="an image showing &quot;Artificial Analysis Intelligence Index vs Output Speed"
    external-image=""
    or-mp4-video-title=""
    or-mp4-video-url=""
    section-header="Gemini 3.5: frontier intelligence with action"
    
    
    
      external-link="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/GeminiModels_Artificial_Analysis_Intelligence_I.original.png"
    
    
    
      autoplay="true"
    
  >
    

    
      <div slot="image-slot">
        <img
          alt="an image showing &quot;Artificial Analysis Intelligence Index vs Output Speed"
          src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/GeminiModels_Artificial_Analysis.width-1200.format-webp.webp"
          
            loading="lazy"
            sizes="(max-width: 768px) 100vw, (max-width: 1024px) 80vw, 1200px"
            srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/GeminiModels_Artificial_Analysis_.width-500.format-webp.webp 500w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/GeminiModels_Artificial_Analysis_.width-800.format-webp.webp 800w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/GeminiModels_Artificial_Analysis.width-1200.format-webp.webp 1200w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/GeminiModels_Artificial_Analysis.width-1600.format-webp.webp 1600w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/GeminiModels_Artificial_Analysis.width-2000.format-webp.webp 2000w"
          
        >
      </div>
    
  </uni-inline-image>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="agentic-tasks"
    aria-label="Agentic tasks at scale"
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="6kaby">3.5 Flash: agentic tasks at scale</h2><p data-block-key="8hu1m">This balance of speed and performance makes 3.5 Flash ideal for tackling long-horizon agentic tasks. What used to take a developer days or an auditor weeks, 3.5 Flash can now help complete in a fraction of the time, often at less than half the cost of other frontier models. It rapidly plans, builds and iterates to solve real-world problems, whether it’s developing new applications, maintaining codebases or helping to prepare financial documents.</p><p data-block-key="f6s3a">When coupled with the updated Antigravity harness, 3.5 Flash becomes a powerful engine for deploying collaborative subagents to tackle problems at scale for the most demanding use cases. Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance.</p></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header="Powered by Antigravity, 3.5 Flash executes multi-step workflows to automatically rename and categorize unstructured assets based on dynamic criteria."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/housecleaning.mp4"
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="house cleaning demo using Gemini 3.5"
  video-title="house cleaning"
  
  
  
    autoplay="true"
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="pf87z">Powered by Antigravity, 3.5 Flash executes multi-step workflows to automatically rename and categorize unstructured assets based on dynamic criteria.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header="Leveraging Antigravity, 3.5 Flash uses two agents to synthesize the AlphaZero paper and code a fully playable game in six hours."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Compressed_alphazero_demo_658w6BO.mp4"
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="MP4 showing AlphaZero"
  video-title="AlphaZero"
  
  
  
    autoplay="true"
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="p1ahh">Leveraging Antigravity, 3.5 Flash uses two agents to synthesize the AlphaZero paper and code a fully playable game in six hours.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="2"
  accordion-header="3.5 Flash uses the Antigravity harness to transform a messy legacy codebase to Next.js."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/AGY-FLASH35.mp4"
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="mp4 showing how 3.5 Flash uses the Antigravity harness to transform a messy legacy codebase"
  video-title="AGY Flash35"
  
  
  
    autoplay="true"
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="p1ahh">3.5 Flash uses the Antigravity harness to transform a messy legacy codebase to Next.js.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="3"
  accordion-header="3.5 Flash uses subagents to create new city landscapes in Antigravity."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Compressed_FINAL_AntiGrav_AgenticCities_DZ_v24_1_1_z5UxMwA.mp4"
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="mp4 showing how 3.5 Flash uses sub agents to create new city landscapes in antigravity"
  video-title="antigravity agentic cities"
  
  
  
    autoplay="true"
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="j2sbc">3.5 Flash uses subagents to create new city landscapes in Antigravity.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="4"
  accordion-header="3.5 Flash uses two agents: a builder and a player, working in a rapid self-improvement loop to develop a game in Antigravity."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Compressed_FINAL_self-improving-games_yoFcPns.mp4"
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="mp4 showing how 3.5 Flash uses two agents: a builder and a player, working in a rapid self-improvement loop to develop a game in Antigravity"
  video-title="self-improving games"
  
  
  
    autoplay="true"
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="j2sbc">3.5 Flash uses two agents: a builder and a player, working in a rapid self-improvement loop to develop a game in Antigravity.</p></div>
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
    id="richer-graphics"
    aria-label="Richer graphics"
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="6kaby">Building on the strong multimodal foundation of Gemini 3, 3.5 Flash generates richer, more interactive web UIs and graphics.</p></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header="3.5 Flash creates interactive animations for a research paper on AI Studio."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Compressed_animated-papers_1_1.mp4"
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="an mp4 showing flash 3.5 creating interactive animations"
  video-title="animated papers"
  
  
  
    autoplay="true"
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="1au38">3.5 Flash creates interactive animations for a research paper on AI Studio.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header="3.5 Flash turns a plain text description into interactive hardware on AI Studio."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Compressed_animated_html_1.mp4"
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="mp4 showing 3.5 Flash turning a plain text description into interactive hardware on AI Studio."
  video-title="animated html"
  
  
  
    autoplay="true"
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="1au38">3.5 Flash turns a plain text description into interactive hardware on AI Studio.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="2"
  accordion-header="3.5 Flash executes multiple concepts in parallel to build a full branding concept for a school fundraiser on AI Studio."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Compressed_FINAL_gemini_brandAgents_260518c_1_LPpucSO.mp4"
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="mp4 showing 3.5 Flash executing multiple concepts in parallel to build a full branding concept for a school fundraiser on AI Studio."
  video-title="Gemini brand agents"
  
  
  
    autoplay="true"
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="1au38">3.5 Flash executes multiple concepts in parallel to build a full branding concept for a school fundraiser on AI Studio.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="3"
  accordion-header="3.5 Flash generates different UX approaches for a checkout flow in just 60 seconds on AI Studio."
>
  <div slot="content">
    






















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Video",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Compressed_FINAL_Payments_UI_04_1.mp4"
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="mp4 showing 3.5 Flash generating different UX approaches"
  video-title="final payments"
  
  
  
    autoplay="true"
  
  >
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="1au38">3.5 Flash generates different UX approaches for a checkout flow in just 60 seconds on AI Studio.</p></div>
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
    id="real-world"
    aria-label="Real-world impact"
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="6kaby">3.5 Flash: real-world impact</h2><p data-block-key="aho2m">3.5 Flash’s real-world agentic capabilities are already driving meaningful progress for our developers and enterprises alike. In developing the 3.5 model series, we worked closely with industry partners to understand where toil and complexity arose in their workflows. Partners are seeing meaningful impact — from banks and fintechs automating multi-week workflows to data science teams unearthing insights amidst complex data environments.</p></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header="Shopify is running subagents in parallel to analyze complex data over a long horizon for more accurate merchant growth forecasts at a global scale."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Gemini 3.5: frontier intelligence with action"
    }'
    index="1"
    thumbnail-alt="YouTube video for shopify"
    video-id="zdY0QaI1paI"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="d09j1">Shopify is running subagents in parallel to analyze complex data over a long horizon for more accurate merchant growth forecasts at a global scale.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header="Macquarie Bank is piloting how 3.5 Flash can accelerate customer onboarding by reasoning over complex 100+ page documents, retrieving relevant information and making reliable recommendations with low latency."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Gemini 3.5: frontier intelligence with action"
    }'
    index="2"
    thumbnail-alt="YouTube video showing macquarie bank"
    video-id="CLxFAk5SvB8"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="d09j1">Macquarie Bank is piloting how 3.5 Flash can accelerate customer onboarding by reasoning over complex 100+ page documents, retrieving relevant information and making reliable recommendations with low latency.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="2"
  accordion-header="Salesforce is integrating 3.5 Flash into Agentforce to reliably automate complicated enterprise tasks by deploying multiple subagents that retain context and execute complex, multi-turn tool calling."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Gemini 3.5: frontier intelligence with action"
    }'
    index="3"
    thumbnail-alt="YouTube video for salesforce"
    video-id="9qfJzcq_ZOg"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="d09j1">Salesforce is integrating 3.5 Flash into Agentforce to reliably automate complicated enterprise tasks by deploying multiple subagents that retain context and execute complex, multi-turn tool calling.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="3"
  accordion-header="3.5 Flash is helping Ramp enable smarter, more reliable OCR through multimodal understanding of complex invoices combined with reasoning over historical patterns."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Gemini 3.5: frontier intelligence with action"
    }'
    index="4"
    thumbnail-alt="YouTube video for ramp"
    video-id="LrrR8OZTrbA"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="d09j1">3.5 Flash is helping Ramp enable smarter, more reliable OCR through multimodal understanding of complex invoices combined with reasoning over historical patterns.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="4"
  accordion-header="Xero is deploying agents to autonomously manage complex, multi-week workflows, such as identifying suppliers and gathering information for 1099 tax forms, enabling small businesses to automate tedious admin tasks."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Gemini 3.5: frontier intelligence with action"
    }'
    index="5"
    thumbnail-alt="YouTube video for xero"
    video-id="0WKFm_t-Nk4"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="d09j1">Xero is deploying agents to autonomously manage complex, multi-week workflows, such as identifying suppliers and gathering information for 1099 tax forms, enabling small businesses to automate tedious admin tasks.</p></div>
          </div>
        

        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="5"
  accordion-header="Databricks is using agentic workflows to monitor and retrieve real-time information, reason across massive datasets to diagnose issues, identify fixes and propose solutions for data scientists."
>
  <div slot="content">
    



<div class="uni-media-carousel__youtube">
  <uni-youtube-player-media-carousel
    data-analytics-module='{
      "module_name": "Media Carousel/YouTube Video",
      "section_header": "Gemini 3.5: frontier intelligence with action"
    }'
    index="6"
    thumbnail-alt="YouTube video for databricks"
    video-id="fskhwriwEh0"
    video-type="video"
    
    >
  </uni-youtube-player-media-carousel>
</div>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        
          <div>
            <div class="rich-text"><p data-block-key="d09j1">Databricks is using agentic workflows to monitor and retrieve real-time information, reason across massive datasets to diagnose issues, identify fixes and propose solutions for data scientists.</p></div>
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
    id="personal-agents"
    aria-label="Personal AI agents"
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="6kaby">Personal AI agents: built with 3.5 Flash</h2><p data-block-key="ev2g0">3.5 Flash is now the default model for the Gemini app and AI Mode in Search globally. At I/O today, we showed how its agentic capabilities are powering new features to bring frontier-level intelligence to your daily life.</p><p data-block-key="6ejcq">The new Gemini Spark, your personal AI agent, uses 3.5 Flash. It runs 24/7, helping you navigate your digital life, taking action on your behalf while under your direction. We’re starting to roll out Gemini Spark to trusted testers today, and we’re planning on bringing the Beta to Google AI Ultra subscribers in the US next week.</p></div>
  </uni-article-paragraph>
</section>

  

  
    











<section class="uni-page--fullbleed uni-media-carousel-wrapper"
  data-analytics-module='{
    "module_name": "Media Carousel",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  >
  <uni-media-carousel class="uni-media-carousel uni-page uni-grid" data-shape-context-provider>
    <uni-media-carousel-viewport slot="viewport" class="uni-media-carousel__viewport">
      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="0"
  accordion-header="Gemini Spark uses 3.5 Flash to help accomplish these tasks"
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="an image of Gemini Spark"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="an image of Gemini Spark"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_1.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_1.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_1.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        

        
          <div>
            <div class="rich-text"><p data-block-key="rwawx">Gemini Spark uses 3.5 Flash to help accomplish these tasks</p></div>
          </div>
        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="1"
  accordion-header="Gemini Spark uses 3.5 Flash to help accomplish these tasks"
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="an image of Gemini Spark"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="an image of Gemini Spark"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_2.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_2.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_2.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        

        
          <div>
            <div class="rich-text"><p data-block-key="o3yud">Gemini Spark uses 3.5 Flash to help accomplish these tasks</p></div>
          </div>
        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="2"
  accordion-header="Gemini Spark uses 3.5 Flash to help accomplish these tasks"
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="an image of Gemini Spark"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="an image of Gemini Spark"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_3.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_3.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_3.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        

        
          <div>
            <div class="rich-text"><p data-block-key="jyv5t">Gemini Spark uses 3.5 Flash to help accomplish these tasks</p></div>
          </div>
        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="3"
  accordion-header="Gemini Spark uses 3.5 Flash to help accomplish these tasks"
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="an image of Gemini Spark"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="an image of Gemini Spark"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_4.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_4.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_4.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        

        
          <div>
            <div class="rich-text"><p data-block-key="r7dda">Gemini Spark uses 3.5 Flash to help accomplish these tasks</p></div>
          </div>
        
      </div>
    </div>
  
</uni-media-carousel-slide>

      
        


<uni-media-carousel-slide
  class="uni-media-carousel__slide"
  data-theme="blue"
  
    shapes='["4-sided-cookie", "bun", "square"]'
  
  data-index="4"
  accordion-header="Gemini Spark uses 3.5 Flash to help accomplish these tasks"
>
  <div slot="content">
    




  
  
  



















<uni-media
  data-analytics-module='{
    "module_name": "Media Carousel/Image",
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'
  or-mp4-video-url=""
  section-header="Gemini 3.5: frontier intelligence with action"
  alt-text="an image of Gemini Spark"
  video-title=""
  
  
  
    autoplay="true"
  
  >
  
    <div slot="image-slot">
      <img
        alt="an image of Gemini Spark"
        src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_5.width-100.format-webp.webp"
        
          loading="lazy"
          data-loading='{
            "mobile": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_5.width-500.format-webp.webp",
            "desktop": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Spark_-_5.width-1000.format-webp.webp"
          }'
        
      >
    </div>
  
</uni-media>

  </div>

  
    <div slot="caption" class="font-caption">
      <div class="uni-media-carousel__caption-within">
        

        

        
          <div>
            <div class="rich-text"><p data-block-key="7t21n">Gemini Spark uses 3.5 Flash to help accomplish these tasks</p></div>
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><p data-block-key="6kaby">The enhanced agentic coding capabilities of 3.5 Flash are also delivering even more intelligent experiences across Search, from introducing new information agents that work for you 24/7 to unlocking more dynamic generative UI experiences. <a href="https://blog.google/products-and-platforms/products/search/search-io-2026">Learn more in our blog post</a>.</p></div>
  </uni-article-paragraph>
</section>

  

  
    





























<section class="uni-page uni-grid uni-inline-image-section" data-component="uni-inline-image">
  <uni-inline-image
    class="uni-inline-image uni-inline-image--full"
    alignment="full"
    alt-text="mp4 showing search leveraging 3.5 flash"
    external-image=""
    or-mp4-video-title="gen widgets"
    or-mp4-video-url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/AIM-GenWidgets_Gyro_1920x1080_small_16D0pmZ.mp4"
    section-header="Gemini 3.5: frontier intelligence with action"
    
    
    
    
    
      autoplay="true"
    
  >
    
      <div slot="caption-slot">
        <div class="rich-text"><p data-block-key="ym1in">Search leverages 3.5 Flash to build an interactive visual explaining Gyroid patterns.</p><p data-block-key="8hfrg"></p></div>
      </div>
    

    
  </uni-inline-image>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="frontier-safeguards"
    aria-label="Built with Frontier safeguards"
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="6kaby">Gemini 3.5: built with frontier safeguards</h2><p data-block-key="312p2">Gemini 3.5 was developed in accordance with our Frontier Safety Framework. We have strengthened our cyber and CBRN safeguards, which means it's less likely to generate harmful content, and to mistakenly refuse to answer safe queries. We achieve this with new, more advanced safety training and mitigations, including <a href="https://arxiv.org/abs/2601.11516v4">interpretability tools</a> that help check and understand the AI's inner reasoning before it provides a response.</p></div>
  </uni-article-paragraph>
</section>

  

  
    <div class="uni-page uni-grid">
  <section
    id="available-today"
    aria-label="Available today"
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
  }'>
  <uni-article-paragraph class="uni-article-paragraph__container uni-grid__col--layout-6">
    <div class="rich-text"><h2 data-block-key="6kaby">3.5 Flash is available today</h2><p data-block-key="9p7uq">Gemini 3.5 Flash is generally available via Google Antigravity, the Gemini API in Google AI Studio and Android Studio, <a href="https://console.cloud.google.com/agent-platform/overview">Gemini Enterprise Agent Platform</a> and <a href="https://cloud.google.com/gemini-enterprise?e=48754805">Gemini Enterprise</a>. It’s also now available to everyone in the Gemini app and AI Mode in Search. On behalf of the entire Gemini team, we can’t wait to see what you build.</p></div>
  </uni-article-paragraph>
</section>

  

  
    








<section class="uni-page">

  <uni-related-content-tout class="uni-related-content-tout uni-grid "
    title="I/O 2026"
    cta="See more"
    summary="Here’s a look at everything we announced at Google I/O 2026."
    hideImage="False"
    eyebrow="Collection"
    image-alt-text="The image shows a colorful abstract design with the Google I/O 2026 logo."
    fullUrl="https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-collection/"
    pageType="collectiondetailpage"
    
      
        
        imageUrl="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/IOCollection_social.width-800.format-webp.webp"
      
    
    
    data-analytics-module='{
      "module_name": "Related Content Tout",
      "section_header": "I/O 2026"
    }'
    
    
      data-theme-color="neutral"
    
  >
    <div class="uni-related-content-tout__container uni-grid__col--span-4 uni-grid__col--span-12-tablet uni-grid__col--start-1-tablet uni-grid__col--span-8-desktop uni-grid__col--start-3-desktop"
      role="group" aria-labelledby="tout-title"
      >
      <div class="uni-related-content-tout__content">
        
          <p class="uni-related-content-tout__eyebrow font-eyebrow">Collection</p>
        

        <h2 id="tout-title" class="uni-related-content-tout__title font-h4">
          I/O 2026
        </h2>

        
          <div class="uni-related-content-tout__summary font-body-s">Here’s a look at everything we announced at Google I/O 2026.</div>
        

        
          <div class="uni-related-content-tout__cta-container">
            <uni-cta emphasis="low" icon-id-right="arrow-forward"
              aria-label="See more" href="https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-collection/"
            >
              See more
            </uni-cta>
          </div>
        
      </div>
      <div class="uni-related-content-tout__image-container">
        
          
            
            
            

            <img
              class="uni-related-content-tout__image"
              srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/IOCollection_social.width-800.format-webp.webp 800w,
                https://storage.googleapis.com/gweb-uniblog-publish-prod/images/IOCollection_social.width-1600.format-webp.webp 1600w,
                https://storage.googleapis.com/gweb-uniblog-publish-prod/images/IOCollection_social.width-2200.format-webp.webp 2200w"
              sizes="(max-width: 1023px) 100vw, 50vw"
              src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/IOCollection_social.width-800.format-webp.webp"
              alt="The image shows a colorful abstract design with the Google I/O 2026 logo."
              fetchpriority="high"
              loading="eager"
              decoding="async"
            >
          
        
      </div>
    </div>
  </uni-related-content-tout>

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
    href="/static/blogv2/images/icons.svg?version=pr20260820-1820#check-circle"></use>
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
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
          
        

        
          
          
          
            <li class="uni-blog-article-tags__tags-item">
              

  <a class="uni-blog-article-tags__tags-value font-body-s uni-blog-article-tags__theme-purple uni-blog-article-tags__link-active"
     href="https://blog.google/innovation-and-ai/technology/ai/"
     

data-ga4-analytics-landing-lead='{
  "event": "landing_page_lead",
  "link_text": "AI"
}'
>
    AI
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
  href="https://blog.google/products-and-platforms/products/search/book-travel-ai-mode/"
  class="uni-article-card"
  aria-label="Search - 3 new ways to plan and book travel in Search - By James Byers - Aug 27, 2026"
  data-index="1"
  data-target="card"
  data-primaryTag="products - search"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "3 new ways to plan and book travel in Search",
    "link_url":  "https://blog.google/products-and-platforms/products/search/book-travel-ai-mode/",
    "source_content": "Related stories",
    "related_index": "1",
    "related_article_tag": "products - search",
    "article_name": "3 new ways to plan and book travel in Search",
    "author_name": "James Byers",
    "content_type": "blogv2 | article page"
  }'
  data-theme-color="aquamarine"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["8-leaf-clover", "ghost-ish", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Search_Travel_Blog_He.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Search_Travel_Blog_He.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Search_Travel_Blog_He.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        3 new ways to plan and book travel in Search
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            James Byers
          
        </span>
      
    </div>
  </div>
</a>

        
          




<a
  href="https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/"
  class="uni-article-card"
  aria-label="Developer tools - Gemini Omni 1.1 Flash lets you build with more control - By Anish Nangia& Alisa Fortin - Aug 27, 2026"
  data-index="2"
  data-target="card"
  data-primaryTag="products - developer tools"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "Gemini Omni 1.1 Flash lets you build with more control",
    "link_url":  "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source_content": "Related stories",
    "related_index": "2",
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
  data-index="3"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "Intelligent transcription with Gemini 3.5 Transcribe",
    "link_url":  "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source_content": "Related stories",
    "related_index": "3",
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
  href="https://blog.google/products-and-platforms/products/search/home-decor-tips/"
  class="uni-article-card"
  aria-label="Search - 5 ways to upgrade your home decor with Google Search - By Megan Stoner - Aug 25, 2026"
  data-index="4"
  data-target="card"
  data-primaryTag="products - search"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "5 ways to upgrade your home decor with Google Search",
    "link_url":  "https://blog.google/products-and-platforms/products/search/home-decor-tips/",
    "source_content": "Related stories",
    "related_index": "4",
    "related_article_tag": "products - search",
    "article_name": "5 ways to upgrade your home decor with Google Search",
    "author_name": "Megan Stoner",
    "content_type": "blogv2 | article page"
  }'
  data-theme-color="aquamarine"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["8-leaf-clover", "ghost-ish", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Home_Decor.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Home_Decor.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Home_Decor.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        5 ways to upgrade your home decor with Google Search
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Megan Stoner
          
        </span>
      
    </div>
  </div>
</a>

        
          




<a
  href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/what-full-stack-development-means/"
  class="uni-article-card"
  aria-label="Gemini models - What does “full\u002Dstack” AI actually mean? - By Lindsey Lanquist - Aug 21, 2026"
  data-index="5"
  data-target="card"
  data-primaryTag="topics - gemini models"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "What does “full\u002Dstack” AI actually mean?",
    "link_url":  "https://blog.google/innovation-and-ai/models-and-research/gemini-models/what-full-stack-development-means/",
    "source_content": "Related stories",
    "related_index": "5",
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
  href="https://blog.google/products-and-platforms/products/search/back-to-school-study-tools/"
  class="uni-article-card"
  aria-label="Search - 5 new ways to level up your learning with Search - By Awaneesh Verma - Aug 19, 2026"
  data-index="6"
  data-target="card"
  data-primaryTag="products - search"
  data-image="true"
  data-ga4-analytics-footer-lead-click='{
    "link_text": "5 new ways to level up your learning with Search",
    "link_url":  "https://blog.google/products-and-platforms/products/search/back-to-school-study-tools/",
    "source_content": "Related stories",
    "related_index": "6",
    "related_article_tag": "products - search",
    "article_name": "5 new ways to level up your learning with Search",
    "author_name": "Awaneesh Verma",
    "content_type": "blogv2 | article page"
  }'
  data-theme-color="aquamarine"
>
  <div class="uni-article-card__shape-container">
    <div
      class="uni-article-card__shape"
      data-shape-context-consumer='["8-leaf-clover", "ghost-ish", "square"]'>
      
        
  


<img
  src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Blog_header_2_JwwDb02.2e16d0ba.fill-300x300.format-webp.webp"
  alt=""

  
    class="uni-article-card__img"
  

  
    sizes="auto"
    srcset="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Blog_header_2_JwwDb02.2e16d0ba.fill-300x300.format-webp.webp 300w, https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Blog_header_2_JwwDb02.2e16d0ba.fill-600x600.format-webp.webp 600w"
  

  
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
        5 new ways to level up your learning with Search
      </h3>
      
    </div>

    <div
      class="uni-article-card__meta"
      data-target="author">
      
        <span class="uni-article-card__author font-author-name">
          By
          
            
            Awaneesh Verma
          
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
    "section_header": "Gemini 3.5: frontier intelligence with action"
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
        value="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/"
        lang="en-us"
        class="uni-lang-picker__option"
        
          selected="selected"
          data-selected-index="0"
        >
        Global (English)
      </option>
      
      <option
        label="Africa (English)"
        value="https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/"
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
        value="https://blog.google/intl/pt-br/gemini-3-5/"
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
        value="https://blog.google/intl/fr-ca/produits/explorez-obtenez-des-reponses/gemini-3-5/"
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
        value="https://blog.google/intl/fr-fr/nouveautes-produits/io-gemini-3-5/"
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
        value="https://blog.google/intl/ja-jp/company-news/technology/gemini-3-5/"
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
        value="https://blog.google/intl/es-419/actualizaciones-de-producto/gemini-3-5/"
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
        value="https://blog.google/intl/pl-pl/nowosci-produktowe/sztuczna-inteligencja/gemini-3-5/"
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
        value="https://blog.google/intl/zh-tw/products/explore-get-answers/gemini-3-5/"
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
