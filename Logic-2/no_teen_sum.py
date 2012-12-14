def no_teen_sum(a, b, c):
  sum = 0
  for i in [a,b,c]:
    if i>12 and i<20:
      sum += fix_teen(i)
    else:
      sum += i
  return sum

def fix_teen(n):
  if n==15 or n==16:
    return n
  return 0