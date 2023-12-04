
class WeightedGraph:
    def __init__(self, adjacent_list = {}):
        self.adjacent_list = adjacent_list
        self.path_length = {}
        self.visited = {}
        self.parent_vertex = {}

    def add_vertex_edge(self, vertices, edges):

        for vertex in vertices:
            if not self.adjacent_list.get(vertex):
                self.adjacent_list[vertex] = {}


        for (vertex1, vertex2), weight in edges.items():

            if not edges.get(vertex1):
                self.adjacent_list[vertex1][vertex2] = weight
                self.adjacent_list[vertex2][vertex1] = weight

    def add_vertex(self, vertex1, vertex2, weight):

        for vertex in vertices:
            if not self.adjacent_list.get(vertex):
                self.adjacent_list[vertex] = {}

        self.adjacent_list[vertex1][vertex2] = weight
        self.adjacent_list[vertex2][vertex1] = weight        


    def set_default_path(self, vertices, source_vertex):

        for vertex in vertices:
            self.path_length[vertex] = float('inf')

        self.path_length[source_vertex] = 0

        self.path_length = dict(sorted(self.path_length.items(), key = lambda x:x[1]))

    def dijkstra_algo(self):

        for current_vertex in self.path_length.keys():
            if not self.visited.get(current_vertex):
                for destination_vertex in self.adjacent_list.get(current_vertex):

                    if not self.visited.get(destination_vertex):
                        min_weight = min(self.path_length[destination_vertex], self.path_length[current_vertex] + self.adjacent_list[current_vertex][destination_vertex])
                        
                        if min_weight < self.path_length[destination_vertex]:

                            self.path_length[destination_vertex] = min_weight
                            self.parent_vertex.update({destination_vertex : current_vertex})

                            #print(self.parent_vertex)

                    self.visited.update({current_vertex : True})                     


if __name__ == "__main__":

    new_graph = WeightedGraph()

    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    #edges = {('A','B') : 2, ('A', 'D') : 8, ('B', 'D') : 5, ('B', 'E') : 6, ('C', 'E') : 9, ('C', 'F') : 3, ('D', 'E') : 3, ('D', 'F') : 2, ('E', 'F') : 1}
    
    #new_graph.add_vertex_edge(vertices, edges)

    new_graph.add_vertex('A','B',2)
    new_graph.add_vertex('A','C',5)
    new_graph.add_vertex('B','C',6)
    new_graph.add_vertex('B','D',1)
    new_graph.add_vertex('B','E',3)
    new_graph.add_vertex('C','F',8)
    new_graph.add_vertex('D','E',4)
    new_graph.add_vertex('E','G',9)
    new_graph.add_vertex('F','G',7)


    new_graph.set_default_path(vertices, 'A')

    new_graph.dijkstra_algo()
    print(new_graph.adjacent_list)
    print(new_graph.path_length)
    print(new_graph.parent_vertex)



#    

