class receive:
    def __init__(self, queuePointer):
        self.queue = queuePointer
    def connect(self, r):
        try:
            response = json.loads(r.text)
            if len(response) > 0:
                for i, x in enumerate(response):
                    if x['channel'] != "/meta/connect":
                        self.queue.add(x)
        except:
            raise KahootError('')
