-- ### Topic 1: Aggregation, Filtering & Case Clauses

-- #### Problem 1.1: Marketplace Completion & Cancellation Breakdown
-- * **Business Context**: Operations teams track trip states to spot marketplace friction. 
-- Write a query to find the total number of trip requests and the percentage breakdown of each status (`completed`, `cancelled_by_rider`, `cancelled_by_driver`, `no_driver`) across all cities.
-- * **SQL Focus**: Aggregate functions, `CASE` statement with aggregate (`SUM(CASE ...)`), percentages.
-- * **Question**: For every city name, calculate:
--   1. Total trip requests.
--   2. Percentage of trips that were completed.
--   3. Percentage of trips cancelled by riders.
--   4. Percentage of trips resulting in `no_driver`.
--   Order the results by total requests descending.

SELECT 
  c.city_name, 
  COUNT(t.trip_id) AS total_requests,
  ROUND(SUM(CASE WHEN t.status = 'completed' THEN 1 ELSE 0 END) * 100 / COUNT(t.trip_id), 2) AS rate_trips_completed,
  ROUND(SUM(CASE WHEN t.status = 'cancelled_by_rider' THEN 1 ELSE 0 END) * 100 / COUNT(t.trip_id), 2) AS rate_trips_cancelled_by_riders,
  ROUND(SUM(CASE WHEN t.status = 'no_driver' THEN 1 ELSE 0 END) * 100 / COUNT(t.trip_id), 2) AS rate_trips_no_driver
FROM trips t
LEFT JOIN cities c
ON t.city_id = c.city_id
GROUP BY c.city_name
ORDER BY total_requests DESC;

-- Rank the top 5 uber drivers by ratings
WITH UberDriversRanked AS (
  SELECT
    first_name,
    signup_date,
    TIMESTAMPDIFF(YEAR, signup_date, NOW()) AS years_singned_up,
    TIMESTAMPDIFF(MONTH, signup_date, NOW()) AS months_signed_up,
    rating,
    RANK() OVER(ORDER BY rating DESC) AS driver_rank
  FROM
    drivers
  WHERE rating IS NOT NULL
)
SELECT *
FROM UberDriversRanked
WHERE driver_rank = 1
ORDER BY signup_date DESC
LIMIT 5;
