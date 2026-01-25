# Time to write all of below including tests, explanation and time and aux 
# space: 2h 34 mins

# I hadn't used SQL before, so I required help from chatGPT to solve this one  

# Problem: https://leetcode.com/problems/combine-two-tables/description/

"""
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId
"""

# Tests: not applicable

# Explanation: the relevant columns are selected from both tables, and a left 
# join is used so that everyone in the person table is shown even if they 
# aren't in the address table. Information between the tables is linked via 
# personId
# Time: not applicable
# Aux space/total space: not applicable

# Learning lessons (done after completing all of above in 2h 34 mins):
#   - My tests could have been improved. My rewrite is below:
#
# Tests:
# Person
# personId - lastName - firstName
# 1 - Doe - John
# 2 - Doe - Jane
# 3 - Smith - Alex
#
# Address:
# addressId - personId - city - state
# 1 - 2 - New York City - New York 
# 2 - 3 - Chicago - Illinois
#
# Expected output:
# firstname - lastname - city - state
# John - Doe - NULL - NULL
# Jane - Doe - New York City - New York
# Alex - Smith - Chicago - Illinois
#
#   - Additionally, my complexity comments could have also been improved. My 
#     rewrite is below:
#
# Time: typically O(n + m) using hash join, worst case O(n * m) with
# nested loop join, where n = num_rows(person), and m = num_rows(address)
# Aux space: O(min(n, m)) for hash join, O(1) for nested loop join










