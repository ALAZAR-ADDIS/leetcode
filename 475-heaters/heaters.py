class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        # def validator(rad):
        #     temp = []
        #     for i in  heaters:
        #         temp.append([i - rad,i + rad])
               
            
        #     ptr =0
        #     for ran in temp:
        #         while ptr < len(houses) and ran[0] <= houses[ptr] <= ran[1] :
        #             ptr += 1
        #     return ptr == len(houses)
        
        # l = 0
        # r = max(*houses,*heaters)

        # while l <= r:
        #     mid = (l + r)//2
        #     if validator(mid):
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return l

        def validator(val):
            l = 0
            r = len(heaters) - 1

            while l <= r:
                mid = (l + r)//2
                if heaters[mid] >= val:
                    r = mid - 1
                else:
                    l = mid + 1
            return l if l < len(heaters) else len(heaters) - 1
        maxx = -float("inf")
        heaters.sort()
        
        for i in range(len(houses)):
            index = validator(houses[i])

            

            if index > 0:
                 maxx = max(maxx, min( abs(houses[i] - heaters[index -1]) , abs(houses[i] - heaters[index]) ))
            else:
                maxx = max(maxx, abs(houses[i] - heaters[index]))
        return maxx
        



        