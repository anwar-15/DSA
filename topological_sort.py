#Time complexities : O(V + E)
#Space complexities : O(V + E)


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

    #resolving the depending vertices, and diving deep to the last of it.
    def topological_util(self, vertex, visited, stack):
        #once the vertex is visited, it is marked as True. 
        visited[vertex] = True

        #iterating through the depandant_vertex of the current vertex and diving deep.
        #example {A: [B,C]} the depandant vertices are B, C --> gets iterateed.
        # if the depandant vertex is already visited, it wont get into recursion. 
        for dependant_vertex in self.adjacent_list.get(vertex,[]):
            if not visited.get(dependant_vertex):
                self.topological_util(dependant_vertex, visited, stack)

        #the last visited vertex gets added to the stack first
        #here the last added vertex will be at top that is at stack[0]
        stack.insert(0,vertex)        

    #Driver method 
    def topological_sort(self):
        visited = {}
        stack = [] 

        #iterate through the vertices of the graph, one at a time
        for vertex in self.adjacent_list.keys():
            # if the vertices is already visited then it wont check for the depandant vertices
            if not visited.get(vertex):
                self.topological_util(vertex, visited, stack)

        print(stack)


if __name__ == "__main__":

    # custom_graph = {'A' : ['C'],
    #                 'B' : ['C','D'],
    #                 'C' : ['E'], 
    #                 'D' : ['F'],
    #                 'E' : ['H'],
    #                 'F' : ['G']}
    custom_graph = {0 : [],
                    1 : [0],
                    2 : [1],
                    3 : [1,7],
                    4 : [3],
                    5 : [3],
                    6 : [3],
                    7 : []}
    
    new_graph = Graph(custom_graph)
    new_graph.topological_sort()                
