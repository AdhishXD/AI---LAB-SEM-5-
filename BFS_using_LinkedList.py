class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return value

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.adj_list[src] = []
        self.adj_list[src].append(dest)


    def bfs(self, start):
        visited = set()
        queue = LinkedListQueue()
        queue.enqueue(start)
        visited.add(start)

        print("BFS traversal:", end=' ')
        while not queue.is_empty():
            current = queue.dequeue()
            print(current, end=' ')

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)


def main():
    g = Graph()
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as 'src dest' (space-separated):")
    for _ in range(num_edges):
        src, dest = map(int, input().split())  # Convert to integers
        g.add_edge(src, dest)

    start_node = int(input("Enter starting node for BFS: "))  # Convert to integer
    g.bfs(start_node)


if __name__ == "__main__":
    main()
