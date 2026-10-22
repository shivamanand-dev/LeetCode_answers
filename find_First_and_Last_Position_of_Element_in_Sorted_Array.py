# 34. Find First and Last Position of Element in Sorted Array


def searchRange(nums: list[int], target: int) -> list[int]:
    def left():
        l, r = 0, len(nums) - 1

        left_index = -1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                left_index = m
                r = m - 1
        return left_index

    def right():
        l, r = 0, len(nums) - 1
        right_index = -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                right_index = m
                l = m + 1
        return right_index

    return [left(), right()]


print(searchRange([5, 7, 7, 8, 8, 10], 8))
