

class Solution:
    def maximumSum(self, arr: list) -> int:
        # Time: O(n)
        # Space: O(1)
        no_delete, one_delete, a = arr[0], float("-inf"), arr[0]
        for i in range(1, len(arr)):
            one_delete = max(one_delete + arr[i], no_delete)
            no_delete = max(no_delete + arr[i], arr[i])
            a = max(a, one_delete, no_delete)
        return a


