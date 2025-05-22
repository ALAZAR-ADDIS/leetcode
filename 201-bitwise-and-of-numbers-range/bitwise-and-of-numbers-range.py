class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # p = 0
        # ans = 0
        # l = left
        # for i in range(32):
        #     val = l & 1 
        #     if val and  right - left < 2 ** p:
        #         ans += 2 ** p                

        #     l >>= 1  
        #     p += 1
        # return ans

        # i = 0
        # while i < 32:
        #     if left == right:
        #         return left << (i)
        #     else:
        #         left >>= 1
        #         right >>= 1
        #     i += 1
        # return 0

        i = 0
        while left != right:

            i += 1
            left  >>= 1
            right >>= 1

        return left<<i
        
        
