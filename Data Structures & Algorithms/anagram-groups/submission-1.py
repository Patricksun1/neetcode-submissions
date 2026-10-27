class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        strDict = defaultdict(list)

        for s in strs:
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c) - ord('a')] += 1
            
            strDict[tuple(alphabet)].append(s)

        for key in strDict.values():
            res.append(key)

        return res



            


                
            
      