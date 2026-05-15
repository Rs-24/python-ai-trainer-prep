

class Solution:
    def checkIfExist(self, arr: list) -> bool:
        # Time: O(n), n = len(arr)
        # Space: O(n)
        seen = set()
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False


