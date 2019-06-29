class Graph():

    def __init__(self, nodes): # vertices 
        self.nodes = nodes
        self.nodes_num = len(nodes)
        self.graph = [None] * self.nodes_num
        

    def add_node(self): # add a node and return its number
        self.graph.append(None)
        self.nodes_num += 1
        return len(self.graph) - 1
    
    def add_edge(self, edge): # edge is a tuple (u, v, w)
        if edge[0] <= self.nodes_num and edge[1] <= self.nodes_num:
            return -1 # indicates edge has a node not in the graph
        self.graph[edge[0]] = (edge[1], edge[2]) # add edge in the source node place

    def add_edges(self, edges): # add multiple edges, edges is list of tuples (u, v, w)
        for edge in edges:
            self.add_edge(edge)
    
    
        


   





    