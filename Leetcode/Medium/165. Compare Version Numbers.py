

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Time: O(n)
        # Space: O(n)
        v1, v2 = version1.split("."), version2.split(".")
        for i in range(max(len(v1), len(v2))):
            t1 = int(v1[i]) if i < len(v1) else 0
            t2 = int(v2[i]) if i < len(v2) else 0
            if t1 < t2:
                return -1
            if t1 > t2:
                return 1
        return 0


