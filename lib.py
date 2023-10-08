import random


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_or_size = [-1] * n
        self.group = n

    def merge(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        self.group -= 1
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        if self.parent_or_size[a] < 0:
            return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        return -self.parent_or_size[self.leader(a)]

    def group_count(self):
        return self.group


class List:
    @staticmethod
    def gen_list(
        n: int, min_value: int = 0, max_value: int = 10**9, is_unique: bool = False
    ) -> list[int]:
        """
        長さ$n$の配列を作成します．
        配列の値はmin_value以上，max_value未満の値からランダムで選ばれます．
        is_uniqueがtrueだと値は配列の中で一意になります．
        """
        if is_unique:
            assert max_value - min_value + 1 >= n
            return random.sample(range(min_value, max_value), k=n)
        else:
            return [random.randrange(min_value, max_value) for _ in range(n)]

    @staticmethod
    def gen_permutation(n: int, is_1index: bool = False) -> list[int]:
        """
        長さ$n$の順列を作成します．
        is_1indexがtrueだと値は[1,n+1), falseだと[0,n)の範囲となります．
        """
        arr = list(range(1, n + 1)) if is_1index else list(range(n))
        random.shuffle(arr)
        return arr


class UndirectedGraph:
    @staticmethod
    def gen_edges(n: int, m: int, is_1index: bool = False) -> list[list[int]]:
        """
        重みなしの辺を作成します．
        $n$: 頂点の数, $m$: 辺の数
        is1index: trueで頂点番号を[1,n+1), falseで[0,n)で出力します．
        """
        assert n - 1 <= m
        while True:
            used = set()
            dsu = UnionFind(n)
            edges = []
            for _ in range(m):
                u = random.randrange(0, n)
                v = random.randrange(0, n)
                while u == v:
                    v = random.randrange(0, n)
                if u > v:
                    u, v = v, u
                if (u, v) in used:
                    continue
                edges.append([u, v])
                dsu.merge(u, v)
                used.add((u, v))
            if dsu.group_count() == 1:
                break
        if is_1index:
            return [[u + 1, v + 1] for u, v in edges]
        return edges

    @staticmethod
    def gen_weighted_edges(
        n: int,
        m: int,
        min_value: int = 1,
        max_value: int = 10**9,
        is_1index: bool = False,
    ) -> list[list[int]]:
        """
        重みありの辺を作成します．
        $n$: 頂点の数, $m$: 辺の数
        is1index: trueで頂点番号を[1,n+1), falseで[0,n)で出力します．
        辺の重みをmin_value以上max_value未満で指定します．
        """
        assert n - 1 <= m
        while True:
            used = set()
            dsu = UnionFind(n)
            edges = []
            for _ in range(m):
                u = random.randrange(0, n)
                v = random.randrange(0, n)
                while u == v:
                    v = random.randrange(0, n)
                if u > v:
                    u, v = v, u
                if (u, v) in used:
                    continue
                w = random.randrange(min_value, max_value)
                edges.append([u, v, w])
                dsu.merge(u, v)
                used.add((u, v))
            if dsu.group_count() == 1:
                break
        if is_1index:
            return [[u + 1, v + 1, w] for u, v, w in edges]
        return edges


class DirectedGraph:
    @staticmethod
    def gen_edges(n: int, m: int, is_1index: bool = False) -> list[list[int]]:
        """
        未作成
        $n$: 頂点の数, $m$: 辺の数
        is1index: trueで頂点番号を[1,n+1), falseで[0,n)で出力します．
        """
        assert n - 1 <= m
        pass


class Tree:
    @staticmethod
    def gen_edges(n: int, root: int = 0, is_1index: bool = False) -> list[list[int]]:
        dsu = UnionFind(n)
        edges = []
        for i in range(n - 1):
            while True:
                u = random.randrange(0, n) if i > 0 else root
                v = random.randrange(0, n)
                while u == v or v == root:
                    v = random.randrange(0, n)
                if dsu.same(u, v):
                    continue
                edges.append([u, v])
                dsu.merge(u, v)
                break
        if is_1index:
            return [[u + 1, v + 1] for u, v in edges]
        return edges

    @staticmethod
    def gen_weighted_edges(
        n: int,
        root: int = 0,
        min_value: int = 1,
        max_value: int = 10**9,
        is_1index: bool = False,
    ) -> list[list[int]]:
        dsu = UnionFind(n)
        edges = []
        for i in range(n - 1):
            while True:
                u = random.randrange(0, n) if i > 0 else root
                v = random.randrange(0, n)
                while u == v or v == root:
                    v = random.randrange(0, n)
                if dsu.same(u, v):
                    continue
                w = random.randrange(min_value, max_value)
                edges.append([u, v, w])
                dsu.merge(u, v)
                break
        if is_1index:
            return [[u + 1, v + 1, w] for u, v, w in edges]
        return edges


class String:
    lw = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def gen_string(n: int, char_list: str = lw):
        size = len(char_list)
        arr = [random.choice(char_list) for _ in range(n)]
        return "".join(arr)
