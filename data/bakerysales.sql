SQL QUERIES- Bakery Sales

1. Extract all bakery sales
SELECT *
FROM bakery_sales;

2. Extract sales for a specific day
SELECT *
FROM bakery_sales
WHERE `day of week` = 'Friday'; 

3. Get total revenue by day
SELECT
    `day of week`,
    SUM(total) AS total_revenue
FROM bakery_sales
GROUP BY `day of week`
ORDER BY total_revenue DESC; 

4. Get average order value by day
SELECT
    `day of week`,
    AVG(total) AS avg_order_value
FROM bakery_sales
GROUP BY `day of week`
ORDER BY avg_order_value DESC; 

5. Get highest and lowest order values
SELECT
    MAX(total) AS highest_order,
    MIN(total) AS lowest_order,
    AVG(total) AS average_order
FROM bakery_sales; 

6. Extract orders above the average order value
SELECT *
FROM bakery_sales
WHERE total > (
    SELECT AVG(total)
    FROM bakery_sales
); 

7. Orders containing Tiramisu
SELECT *
FROM bakery_sales
WHERE tiramisu > 0; 

8. Orders containing Angbutter
SELECT *
FROM bakery_sales
WHERE angbutter > 0;
