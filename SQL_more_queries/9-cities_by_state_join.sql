-- Task: List all cities with their corresponding state names

-- Select cities and their state names using an inner join.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
