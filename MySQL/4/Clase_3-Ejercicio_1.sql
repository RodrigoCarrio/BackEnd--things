USE classicmodels;

SELECT
	lastName
    , firstName
    , jobTitle
    , officeCode
    , city
    , country 
FROM
	employees INNER JOIN
    offices USING(officeCode)
ORDER BY 
	country DESC
    , city ASC
    , lastName ASC;
    
SELECT
	orderLineNumber
    , productCode
    , productName
    , quantityOrdered
    , priceEach
FROM
	orderdetails INNER JOIN
    products USING(productCode)
WHERE
	orderNumber = 10103
ORDER BY
	orderNumber ASC
    , orderLineNumber ASC;