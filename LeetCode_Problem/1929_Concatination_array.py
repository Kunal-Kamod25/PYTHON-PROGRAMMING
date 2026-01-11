class Solution:
    def getConcatenation(self, nums):
        sz = len(nums)
        ans = [0] * (2 * sz)

        for i in range(sz):
            ans[i] = nums[i]
            ans[i + sz] = nums[i]

        return ans
