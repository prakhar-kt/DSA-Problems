def prime_numbers(n):
  prime_numbers = []
  for i in range(n):
    if i > 1:
      for j in range(2,i):
        if (i % j) == 0:
          break
    
      
      else:
        prime_numbers.append(i)

  return prime_numbers

print(prime_numbers(10))