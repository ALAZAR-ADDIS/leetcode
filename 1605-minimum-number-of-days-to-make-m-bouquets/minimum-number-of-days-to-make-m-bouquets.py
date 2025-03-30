class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:


        def validator(day):
            i = 0
            common = 0            

            while i < len(bloomDay):
                j = i
                while j < i + k and j < len(bloomDay):
                    if bloomDay[j] > day:
                        i = j 
                        break
                    j += 1
                else:
                    print(day,j - i + 1, "this is i")
                    if j  == i + k:
                        common += 1
                    i += k -1
                i += 1
          
            return common >= m


        if m* k >len(bloomDay):
                return -1
        
        l = 0
        r = max(bloomDay)

        while l + 1 < r:
            mid = ( l + r)//2

            if validator(mid):
                r = mid
            else:
                l = mid
        return r
                
                
                
                
                

            
        