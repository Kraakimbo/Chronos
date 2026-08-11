// Accessibility smoke test: runs axe-core against every major page (public
// and authenticated) and fails the build on serious/critical violations.
// Moderate/minor findings are printed but don't fail CI, to keep this gate
// useful instead of blocking on every nitpick.
import { chromium } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

const BASE = process.env.A11Y_BASE_URL || "http://127.0.0.1:5000";
const FAIL_ON = new Set(["serious", "critical"]);

const PUBLIC_PAGES = ["/auth/connexion", "/auth/inscription", "/decouvrir", "/decouvrir/prise-de-la-bastille"];
const AUTH_PAGES = ["/", "/explorer", "/evenement/prise-de-la-bastille", "/quiz", "/profil"];

async function auditPage(page, path) {
  await page.goto(`${BASE}${path}`, { waitUntil: "networkidle" });
  const results = await new AxeBuilder({ page }).analyze();
  return { path, violations: results.violations };
}

async function main() {
  const browser = await chromium.launch({ executablePath: process.env.PLAYWRIGHT_CHROMIUM_PATH || undefined });
  const context = await browser.newContext();
  const page = await context.newPage();

  const allResults = [];

  for (const path of PUBLIC_PAGES) {
    allResults.push(await auditPage(page, path));
  }

  // Register a throwaway user so the authenticated pages have real content.
  const username = `a11y_${Date.now()}`;
  await page.goto(`${BASE}/auth/inscription`, { waitUntil: "networkidle" });
  await page.fill("input[name=username]", username);
  await page.fill("input[name=email]", `${username}@example.com`);
  await page.fill("input[name=password]", "A11yTest1234!");
  await page.fill("input[name=confirm_password]", "A11yTest1234!");
  await page.check("input[name=study_level][value=lycee]");
  await page.click("input[type=submit]");
  await page.waitForLoadState("networkidle");

  for (const path of AUTH_PAGES) {
    allResults.push(await auditPage(page, path));
  }

  await browser.close();

  let hasBlockingViolations = false;
  for (const { path, violations } of allResults) {
    if (violations.length === 0) continue;
    for (const v of violations) {
      const blocking = FAIL_ON.has(v.impact);
      if (blocking) hasBlockingViolations = true;
      console.log(
        `${blocking ? "[FAIL]" : "[warn]"} ${path} — ${v.id} (${v.impact}): ${v.help} — ${v.nodes.length} element(s)`
      );
    }
  }

  if (hasBlockingViolations) {
    console.error("\nAccessibility check failed: serious/critical violations found above.");
    process.exit(1);
  }
  console.log("\nAccessibility check passed (no serious/critical violations).");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
