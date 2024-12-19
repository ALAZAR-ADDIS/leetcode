class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Dict={n:i for i,n in enumerate(nums1)}
        print(num1Dict)
        stack=[]
        ans=[-1]*len(nums1)

        for num in nums2:
            while stack and stack[-1]<num:
                val=stack.pop()
                if val in num1Dict:
                    ans[num1Dict[val]]=num
            stack.append(num)
        return ans


                 

        
