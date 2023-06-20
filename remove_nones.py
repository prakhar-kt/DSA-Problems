def remove_nones(arr):

  for i in range(1,len(arr)):
    if arr[i] is None:
      arr[i] = arr[i-1]

  return arr


print(remove_nones([1,None,2,3,None,None,5,None]))