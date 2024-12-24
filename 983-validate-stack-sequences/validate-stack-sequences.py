class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        l=0
        r=0
        while r<len(popped):
            while (l<len(pushed))  and (not stack or stack[-1]!=popped[r]):
                
                stack.append(pushed[l])
                l+=1
                if stack[-1]==popped[r]:break
                
            print(stack[-1],popped[r])
            if stack[-1]==popped[r]:
                stack.pop()
            else:
                return False
            r+=1
        return True
        

        