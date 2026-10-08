class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0
            
        start = 0
        maxLen = 1
        seen = {}
        currLen = 1
        seen[s[0]] = 1
        for i in range(1, len(s)):
            if seen.get(s[i]) == None:
                seen[s[i]] = 1
                

            else:
                while seen.get(s[i]):
                    seen[s[start]] = None
                    start += 1
                
                seen[s[i]] = 1
        
            
            currLen = i - start + 1
            if currLen > maxLen:
                maxLen = currLen

        return maxLen
