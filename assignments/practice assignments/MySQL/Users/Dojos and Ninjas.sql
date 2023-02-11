SELECT * FROM dojos_and_ninjas_schema.ninja;
SELECT *
FROM dojos_and_ninjas_schema.dojo
JOIN ninja
ON dojo.id = ninja.dojo_id
WHERE dojo.id = 4;
SELECT *
FROM dojos_and_ninjas_schema.dojo
JOIN ninja
ON dojo.id = ninja.dojo_id
WHERE dojo.id = 6;
SELECT * FROM dojos_and_ninjas_schema.dojo
WHERE dojo.id = (SELECT dojo_id FROM ninja ORDER BY dojo_id DESC LIMIT 1);