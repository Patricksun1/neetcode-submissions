class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        
        if len(s) != len(t):
            return False

        for char in s:
            if char in chars:
                chars[char] += 1
            
            else:
                chars[char] = 1
        

        for char in t:
            if char not in chars:
                return False
            
            else:
                chars[char] -= 1
                if chars[char] < 0:
                    return False

        return True
        
