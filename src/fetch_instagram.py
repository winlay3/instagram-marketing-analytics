import os, requests, pandas as pd
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("IG_TOKEN")
BASE = "https://graph.instagram.com/v21.0"

def get_media():
    url = f"{BASE}/me/media"
    params = {
        "fields": "id,caption,media_type,timestamp,like_count,comments_count,permalink",
        "limit": 50,
        "access_token": TOKEN,
    }
    rows = []
    while url:
        r = requests.get(url, params=params).json()
        rows += r.get("data", [])
        url = r.get("paging", {}).get("next")
        params = None  # the next URL already includes the params
    return rows

def get_insights(media_id):
    r = requests.get(
        f"{BASE}/{media_id}/insights",
        params={"metric": "reach,saved,shares", "access_token": TOKEN},
    ).json()
    return {m["name"]: m["values"][0]["value"] for m in r.get("data", [])}

rows = get_media()
for row in rows:
    row.update(get_insights(row["id"]))

df = pd.DataFrame(rows)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["engagement"] = df["like_count"] + df["comments_count"]
df.to_csv("instagram_posts.csv", index=False)
print(df.head())