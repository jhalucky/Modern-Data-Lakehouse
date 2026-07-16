USE DATABASE MODERN_LAKEHOUSE;
USE SCHEMA GOLD;
-- Top 10 customers
SELECT
    customer_id,
    lifetime_value
FROM CLV_ANALYTICS
ORDER BY lifetime_value DESC
LIMIT 10;

-- Revenue by state
SELECT
    customer_state,
    SUM(total_spent) AS revenue
FROM CUSTOMER_ANALYTICS
GROUP BY customer_state
ORDER BY revenue DESC;


-- Top producst

SELECT 
 product_category_name,
 SUM(total_revenue) AS revenue
FROM PRODUCT_ANALYTICS
GROUP BY product_category_name
ORDER BY revenue DESC;


SELECT
    order_date,
    total_revenue
FROM SALES_ANALYTICS
ORDER BY order_date;

SELECT
    customer_segment,
    COUNT(*) AS customers
FROM CLV_ANALYTICS
GROUP BY customer_segment;

SELECT * FROM SALES_ANALYTICS LIMIT 10;

SELECT * FROM CUSTOMER_ANALYTICS LIMIT 10;

SELECT * FROM PRODUCT_ANALYTICS LIMIT 10;

SELECT * FROM SELLER_ANALYTICS LIMIT 10;

SELECT * FROM CLV_ANALYTICS LIMIT 10;