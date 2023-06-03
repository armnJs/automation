from datetime import datetime, timedelta
import os
import random
import subprocess

REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_PATH)

# Range from May 9, 2023 to Nov 24, 2023 (or extend as needed)
start_date = datetime(2023, 5, 9)
end_date = datetime(2023, 11, 24)

current_date = start_date
total_days = (end_date - start_date).days + 1
total_commits = 0

print(f"[*] Re-backfilling range {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')} with explicit ISO 8601 timezone (+05:30)...")

while current_date <= end_date:
    commit_hour = random.randint(9, 21)
    commit_min = random.randint(0, 59)
    commit_sec = random.randint(0, 59)
    
    date_with_time = current_date.replace(hour=commit_hour, minute=commit_min, second=commit_sec)
    # ISO 8601 format with timezone offset +05:30
    iso_date_str = date_with_time.strftime("%Y-%m-%dT%H:%M:%S+05:30")

    num_commits = random.randint(2, 5)

    for _ in range(num_commits):
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

    current_date += timedelta(days=1)

print(f"[+] Finished generating {total_commits} ISO 8601 commits across {total_days} days for May 9 2023 to Nov 24 2023!")
