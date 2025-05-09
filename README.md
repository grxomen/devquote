# 🧠 devquote

A lightweight, developer-themed quote package — with optional AI support via OpenAI.

---

## ✨ Features

* Get random quotes from categories like `motivation`, `debug`, and `tips`
* Use from Python or as a CLI tool (`devquote`)
* Optional GPT-powered quotes via `--ai`
* Easy to install, easy to extend

---

## 🚀 Installation

**From GitHub (editable):**

```bash
pip install git+https://github.com/yourusername/devquote.git
```
Or locally:
```bash
pip install -e .
```

🔧 Usage

📌 In Python
```python
from devquote import get_quote
print(get_quote("motivation"))
```

📌 From CLI
```bash
devquote motivation
devquote debug
devquote --ai
```

> Set your OpenAI key via `.env`:
>
> ```env
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
> ```
---
📂 Project Structure
```text
devquote/
├── devquote/
│   ├── __init__.py
│   ├── cli.py
│   ├── core.py
│   └── ai.py
├── tests/
├── pyproject.toml
├── .env.example
└── README.md
```

🧪 Coming Soon

* Discord bot integration

* Custom quote submissions

* Leaderboards and user stats


---

> ✅ Now you can paste this directly into your `README.md`, save, and then commit + push:

```powershell
git add README.md
git commit -m "Update README with clean formatting"
git push
```

