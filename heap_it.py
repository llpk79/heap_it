from math import floor
from typing import TypeVar

Q = TypeVar('Q', int, str, float, tuple)


class MinHeap(list):

    """MinHeap keeps minimum element available for pop in O(1) time.

    Inherits from list.
    Overrides methods pop, insert and clear.

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

    def __init__(self) -> None:
        """MinHeap instantiated as an empty list with size 0."""
        self.size = 0
        super(MinHeap, self).__init__()

    def is_empty(self) -> bool:
        """Returns True if heap is empty.

        :return: bool
        """
        return self.size == 0

    def min_heapify(self, array: list) -> list:
        """Heapifies a given array in place.

        Sets self as array.
        Calls _sift_down for each index capable of having a child the last of which we call last_parent.

        :param array: Array to heapify.
        :return: Heapified array.
        """
        if not isinstance(array, list):
                raise TypeError(f'min_heapify accepts type: list. You have entered type: {type(array)}')
        else:
            self.clear()
            self += array
            self.size = len(self)

        # We only need to call _sift_down from the last parent to the start of the list as
        # higher indexes have children with indexes higher than len(array).
        last_parent = floor((self.size - 1) / 2)
        for i in range(last_parent, -1, -1):
            self._sift_down(i)
        return self

    def pop(self, **kwargs) -> Q:
        """Returns and removes minimum value from MinHeap or notification of empty heap.

        Swaps minimum at root with value at end of list, pops min value from end of list and
        sifts new root down to correct position.

        :return: int, float, str, or tuple.
        """
        # Move min value to the end of list for easy popping, move last value to root.
        if self:
            self[0], self[-1] = self[-1], self[0]
            popped = super(MinHeap, self).pop()
            self.size -= 1

            # Sift the new root value down.
            self._sift_down(0)

            return popped
        else:
            return 'MinHeap is empty.'

    def peek(self) -> Q:
        """Returns maximum value or notification of empty heap.

        :return: int, float, str or tuple.
        """
        if self:
            return self[0]
        else:
            return 'MinHeap is empty.'

    def insert(self, data: Q, **kwargs) -> None:
        """Appends data to heap, increments size, and calls _sift_up with last index in heap.

        :param data: int, float, str or tuple.
        """
        if not isinstance(data, int or float or tuple or str):
            raise TypeError(f'insert accepts types: int, float, tuple, or str. You have entered type: {type(data)}')
        else:
            super(MinHeap, self).append(data)
            self.size += 1
            self._sift_up(self.size - 1)

    def _sift_up(self, i: int) -> None:
        """Swaps data at heap[i] with its parent if parent is larger and calls _sift_up on parent index.

        :param i: An index of self
        """
        parent = floor((i - 1) / 2)
        if self[i] < self[parent]:
            self[i], self[parent] = self[parent], self[i]
        if parent > 0:
            self._sift_up(parent)

    def _sift_down(self, i: int) -> None:
        """Sifts data down heap.

        Finds left and right children of heap[i]
        Checks if either child is smaller and swaps with the smallest.
        Calls _sift_down on index of swap.

        :param i: An index of self
        """
        left = i * 2 + 1
        right = i * 2 + 2
        smallest = i

        # Check if children are within array. Find smallest value among the three.
        if left < self.size and self[left] < self[smallest]:
            smallest = left
        if right < self.size and self[right] < self[smallest]:
            smallest = right

        if smallest != i:
            # If we found a child with a larger value, swap it with the parent.
            self[i], self[smallest] = self[smallest], self[i]

            if smallest * 2 < self.size:
                # If children of smallest are within array, sift it down further.
                self._sift_down(smallest)

    def min_merge(self, min_heap_1: list, min_heap_2: list) -> list:
        """Merges two lists into a MinHeap.

        :param min_heap_1: A list
        :param min_heap_2: A list
        :return: A min_heap
        """
        new_min = min_heap_1 + min_heap_2
        return self.min_heapify(new_min)

    def clear(self) -> None:
        """Clears heap of all data."""
        self.size = 0
        super(MinHeap, self).clear()


class MaxHeap(list):

    """MaxHeap keeps maximum element available for pop in O(1) time.

    Inherits from list.
    Overrides methods pop, insert and clear.

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

    def __init__(self) -> None:
        """MaxHeap instantiated as an empty list with size 0."""
        self.size = 0
        super(MaxHeap, self).__init__()

    def is_empty(self) -> int:
        """Returns True if heap is empty.

        :return: bool
        """
        return self.size == 0

    def max_heapify(self, array: list) -> list:
        """Heapifies a given array.

        Sets self as array.
        Calls _sift_down for each index capable of having a child the last of which we call last_parent.

        :param array: Array to heapify.
        :return: Heapified array.
        """
        if not isinstance(array, list):
                raise TypeError(f'max_heapify accepts type: list. You have entered type: {type(array)}')
        else:
            self.clear()
            self += array
            self.size = len(self)

        # We only need to call _sift_down from the last parent to the start of the list as
        # higher indexes have children with indexes higher than len(array).
        last_parent = floor((self.size - 1) / 2)
        for i in range(last_parent, -1, -1):
            self._sift_down(i)
        return self

    def pop(self, **kwargs) -> Q:
        """Removes and returns maximum value from MaxHeap or notification of empty heap.

        Swaps maximum at root with value at end of list, pops max value from end of list and
        sifts new root down to correct position.

        :return: int, float, str, or tuple.
        """
        # Move min value to the end of list for easy popping, move last value to root.
        if self:
            self[0], self[-1] = self[-1], self[0]
            popped = super(MaxHeap, self).pop()
            self.size -= 1

            # Sift the new root value down.
            self._sift_down(0)
            return popped
        else:
            return 'MaxHeap is empty.'

    def peek(self) -> Q:
        """Returns maximum value or notification of empty heap.

        :return: int, float, str or tuple.
        """
        if self:
            return self[0]
        else:
            return 'MaxHeap is empty.'

    def insert(self, data: Q, **kwargs) -> None:
        """Appends data to heap, increments size, and calls _sift_up with last index in heap.

        :param data: int, float, str or tuple.
        """
        if not isinstance(data, int or float or tuple or str):
            raise TypeError(f'insert accepts types: int, float, tuple, or str. You have entered {type(data)}')
        else:
            super(MaxHeap, self).append(data)
            self.size += 1
            self._sift_up(self.size - 1)

    def _sift_up(self, i: int) -> None:
        """Swaps data at heap[i] with its parent if parent is smaller and calls _sift_up on parent index.

        :param i: An index of self
        """
        parent = floor((i - 1) / 2)
        if self[i] > self[parent]:
            self[i], self[parent] = self[parent], self[i]
        if parent > 0:
            self._sift_up(parent)

    def _sift_down(self, i: int) -> None:
        """Sifts data down heap.

        Finds left and right children of heap[i]
        Checks if either child is larger and swaps with the largest.
        Calls _sift_down on index of swap.

        :param i: An index of self
        """
        left = i * 2 + 1
        right = i * 2 + 2
        biggest = i

        # Check if children are within array. Find largest value among the three.
        if left < self.size and self[left] > self[biggest]:
            biggest = left
        if right < self.size and self[right] > self[biggest]:
            biggest = right
        if biggest != i:
            # If we found a child with a larger value, swap it with the parent.
            self[i], self[biggest] = self[biggest], self[i]
            if biggest * 2 < self.size:
                # If children of biggest are within array, sift it down further.
                self._sift_down(biggest)

    def max_merge(self, max_heap_1: list, max_heap_2: list) -> list:
        """Merges two lists into a MaxHeap.

        :param max_heap_1: A list
        :param max_heap_2: A list
        :return: A max_heap
        """
        new_max = max_heap_1 + max_heap_2
        return self.max_heapify(new_max)

    def clear(self) -> None:
        """Clears heap of all data."""
        self.size = 0
        super(MaxHeap, self).clear()


if __name__ == "__main__":
    pass
