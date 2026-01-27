# Time to write all of below including tests, explanation and time and aux
# and total space: 23 mins

# Problem: https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        power = 0

        while 2**power < n:
            power += 1
        
        count = 0

        total = n

        while total > 0:
            if 2**power <= total:
                total -= 2**power
                count += 1
            power -= 1
        
        return count

if __name__ == "__main__":
    sol = Solution()
    assert sol.hammingWeight(1) == 1
    assert sol.hammingWeight(2) == 1
    assert sol.hammingWeight(3) == 2
    assert sol.hammingWeight(4) == 1
    assert sol.hammingWeight(2**10 - 1) == 10
    assert sol.hammingWeight(2**31 - 1) == 31

# Explanation: the max power of two is calculated, and then the function
# iterates until total <= 0, and increments count accordingly which represents
# the number of ones in the binary number. Then count is returned once the loop
# ends
# Time: O(n)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 23 mins):
#   - I now realise my solution is wrong, my rewrite is below:
#
# def hammingWeight(self, n: int) -> int:
#     # Time: O(log n)
#     # Aux space, excluding output and input: O(1) 
#     # Total space, including output, excluding input: O(1) 
#     count = 0
#     while n:
#         count += (n & 1)
#         n >>= 1
#     return count
#
#   - Additionally, there is also a Brian Kernighan method, my attempt is below:
#
# def hammingWeight(self, n: int) -> int:
#     # Time: O(m), m = number of set bits in n
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     count = 0
#     while n:
#         n &= (n-1)
#         count += 1
#     return count











