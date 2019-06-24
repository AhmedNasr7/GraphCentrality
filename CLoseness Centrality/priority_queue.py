import sys

class priority_queue():
    def __init__(self):
        self.queue=[]
   
    def quick_sort(self,start,end):
        
        if(start>=end):
            return
        
        pivot=self.queue[start]
        i=start+1
        j=end
        
        while(i<=j):
          while(i<=end and self.queue[i][1]<=pivot[1]):
              i=i+1
          while(j>=start and self.queue[j][1]>pivot[1]):
              j=j-1
              
          if(i<j):
              temp=self.queue[i]
              self.queue[i]=self.queue[j]
              self.queue[j]=temp
              
        temp=self.queue[start]
        self.queue[start]=self.queue[j]
        self.queue[j]=temp
        
        self.quick_sort(start,j-1)
        self.quick_sort(i,end)
        
    def add_item(self,node,weight,parent):
        self.queue.append([node,weight,parent])
        self.quick_sort(0,len(self.queue)-1)
    def remove_item(self):
        
        list1=self.queue.pop(0)
        return list1
                    
    def print_queue(self):
        for i in range(len(self.queue)):
            print(self.queue[i])
    def is_empty(self):
        if(len(self.queue)==0):
         return True;
    
##list1=priority_queue()
##list1.add_item(0,5)
####list1.add_item(1,2)
####list1.add_item(3,6)
##list1.print_queue()
##print("next")
##list2=list1.remove_item()
####list1.print_queue()
####print("next")
##print(list2)
##print("fg")
##print(list1.is_empty())

        
        
