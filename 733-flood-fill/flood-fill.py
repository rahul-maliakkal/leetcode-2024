class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        f = image[sr][sc]

        def helper(r,c):
            if(r>=0 and r<ROWS and c>=0 and c<COLS and image[r][c] == f):
                image[r][c] = color
                helper(r+1,c)
                helper(r-1,c)
                helper(r,c+1)
                helper(r,c-1)

        if(f != color):
            helper(sr,sc)



        return image