import requests, pandas as pd

SITE = "http://ig-analytics-demo.local"

posts = requests.get(f"{SITE}/wp-json/wp/v2/posts", params={"per_page": 50}).json()

df = pd.DataFrame([{
    "id": p["id"],
    "date": p["date"],
    "title": p["title"]["rendered"],
    "link": p["link"],
} for p in posts])

df.to_csv("data/wordpress_posts.csv", index=False)
print(df)