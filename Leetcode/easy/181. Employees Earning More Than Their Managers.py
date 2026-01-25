# Time to write all of below including tests, explanation and time and aux 
# space: 10 mins

# Problem: https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

"""
SELECT e.name
FROM Employee e
WHERE e.salary > SELECT salary WHERE id is e.managerId
"""

# Tests:
#
# Employee
# id - name - salary - managerId
# 1 - John - 30000 - 3
# 2 - Jane - 40000 - 4
# 3 - Tom - 35000 - Null
# 4 - Alex - 30000 - Null
#
# output should be:
# Employee
# Jane

# Explanation: the name is selected from the table where the salary is 
# greater than the salary of the person corresponding to managerId
# Time: O(n^2) for nested loop method, O(n) for hash method
# Aux space: O(1) for nested loop method, O(n) for hash method

# Learning lessons (done after completing all of above in 10 mins):
#   - I now realise my solution is wrong. My rewrite is below:
#
# SELECT e.name as Employee
# FROM Employee e
# JOIN Employee m
# ON e.managerId = m.id
# WHERE e.salary > m.salary;
# Time: depends on query planner, e.g. O(n) using hash join method, O(n^2) for
# nested loop join method
# Aux space, excluding output and input: depends on join strategy, e.g. O(n)
# for hash join method, O(1) for nested loop method
#
#   - Additionally, there is another method using a correlated subquery. My
#     attempt is below:
#
# SELECT e.name as Employee
# FROM Employee e
# WHERE e.salary > (
#  SELECT m.salary
#  FROM Employee m
#  WHERE m.id = e.managerId 
# );
# Time: depends on query plan, e.g. O(n) using hash method, or O(n^2) for
# nested loop method, where n = number of rows in Employee table
# Aux space, excluding output and input: depends on query plan, e.g. O(n) for
# hash method, or O(1) for nested loop method















