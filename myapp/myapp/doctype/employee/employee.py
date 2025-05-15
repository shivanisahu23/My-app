# # # # Copyright (c) 2025, Shivani Sahu and contributors
# # # # For license information, please see license.txt

# # # import frappe
# # # from frappe.model.document import Document

# # # class Employee(Document):
# # #     def validate(self):
# # #         # Concatenate first name, middle name (if exists), and last name to form full name
# # #         name_parts = [self.first_name, self.middle_name, self.last_name]
# # #         self.full_name = " ".join(filter(None, name_parts))  # Removes None or empty values

# # #         # Calculate total in-hand salary
# # #         if self.salary and self.pf_provident_fund is not None:  # Ensure PF is considered even if it's zero
# # #             self.total_in_hand_salary = self.salary - self.pf_provident_fund
# # #         else:
# # #             self.total_in_hand_salary = self.salary  # If PF is not provided, full salary remains




# # import frappe
# # from frappe.model.document import Document
# # from frappe.utils import getdate, today, cint

# # class Employee(Document):
# #     def validate(self):
# #         """Runs before saving the Employee record to check data validity."""
        
# #         # Generate Full Name
# #         self.full_name = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))

# #         self.set_salary_based_on_role()

# #         # Calculate Total In-Hand Salary
# #         self.total_in_hand_salary = cint(self.salary) - cint(self.pf_provident_fund)

# #         # Validate Date of Birth (Minimum Age: 18)
# #         if self.dob_date_of_birth:
# #             self.age = self.get_age(self.dob_date_of_birth)
# #             if self.age < 18:
# #                 frappe.throw("Employee must be at least 18 years old.")

# #         # Validate Date of Joining (No future dates allowed)
# #         if self.date_of_joining and getdate(self.date_of_joining) > getdate(today()):
# #             frappe.throw("Date of Joining cannot be in the future.")

# #     def set_salary_based_on_role(self):
# #         role_salary_mapping = {
# #             "Intern": 5000,
# #             "Developer": 30000,
# #             "Functional Consultant": 25000,
# #             "HR": 50000
# #         }

# #         if self.role in role_salary_mapping:
# #             self.salary = role_salary_mapping[self.role]

# #     def get_age(self, dob):
# #         """Calculate age based on Date of Birth using Frappe utilities."""
# #         dob = getdate(dob)
# #         today_date = getdate(today())

# #         age = today_date.year - dob.year
# #         if (today_date.month, today_date.day) < (dob.month, dob.day):
# #             age -= 1  # Adjust age if birthday hasn't occurred yet this year

# #         return age
    
# #     self.experience = self.calculate_experience()
    
# #     def calculate_experience(self):
# #         if self.date_of_joining:
# #             joining_date = getdate(self.date_of_joining)
# #             current_date = getdate(today())

# #             years = current_date.year - joining_date.year

# #             if (current_date.month, current_date.day) < (joining_date.month, joining_date.day):
# #                 years -= 1

# #             return years
        
# #         return 0
    
    

# #     def on_submit(self):
# #         frappe.msgprint("Employee record has been successfully submitted.")

# #     def on_cancel(self):
# #         frappe.msgprint("Employee record has been canceled.")

# #     def on_update_after_submit(self):
# #         frappe.msgprint("Employee record has been updated.")

import frappe
from frappe.model.document import Document
from frappe.utils import month_diff, getdate, today, cint

class Employee(Document):
    def validate(self):
       
        # self.full_name = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))

        self.set_salary_based_on_role()

        self.total_in_hand_salary = cint(self.salary) - cint(self.pf_provident_fund)

        if self.dob_date_of_birth:
            self.age = self.get_age(self.dob_date_of_birth)
            if self.age < 18:
                frappe.throw("Employee must be at least 18 years old.")

        self.experience = self.calculate_experience()

        if self.date_of_joining and getdate(self.date_of_joining) > getdate(today()):
            frappe.throw("Date of Joining cannot be in the future.")
        
        self.full_name = self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def calculate_experience(self):
        """Calculate experience in 'years.months' format (e.g., 1.3 for 1 year, 3 months)."""
        if self.date_of_joining:
            joining_date = getdate(self.date_of_joining)
            current_date = getdate(today())

            total_months = month_diff(current_date, joining_date)
            years = total_months // 12
            months = total_months % 12

            # Ensure single decimal place without extra digits
            experience_value = float(f"{years}.{months}")

            return experience_value  # Returns in X.Y format
        
        return 0.0

    def set_salary_based_on_role(self):

        role_salary_mapping = {
            "Intern": 5000,
            "Developer": 30000,
            "Functional Consultant": 25000,
            "HR": 50000
        }

        if self.role in role_salary_mapping:
            self.salary = role_salary_mapping[self.role]

    def get_age(self, dob):

        dob = getdate(dob)
        today_date = getdate(today())

        age = today_date.year - dob.year
        if (today_date.month, today_date.day) < (dob.month, dob.day):
            age -= 1 

        return age
    
    def before_submit(self):
        frappe.msgprint("Employee record is to be Submit! Are yo sure about")

    def on_submit(self):
        frappe.msgprint("Employee record has been successfully submitted.")

    def on_cancel(self):
        frappe.msgprint("Employee record has been canceled.")

    def on_update_after_submit(self):
        frappe.msgprint("Employee record has been updated.")




# my_dict = {"name": "Alice", "age":25}
# print(my_dict.get("name"))

# print(my_dict.keys())

# print(my_dict.get("salary"))
# my_dict.get("salary", 1000)
# print(my_dict.get("salary"))

# del my_dict["age"]

# my_list = ["Hello", 23, {"a":1}, 456, "Shivani", True]
# print(my_list)

# int_list = [item for item in my_list if type(item) == int]
# print(int_list)

# pep8

# class grandparent:
#     def show(self):
#         print("Grandparent")
#     def show3(self):
#         print("Grand1")

# class parent(grandparent):
#     def show1(self):
#         print("Parent")
#     def show3(self):
#         print("Grand2")

# class child(parent):
#     def show2(self):
#         print("Child")
#     # def show3(self):
#     #     print("Grand3")


# c = child()
# c.show()
# c.show1()
# c.show2()
# c.show3()

#MRO in details



# class animal:
#     def sound(self):
#         print("Some Sound")

# class Dog(animal):
#     def sound(self):
#         print("Barkk")

# d = Dog()
# d.sound()

