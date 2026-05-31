

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if money < children:
            return -1
        money -= children
        max_8 = min(money // 7, children)
        money -= max_8 * 7
        children -= max_8
        if children == 0 and money > 0:
            return max_8 - 1
        if children == 1 and money == 3:
            if max_8 > 0:
                return max_8 - 1
        return max_8


