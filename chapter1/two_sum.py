

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

def twosum_alg(array: list[int], t: int) -> None:
    i, j = 0, len(array)-1
    while i <= j:
        if array[i] + array[j] == t:
            print(f"i = {i+1}; j = {j+1}")
            return
        if array[i] + array[j] < t:
            i += 1
        else:
            j -= 1
    print(f"no two numbers add up to {t}.")

def main() -> str:
    numbers = input("enter the array: ")
    t = input("enter t: ")
    array = create_array(numbers)
    twosum_alg(array,int(t))

if __name__ == "__main__":
    main()