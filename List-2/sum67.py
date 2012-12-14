def sum67(nums):
  sum = 0
  spot = 0
  sixed = False
  while(spot < len(nums)):
    if sixed:
      if nums[spot]==7:
        sixed = False
      spot+=1
    else:
      if nums[spot]==6:
        sixed=True
      else:
        sum+= nums[spot]
      spot+=1
  return sum