# Instagram Marketing Analytics Dashboard

A small data project that pulls post performance data from the Instagram API and visualizes it in Power BI, answering: which content works best for marketing?

## What it does
- Extracts posts and insights (likes, comments, reach, saves, shares) using the Instagram Graph API
- Cleans the data with Python (pandas) and saves it as a CSV
- Visualizes engagement by post type, posting day and time trends in Power BI

## Tech stack
Python, pandas, Instagram Graph API, Power BI

## Dashboard
![Dashboard](screenshots/dashboard.png)

## How to run
1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your Instagram access token
3. Run `python fetch_instagram.py` to generate `instagram_posts.csv`
4. Open `instagram_dashboard.pbix` in Power BI Desktop and refresh the data
