import networkx as nx
import matplotlib.pyplot as plt

file=open("graph.txt","r")
lines=file.readlines()
#getting number of node and number of edges from first line in file
first_line=lines[0]
first_line=first_line.split()
number_nodes=int(first_line[0])
number_edges=int(first_line[1])

graph=[[] for j in range (number_nodes)]
#initialization for graph
for i in range (number_edges):
  my_line=lines[i+1]
  my_line=my_line.split()
  my_line=[int (i) for i in (my_line)]
  graph[my_line[0]].append([my_line[1],my_line[2]])
  graph[my_line[1]].append([my_line[0],my_line[2]])
  i=i+1
  

  
file1=open("output.txt","r")
output_lines=file1.readlines()
output_lines=output_lines[0].split()

centrality=[float(i) for i in output_lines]
#list_of_size=[10000*i for i in centrality]
list_of_size= []
for i in centrality:
  list_of_size.append(int(1500 * i))

print(centrality)
print(list_of_size)
node_list= [v for v in range(number_nodes)]

G=nx.Graph()
#d = G.degree([i for i in range(number_nodes)])
#print("deg: ", d)
##for i in range (number_nodes):
##    if i == 0:
##      size_node = 3
##    else:
##      size_node=list_of_size[i]
##    G.add_node(i, size=size_node)
##    
    
for i in range(len(graph)):
        for j in range(len(graph[i])):
            G.add_edge(i, graph[i][j][0], weight=graph[i][j][1])
#nx.draw(G,with_labels=True,font_weight='bold',node_size=[v * (100 + 200) for v in range(number_nodes)])
nx.draw_networkx(G, nodelist = node_list, node_size = list_of_size)
plt.show()
