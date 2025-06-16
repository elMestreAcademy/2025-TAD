from tad import Tad


class Queue(Tad):
    def enqueue(self, item):
        super().push(item)

    def dequeue(self):
        if self.isEmpty():
            raise OverflowError

        return self.buffer.pop(0)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(q)

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    try:
        print(q.dequeue())
    except OverflowError:
        print("ERROR No podemos seguir desencolando, la cola está vacía")
        print("Y AHORA vamos a provocar el error adrede")
    q.dequeue()
    print(q)
