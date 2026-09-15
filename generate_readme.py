"""
Reads categorized data from btc_stack_data.py, launches headless Playwright browser
to trigger RepoGrade JavaScript evaluators, and generates a polished README.md.
"""

import asyncio
from playwright.async_api import async_playwright
from jinja2 import Template
from btc_stack_data import STACK_DATA

README_TEMPLATE = """# 🔐 Bitcoin Self-Custody & Infrastructure Health

Automated tracking index monitoring open-source Bitcoin wallets, hardware firmware, and protocol dependencies alongside real-time **RepoGrade** quality badges.

---

{% for cat in categories %}
## 🛠 {{ cat.category }}

| Project / Target | Primary Dependencies | Repo Grade | GitHub Stars |
| :--- | :--- | :---: | :---: |
{% for item in cat.projects %}| **[{{ item.name }}](https://github.com/{{ item.repo }})**<br><sub>{{ item.description }}</sub> | {% if item.dependencies %}{% for dep in item.dependencies %}• **[{{ dep.name }}](https://github.com/{{ dep.repo }})** [![Grade](https://repo-grade.com/api/badge/{{ dep.repo }})](https://repo-grade.com/report/{{ dep.repo }})<br>&nbsp;&nbsp;&nbsp;&nbsp;<sub><i>{{ dep.role }}</i></sub>{% if not loop.last %}<br>{% endif %}{% endfor %}{% else %}<sub>None listed</sub>{% endif %} | [![Grade](https://repo-grade.com/api/badge/{{ item.repo }})](https://repo-grade.com/report/{{ item.repo }}) | ![Stars](https://img.shields.io/github/stars/{{ item.repo }}?style=social) |
{% endfor %}

---
{% endfor %}

<sub>*Dashboard updated automatically via Python scripts and Playwright.*</sub>
"""

async def trigger_repograde_scan(page, repo_path: str):
    url = f"https://repo-grade.com/report/{repo_path}"
    print(f"[Browser] Navigating to: {url}")
    try:
        await page.goto(url, wait_until="networkidle", timeout=20000)
        await page.wait_for_timeout(3000)
    except Exception as e:
        print(f"[Warning] Timeout loading {repo_path}: {e}")

async def prefetch_all_with_browser(categories):
    seen = set()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()

        for cat in categories:
            for project in cat.get("projects", []):
                repo = project.get("repo")
                if repo and repo not in seen:
                    await trigger_repograde_scan(page, repo)
                    seen.add(repo)

                for dep in project.get("dependencies", []):
                    dep_repo = dep.get("repo")
                    if dep_repo and dep_repo not in seen:
                        await trigger_repograde_scan(page, dep_repo)
                        seen.add(dep_repo)

        await browser.close()

def main():
    asyncio.run(prefetch_all_with_browser(STACK_DATA))

    template = Template(README_TEMPLATE)
    rendered_markdown = template.render(categories=STACK_DATA)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(rendered_markdown)

    print("Successfully rendered README.md!")

if __name__ == "__main__":
    main()
