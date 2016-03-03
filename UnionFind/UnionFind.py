# from QuickFind import QuickFindUF as UF
# from QuickUnion import QuickUnionUF as UF
# from WeightedQuickUnion import WeightedQuickUnionUF as UF
from WeightedQuickUnionPathCompression import WeightedQuickUnionPathCompressionUF as UF

def main():
    N = int(input())
    uf = UF(N)
    while True:
        pair = input().split()
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
