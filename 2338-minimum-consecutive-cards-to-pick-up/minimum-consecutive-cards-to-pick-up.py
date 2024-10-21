class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count=float("inf")
        freq={}
        l=0
        for  r in range(len(cards)):
            freq[cards[r]]=freq.get(cards[r],0)+1
            while freq[cards[r]]>=2:
                print(r,l)
                count=min(count,r-l+1)
                print(count)
                freq[cards[l]]-=1
                l+=1
        return -1 if count==float("inf") else count
        