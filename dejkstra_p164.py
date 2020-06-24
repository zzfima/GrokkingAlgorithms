def main():
    tableOfDone = {}
    tableOfDone["A"] = False
    tableOfDone["B"] = False
    tableOfDone["C"] = False
    tableOfDone["D"] = False

    tableOfWeights = {}
    tableOfWeights["S"] = ("A", 5), ("B", 0)
    tableOfWeights["A"] = ("C", 15), ("D", 20)
    tableOfWeights["B"] = ("C", 30), ("D", 35)
    tableOfWeights["C"] = ("E", 20)
    tableOfWeights["D"] = ("E", 10)

if __name__ == "__main__":
    main()
