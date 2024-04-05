class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-(len(needle)-1)):
            length=len(needle)
            if haystack[i:i+length]==needle:
                return i
        return -1