def binarySearch(elem : int , arr : list[int]) -> int:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            raise ValueError("the array have to be sorted")
        
    left = 0
    right = len(arr)

    while left < right :
        mid = (left + right)//2

        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            left = mid +1
        else:
            right = mid -1
    return -1
