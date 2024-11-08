class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        dict1={n:i for i,n in enumerate(s)}
        
        
        for i,n in enumerate(s):
            
            if n not in stack:
                while stack and stack[-1]>=n and dict1[stack[-1]]>i:
                    stack.pop()
            if n not in stack:
                   stack.append(n)
        return "".join(stack)
        
        