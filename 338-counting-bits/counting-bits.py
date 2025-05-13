class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = []
        # for i in range(n+1):
        #     count = Counter(str(bin(i)[2:]))
            
        #     ans.append(count["1"])
        # return ans

        ans = []
        for num in range(n+ 1):
            count = 0
            while num > 0:
                if num & 1 == 1:
                    count += 1
                num >>= 1
            ans.append(count)
        return ans
        