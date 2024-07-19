class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count={"T":0,"F":0}
        l=0
        MR=0
        for r in range (len(answerKey)):
            count[answerKey[r]]=count[answerKey[r]]+1

            mine=min(count["T"],count["F"])

            while mine>k:
                count[answerKey[l]]-=1
                l+=1
                mine=min(count["T"],count["F"])
            
            MR=max(MR,r-l+1)
        return MR