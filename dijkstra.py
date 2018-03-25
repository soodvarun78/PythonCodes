#graph = {
#          'A': {'B': 4, 'H': 3},
#          'B': {'A':4,'C': 4},
#          'C': {'B': 4, 'I': 1},
#          'H': {'A': 3, 'I':  1},
#          'I': {'H': 1,'C':1}
#        }

graph = {
         'A': {'B': 4,'H':8},
          'B': {'A':4,'C': 8,'H':11},
          'C': {'B':8,'D': 7,'F':4,'I':2},
          'D': {'C':7,'E': 9, 'F': 14},
          'E': {'D':9,'F': 10},
          'F': {'C':4,'D':14,'G': 2,'E':10},
          'G': {'F':2,'H':1,'I': 6},
          'H': {'A':8,'B':11,'G': 1,'I':7},
          'I': {'C': 2,'G':6,'H':7}
        }

v=[] #v visited vertex 
d={} # Distance from the start vertex 
u=[] #u is unvisited vertex
# c is current vertex 
# nVertices is nearby vertices to vertex being looped


for i in graph.keys():
	d[i]=100 #Initially assign a high value to distance of the vertex from starting
             # This is genearlly mentioned as infinity in Wikipedia 

for i in graph.keys():
	u.append(i) #Add all vertices as unvisited	

def calculate_next_vertex_to_visit():
	""" Function to calulate the next vertex to visit, which is the at the smallest distance among the unvisited vertex """ 	
	nextvertex = None
	dist = 100 #An arbitrary high value
	for i in graph.keys():
		if not i in v:
			if dist > d[i]:
				nextvertex = i
				dist = d[i]
	return nextvertex 

def tr(s):
	""" Function to tranverse the graph """ 	
	nextVertexToVisit=s
	d[nextVertexToVisit]=0 #start vertex 
	while len(u) is not 0:
		u.remove(nextVertexToVisit)
		v.append(nextVertexToVisit)
		c=nextVertexToVisit
		nVertices=graph[c]
		nextVertexToVisit = None
		for i in nVertices.keys():
			if i not in  v:  #vertex is not visited 
				if d[c] + nVertices[i] < d[i]:
					d[i] = d[c] + nVertices[i]
		nextVertexToVisit = 	calculate_next_vertex_to_visit()
		if nextVertexToVisit is None: #transversed all vertices
			break

tr("I") # start vertex
print("The distance from start vertex")
print (d)
