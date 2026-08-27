-- ============================================================================
-- PSET_01: Find the top 5 ratings drivers
-- ============================================================================

SELECT first_name, rating, signup_date, driver_status
FROM (
  SELECT
    first_name, rating, signup_date, driver_status,
    RANk() OVER(ORDER BY rating DESC) AS DriverRank
  FROM drivers
) ranked_driver
WHERE DriverRank = 1
ORDER BY signup_date DESC
LIMIT 5;

-- With CTE
WITH TopFiveDrivers AS (
  SELECT 
    CONCAT(first_name, ' ', last_name) AS DriverName,
    signup_date,
    driver_status, 
    rating,
    RANK() OVER(ORDER BY rating DESC) AS DriverRank
  FROM drivers
)
SELECT *
FROM TopFiveDrivers
WHERE DriverRank = 1
ORDER BY signup_date
LIMIT 5;