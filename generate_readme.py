"""
Reads categorized data from btc_stack_data.py, triggers scan/report pages
to force grading, and generates README.md with embedded RepoGrade badges.
"""

import urllib.request
import urllib.error
from jinja2 import Template
from btc_stack_data import STACK_DATA

README_TEMPLATE = """# 🔐 Bitcoin Self-Custody & Infrastructure Health

Automated tracking index monitoring major open-source Bitcoin wallets, hardware firmware, and protocol dependencies alongside real-time **RepoGrade** quality badges.

---

{% for cat in categories %}
## 🛠 {{ cat.category }}

| Project / Repository | Primary Dependencies & Grades | Repo Grade | GitHub Stars |
| :--- | :--- | :---: | :---: |
{% for item in cat.projects %}| **[{{ item.name }}](https://github.com/{{ item.repo }})**<br><sub>{{ item.description }}</sub> | {% if item.dependencies %}{% for dep in item.dependencies %}**[{{ dep.name }}](https://github.com/{{ dep.repo }})** [![Grade](https://repo-grade.com/api/badge/{{ dep.repo }})](https://repo-grade.com/report/{{ dep.repo }})<br><sub>{{ dep.role }}</sub>{% if not loop.last %}<br><br>{% endif %}{% endfor %}{% else %}<sub>None listed</sub>{% endif %} | [![Grade](https://repo-grade.com/api/badge/{{ item.repo }})](https://repo-grade.com/report/{{ item.repo }}) | ![Stars](https://img.shields.io/github/stars/{{ item.repo }}?style=social) |
{% endfor %}

---
{% endfor %}

<sub>*Dashboard updated automatically via Python scripts using Jinja2 templates.*</sub>
"""

def ping_repo_grade(repo_path: str):
    """Pings the RepoGrade report URL to queue/trigger an initial evaluation scan."""
    report_url = f"https://repo-grade.com/report/{repo_path}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        req = urllib.request.Request(report_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"[Triggered Scan] {repo_path} (HTTP {resp.status})")
    except urllib.error.HTTPError as e:
        print(f"[HTTP Error {e.code}] Could not trigger scan for {repo_path}")
    except Exception as e:
        print(f"[Warning] Failed to ping {repo_path}: {e}")

def prefetch_all_grades(categories):
    """Iterates through all main projects and dependencies to trigger grade scans."""
    print("Initiating pre-fetch scan triggers for unindexed repos...")
    seen = set()
    
    for cat in categories:
        for project in cat.get("projects", []):
            repo = project.get("repo")
            if repo and repo not in seen:
                ping_repo_grade(repo)
                seen.add(repo)
                
            for dep in project.get("dependencies", []):
                dep_repo = dep.get("repo")
                if dep_repo and dep_repo not in seen:
                    ping_repo_grade(dep_repo)
                    seen.add(dep_repo)

def main():
    # 1. Ping report pages to force RepoGrade to run an analysis pass
    prefetch_all_grades(STACK_DATA)
    
    # 2. Render Jinja template into README.md
    template = Template(README_TEMPLATE)
    rendered_markdown = template.render(categories=STACK_DATA)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(rendered_markdown)
    
    print("Successfully rendered README.md!")

if __name__ == "__main__":
    main()
