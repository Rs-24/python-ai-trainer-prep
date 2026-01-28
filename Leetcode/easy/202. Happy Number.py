# Time to write all of below including tests, explanation and time and aux
# and total space: 29 mins

# Problem: https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:        
        seen = set()
        while n != 1:
            total = 0
            s = str(n)
            for d in s:
                total += int(d)**2
            n = total
            if n in seen:
                return False
            seen.add(n)
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isHappy(1) == True
    assert sol.isHappy(2) == False
    assert sol.isHappy(19) == True
    assert sol.isHappy(82) == True
    assert sol.isHappy(68) == True
    assert sol.isHappy(10) == True
    assert sol.isHappy(100) == True
    assert sol.isHappy(1000) == True

# Explanation: The code repeatedly finds the sum of the squares of its digits,
# while adding each number to the set seen. If any numbers are repeats, then
# False is returned, and if 1 is reached, then True is returned
# Time: O(k), k = number of iterations completed
# Aux space, excluding output and input: O(max(k, len(s)))
# Total space, including output, excluding input: O(max(k, len(s)))

# Learning lessons (done after completing all of above in 29 mins):
#   - My complexity comments could have been improved. My rewrite is below: 
#
# Time: O(k * d), k = number of iterations in while loop, d = number of digits in
# n per iteration 
# Aux space, excluding output and input: O(k), due to seen set
# Total space, including output, excluding input: O(k)
#
#   - There is another solution using Floyd's version, my attempt is below:
#
# def isHappy(self, n: int) -> bool:
#     # Time: O(k * d), k = number of loops completed in while loop, d = 
#     # number of digits in each argument to next_num() 
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     def next_num(num: int) -> int:
#         total = 0
#         while num != 0:
#             total += (num % 10)**2
#             num //= 10
#         return total
#     slow = fast = n
#     while slow != 1 and fast != 1:
#         slow = next_num(slow)
#         fast = next_num(next_num(fast))
#         if slow == fast:
#             return False
#     return True












