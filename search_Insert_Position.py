# 35. Search Insert Position
def searchInsert(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif i == len(nums) - 1 and nums[i] < target:
            nums.insert(i + 1, target)
            print(f"nums = {nums}")
            return i + 1
        elif nums[i] > target:
            nums.insert(i, target)
            print(f"nums = {nums}")
            return i
        else:
            continue


print(searchInsert([1, 3, 5, 6], 2))
