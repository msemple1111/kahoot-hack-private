import queue
import queueWorker
import time
import Kahoot
class kahootQueue(Kahoot):
    def __init__(self):
        self.num_worker_threads = 5
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
                time.sleep(0.25)
            work_on = queueWorker(workerType, item)
            self.q.task_done()
    def end(self):
        for i in range(self.num_worker_threads):
            self.q.put((None, None))
        for t in self.threads:
            t.join()
    def map(self, sequence):
        for item in sequence:
            self.q.put(item)
