

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
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if (array[i] + array[j+1] == t):
                print(f"i = {i+1}, j = {j+2}")
                return
    print("no two numbers add up to t.")
    return

def main() -> str:
    numbers = input("enter the array: ")
    t = input("enter t: ")
    array = create_array(numbers)
    twosum_alg(array,int(t))

if __name__ == "__main__":
    main()