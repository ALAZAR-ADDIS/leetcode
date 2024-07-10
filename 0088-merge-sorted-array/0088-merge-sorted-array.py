class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return nums1
        else:
            left=0
            right=0
            temp=[]
            while left<m or right<n:
                if right==n or (nums1[left]<=nums2[right] and left<m):
                    temp.append(nums1[left])
                    left+=1
                else:
                    temp.append(nums2[right])
                    right+=1
            
            for i in range(len(temp)):
                nums1[i]=temp[i]

        