# Queue2개를 가지고 Stackd의 push와 pop을 구현해 보세요.

import queue

class Stack(object):
    def __init__(self) -> None:
        self.__q1 = queue.Queue()
        self.__q2 = queue.Queue()

    def push(self, obj):
        self.__q1.put(obj)
        print(self.__q1.queue)

    def pop(self):
        while self.__q1.qsize() > 1:
            self.__q2.put(self.__q1.get())

        temp = self.__q1
        self.__q1 = self.__q2
        self.__q2 = temp

        print(self.__q1.queue)
        return self.__q2.get()

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)

stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()