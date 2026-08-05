class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        start_color = image[sr][sc]

        if start_color == color:
            return image
        
        stack = [(sr, sc)]
        image[sr][sc] = color

        while stack:
            r, c = stack.pop()
            

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0  <= nc < cols and image[nr][nc] == start_color:
                    image[nr][nc] = color
                    stack.append((nr, nc))
        return image

        