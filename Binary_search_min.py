def findMin(nums):

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left+right) // 2

        if nums[mid] == nums[right]:
            right -= 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left]

test = {
    "input": {
        "nums": [300, 400, 500, 100, 200]
    },
    "output": 100
}

print(findMin(**test["input"]))