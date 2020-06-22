def sumRec(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum(arr[1:])


def countRec(arr):
    if len(arr) == 1:
        return 1
    return 1 + countRec(arr[1:])


def maxRec(arr, max=None):
    if len(arr) == 0:
        return max
    if max == None:
        max = -(arr[0] ** 2)
    if arr[0] > max:
        max = arr[0]
    return maxRec(arr[1:], max)


def main():
    arr = [2, 2, 4, 4, 8]
    print(sumRec(arr))
    print(countRec(arr))
    print(maxRec(arr))


if __name__ == "__main__":
    main()
