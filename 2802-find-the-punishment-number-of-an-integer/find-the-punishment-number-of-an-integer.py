class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def solve(num,total,i,tar):
            if len(num)== i:                
                if total == tar:
                    return True
                return False
            val = 0

            for j in range(i,len(num)):

                val = val * 10 + int(num[j]) 
                ans = solve(num,val + total,j + 1,tar)

                if ans :
                    return True
      

        ans = 0
        for i in range(1, n+ 1):
            # print(i)
            # print( solve(str(i * i),0 ,0))
            if solve(str(i * i),0 ,0,i):
                ans += i * i
        return ans

            
            

        