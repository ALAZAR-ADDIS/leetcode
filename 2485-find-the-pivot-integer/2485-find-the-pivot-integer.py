class Solution:
    def pivotInteger(self, n: int) -> int:
        list1=[]
        if n==1:
            return n
        else:
            for i in range(1,n+1):
                list1.append(i)
            for i in range(1,len(list1)):
                list1[i]=list1[i]+list1[i-1]
            for i in range(len(list1)-1):
                if list1[i]==(list1[len(list1)-1]-list1[i+1]):
                    return i+2
        return -1


        
    
        