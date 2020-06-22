def QuickSort(arr):
    if len(arr) < 2:
        return arr
    return QuickSort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + QuickSort([x for x in arr[1:] if x > arr[0]])


def main():
    arr = [8, 1, 5, 2, 3, 7, 9, 0]
    print(QuickSort(arr))


if __name__ == "__main__":
    main()
