"""Simple data structure: Stack, Queue, Heap"""


class SimpleStructure:
    def is_empty(self):
        """Examination empty stack"""
        if self.size == 0:
            return 1
        else:
            return 0

    def push(self, value):
        """Add element in stack"""
        if len(self.lst) < self.max_size:
            self.lst.append(value)
            self.size += 1
        else:
            self.massiv.append(value)


class Stack(SimpleStructure):

    def __init__(self, max_size):
        self.lst = []
        self.size = 0
        self.max_size = max_size
        self.massiv = []

    def pop(self):
        """Pick up the element"""
        if not self.is_empty():
            self.size -= 1
            remove = self.lst.pop()
            while self.size <= self.max_size and len(self.massiv) != 0:
                self.push(self.massiv.pop(0))
            return remove
        else:
            return None


class Queue(SimpleStructure):

    def __init__(self, max_size):
        self.lst = []
        self.size = 0
        self.max_size = max_size
        self.massiv = []

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            remove = self.lst.pop(0)
            while self.size <= self.max_size and len(self.massiv) != 0:
                self.push(self.massiv.pop(0))
            return remove
        else:
            return None


class MaxHeap:

    def __init__(self, heap_size):
        self.lst = []
        self.size = 0
        self.heap_size = heap_size

    def parent(self, i):
        return self.lst[i / 2]

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

