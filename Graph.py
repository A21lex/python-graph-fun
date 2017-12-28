class Graph(dict):
    def __init__(self, vertex_list, edge_list):
        for vertex in vertex_list:
            self[vertex] = set() # create dict where every vertex returns an empty set
        for edge in edge_list:
            self.add_edge(edge)  # for every edge: add 2nd element to 1st element's mapped set and vice versa
    def add_edge(self, edge):
        self[edge[0]].add(edge[1])
        self[edge[1]].add(edge[0])
    def add_vertex(self, vertex):
        self[vertex] = set()     # add a new vertex with empty set
    def delete_edge(self, edge):
        self[edge[0]].remove(edge[1])
        self[edge[1]].remove(edge[0])
    def delete_vertex(self, vertex):
        temp_neighbour_set = self[vertex].copy()  # set of all the neighbours of the vertex
        for neighbour in temp_neighbour_set:
            self.delete_edge((neighbour, vertex)) # delete the edge between some neighbour and the vertex
        del self[vertex] # finish by deleting the vertex itself

# test graphs

# graph = Graph(['A', 'B'], [('A', 'B')]) # very simple: A----B
# graph.add_vertex('C')
# graph.add_edge( ('A', 'C') ) # now: A----B and A----C
# neighbours_of_A = graph['A'] # will return all nodes adjacent to 'A'
# print (neighbours_of_A)
# graph.delete_edge( ('A', 'C') )
# print (neighbours_of_A)
# graph.delete_vertex('B')
# print (neighbours_of_A)