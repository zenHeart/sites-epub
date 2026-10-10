<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <link rel="shortcut icon" href="https://statics.kimi.ai/kimi-design-web/favicon-kimi.ico" />
    <link rel="icon" type="image/x-icon" href="https://statics.kimi.ai/kimi-design-web/favicon-light.ico" media="(prefers-color-scheme: light)" />
    <link rel="icon" type="image/x-icon" href="https://statics.kimi.ai/kimi-design-web/favicon-dark.ico" media="(prefers-color-scheme: dark)" />
    <meta name="renderer" content="webkit" />
    <link rel="preconnect" href="https://statics.kimi.ai" crossorigin />
    <link rel="dns-prefetch" href="https://statics.kimi.ai" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
    <title>Kimi Design</title>
    <script>
      (function() {
        var theme = 'light'
        var isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches

        var stored = null
        try { stored = localStorage.getItem('CUSTOM_THEME') } catch (e) {}
        if (stored) {
          try {
            var parsed = JSON.parse(stored)
            if (parsed === 'dark') theme = 'dark'
            else if (parsed === 'light') theme = 'light'
            else if (parsed === 'system') theme = isDark ? 'dark' : 'light'
          } catch (e) {}
        } else if (window.INJECT_ENV && window.INJECT_ENV.theme) {
          theme = window.INJECT_ENV.theme === 'dark' ? 'dark' : 'light'
        } else {
          theme = isDark ? 'dark' : 'light'
        }
        document.documentElement.classList.add(theme)
      })()
    </script>
    <script type="module" crossorigin src="https://statics.kimi.ai/kimi-design-web/assets/index-BTsbrcJZ.js"></script>
    <link rel="modulepreload" crossorigin href="https://statics.kimi.ai/kimi-design-web/assets/vue-Dr_Kvv8m.js">
    <link rel="modulepreload" crossorigin href="https://statics.kimi.ai/kimi-design-web/assets/rolldown-runtime-Dd_uD5pT.js">
    <link rel="modulepreload" crossorigin href="https://statics.kimi.ai/kimi-design-web/assets/core-DSAJGeJG.js">
    <link rel="modulepreload" crossorigin href="https://statics.kimi.ai/kimi-design-web/assets/preload-helper-CnP0D9Kr.js">
    <link rel="modulepreload" crossorigin href="https://statics.kimi.ai/kimi-design-web/assets/useChatInputModel-CWHCwxW3.js">
    <link rel="stylesheet" crossorigin href="https://statics.kimi.ai/kimi-design-web/assets/preload-helper-zqSMMjV9.css">
    <link rel="stylesheet" crossorigin href="https://statics.kimi.ai/kimi-design-web/assets/useChatInputModel-DeGInmkw.css">
    <link rel="stylesheet" crossorigin href="https://statics.kimi.ai/kimi-design-web/assets/index-DU3ApxL3.css">
  </head>
  <body>
    <div id="app"></div>
    <!-- Kimi Design Copyright © Kimi. All rights reserved. Built at 2026-10-10T07:23:37.690Z, 9c67ef -->
  </body>

</html>
