def sumThree(nums):
    if not nums:
        return False
    for i in range(1, len(nums)):
        for j in range(2, len(nums)):
            if nums[0] + nums[i] + nums[j] == 2020:
                return nums[0]*nums[i]*nums[j]
    return sumThree(nums[1:])

def sumTwo(nums):
    if not nums:
        return False

    for i in range(1, len(nums)):
        if nums[0] + nums[i] == 2020:
            return nums[0]*nums[i]
    return sumTwo(nums[1:])

if __name__ == '__main__':
    with open('input1.txt') as f:
        nums = list(map(int, f.readlines()))
    a = sumThree(nums)
    if a: print(a)