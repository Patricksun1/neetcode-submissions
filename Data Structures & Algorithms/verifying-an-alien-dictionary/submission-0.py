class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        seen = dict()
        index = 0
        for c in order:
            seen[c] = index
            index += 1


        for i in range(0, len(words) - 1):
            currWord = words[i]
            nextWord = words[i + 1]
            
            currChar = 0
            sameLengthFlag = 0
            for c in currWord:
                if currChar >= len(nextWord):
                    sameLengthFlag = 1
                    break
                if c == nextWord[currChar]:
                    currChar += 1
                    continue
                if seen[c] > seen[nextWord[currChar]]:
                    return False
                elif seen[c] < seen[nextWord[currChar]]:
                    break

                currChar += 1

            if sameLengthFlag == 1:
                return False

        return True