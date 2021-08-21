
def findCenter( edges: list[list[int]]):
    
    if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
        
        return edges[0][0]
    return edges[0][1]


if __name__  == '__main__':
    edges = [[1,2],[3,2],[4,2]]
    print(findCenter(edges))