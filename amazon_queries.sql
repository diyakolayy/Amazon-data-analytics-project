SELECT category, COUNT(product_id) AS product_count
FROM amazon_products
GROUP BY category
ORDER BY product_count DESC;

SELECT product_name, rating
FROM amazon_products
ORDER BY rating DESC
LIMIT 10;