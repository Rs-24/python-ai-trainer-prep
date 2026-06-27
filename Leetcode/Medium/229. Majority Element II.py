

class Solution:
    def majorityElement(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(1)
        a = b = None
        c1 = c2 = 0
        for x in nums:
            if x == a:
                c1 += 1
            elif x == b:
                c2 += 1
            elif c1 == 0:
                a = x
                c1 = 1
            elif c2 == 0:
                b = x
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = c2 = 0
        for x in nums:
            c1 += x == a
            c2 += x == b
        out = []
        if c1 > len(nums) // 3:
            out.append(a)
        if c2 > len(nums) // 3:
            out.append(b)
        return out


