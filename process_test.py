from multiprocessing import Process
import os
import time

# 子进程要执行的代码
def run_proc(name):
    time.sleep(20)
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    p.daemon=False
    p.start()
    print('Child process will start.')
    print('Child process end.')