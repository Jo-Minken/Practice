"""
Selection sort
O(N^2)

The algorithm divides the input list into two parts: 
a sorted sublist of items which is built up from left to right at the front (left) of the list 
and a sublist of the remaining unsorted items that occupy the rest of the list. 

Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. 
The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, 
exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

https://en.wikipedia.org/wiki/Selection_sort

"""

def selection_sort(_list):
    start_index = 0
    while start_index < len(_list):
        min_idx = start_index
        for idx in range(start_index + 1, len(_list)):
            if _list[idx] < _list[min_idx]:
                min_idx = idx

        tmp = _list[start_index]
        _list[start_index] = _list[min_idx]
        _list[min_idx] = tmp

        start_index += 1
        print(_list)

    print(_list)

selection_sort([100, 3, 44, 29, 5, 17])