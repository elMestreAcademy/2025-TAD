from tad import Tad


class Stack(Tad):
    pass


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
    try:
        print(stack.pop())  # <--
    except OverflowError:
        print("ERROR No podemos seguir popeando, el stack está vacío")
