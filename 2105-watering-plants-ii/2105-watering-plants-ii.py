class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        lc=capacityA
        rc=capacityB
        left=0
        right=len(plants)-1
        numRf=0
        while right>=left :
            if left!=right:
                if lc<plants[left]:
                     lc=capacityA
                     numRf+=1
                lc-=plants[left]
                left+=1
          
                if rc<plants[right]:
                    rc=capacityB
                    numRf+=1
                rc-=plants[right]
                right-=1
            elif left==right and lc<plants[right]<=rc:
                     rc-=plants[right]
                     right-=1
            else:
                if lc<plants[left]:
                     lc=capacityA
                     numRf+=1
                lc-=plants[left]
                left+=1

        return numRf
