-- Counts records sharing the same score, ordered by frequency
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
