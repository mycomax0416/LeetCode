class Solution:
    import collections
    def regionsBySlashes(self, grid: List[str]) -> int:    
        N = len(grid)
        arr = [[0 for _ in range(N*3)] for _ in range(N*3)]
        for y in range(N):
            for x in range(N):
                if grid[y][x] == '/':
                    for n in range(3):
                        arr[3*y+n][3*x+2-n] = 1
                elif grid[y][x] == '\\':
                    for n in range(3):
                        arr[3*y+n][3*x+n] = 1         
        ans = 0
        # 동 서 남 북
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for j in range(N*3):
            for i in range(N*3):
                if arr[j][i] == 0:
                    ans += 1
                    arr[j][i] = 1
                    deque = collections.deque([(i, j)])
                    while deque:
                        x, y = deque.popleft()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx < N*3 and 0 <= ny < N*3 and arr[ny][nx] == 0:
                                arr[ny][nx] = 1
                                deque.append((nx, ny))
        return ans