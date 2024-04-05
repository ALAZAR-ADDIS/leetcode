class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length=200
        for words in strs:
            min_length=min(min_length,len(words))

        sameprefix=""
        states_flag=True
        for i in range(min_length):
            letter=strs[0][i]
            for j in range(len(strs)):
                if letter!=strs[j][i]:
                    states_flag=False
            if not states_flag:
                break
            sameprefix+=strs[0][i]

        return sameprefix
            
                



