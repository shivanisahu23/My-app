// Copyright (c) 2025, Shivani Sahu and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Employee", {
// 	refresh(frm) {
//         frappe.msgprint('Welcome to Employee Form! ');
// 	},

//     validate: function(frm) {
//         if (frm.doc.salary < 0) {
//             frappe.throw('Salary cannot be negative. ')
//         }
//     },

//     first_name: function(frm) {
//         if (frm.doc.first_name && frm.doc.last_name) {
//             frm.set_value('full_name', frm.doc.first_name + " " + frm.doc.last);
//         }
//     }
// });


frappe.ui.form.on("Employee", {
    refresh(frm) {
        frappe.msgprint("Welcome to Employee Form!");
    },

    validate(frm) {
        if (frm.doc.salary < 0) {
            frappe.throw("Salary cannot be negative.");
        }
    },

    first_name(frm) {
        if (frm.doc.first_name && frm.doc.last_name) {
            frm.set_value('full_name', frm.doc.first_name + " " + frm.doc.last_name);
        }
    },

    last_name(frm) {
        if (frm.doc.first_name && frm.doc.last_name) {
            frm.set_value('full_name', frm.doc.first_name + " " + frm.doc.last_name);
        }
    }
});
