class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        list1=[0]*(max(arr1)+1)
        ans=[]
        
        for i in arr1:
            list1[i]+=1
        index=0
        for i in arr2:
            
            j=list1[i]
            while j>0:
                arr1[index]=i
                list1[i]-=1
                index+=1
                j-=1
        

        print(list1)
        for i in range(len(list1)):            
            j=list1[i]                
            while j>0:
                arr1[index]=i
                index+=1
                j-=1
        return arr1
        