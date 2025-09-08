class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for i in ransomNote:
            count[i] -= 1
            if count[i] < 0:
                return False
        return True
        