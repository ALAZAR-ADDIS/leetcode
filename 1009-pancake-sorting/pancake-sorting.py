class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """
        fist find the index of  the  max num withe the sliced range of the array
        the reverce it throuh the index of the larger element 
        largest index   + 1 
        and again reverce the hole till the limited index
        limit index  +1 


        
        """
        ans = []

        for i  in range(len(arr)):
            max_index = 0
            for j in range(len(arr)-i):
                if arr[max_index]< arr[j]:                   
                    max_index = j
           
            
            self.swap(arr,max_index)
            self.swap(arr,len(arr)-i-1)
            ans.append(max_index + 1)
            ans.append(len(arr)- i)
    
      
        return ans
        
    def swap(self, arr, end):
        
        l = 0
        r = end
        while l < r:
            arr[l], arr[r] = arr[r] , arr[l]            
            l += 1
            r -=1
        