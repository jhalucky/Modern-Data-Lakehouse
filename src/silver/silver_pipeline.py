from pyspark.sql.functions import col

from src.spark.spark_session import get_spark_session
from src.bronze.bronze_pipeline import load_bronze_tables

from src.transformations.transform import transform
from src.transformations.write_delta import write_Delta

from src.config.aws_config import SILVER_PATH

from schemas import (
    CUSTOMER_SCHEMA,
    ORDER_SCHEMA,
    GEOLOCATION_SCHEMA,
    PRODUCT_SCHEMA,
    CATEGORY_SCHEMA,
    ORDER_ITEM_SCHEMA,
    ORDER_PAYMENT_SCHEMA,
    SELLER_SCHEMA,
    REVIEW_SCHEMA
)

spark = get_spark_session()

tables = load_bronze_tables(spark)

customers = tables["customers"]
categories = tables["categories"]
orders = tables["orders"]
geolocation = tables["geolocation"]
products = tables["products"]
order_items = tables["order_items"]
payments = tables["payments"]
reviews = tables["reviews"]


reviews.printSchema()

reviews.show(
    5,
    truncate=False
)

reviews = transform(
    reviews,
    REVIEW_SCHEMA,
    {
        "review_comment_title": "",
        "review_comment_message": ""
    }
)
sellers = tables["sellers"]


# ==========================
# Customers
# ==========================

print("\n========== CUSTOMERS ==========")

customers = transform(
    customers,
    CUSTOMER_SCHEMA,
    {
        "customer_city": "Unknown",
        "customer_state": "Unknown"
    }
)

write_Delta(
    customers,
    SILVER_PATH + "customers"
)


# ==========================
# Categories
# ==========================

print("\n========== CATEGORIES ==========")

categories = transform(
    categories,
    CATEGORY_SCHEMA,
    {
        "product_category_name_english": "Unknown"
    }
)

write_Delta(
    categories,
    SILVER_PATH + "categories"
)


# ==========================
# Orders
# ==========================

print("\n========== ORDERS ==========")

orders = transform(
    orders,
    ORDER_SCHEMA,
    {
        "order_status": "Unknown"
    }
)

orders = orders.filter(
    col("order_status") != "cancelled"
)

write_Delta(
    orders,
    SILVER_PATH + "orders"
)


# ==========================
# Geolocation
# ==========================

print("\n========== GEOLOCATION ==========")

geolocation = transform(
    geolocation,
    GEOLOCATION_SCHEMA,
    {
        "geolocation_city": "Unknown",
        "geolocation_state": "Unknown"
    }
)

write_Delta(
    geolocation,
    SILVER_PATH + "geolocation"
)


# ==========================
# Products
# ==========================

print("\n========== PRODUCTS ==========")

products = transform(
    products,
    PRODUCT_SCHEMA,
    {
        "product_category_name": "Unknown"
    }
)

write_Delta(
    products,
    SILVER_PATH + "products"
)


# ==========================
# Order Items
# ==========================

print("\n========== ORDER ITEMS ==========")

order_items = transform(
    order_items,
    ORDER_ITEM_SCHEMA,
    {}
)

write_Delta(
    order_items,
    SILVER_PATH + "order_items"
)


# ==========================
# Payments
# ==========================

print("\n========== PAYMENTS ==========")

payments = transform(
    payments,
    ORDER_PAYMENT_SCHEMA,
    {}
)

write_Delta(
    payments,
    SILVER_PATH + "payments"
)


# ==========================
# Reviews
# ==========================

print("\n========== REVIEWS ==========")

reviews = transform(
    reviews,
    REVIEW_SCHEMA,
    {
        "review_comment_title": "",
        "review_comment_message": ""
    }
)

reviews.printSchema()

reviews.select(
    "review_score",
    "review_creation_date",
    "review_answer_timestamp"
).show(20, truncate=False)

write_Delta(
    reviews,
    SILVER_PATH + "reviews"
)


# ==========================
# Sellers
# ==========================

print("\n========== SELLERS ==========")

sellers = transform(
    sellers,
    SELLER_SCHEMA,
    {
        "seller_city": "Unknown",
        "seller_state": "Unknown"
    }
)

write_Delta(
    sellers,
    SILVER_PATH + "sellers"
)


print("\nSilver Layer Pipeline Completed Successfully!")