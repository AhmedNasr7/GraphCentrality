import sys
import Dijkistra

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
  
centrality_list=[0  for i in range (number_nodes)]
#getting shortest path for every node and putting it in s_list
for i in range (number_nodes):
     s_list=Dijkistra.shortest_path(graph,i)
     for j in range (len(s_list)):
         centrality_list[i]=centrality_list[i]+s_list[j]
         j=j+1
     i=i+1
#centrality list contained sum of shortest path for every node
centrality_list=[((number_nodes-1)/i) for i in centrality_list]
print(centrality_list)
