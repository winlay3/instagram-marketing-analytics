import sqlite3
import pandas as pd

QUERIES = {
    "Leads and revenue per campaign": """
        SELECT campaign, COUNT(*) AS leads, SUM(expected_revenue) AS revenue
        FROM odoo_leads
        WHERE campaign IS NOT NULL
        GROUP BY campaign
        ORDER BY revenue DESC
    """,
    "Instagram engagement per campaign": """
        SELECT campaign, COUNT(*) AS posts, SUM(engagement) AS total_engagement,
               ROUND(AVG(engagement), 1) AS avg_engagement
        FROM instagram_posts
        GROUP BY campaign
    """,
    "Full funnel": """
        WITH ig AS (
            SELECT campaign, COUNT(*) AS ig_posts, SUM(engagement) AS engagement
            FROM instagram_posts GROUP BY campaign),
        wp AS (
            SELECT campaign, COUNT(*) AS web_posts
            FROM wordpress_posts GROUP BY campaign),
        od AS (
            SELECT campaign, COUNT(*) AS leads, SUM(expected_revenue) AS revenue
            FROM odoo_leads WHERE campaign IS NOT NULL GROUP BY campaign)
        SELECT ig.campaign, ig.ig_posts, ig.engagement,
               wp.web_posts, od.leads, od.revenue
        FROM ig
        LEFT JOIN wp ON ig.campaign = wp.campaign
        LEFT JOIN od ON ig.campaign = od.campaign
        ORDER BY od.revenue DESC
    """,
}

con = sqlite3.connect("data/marketing.db")
for name, sql in QUERIES.items():
    df = pd.read_sql(sql, con)
    print(f"\n== {name} ==")
    print(df.to_string(index=False))
    if name == "Full funnel":
        df.to_csv("data/funnel.csv", index=False)
con.close()