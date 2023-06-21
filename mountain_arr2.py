def mountain_arr2(arr):

  len_arr = len(arr)
  

  if len_arr < 3:
    return False

  i = 1

  while (i < len_arr and arr[i] >= arr[i-1]):
    i += 1
  
  if (i == 1 or i == len_arr):
    return False

  

  while (i < len_arr and arr[i] <= arr[i-1]):
    
    i += 1
    
  

  return i == len_arr


print(mountain_arr2([1,3,4,4,5,7,4,3,2,1]))