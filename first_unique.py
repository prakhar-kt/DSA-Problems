def get_first_unique(x:str):

  len_x = len(x)

  for ch in x:
    first_index = x.index(ch)
    last_index = x[::-1].index(ch)

    if (first_index + last_index) == (len_x - 1):
      return ch, first_index

    
    
print(get_first_unique("stringst mangoer"))


