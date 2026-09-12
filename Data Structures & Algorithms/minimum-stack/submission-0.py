class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            minimum = val
        else:
            minimum = self.mins[-1]
            if val <= minimum:
                minimum = val
        self.mins.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

        
