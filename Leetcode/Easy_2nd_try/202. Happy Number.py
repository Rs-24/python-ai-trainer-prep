# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        total = 0
        while n not in seen:
            seen.add(n)
            total = 0
            while n > 0:
                total += ((n % 10)**2)
                n //= 10
            n = total
            if n == 1:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.isHappy(1) == True
    assert sol.isHappy(2) == False
    assert sol.isHappy(19) == True
    assert sol.isHappy(100) == True

# Explanation: the code uses a seen set to store seen values, and repeatedly
# calculates the next value of n. If n is in seen, then False is returned,
# and if n is ever equal to 1, then True is returned
# Time: O(k * d), k = number of loops completed in 'while n not in seen:'
# loop, and d = average number of digits in n over all loops within 
# 'while n not in seen:' loop
# Space: O(k)

# Learning lessons (done after completing all of above in 12 mins):
#   - There is another solution using Floyd's version, my attempt is below:
#
# def isHappy(self, n: int) -> bool:
#     # Time: O(k * d), k = number of times 'slow = next_num(slow)' loop runs,
#     # d = average number of digits in x argument to next_nums over all loops
#     # within 'slow = next_num(slow)' loop
#     # Space: O(1)
#     def next_num(x: int) -> int:
#         total = 0
#         while x > 0:
#             total += ((x % 10)**2) 
#             x //= 10
#         return total
#     slow = fast = n
#     while slow != 1 and fast != 1:
#         slow = next_num(slow)
#         fast = next_num(next_num(fast))
#         if slow == fast:
#             return False
#     return True














