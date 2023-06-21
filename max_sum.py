def max_sum(arr, window):

  n = len(arr)
  k = window

  if n <= k:
    print("Window is greater than array length")
    return None

  max_sum = float("-inf")

  for i in range(0, n-k+1):
    current_sum = 0
    for j in range(0,k):
      current_sum += arr[i+j]

    max_sum = max(current_sum, max_sum)

  return max_sum

print(max_sum([10,-20,40,70,80],2))
  

  

  