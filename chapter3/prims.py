        

def create_adj_list(numbers: str) -> list[list[list[int]]]:
    retval = []
    u = []
    edge = []
    current_num = ""
    close_bracket_just_seen = False

    for i in range(len(numbers)):
        if numbers[i].isdigit():
            current_num += numbers[i]
            close_bracket_just_seen = False
        elif numbers[i] == ',' and close_bracket_just_seen == False:
            edge.append(int(current_num))
            current_num = ""
            close_bracket_just_seen = False
        elif numbers[i] == ']' and close_bracket_just_seen == False:
            edge.append(int(current_num))
            current_num = ""
            u.append(edge)
            edge = []
            close_bracket_just_seen = True
        elif numbers[i] == ']' and close_bracket_just_seen == True:
            retval.append(u)
            u = []
    return retval


def prims(G: list[list[list[int]]]) -> list[list[int]]:
    S = [False] * len(G)
    S[0] = True
    F = []

    for i in range(len(G)-1):
        lightest_edge = [-1, -1, -1]
        for j in range(len(S)):
            if S[j] == True:
                for u in G[j]:
                    if (u[1] < lightest_edge[2] or lightest_edge[2] == -1) and S[u[0]-1] != True:
                        lightest_edge[0] = j
                        lightest_edge[1] = u[0]-1
                        lightest_edge[2] = u[1]
        S[lightest_edge[1]] = True
        new_edge = [lightest_edge[0]+1, lightest_edge[1]+1, lightest_edge[2]]
        F.append(new_edge)

    return F


def main():
    numbers = input("enter adj list: ")
    G = create_adj_list(numbers)
    F = prims(G)
    print(f"minimum spanning tree edges:\n{F}")


if __name__ == "__main__":
    main()