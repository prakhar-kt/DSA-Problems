def container_most_water(arr: list):

  max_area = 0

  n = len(arr)

  l = 0
  r = n-1

  container = [0,0]
  max_area = 0

  while l < r:
    area = min(arr[l],arr[r]) * (r-l)
    if area > max_area:
      max_area = area
      container[0] = arr[l]
      container[1] = arr[r]

    if arr[l] < arr[r]:
      l += 1
    else:
      r -= 1
    
    

  return container

print(container_most_water([1,8,6,2,5,4,6,3,7]))
        

      