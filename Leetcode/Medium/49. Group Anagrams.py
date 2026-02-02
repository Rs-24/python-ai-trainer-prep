# Time to write all of below including tests, explanation and time and aux
# and total space: 26 mins

# Problem: https://leetcode.com/problems/group-anagrams/description/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        def check(string1: str, string2: str) -> bool:
            d1 = {}
            for ch in string1:
                d1[ch] = d1.get(ch, 0) + 1
            d2 = {}
            for ch in string2:
                d2[ch] = d2.get(ch, 0) + 1
            return d1 == d2
        out = []
        cur_anagrams = []
        done = []
        for i, s1 in enumerate(strs):
            if i in done:
                continue
            cur_anagrams = [s1]
            done.append(i)
            for j, s2 in enumerate(strs):
                if j <= i:
                    continue
                if check(s1, s2):
                    cur_anagrams.append(s2)
                    done.append(j)
            out.append(cur_anagrams)
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]
    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["", ""]) == [["", ""]]
    assert sol.groupAnagrams(["", "a"]) == [[""], ["a"]]
    assert sol.groupAnagrams(["a", "a"]) == [["a", "a"]]
    assert sol.groupAnagrams(["ab", "ba"]) == [["ab", "ba"]]
    assert sol.groupAnagrams(["ate", "tea", "eat", "cat"]) == [["ate", "tea", "eat"], ["cat"]]

# Explanation: the code uses a nested loop to find all possible anagrams,
# groups them together and appends each group to out
# Time: O(n^2), n = len(strs)
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 26 mins):
#   - I now realise there is a faster solution, my rewrite is below:
#
# from collections import defaultdict
# def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#     # Time: O(n * L), n = len(strs), L = average length of all strings in strs
#     # Aux space, excluding output and input: O(n)
#     # Total space, including output, excluding input: O(n)
#     groups = defaultdict(list)
#     for s in strs:
#         count = [0] * 26
#         for ch in s:
#             count[ord(ch) - ord("a")] += 1
#         groups[tuple(count)].append(s)
#     return list(groups.values())
#
#   - Additionally, there is another method using the sorted() function, my
#     rewrite is below:
#
# from collections import defaultdict
# def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#     # Time: O(n * L log L), n = len(strs), L = average length of all strings
#     # in strs
#     # Aux space, excluding output and input: O(n * L)
#     # Total space, including output, excluding input: O(n * L)
#     groups = defaultdict(list)
#     for s in strs:
#         groups["".join(sorted(s))].append(s)
#     return list(groups.values())
#
#   - Additionally, my tests could have been improved. My rewrite is below:
#
# def norm(groups):
#     return tuple(sorted(tuple(sorted(g)) for g in groups))
# if __name__ == "__main__":
#     sol = Solution()
#     assert norm(sol.groupAnagrams([""])) == norm([[""]])
#     assert norm(sol.groupAnagrams(["a"])) == norm([["a"]])
#     assert norm(sol.groupAnagrams(["", ""])) == norm([["", ""]])
#     assert norm(sol.groupAnagrams(["", "a"])) == norm([[""], ["a"]])
#     assert norm(sol.groupAnagrams(["a", "a"])) == norm([["a", "a"]])
#     assert norm(sol.groupAnagrams(["ab", "ba"])) == norm([["ab", "ba"]])
#     assert norm(sol.groupAnagrams(["ate", "tea", "eat", "cat"])) == norm([["ate", "tea", "eat"], ["cat"]])


















