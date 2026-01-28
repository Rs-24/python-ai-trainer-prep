# Time to write all of below including tests, explanation and time and aux 
# space: 60 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/delete-duplicate-emails/description/

"""
DELETE p
FROM Person p
JOIN Person d
  ON p.email = d.email
  AND p.id > d.id;
"""

# Tests:

# Person
# id - email
# 1 - a@b.com
# 2 - a@b.com
# 3 - a@b.com
# 4 - c@d.com
# 5 - c@d.com
#
# Expected output: 
# id - email
# 1 - a@b.com
# 4 - c@d.com

# Person
# id - email
# 1 - a@b.com
# 4 - c@d.com
#
# Expected output: 
# id - email
# 1 - a@b.com
# 4 - c@d.com

# Person
# id - email
# 1 - a@b.com
#
# Expected output: 
# id - email
# 1 - a@b.com

# Person
# id - email
# 1 - a@b.com
# 2 - a@b.com
#
# Expected output: 
# id - email
# 1 - a@b.com

# Person
# id - email
# -- no rows --
#
# Expected output: 
# id - email
# -- no rows --

# Explanation: The code does a self join on the table and deleted all rows where
# emails match and where the p.id > d.id
# Time: depends on query plan, e.g. O(n) for hash method, O(n^2) for nested loop
# method, where n = number of rows in Person
# Aux space, excluding output and input: depends on query plan, e.g. O(n) for hash
# method, O(1) for nested loop method

# Learning lessons (done after completing all of above in 60 mins):
#   - No major learning lessons










