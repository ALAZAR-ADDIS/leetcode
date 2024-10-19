class Solution:
    def minimizedStringLength(self, s: str) -> int:
        dict={}
        for i in s:
             dict[i]=dict.get(i,0)+1
        return len(dict)
        