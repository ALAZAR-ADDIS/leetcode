class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for i in s:
            if i==")":
                if stack[-1]==0:
                    stack[-1]=1
                else:
                    total=0
                    while stack[-1]!=0:
                        total+=stack.pop()
                    stack[-1]=total*2
                        
            else:
                stack.append(0)

        return sum(stack)
        