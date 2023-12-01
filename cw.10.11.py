import threading
import time

import logging

logging.basicConfig(level=logging.DEBUG)
class ThreadReturnig(threading.Thread):

    def __init__(self, fun, args=()):

        threading.Thread.__init__(self)
        self.result = None
        self._fun = fun
        self._args = args
        self._exept = None

    def run(self):
        try:
            self.result = self._fun(*self._args)
        except ValueError as e:
            self._exept = e

    def getResult(self):
        return self.result

    def getExept(self):
        return self._exept

def factoriall1(n:int) -> int:

    try:
        m = int(n)
    except ValueError as e:
        raise e

    if n <= 1:
        return 1
    r = n * factoriall1(n-1)
    logging.debug("Result {}". format(r))

def factoriall2(n:int) -> int:
    logging.debug("Обчислення факторіалу циклами {}"
                  .format(n))
    try:
        m = int(n)
    except Exception as e:
        raise e

    p = 1
    for i in range(1, n+1):
        logging.debug("Обчислення факторіалу циклами {}"
                      .format(i))
        p *= i
    logging.debug("Result {}".format(p))
    return p

n = 20

# thread1 = threading.Thread(target=factoriall1, args=(n,))
# thread2 = threading.Thread(target=factoriall2, args=(n,))

thread1 = ThreadReturnig(factoriall1, args=(n,))
thread2 = ThreadReturnig(factoriall2, args=(n,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

if thread1.getExept():
    print("Отримано виключення в потоці 1: ", thread1.getExept())
else:
    print("Потік 1 завершився успішно: ", thread1.getResult())

if thread2.getExept():
    print("Отримано виключення в потоці 2: ", thread2.getExept())
else:
    print("Потік 2 завершився успішно: ", thread2.getResult())