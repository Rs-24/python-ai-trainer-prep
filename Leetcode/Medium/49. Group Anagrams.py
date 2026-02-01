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


















