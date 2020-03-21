class Solution:
    import collections
    def numIslands(self, grid: List[List[str]]) -> int:
        # 동 서 남 북
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]  
        ans = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == "1":
                    ans += 1
                    grid[j][i] = "0"
                    deque = collections.deque([(i, j)])
                    while deque:
                        x, y = deque.popleft()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == "1":
                                grid[ny][nx] = "0"
                                deque.append((nx, ny))
        return ans