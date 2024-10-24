class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        
        for i in s:
            if  i=="#":
                if  stack1:                   
                   stack1.pop()
                continue
            stack1.append(i)
        for  i in t:
            if  i=="#":
                if  stack2:
                    stack2.pop()
                continue
            stack2.append(i)
        return stack2==stack1
            
            
            
        