class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(0, n + 1):
            total = 0
            for i in range(32):
                if num & (1 << i): 
                    total += 1
            
            res.append(total)
            
        
        return res




        
        
