# Time to write all of below including tests, explanation and time and aux
# and total space: 2h 45 mins

# I hadn't used bash before, and needed help from chatGPT to solve this problem

# Problem: https://leetcode.com/problems/valid-phone-numbers/description/

"""
grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt
"""

# Tests: 
# 
# file.txt has following lines:
# (123) 456-7890
# 123-456-7890
# (123)-456-7890
# 123 456-7890
# (123) 456 7890
# 123 456 7890
# 
# Only the following lines should be outputted:
# (123) 456-7890
# 123-456-7890

# Explanation: the bash code uses grep with extended regex with an OR operator
# to only allow lines which only consist of either allowed phone number type
# Time: O(n), n = number of lines in file.txt
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(k), k = number of lines
# containing valid phone numbers

# Learning lessons (done after completing all of above in 2h 45 mins):
#   - No major learning lessons













