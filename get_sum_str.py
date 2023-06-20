def get_sum(x1: str, x2: str):
  n1, n2 = 0,0

  m1 = 10**(len(x1)-1)
  m2 = 10**(len(x2)-1)

  for i in x1:
    n1 += (ord(i) - ord("0")) * m1
    m1 = m1 // 10

  for i in x2:
    n2 += (ord(i) - ord("0")) * m2
    m2 = m2 // 10


  return n1 + n2


print(get_sum('1834', '231'))


