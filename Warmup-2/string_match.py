def string_match(a, b):
  count = 0
  smallest = min(len(a), len(b))
  
  for i in range(smallest-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count