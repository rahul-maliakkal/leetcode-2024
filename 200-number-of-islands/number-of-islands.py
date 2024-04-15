class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def helper(x,y):
            if(x>=0 and x <ROWS and y>=0 and y < COLS and grid[x][y] == '1'):
                grid[x][y] = 'x'
                helper(x+1,y)
                helper(x-1,y)
                helper(x,y+1)
                helper(x,y-1)
                return 1
            return 0


        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == '1'):
                    res += helper(i,j)
        
        return res