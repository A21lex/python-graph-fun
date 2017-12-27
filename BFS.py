from Graph import Graph
from collections import deque

# above: importing Graph class from Graph.py module

""" Here we will implement Breadth First Search method of Graph Traversal"""

# test graphs

graph = Graph(['A', 'B'], [('A', 'B')]) # very simple: A----B
graph.add_vertex('C')
graph.add_edge( ('A', 'C') ) # now: A----B and A----C
neighbours_of_A = graph['A'] # will return all nodes adjacent to 'A'
print (neighbours_of_A)
graph.delete_edge( ('A', 'C') )
print (neighbours_of_A)
graph.delete_vertex('B')
print (neighbours_of_A)

# seems to be working.. now, to BFS
# deque is an efficient implementation of a queue: no need to shift all elements when popping
queue = deque([])
queue.append("Alice")
queue.append("Bob")
print queue
print queue.popleft() + " is now leaving"
print queue
queue.popleft()
print queue

# graph used for the example run of the algorithm
graph = Graph(
    ['A','B','S','C','D','F','G','E','H'],
    [('A','B'), ('A','S'), ('S','C'), ('S','G'), ('C','D'), ('C','E'), ('C','F'), ('G','F'), ('G','H'), ('E','H')]
)
neighbours_of_E = graph['E']
print neighbours_of_E

current_node = 'A' # currently worked on node: start with A for instance
queue.append(current_node)
output = [] # list storing output (i.e. visited nodes)
output.append(current_node)
print output

while queue:
    current_node = queue.popleft()
    if not output.__contains__(current_node): # avoiding duplicates
        output.append(current_node)
    neighbours = graph[current_node]
    for node in neighbours:
        if not output.__contains__(node):
            queue.append(node)
            output.append(node)


print "ba"
print output




# # aka do-while here
# while True:
#     print "current output: "
#     print output
#     print "current queue: "
#     print queue
#     neighbours = graph[current_node]
#     for node in neighbours:
#         if output.__contains__(node):
#             break
#         queue.append(node)
#         output.append(node)
#     if queue: # if queue is NOT EMPTY
#         current_node = queue.popleft()
#     #neighbours = graph[current_node]
#
#     if not queue:
#         break
#
# print output
#
# neighbours = graph[current_node] # neighbours of the currently worked on node
# for node in neighbours:
#     queue.append(node) # add to queue
#     if not output.__contains__(node):
#         output.append(node) # and mark as visited
#
# current_node = queue.popleft() # this changes currently worked on node to first element of the queue and dequeues it
# neighbours = graph[current_node]
# for node in neighbours:
#     if output.__contains__(node):
#         break # if the node is visited already, switch currently worked on node to the first element of the queue
#     queue.append(node)
#     if not output.__contains__(node):
#         output.append(node)
# current_node = queue.popleft()
# neighbours = graph[current_node]