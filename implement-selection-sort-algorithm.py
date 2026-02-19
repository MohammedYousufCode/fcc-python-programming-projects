#** start of main.py **

def selection_sort(array):
    n = len(array)
    # Outer loop: iterate over each position in the list
    for i in range(n):
        # Assume the current position is the minimum
        min_index = i
        # Inner loop: find the index of the smallest element in the unsorted portion
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array

    


#** end of main.py **

