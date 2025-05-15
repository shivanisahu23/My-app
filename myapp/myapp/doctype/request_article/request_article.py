# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

@frappe.whitelist()
def get_article_details(article_request):
    return frappe.get_all(
        "Article Details",
        filters={"parent": article_request},
        fields=["article_name", "rate", "quantity"]
    )

class RequestArticle(Document):
    pass
    # def validate(self):
    #     self.calculate_total_amount()

    # def calculate_total_amount(self):
    #     total = 0
    #     for item in self.article_details:
    #         if item.rate and item.quantity:
    #             total += (item.rate * item.quantity)
    #     self.total_amount = total


