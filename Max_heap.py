def max_heapify(array,i):
    l = 2*i
    r = 2*i + 1
    if ((len(array)-1) >= l and array[l] > array[i]):
        largest = l
    else:
        largest = i
    if ((len(array)-1) >= r and array[r] > array[largest]):
        largest = r

    if (largest != i):
        temp = array[largest]
        array[largest] = array[i]
        array[i] = temp
        max_heapify(array,largest)

def extract_max(array):
    if (len(array) - 1) < 1:
        print('Underflow heap')
        exit(-1111)
    max = array[1]
    len_heap = len(array) -1
    array[1] = array[len_heap]
    array.pop(len_heap)
    max_heapify(array,1)
    return max

# A = [9,6,5,0,8,2,7,1,3]
# dummy = ['dummy']
# A = dummy + A
# heap_size = len(A) - 1
#
# for i in range(math.floor(heap_size/2), 0, -1):
#     max_heapify(A,i)
# print(A)
#
# print(extract_max(A))
# print(A)






