def monotonic(x):

  return all(x[i] <= x[i+1] for  i in range(len(x)-1)) or all(x[i] >= x[i+1] for i in range(len(x)-1))



print(monotonic([1,1,1,3,3,4,3,2,4,2]))

