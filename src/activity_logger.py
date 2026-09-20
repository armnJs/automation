#!/usr/bin/env python3
# ==============================================================================
#  Copyright (c) 2023-present armnJs (Armaan Sheikh). All Rights Reserved.
#  Author: armnJs (https://github.com/armnJs/automation)
#  License: MIT with Educational Attribution & Legal Liability Shield.
# ==============================================================================
"""
Activity Logger Script
----------------------
Appends structured activity telemetry to data/activity_log.json.
Can be executed standalone, locally, or as part of a GitHub Actions workflow.
"""

import argparse
import datetime
import json
import os
import random
import subprocess
import sys
from pathlib import Path

# Paths relative to repository root
REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "config" / "default_config.json"
DATA_LOG_PATH = REPO_ROOT / "data" / "activity_log.json"


def load_config(config_path: Path) -> dict:
    """Loads JSON configuration file."""
    if not config_path.exists():
        return {
            "log_file_path": "data/activity_log.json",
            "commit_messages": ["chore: automated activity update"],
            "default_user_name": "github-actions[bot]",
            "default_user_email": "github-actions[bot]@users.noreply.github.com",
        }
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


# Mumbai Timezone (IST, UTC+5:30)
MUMBAI_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))


def append_activity_log(log_file: Path, message: str, run_type: str = "daily_automation") -> dict:
    """Appends a new structured entry to the activity log file in Mumbai Timezone (IST)."""
    log_file.parent.mkdir(parents=True, exist_ok=True)

    entries = []
    if log_file.exists():
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                entries = json.load(f)
        except json.JSONDecodeError:
            entries = []

    timestamp = datetime.datetime.now(MUMBAI_TZ).isoformat()
    entry = {
        "timestamp": timestamp,
        "status": "active",
        "message": message,
        "run_type": run_type,
        "entry_id": len(entries) + 1,
    }

    entries.append(entry)

    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)

    print(f"[+] Appended activity entry #{entry['entry_id']} at {timestamp}")
    return entry


def run_git_commit(commit_message: str, user_name: str, user_email: str, dry_run: bool = False):
    """Configures git identity, stages log file, and creates a commit."""
    if dry_run:
        print(f"[Dry-Run] Would commit with message: '{commit_message}'")
        return

    try:
        subprocess.run(["git", "config", "user.name", user_name], check=True, cwd=REPO_ROOT)
        subprocess.run(["git", "config", "user.email", user_email], check=True, cwd=REPO_ROOT)
        subprocess.run(["git", "add", str(DATA_LOG_PATH)], check=True, cwd=REPO_ROOT)

        result = subprocess.run(
            ["git", "commit", "-m", commit_message],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )

        if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
            print("[=] Nothing new to commit.")
        else:
            print(f"[+] Git commit created: {commit_message}")

    except subprocess.CalledProcessError as e:
        print(f"[-] Error executing git command: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="GitHub Activity Logger")
    parser.add_argument("--message", type=str, help="Custom commit message")
    parser.add_argument("--config", type=str, help="Path to config file")
    parser.add_argument("--dry-run", action="store_true", help="Log without creating git commits")
    parser.add_argument("--no-commit", action="store_true", help="Only update log file, skip git commit")
    args = parser.parse_args()

    cfg_path = Path(args.config) if args.config else CONFIG_PATH
    config = load_config(cfg_path)

    message = args.message
    if not message:
        messages = config.get("commit_messages", ["chore: automated activity update"])
        message = random.choice(messages)

    user_name = os.getenv("GIT_USER_NAME", config.get("default_user_name", "github-actions[bot]"))
    user_email = os.getenv("GIT_USER_EMAIL", config.get("default_user_email", "github-actions[bot]@users.noreply.github.com"))

    append_activity_log(DATA_LOG_PATH, message)

    if not args.no_commit:
        run_git_commit(message, user_name, user_email, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
