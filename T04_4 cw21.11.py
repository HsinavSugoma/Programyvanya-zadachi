from threading import Thread
from queue import Queue
from time import time, sleep
import random
import logging
from collections import deque, defaultdict

logging.basicConfig(level=logging.DEBUG)

start = time()
P = 2


class MessageQueue:
    def __init__(self):
        self.data = defaultdict(Queue)

    def put(self, message, priority):
        self.data[priority].put(message)

    def get(self):
        for p in range(P, 0, -1):
            if not self.data[p]:
                continue
            return self.data[p].get()
        return None


q = MessageQueue()


def put(n, p_time, fixed=False):
    for i in range(n):
        t = p_time if fixed else random.random() * (p_time - 1) + 1
        sleep(t)
        priority = random.randint(1, 2)
        message = f"ПОВІДОМЛЕННЯ {i} (створенно o {time() - start:.4f}) пріорітет {priority}"
        logging.debug(f"В чергу додано {message}, яке створювалось {t:.4f} секунд")
        q.put(message, priority)


def get(n, p_time, fixed=False):
    for i in range(n):
        t = p_time if fixed else random.random() * (p_time - 1) + 1
        message = q.get()
        logging.debug(f"З черги отримано {message}, яке буде оброблятись {t:.4f} секунд")
        sleep(t)
        print(f"\"{message}\" оброблене на {time() - start:.4f} секунді")


if __name__ == '__main__':
    n = 10
    t1 = 2
    t2 = 4

    th1 = Thread(target=put, args=(n, t1))
    th2 = Thread(target=get, args=(n, t2))
    th1.start()
    th2.start()

    th1.join()
    th2.join()
