def linear_search(arr, target):
    c = 0
    for i in range(len(arr)):
        c += 1
        if arr[i] == target:
            return i, c
    return -1, c

def binary_search(arr, target):
    low = c = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        
        elem = arr[mid]
        c += 1
        if elem == target:
            if elem in arr[:mid]:
                high = mid - 1
                continue
            else:
                return mid, c
        if elem < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, c

def compare_search_algorithms(arr, target):
    i1, c1 = linear_search(arr, target)
    i2, c2 = binary_search(arr, target)
    output = []
    output.append("Search Comparison Report")
    output.append("Linear Search")
    output.append(f"Index: {i1}")
    output.append(f"Comparisons: {c1}")
    output.append("Binary Search")
    output.append(f"Index: {i2}")
    output.append(f"Comparisons: {c2}")
    if c1 > c2:
        output.append("Better Algorithm: Binary Search")
    else:
        output.append("Better Algorithm: Linear Search")
    return output

def run():
    arrays = [[1,2,3,4,5],[-10,-5,0,5,10],[100,50,0,-50,-100]]
    targets = [1,10,0]
    for i in range(len(arrays)):
        arr = arrays[i]
        target = targets[i]
        out = compare_search_algorithms(arr,target)
        print(f"Case {i+1}")
        for output in out:
            print(output)
        print(f"{'-'*30}")
run()