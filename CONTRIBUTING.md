# Contributing Guidelines 🤝

Thank you for considering contributing to the **GitHub Contribution Automation** project!

---

## 🛠️ Local Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd "YOUR_REPO_NAME"
   ```

2. Test the activity logger script locally:
   ```bash
   python src/activity_logger.py --dry-run
   ```

3. Test the historical backfill engine locally:
   ```bash
   python src/backfill_engine.py --days 5 --email user@example.com --dry-run
   ```

---

## 📐 Code Style & Guidelines

- **Python Version**: Write Python 3.9+ compatible standard library code.
- **Zero Third-Party Dependencies**: Keep core scripts zero-dependency (`json`, `subprocess`, `pathlib`, `argparse`, `datetime`) so workflows run fast out of the box in GitHub Actions without `pip install`.
- **Modular Code**: Place core generator logic inside `src/` and keep configurations inside `config/`.

---

## 🧪 Testing Before Pull Requests

Before submitting a PR, make sure both dry-run executions complete cleanly without error:

```bash
python src/activity_logger.py --dry-run
python src/backfill_engine.py --days 3 --email test@example.com --dry-run
```
