dataarray = [0, 3, 4, 56, 67, 44, 43, 32, 31, 345, 45, 6, 54, 1]


def insertionsort(dataarray):
    for i in range(1, len(dataarray)):
        value = dataarray[i]
        y = i - 1

        while y >= 0 and dataarray[y] > value:
            dataarray[y + 1] = dataarray[y]
            y = y - 1

        dataarray[y + 1] = value

    return dataarray


def outputArray(dataarray):
    output = ""
    for i in dataarray:
        output = output + str(i) + " "
    print(output)


outputArray(dataarray)
sorted_array = insertionsort(dataarray)
outputArray(sorted_array)


def binarysearch(dataarray,itemtofind):
    low= 0
    high = len(dataarray) - 1
    found = False

    while low <= high and not found:
        mid = (low + high) // 2
        if dataarray[mid] == itemtofind:
            found = True
        else:
            if itemtofind < dataarray[mid]:
                high = mid - 1
            else:
                low = mid + 1
                return mid 
        return -1
  

    def bubble_sort(arr):
     n = len(arr)
     for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:        # optimisation: stop early if already sorted
            break
     return arr
