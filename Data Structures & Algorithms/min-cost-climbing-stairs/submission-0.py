class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return cost[0]

        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = min(cost[0], cost[1])

        for i in range(3, len(cost) + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        return dp[len(cost)]