# import frappe

# @frappe.whitelist()
# def rename_accounts():
#     accounts = frappe.get_all("Account",
#                               filters={'disabled': 1, 'name': 'E24 THIRUVASTHRADHIKAL - RIMS'},
#                               fields=['name', 'company', 'account_name'])
#     sorted_accounts = sorted(accounts, key=lambda x: x['name'])
#     companies = frappe.get_all("Company", fields=['name', 'abbr'])
#     sorted_companies = sorted(companies, key=lambda x: x['name'])
#     for account in sorted_accounts:
#         company_abbr = next((c['abbr'] for c in sorted_companies if c['name'] == account['company']), "")
#         frappe.msgprint(f"Processing account: {account['name']}")
#         if company_abbr:
#             new_account_name = f"{account['account_name']} - {company_abbr}"
#             frappe.msgprint(f"New account name: {new_account_name}")
#             frappe.db.set_value("Account", account['name'], "account_name", new_account_name)
    
#     frappe.db.commit()
#     frappe.msgprint("Done")
