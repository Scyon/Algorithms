import heapq

class Vertex:

	def __init__(self, name):
		self.name = name
		self.visited = False
		self.predecessor = None
		self.adjacenciesList = []
		
	def __str__(self):
		return self.name
		
class Edge:

	def __init__(self, weight, startVertex, targetVertex):
		self.weight = weight
		self.startVertex = startVertex
		self.targetVertex = targetVertex
		
	def __lt__(self, other):
		# overriding 'less than' function in order to facillitate edge comparison
		return self.weight < other.weight
	
	
class Prims:

	def __init__(self, unvisitedList):
		self.unvisitedList = unvisitedList
		self.spanningTree = []
		self.edgeHeap = []
		self.fullCost = 0
		
	def calculateSpanningTree(self, vertex):
		# remove starting node from unvisited list
		self.unvisitedList.remove(vertex)
		# while there are nodes to visit
		while self.unvisitedList:
			# for every edge connected to vertex
			for edge in vertex.adjacenciesList:
				# if targetVertex has not been visited
				if edge.targetVertex in self.unvisitedList:
					# push the edge to the heap
					heapq.heappush(self.edgeHeap, edge)
			# get the edge with the smallest weight from the heap
			# remove + return it
			minEdge = heapq.heappop(self.edgeHeap)
			# append to the spanning tree
			self.spanningTree.append(minEdge)
			# print
			print('Edge added to spanning tree: {} - {}'.format(minEdge.startVertex.name, minEdge.targetVertex.name))
			# add the edge's weight to the fullcost variable
			self.fullCost = self.fullCost + minEdge.weight
			# set the new starting vertex to be the target vertex of the minimum edge
			vertex = minEdge.targetVertex
			# remove the target vertex from the unvisited list
			self.unvisitedList.remove(vertex)

	def getSpanningTree(self):
		return self.spanningTree


node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")

edge1 = Edge(100,node1,node2)
edge2 = Edge(100,node2,node1)
edge3 = Edge(1000,node1,node3)
edge4 = Edge(1000,node3,node1)
edge5 = Edge(0.01,node3,node2)
edge6 = Edge(0.01,node2,node3)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge3)
node2.adjacenciesList.append(edge2)
node2.adjacenciesList.append(edge6)
node3.adjacenciesList.append(edge4)
node3.adjacenciesList.append(edge5)

unvisitedList = []
unvisitedList.append(node1)
unvisitedList.append(node2)
unvisitedList.append(node3)

algorithm = Prims(unvisitedList)
algorithm.calculateSpanningTree(node2)
