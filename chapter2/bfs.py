class Node:

    def __init__(self, value: int):
        self.value = value
        self.next = None


class Queue:

    def __init__(self, head: Node):
        self.head = head
        self.tail = head
        self.size = 1

    def dequeue(self) -> int:
        temp = self.head.value
        self.head = self.head.next
        self.size -= 1
        return temp

    def enqueue(self, new_node: Node):
        if (self.size == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


def create_array(numbers: str) -> list[int]:
    retval = []
    current_num = ""
    for char in numbers:
        if (char.isdigit()):
            current_num += char
        if (char == ','):
            if (current_num != ""):
                retval.append(int(current_num))
            current_num = ""
        if (char == ']'):
            if (current_num != ""):
                retval.append(int(current_num))
            return retval
    return []


def create_adj_list(numbers: str) -> list[list[int]]:
    retval = []
    for i in range(len(numbers)):
        if (numbers[i] == '['):
            retval.append(create_array(numbers[i+1:]))
    return retval


def bfs(G: list[list[int]], S: int) -> list[int]:
    distances = [-1] * len(G)
    distances[S-1] = 0
    q = Queue(Node(S))
    while q.size >= 1:
        u = q.dequeue()
        for v in G[u-1]:
            if (distances[v-1] == -1):
                distances[v-1] = distances[u-1]+1
                q.enqueue(Node(v))
    return distances


def main() -> str:
    numbers = input("enter the adjacency list G: ")
    G = create_adj_list(numbers)
    S = int(input("enter the starting vertex: "))
    distances = bfs(G, S)
    print(f"distances = {distances}")

if __name__ == "__main__":
    main()