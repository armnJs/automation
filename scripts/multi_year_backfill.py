# ==============================================================================
#  Copyright (c) 2023-present armnJs (Armaan Sheikh). All Rights Reserved.
#  Author: armnJs (https://github.com/armnJs/automation)
#  License: MIT with Educational Attribution & Legal Liability Shield.
# ==============================================================================

from datetime import datetime, timedelta
import os
import random
import subprocess

REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_PATH)

# Range for 2024-01-01 to 2025-09-20
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 9, 20)

current_date = start_date
total_days = (end_date - start_date).days + 1
total_commits = 0

print(f"[*] Starting backfill for years 2024 and 2025 ({start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}, {total_days} days)...")

while current_date <= end_date:
    # Randomize time during the day (09:00 to 21:00)
    commit_hour = random.randint(9, 21)
    commit_min = random.randint(0, 59)
    commit_sec = random.randint(0, 59)
    
    date_with_time = current_date.replace(hour=commit_hour, minute=commit_min, second=commit_sec)
    date_str = date_with_time.strftime("%Y-%m-%d %H:%M:%S")

    # Randomize number of commits per day (1 to 5)
    num_commits = random.randint(1, 5)

    for _ in range(num_commits):
        with open("contribution_log.txt", "a") as f:
            f.write(f"Commit on {date_str}\n")

        subprocess.run(["git", "add", "contribution_log.txt"])

        env = {
            **os.environ,
            "GIT_AUTHOR_DATE": date_str,
            "GIT_COMMITTER_DATE": date_str,
        }
        subprocess.run(
            ["git", "commit", "-m", f"Auto commit for {date_str}"], env=env
        )
        total_commits += 1

    current_date += timedelta(days=1)

print(f"[+] Finished generating {total_commits} commits across {total_days} days for 2024-2025! Syncing to GitHub...")
