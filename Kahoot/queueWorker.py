import Kahoot
class queueWorker(kahootQueue):
    def __init__(self, workerType, item):
        func = workerType
