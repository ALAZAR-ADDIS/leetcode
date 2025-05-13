class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]

        for i in range(1,len(pref)):
            x = pref[i] ^ pref[i- 1]
            ans.append(x)
        return ans
        