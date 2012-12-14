def sum13(nums):
  sum = 0
  if 13 in nums:
    x = 0
    while(x<len(nums)):
      if nums[x]==13:
        x+=2
        continue
      sum+=nums[x]
      x+=1
    
  else:
    for i in nums:
      sum += i
  return sum