CUSTOMER_SCHEMA = {
    "customer_id" : "string","customer_unique_id": "string","customer_zip_code_prefix": "int","customer_city": "string","customer_state":"string"
}

ORDER_SCHEMA = {
    "order_id": "string",
    "customer_id": "string",
    "order_status": "string",
    "order_purchase_timestamp": "timestamp",
    "order_approved_at": "timestamp",
    "order_delivered_carrier_date": "timestamp",
    "order_delivered_customer_date": "timestamp",
    "order_estimated_delivery_date": "timestamp"
}