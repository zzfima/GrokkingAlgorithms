def main():
    myArr = [3, 5, 8, 22, 27, 29, 32, 34, 35, 37, 38, 41, 43, 55, 56, 78]
    print(Search(myArr, 25))


def Search(arr, num):
    startIndex = 0
    endIndex = len(arr) - 1
    while startIndex <= endIndex:
        middleIndex = (endIndex + startIndex) // 2
        if num == arr[middleIndex]:
            return True
        elif num > arr[middleIndex]:
            startIndex = middleIndex + 1
        elif num < arr[middleIndex]:
            endIndex = middleIndex - 1
    return False


if __name__ == "__main__":
    main()
