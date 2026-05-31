

class Solution:
    def distinctDifferenceArray(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        o = []
        l = set()
        r = set(nums)
        for n in nums:
            l.add(n)
            r.remove(n)
            o.append(len(l) - len(r))
        return o


