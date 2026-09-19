# 🟩 GitHub Contribution & Activity Automation

[![Daily Activity Automation](https://github.com/your-username/your-repo/actions/workflows/daily-activity.yml/badge.svg)](https://github.com/your-username/your-repo/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)

A clean, production-ready, zero-dependency automated activity generator and contribution graph backfill engine built with Python and GitHub Actions.

---

## 📌 Project Overview

This repository provides an automated system to maintain your GitHub contribution graph ("green dots"). It supports:
1. **Automated Daily Activity**: Scheduled GitHub Actions workflow (`daily-activity.yml`) running at `09:00 AM IST` (`03:30 UTC`, Mumbai Timezone) every day.
2. **Historical Backfilling**: Interactive workflow (`backfill-history.yml`) or CLI command (`src/backfill_engine.py`) to generate commits retroactively for past days/years.
3. **Structured Telemetry Logging**: Appends readable JSON telemetry logs to `data/activity_log.json`.

---

## 📂 Repository File Structure

```
.
├── .github/
│   └── workflows/
│       ├── daily-activity.yml       # Production automated daily update workflow
│       ├── backfill-history.yml     # Interactive past contribution backfill workflow
│       ├── auto-activity.yml        # Direct shell update alternative workflow
│       └── marketplace-activity.yml # Marketplace action integration alternative
├── config/
│   └── default_config.json          # System configuration & random message templates
├── data/
│   └── activity_log.json            # Telemetry activity log storage
├── docs/
│   ├── ARCHITECTURE.md              # Technical design & Mermaid system diagram
│   └── SETUP_GUIDE.md               # End-to-end setup & permissions guide
├── scripts/
│   ├── run_local.bat                # Quickstart runner for Windows
│   └── run_local.sh                 # Quickstart runner for Linux/macOS
├── src/
│   ├── __init__.py                  # Package marker
│   ├── activity_logger.py           # Core daily telemetry generator
│   └── backfill_engine.py           # Historical backfill engine
├── .gitignore                       # Standard git ignore rules
├── CONTRIBUTING.md                  # Guidelines for maintainers and contributors
├── LICENSE                          # MIT License
├── README.md                        # Primary documentation
└── requirements.txt                 # Dependencies marker (Zero 3rd party deps)
```

---

## ⚡ Quickstart

### 1. Local Preview & Dry-Run

You can preview the activity generator locally without creating git commits:

```bash
# Preview daily activity logger
python src/activity_logger.py --dry-run

# Preview 30-day historical backfill
python src/backfill_engine.py --days 30 --email your-email@example.com --dry-run
```

### 2. Local Execution Scripts
- **Windows**: Double-click or run `scripts\run_local.bat`
- **Linux/macOS**: Execute `./scripts/run_local.sh`

---

## ⚙️ GitHub Actions Setup Guide

To ensure GitHub Actions can commit and update your contribution graph:

1. **Repository Settings**:
   - Go to **Settings** ➔ **Actions** ➔ **General**.
   - Under **Workflow permissions**, choose **Read and write permissions** ➔ Click **Save**.

2. **Attribution Email**:
   - Add your GitHub account email address as a secret named `USER_EMAIL` under **Settings** ➔ **Secrets and variables** ➔ **Actions**.

3. **Private Contributions Graph**:
   - If this repo is private, enable **"Include private contributions on my profile"** in your GitHub profile settings.

For detailed setup instructions, read the [`docs/SETUP_GUIDE.md`](file:///d:/Armaan/git%20commit%20autoomation%20%28green%20dots%29/docs/SETUP_GUIDE.md).

---

## 📖 Architecture & Design

For technical specifications, state diagrams, and module breakdowns, see [`docs/ARCHITECTURE.md`](file:///d:/Armaan/git%20commit%20autoomation%20%28green%20dots%29/docs/ARCHITECTURE.md).

---

## 🤝 Contributing

Contributions and enhancements are welcome! Please read [`CONTRIBUTING.md`](file:///d:/Armaan/git%20commit%20autoomation%20%28green%20dots%29/CONTRIBUTING.md) for developer setup and testing rules.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
