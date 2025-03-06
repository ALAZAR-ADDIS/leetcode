class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        for i in range(len(s)):
            if s[i]== "(":
                stack.append(0)
            elif stack[-1] == 0:
                stack[-1] = 1
            else:
                val = 0
                while stack[-1] != 0:
                    val += stack.pop()
                stack[-1] = val * 2
        return sum(stack)

        