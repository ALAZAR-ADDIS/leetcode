class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = defaultdict(int)
        ans = [-1] * len(nums1)
        stack = []

        for i in range(len(nums1)):
            index[nums1[i]] = i
        
        for i,val in enumerate(nums2):

            while stack and stack[-1] < val:
                poped = stack.pop()

                if poped in  index:
                    ans[index[poped]] = val

            stack.append(val)
        
        return ans


        