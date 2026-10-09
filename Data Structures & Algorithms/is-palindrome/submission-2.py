class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        pattern = r"^[a-zA-Z0-9]+$"

        while l < r:
            if s[l] == " " or not re.match(pattern, s[l]):
                l += 1
                continue
                
            if s[r] == " " or not re.match(pattern,s[r]):
                r -= 1
                continue

            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        

        return True