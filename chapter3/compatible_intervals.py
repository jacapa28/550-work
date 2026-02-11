import math

def create_array(intervals: str) -> list[list[int]]:
    retval = []
    current_interval = []
    current_num = ""

    for i in range(len(intervals)):
        if intervals[i].isdigit():
            current_num += intervals[i]
        elif intervals[i] == ',' and len(current_num) > 0:
            current_interval.append(int(current_num))
            current_num = ""
        elif intervals[i] == ']':
            current_interval.append(int(current_num))
            current_num = ""
            retval.append(current_interval)
            current_interval = []

    return retval


def merge_sort_intervals(array: list[list[int]]) -> list[list[int]]:
    if len(array) == 1:
        return array
    k = math.floor(len(array)/2)
    A_L = merge_sort_intervals(array[0:k])
    A_R = merge_sort_intervals(array[k:])
    i = 0
    j = 0
    B = []
    while i <= k-1 and j <= len(array)-k-1:
        if A_L[i][1] <= A_R[j][1]:
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


def check_conflicting_intervals(interval1: list[int], interval2: list[int]) -> bool:
    if interval1[0] <= interval2[0] and interval1[1] >= interval2[0]:
        return False
    if interval1[0] <= interval2[1] and interval1[1] >= interval2[1]:
        return False
    return True


def earliest_end_time(array: list[list[int]]) -> list[list[int]]:
    S = [array[0]]
    for interval in array:
        if check_conflicting_intervals(interval, S[-1]):
            S.append(interval)
    return S


def main():
    intervals = input("enter intervals here: ")
    A = create_array(intervals)
    A = merge_sort_intervals(A)
    S = earliest_end_time(A)
    print(f"optimal intervals:\n{S}")


if __name__ == "__main__":
    main()