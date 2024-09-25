class Solution:
    def isValid(self, s: str) -> bool:
        braces={"}":"{","]":"[",")":"("}
        stack=[]
        for i in range(len(s)):
            if s[i] in braces  and stack  :
                 if  stack[-1]==braces[s[i]]:
                    stack.pop()
                 else:break
            else:
                stack.append(s[i])
        return True if len(stack)==0 else False
        
                
