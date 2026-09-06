class MyStack:

    def __init__(self):
        self.stack = deque()


    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        buffer = deque()
        for i in range(0, len(self.stack) - 1):
            val = self.stack.popleft()
            buffer.append(val)

        retval = self.stack.popleft()
        self.stack = buffer

        return retval


    def top(self) -> int:
        buffer = deque()
        for i in range(0, len(self.stack) - 1):
            val = self.stack.popleft()
            buffer.append(val)

        val = self.stack.popleft()
        buffer.append(val)

        self.stack = buffer
        
        return val

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()