
# GRAPHS By Ericson Karanja.
# Graphs are a collection of node/ vertices connected by edges
# DFS traversal: a way of visiting all nodes by going as deep as possible along each branch before going back.
# BFS traversal: O(V + E) where V=vertices, E=edge

  from collections import defaultdict

class Graph:
    """Simple undirected graph using adjacency list"""
    
    def __init__(self):
        # key - node, value - list of neighboring nodes
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Add an undirected edge between nodes u and v"""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_iterative(self, start):
        """Iterative DFS using a stack - prints nodes in discovery order"""
        if start not in self.graph:
            return
        
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()              # LIFO → depth-first
            
            if node not in visited:
                visited.add(node)
                order.append(node)
                
                # Push neighbors in reverse to better match recursive order
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        # Print result
        print("DFS Iterative from 0:")
        print(" -> ".join(map(str, order)))

    def dfs_recursive(self, start):
        """Recursive DFS - prints nodes in discovery order"""
        visited = set()
        order = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            order.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        if start in self.graph:
            dfs(start)

        # Print result 
        print("DFS Recursive from 0:")
        print(" -> ".join(map(str, order)))

#Example usage

if __name__ == "__main__":
    g = Graph()
    
    # Edges that connect nodes 0, 1, 2, 3
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    # Execute both DFS versions
    g.dfs_iterative(0)

    print()  # empty line between outputs

    g.dfs_recursive(0)
	

