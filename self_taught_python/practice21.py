class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return last

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    for c in "Hello":
        stack.push(c)

    reverse = ""

    while stack.size():
        reverse += stack.pop()

    print(reverse)
