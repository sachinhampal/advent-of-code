class DisjointSetUnion:
    def __init__(self, num_nodes):
        self.__parents = list(range(num_nodes))
        self.__size = [1] * num_nodes

    def find(self, node):
        if node != self.__parents[node]:
            self.__parents[node] = self.find(self.__parents[node])
        return self.__parents[node]

    def union(self, node_1, node_2):
        a = self.find(node_1)
        b = self.find(node_2)
        if a == b:
            return

        if self.__size[a] < self.__size[b]:
            a, b = b, a

        self.__parents[b] = a
        self.__size[a] += self.__size[b]
