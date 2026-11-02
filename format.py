def find_max(nums):
    big = nums[0]
    for n in nums:
        if n > big:
            big = n
    return big
# call with predefined values
print(find_max([1,4,7,8]))
