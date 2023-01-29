from typing import Callable

from non_sync.util import long_func
from multiprocessing import Process


class WorkerProcess(Process):
    def __init__(self, name: str, function: Callable, args: tuple = (), kwargs: dict = {}):
        Process.__init__(self)
        self.name = name
        self.function = function
        self.args = args
        self.kwargs = kwargs

        print(f'Create {self.name}')

    def run(self):
        print(f'Start {self.name}')
        self.function(*self.args, **self.kwargs)


if __name__ == '__main__':
    processes = []
    workers = [WorkerProcess(name=f'Worker[{c}]', function=long_func, args=(c,))
               for c in range(4)]

    [w.start() for w in workers]

    [w.join() for w in workers]
