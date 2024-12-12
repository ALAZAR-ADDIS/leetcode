class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        n = len(customers)
        count_Y = count_N = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                count_Y += 1

        min_ = count_Y
        idx = 0
        for i in range(n):  
            if min_ > count_N + count_Y:
                min_ = count_N + count_Y
                idx = i
            if customers[i] == 'Y':
                count_Y -= 1
            else:
                count_N += 1 

        if min_ > count_N + count_Y :
            return n         
        return idx
