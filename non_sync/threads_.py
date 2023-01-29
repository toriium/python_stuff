from threading import Thread

import time
from util import time_execution, long_func

await_list = []

def main():
    print('[main] START')
    print('[main] long_func(1)')
    p = Thread(target=long_func, args=(1,))
    p.start()
    await_list.append(p)

    print('[main] waiting between functions calls')
    time.sleep(1)

    print('[main] long_func(2)')
    p = Thread(target=long_func, args=(2,))
    p.start()
    await_list.append(p)

    print('[main] --------- waiting Threads to end ---------')
    [p.join() for p in await_list]
    print('[main] END')


if __name__ == '__main__':
    with time_execution():
        main()
