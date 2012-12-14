def end_other(a, b):
  return a.lower()==b[-len(a):].lower() or b.lower()==a[-len(b):].lower()