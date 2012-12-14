def centered_average(nums):
  del nums[nums.index(max(nums))]
  del nums[nums.index(min(nums))]
  
  count = 0
  for i in nums:
    count += i
  return count/len(nums)