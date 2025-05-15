# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BulkOvertime(Document):
	pass

@frappe.whitelist()
def get_workers():
    workers = frappe.get_all("Worker", fields=["name", "full_name"])
    return workers

@frappe.whitelist()
def create_overtime_requests(details, date, reason, status):
    import json
    details = json.loads(details)

    for row in details:
        ot_request = frappe.new_doc("Overtime Request")
        ot_request.date = date
        ot_request.reason = reason
        ot_request.status = status
        ot_request.hours = row.get("ot_hours") or 0
        ot_request.worker = row.get("worker")
        ot_request.full_name = row.get("full_name")
        ot_request.insert(ignore_permissions=True)

    return frappe.msgprint("Requests are formed.")

