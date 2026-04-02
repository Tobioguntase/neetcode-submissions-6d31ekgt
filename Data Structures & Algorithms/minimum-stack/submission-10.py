class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            if val > self.minStack[-1]:   
                self.minStack.append(self.minStack[-1])
            else: 
                self.minStack.append(val)
    
        #print(f" min stack:  {self.minStack}")
        #print(f"main stack:  {self.stack}")
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        #print(self.minStack)
        return self.minStack[-1]
    
        
