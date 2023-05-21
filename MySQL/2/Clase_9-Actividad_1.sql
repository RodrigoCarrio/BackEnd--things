USE classicmodels;

-- 1.
SELECT 
	productLine AS "Categoria",
    COUNT(quantityInStock) AS "Cantidad"
FROM
	productlines
    INNER JOIN products USING (productLine)
GROUP BY
	productLine;
    
-- 2.
SELECT
	orderNumber AS "Orden",
    SUM(quantityOrdered * priceEach) AS "Monto"
FROM
	orders
    INNER JOIN orderdetails USING (orderNumber)
WHERE
    YEAR(orderDate) = 2005
GROUP BY 
	orderNumber
ORDER BY
	orderNumber DESC;

-- 3.
SELECT DISTINCT
	customerNumber,
    customerName
FROM 
	customers
WHERE
	customerNumber NOT IN (SELECT DISTINCT customerNumber FROM orders)
ORDER BY 
	customerNumber;