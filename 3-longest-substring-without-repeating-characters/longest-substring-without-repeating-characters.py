class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        l=0
        max_l = 0

        for r in range(len(s)):

            while s[r] in char:
                char.remove(s[l])
                l += 1

            char.add(s[r])
            max_l  = max(max_l,r - l + 1)
        

        return max_l
      
        