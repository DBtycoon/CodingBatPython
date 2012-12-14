def count_evens(nums):
  evens = [x%2 for x in nums]
  return evens.count(0)