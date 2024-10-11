class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1 for i in range(len(nums1))]
        HT={n:i for i,n in enumerate(nums1)}
        print(HT)
        stack=[]

        for i in nums2:
                               
                    while stack and stack[-1]<i:
                        index=HT[stack[-1]]
                        ans[index]=i
                        stack.pop()
                    if i in nums1: 
                       stack.append(i)
        return ans