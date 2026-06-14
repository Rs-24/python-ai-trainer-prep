

class Solution:
    def recoverOrder(self, order: list, friends: list) -> list:
        # Time: O(n)
        # Space: O(n)
        f = set(friends)
        return [x for x in order if x in f]


