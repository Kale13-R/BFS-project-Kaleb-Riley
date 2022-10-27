from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def BFS(self, s, e):
        visited = [] #store visited item
        path = []

        
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
 
            # check each indicie and see if it has been visited and add to queue
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                 

def file_to_graph(file_name):
  g = {
    
  }
  f = open(file_name, "r")
  for x in f:
    y=1 # starting point so that my code doesn't read the key pair twice
    split_line = x.split(",")
    # print(split_line)
    key = split_line[0]
    g[key] = []
    for y in range(1, len(split_line)):
      val = split_line[y]
      g[key].append(val.strip("\n"))
      # print("Maybe")
      # g[key] += key[y]
      # print(split_line[y])
    
      # g.addEdge(key, split_line[y])
      y+=1
  print(g)

  return g



def bfs(graph, start, end):
  # maintain a queue of paths
  queue = []
  # push the first path into the queue
  queue.append(start)
  while queue:
      # get the first path from the queue
      path = queue.pop(0)
      # get the last node from the path
      graph[key] 
      node = path[-1]
      # path found
      if node == end:
          return path
      # enumerate all adjacent nodes, construct a 
      # new path and push it into the queue
      for adjacent in graph.get(node, []):
          new_path = list(path)
          new_path.append(adjacent)
          queue.append(new_path)

def main():
  # print("Hello world!")
  file_name = input("What file would you like to read from? ")
  graphed = file_to_graph(file_name)
  start = input("Where would you like to start? ")
  end = input("Where would you like to stop? ")
  print("Your path is: ")
  bfs(graphed,start,end)
  # graphed.BFS(start,end)
  
  
  
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