def insertion_sort(lst):
    counter_operations = 0
    for i in range(len(lst)):
        key = lst[i]
        j = i - 1
        while j > -1 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
            counter_operations += 1

        lst[j + 1] = key
    return counter_operations


def selection_sort(lst):
    counter_operations = 0
    for i in range(len(lst)):
        min_elem_indx = i
        for j in range(i+1, len(lst)):
            if lst[min_elem_indx] > lst[j]:
                min_elem_indx = j
            counter_operations += 1
            
        lst[i], lst[min_elem_indx] = lst[min_elem_indx], lst[i]
    return counter_operations


def merge_sort(lst):
    counter_operations = 0
    if len(lst) > 1:
        mid = len(lst)//2
        L = lst[:mid]
        R = lst[mid:]

        merge_sort(L)
        merge_sort(R)
  
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
                counter_operations += 1
            else:
                lst[k] = R[j]
                j += 1
                counter_operations += 1
            k += 1

        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
            counter_operations += 1
  
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
            counter_operations += 1

    return counter_operations


def shell_sort(lst):
    counter_operations = 0
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            var = lst[i]
            counter_operations += 1
            while j >= gap and lst[j - gap] > var:
                lst[j] = lst[j - gap]
                j -= gap
                counter_operations += 1

            lst[j] = var
        gap = gap // 2
    return counter_operations


if __name__ == '__main__':
    a = [1,5,2,7,3,5,3,4,5,6,7]
    print(shell_sort(a))