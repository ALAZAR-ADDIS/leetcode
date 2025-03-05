class Solution:
    def isValid(self, s: str) -> bool:

        closing = {"]", "}", ")"}

        map = {"]":"[",")":"(", "}":"{"}
        stack = []

        for i in range(len(s)):

            if s[i] in closing:
                if stack and stack[-1] == map[s[i]]:
                    stack.pop()
                    continue
                else:
                    return False

            stack.append(s[i])
        
        return False if len(stack) else True
