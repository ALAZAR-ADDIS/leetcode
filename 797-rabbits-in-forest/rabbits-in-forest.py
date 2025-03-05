class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        rab_ans = defaultdict(int)
        total = 0
        for  i in range(len(answers)):
            rab_ans[answers[i]] += 1
        print(rab_ans)
        
        for key,val in rab_ans.items():
            if val > (key + 1):
                if key:
                    total += (val // (key + 1)) * (key + 1)
                    total += (key + 1) if val % (key + 1) else 0
                else:
                    total += val
            else:

                 total += (key + 1)
        return total
        
        