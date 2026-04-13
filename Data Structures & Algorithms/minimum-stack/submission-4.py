class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) <= 0:
            self.min_stack.append(val)
        else:
            if self.min_stack[len(self.min_stack) - 1] < val:
                temp = self.min_stack[len(self.min_stack) - 1]
                self.min_stack[len(self.min_stack) - 1] = val
                self.min_stack.append(temp)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return min(self.stack)
