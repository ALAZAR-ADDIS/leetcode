class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def validate(distance):
            l = 0
            count = 0
            for i in range(1,len(position)):
                if position[i]  - position[l] >= distance:
                    count += 1
                    l = i
          
            return count >= m-1
        l = 1
        r = max(position)
        position.sort()
        
        while  l <= r:
            mid = (l + r)//2
            print(mid,validate(mid),l,r)

            if validate(mid):
                l = mid + 1                
            else:
                r = mid - 1
        return r
                
        