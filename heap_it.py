from math import floor
from typing import TypeVar

Q = TypeVar('Q', int, str, float, tuple)


class MinHeap(object):

    """MinHeap keeps minimum element available for pop in O(1) time.

    Instantiate a new, empty MinHeap:
        min_heap = MinHeap()

    Heapify an array of: int, float, str or tuple; Q:
        min_heap.min_heapify([Q])

    Insert a new value into heap:
        min_heap.insert(Q)

    Pop minimum value from heap:
        min_heap.pop()

    Peek minimum value in heap:
        min_heap.peek()

    Check heap is empty:
        is_empty()

    Clear heap of all data:
        clear()

    """

    def __init__(self):
        """MinHeap instantiated as an empty list with size 0."""
        self.heap = []
        self.size = 0

    def is_empty(self)-> bool:
        """Returns True if heap is empty.

        :return: bool
        """
        return self.size == 0

    def min_heapify(self, array: list)-> list:
        """Heapifies a given array in place.

        Sets self.heap as array.
        Calls _sift_down for each index capable of having a child the last of which we call last_parent.

        :param array: Array to heapify.
        :return: Heapified array.
        """
        self.heap = array
        self.size = len(array)

        # We only need to call _sift_down from the last parent to the start of the list as
        # higher indexes have children with indexes higher than len(array).
        last_parent = floor((self.size - 1) / 2)
        for i in range(last_parent, -1, -1):
            self._sift_down(i)
        return self.heap

    def pop(self)-> Q:
        """Returns and removes minimum value from MinHeap.

        Swaps minimum at root with value at end of list, pops min value from end of list and
        sifts new root down to correct position.

        :return: int, float, str, or tuple.
        """
        # Move min value to the end of list for easy popping, move last value to root.
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped = self.heap.pop()
        self.size -= 1

        # Sift the new root value down.
        self._sift_down(0)

        return popped

    def peek(self)-> Q:
        """Returns minimum value.

        :return: int, float, str or tuple.
        """
        return self.heap[0]

    def insert(self, data: Q)-> None:
        """Appends data to heap, increments size, and calls _sift_up with last index in heap.

        :param data: int, float, str or tuple.
        """
        self.heap.append(data)
        self.size += 1
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i: int)-> None:
        """Swaps data at heap[i] with its parent if parent is larger and calls _sift_up on parent index.

        :param i: int, an index of self.heap
        """
        parent = floor((i - 1) / 2)
        if self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._sift_up(parent)

    def _sift_down(self, i: int)-> None:
        """Sifts data down heap.

        Finds left and right children of heap[i]
        Checks if either child is smaller and swaps with the smallest.
        Calls _sift_down on index of swap.

        :param i: int, an index of self.heap
        """
        left = i * 2 + 1
        right = i * 2 + 2
        smallest = i

        # Check if children are within array. Find smallest value among the three.
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            # If we found a child with a larger value, swap it with the parent.
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]

            if smallest * 2 < self.size:
                # If children of biggest are within array, sift it down further.
                self._sift_down(smallest)

    def min_merge(self, min_heap_1: list, min_heap_2: list)-> list:
        """Merges two min_heaps.

        :param min_heap_1: A min_heap
        :param min_heap_2: A min_heap
        :return: A min_heap
        """
        new_min = min_heap_1 + min_heap_2
        return self.min_heapify(new_min)

    def min_meld(self, min_heap_1: 'MinHeap', min_heap_2: 'MinHeap')-> list:
        """Merges two MinHeap objects.

        :param min_heap_1: A MinHeap object
        :param min_heap_2: A MinHeap object
        :return: A min_heap
        """
        heap_1 = min_heap_1.heap
        heap_2 = min_heap_2.heap
        new_min = heap_1 + heap_2
        return self.min_heapify(new_min)

    def clear(self):
        """Clears heap of all data."""
        self.heap = []
        self.size = 0


class MaxHeap(object):

    """MaxHeap keeps maximum element available for pop in O(1) time.

    Instantiate a new, empty MaxHeap:
        max_heap = MaxHeap()

    Heapify an array of: int, float, str or tuple; Q:
        max_heap.max_heapify([Q])

    Insert a new value into heap:
        max_heap.insert(Q)

    Pop maximum value from heap:
        max_heap.pop()

    Peek maximum value in heap:
        max_heap.peek()

    Check heap is empty:
        is_empty()

    Clear heap of all data:
        clear()

    """

    def __init__(self)-> None:
        """MaxHeap instantiated as an empty list with size 0."""
        self.heap = []
        self.size = 0

    def is_empty(self)-> int:
        """Returns True if heap is empty.

        :return: bool
        """
        return self.size == 0

    def max_heapify(self, array: list)-> list:
        """Heapifies a given array in place.

        Sets self.heap as array.
        Calls _sift_down for each index capable of having a child the last of which we call last_parent.

        :param array: Array to heapify.
        :return: Heapified array.
        """
        self.heap = array
        self.size = len(self.heap)

        # We only need to call _sift_down from the last parent to the start of the list as
        # higher indexes have children with indexes higher than len(array).
        last_parent = floor((self.size - 1) / 2)
        for i in range(last_parent, -1, -1):
            self._sift_down(i)
        return self.heap

    def pop(self)-> list:
        """Returns and removes maximum value from MaxHeap.

        Swaps maximum at root with value at end of list, pops max value from end of list and
        sifts new root down to correct position.

        :return: int, float, str, or tuple.
        """
        # Move min value to the end of list for easy popping, move last value to root.
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped = self.heap.pop()
        self.size -= 1

        # Sift the new root value down.
        self._sift_down(0)
        return popped

    def peek(self)-> list:
        """Returns maximum value.

        :return: int, float, str or tuple.
        """
        return self.heap[0]

    def insert(self, data: Q)-> None:
        """Appends data to heap, increments size, and calls _sift_up with last index in heap.

        :param data: int, float, str or tuple.
        """
        self.heap.append(data)
        self.size += 1
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i: int)-> None:
        """Swaps data at heap[i] with its parent if parent is smaller and calls _sift_up on parent index.

        :param i: int, an index of self.heap
        """
        parent = floor((i - 1) / 2)
        if self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._sift_up(i)

    def _sift_down(self, i: int)-> None:
        """Sifts data down heap.

        Finds left and right children of heap[i]
        Checks if either child is larger and swaps with the largest.
        Calls _sift_down on index of swap.

        :param i: int, an index of self.heap
        """
        left = i * 2 + 1
        right = i * 2 + 2
        biggest = i

        # Check if children are within array. Find largest value among the three.
        if left < self.size and self.heap[left] > self.heap[biggest]:
            biggest = left
        if right < self.size and self.heap[right] > self.heap[biggest]:
            biggest = right
        if biggest != i:
            # If we found a child with a larger value, swap it with the parent.
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i]
            if biggest * 2 < self.size:
                # If children of biggest are within array, sift it down further.
                self._sift_down(biggest)

    def max_merge(self, max_heap_1: list, max_heap_2: list)-> list:
        """Merges two max_heaps.

        :param max_heap_1: A max_heap
        :param max_heap_2: A max_heap
        :return: A max_heap
        """
        new_max = max_heap_1 + max_heap_2
        return self.max_heapify(new_max)

    def max_meld(self, max_heap_1: 'MaxHeap', max_heap_2: 'MaxHeap')-> list:
        """Merges two MaxHeap objects.

        :param max_heap_1: A MaxHeap object
        :param max_heap_2: A MaxHeap object
        :return: A max_heap
        """
        heap_1 = max_heap_1.heap
        heap_2 = max_heap_2.heap
        new_max = heap_1 + heap_2
        return self.max_heapify(new_max)

    def clear(self):
        """Clears heap of all data."""
        self.heap = []
        self.size = 0


if __name__ == "__main__":
    pass
