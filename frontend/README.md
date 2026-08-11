# Frontend build

Chronos' CSS and fonts used to be pulled at runtime from `cdn.tailwindcss.com`
and `fonts.googleapis.com`. That's fine for a prototype, but it means the
entire site loses its styling if that CDN is slow, blocked (some corporate
and school networks do this), or briefly down -- and it re-compiles the full
Tailwind build in every visitor's browser on every page load.

This directory builds the exact same design tokens (see `tailwind.config.js`,
the single source of truth both `base.html` and `base_app.html` now share)
into a static CSS file, and self-hosts the two Google Fonts plus the Material
Symbols icon font, so the app has zero third-party runtime dependency for its
look.

The build output is committed to `app/static/css/chronos.css` and
`app/static/fonts/`, so nothing needs to run at deploy time on Render --
regenerate it locally whenever `tailwind.config.js`, `input.css`, or a
template's class names change:

```sh
cd frontend
npm install
npm run build
```

`npm run build` runs the Tailwind CLI against every template under
`app/templates/` and writes the minified CSS to `../app/static/css/chronos.css`.
