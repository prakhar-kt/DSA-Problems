def reverse(x):

  strx = str(x)

  if strx[0] == '-' :
    result = strx[0] + strx[:0:-1]

  else:
    result = strx[:0:-1]

  return int(result)

print(reverse(-1234))
print(reverse(234))
