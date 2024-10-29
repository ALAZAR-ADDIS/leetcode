class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # l=0
        # r=c
        # mid=0
        # while l<=r:
        #     mid=(l+r)//2
        #     sqr=mid**2
        #     if sqr==c:
        #         break
        #     elif sqr>c:
        #         r=mid-1
        #     else:
        #         l=mid+1

        # l=0
        # r=mid
        # while l<=r:
        #     res=l**2 +r**2
        #     if res==c:
        #         return True
        #     elif res>c:
        #         r-=1
        #     else:
        #         l+=1
        # return False

        l,r=0,int(sqrt(c))
        while l<=r:
            total=l**2 + r**2
            if total==c:
                return True
            elif total>c:
                r-=1              
                
            else:
                l+=1
        return False

        
        