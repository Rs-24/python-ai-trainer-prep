# Time to write all of below including tests, explanation and time and aux 
# space: 10 mins

# Problem: https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

"""
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
ON e.managerid = m.id
WHERE e.salary > m.salary;
"""

# Tests:

# Employee:
# id - name - salary - managerId
# 1 - John - 30000 - 3
# 2 - Jane - 40000 - 4
# 3 - Adam - 40000 - NULL
# 4 - Sarah - 30000 - NULL
#
# Expected output:
# Employee
# Jane

# Employee:
# id - name - salary - managerId
# 1 - John - 30000 - 3
# 2 - Jane - 40000 - 4
# 3 - Adam - 50000 - NULL
# 4 - Sarah - 60000 - NULL
#
# Expected output:
# Employee
# -- no rows --

# Employee:
# id - name - salary - managerId
# 1 - John - 30000 - NULL
#
# Expected output:
# Employee
# -- no rows --

# Employee:
# id - name - salary - managerId
# -- no rows --
#
# Expected output:
# Employee
# -- no rows --

# Explanation: the code does a self-join where e.managerId = m.id, and only 
# outputs the names where e.salary > m.salary
# Time: depends on query plan, e.g. O(n) for hash method, O(n^2) for nested
# loop method, n = number of rows in Employee
# Space: depends on query plan, e.g. O(n) for hash method, O(1) for nested
# loop method

# Learning lessons (done after completing all of above in 10 mins):
#   - Additionally, there is another method using a correlated subquery. My
#     attempt is below:
#
# Time: depends on query plan, e.g. O(n) for hash method, O(n^2) for nested
# loop method, n = number of rows in Employee
# Space: depends on query plan, e.g. O(n) for hash method, O(1) for nested
# loop method
# SELECT e.name AS Employee
# FROM Employee e
# WHERE e.salary > (
#   SELECT m.salary
#   FROM Employee m
#   WHERE m.id = e.managerId
# );







