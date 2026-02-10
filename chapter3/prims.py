        

def create_adj_list(numbers: str) -> list[list[list[int]]]:
    retval = []
    u = []
    edge = []
    close_bracket_just_seen = False

    for i in range(len(numbers)):
        if numbers[i].isdigit():
            edge.append(int(numbers[i]))
            close_bracket_just_seen = False
        elif numbers[i] == ']' and close_bracket_just_seen == False:
            u.append(edge)
            edge = []
            close_bracket_just_seen = True
        elif numbers[i] == ']' and close_bracket_just_seen == True:
            retval.append(u)
            u = []
            close_bracket_just_seen = False
    return retval


def main():
    numbers = input("enter adj list: ")
    G = create_adj_list(numbers)


if __name__ == "__main__":
    main()