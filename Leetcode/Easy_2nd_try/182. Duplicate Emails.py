# Time to write all of below including tests, explanation and time and aux 
# space: 30 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/duplicate-emails/description/

"""
SELECT email AS Email
FROM Person
GROUP BY email
HAVING count(*) > 1
"""

# Tests:

# Person
# id - email
# 1 - a@b.com
# 2 - c@d.com
# 3 - a@b.com
#
# Expected output:
# Email
# a@b.com

# Person
# id - email
# 1 - a@b.com
# 2 - c@d.com
# 3 - a@b.com
# 4 - c@d.com
#
# Expected output:
# Email
# a@b.com
# c@d.com

# Person
# id - email
# 1 - a@b.com
# 2 - c@d.com
#
# Expected output:
# Email
# -- no rows --

# Person
# id - email
# 1 - a@b.com
#
# Expected output:
# Email
# -- no rows --

# Person
# id - email
# -- no rows --
#
# Expected output:
# Email
# -- no rows --

# Explanation: the code groups all the emails together in Person, and only
# outputs the ones with more than one email
# Time: depends on query plan, e.g. O(n) for hash method, n = number of rows
# in Person
# Space: depends on query plan, e.g. O(k) for hash method, k = number of
# unique entries, worst case O(n)

# Learning lessons (done after completing all of above in 30 mins):
#   - Additionally, there is another method using a self-join. My attempt is
#     below:
#
# Time: depends on query plan, e.g. O(n) for hash method, O(n^2) for nested
# loop method, n = number of rows in Person
# Space: depends on query plan, e.g. O(n) for hash method, O(1) for nested
# loop method
# SELECT DISTINCT p.email AS Email
# FROM Person p
# JOIN Person d
# ON p.email = d.email AND p.id <> d.id
