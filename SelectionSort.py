def main():
    print("Selection sort")
    unsortedArray = [6, 3, 8, 1, 0, 2, 7]
    print(SelectionSort(unsortedArray))


def SelectionSort(unsortedArray):
    """Selection sort algortihm

    Args:
        unsortedArray (array): unsorted numeric array

    Returns:
        array: sorted numeric array
    """    
    sortedArray = []
    while len(unsortedArray) != 0:
        maxIndex = FindMax(unsortedArray)
        sortedArray.append(unsortedArray.pop(maxIndex))
    return sortedArray
    

def FindMax(unsortedArray):
    """Find max number in array

    Args:
        unsortedArray (array): unsorted numeric array

    Returns:
        int: max number
    """    
    maxIndex = 0
    maxVal = unsortedArray[maxIndex]
    for i in range(0, len(unsortedArray)):
        if unsortedArray[i]> maxVal:
            maxVal = unsortedArray[i]
            maxIndex = i
    return maxIndex

if __name__ == "__main__":
    main()
