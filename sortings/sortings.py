""" Main sorting algorithm """
import collections

def swap(massiv: list, pos_1: int, pos_2: int):
    tmp = massiv[pos_1]
    massiv[pos_1] = massiv[pos_2]
    massiv[pos_2] = tmp


def selected_sort(massiv: list) -> list:
    """Sorting selected: go on massiv and find min, then change min and 0->1->2 etc."""
    for j in range(len(massiv)):
        min_position = j
        min_elem = massiv[j]
        for i in range(j, len(massiv)):
            if massiv[i] < min_elem:
                min_position = i
        swap(massiv, j, min_position)
    return massiv


def insertion_sort(massiv: list) -> list:
    """Sorting insert: compare first elem and second, then third and massiv[first, second]"""
    for i in range(1, len(massiv)):
        j = i - 1
        while j >= 0 and massiv[j + 1] < massiv[j]:
            swap(massiv, j, j + 1)
            j -= 1
    return massiv


def heap_sort():
    pass



if __name__ == '__main__':
    print("Hello, world!")

