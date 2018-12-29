def min_heapify(array,i):
    l = 2*i
    r = 2*i + 1
    if ((len(array)-1) >= l and array[l] < array[i]):
        smallest = l
    else:
        smallest = i
    if ((len(array)-1) >= r and array[r] < array[smallest]):
        smallest = r

    if (smallest != i):
        temp = array[smallest]
        array[smallest] = array[i]
        array[i] = temp
        # print(array)
        min_heapify(array,smallest)

def extract_min(array):
    if (len(array) - 1) < 1:
        print('Underflow heap')
        exit(-1111)
    min = array[1]
    len_heap = len(array) -1
    array[1] = array[len_heap]
    array.pop(len_heap)
    min_heapify(array,1)
    return min

# A = [9,6,5,0,8,2,7,1,3]
# dummy = ['dummy']
# A = dummy + A
# heap_size = len(A) - 1
#
# for i in range(math.floor(heap_size/2), 0, -1):
#     min_heapify(A,i)
# print(A)
#
# print(extract_min(A))
# print(A)

