SELECT animal_type, COUNT(DATETIME) AS count FROM animal_ins
WHERE animal_type IN('Cat','Dog')
GROUP BY animal_type
order by animal_type;
