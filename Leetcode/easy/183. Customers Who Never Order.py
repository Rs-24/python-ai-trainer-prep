# Time to write all of below including tests, explanation and time and aux 
# space: 14 mins

# Problem: https://leetcode.com/problems/customers-who-never-order/description/

"""
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
"""

# Tests:

# Customers
# id - name
# 1 - John
# 2 - Jane
#
# Orders
# id - customerId
# 3 - 1
#
# Expected output:
# Customers
# Jane  

# Customers
# id - name
# 1 - John
# 2 - Jane
#
# Orders
# id - customerId
# 3 - 1
# 4 - 2
#
# Expected output:
# Customers
# -- no rows --

# Customers
# id - name
# -- no rows --
#
# Orders
# id - customerId
# -- no rows --
#
# Expected output:
# Customers
# -- no rows --

# Explanation: the code does a left join via c.id = o.customerId, and outputs
# the names where o.customerId is NULL
# Time: depends on query plan, e.g. O(n + m) for hash method, O(n * m) for
# nested loop method where n = number of rows in Customers, m = number of rows
# in Orders
# Space: depends on query plan, e.g. O(min(n, m)) for hash method, O(1) for
# nested loop method

# NOT IN method:
# Time: depends on query plan, e.g. O(n + m) for hash method, O(n * m) for
# nested loop method where n = number of rows in Customers, m = number of rows
# in Orders
# Space: depends on query plan, e.g. O(min(n, m)) for hash method, O(1) for
# nested loop method
# SELECT c.name AS Customers
# FROM Customers c
# WHERE c.id NOT IN (
# SELECT o.customerId
# FROM Orders o
# WHERE o.customerId IS NOT NULL
# );

# NOT EXISTS method:
# Time: depends on query plan, e.g. O(n + m) for hash method, O(n * m) for
# nested loop method where n = number of rows in Customers, m = number of rows
# in Orders
# Space: depends on query plan, e.g. O(min(n, m)) for hash method, O(1) for
# nested loop method
# SELECT c.name AS Customers
# FROM Customers c
# WHERE NOT EXISTS (
# SELECT 1
# FROM Orders o
# WHERE o.customerId = c.id
# );


