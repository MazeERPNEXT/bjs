app_name = "bjs"
app_title = "BJs Raw Pet Food"
app_publisher = "Avunu LLC"
app_description = "Frappe scripts for BJs Raw Pet Food"
app_email = "mail@avu.nu"
app_license = "mit"
required_apps = [
    "erpnext",
    "shipstation_integration"
]
doc_events = {
    "Sales Order": {
        "submit": "bjs.bjs_raw_pet_food.hooks.sales_order.generate_shipments"
    }
}