#Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    # your code here
    tour = []
    tour.append(graph[0][0])
    final = graph[0][1]
    graph.pop(0)
    while len(graph) > 0:
        l = len(graph)
        print(graph)
        for i in range(l):
            print(final)
            if(graph[i][0] == final):
                tour.append(final)
                final = graph[i][1]
                graph.pop(i)
                break
            if(graph[i][1] == final):
                tour.append(final)
                final = graph[i][0]
                graph.pop(i)
                break
        if(len(graph) == l):
            subtour = find_eulerian_tour(graph);
            try:
                dato = tour.index(subtour[0])
                tour.pop(dato)
                for i in range(len(subtour)):
                    tour.insert(dato + i, subtour[i])
            except ValueError:
                print("No es euleriano")                  
    
    tour.append(final)
    print(tour)
    if (tour[0] == tour[len(tour)-1]):
        return tour
    else:
        return "No es euleriano"
    
#print (find_eulerian_tour([(1, 2), (2, 3), (3, 1)]))
#print (find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]))
print (find_eulerian_tour([(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)]))
