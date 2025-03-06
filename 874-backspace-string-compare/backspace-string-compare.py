class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for i in range(len(s)):
            if  s[i] == "#":
                if stack_s :
                    stack_s.pop()
                continue
            stack_s.append(s[i])
        for i in range(len(t)):
            if  t[i] == "#":
                if stack_t:
                  stack_t.pop()
                continue
            stack_t.append(t[i])
        return "".join(stack_t) == "".join(stack_s)