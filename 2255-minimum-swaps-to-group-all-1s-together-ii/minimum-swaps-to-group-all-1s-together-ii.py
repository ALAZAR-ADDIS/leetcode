class Solution:
    def minSwaps(self, arr: List[int]) -> int:

        binaryFreq=defaultdict(int)
        Ones=0
        for i in arr:
            if i==1:
              Ones+=1

        l=0
        minswap=float("inf")
        for r in range(len(arr)+Ones-1):
        
            binaryFreq[arr[r%len(arr)]]+=1
           
           
            while sum(binaryFreq.values())>Ones:
                    binaryFreq[arr[l]]-=1
                    l+=1
             

           
            if  sum(binaryFreq.values())==Ones:
                minswap=min(minswap,binaryFreq[0])

        return minswap if minswap!=float("inf") else 0




        