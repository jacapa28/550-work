t = 1

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


def explore(G: list[list[int]], pre: list[int], post: list[int], u: int) -> None:
    global t
    pre[u] = t
    t += 1
    for v in G[u]:
        if pre[v-1] == -1:
            explore(G, pre, post, v-1)
    post[u] = t
    t += 1


def dfs(G: list[list[int]], pre: list[int], post: list[int]) -> None:
    global t
    for u in range(len(G)):
        if pre[u] == -1:
            explore(G, pre, post, u)

def back_edges(G: list[list[int]], pre: list[int], post: list[int]) -> int:
    count = 0
    for u in range(len(G)):
        for v in G[u]:
            if pre[v-1] < pre[u] and pre[u] < post[u] and post[u] < post[v-1]:
                count += 1
    return count


def main() -> str:
    numbers = input("enter the adjacency list G: ")
    G = create_adj_list(numbers)
    pre = [-1] * len(G)
    post = [-1] * len(G)
    dfs(G, pre, post)
    print(f"pre = {pre}\npost = {post}")
    print(f"back edges = {back_edges(G, pre, post)}")

if __name__ == "__main__":
    main()