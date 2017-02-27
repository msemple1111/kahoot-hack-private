class receive:
    def processResponse(self, r):
        response = json.loads(r.text)
        if len(response) > 0:
            for i, x in enumerate(response):
                if x['channel'] != "/meta/connect":
                    self.queue.append(x)
