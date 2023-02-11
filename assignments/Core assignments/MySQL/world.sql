SELECT * FROM world.languages;
SELECT countries.name , languages.language , languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;

SELECT countries.name , COUNT(cities.name) 
FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.name) DESC;

SELECT name , population, country_id FROM cities
WHERE (cities.population>=500000)
AND cities.country_id = ( SELECT id FROM countries WHERE countries.name = "Mexico" )
ORDER BY cities.population DESC;

SELECT languages.language, countries.name,languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;


SELECT name , surface_area, population FROM countries
WHERE surface_area > 501
AND population>100000;


SELECT name ,  capital,life_expectancy FROM countries
WHERE capital > 200
AND life_expectancy > 75;


SELECT countries.name as country_name, cities.name as city_name, cities.district, cities.population from countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.district = "Buenos Aires"
AND cities.population > 500000
ORDER BY cities.population DESC;

SELECT countries.region, COUNT(countries.name) as countries
FROM countries
GROUP BY countries.region
ORDER BY countries DESC;