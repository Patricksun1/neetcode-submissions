class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        

        for i in range(numRows):
            currRow = [1] * (i + 1)
            for j in range(1, i):
                currRow[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(currRow)

        
        return res
