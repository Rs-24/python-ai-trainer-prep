

from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: list) -> list:
        # Time: O(n)
        # Space: O(n)
        groups = defaultdict(list)
        ans = []
        for person, size in enumerate(groupSizes):
            groups[size].append(person)
            if len(groups[size]) == size:
                ans.append(groups[size])
                groups[size] = []
        return ans


