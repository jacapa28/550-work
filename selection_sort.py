

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

def selection_sort(array: list[int]) -> None:
    for i in range(len(array)):
        m = i
        for j in range(i + 1, len(array)):
            if array[j] < array[m]:
                m = j
        temp = array[i]
        array[i] = array[m]
        array[m] = temp
        print(f"iteration {i+1}: {array}")

def main() -> str:
    numbers = input("enter the array: ")
    array = create_array(numbers)
    selection_sort(array)

if __name__ == "__main__":
    main()