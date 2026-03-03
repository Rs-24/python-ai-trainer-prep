# Time to write all of below including tests, explanation and time and aux
# and total space: 26 mins

# Problem: https://leetcode.com/problems/group-anagrams/description/

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            groups[tuple(count)].append(s)
        out = []
        for count, strings in groups.items():
            out.append(strings)
        return out

def norm(groups):
    return tuple(sorted(tuple(sorted(g)) for g in groups))

if __name__ == "__main__":
    sol = Solution()
    assert norm(sol.groupAnagrams([""])) == norm([[""]])
    assert norm(sol.groupAnagrams(["a"])) == norm([["a"]])
    assert norm(sol.groupAnagrams(["", ""])) == norm([["", ""]])
    assert norm(sol.groupAnagrams(["", "a"])) == norm([[""], ["a"]])
    assert norm(sol.groupAnagrams(["a", "a"])) == norm([["a", "a"]])
    assert norm(sol.groupAnagrams(["ab", "ba"])) == norm([["ab", "ba"]])
    assert norm(sol.groupAnagrams(["ate", "tea", "eat", "cat"])) == norm([["ate", "tea", "eat"], ["cat"]])

# Explanation: the code uses a dictionary of lists, and groups all anagrams
# together according to the count variable, and outputs these groups
# Time: O(c), c = total number of characters in strs
# Space: excluding output: worst case O(26 * n) = O(n), n = len(strs)

# sorted() method:
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time: O(n * L log L), n = len(strs), L = average number of
        # characters per string in strs
        # Space: excluding output: O(n * L)
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())


