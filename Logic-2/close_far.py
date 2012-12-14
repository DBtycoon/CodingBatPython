def close_far(a, b, c):
  if abs(a-b)<2:
    if abs(a-c)>1 and abs(b-c)>1:
      return True
    return False
  elif abs(a-c)<2:
    if abs(a-b)>1 and abs(b-c)>1:
      return True
    return False
  else:
    return False