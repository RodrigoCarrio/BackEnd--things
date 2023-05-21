USE classicmodels;

SELECT 
	employeeNumber
    , lastName
    , firstName
FROM
	employees
WHERE
	employeeNumber > 1060
ORDER BY 
	lastName;

SELECT
	customerNumber
    , checkNumber
FROM
	payments
WHERE
	customerNumber BETWEEN 110 AND 120;
    
SELECT
	country
    , state
    , city
    , addressLine1
    , addressLine2
FROM 
	offices
WHERE
	addressLine2 IS NOT NULL AND
	city LIKE "%o%"
ORDER BY
	country DESC
    , state ASC;
    