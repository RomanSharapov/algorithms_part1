class WeightedQuickUnionUF(object):
    """
    Weighted Quick-union algorithm
    Worst-time: N + M lgN
    where M union-find ops on a set of N objects
    """
    def __init__(self, N):
        self.N = N
        self._id = list(range(N))
        self.sz = [1 for _ in range(N)]

    def _root(self, i):
        """Chase parent pointers until reach root"""
        while i != self._id[i]:
            i = self._id[i]
        return i

    def union(self, p, q):
        """Change root of p to point to root of q"""
        i = self._root(p)
        j = self._root(q)
        if self.sz[i] < self.sz[j]:
            self._id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self._id[j] = i
            self.sz[i] += self.sz[j]

    def connected(self, p, q):
        return self.find(p, q)

    def find(self, p, q):
        """Check if p and q have the same root"""
        return self._root(p) == self._root(q)

    def count(self):
        pass
