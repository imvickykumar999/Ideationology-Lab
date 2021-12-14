show databases;
use w3schools;
SELECT DISTINCT Country FROM Customers;
SELECT Country FROM Customers;

SELECT COUNT(DISTINCT Country) FROM Customers;

SELECT * FROM Customers
WHERE Country='Mexico';

SELECT * FROM Customers
WHERE CustomerID=1;

SELECT * FROM Customers;
SELECT * FROM Categories;
SELECT * FROM Employees;
SELECT * FROM Orders;
SELECT * FROM Products;