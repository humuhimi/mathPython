
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, items):
        self.items.insert(0, items)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    a_queue = Queue()

    for i in range(1, 5):
        a_queue.enqueue(i)

    while a_queue.size():
        print(a_queue.dequeue())

    print()
    print(a_queue.size())