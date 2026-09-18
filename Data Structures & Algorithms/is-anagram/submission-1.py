class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        if len(s) != len(t):
            return False
            
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        

        for c in t:
            if c in chars:
                chars[c] -= 1
                if chars.get(c) < 0:
                    return False
            else:
                return False

            
            
        return True