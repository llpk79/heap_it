from heap_it import MaxHeap, MinHeap
from math import floor
from random import randint


def is_min_heap(array):
    array_len = len(array) - 1
    valid_heap = True
    for i in range(array_len // 2):
        left = i * 2 + 1
        right = i * 2 + 2
        if left > array_len:
            break
        if array[left] < array[i]:
            print(f'i is {i}, array[i] is {array[i]}, array[left] is {array[left]}. Array[i] must be < array[left]')
            valid_heap = False
        if right > array_len:
            break
        if array[right] < array[i]:
            print(f'i is {i}, array[i] is {array[i]}, array[right] is {array[right]}. Array[i] must be < array[right]')
            valid_heap = False
    for i in range(array_len, 0, -1):
        parent = floor((i - 1) / 2)
        if parent > len(array) - 1:
            break
        if array[parent] > array[i]:
            print(
                f'i is {i}, array[i] is {array[i]}, array[parent] is {array[parent]}. Array[i] must be > array[parent]')
            valid_heap = False
    return 'Heap is {}'.format('valid' if valid_heap else 'invalid')


def is_max_heap(array):
    array_len = len(array) - 1
    valid_heap = True
    for i in range(array_len // 2):
        left = i * 2 + 1
        right = i * 2 + 2
        if left > array_len:
            break
        if array[i] < array[left]:
            print(f'i is {i}, array[i] is {array[i]}, array[left] is {array[left]}. Array[i] must be > array[left]')
            valid_heap = False
        if right > array_len:
            break
        if array[i] < array[right]:
            print(f'i is {i}, array[i] is {array[i]}, array[right] is {array[right]}. Array[i] must be > array[right]')
            valid_heap = False
    for i in range(array_len, 0, -1):
        parent = floor((i - 1) / 2)
        if parent > len(array) - 1:
            break
        if array[parent] < array[i]:
            print(
                f'i is {i}, array[i] is {array[i]}, array[parent] is {array[parent]}. Array[i] must be > array[parent]')
            valid_heap = False
    return 'Heap is {}'.format('valid' if valid_heap else 'invalid')


def main():
    heap = MaxHeap()
    print(heap)
    print(heap.is_empty())
    heap.max_heapify([randint(-40, 40) for _ in range(40)])
    print(heap.heap)
    print(heap.size)
    print(heap.is_empty())
    print(is_max_heap(heap.heap))

    for _ in range(40):
        print(heap.pop())
    print(heap.is_empty())

    for _ in range(40):
        heap.insert(randint(-40, 40))
    print(heap.heap)

    heap1 = MaxHeap()
    heap1.max_heapify([randint(-40, 40) for _ in range(40)])
    print(is_max_heap(heap1.heap))

    merged = MaxHeap()
    merged.max_merge(heap.heap, heap1.heap)
    print(is_max_heap(merged.heap))
    print(merged.size)

    heap2 = MinHeap()
    heap2.min_heapify([randint(-50, 50) for _ in range(50)])
    print(is_min_heap(heap2.heap))
    print(heap2.size)

    heap3 = MinHeap()
    heap3.min_heapify([randint(-50, 50) for _ in range(50)])
    print(is_min_heap(heap3.heap))
    # print(heap3.size)

    merged1 = MinHeap()
    merged1.min_meld(heap2, heap3)
    print(is_min_heap(merged1.heap))
    print(merged1.size, merged1.heap)

    merged2 = MaxHeap()
    merged2.max_meld(heap, heap1)
    print(is_max_heap(merged2.heap))
    print(merged2.size, merged2.heap)

    tuple_heap = MaxHeap()
    tuples = [(randint(-40, 40), y) for _, y in zip(range(52), 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ')]
    tuple_heap.max_heapify(tuples)
    print(is_max_heap(tuple_heap.heap))
    print(tuple_heap.size, tuple_heap.heap)

    string_heap = MaxHeap()
    strings = [x for x in 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ']
    string_heap.max_heapify(strings)
    print(is_max_heap(string_heap.heap))
    print(string_heap.size, string_heap.heap)


if __name__ == "__main__":
    main()
