# QA Intelligence — Deployment Guide

AI-powered QA & testing co-pilot. Built with Python (FastAPI) + Anthropic Claude API.

---

## 📁 Project Structure

```
qa-intelligence/
├── main.py              ← FastAPI backend (handles API calls)
├── requirements.txt     ← Python dependencies
├── Procfile             ← Tells Railway how to start the app
├── .gitignore           ← Keeps secrets out of Git
├── README.md            ← This file
└── static/
    └── index.html       ← Your frontend (the full website)
```

---

## 🔑 STEP 1 — Get Your Anthropic API Key

1. Go to https://console.anthropic.com
2. Sign up or log in
3. Click **"API Keys"** in the left sidebar
4. Click **"Create Key"** → give it a name like "qa-intelligence"
5. **Copy the key** — it starts with `sk-ant-...`
6. Save it somewhere safe — you only see it once!

---

## 💻 STEP 2 — Push to GitHub

You need a GitHub account. If you don't have one: https://github.com/signup

### 2a. Install Git (if not already installed)
- Mac: open Terminal, type `git --version` (it will prompt install if missing)
- Windows: download from https://git-scm.com/download/win

### 2b. Create a new GitHub repository
1. Go to https://github.com/new
2. Repository name: `qa-intelligence`
3. Set to **Public**
4. Click **"Create repository"**

### 2c. Upload your files from Terminal / Command Prompt

Open Terminal (Mac) or Command Prompt (Windows), then run these commands one by one:

```bash
# Go into your project folder (adjust path to where you saved it)
cd /path/to/qa-intelligence

# Initialize git
git init

# Add all files
git add .

# Save with a message
git commit -m "Initial deploy"

# Connect to your GitHub repo (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/qa-intelligence.git

# Push to GitHub
git branch -M main
git push -u origin main
```

✅ Refresh your GitHub page — you should see all your files there.

---

## 🚀 STEP 3 — Deploy on Railway

Railway is free and takes about 2 minutes.

### 3a. Sign up for Railway
1. Go to https://railway.app
2. Click **"Login"** → **"Login with GitHub"**
3. Authorize Railway to access your GitHub

### 3b. Create a new project
1. Click **"New Project"** (big button on dashboard)
2. Click **"Deploy from GitHub repo"**
3. Find and click **"qa-intelligence"** in the list
4. Railway will start deploying automatically

### 3c. Add your API key (IMPORTANT)
Your app will crash without this step.

1. Click on your project in Railway
2. Click the service box (the one named "qa-intelligence")
3. Click the **"Variables"** tab
4. Click **"New Variable"**
5. Set:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Value:** `sk-ant-your-key-here` (paste your key from Step 1)
6. Click **"Add"**
7. Railway will automatically redeploy

### 3d. Get your live URL
1. Click the **"Settings"** tab
2. Under "Domains" click **"Generate Domain"**
3. You'll get a URL like: `qa-intelligence.up.railway.app`

✅ Open that URL in your browser — your site is live!

---

## ✅ Test It Works

1. Open your Railway URL
2. Click **"Get Started"** or **"Try Demo"**
3. Go to the **Onboarding** page
4. Type a message and press Enter
5. You should get a real AI response within a few seconds

---

## 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| Site loads but AI doesn't respond | Check that `ANTHROPIC_API_KEY` variable is set in Railway |
| Railway shows "Build failed" | Make sure all 4 files are pushed to GitHub (main.py, requirements.txt, Procfile, static/index.html) |
| Page shows blank/error | Click "Logs" tab in Railway to see what went wrong |
| "Module not found" error | Check requirements.txt has all 4 packages listed |

---

## 💰 Cost

- **Railway:** Free tier gives you $5/month credit — more than enough for a portfolio project
- **Anthropic API:** Pay per use. Claude Sonnet costs ~$0.003 per message. Very cheap for demos.

---

## 🔄 Update Your Site Later

After making changes to your files:

```bash
git add .
git commit -m "Update site"
git push
```

Railway will automatically redeploy within 1-2 minutes.

---

Developed by Iswarya Malayamaan · github.com/IshuDhana
