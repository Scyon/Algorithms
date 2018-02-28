class Node:

	def __init__(self, name):
		self.name = name
		self.adjacencyList = []
		self.visited = False
		self.predecessor = None


class BreadthFirstSearch:

	def bfs(self, startNode):
		queue = []
		queue.append(startNode)
		startNode.visited = True
		while queue:
			# pop() removes and returns specified item in list
			currentNode = queue.pop(0)
			print('{}'.format(currentNode.name))
			for n in currentNode.adjacencyList:
				if not n.visited:
					n.visited = True
					queue.append(n)


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

	bfs = BreadthFirstSearch();
	bfs.bfs(node1);
