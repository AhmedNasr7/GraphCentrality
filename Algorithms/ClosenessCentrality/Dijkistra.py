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

    

    
