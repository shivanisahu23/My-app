// // Copyright (c) 2025, Shivani Sahu and contributors
// // For license information, please see license.txt

frappe.ui.form.on("Bulk Overtime", {
    refresh(frm) {
        frm.disable_save();

        frm.add_custom_button('Create Overtime request', function () {
            if (!frm.doc.overtime_details || frm.doc.overtime_details.length === 0) {
                frappe.msgprint("No workers in the Overtime Details table.");
                return;
            }

            if (!frm.doc.date || !frm.doc.reason || !frm.doc.status) {
                frappe.msgprint("Please ensure all fields (Date, Reason, Status) are filled out.");
                return;
            }

            frappe.call({
                method: "myapp.myapp.doctype.bulk_overtime.bulk_overtime.create_overtime_requests",
                args: {
                    date: frm.doc.date,
                    reason: frm.doc.reason,
                    details: frm.doc.overtime_details,
                    status: frm.doc.status
                }
            });
        });
    },

    get_workers: function(frm) {
        frappe.call({
            method: "myapp.myapp.doctype.bulk_overtime.bulk_overtime.get_workers",
            callback: function(res) {
                let workers = res.message;
                if (!workers) return;
    
                frm.clear_table("overtime_details");
    
                for (let i = 0; i < workers.length; i++) {
                    let row = frm.add_child("overtime_details");
                    row.worker = workers[i].name;
                    row.full_name = workers[i].full_name;
                }
                // console.log(message)
                frm.refresh_field("overtime_details");
            }
        });
    }
    
});

