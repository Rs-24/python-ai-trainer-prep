# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/rearrange-spaces-between-words/description/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Time: O(n), n = len(text)
        # Space, excluding output: O(n)
        space_count = text.count(" ")
        text = text.split()
        word_count = len(text)
        if word_count == 1:
            return text[0] + " " * space_count
        space_width, additional_spaces = divmod(space_count, (word_count - 1))
        spaces = " " * space_width
        return spaces.join(text) + " " * additional_spaces


