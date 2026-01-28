# Time to write all of below including tests, explanation and time and aux 
# space: 19 mins

# Problem: https://leetcode.com/problems/rising-temperature/description/

"""
SELECT w.id
FROM Weather w
JOIN Weather w_prev
  ON w.recordDate = w_prev.recordDate + 1
  AND w.temperature > w_prev.temperature
"""

# Tests:

# Weather
# id - recordDate - temperature
# 1 - 2025-01-01 - 10
# 2 - 2025-01-02 - 25
# 3 - 2025-01-03 - 20
# 4 - 2025-01-04 - 30
#
# Expected output:
# id
# 2
# 4

# Weather
# id - recordDate - temperature
# 1 - 2025-01-01 - 10
#
# Expected output:
# id
# -- no rows --

# Weather
# id - recordDate - temperature
# 1 - 2025-01-01 - 20
# 2 - 2025-01-02 - 15
# 3 - 2025-01-03 - 10
# 4 - 2025-01-04 - 10
#
# Expected output:
# id
# -- no rows -- 

# Weather
# id - recordDate - temperature
# -- no rows --
#
# Expected output:
# id
# -- no rows --

# Explanation: The SQL does a self-join and outputs w.id whereby w.recordDate
# is one day greater than w_prev.recordDate, and whereby w.temperature
# is greater than w_prev.temperature
# Time: depends on query plan, e.g. O(n) for hash method, O(n^2) for nested 
# loop method, where n = number of rows in Weather
# Aux space, excluding output and input: depends on query plan, e.g. O(n) for 
# hash method, O(1) for nested loop method

# Learning lessons (done after completing all of above in 19 mins):
#   - I now realise the line "ON w.recordDate = w_prev.recordDate + 1" is not
#     valid syntax, it should have been: 
#
# ON w_prev.recordDate = DATE_SUB(w.recordDate, INTERVAL 1 DAY)








