# Selection Sort

def SelectionSort(array : list[int]):
    size = len(array)
    for i in range(size):
        mIn = i
        for j in range(i + 1 ,size):
            if array[j] < array[mIn]:
                mIn = j
        
        if mIn != i:
            array[i],array[mIn] = array[mIn] ,array[i]
        
    return array

