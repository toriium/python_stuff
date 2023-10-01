import time
from queue import Queue, Empty
from threading import Thread
from typing import Callable


class WorkerQueue:
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
    def __init__(self, queue_name: str, target: Callable, qtd_workers: int):
        self.queue_name = queue_name
        self.target = target
        self.qtd_workers = qtd_workers
        self.workers = None
        self.queue = WorkerQueue()
        self.must_stop_workers = False

    def start_workers(self):
        self.workers = [
            ConsumerQueueWorker(worker_name=f'Worker[{c}]', worker_queue_manager=self)
            for c in range(self.qtd_workers)]
        [w.start() for w in self.workers]

    def stop_workers(self):
        self.must_stop_workers = True
        [w.join() for w in self.workers]


class ConsumerQueueWorker(Thread):
    def __init__(self, worker_name: str, worker_queue_manager: WorkerQueueManager):
        Thread.__init__(self)
        self.worker_name = worker_name
        self.queue_name = worker_queue_manager.queue_name
        self.worker_queue_manager = worker_queue_manager
        self.queue = worker_queue_manager.queue
        self.target = worker_queue_manager.target

        print(f'Created worker {self.worker_name} for queue {self.queue_name}')

    def run(self):
        while True:
            if self.queue.is_empty():
                if self.worker_queue_manager.must_stop_workers:
                    break
                time.sleep(0.2)
                continue

            next_call = self.queue.get()
            if not next_call:
                continue

            try:
                self.target(next_call)
            except Exception as error:
                print(error)


if __name__ == '__main__':
    manager = WorkerQueueManager(queue_name='target_fun_Queue', target=target_fun, qtd_workers=4)
    manager.start_workers()
    for v in range(10):
        manager.queue.put(v)
    print('put all items')
    manager.stop_workers()
