

class Solution:
    def sumEvenAfterQueries(self, nums: list, queries: list) -> list:
        # Time: O(n)
        # Space: O(n)
        t, a = sum(x for x in nums if x % 2 == 0), []
        for x, i in queries:
            if nums[i] % 2 == 0:
                t -= nums[i]
            nums[i] += x
            if nums[i] % 2 == 0:
                t += nums[i]
            a.append(t)
        return a


        