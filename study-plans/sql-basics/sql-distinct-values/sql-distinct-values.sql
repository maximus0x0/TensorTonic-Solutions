-- Write your SQL query here
SELECT customer_name, 
    count(distinct product) AS unique_products
FROM orders
group by customer_name
ORDER BY unique_products DESC, customer_name ASC;