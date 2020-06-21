def main():
    print(SummArrayNumbers([3, 5, 2, 10]))


def SummArrayNumbers(arr):
    """Sum array of numbers in recursive way

    Args:
        arr (array): numerical array

    Returns:
        int: sum of numbers
    """
    if len(arr) == 1:
        return arr[0]
    return arr[0] + SummArrayNumbers(arr[1:])


if __name__ == "__main__":
    main()
