import queue, threading, time
class kahootQueue:
    def __init__(self, noWorkers=5):
        self.num_worker_threads = int(noWorkers)
        self.q = queue.Queue()
        self.threads = []
        for i in range(self.num_worker_threads):
            self.addSingleWorkerThread()
    def addSingleWorkerThread(self):
        t = threading.Thread(target=self.worker)
        t.start()
        self.threads.append(t)
    def add(self, workerType, *args, **kwargs):
        self.q.put((workerType, args, kwargs))
    def worker(self):
        while True:
            if self.q.empty():
                time.sleep(0.05)
            else:
                workerType, args, kwargs = self.q.get()
                if workerType is None:
                    break
                self.doWork(workerType, args, kwargs)
    def doWork(self, workerType, args, kwargs):
        if workerType is False:
            time.sleep(0.05)
        workerType(*args, **kwargs)
        self.q.task_done()
    def end(self):
        for i in range(self.num_worker_threads):
            self.q.put((None, [], {}))
        for t in self.threads:
            t.join()
    def map(self, sequence):
        for x in sequence:
            workerType, args, kwargs = x
            self.add(workerType, *args, **kwargs)
    def join(self):
        for t in self.threads:
            t.join()
