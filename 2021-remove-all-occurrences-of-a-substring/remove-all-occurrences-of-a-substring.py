class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l=len(part)
        stack=[]
        for i in range(len(s)):
            stack.append(s[i])
            if stack  and len(stack)>=l and "".join(stack[-l:])==part:
                i=l
                while i>0:
                    stack.pop()
                    i-=1
          
           
        return "".join(stack)

                
