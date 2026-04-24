class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        self.length=0

    def push(self, val: int) -> None:
        if self.stack==[]:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1]))
        self.stack.append(val)
        self.length+=1
        
    def pop(self) -> None:
        self.length-=1
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[self.length-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
        
