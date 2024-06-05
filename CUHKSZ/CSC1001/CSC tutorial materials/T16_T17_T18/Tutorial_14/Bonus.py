class Solution:
    class Node:
        def __init__(self, num):
            self.edges = []
            self.num = num
            self.color = 0
            self.subBlackNum = 0


#Edge between two nodes, attributes indicating the weight of edge, the starting and ending node of the edge.
    class edge:
        def __init__(self, weight, parent_idx, child_idx):
            self.weight = weight
            self.parent_idx = parent_idx
            self.child_idx = child_idx


#To compute total number of black nodes.
    def Main(self):
        total = 0
        total_black = self.depth_first_search(self.nodes[1])
        for i in range(1, len(self.nodes)):
            for edge in self.nodes[i].edges:
                inBlackNodes = total_black - self.nodes[edge.child_idx].subBlackNum
                outBlackNodes = self.nodes[edge.child_idx].subBlackNum
                total += edge.weight * inBlackNodes * outBlackNodes
        return total

#To find total number of balck nodes in the subtree of a node.
    def depth_first_search(self, node):
        total = 0
        for edge in node.edges:
            total += self.depth_first_search(self.nodes[edge.child_idx])
        node.subBlackNum += total
        return node.subBlackNum

    def read(self):
        num = int(input())
        color_list = list(map(int, input().split()))
        self.nodes = [self.Node(i) for i in range(num + 1)]
        for i in range(1, num + 1):
            self.nodes[i].color = color_list[i - 1]
            if self.nodes[i].color == 1:
                self.nodes[i].subBlackNum = 1
        for i in range(1, num):
            parent_idx, weight = map(int, input().split())
            child = i + 1
            new_edge = self.edge(weight, parent_idx, child)
            self.nodes[parent_idx].edges.append(new_edge)

if __name__ == '__main__':
    solver = Solution()
    solver.read()
    result = solver.Main()
    print(result)