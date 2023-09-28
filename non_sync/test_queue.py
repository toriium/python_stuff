import time
from queue import Queue, Empty
from threading import Thread
from typing import Callable


class ParserQueue:
    __queue = Queue()

    @classmethod
    def put(cls, data):
        cls.__queue.put(data)

    @classmethod
    def get(cls):
        try:
            return cls.__queue.get(block=False)
        except Empty:
            return None

    @classmethod
    def is_empty(cls):
        return cls.__queue.empty()


def target_fun(name: int):
    print(f'{name} START')
    time.sleep(3)
    print(f'{name} END')


class WorkerQueueManager:
    def __init__(self, qtd_threads: int):
        self.qtd_threads = qtd_threads
        self.workers = None
        self.must_stop_workers = False

    def start_workers(self, target: Callable):
        self.workers = [ConsumerQueueWorker(name=f'Worker[{c}]', worker_queue_manager=self, target=target) for c in
                        range(4)]
        [w.start() for w in self.workers]

    def stop_workers(self):
        self.must_stop_workers = True
        [w.join() for w in self.workers]


class ConsumerQueueWorker(Thread):
    def __init__(self, name: str, worker_queue_manager: WorkerQueueManager, target: Callable):
        Thread.__init__(self)
        self.name = name
        self.worker_queue_manager = worker_queue_manager
        self.target = target

        print(f'Created worker {self.name}')

    def run(self):
        while True:
            if ParserQueue.is_empty():
                if self.worker_queue_manager.must_stop_workers:
                    break
                time.sleep(0.2)
                continue

            crawler_response = ParserQueue.get()
            if not crawler_response:
                continue

            try:
                self.target(crawler_response)
            except Exception as error:
                print(error)


if __name__ == '__main__':
    manager = WorkerQueueManager(4)
    manager.start_workers(target=target_fun)
    for v in range(10):
        ParserQueue.put(v)
    print('put all items')
    manager.stop_workers()
