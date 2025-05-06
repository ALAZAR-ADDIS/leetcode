class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        val = Counter(s)
        for char in t:
            if not val[char] :
                return char
            else:
                val[char]-=1
            
        