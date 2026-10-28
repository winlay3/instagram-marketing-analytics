import os, xmlrpc.client, pandas as pd
from dotenv import load_dotenv

load_dotenv()
url, db = os.getenv("ODOO_URL"), os.getenv("ODOO_DB")
user, pwd = os.getenv("ODOO_USER"), os.getenv("ODOO_PASSWORD")

uid = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common").authenticate(db, user, pwd, {})
if not uid:
    raise SystemExit("Login failed: check ODOO_DB, ODOO_USER, ODOO_PASSWORD")

models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
leads = models.execute_kw(db, uid, pwd, "crm.lead", "search_read", [[]],
    {"fields": ["name", "create_date", "source_id", "campaign_id", "expected_revenue"]})

df = pd.DataFrame(leads)
df.to_csv("data/odoo_leads.csv", index=False)
print(df.head())