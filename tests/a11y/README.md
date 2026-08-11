# Accessibility smoke test

Runs [axe-core](https://github.com/dequelabs/axe-core) via Playwright against
every major Chronos page (public and authenticated) and fails on
serious/critical violations. It's a separate CI job (`accessibility` in
`.github/workflows/tests.yml`) because it needs Node + a real browser + the
Flask app actually running, unlike the Python test suite.

## Run locally

```sh
cd tests/a11y
npm install
npx playwright install chromium   # first time only

# in another terminal, from the repo root:
SECRET_KEY=dev DATABASE_URL=sqlite:////tmp/chronos_a11y.db python run.py

npm test
```

Moderate/minor findings are printed but don't fail the run — the goal is to
catch real barriers (missing labels, bad contrast, broken heading order),
not to gate every stylistic nitpick.
