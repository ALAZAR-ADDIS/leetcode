class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        size=len(citations)
        left=0
        right=len(citations)-1
        while(right>=left):
            mid=(right+left)//2
            if (size-mid)<=citations[mid]:
                right=mid-1
            else:
                left=mid+1
        return size-(right+1)