class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict={}
        for i,n in enumerate(s):
            dict[n]=i
        ans =[]
        end=0
        size=0
        for i,n in enumerate(s):
            size+=1
            end=max(end,dict[n])
            if end==i:
                ans.append(size)
                size=0
        return ans

        