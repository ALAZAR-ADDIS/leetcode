class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        l=0
        while l<len(tokens):
            val=None
            if tokens[l]=="*":
                val=stack[-1]*stack[-2]
                
            elif tokens[l]=="-":
                val=stack[-2]-stack[-1]
                
            elif tokens[l]=="+":
                val=stack[-1]+stack[-2]
                
            elif tokens[l]=="/":
                val=int(stack[-2]/stack[-1])
                
            else:
                stack.append(int(tokens[l]))
            
            

            if tokens[l]=="*" or tokens[l]=="-" or tokens[l]=="/" or tokens[l]=="+":
                stack.pop()
                stack.pop()
                stack.append(val)          
                
               
            l+=1
        return stack[-1]
        