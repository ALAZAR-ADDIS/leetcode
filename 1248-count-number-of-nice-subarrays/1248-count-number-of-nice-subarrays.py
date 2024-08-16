class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #counter => to count all the odd numbers in the window
        #left pointer
        #right pointer
        counter=0
        windows=0
        m,l=0,0
        for  r in range(len(nums)):
            if nums[r]%2!=0:
                counter+=1
            while counter>k:
                if nums[l]%2!=0:
                   counter-=1
                l+=1
                m=l
            if counter==k:
                while nums[m]%2==0:
                    m+=1
                windows+=m-l+1
        return windows
