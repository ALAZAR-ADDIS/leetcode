class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        check=[0]*(1000+1)
        for i in trips:
            check[i[1]]+=i[0]
            check[i[2]]-=i[0]
        for i  in range(1,len(check)):
            check[i]=check[i]+check[i-1]
        for i in range(len(check)):
            if check[i]>capacity:
                return    False
        return True
        