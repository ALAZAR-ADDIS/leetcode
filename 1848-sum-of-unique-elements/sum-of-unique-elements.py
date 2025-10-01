class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        summ = 0
        for c in count:
            if count[c] == 1:
                summ += c
            
        
        return summ

        