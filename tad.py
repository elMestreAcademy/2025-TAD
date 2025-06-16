class Tad:
    def __init__(self):
        self.buffer = []

    def isEmpty(self):
        return len(self.buffer) == 0

    def push(self, item):
        self.buffer.append(item)

    def pop(self):
        if self.isEmpty():
            raise OverflowError

        return self.buffer.pop()

    def __str__(self) -> str:
        return str(self.buffer)
