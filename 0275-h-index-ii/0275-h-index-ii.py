class Solution:
    def hIndex(self, citations: List[int]) -> int:
        right=len(citations)-1
        left=0
        while right>=left:
            mid=(right+left)//2
            if (len(citations)-(mid))<=citations[mid]:
                right=mid-1
            else:
                left=mid+1
        return (len(citations)-(right+1))