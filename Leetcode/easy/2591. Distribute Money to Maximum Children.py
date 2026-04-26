# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/distribute-money-to-maximum-children/description/

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if money < children:
            return -1
        money -= children
        max_eights = min(money // 7, children)
        money -= max_eights * 7
        children -= max_eights
        if children == 0 and money > 0:
            return max_eights - 1
        if children == 1 and money == 3:
            if max_eights > 0:
                return max_eights - 1
        return max_eights


