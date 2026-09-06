class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        prev = 0
        prevprev = 0
        sum = 0
        k = 0
        for i in range(len(operations)):
            if operations[i] == '+':
                prev = int(result[k - 1])
                prevprev = int(result[k - 2])
                result.append(prev + prevprev)
                k += 1

            elif operations[i] == 'D':
                prev = int(result[k - 1])
                result.append(prev * 2) 
                k += 1
            elif operations[i] == 'C':
                result.pop()
                k -= 1
            else:
                result.append(operations[i])
                k += 1 

        for j in range(len(result)):
            sum += int(result.pop())

        return sum