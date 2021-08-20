n = 5
graph = [[0 for _ in range(n+1)] for _ in range (n+1)]

def addEdge(start , end , weight , directed):

    graph[start][end] = weight

    if not directed :

        graph[end][start] = weight

graphdict = dict()
def addedgeAdg(start , end , weight , directed):

    if start not in graphdict:
        graphdict[start] = list()
    graphdict[start].append((end , weight))

    if not directed :
        if end not in graphdict:
                graphdict[end] = list()
    graphdict[end].append((start , weight))

if __name__ == '__main__':
    addEdge(0,1,2,False)
    addEdge(0,3,4,False)
    addEdge(0,4,1,False)
    addEdge(1,3,1,False)
    addEdge(3,4,2,False)

    for i in range (n+1):
        print(*graph[i])
   

    addedgeAdg(0,1,2,False)
    addedgeAdg(0,3,4,False)
    addedgeAdg(0,4,1,False)
    addedgeAdg(1,3,1,False)
    addedgeAdg(3,4,2,False)
    print()
    print(graphdict)
    print()

    for key , value in graphdict.items():
        print(f"{key} has neighbour  {value}" )
