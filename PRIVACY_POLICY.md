# Privacy Policy & Legal Compliance

**Last Updated:** September 19, 2026

This document outlines the privacy policy, legal compliance, copyright status, and usage terms for the **GitHub Contribution & Activity Automation** project repository.

---

## 1. Overview & Data Privacy

- **Zero Data Collection**: This project does **not** collect, track, store, transmit, or harvest any personal data, user analytics, tracking cookies, IP addresses, or telemetry to external servers.
- **Local & Isolated Execution**: All scripts (`src/activity_logger.py`, `src/backfill_engine.py`) execute locally on your machine or within isolated GitHub Actions virtual runners (`ubuntu-latest`).
- **Data Retention**: The only data modified by this repository is the activity telemetry log stored strictly inside [`data/activity_log.json`](data/activity_log.json) within your own GitHub repository.

---

## 2. Intellectual Property & Copyright

- **Original Codebase**: All source code, workflows, scripts, and documentation contained in this repository are 100% original work.
- **Licensing**: This project is released under the open-source **MIT License** (see [`LICENSE`](LICENSE)). You are free to use, modify, distribute, and integrate this software without copyright restrictions.
- **Third-Party Rights**: This repository does not violate or infringe upon any third-party copyrights, patents, trademarks, or trade secrets.

---

## 3. Legal Status & Safety

- **Legal Compliance**: Running automated commit workflows in your own personal repository is fully legal.
- **No Unauthorized Access**: The scripts inside this repository interact exclusively with the host repository in which they reside. They do not attempt unauthorized network access, scraping, or automated actions on third-party systems.

---

## 4. GitHub Terms of Service & Fair Resource Usage

- **Built-in GitHub Features**: The automated workflows utilize official GitHub Actions infrastructure provided by GitHub.
- **Compute Resource Limits**: The daily workflow uses approximately 10 seconds of runner execution time per day (~5 minutes per month), staying far below GitHub's monthly free tier allowance of 2,000 build minutes.
- **Acceptable Use**: This project complies with GitHub’s Acceptable Use Policies. It does not perform spamming, crypto-mining, automated interaction on third-party repositories, or service disruption.

---

## 5. Contact & Questions

If you have any questions regarding this Privacy Policy or codebase compliance, please refer to the project documentation in [`README.md`](README.md) or open an Issue in the official repository.
