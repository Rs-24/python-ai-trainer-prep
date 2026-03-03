# Time to write all of below including tests, explanation and time and aux 
# space: 16 mins

# Problem: https://leetcode.com/problems/rising-temperature/description/

"""
SELECT w.id AS id
FROM Weather w
JOIN Weather prev
ON prev.recordDate = DATE_SUB(w.recordDate, INTERVAL 1 DAY)
WHERE w.temperature > prev.temperature;
"""

# Tests:

# Weather
# id - recordDate - temperature
# 1 - 2026-01-01 - 10
# 2 - 2026-01-02 - 20
# 3 - 2026-01-03 - 10
# 4 - 2026-01-04 - 20
#
# Expected output:
# id
# 2
# 4

# Weather
# id - recordDate - temperature
# 1 - 2026-01-01 - 40
# 2 - 2026-01-02 - 30
# 3 - 2026-01-03 - 20
# 4 - 2026-01-04 - 10
#
# Expected output:
# id
# -- no rows --

# Weather
# id - recordDate - temperature
# 1 - 2026-01-01 - 10
# 2 - 2026-01-02 - 20
# 3 - 2026-01-03 - 30
# 4 - 2026-01-04 - 40
#
# Expected output:
# id
# 2
# 3
# 4

# Weather
# id - recordDate - temperature
# 1 - 2026-01-01 - 10
# 2 - 2026-01-02 - 10
# 3 - 2026-01-03 - 10
# 4 - 2026-01-04 - 10
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

# Explanation: the code does a self join on prev.recordDate being one day
# before w.recordDate and outputs the id where w.temperature > prev.temperature
# Time: depends on query plan, e.g. O(n) for hash method, O(n^2) for nested
# loop method, n = number of rows in Weather
# Space: depends on query plan, e.g. O(n) for hash method, O(1) for nested
# loop method


