class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if (self.isEmpty()):
            raise OverflowError

        return self.stack.pop()

    def __str__(self) -> str:
        return str(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")

    print("popped : " + stack.pop())
    print("current stack " + str(stack))
    print("popped : " + stack.pop())
    print("current stack " + str(stack))
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
