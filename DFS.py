class Node:

	def __init__(self, name):
		self.name = name
		self.visited = False
		self.adjacencyList = []
		self.predecessor = None


class DepthFirstSearch(self):

	def dfs(self, node):
		node.visited = True
		print('{}'.format(node.name))
		for n in node.adjacencyList:
			if not n.visited:
				self.dfs(n)


if __name__ == '__main__':

	node1 = Node('A');
	node2 = Node('B');
	node3 = Node('C');
	node4 = Node('D');
	node5 = Node('E');

	node1.adjacencyList.append(node2);
	node1.adjacencyList.append(node3);
	node2.adjacencyList.append(node4);
	node4.adjacencyList.append(node5);

	dfs = DepthFirstSearch();
	dfs.dfs(node1);
