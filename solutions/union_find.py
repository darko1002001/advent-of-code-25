import heapq
from collections import defaultdict
from typing import Generic, TypeVar

T = TypeVar("T")


class UnionFind(Generic[T]):
    def __init__(self):
        self.parent: dict[T, T] = {}
        self.rank: dict[T, int] = {}

    def find(self, item: T) -> T:
        if item not in self.parent:
            self.parent[item] = item
            self.rank[item] = 0
            return item

        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])

        return self.parent[item]

    def union(self, item1: T, item2: T) -> bool:
        root1 = self.find(item1)
        root2 = self.find(item2)

        if root1 == root2:
            return False

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True

    def get_largest_components(self, n: int | None = None) -> list[list[T]]:
        components: dict[T, list[T]] = defaultdict(list)
        for element in self.parent:
            root = self.find(element)
            components[root].append(element)

        all_components = list(components.values())
        if n is not None:
            largest = heapq.nlargest(n, all_components, key=len)
            return largest
        return sorted(all_components, key=len)
