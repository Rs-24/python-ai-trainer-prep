

class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        # Time: O(n)
        # Space: O(n)
        s = []
        j = 0
        for x in pushed:
            s.append(x)
            while s and j < len(popped) and s[-1] == popped[j]:
                s.pop()
                j += 1
        return j == len(popped)


        