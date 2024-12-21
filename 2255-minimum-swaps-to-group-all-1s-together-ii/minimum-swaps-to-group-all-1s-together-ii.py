class Solution:
    def minSwaps(self, arr: List[int]) -> int:

        f=defaultdict(int)
        Ones=0
        for i in arr:
            if i==1:
              Ones+=1

        l=0
        minswap=float("inf")
        for r in range(len(arr)+Ones-1):
        
            f[arr[r%len(arr)]]+=1
           
           
            while sum(f.values())>Ones:
                    f[arr[l]]-=1
                    l+=1
             

           
            if  sum(f.values())==Ones:
                minswap=min(minswap,f[0])

        return minswap if minswap!=float("inf") else 0




        