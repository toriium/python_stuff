from typing import Callable

from non_sync.util import long_func
from threading import Thread


def func_with_return():
    return 'this a return'


class WorkerThread(Thread):
    def __init__(self, name: str, function: Callable, args: tuple = (), kwargs: dict = {}):
        Thread.__init__(self)
        self.name = name
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.function_return = None

        print(f'Create {self.name}')

    def run(self):
        print(f'Start {self.name}')
        self.function_return = self.function(*self.args, **self.kwargs)

    def function_return(self):
        return self.function_return



if __name__ == '__main__':
    processes = []
    workers = [WorkerThread(name=f'Worker[{c}]', function=func_with_return)
               for c in range(4)]

    [w.start() for w in workers]

    [w.join() for w in workers]

    a = [w.function_return for w in workers]
    print(a)
