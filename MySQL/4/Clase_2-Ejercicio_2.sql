USE classicmodels;

SELECT DISTINCT
	productCode
FROM
	orderdetails
ORDER BY
	productCode DESC;
    
SELECT
	country
    , city
FROM
	customers
ORDER BY
	country ASC
    , city DESC
LIMIT
	5 , 5;
