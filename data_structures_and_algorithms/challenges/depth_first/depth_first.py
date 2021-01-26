class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, start_node, end_node, weight=1):
        start_node_check = False
        end_node_check = False

        for n in self.adjacency_list.keys():
            if not start_node_check:
                if str(n.value) == start_node:
                    start_node_check = True
            if not end_node_check:
                if str(n.value) == end_node:
                    end_node_check = True
            if start_node_check and end_node_check:
                break

        if start_node_check and end_node_check:
            for i in self.adjacency_list.keys():
                if str(i.value) == start_node:
                    self.adjacency_list[i].append([weight,end_node])
                    break
        else:
            return 'Invaild Input'

    def get_nodes(self):
        if len(list(self.adjacency_list.keys())) > 0:
            start = list(self.adjacency_list.keys())[0].value
            return self.bfs(start)
        else:
            return 'Graph is empty'

    def get_neighbours(self, node):
        if len(list(self.adjacency_list.keys())) > 0:

            for i in self.adjacency_list.keys():
                if str(i.value) == node:
                    return self.adjacency_list[i]
            
            return 'Node does not exist'
        else:
            return 'Graph is empty'

    def size(self):
        if len(list(self.adjacency_list.keys())) > 0:
            start = list(self.adjacency_list.keys())[0].value
            return len(self.bfs(start))
        else:
            return 'Graph is empty'

    def bfs(self, start_node):
        nodes=set([])
        temp = [start_node]
        values = []

        while len(temp) >0:
            front_node = temp.pop(0)
            nodes.add(front_node)

            for i in self.adjacency_list.keys():
                if str(i.value) == str(front_node):
                    values.append(self.adjacency_list[i])
                    break

            if len(values) > 0:
                for n in values[0]:
                    if n[1] not in nodes:
                        temp.append(n[1])
                        nodes.add(n[1])
            else:
                return False
        return nodes
    
    def path_in_two(self,node1,node2):
        list1 = self.get_neighbours(node1)
        list2 = self.get_neighbours(node2)

        if type(list1) != list or type(list2) != list:
            return "Invaild Input"
        else:
            check = False
            for i in list1:
                if i[1] == node2:
                    check = True  
            if check == False:
                for j in list2:
                    if j[1] == node1:
                        check = True
            
            return check


def DFS(graph_sample):
    result=[]
    s = list(graph_sample.adjacency_list.keys())[0].value
    visited = {}

    for i in graph_sample.adjacency_list:
        visited[i.value] = False
    
    stack = []
    stack.append(s)

    while (len(stack)):
        s = stack[-1]
        stack.pop()
        if (not visited[s]):
            result.append(s)
            visited[s] = True
        for node in graph_sample.get_neighbours(s): 
            if (not visited[node[1]]): 
                stack.append(node[1])

    return result

if __name__=='__main__':
    test1 = Graph()
    test1.add_node('a')
    test1.add_node('b')
    test1.add_node('c')
    test1.add_node('d')
    test1.add_node('x')
    test1.add_edge('a','b',4)
    test1.add_edge('a','d',9)
    test1.add_edge('a','c',3)
    test1.add_edge('b','a',4)
    test1.add_edge('c','a',3)
    test1.add_edge('c','d',6)
    test1.add_edge('d','a',9)
    test1.add_edge('d','b',5)
    test1.add_edge('d','c',6)
    
    print(DFS(test1))
