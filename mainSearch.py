
from SortCode.bubbleSort import bubbleSort
from SearchCode.BinarySearch import binarySearch


array : list[int] = [7,4,10,8,3,1]

if __name__ == "__main__":
    sortedlist = bubbleSort(array)
    print(sortedlist)
    print(binarySearch(22 , sortedlist ))

    