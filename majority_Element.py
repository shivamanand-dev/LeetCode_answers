# 169. Majority Element
def majorityElement(nums: list[int]) -> int:
    # num_dict = {}
    # n = len(nums)

    # for v in nums:
    #     if v in num_dict:
    #         num_dict[v] += 1
    #         if num_dict[v] > (n // 2):
    #             return v
    #     else:
    #         num_dict[v] = 1
    # return nums[0]

    candidate = 0
    cnt = 0
    for i in nums:
        if cnt == 0:
            candidate = i
            cnt += 1
        elif candidate == i:
            cnt += 1
        else:
            cnt -= 1
    return candidate


print(majorityElement([3]))
