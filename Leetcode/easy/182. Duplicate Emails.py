# Time to write all of below including tests, explanation and time and aux 
# space: 9 mins

# Problem: https://leetcode.com/problems/duplicate-emails/description/

"""
SELECT p.email AS Email
FROM Person p
WHERE p.email = (
  SELECT p.email
  FROM Person d
  WHERE p.id != d.id
);
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

# Explanation: the query finds emails which are also in the same table but
# with a different id, as these correspond to the duplicates
# Time: depends on query plan, e.g. O(n) for hash method, or O(n^2) for 
# nested loop method, where n = number of rows in table
# Aux space, excluding output and input: depends on query plan, e.g. O(n) for
# hash method, or O(1) for nested loop method

# Learning lessons (done after completing all of above in 9 mins):
#   - I now realise my solution is wrong. My rewrite is below:
#
# SELECT email AS Email
# FROM Person
# GROUP BY email
# HAVING COUNT(*) > 1
# Time: depends on query plan, e.g. O(n) using hash method, where n = number of rows in table
# Aux space, excluding output and input: depends on query plan, e.g. O(k) for
# hash method where k = number of distinct emails, worst case O(n)
#
#   - Additionally, there is another method using a self-join. My attempt is
#     below:
#
# SELECT DISTINCT p.email AS Email
# FROM Person p
# JOIN Person d
# ON p.email = d.email
# AND p.id <> d.id;
# Time: depends on query plan, e.g. O(n) with hash method, or O(n^2) with nested
# loop method
# Aux space, excluding output and input: depends on query plan, e.g. O(n) for
# hash method, and O(1) for nested loop method
#
#   - Additionally, my tests could have been improved. My new tests are below:
#
# Tests:
# Person
# id - email
# 1 - a@b.com
# 2 - c@d.com
# 3 - a@b.com
# Expected output:
# Email
# a@b.com
#
# Person
# id - email
# 1 - a@b.com
# 2 - c@d.com
# 3 - e@bf.com
# Expected output:
# Email
# -- no rows --
#
# Person
# id - email
# 1 - a@b.com
# 2 - a@b.com
# 3 - a@b.com
# Expected output:
# Email
# a@b.com
#
# Person
# id - email
# 1 - a@b.com
# Expected output:
# Email
# -- no rows --




