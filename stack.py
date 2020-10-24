class NotEnoughElements(Exception):
    pass


class EmptyStackError(Exception):
    pass


class Stack:
    def __init__(self):
        self._data = []

    @property
    def size(self):
        return len(self._data)

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if not self._data:
            raise EmptyStackError
        return self._data.pop()

    def multi_pop(self, n):
        if len(self._data) < n:
            raise NotEnoughElements
        return [self.pop() for _ in range(n)]

    def peek(self):
        return self._data[-1]

    def clear(self):
        self._data.clear()