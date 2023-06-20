def remove_zeros(nums):

  for i in nums:
    if i == 0:
      nums.remove(0)
      nums.append(0)
  return nums

  



print(remove_zeros([1,1,0,3,0,4,3,2,4,2]))

