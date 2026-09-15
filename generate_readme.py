"""
Reads categorized data from btc_stack_data.py and generates README.md
with embedded RepoGrade quality badges.
"""

from jinja2 import Template
from btc_stack_data import STACK_DATA

README_TEMPLATE = """# 🔐 Bitcoin Self-Custody & Infrastructure Health

Automated tracking index monitoring major open-source Bitcoin wallets, hardware firmware, and protocol dependencies alongside real-time **RepoGrade** quality badges.

---

{% for cat in categories %}
## 🛠 {{ cat.category }}

| Project / Repository | Primary Dependencies | Repo Grade | GitHub Stars |
| :--- | :--- | :---: | :---: |
{% for item in cat.projects %}| **[{{ item.name }}](https://github.com/{{ item.repo }})**<br><sub>{{ item.description }}</sub> | {% if item.dependencies %}{% for dep in item.dependencies %}**[{{ dep.name }}](https://github.com/{{ dep.repo }})**<br><sub>{{ dep.role }}</sub>{% if not loop.last %}<br><br>{% endif %}{% endfor %}{% else %}<sub>None listed</sub>{% endif %} | [![Grade](https://repo-grade.com/api/badge/{{ item.repo }})](https://repo-grade.com/report/{{ item.repo }}) | ![Stars](https://img.shields.io/github/stars/{{ item.repo }}?style=social) |
{% endfor %}

---
{% endfor %}

<sub>*Dashboard updated automatically via Python scripts using Jinja2 templates.*</sub>
"""

def main():
    template = Template(README_TEMPLATE)
    rendered_markdown = template.render(categories=STACK_DATA)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(rendered_markdown)
    
    print("Successfully rendered README.md with clean GitHub Markdown table syntax!")

if __name__ == "__main__":
    main()
