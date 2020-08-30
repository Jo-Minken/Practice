"""
Bubble sort
O(N^2)

sometimes referred to as sinking sort, 
is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements and swaps them if they are in the wrong order. 

The pass through the list is repeated until the list is sorted.

https://en.wikipedia.org/wiki/Bubble_sort
"""

def bubble_sort(_list):
    end_index = len(_list)
    while end_index > 0:
        for idx in range(0, end_index - 1):
            if _list[idx] > _list[idx + 1]:
                # switch the elements
                tmp = _list[idx + 1]
                _list[idx + 1] = _list[idx]
                _list[idx] = tmp

        end_index -= 1
        print(_list)

    print(_list)

bubble_sort([100, 3, 44, 29, 5, 17])