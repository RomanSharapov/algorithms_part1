# from UnionFind.QuickFind import QuickFindUF as UF
# from UnionFind.QuickUnion import QuickUnionUF as UF
# from UnionFind.WeightedQuickUnion import WeightedQuickUnionUF as UF
from UnionFind.WeightedQuickUnionPathCompression import WeightedQuickUnionPathCompressionUF as UF


def main():
    N = int(input('Enter number of objects: '))
    uf = UF(N)
    while True:
        pair = input('Enter pair delimited by space: ').split()
        if not pair:
            break
        p, q = [int(entry) for entry in pair]
        if not uf.connected(p, q):
            uf.union(p, q)
            print(p, q)
        print([x for x in range(10)])
        print(uf._id)


if __name__ == "__main__":
    main()
