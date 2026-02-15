# Time to write all of below including tests, why the solution works and time 
# and space complexity: 9 mins

# Problem: https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i**2 < x:
            i += 1
        return i if i**2 == x else i - 1

if __name__ == "__main__":
    sol = Solution()
    assert sol.mySqrt(0) == 0
    assert sol.mySqrt(1) == 1
    assert sol.mySqrt(2) == 1
    assert sol.mySqrt(3) == 1
    assert sol.mySqrt(4) == 2
    assert sol.mySqrt(5) == 2
    assert sol.mySqrt(36) == 6
    assert sol.mySqrt(48) == 6

# Explanation: the code iterates from i = 0 to x, and stops the loop once
# i to the power of 2 is greater than or equal to x, then i is returned if
# i**2 == x, otherwise i - 1 is returned
# Time: O(x)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 9 mins):
#   - I now realise there is a method with O(log x) time complexity, my
#     rewrite is below:
#
# def mySqrt(self, x: int) -> int:
#     # Time: O(log x)
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1) 
#     l, r = 0, x
#     while l <= r:
#         mid = (l + r) // 2
#         square = mid**2
#         if square == x:
#             return mid
#         elif square < x:
#             l = mid + 1
#         else:
#             r = mid - 1
#         return r




