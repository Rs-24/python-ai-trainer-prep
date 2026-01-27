# Time to write all of below including tests, explanation and time and aux 
# space: 27 mins

# Problem: https://leetcode.com/problems/customers-who-never-order/description/

"""
SELECT c.name as Customers
FROM Customers c
JOIN Orders o
ON c.id <> o.customerId 
"""

# Tests:
# Customers
# id - name
# 1 - John
# 2 - Jane
# 3 - Joe
#
# Orders:
# id - customerId
# 1 - 2
# 2 - 3
#
# Expected output:
# Customers
# John

# Customers
# id - name
# 1 - John
# 2 - Jane
# 3 - Joe
#
# Orders:
# id - customerId
# 1 - 1
# 2 - 2
# 3 - 3
#
# Expected output:
# Customers

# Customers
# id - name
# 1 - John
# 2 - Jane
# 3 - Joe
#
# Orders:
# id - customerId
#
# Expected output:
# Customers
# John
# Jane
# Joe

# Explanation: The tables are joined via inner join where the id in the
# Customers table is not in the customerId column in the Orders table
# Time: depends on query plan, e.g. O(n + m) for hash method, O(n*m) for
# nested loop method where n, m = number of rows in Customers, Orders
# Aux space, excluding output and input: depends on query plan,
# e.g. O(min(n, m)) for hash method, O(1) for nested loop method
#
# Learning lessons (done after completing all of above in 27 mins):
#   - I now realise my solution is wrong. My rewrite is below:
#
# SELECT c.name AS Customers
# FROM Customers c
# LEFT JOIN Orders o
#   ON c.id = o.customerId
# WHERE o.customerId IS NULL;
# Time: depends on query plan, e.g. O(n) for hash method, O(n^2) for nested
# loop method
# Aux space, excluding output and input: depends on query plan,
# e.g. O(min(n, m)) for hash method, O(1) for nested loop method
#
#   - Additionally, there is also another method using NOT IN, my attempt is
#     below:
#
# SELECT name AS Customers
# FROM Customers
# WHERE id NOT IN (
# SELECT customerId
# FROM Orders
# )
# Time: depends on query plan, e.g. O(n + m) for hash method (O(m) is for one 
# pass through Orders, O(n) is for hashing method), O(m + n*m) for nested loop
# method (O(m) for one pass through Orders, O(n*m) for checking if each id is
# in the subquery result)
# Aux space, excluding output and input: depends on query plan, e.g. O(n + m)
# for hash method (O(m) for subquery result, O(n) for hash table of Orders),
# or O(m) for nested loop method, where O(m) is for the subquery result
#
#   - Additionally, there is also another method using NOT EXISTS, my attempt
#     is below:
#
# SELECT c.name AS Customers
# FROM Customers c
# WHERE NOT EXISTS (
#   SELECT 1
#   FROM Orders o
#   WHERE o.customerId = c.id
# );
# Time: depends on query plan, e.g. O(n + m) for hash method, O(n*m) for
# nested loop method, where n, m = number of rows in Customers, Orders
# Aux space, excluding output and input: depends on query plan, e.g.
# O(min(n, m)) for hash method, or O(1) for nested loop method







