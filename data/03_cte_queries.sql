USE mysql;

WITH PopularProducts AS (
  SELECT
    p.product_name AS ProductName,
    SUM(o.quantity) AS TotalQuantitySold
  FROM products p
  LEFT JOIN order_items o
  ON p.product_id = o.product_id
  GROUP BY p.product_name
  HAVING SUM(o.quantity) > 10 
)
SELECT *
FROM PopularProducts
ORDER BY TotalQuantitySold DESC;