class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        curr = defaultdict(int)

        for i in range(len(bills)):
            change = bills[i] - 5

            if change == 15:
                if curr[10] >= 1 and curr[5] >= 1:
                    curr[10] -= 1
                    curr[5] -=1
                elif curr[5] >=3 :
                    curr[5] -= 3
                else:
                    return False

            elif change >= 5:
                if curr[5] >=1 :
                    curr[5] -= 1
                else:
                    return False 
            curr[bills[i]] += 1
        return True
                
                
                       