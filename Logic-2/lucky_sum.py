def lucky_sum(a, b, c):
  seq=[a,b,c]
  if 13 in seq:
    seq=seq[:seq.index(13)]
  sum = 0
  for i in seq:
    sum += i
  return sum