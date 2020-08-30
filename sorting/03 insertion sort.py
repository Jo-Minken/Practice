"""
Insertion sort
O(N^2)

Insertion sort iterates, consuming one input element each repetition, 
and growing a sorted output list.

At each iteration, insertion sort removes one element from the input data, 
finds the location it belongs within the sorted list, 
and inserts it there. It repeats until no input elements remain.

https://en.wikipedia.org/wiki/Insertion_sort
"""

def insertion_sort(_list):
    for index in range(1, len(_list)):
        position = index
        temp_value = _list[index]
        while position > 0 and _list[position - 1] > temp_value: 
            _list[position] = _list[position - 1]
            position = position - 1

        _list[position] = temp_value
        print(_list)

    print(_list)

insertion_sort([100, 3, 44, 29, 5, 17])