from math import floor

def make_simple_array(array: str) -> list[int]:
    retval = []
    current_num = ""

    for i in range(len(array)):
        if array[i].isdigit():
            current_num += array[i]
        if array[i] == ',' or array[i] == ']':
            retval.append(int(current_num))
            current_num = ""
    return retval


def make_combined_array(v: list[int], w: list[int]):
    retval = []

    for i in range(len(v)):
        retval.append([v[i], w[i], i])
    return retval


def merge_sort_fractions(array: list[list[int]]) -> list[list[int]]:
    if len(array) == 1:
        return array
    k = floor(len(array)/2)
    A_L = merge_sort_fractions(array[0:k])
    A_R = merge_sort_fractions(array[k:])
    i = 0
    j = 0
    B = []
    while i <= k-1 and j <= len(array)-k-1:
        if A_L[i][0]/A_L[i][1] >= A_R[j][0]/A_R[j][1]:
            B.append(A_L[i])
            i += 1
        else:
            B.append(A_R[j])
            j += 1
    if i > k-1:
        for m in range(j, len(array)-k):
            B.append(A_R[m])
    else:
        for m in range(i, k):
            B.append(A_L[m])
    return B


def knapsack(v_w: list[list[int]], capacity: int) -> list[int]:
    x = [0] * len(v_w)
    spent_weight = 0
    i = 1

    for item in v_w:
        if item[1] < capacity-spent_weight:
            x[item[2]] = 1
            print(f"{i}: for item at index {item[2]+1}, get fraction: 1/1")
            spent_weight += item[1]
        elif capacity-spent_weight > 0:
            x[item[2]] = (capacity-spent_weight)/item[1]
            print(f"{i}: for item at index {item[2]+1}, get fraction: {capacity-spent_weight}/{item[1]}")
            spent_weight += item[1]
        i += 1

    return x


def main():
    v_string = input("enter v: ")
    v = make_simple_array(v_string)

    w_string = input("enter w: ")
    w = make_simple_array(w_string)

    capacity = int(input("enter B: "))

    v_w = make_combined_array(v, w)
    v_w = merge_sort_fractions(v_w)

    x = knapsack(v_w, capacity)


if __name__ == "__main__":
    main()

