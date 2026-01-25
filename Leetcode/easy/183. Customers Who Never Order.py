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







