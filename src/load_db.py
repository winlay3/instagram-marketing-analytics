import sqlite3
import pandas as pd

ig = pd.read_csv("data/instagram_posts.csv")
wp = pd.read_csv("data/wordpress_posts.csv")
odoo = pd.read_csv("data/odoo_leads.csv")

# Odoo: make sure a clean campaign column exists
if "campaign" not in odoo.columns:
    odoo["campaign"] = odoo["campaign_id"].apply(
        lambda v: eval(v)[1] if isinstance(v, str) and v.startswith("[") else None
    )

# Simulated campaign links for demo purposes
campaigns = ["ig_oct_promo", "ig_new_product", "ig_giveaway"]
ig["campaign"] = [campaigns[i % 3] for i in range(len(ig))]
wp["campaign"] = [campaigns[i % 3] for i in range(len(wp))]

con = sqlite3.connect("data/marketing.db")
ig.to_sql("instagram_posts", con, if_exists="replace", index=False)
wp.to_sql("wordpress_posts", con, if_exists="replace", index=False)
odoo.to_sql("odoo_leads", con, if_exists="replace", index=False)
con.close()

print("Loaded into data/marketing.db")