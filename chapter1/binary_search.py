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

def binary_search(array: list[int], t: int) -> None:
    i, j = 0, len(array)-1
    while i <= j:
        m = math.floor((i+j)/2)
        print(m+1, end="")
        if array[m] == t:
            return 
        if array[m] < t:
            i = m + 1
            print(", ", end="")
        else:
            j = m - 1
            print(", ", end="")

def main() -> str:
    numbers = input("enter the array: ")
    t = input("enter t: ")
    array = create_array(numbers)
    binary_search(array,int(t))

if __name__ == "__main__":
    main()