class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area  = 0
        area = 0

        def helper(x,y):
            if(x>=0 and x<ROWS and y>=0 and y<COLS and grid[x][y] == 1):
                grid[x][y] = 'x'
                return 1+helper(x+1,y)+helper(x-1,y)+helper(x,y+1)+helper(x,y-1)
            else:
                return 0    

        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 1):
                    area = helper(r,c)
                max_area = max(max_area, area)    
        
        return max_area