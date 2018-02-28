import sys
import heapq

class Edge(object):

	def __init__(self, weight, startVertex, targetVertex):
		self.weight = weight
		self.startVertex = startVertex
		self.targetVertex = targetVertex
		
class Node(object):

	def __init__(self, name):
		self.name = name
		self.predecessor = None
		self.adjacenciesList = []
		self.minDistance = sys.maxsize
		
	def __lt__(self, other):
		# overriding 'less than' function in order to facillitate heap creation
		# which requires comparison of nodes in order to build min heap
		# (parents must be smaller than children)
		return self.minDistance < other.minDistance

class Algorithm(object):

	def calculateShortestPath(self, vertexList, startVertex):
		# initialize heap
		q = []
		# set distance of starting vertex to 0
		startVertex.minDistance = 0
		# push starting vertex to heap
		heapq.heappush(q, startVertex)
		# while heap is not empty
		while q:
			# set currentVertex to the root node in the heap
			currentVertex = heapq.heappop(q)
			# iterate through edges connected to node
			for edge in currentVertex.adjacenciesList:
				# u --> starting node
				u = edge.startVertex
				# v --> terminal node
				v = edge.targetVertex
				# distance = distance to starting node + distance between
				# starting and terminal nodes
				newDistance = u.minDistance + edge.weight
				# if new distance is less than distance to terminal node
				if newDistance < v.minDistance:
					# set predecessor of terminal node to starting node
					v.predecessor = u
					# update the minimum distance to new distance
					v.minDistance = newDistance
					# push terminal node to heap
					heapq.heappush(q, v)
					
	def getShortestPathTo(self, targetVertex):
		print('The shortest path to vertex {} is: {}'.format(targetVertex.name, targetVertex.minDistance))
		node = targetVertex
		while node is not None:
			print('{}'.format(node.name))
			node = node.predecessor


if __name__ == '__main__':

	node1 = Node("A")
	node2 = Node("B")
	node3 = Node("C")
	node4 = Node("D")
	node5 = Node("E")
	node6 = Node("F")
	node7 = Node("G")
	node8 = Node("H")

	edge1 = Edge(5,node1,node2)
	edge2 = Edge(8,node1,node8)
	edge3 = Edge(9,node1,node5)
	edge4 = Edge(15,node2,node4)
	edge5 = Edge(12,node2,node3)
	edge6 = Edge(4,node2,node8)
	edge7 = Edge(7,node8,node3)
	edge8 = Edge(6,node8,node6)
	edge9 = Edge(5,node5,node8)
	edge10 = Edge(4,node5,node6)
	edge11 = Edge(20,node5,node7)
	edge12 = Edge(1,node6,node3)
	edge13 = Edge(13,node6,node7)
	edge14 = Edge(3,node3,node4)
	edge15 = Edge(11,node3,node7)
	edge16 = Edge(9,node4,node7)

	node1.adjacenciesList.append(edge1)
	node1.adjacenciesList.append(edge2)
	node1.adjacenciesList.append(edge3)
	node2.adjacenciesList.append(edge4)
	node2.adjacenciesList.append(edge5)
	node2.adjacenciesList.append(edge6)
	node8.adjacenciesList.append(edge7)
	node8.adjacenciesList.append(edge8)
	node5.adjacenciesList.append(edge9)
	node5.adjacenciesList.append(edge10)
	node5.adjacenciesList.append(edge11)
	node6.adjacenciesList.append(edge12)
	node6.adjacenciesList.append(edge13)
	node3.adjacenciesList.append(edge14)
	node3.adjacenciesList.append(edge15)
	node4.adjacenciesList.append(edge16)


	vertexList = (node1, node2, node3, node4, node5, node6, node7, node8)

	algorithm = Algorithm()
	algorithm.calculateShortestPath(vertexList, node1)
	algorithm.getShortestPathTo(node7)
