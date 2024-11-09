class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack=[]
        end={n:i for i,n in enumerate(s)}

        for i,n in enumerate(s):
            if n  not in stack:
                while stack and stack[-1]>n and end[stack[-1]]>i:
                    stack.pop()
                stack.append(n)
        return "".join(stack)
        