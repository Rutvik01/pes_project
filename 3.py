from math import floor
def binary_search(Array, Search_Term):
    n = len(Array)
    L = 0
    R = n-1

    while L <= R:
        mid = floor((L+R)/2)
        if Array[mid] < Search_Term:
            L = mid + 1
        elif Array[mid] > Search_Term:
            R = mid - 1
        else:
            return mid
    return -1



A = [53,58,65,76,79,85,88,91,99,132,567]

term = 88
index = binary_search(A, term)
if index >= 0:
    print("{} is at index {}".format(A[index], index))
else:
    print("Search term not found")
