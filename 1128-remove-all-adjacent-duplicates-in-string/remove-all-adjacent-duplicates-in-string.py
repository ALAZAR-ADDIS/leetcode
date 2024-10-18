class Solution:
    def removeDuplicates(self, s: str) -> str:
       stack=[]
       for i in s:
            noDup=True
            while stack and stack[-1]==i:
                stack.pop()
                noDup=False
        
            if noDup:
              stack.append(i)
       return "".join(stack)
        