class Solution:
    from collections import Counter
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_cnt = max(cnt.values())
        min_len = 50001
        for key, val in cnt.items():
            if val == max_cnt:
                min_len = min(min_len, len(nums)-nums.index(key)-nums[::-1].index(key))     
        return min_len