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
  

for i in range (number_nodes):
     output=0
     output=shortest_path(graph,i)
     
     output=(number_nodes-1)/output
     print(round(output,12))
