class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(path,added:set):
            if len(path) == len(nums):
                ans.append(path[::])
                return
            

            for i in range(len(nums)):

                if nums[i] not in added:
                    path.append(nums[i])
                    added.add(nums[i])

                    helper(path, added)

                    path.pop()
                    added.remove(nums[i])

        ans = []
        helper([],set())
        return ans