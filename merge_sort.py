import math

def create_array(numbers: str) -> list[int]:
    retval = []
    currentnum = ""
    for char in numbers:
        if (char.isdigit()):
            currentnum += char
        if (char == ',' or char == ']'):
            retval.append(int(currentnum))
            currentnum = ""
    return retval

def merge_sort(array: list[int]) -> list[int]:
    if len(array) == 1:
        print(array)
        return array
    k = math.floor(len(array)/2)
    A_L = merge_sort(array[0:k])
    A_R = merge_sort(array[k:])
    i = 0
    j = 0
    B = []
    while i <= k-1 and j <= len(array)-k-1:
        if A_L[i] <= A_R[j]:
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
    print(B)
    return B

def main() -> str:
    numbers = input("enter the array: ")
    array = create_array(numbers)
    merge_sort(array)

if __name__ == "__main__":
    main()