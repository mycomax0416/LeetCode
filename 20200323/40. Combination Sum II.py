class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = [[]]
        for candidate in candidates:
            for idx in range(len(arr)):
                test = arr[idx][:]
                test.append(candidate)
                if sum(test) == target and sorted(test) not in ans:
                    ans.append(sorted(test))
                elif sum(test) < target:
                    arr.append(test)
        return ans