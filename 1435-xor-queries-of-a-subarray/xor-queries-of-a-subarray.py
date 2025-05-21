class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # ans = []
        
        # for x,y in queries:
        #     temp = 0
        #     for i in range(x,y + 1):
        #         temp ^= arr[i]
        #     ans.append(temp)

        # return ans

        temp = [0] * (len(arr) + 1)
        ans = []
       

        for i in range(1,len(temp)):
            temp[i] = temp[i - 1] ^ arr[i -1]
        
       
        
        for x,y in queries:
            val =  temp[x] ^ temp[y + 1] 
            ans.append(val)
        
        return ans

        