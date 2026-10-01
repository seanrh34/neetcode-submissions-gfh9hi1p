class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
                nums[0],
                self.helper(nums[1:]), 
                self.helper(nums[:-1])
            )

    def helper(self, nums2):
        if len(nums2) == 0:
            return 0

        if len(nums2) == 1:
            return nums2[0]

        dp = [0] * len(nums2)
        dp[0] = nums2[0]
        dp[1] = max(nums2[0], nums2[1])

        for i in range(2, len(nums2)):
            dp[i] = max(dp[i-1], nums2[i] + dp[i-2])

        return dp[len(nums2)-1]