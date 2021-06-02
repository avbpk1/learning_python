class Stack:
    def __init__(self, stack_len = 2):
        self.data = []
        self.max_len = stack_len


    @property
    def length(self):
        return len(self.data)

    def push(self,value):
        self.data.append(value)
        if s.length > s.max_len:
            print(f"Stack Full! A Max of {s.max_len} can be accepted")

    def pop(self):
        try:
            return self.data.pop()
        except Exception as ex:
            print("Stack Empty Error: " , ex)

# Testing
s = Stack(stack_len=2)
#Stack full error
s.push(10)
s.push(20)
s.push(30)
#stack empty error
s.pop()
s.pop()
s.pop()
s.pop()
