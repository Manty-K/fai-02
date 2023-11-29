from go import go
from distance import distance,road
graph = [
    ('A','B',21),
    ('B','C',40),
    ('C','D',20),
    ('B','E',44),

]

def robot(graph):
    src = input('Enter the the Source: ')
    dst = input('Enter the the Destination: ')

    if not road(src,dst,graph):
        print(f'There does not exist a road from {src} to {dst}')
        return

    pathString = ''
    for p in go(src,dst,graph)[0]:
        pathString = pathString + ' ' +p + ' -> '
    pathString = pathString[:-3]
    print(f'Robot will take path {pathString}')
    print(f'Total distance to be travelled is {distance(src,dst,graph)[0]}.')

robot(graph)

# print(road('A','C',graph))
# print(go('A','C',graph))
# print(distance('A','C',graph))




