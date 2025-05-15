// Copyright (c) 2025, Shivani Sahu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Request Article", {
    refresh: function(frm) {
        frm.add_custom_button('Article Request', function() {
            var dialog = new frappe.ui.Dialog({
                title: 'Select Article Request',
                fields: [
                    {
                        label: 'Article Request',
                        fieldname: 'article_request',
                        fieldtype: 'Link',
                        options: 'Article Request',
                        reqd: true,
                        onchange: function() {
                            var req_name = dialog.get_value('article_request');
                            if (req_name) {
                                frappe.call({
                                    method: 'myapp.myapp.doctype.request_article.request_article.get_article_details',
                                    args: {
                                        article_request: req_name
                                    },
                                    callback: function(response) {
                                        var data = response.message;
                                        dialog.fields_dict.articles.df.data = data;
                                        dialog.fields_dict.articles.grid.refresh();
                                    }
                                });
                            } else {
                                frappe.msgprint("No Article found in the Article Request.");
                            }
                        }
                    },
                    {
                        label: 'Articles',
                        fieldname: 'articles',
                        fieldtype: 'Table',
                        fields: [
                            {
                                fieldname: 'article_name',
                                label: 'Article Name',
                                fieldtype: 'Link',
                                options: 'Article',
                                in_list_view: 1,
                                get_query: function () {
                                    return {
                                        filters: {
                                            status: 'Active'
                                        }
                                    };
                                }
                            },
                            {
                                fieldname: 'rate',
                                label: 'Rate',
                                fieldtype: 'Currency',
                                in_list_view: 1
                            },
                            {
                                fieldname: 'quantity',
                                label: 'Quantity',
                                fieldtype: 'Float',
                                in_list_view: 1
                            }
                        ]
                        
                    }
                ],
                primary_action_label: 'Get Articles',
                primary_action: function(values) {
                    dialog.hide();
                    // console.log("=======", values.articles);

                    let articles = values.articles;
                    let k = articles.length;

                    // console.log(frm.doc.article_details);

                    for (let i = 0; i < k; i++) {
                        let article = articles[i];
                        let row = frm.add_child('article_details', {
                            article_name: article.article_name,
                            rate: article.rate,
                            quantity: article.quantity
                        });
                    }
                    
                    frm.refresh_field('article_details');
                }

                
                
            });

            dialog.show();
        }, __('Get Request From'));
        frm.set_query('article_name', 'article_details', () => {
            return {
                filters: { 
                    status: 'Active' 
                }
            }
        }),
        calculate_total(frm)
    }
});


frappe.ui.form.on('Article Details', {
    rate: function(frm, cdt, cdn) {
        calculate_total(frm);
    },
    quantity: function(frm, cdt, cdn) {
        calculate_total(frm);
    }
});

function calculate_total(frm) {
    let total = 0;
    for (let i = 0; i < frm.doc.article_details.length; i++) {
        let row = frm.doc.article_details[i];
        if (row.rate && row.quantity) {
            total += row.rate * row.quantity;
        }
    }
    frm.set_value('total_amount', total);
    frm.refresh_field('total_amount')
}


