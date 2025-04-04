class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def validator(mid):
            count = 0
            for num in quantities:
                count += num//mid + ( 1 if num % mid else 0)
            return count <= n
        l = 0
        r = max(quantities) + 1

        while l + 1 < r:
            mid = ( l + r)//2

            if validator(mid):
                r = mid
            else:
                l = mid
        return r



        