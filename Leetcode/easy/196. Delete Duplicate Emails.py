# Time to write all of below including tests, explanation and time and aux 
# space: 13 mins

# Problem: https://leetcode.com/problems/delete-duplicate-emails/description/

"""
DELETE d
FROM Person d
JOIN Person p
ON p.email = d.email
AND d.id > p.id;
"""

# Tests:

# Person:
# id - email
# 1 - a@b.com
# 2 - c@d.com
# 3 - a@b.com
#
# Expected Person table after deletion:
# Person
# id - email
# 1 - a@b.com
# 2 - c@d.com

# Person:
# id - email
# 1 - a@b.com
# 2 - c@d.com
#
# Expected Person table after deletion:
# Person
# id - email
# 1 - a@b.com
# 2 - c@d.com

# Person:
# id - email
# -- no rows --
#
# Expected Person table after deletion:
# Person
# id - email
# -- no rows --

# Explanation: the code does a self join with a DELETE on p.email = d.email,
# and d.id > p.id
# Time: depends on query plan, e.g. O(n) for hash method, O(n^2) for nested
# loop method, n = number of rows in Person
# Space: depends on query plan, e.g. O(n) for hash method, O(1) for nested
# loop method 


