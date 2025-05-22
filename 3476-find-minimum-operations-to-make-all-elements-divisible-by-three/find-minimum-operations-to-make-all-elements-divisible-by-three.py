class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in  nums:
            div = (i//3)
            if i % 3:
                val = min( abs(div * 3 - i) , abs( ((div + 1)* 3 ) - i ))
                print(val, i)
                ans += val

        return ans
        