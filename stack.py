class Stack():
    def __init__(self,size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self,content):
        if self.Full():
            print ("stack is Full!")
        else:
            self.stack.append(content)
            self.top = self.top+1


    def out(self):
        if self.Empty():
            print("stack is Empty!")
        else:
            self.top =self.top - 1
            self.stack.pop()


    def Full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def Empty(self):
        if self.top == -1:
            print ("stack is Empty!")


