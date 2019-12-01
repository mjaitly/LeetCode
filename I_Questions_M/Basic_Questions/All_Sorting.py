# n^2 for worst case
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # temp = arr[i]
                # arr[i] = arr[i+1]
                # arr[i+1] = temp
                swapped = True
    
    print(arr)


# n^2 for worst case
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    print(arr)


def insertion_sort(arr):
    pass


def merge_sort(arr):
    pass


def heap_sort(arr):
    pass


def quick_sort(arr):
    pass


if __name__ == "__main__":
    arr = [2, 3, 4, 6, 8, 1, 5, 9, 7, 10]
    # bubble_sort(arr)
    selection_sort(arr)
    # insertion_sort(arr)
    # merge_sort(arr)
    # heap_sort(arr)
    # quick_sort(arr)