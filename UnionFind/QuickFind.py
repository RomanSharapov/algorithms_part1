class QuickFindUF(object):
    """
    Quick-find algorithm
    So called eager approach
    Worst-time: MN
    where M union-find ops on a set of N objects
    """
    def __init__(self, N):
        self.N = N
        self._id = list(range(N))

    def union(self, p, q):
        pid = self._id[p]
        qid = self._id[q]
        for i in range(len(self._id)):
            if self._id[i] == pid:
                self._id[i] = qid

    def connected(self, p, q):
        return self.find(p, q)

    def find(self, p, q):
        return self._id[p] == self._id[q]

    def count(self):
        pass
