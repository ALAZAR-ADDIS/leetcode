class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        list1=[0]*(max(costs)+1)
        for  i in costs:
            list1[i]+=1
        total=0
        count=0
        for i in range(len(list1)):
            j=list1[i]
            while j>0:
                if total+i>coins:
                    return count
                elif total+i==coins:
                    return count+1
               
                
                
                total+=i
                j-=1
                count+=1
        return count
            


        