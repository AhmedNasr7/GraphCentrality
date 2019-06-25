import sys
import heapq

def shortest_path(graph_list,index): #graph_list is list of lists of lists
  pq=[]
  short_list=[]
  parent_list=[]
  
  for i in range (len(graph_list)):#initialization
      short_list.append(10000)
      parent_list.append(-1)
      i=i+1
  short_list[index]=0
  parent_list[index]=-1
  
  for i in range (len(graph_list)):
    j=0
    for j in range(len(graph_list[i])):
        if(i==index ):
          heapq.heappush(pq,[graph_list[i][j][1],graph_list[i][j][0],i])
       


        j=j+1
    i=i+1
      
  while(not(len(pq)==0)):
      temp_list=heapq.heappop(pq)#weight,node,parent
      if(short_list[temp_list[1]]==10000): 
       short_list[temp_list[1]]=temp_list[0]
       parent_list[temp_list[1]]=temp_list[2]
       weight=temp_list[0]
       
      else:
         continue 
      

      for i in range (len(graph_list)):
        j=0
        for j in range(len(graph_list[i])):
          if(i==temp_list[1]):
            heapq.heappush(pq,[graph_list[i][j][1]+weight,graph_list[i][j][0],i])
         
          j=j+1
        i=i+1     
  
  return short_list

##file=open("graph.txt","r")
##lines=file.readlines()
##
##first_line=lines[0]
##first_line=first_line.split()
##number_nodes=int(first_line[0])
##number_edges=int(first_line[1])
##
##graph=[[] for j in range (number_nodes)]
##
##for i in range (number_edges):
##  my_line=lines[i+1]
##  my_line=my_line.split()
##  my_line=[int (i) for i in (my_line)]
##  graph[my_line[0]].append([my_line[1],my_line[2]])
##  graph[my_line[1]].append([my_line[0],my_line[2]])
##  i=i+1
##  
##s_list=shortest_path(graph,0)
##print(s_list)
  
##graph=[[] for i in range (4)]
##
##graph[0].append([2,10])
##graph[2].append([0,10])
##
##graph[1].append([0,1])
##graph[0].append([1,1])
##
##graph[0].append([3,5])
##graph[3].append([0,5])
##
##graph[3].append([1,1])
##graph[1].append([3,1])
##
##graph[2].append([3,4])
##graph[3].append([2,4])
##print(graph)
##s_list=shortest_path(graph,0)
##print(s_list)
    

    
