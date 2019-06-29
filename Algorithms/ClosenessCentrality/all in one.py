import sys
import heapq

def shortest_path(graph_list,index): #graph_list is list of lists of lists
  pq=[]
  short_list=[]
  parent_list=[]
  output=0
  for i in range (len(graph_list)):#initialization
      short_list.append(100000)
      parent_list.append(-1)
      i=i+1
  short_list[index]=0
  parent_list[index]=-1
  
  for i in range (len(graph_list)):
    if(i==index ):
      j=0
      for j in range(len(graph_list[i])):
          heapq.heappush(pq,[graph_list[i][j][1],graph_list[i][j][0],i])
          j=j+1
    i=i+1
      
  while(not(len(pq)==0)):
      temp_list=heapq.heappop(pq)#weight,node,parent
      if(short_list[temp_list[1]]==100000): 
       short_list[temp_list[1]]=temp_list[0]
       output=output+temp_list[0]
       parent_list[temp_list[1]]=temp_list[2]
       weight=temp_list[0]
       
      else:
         continue 
      

      for i in range (len(graph_list)):
        if(i==temp_list[1]):
          j=0
          for j in range(len(graph_list[i])):
            
              heapq.heappush(pq,[graph_list[i][j][1]+weight,graph_list[i][j][0],i])
              j=j+1
        i=i+1     
  
  return output




first_line=input()
first_line=first_line.split()
number_nodes=int(first_line[0])
number_edges=int(first_line[1])

graph=[[] for j in range (number_nodes)]

for i in range (number_edges):
  my_line=input()
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
     i=i+1


    

    
