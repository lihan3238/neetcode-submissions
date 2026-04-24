class MinStack:

    def __init__(self):
        self.stack=[]
        self.length=0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length+=1
        
    def pop(self) -> None:
        self.length-=1
        self.stack.pop()

    def top(self) -> int:
        return self.stack[self.length-1]

    def getMin(self) -> int:
        mini=self.stack[0]
        for i in self.stack:
            mini=min(i,mini)
        return mini
        
        
