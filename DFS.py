from Graph import Graph

""" Implementation of Depth First Search method of Graph Traversal"""

# graph used for the example run of the algorithm
graphDFS = Graph(
    ['A','B','S','C','D','F','G','E','H'],
    [('A','B'), ('A','S'), ('S','C'), ('S','G'), ('C','D'), ('C','E'), ('C','F'), ('G','F'), ('G','H'), ('E','H')]
)
neighbours_of_E = graphDFS['E']
print neighbours_of_E

