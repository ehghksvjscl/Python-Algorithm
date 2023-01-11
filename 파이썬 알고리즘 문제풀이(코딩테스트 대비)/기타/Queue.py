# Stack 2개를 이용하여 Queue의 enqueue와 dequeue를 구현하시오


class Queue(object):
    def __init__(self) -> None:
        self.__inStack = []
        self.__outStack = []

    def enqueue(self, obj):
        self.__inStack.append(obj)
        print(self.__inStack)

    def dequeue(self):
        if not self.__outStack:
            while self.__inStack:
                self.__outStack.append(self.__inStack.pop())

        print(self.__outStack)
        return self.__outStack.pop()

queue1 = Queue()

queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)

queue1.dequeue()
queue1.dequeue()
queue1.dequeue()
queue1.dequeue()