class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        ans = 0

        for c in charSet:
            count = 0
            start = 0
            replacementsNeeded = 0
            for i in range(len(s)):
                if s[i] == c:
                    count += 1
                
                while i - start + 1 - count > k:
                    if s[start] == c:
                        count -= 1
                
                    start += 1
                
                if (i - start + 1) > ans:
                    ans = i - start + 1
            
        return ans