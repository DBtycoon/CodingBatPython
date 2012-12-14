def caught_speeding(speed, is_birthday):
  extra = 0
  if is_birthday:
    extra = 5
  if speed<61+extra:
    return 0
  elif speed>60+extra and speed<81+extra:
    return 1
  return 2