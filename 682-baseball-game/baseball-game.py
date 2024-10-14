class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i.upper()=="+" :
               stack.append(stack[-1]+stack[-2])
            elif i.upper()=="C":
                stack.pop()
            elif i.upper()=="D":
                stack.append(stack[-1]*2)
            else:
                 stack.append(int(i))
        return sum(stack)
        