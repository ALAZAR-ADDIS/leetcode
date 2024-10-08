class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        l,r=0,0
        newlist=[]
        while l<m or r<n:
                if (l<m and r<n and nums1[l]<=nums2[r]) or (r==n ):
                    newlist.append(nums1[l])
                    l+=1

                else:
                    newlist.append(nums2[r])
                    r+=1
        l=n+m
        
        if (l)%2==0:
           mid=int(l/2)
           print(newlist)
           return (newlist[mid]+newlist[mid-1])/2
        else:
            mid=l//2
            return newlist[mid]
        

