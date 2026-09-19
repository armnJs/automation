#!/usr/bin/env python3
"""
Backfill Engine Script
---------------------
Generates historical git commits over a specified date range to populate
the contribution graph retroactively.
"""

import argparse
import datetime
import os
import random
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_LOG_PATH = REPO_ROOT / "data" / "activity_log.json"


# Mumbai Timezone (IST, UTC+5:30)
MUMBAI_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))


def generate_backfill(
    days: int,
    min_commits: int,
    max_commits: int,
    user_name: str,
    user_email: str,
    include_weekends: bool = True,
    dry_run: bool = False,
):
    """Generates commits backward from today for `days` count in Mumbai Timezone (IST)."""
    today = datetime.datetime.now(MUMBAI_TZ)
    total_commits_created = 0

    print(f"[*] Starting backfill generation for the past {days} days (Mumbai Time IST, UTC+5:30)...")
    print(f"[*] Commit range per day: {min_commits} to {max_commits}")
    print(f"[*] Identity: {user_name} <{user_email}>")

    if not dry_run:
        subprocess.run(["git", "config", "user.name", user_name], check=True, cwd=REPO_ROOT)
        subprocess.run(["git", "config", "user.email", user_email], check=True, cwd=REPO_ROOT)

    for day_offset in range(days, -1, -1):
        target_date = today - datetime.timedelta(days=day_offset)

        # Check weekend filter
        if not include_weekends and target_date.weekday() in (5, 6):
            continue

        num_commits = random.randint(min_commits, max_commits)

        for i in range(num_commits):
            # Randomize hour/minute for natural commit history
            commit_time = target_date.replace(
                hour=random.randint(9, 21),
                minute=random.randint(0, 59),
                second=random.randint(0, 59),
                tzinfo=MUMBAI_TZ,
            )

            formatted_date = commit_time.strftime("%Y-%m-%dT%H:%M:%S+05:30")

            commit_msg = f"chore(backfill): historical activity log for {commit_time.strftime('%Y-%m-%d')}"

            if dry_run:
                print(f"  [Dry-Run] {formatted_date} -> {commit_msg}")
                total_commits_created += 1
                continue

            # Update log file or empty commit
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = formatted_date
            env["GIT_COMMITTER_DATE"] = formatted_date

            try:
                # Stage changes or allow empty commit
                subprocess.run(
                    ["git", "commit", "--allow-empty", "-m", commit_msg, "--date", formatted_date],
                    check=True,
                    cwd=REPO_ROOT,
                    env=env,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                total_commits_created += 1
            except subprocess.CalledProcessError as e:
                print(f"[-] Failed to create commit for {formatted_date}: {e}", file=sys.stderr)

    print(f"[+] Successfully completed! Total commits generated: {total_commits_created}")


def main():
    parser = argparse.ArgumentParser(description="Historical Contribution Backfill Engine")
    parser.add_argument("--days", type=int, default=30, help="Number of past days to backfill (default: 30)")
    parser.add_argument("--min-commits", type=int, default=1, help="Minimum commits per active day (default: 1)")
    parser.add_argument("--max-commits", type=int, default=3, help="Maximum commits per active day (default: 3)")
    parser.add_argument("--name", type=str, default="github-actions[bot]", help="Git user name")
    parser.add_argument("--email", type=str, required=True, help="Git user email associated with GitHub account")
    parser.add_argument("--exclude-weekends", action="store_true", help="Skip creating commits on Saturdays/Sundays")
    parser.add_argument("--dry-run", action="store_true", help="Preview backfill dates without making git commits")
    args = parser.parse_args()

    generate_backfill(
        days=args.days,
        min_commits=args.min_commits,
        max_commits=args.max_commits,
        user_name=args.name,
        user_email=args.email,
        include_weekends=not args.exclude_weekends,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
