import os, random, xmlrpc.client
from dotenv import load_dotenv

load_dotenv()
url, db = os.getenv("ODOO_URL"), os.getenv("ODOO_DB")
user, pwd = os.getenv("ODOO_USER"), os.getenv("ODOO_PASSWORD")

uid = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common").authenticate(db, user, pwd, {})
m = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

def get_or_create(model, name):
    ids = m.execute_kw(db, uid, pwd, model, "search", [[["name", "=", name]]])
    return ids[0] if ids else m.execute_kw(db, uid, pwd, model, "create", [{"name": name}])

source = get_or_create("utm.source", "Instagram")
campaigns = [get_or_create("utm.campaign", n)
             for n in ["ig_oct_promo", "ig_new_product", "ig_giveaway"]]

for i in range(12):
    m.execute_kw(db, uid, pwd, "crm.lead", "create", [{
        "name": f"Instagram lead {i+1}",
        "type": "opportunity",
        "expected_revenue": random.randint(500, 5000),
        "source_id": source,
        "campaign_id": random.choice(campaigns),
    }])
print("Done")