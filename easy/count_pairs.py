def count_pairs( nums: list[int], target: int) -> int:
    res = 0
    for i in range(len(nums)):
        for num in nums[i+1:]:
            if (nums[i] + num) < target:
                res += 1
    return res
print(count_pairs([-6,2,5,-2,-7,-1,3], -2))
print(count_pairs([-1,1,2,3,1], 2))
