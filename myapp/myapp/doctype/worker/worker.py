# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, today

class Worker(Document):
    def validate(self):
        self.full_name = self.get_full_name()
        self.age = self.get_age(self.date_of_birth)
        self.get_salutation()

        if self.email:
            existing_user = frappe.db.exists("User", {"email": self.email})

            if not existing_user:
                new_user = frappe.new_doc("User")
                new_user.email = self.email
                new_user.first_name = self.first_name
                new_user.last_name = self.last_name
                new_user.enabled = 1
                new_user.save(ignore_permissions = True)

                frappe.msgprint(f"A new user has been created with email {self.email} .")

    def get_age(self, dob):
        dob = getdate(dob)
        today_date = getdate(today())
        age = today_date.year - dob.year
        if (today_date.month, today_date.day) < (dob.month, dob.day):
            age -= 1
        return age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_salutation(self):
        if self.gender == "Female":
            self.salutation = "Miss"
        else:
            self.salutation = "Mr"

    