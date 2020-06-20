def main():
    print("Selection sort")

    unsortedArray = [6, 3, 8, 1, 0, 2, 7]
    sortedArray = []

    while len(unsortedArray) != 0:
        maxIndex = 0
        maxVal = unsortedArray[maxIndex]
        for i in range(0, len(unsortedArray)):
            if unsortedArray[i]> maxVal:
                maxVal = unsortedArray[i]
                maxIndex = i
        sortedArray.append(unsortedArray.pop(maxIndex))
    
    print(sortedArray)


if __name__ == "__main__":
    main()
