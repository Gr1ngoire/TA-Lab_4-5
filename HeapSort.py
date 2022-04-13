from Sort import Sort


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


class HeapSort(Sort):

    def __init__(self):
        super().__init__()
        pass

    def sort(self, array):
        n = len(array)
        for i in range(n // 2, -1, -1):
            heapify(array, n, i)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapify(array, i, 0)

