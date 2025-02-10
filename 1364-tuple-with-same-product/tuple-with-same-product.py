class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pairs = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pairs[nums[i]*nums[j]] += 1
        
        ans =0
        for i in pairs:
           
            ans += ((pairs[i]-1)*(pairs[i])//2)*8
        return ans


        