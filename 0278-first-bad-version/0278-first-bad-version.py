# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        
        leftbound=1
        rightbound=n
        firstbad=[]
        while  rightbound>=leftbound:
                mid=(rightbound+leftbound)//2
                if isBadVersion (mid):
                    firstbad=mid
                    rightbound=mid-1
                else:
                    leftbound=mid+1
        return firstbad


                