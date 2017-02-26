import queue, threading, time
from Kahoot import queueWorker
class kahootQueue:
    def __init__(self, noWorkers=5):
        self.num_worker_threads = noWorkers
        self.q = queue.Queue()
        self.threads = []
        for i in range(self.num_worker_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            self.threads.append(t)
    def add(self, workerType, item):
        self.q.put((workerType, item))
    def worker(self):
        while True:
            workerType, item = self.q.get()
            if item is None:
                break
            elif item is False:
                time.sleep(0.05)
            work_on = queueWorker(workerType, item)
            self.q.task_done()
    def end(self):
        for i in range(self.num_worker_threads):
            self.q.put((None, None))
        for t in self.threads:
            t.join()
    def map(self, sequence):
        for workerType, item in sequence:
            self.add(workerType, item)

def queueWorker(workerType, item):
    workerType(item)
