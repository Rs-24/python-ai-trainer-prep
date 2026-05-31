

class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        max_num = str(num)
        for d in max_num:
            if d != "9":
                max_num = max_num.replace(d, "9")
                break
        return int(max_num) - int(str(num).replace(str(num)[0], "0"))


