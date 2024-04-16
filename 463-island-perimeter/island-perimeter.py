class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        # ox
        # xx
        

        def helper(x,y):
            if(x>=0 and x < ROWS and y >=0 and y <COLS):
                if(grid[x][y] == 'x'):
                    return 0
                elif(grid[x][y] == 1):
                    grid[x][y] = 'x'
                    return helper(x-1,y) + helper(x+1,y) + helper(x,y+1) + helper(x,y-1)
                else:
                    return 1
            else:
                return 1

        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1):
                    res = helper(r,c)

        return res

        