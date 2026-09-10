def bubble_sort(arr):
  n = len(arr)
  s = c = 0
  for i in range(n-1):
    swapped = False
    for j in range(n-1-i):
      c += 1
      if arr[j] > arr[j+1]:
        s += 1
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    if not swapped:
      break
  return " ".join(map(str, arr)), s, c
def insertion_sort(arr):
  n = len(arr)
  i = 1
  s = c = 0
  while i < n:
    x = arr[i]
    j = i - 1
    while j >= 0:
      c += 1
      if arr[j] > x:
        s += 1
        arr[j+1] = arr[j]
        j -= 1
      else:
        break
    arr[j+1] = x
    i += 1
  return " ".join(map(str, arr)), s, c
def compare(dataset):
  output = []
  bs_sort, bs_s, bs_c = bubble_sort(dataset[:])
  is_sort, is_s, is_c = insertion_sort(dataset[:])
  output.append(f"Bubble Sorted: {bs_sort}")
  output.append(f"Bubble Comparisons: {bs_c}")
  output.append(f"Bubble Swaps: {bs_s}")
  output.append(f"Insertion Sorted: {is_sort}")
  output.append(f"Insertion Comparisons: {is_c}")
  output.append(f"Insertion Shifts: {is_s}")
  if bs_c < is_c:
    output.append("Better Algorithm: Bubble Sort")
  elif bs_c > is_c:
    output.append("Better Algorithm: Insertion Sort")
  else:
    output.append("Better Algorithm: Both Equal")
  return output
def compare_bubble_insertion(random_data, sorted_data, reverse_data):
  output = []
  output.append("Sorting Performance Report")
  output.append("Random Dataset")
  output.extend(compare(random_data))
  output.append("Sorted Dataset")
  output.extend(compare(sorted_data))
  output.append("Reverse Dataset")
  output.extend(compare(reverse_data))
  return output