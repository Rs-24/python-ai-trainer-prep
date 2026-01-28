# Time to write all of below including tests, explanation and time and aux
# and total space: 52 mins

# I required help from chatGPT to solve this problem

# Problem: https://leetcode.com/problems/tenth-line/description/

"""
sed -n '10p' file.txt
"""

# Tests:
#
# file.txt consists of the below:
# q1
# 4w
# 6r
# 2f
# 35t
# 5q
# 7c
# 2r
# 45h
# 13y
# 165
#
# It should output 13y
#
# file.txt consists of the below:
# Hi 
# There
#
# It should output nothing

# Explanation: the code uses the sed command with -n to prevent it from
# outputting every line. Then it does '10p' to print just the tenth line 
# from file.txt
# Time: O(1)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 52 mins):
#   - There is another way to solve this problem using awk, my attempt is
#     below: 
#
# awk 'NR==10 { print }' file.txt
# Time: O(1)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)
#
#   - Additionally, there is another method using head and tail pointers,
#     my attempt is below:
#
# tail -n +10 file.txt | head -n 1
# Time: O(n), n = number of lines in file.txt
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)












