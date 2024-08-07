# Slice Operator
* Basic Slicing
* Step Value
* Negative Indices
* Revers Slicing


## Basic Slicing:-
* You can use the colon (:) to create slices. The syntax is:
* a[start:stop]: Selects items from start through stop-1.
* a[start:]: Selects items from start to the end of the array.
* a[:stop]: Selects items from the beginning up to stop-1.
* a[:]: Creates a copy of the whole array.
* The key point is that the stop value represents the first value not in the selected slice.

## Step Value:-
* You can also specify a step value:
* a[start:stop:step]: Selects items from start through not past stop, with a step of step.
* For example, a[::2] selects every second item.

## Negative Indices:-
* You can use negative indices:
* a[-1]: Gets the last item in the array.
* a[-2:]: Gets the last two items.
* a[:-2]: Gets everything except the last two items.

## Revers Slicing:-
* To reverse the entire array, use:
* a[::-1]
* To reverse the first two items:
* a[1::-1]
* To get the last two items in reverse:
* a[:-3:-1]
* And to get everything except the last two items in reverse:
* a[-3::-1]
