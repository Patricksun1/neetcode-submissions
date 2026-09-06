class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        if len(s) % 2 != 0:
            return False 
        for i in s:
            if i == '(' or i == '[' or i == '{':
                result.append(i)
            else:
                if len(result) == 0:
                    return False
                    
                if i == ')' and result.pop() != '(':
                    return False
                elif i == ']' and result.pop() != '[':
                    return False
                elif i == '}' and result.pop() != '{':
                    return False

        if len(result) != 0:
            return False
        
        return True
                