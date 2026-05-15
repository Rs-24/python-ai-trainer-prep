

class Solution:
    def findTheDistanceValue(self, arr1: list, arr2: list, d: int) -> int:
        # Time: O(m * n), m = len(arr1), n = len(arr2)
        # Space: O(1)
        count = 0
        for num1 in arr1:
            valid = 1
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    valid = 0
            count += valid
        return count


