def findPeakElement(nums):
        n = len(nums)
        if (n == 1):
            return 0
        if (nums[0] >= nums[1]):
            return 0
        if (nums[n - 1] >= nums[n - 2]):
            return n - 1

        for i in range(1, n - 1):

            if (nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]):
                return i

test = {
    "input": {
        "nums": [12, 33, 43,53 ,1 , 0, 9]
    },
    "output": 3
}

print(findPeakElement(**test["input"]))