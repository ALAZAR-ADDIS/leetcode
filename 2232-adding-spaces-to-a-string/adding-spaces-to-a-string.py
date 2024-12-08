class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l=0
        newStr=""
        for i in range(len(s)):

            if l<len(spaces) and i==spaces[l]:
                newStr+=" "
                l+=1
            newStr+=s[i]
        return newStr
            
        