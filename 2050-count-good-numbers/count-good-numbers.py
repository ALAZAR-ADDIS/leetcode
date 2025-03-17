class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def helper(num,val,total = 0):
            total += 1
            if num == 0:
                print(total)
                return 1
            print("hello")
            
            if num % 2:
                return ((val)% (10**9 + 7) * helper(num - 1,val,total)) % (10**9 + 7)

            else:
                val = (val * val) % (10** 9 + 7)
                return (helper(num//2,val,total )) % (10**9 + 7)
            

      

        if (n-1) % 2:
            even = ((n-1)//2) + 1
            odd = ((n-1)//2) + 1

            return (helper(even , 5) * helper(odd, 4))% (10**9 + 7)
            

        else: 
            even = ((n-1)//2) + 1
            odd = ((n-1)//2)


            return (helper(even , 5) * helper(odd, 4))% (10**9 + 7) 
    
        
        