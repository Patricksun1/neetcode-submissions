class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = defaultdict(list)
        for s in strs:
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c) - ord("a")] += 1
            
            dic[tuple(alphabet)].append(s)
        
        for val in dic.values():
            res.append(val)
    
        return res
        

                
            
      