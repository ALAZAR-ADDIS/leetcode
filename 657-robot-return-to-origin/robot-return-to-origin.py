class Solution:
    def judgeCircle(self, moves: str) -> bool:
        k = 0
        j = 0
        for i in moves:
            if i == "L":
                k -= 1
            elif i == "D":
                j -= 1
            elif i == "U":
                j += 1
            else:
                k += 1
        return k == 0 and j == 0
        