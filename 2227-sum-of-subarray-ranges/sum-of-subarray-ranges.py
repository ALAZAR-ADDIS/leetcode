class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sumMin=0
        sumMax=0
        stack=[]
        for i,n in enumerate(nums):
            while stack and stack[-1][1]>n:
                j,val=stack.pop()
                l=j-stack[-1][0] if stack else j+1
                r=i-j
                sumMin+=(val)*l*r


            stack.append([i,n])

        for i in range(len(stack)):
                j,val=stack[i]
                l=j-stack[i-1][0] if i>0 else j+1
                r=len(nums)-j
                sumMin+=(val)*l*r
        stack.clear()
        for i,n in enumerate(nums):
            while stack and stack[-1][1]<n:
                j,val=stack.pop()
                l=j-stack[-1][0] if stack else j+1
                 
                r=i-j
                sumMax+=(val)*l*r
            stack.append([i,n])

        for i in range(len(stack)):
                j,val=stack[i]
                l=j-stack[i-1][0] if i>0 else j+1
                r=len(nums)-j
                print(r,l)
                sumMax+=(val)*l*r
        print(sumMax,sumMin)
            




        return sumMax-sumMin

