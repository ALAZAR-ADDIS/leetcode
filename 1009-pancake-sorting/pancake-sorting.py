class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        #first find the max in the given range
        #second find reverce the element until that index
        #append the index+1
        #And swintch the element with the last  pointer

        def find_max(end):
            
            i=0
            for j in range(end+1):
                if arr[i]<arr[j]:
                    i=j
            return i
        def rev_arr(end):
            l=0
            r=end
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        
        ans=[]
       
        for i in range(len(arr)-1,0,-1):
            maxInd=find_max(i)
            rev_arr(maxInd)
            rev_arr(i)
            ans.append(maxInd+1)
            ans.append(i+1)
            



        return ans
        
        

        
 
            