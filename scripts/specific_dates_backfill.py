# ==============================================================================
#  Copyright (c) 2023-present armnJs (Armaan Sheikh). All Rights Reserved.
#  Author: armnJs (https://github.com/armnJs/automation)
#  License: MIT with Educational Attribution & Legal Liability Shield.
# ==============================================================================

from datetime import datetime
import os
import random
import subprocess

REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_PATH)

# Exact target dates requested by user
target_dates = [
    datetime(2025, 9, 21),
    datetime(2026, 8, 30),
    datetime(2026, 9, 4),
    datetime(2026, 9, 5),
    datetime(2026, 9, 8),
    datetime(2026, 9, 9),
    datetime(2026, 9, 13),
]

total_commits = 0

print(f"[*] Starting targeted backfill for {len(target_dates)} specific dates...")

for dt in target_dates:
    # Generate 3 to 5 commits per date
    num_commits = random.randint(3, 5)

    for _ in range(num_commits):
        commit_hour = random.randint(9, 21)
        commit_min = random.randint(0, 59)
        commit_sec = random.randint(0, 59)
        
        date_with_time = dt.replace(hour=commit_hour, minute=commit_min, second=commit_sec)
        iso_date_str = date_with_time.strftime("%Y-%m-%dT%H:%M:%S+05:30")

        with open("contribution_log.txt", "a") as f:
            f.write(f"Commit on {iso_date_str}\n")

        subprocess.run(["git", "add", "contribution_log.txt"])

        env = {
            **os.environ,
            "GIT_AUTHOR_DATE": iso_date_str,
            "GIT_COMMITTER_DATE": iso_date_str,
        }
        subprocess.run(
            ["git", "commit", "--date", iso_date_str, "-m", f"Auto commit for {iso_date_str}"],
            env=env
        )
        total_commits += 1

print(f"[+] Successfully generated {total_commits} commits across {len(target_dates)} target dates!")
