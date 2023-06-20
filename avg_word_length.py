def avg_word_length(x: str) -> float:
  for p in ".,;:'?!":
    x = x.replace(p,"")

  listx = x.split()

  no_of_words = len(listx)

  total_sentence_length = len(x.replace(" ",""))

  return total_sentence_length/no_of_words


print(avg_word_length("I need to work very hard to learn more about algorithms in Python!"))


