# Time to write all of below including tests, explanation and time and aux
# and total space: 21 mins

# Problem: https://leetcode.com/problems/valid-phone-numbers/description/

# grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt

# Tests:

# file.txt has the following lines:
# (123) 456-7890
# 123-456-7890
# (123)-456-7890
# 123 456-7890
#
# Expected output:
# (123) 456-7890
# 123-456-7890

# file.txt has the following lines:
# -- no lines --
#
# Expected output:
# -- no lines --

# Explanation: the script uses grep -E to search through file.txt, and uses
# single quotes, and a ^ and $ symbol to signify how the line should start
# and end, and uses an | symbol so that either expression is read
# Time: O(n), n = number of lines in file.txt
# Space: O(1)


