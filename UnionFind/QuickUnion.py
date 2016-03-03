class QuickUnionUF(object):
    """
    Quick-union algorithm
    So called lazy approach
    Worst-time: MN
    where M union-find ops on a set of N objects
    """
    def __init__(self, N):
        self.N = N
        self._id = list(range(N))

    def _root(self, i):
        """Chase parent pointers until reach root"""
        while i != self._id[i]:
            i = self._id[i]
        return i

    def union(self, p, q):
        """Change root of p to point to root of q"""
        i = self._root(p)
        j = self._root(q)
        self._id[i] = j

    def connected(self, p, q):
        return self.find(p, q)

    def find(self, p, q):
        """Check if p and q have the same root"""
        return self._root(p) == self._root(q)

    def count(self):
        pass
