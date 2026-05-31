

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Time: O(1)
        # Space: O(1)
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        a_a = sum(m[:(int(arriveAlice[:2]) - 1)]) + int(arriveAlice[3:])
        l_a = sum(m[:(int(leaveAlice[:2]) - 1)]) + int(leaveAlice[3:])
        a_b = sum(m[:(int(arriveBob[:2]) - 1)]) + int(arriveBob[3:])
        l_b = sum(m[:(int(leaveBob[:2]) - 1)]) + int(leaveBob[3:])
        return max(0, min(l_a, l_b) - max(a_a, a_b) + 1)


