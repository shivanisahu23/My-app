// Copyright (c) 2025, Shivani Sahu and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article Request', {
    refresh: function(frm) {
        if(!frm.is_new()){
            frm.add_custom_button('Request Article', () => {
                frappe.model.open_mapped_doc({
                    method: 'myapp.myapp.doctype.article_request.article_request.make_request_articles',
                    frm: frm
                });
            }, __('Create'));
        }
        
    }
});