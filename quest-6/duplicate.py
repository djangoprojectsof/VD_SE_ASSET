def find_duplicate(nums):

    x = nums[0]
    y = nums[0]


    while True:
        x = nums[x]
        y = nums[nums[y]]
        if x == y:
            break


    x = nums[0]
    while x != y:
        x = nums[x]
        y = nums[y]
    return y

nums = [1, 3, 4, 2, 2]
duplicate = find_duplicate(nums)
print(duplicate)
