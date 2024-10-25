class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prev=None
        l=0
        r=1
       
        maximum=1

        while r<len(arr):           
            if prev!=None and prev==(arr[r-1]>arr[r]):              
                while l<r-1:
                    l+=1
            while  r<len(arr) and arr[r-1]==arr[r]:
                l=r
                r+=1
                
                
            
            if r <len(arr):
                prev=arr[r-1]>arr[r]            
                maximum=max(maximum,r-l+1)
            r+=1
        return maximum
            

        