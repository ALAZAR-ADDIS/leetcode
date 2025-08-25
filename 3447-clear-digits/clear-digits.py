class Solution:
    def clearDigits(self, s: str) -> str:
        sett = {"0","1","2","3","4","5","6","7","8","9"}

        stack = []
        for i in s:
            if i in sett:

                if stack:
                    stack.pop()
                continue

            stack.append(i)

        return "".join(stack)
