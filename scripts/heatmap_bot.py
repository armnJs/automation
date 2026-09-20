from datetime import datetime, timedelta
import os
import random
import subprocess

# Number of days back to populate
DAYS_BACK = 30
REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.chdir(REPO_PATH)

for i in range(DAYS_BACK):
  # Calculate date going back 'i' days
  date = datetime.now() - timedelta(days=i)
  date_str = date.strftime("%Y-%m-%d %H:%M:%S")

  # Randomize number of commits per day (0 to 4)
  num_commits = random.randint(0, 4)

  for _ in range(num_commits):
    # Modify a dummy file to create a change
    with open("contribution_log.txt", "a") as f:
      f.write(f"Commit on {date_str}\n")

    # Stage the file
    subprocess.run(["git", "add", "contribution_log.txt"])

    # Commit with backdated environment variables
    env = {
        **os.environ,
        "GIT_AUTHOR_DATE": date_str,
        "GIT_COMMITTER_DATE": date_str,
    }
    subprocess.run(
        ["git", "commit", "-m", f"Auto commit for {date_str}"], env=env
    )

print("Finished generating commits! Run 'git push origin main' to sync.")
