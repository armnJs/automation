# Complete Setup & Configuration Guide 🚀

Follow this step-by-step guide to configure the repository for automated daily activity logging and contribution graph backfilling.

---

## Step 1: Push Repository to GitHub

Ensure your project is published to GitHub:

```bash
git init
git add .
git commit -m "feat: initial commit with modular activity engine"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

---

## Step 2: Enable GitHub Actions Write Permissions ⚙️

1. Navigate to your repository on GitHub.
2. Click **Settings** ➔ **Actions** ➔ **General**.
3. Scroll down to **Workflow permissions**.
4. Select **Read and write permissions**.
5. Click **Save**.

---

## Step 3: Configure GitHub Email Attribution 📧

GitHub requires commits to match an email address registered on your GitHub account for green dots to show on your profile graph.

### Option A: Using GitHub Secrets (Recommended for Privacy)
1. Go to repository **Settings** ➔ **Secrets and variables** ➔ **Actions**.
2. Click **New repository secret**.
3. Name: `USER_EMAIL`
4. Value: `your-email@example.com` (Your GitHub account email address)

### Option B: Using GitHub `noreply` Email
You can also use your GitHub-provided anonymous email (found under GitHub **Settings** ➔ **Emails**):
`username@users.noreply.github.com`

---

## Step 4: Show Private Contributions (If Repository is Private) 🔒

If this repository is **Private**, GitHub hides contributions by default:
1. Go to your GitHub profile (`https://github.com/YOUR_USERNAME`).
2. Click **Edit profile**.
3. Check **"Include private contributions on my profile"**.
4. Click **Save**.

---

## Step 5: Test & Trigger Workflows Manually 🧪

1. Go to the **Actions** tab in your repository.
2. Select **Daily Activity Automation** from the left sidebar.
3. Click **Run workflow** ➔ **Run workflow**.
4. Verify that the workflow completes successfully and updates `data/activity_log.json`!
