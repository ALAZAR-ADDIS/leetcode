class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxx = deque()
        minn = deque()
        l = 0
        ans = -float("inf")

        for r in range(len(nums)):

            while maxx and maxx[ - 1] < nums[r]:
                maxx.pop()
            maxx.append(nums[r])

            while minn and minn[-1] > nums[r]:
                minn.pop()
            minn.append(nums[r])
            
            while maxx[0] - minn[0] > limit:
                if maxx and nums[l] == maxx[0]:
                    maxx.popleft()
                elif minn and nums[l] == minn[0]:
                    minn.popleft()
                l += 1
            

            ans = max(ans, r - l + 1)
        return  ans
        