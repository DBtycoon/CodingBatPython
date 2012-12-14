def lone_sum(a, b, c):
  if a==b:
    if b==c:
      return 0
    return c
  elif b==c:
    if a==b:
      return 0
    return a
  elif a==c:
    if c==b:
      return 0
    return b
  return a + b + c