

class Solution:
    def removeSubfolders(self, folder: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        folder.sort()
        ans = []
        for path in folder:
            if not ans or not path.startswith(ans[-1] + "/"):
                ans.append(path)
        return ans


