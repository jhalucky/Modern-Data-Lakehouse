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

CATEGORY_SCHEMA = {
    "product_category_name": "string",
    "product_category_name_english": "string"
}

GEOLOCATION_SCHEMA = {
    "geolocation_zip_code_prefix": "int",
    "geolocation_lat": "double",
    "geolocation_lng": "double",
    "geolocation_city": "string",
    "geolocation_state": "string"
}

ORDER_ITEM_SCHEMA = {
    "order_id": "string",
    "order_item_id": "int",
    "product_id": "string",
    "seller_id": "string",
    "shipping_limit_date": "timestamp",
    "price": "double",
    "freight_value": "double"
}

ORDER_PAYMENT_SCHEMA = {
    "order_id": "string",
    "payment_sequential": "int",
    "payment_type": "string",
    "payment_installments": "int",
    "payment_value": "double"
}

PRODUCT_SCHEMA = {
    "product_id": "string",
    "product_category_name": "string",
    "product_name_lenght": "int",
    "product_description_lenght": "int",
    "product_photos_qty": "int",
    "product_weight_g": "int",
    "product_length_cm": "int",
    "product_height_cm": "int",
    "product_width_cm": "int"
}

SELLER_SCHEMA = {
    "seller_id": "string",
    "seller_zip_code_prefix": "int",
    "seller_city": "string",
    "seller_state": "string"
}

REVIEW_SCHEMA = {
    "review_id": "string",
    "order_id": "string",
    "review_score": "int",
    "review_comment_title": "string",
    "review_comment_message": "string",
    "review_creation_date": "timestamp",
    "review_answer_timestamp": "timestamp"
}