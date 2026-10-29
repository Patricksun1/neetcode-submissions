class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "~"
        buffer = ""
        for s in strs:
            buffer += s
            buffer += "\n"

        buffer = buffer[:-1]
        return buffer

    def decode(self, s: str) -> List[str]:
        if s == "~":
            return []
        res = []
        index = 0
        start = 0
        while True:
            prevIndex = index
            index = s.find("\n")
            if index == -1:
                message = s[start:]
                res.append(message)
                break
            
            message = s[start:index]
            res.append(message)
            s = s[index + 1:]
            

        return res
