def mountain_arr(arr):

  len_arr = len(arr)

  max_v = max(arr)
  ind_max = arr.index(max_v)
  print(max_v, ind_max)

  return (all(arr[i] >= arr[i-1] for i in range(1,ind_max))
          & all(arr[i] <= arr[i-1] for i in range(ind_max+1,len_arr)))


print(mountain_arr([1,3,4,5,7,4,4,3,3,2,1]))