#Time comlexity : O(E)
#space complexity : O(E)

class DirectedGraph:
    def __init__(self, adjacent_list = {}):
        self.adjacent_list = adjacent_list

    def add_vertex_edge(self, vertex1, vertex2):

        if not self.adjacent_list.get(vertex1):
            self.adjacent_list[vertex1] = []

        elif not self.adjacent_list.get(vertex2):   
            self.adjacent_list[vertex2] = []

        else:
            self.adjacent_list[vertex1] = vertex2

    def bfs(self, start_vertex, end_vertex):

        path = []
        all_shortest_path = []
        queue = [[start_vertex]]

        while queue: # time complexity : O(V)
            
            print(queue)
            path = queue.pop(0)
            print("\n")
            print(f" path ---> {path}")
            last_vertex = path[-1]


            if last_vertex == end_vertex:
                all_shortest_path.append(path)

                for inst_path in queue: # O(m) where m is the number of vertices in the path        
                    if inst_path[-1] == last_vertex:
                        all_shortest_path.append(inst_path)
                print(f"all shortest path from {start_vertex} to {end_vertex} : {all_shortest_path}") 

                return path

            for adjacent_vertex in self.adjacent_list[last_vertex]: # time complexity : O(E)
                
                print('edge_count')
                new_path = path.copy()
                new_path.append(adjacent_vertex)
                queue.append(new_path)        

if __name__ == "__main__":

    custom_graph = {'A':['B','C'],
                    'B':['D','G'],
                    'C':['D','E'],
                    'D':['F'],
                    'E':['F'],
                    'G':['F']}

    new_dgraph = DirectedGraph(custom_graph)
    
    #new_dgraph.add_vertex_edge()

    print(new_dgraph.bfs('A', 'F'))           

