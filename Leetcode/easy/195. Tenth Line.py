# Time to write all of below including tests, explanation and time and aux
# and total space: 17 mins

# Problem: https://leetcode.com/problems/tenth-line/description/

# sed -n '10p' file.txt

# Tests:

# file.txt has the following lines:
# Hi 
# hello
# hiya
# good day
# bye
# goodbye
# Hi 
# hello
# hiya
# good day
# bye
# goodbye
#
# Expected output:
# good day

# file.txt has the following lines:
# Hi 
# hello
#
# Expected output:
# -- no output --

# file.txt has the following lines:
# -- no lines --
#
# Expected output:
# -- no output --

# Explanation: the script uses sed to be able to print out the relevant line,
# and uses -n so it doesn't output every line. Then it does '10p' so that it only
# prints the 10th line
# Time: O(n), n = number of lines in file
# Space: O(1)

# awk method:
# Time: O(n), n = number of lines in file.txt
# Space: O(1)
# awk 'NR == 10 { print }' file.txt

# head and tail method:
# Time: O(n), n = number of lines in file.txt
# Space: O(1)
# tail -n +10 file.txt | head -n 1


