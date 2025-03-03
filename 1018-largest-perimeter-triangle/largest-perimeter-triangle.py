class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        print(nums)

        a = 0
        b = 1
        c = 2

        while  c < len(nums):
            print(nums[c] , nums[b] + nums[a])
            if nums[a] < nums[b] + nums[c]:
                return (nums[c] + nums[b] + nums[a])
            a += 1
            b += 1
            c += 1



        return 0        