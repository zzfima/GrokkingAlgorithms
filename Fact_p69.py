def main():
    print(FactCalc(4))


def FactCalc(n):
    """Calculate Factorial

    Args:
        n (int): number to find factorial

    Returns:
        int: factorial of an number
    """
    if n == 1:
        return 1
    return n * FactCalc(n - 1)


if __name__ == "__main__":
    main()
