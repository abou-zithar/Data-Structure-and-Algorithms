def swap (a : int,b :int):
    a ,b = b,a
    return a,b



def insert(A: list[int],j :int):
    i =j-1
    while i >=0:
        if A[i] > A[i+1]:
            # A[i+1],A[i] = swap(A[i],A[i+1])
            A[i],A[i+1] = A[i+1],A[i]
        else:
            break
        i-=1

def insertionSort(A : list[int]):
    for j in range(1,len(A)):
        insert(A,j)
    return A
