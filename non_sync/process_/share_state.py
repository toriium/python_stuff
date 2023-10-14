import time
from datetime import datetime
from typing import Callable

from non_sync.util import long_func
from multiprocessing import Process, Value


class WorkerProcess(Process):
    def __init__(self, name: str, obj_class, function: Callable, args: tuple = (), kwargs: dict = {}):
        Process.__init__(self)
        self.name = name
        self.obj_class = obj_class
        self.function = function
        self.args = args
        self.kwargs = kwargs

        print(f'Create {self.name}')

    def run(self):
        while True:
            # self.function(self.obj_class, self.name)
            r = self.function(self.name)
            if r:
                break


class Test:
    def __init__(self):
        self.values = {
            "v1": 0,
            "v2": 0,
        }

    def add(self, worker_name: str):
        # time.sleep(1)

        print('instance', worker_name, self.values)
        self.values['v1'] += 1
        self.values['v2'] += 1
        if self.values['v1'] >= 900_000:
            raise ValueError('fim')

    def change(self):
        print('calling change')
        self.values = 0


class TestC:
    values = {
        "v1": 0,
        "v2": 0,
    }

    @classmethod
    def add(cls, worker_name: str):
        time.sleep(1)

        print('class', worker_name, cls.values)

        cls.values['v1'] += 1
        cls.values['v2'] += 1
        if cls.values['v1'] >= 100:
            return 1

    @classmethod
    def change(cls):
        print('calling change')
        cls.values = 0


if __name__ == '__main__':
    # obj = Test()
    # obj = TestC
    processes = []
    workers = [WorkerProcess(name=f'Worker[{c}]', obj_class=None, function=TestC.add) for c in range(4)]

    start = datetime.now()
    [w.start() for w in workers]
    # time.sleep(2)
    # TestC.change()
    [w.join() for w in workers]
    print(f'time {datetime.now() - start}')
