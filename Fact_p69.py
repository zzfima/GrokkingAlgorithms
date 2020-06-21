def main():
    print(FactCalc(4))
    print(FactCalcNonRec(4))


def FactCalcNonRec(n):
    """Calculate Factorial in Non recursive manner

    Args:
        n (int): number to find factorial

    Returns:
        int: factorial of an number
    """
    fct = 1
    for i in range(2, n + 1):
        fct *= i
    return fct

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
