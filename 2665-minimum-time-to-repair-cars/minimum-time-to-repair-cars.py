class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def validator(time):
            car = 0
            for i in range(len(ranks)):
                car += int(sqrt(time/ranks[i]))
            return car
        
        l = 1
        r = ranks[0] * cars* cars
        

        while l <= r:
            mid = (l + r)//2

            if validator(mid) >= cars:
                r = mid - 1
            else:

                l = mid + 1
        return l