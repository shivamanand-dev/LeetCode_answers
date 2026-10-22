# 1.Two Sum
def two_sum(arr: list[int], target: int):
    seen = {}
    result = []

    for i, v in enumerate(arr):
        diff = target - v
        if diff in seen:
            result = [seen[diff], i]
            return result

        seen[v] = i


print(two_sum([2, 7, 11, 15], 9))
