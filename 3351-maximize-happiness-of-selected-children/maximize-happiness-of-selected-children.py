class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse = True)
        i = 0
        ans = 0
        
        for j in range(len(happiness)):
            if happiness[j] > i:
                ans += happiness[j] - i
      
            if j == k-1:
                return ans
            i += 1
        