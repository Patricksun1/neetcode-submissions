class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
            
        image[sr][sc] = color

        numCols = len(image[0])
        numRows = len(image)

        if sc + 1 < numCols and image[sr][sc + 1] == original:
            self.floodFill(image, sr, sc + 1, color)
        if sr + 1 < numRows and image[sr + 1][sc] == original:
            self.floodFill(image, sr + 1, sc, color)
        if sc - 1 >= 0 and image[sr][sc - 1] == original:
            self.floodFill(image, sr, sc - 1, color)
        if sr - 1 >= 0 and image[sr - 1][sc] == original:
            self.floodFill(image, sr - 1, sc, color)

        return image

        