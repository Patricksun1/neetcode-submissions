class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        for j in range(0, len(sandwiches)):
            successFlag = 0
            for i in range(0, len(students)) :
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                    successFlag = 1
                    break
                else:
                    val = students.pop(0)
                    students.append(val)
            
            if successFlag == 0:
                return len(students)
        
        return 0
        