class Queue():
    def __init__(self,size):
        self.queues = []
        self.size = size
        self.head = -1
        self.tail = -1

    def Empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def Full(self):
        if self.tail - self.head +1 == self.size:
            return True
        else:
            return False

    def push(self,content):
        if self.Full():
            print("Quene is Full!")
        else:
            self.queues.append(content)
            self.tail = self.tail + 1
    def out(self):
        if self.Empty():
            print("Quene is Empty!")
        else:
            self.head = self.head + 1
            self.queues.pop(0)

