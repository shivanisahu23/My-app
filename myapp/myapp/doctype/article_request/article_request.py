# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_request_articles(source_name):
	return get_mapped_doc(
		"Article Request",
		source_name,
		{
			"Article Request": {
				"doctype": "Request Article"
			},
			"Articles Details": {
				"doctype": "Articles Details",
				"field_map": {
					"article_name": "article_name",
					"rate": "rate",
					"qyt": "qyt"
				},
				"add_if_empty": True
			}
		}
	)

class ArticleRequest(Document):
	pass






# import frappe
# from frappe.model.document import Document
# from frappe.model.mapper import get_mapped_doc

# @frappe.whitelist()
# def make_request_articles(source_name, target_doc=None):
# 	def set_missing_values(source, target):
# 		target.date = source.date
	
# 	doc = get_mapped_doc(
# 		"Article Request",
# 		source_name,
# 		{
# 			"Article Request": {
# 				"doctype": "Request Article",
# 				"field_map": {
# 					"date": "date"
# 				}
# 			},
# 			"Articles Details": {
# 				"doctype": "Articles Details",
# 				"field_map": {
# 					"article_name": "article_name",
# 					"rate": "rate",
# 					"qyt": "qyt"
# 				},
# 				"add_if_empty": True
# 			}
# 		},
# 		target_doc,
# 		set_missing_values
# 	)
# 	return doc
