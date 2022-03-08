
-- https://www.w3schools.com/sql/sql_select.asp

show databases;

use w3schools;

SELECT DISTINCT Country FROM Customers;
SELECT Country FROM Customers;

SELECT COUNT(DISTINCT Country) FROM Customers;

SELECT * FROM Customers
WHERE Country='Mexico';

SELECT * FROM Customers
WHERE CustomerID=1;

SELECT * FROM Customers
WHERE Country='Germany' AND City='Berlin';

SELECT * FROM Customers
WHERE City='Berlin' OR City='München';

SELECT * FROM Customers
WHERE Country='Germany' OR Country='Spain';

SELECT * FROM Customers
WHERE NOT Country='Germany';

SELECT * FROM Customers
WHERE Country='Germany' AND (City='Berlin' OR City='München');

SELECT * FROM Customers
WHERE NOT Country='Germany' AND NOT Country='USA';

SELECT * FROM Customers
ORDER BY Country;

SELECT * FROM customers
ORDER BY Country DESC;

SELECT * FROM Customers
ORDER BY Country, CustomerName;

-- hand written...

select * from customers
order by country asc, CustomerName desc;

-- use w3schools;

SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

/*
Note: 
The LEFT JOIN keyword returns all records from the left table (Customers), 
even if there are no matches in the right table (Orders).
*/

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

SELECT Orders.OrderID, Employees.LastName, 
Employees.FirstName, Employees.EmployeeID, Orders.EmployeeID
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;

SELECT MIN(Price) AS SmallestPrice
FROM Products;

SELECT MAX(Price) AS LargestPrice
FROM Products;

SELECT COUNT(ProductID)
FROM Products;

SELECT AVG(Price)
FROM Products;

SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';

SELECT * FROM Customers
WHERE City LIKE '_ondon';

SELECT * FROM Customers
WHERE City LIKE '[bsp]%';

SELECT * FROM Customers
WHERE City LIKE '[a-c]%';

SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');

SELECT Country FROM Suppliers;

SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID NOT IN (1,2,3);

SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;

SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';

-- SQL Aliases

/*
SQL aliases are used to give a table, 
or a column in a table, a temporary name.

Aliases are often used to make column names more readable.
*/

SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;

SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
FROM Customers;

SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address
FROM Customers;

SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName='Around the Horn' AND c.CustomerID=o.CustomerID;

SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
FROM Customers, Orders
WHERE Customers.CustomerName='Around the Horn' AND Customers.CustomerID=Orders.CustomerID;

INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM Suppliers;

select * from customers;

SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    WHEN City IS NULL THEN Country
    ELSE City
END);

-- -------------------------------

CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;

select * from TestTable;

 -- ------------------------------

