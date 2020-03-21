class Solution:
    import collections
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        line = collections.deque()
        for row in nums:
            for num in row:
                line.append(num)
        reshape = []
        if len(line) == r*c:
            for y in range(r):
                row = []
                for x in range(c):
                    row.append(line.popleft())
                reshape.append(row)
            return reshape
        else:
            return nums