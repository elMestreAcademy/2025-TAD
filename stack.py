def create_stack():
    stack = []
    return stack


def isEmpty(stack):

    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed : " + item)


def pop(stack):
    if (isEmpty(stack)):
        return "UNDERFLOW"

    return stack.pop()


stack = create_stack()
push(stack, str("A"))
push(stack, str("B"))
push(stack, str("C"))
push(stack, str("D"))

print("popped : " + pop(stack))
print("current stack " + str(stack))
print("popped : " + pop(stack))
print("current stack " + str(stack))