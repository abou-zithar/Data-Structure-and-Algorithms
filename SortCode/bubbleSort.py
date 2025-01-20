
def bubbleSort(arr : list[int]):
    for i in range(len(arr)):
        swap =False
        for j in range(len(arr)-i-1):

            if arr [j] > arr[j+1]:
               arr [j], arr[j+1]   =  arr[j+1]    ,arr [j]

               swap = True

        if not swap:
            break
    return arr