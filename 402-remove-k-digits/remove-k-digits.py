class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            
            while k>0 and stack and stack[-1]>i:
             
                stack.pop()
                k-=1
            stack.append(i)
        

        # while k>0:
        #   stack.pop()
        #   k-=1
        stack=stack[:len(stack)-k]
        i=0
        while i<len(stack) and stack[i]=="0":
            i+=1
        stack=stack[i:]
        

        return "".join(stack) if stack else "0"
            
            
        