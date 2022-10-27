from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def BFS(self, s, e):
        visited = []
 
        
        queue = [] # FIFO queue for next vertice
 
        queue.append(s)
        visited.append(s)
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
            if s == e:
              break
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                 

def file_to_graph(file_name):
  g = Graph()
  f = open(file_name, "r")
  for x in f:
    y=1
    split_line = x.split(",")
    key = split_line[0]
    for y in range(1, len(split_line)):
      print(split_line[y])
      g.addEdge(key, split_line[y])
      y+=1

  return g

def main():
  # print("Hello world!")
  file_name = input("What file would you like to read from? ")
  graphed = file_to_graph(file_name)
  start = input("Where would you like to start? ")
  end = input("Where would you like to stop? ")
  print("Your path is ")
  graphed.BFS(start,end)
  
  
  
main()

# def file_to_graph(file_name):
#   g = Graph()
#   f = open(file_name, "r")
#   for x in f:
#     split_line = x.split(",")
#     key = split_line[0]
#     while x < len(split_line):
#       x+=1
#       g.add(key, split_line[x])

#   return g
# def map(file_name):
#   g = Graph()
#   f = open(file_name, "r")
#   for x in f:
#     split_line = x.split(",")
#     key = split_line[0]
#     while x < len(split_line):
#       x+=1
#       g.add(key, split_line[x])