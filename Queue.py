class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.heigth = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.heigth += 1

    def dequeue(self):
        if self.heigth == 0:
            return None
        temp = self.first
        if self.heigth == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.heigth -= 1
        return temp

queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.dequeue()

queue.print_queue()