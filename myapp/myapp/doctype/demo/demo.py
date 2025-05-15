# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class demo(Document):
	def validate(self):
		self.total = int(self.price1) + int(self.price2)
