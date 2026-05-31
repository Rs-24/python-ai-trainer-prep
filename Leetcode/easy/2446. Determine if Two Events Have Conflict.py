

class Solution:
    def haveConflict(self, event1: list, event2: list) -> bool:
        # Time: O(1)
        # Space: O(1)
        return event1[1] >= event2[0] and event1[0] <= event2[1]


