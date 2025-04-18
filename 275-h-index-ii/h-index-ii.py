class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        l = -1
        r = len(citations)
        while l + 1 < r:
            mid = (l + r)//2
            if citations[mid] >= len(citations) - mid:
                r = mid
            else:
                l = mid
        return len(citations) - r