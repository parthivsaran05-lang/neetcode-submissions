class MinStack:
    def __init__(self):
        self.MinStack=[]
        self.out=[]

    def push(self, val: int) -> None:
        self.out.append(val)
        if not self.MinStack or val <= self.MinStack[-1]:
            self.MinStack.append(val)
    def pop(self) -> None:
        val=self.out.pop()
        if val==self.MinStack[-1]:
            self.MinStack.pop()

    def top(self) -> int:
        return self.out[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]