

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        # Time: O(n)
        # Space: O(n)
        e = sum(n % 2 == 0 for n in nums)
        o = len(nums) - e
        out = []
        for n in nums:
            if n % 2 == 0:
                out.append(o)
                e -= 1
            else:
                out.append(e)
                o -= 1
        return out


