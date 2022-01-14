from cmath import pi


array = [5,6,1,4,8,2,3,9,7]

def quick_sort(array, start, end):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if left <= end and array[left] <= array[pivot] :
            left += 1

        if right > start and array[right] >= array[pivot]:
            right -=1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

array = [5,6,1,4,8,2,3,9,7]
def pythonic_quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return pythonic_quick_sort(left) + [pivot] + pythonic_quick_sort(right)

print(pythonic_quick_sort(array))



