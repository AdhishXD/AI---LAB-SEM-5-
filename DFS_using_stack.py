class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.adj_list[src] = []
        self.adj_list[src].append(dest)


    def dfs(self, start):
        visited = set()
        stack = [start]

        print("DFS traversal:", end=' ')
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current, end=' ')
                visited.add(current)
                # Push neighbors in reverse to maintain left-to-right traversal
                for neighbor in reversed(self.adj_list.get(current, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)

def main():
    g = Graph()
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as 'src dest' (space-separated):")
    for _ in range(num_edges):
        src, dest = map(int, input().split())  # Convert to integers
        g.add_edge(src, dest)

    start_node = int(input("Enter starting node for DFS: "))
    g.dfs(start_node)

# Run the program
if __name__ == "__main__":
    main()
