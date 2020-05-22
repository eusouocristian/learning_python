from SSDB import SSDB

class Client:

    def __init__(self, host, port):
        self.ssdb = SSDB(host, port)

    def qpush(self, name, item):
        return self.ssdb.request('qpush', [name, item])

    def qpop(self, name, size = 1):
        r = self.ssdb.request('qpop', [name, size])
        return r.data

    def qsize(self, name):
        r = self.ssdb.request('qsize', [name])
        return r.data

    def qclear(self, name):
        return self.ssdb.request('qclear', [name])
