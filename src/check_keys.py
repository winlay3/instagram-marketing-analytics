import pandas as pd

ig = pd.read_csv("data/instagram_posts.csv")
wp = pd.read_csv("data/wordpress_posts.csv")
od = pd.read_csv("data/odoo_leads.csv")

print("INSTAGRAM captions:")
print(ig[["id", "caption"]].to_string(), "\n")
print("WORDPRESS slugs:")
print(wp[["id", "title"] + (["slug"] if "slug" in wp else [])].to_string(), "\n")
print("ODOO campaigns:")
print(od["campaign_id"].value_counts(dropna=False))