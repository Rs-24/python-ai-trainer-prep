# Time to write all of below including tests, explanation and time and aux 
# space: 16 mins

# Problem: https://leetcode.com/problems/combine-two-tables/description/

"""
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId
"""

# Tests:

# Person:
# personId - lastName - firstName
# 1 - Doe - John
# 2 - Doe - Jane
#
# Address
# addressId - personId - city - state
# 3 - 1 - New York City - New York
# 4 - 2 - Chicago - Illinois
#
# Expected output:
# firstName - lastName - city - state
# John - Doe - New York City - New York
# Jane - Doe - Chicago - Illinois
 
# Person:
# personId - lastName - firstName
# 1 - Doe - John
# 2 - Doe - Jane
#
# Address
# addressId - personId - city - state
# -- no rows --
#
# Expected output:
# firstName - lastName - city - state
# John - Doe - Null - Null
# Jane - Doe - Null - Null
 
# Person:
# personId - lastName - firstName
# 1 - Doe - John
#
# Address
# addressId - personId - city - state
# 2 - 1 - New York City - New York
#
# Expected output:
# firstName - lastName - city - state
# John - Doe - New York City - New York

# Person:
# personId - lastName - firstName
# -- no rows -- 
#
# Address
# addressId - personId - city - state
# -- no rows -- 
#
# Expected output:
# firstName - lastName - city - state
# -- no rows --

# Explanation: the code does a left join with Person and Address via the
# parameter personId, and obtains the first name, last name, city and state
# from the relevant tables
# Time: depends on query plan, e.g. O(n + m) with hash method or O(n * m) for
# nested loop method, n = number of rows in Person, m = number of rows in
# Address
# Space: depends on query plan, e.g. O(min(m, n)) for hash method, O(1) for
# nested loop method

# Learning lessons (done after completing all of above in 16 mins):
#   - No major learning lessons




