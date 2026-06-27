

class Solution:
    def wiggleSort(self, nums: list) -> None:
        # Time: O(n log n)
        # Space: O(n)
        nums.sort()
        n = len(nums)
        m = (n + 1) // 2
        l = nums[:m][::-1]
        r = nums[m:][::-1]
        i = 0
        for j in range(len(l)):
            nums[i] = l[j]
            i += 2
        i = 1
        for j in range(len(r)):
            nums[i] = r[j]
            i += 2


