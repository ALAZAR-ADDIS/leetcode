class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            ispop=False
            if s[i].lower() == s[i + 1].lower():
                if s[i] != s[i + 1]:
                    s=s[:i]+s[i+2:]
                    ispop=True
            i += 1
            if ispop:
                i=0
        return s
        