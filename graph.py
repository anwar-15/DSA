class Graph:
    def __init__(self, adjacent_list = {}):
        self.adjacent_list = adjacent_list

    def add_vertex(self, vertex):
        if vertex not in self.adjacent_list.keys():
            self.adjacent_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):

        self.adjacent_list[vertex1].append(vertex2)
        self.adjacent_list[vertex2].append(vertex1)
        
    def remove_edge(self, vertex1, vertex2):
        
        if vertex1 in self.adjacent_list.keys() and vertex2 in self.adjacent_list.keys():
            try:
                self.adjacent_list[vertex1].remove(vertex2)
                self.adjacent_list[vertex2].remove(vertex1)

            except ValueError:
                print(f'There is no edge between {vertex1} and {vertex2}')

            return True

        return False

    def remove_vertex(self, vertex):
        
        if vertex in self.adjacent_list.keys():
            #self.adjacent_list[vertex] : this list gets modified after every iteration, hence
            #the copy of this list is stored separated for iteration.
            value_list = self.adjacent_list[vertex].copy()
            #python list should be copied using .copy(), otherwise it assigns diff name to the same list
            
            for vertex1 in value_list:
                self.remove_edge(vertex, vertex1)
            del self.adjacent_list[vertex]
            return True
        return False

    #time complexity of bfs is O(V+E) == max(V,E). space complexity is O(V)
    def bfs(self, vertex):    #O(V+E)
        #visted is {} taken for marking visited vertices
        #queue storing the visited vertices
        visited = {vertex : True}
        queue = [vertex]

        while queue:
            visited_vertex = queue.pop(0)
            print(f"visited vertex ---> {visited_vertex}")
            for adjacent_vertex in self.adjacent_list[visited_vertex]:
                
                if not visited.get(adjacent_vertex):
                    queue.append(adjacent_vertex)
                    visited[adjacent_vertex] = True

    #time complexity of dfs is O(V+E) == max(V,E). space complexity is O(V)
    def dfs(self, vertex):
        stack = [vertex]
        visited = {vertex : True}

        while stack:
            visited_vertex = stack.pop()
            print(f"visited vertex ---> {visited_vertex}")  
            for adjacent_vertex in self.adjacent_list[visited_vertex]:

                if not visited.get(adjacent_vertex):
                    stack.append(adjacent_vertex)
                    visited[adjacent_vertex] = True

    

                    



if __name__ == "__main__":

    new_graph = Graph()

    new_graph.add_vertex('A')
    new_graph.add_vertex('B')
    new_graph.add_vertex('C')
    new_graph.add_vertex('D')
    new_graph.add_vertex('E')
    new_graph.add_vertex('F')

    new_graph.add_edge('A','B')
    new_graph.add_edge('A','C')
    new_graph.add_edge('B','D')
    new_graph.add_edge('B','E')
    new_graph.add_edge('C','E')
    new_graph.add_edge('D','E')
    new_graph.add_edge('D','F')
    new_graph.add_edge('E','F')
    


    # new_graph.remove_edge('A','B')
    # print(new_graph.adjacent_list)
    # new_graph.remove_vertex('D')


    print(new_graph.adjacent_list)
    print("--------------bfs----------------------")

    new_graph.bfs('A')
    print("--------------dfs--------------------")

    new_graph.dfs('A')

    print("---------------bfs2-------------------")

    

    custom_dict =  {'A' : ['B','C'],
                    'B' : ['A','D','G'],
                    'C' : ['A', 'D', 'E'],
                    'D' : ['B', 'C', 'F'],
                    'E' : ['C', 'F'],
                    'F' : ['D', 'E'],
                    'G' : ['B', 'F']}

    demo_graph = Graph(custom_dict)                

    demo_graph.bfs('A')
    print(f"--------------dfs2------------------")

    demo_graph.dfs('A')                

