class MinStack:

    def __init__(self):
        self.arr = []
        self.prefix = []
        
        

    def push(self, val: int) -> None:
            
        if len(self.prefix) == 0 or val <= self.prefix[-1]:
            self.prefix.append(val)
        else:
            self.prefix.append(self.prefix[-1])

        self.arr.append(val)

    def pop(self) -> None:
        
        val = self.arr.pop()
        self.prefix.pop()
            

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        
        return self.prefix[-1]
