from threading import Thread, RLock
import time
res = 0
M = 10_100_00
v1=[1+i for i in range(M)]
v2=[i-1 for i in range(M)]
N = 4
T = M//N
scal_lock = Rlock()
def scalar(v1,v2):
    global res
    for a,b in zip(v1,v2):
        with scal_lock:
            res += a*b
if __name__ == '__main__':
    run = [Thread(target=scalar, args=(v1[T*i:T*(1+i)],v2[T*i:T*(i+1)])) for i in range(0,N)]
    for run_thr in run:
        run_thr.start()
    for run_thr in run:
        run_thr.join()
    print(f"res = {res}")
