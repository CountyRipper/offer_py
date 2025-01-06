class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        curr = 0
        for i in range(2, len(cost) + 1):
            next = min(cost[i - 1] + curr, cost[i - 2] + prev)
            prev = curr
            curr = next
        return curr
