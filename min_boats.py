def min_boats(arr, max_w):

  arr.sort()

  len_arr = len(arr)

  if len_arr % 2 == 0:
    n = int(len_arr / 2)
    boat_cnts = 0
    print("even")
  else: 
    n = int((len_arr - 1)/2)
    boat_cnts = 1
    len_arr = len_arr - 1
    print("odd")

  

  for i in range(n):
    if arr[i] >= max_w:
      boat_cnts +=1
      print("hello",boat_cnts)
      continue
      
      
    
    else:
      for j in range(len_arr-1,n-1,-1):
        if (arr[i] + arr[j]) > max_w:
          boat_cnts +=1
          print("hi", boat_cnts, i, j)
          
          
          continue 
        else:
          boat_cnts +=1
          print("hola",boat_cnts, i, j)
          len_arr = len_arr -1
          break

  return boat_cnts

print(min_boats([3,2,2,1,4,2,3],6))

# [1,2,2,2,3,3,4]

  
      

  

  