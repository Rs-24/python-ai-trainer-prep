

class Solution:
    def answerQueries(self, nums: list, queries: list) -> list:
        # Time: O(n log n + n^2)
        # Space: O(n)
        nums.sort()
        out = []
        for q in queries:
            total = 0
            length = 0
            for i, num in enumerate(nums):
                total += num
                if total > q:
                    length = i
                    break
                elif i == len(nums) - 1:
                    length = i + 1
            out.append(length)
        return out


