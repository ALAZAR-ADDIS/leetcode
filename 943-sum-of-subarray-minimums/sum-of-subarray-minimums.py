class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        total=0
        stack=[]
        for i,n in enumerate(arr):
            while stack and n<stack[-1][1]:
                j,val=stack.pop()
                l=j-stack[-1][0] if stack else j+1
                r=i-j
                total+=(l*r*val)%(10**9+7)
            stack.append([i,n])
        for i in range(len(stack)):
            j,val=stack[i]
            r=len(arr)-j
            l=j-stack[i-1][0] if i>0 else j+1
            total+=(l*r*val)%(10**9+7)
        


        return total%(10**9+7)

        