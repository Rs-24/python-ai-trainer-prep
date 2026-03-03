# Time to write all of below including tests, why the solution works and time 
# and space complexity: 10 mins

# Problem: https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev_prev = 1
        prev = 2
        for i in range(3, n + 1):
            cur = prev + prev_prev
            prev_prev = prev
            prev = cur
        return prev

if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(4) == 5
    assert sol.climbStairs(5) == 8

# Explanation: the code uses the logic that num_ways(n) = num_ways(n - 1) +
# num_ways(n - 2), and iterates up to n while storing the previous and 
# previous previous values which represent the number of ways for n - 1 and 
# n - 2 steps respectively
# Time: O(n)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)


