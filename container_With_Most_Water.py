# 11.Container With Most Water
def calculate_area(l: int) -> int:
    return l * l


def maxArea(height: list[int]) -> int:
    l = 0
    r = len(height) - 1
    largest_area = 0

    while l < r:
        area = min(height[l], height[r]) * (r - l)
        largest_area = max(largest_area, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return largest_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
