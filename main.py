def file_to_graph(file_name):
  g = {}
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



# def bfs(graph, start, end):
#   q = []
#   visited = [start]

#   q.append(start)

#   while q:
    
#     # I need this to look thorugh the starting key's value list and check if it contains the end. if it contains the end return the path. if not then check the value list's adjacent vals and see if it is in there until we have visited all nodes
  
#   # maintain a queue of paths
  
#   queue = []
#   # push the first path into the queue
#   queue.append(start)
#   while queue:
    
#     # get the first path from the queue
#     path = queue.pop(0)
#     # get the last node from the path
#     adj = graph[path]
#     # queue.append(adj)
#     print(adj)
#     node = adj[-1]
#     print(node)
#     # node = path[-1]
#     # path found
#     if node == end:
#         return path
#     # enumerate all adjacent nodes, construct a 
#     # new path and push it into the queue
#     for adjacent in graph.get(node, []):
#         new_path = list(path)
#         new_path.append(adjacent)
#         queue.append(new_path)
def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
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
  print(bfs(graphed,start,end))
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