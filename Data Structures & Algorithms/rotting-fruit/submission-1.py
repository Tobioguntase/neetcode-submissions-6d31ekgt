class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        rotten = 0
        count = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten += 1
                    count += 1
                    q.append((r,c))
                if grid[r][c] == 1:
                    count += 1

        while rotten != count and q:
            n = len(q)
            for i in range(n):
                (r,c) = q.popleft()
                
                nbrs = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]
                
                for i,j in nbrs:
                    if (i in range(len(grid))
                        and j in range(len(grid[0]))
                        and grid[i][j] == 1
                    ):
                        grid[i][j] = 2
                        q.append((i,j))
                        rotten += 1
            time += 1
        if rotten == count:
            return time
        else: 
            return -1  










        