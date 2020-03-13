class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0, 1]
        for _ in range(n):
            ans.append(ans[-1]+ans[-2])
        return ans[-1]