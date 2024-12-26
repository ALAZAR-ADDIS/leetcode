class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l=0
        newStr=[]
        for i in range(len(s)):

            if l<len(spaces) and i==spaces[l]:
                newStr.append(" ")
                l+=1
            newStr.append(s[i])
        return "".join(newStr)
            
        