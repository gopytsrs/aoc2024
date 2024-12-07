def parse():
    result = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            test_val, rest = line.split(":")
            test_val = int(test_val.strip())
            nums = list(map(int, rest.strip().split()))
            result.append((test_val, nums))
    
    return result

def backtrack(target, nums, idx, curr_sum):
    if idx == len(nums):
        return curr_sum == target
    return (
        backtrack(target, nums, idx + 1, curr_sum + nums[idx]) or 
        backtrack(target, nums, idx + 1, curr_sum * nums[idx])
    )

def backtrack2(target, nums, idx, curr_sum):
    if idx == len(nums):
        return curr_sum == target
    return (
        backtrack2(target, nums, idx + 1, curr_sum + nums[idx]) or 
        backtrack2(target, nums, idx + 1, curr_sum * nums[idx]) or 
        backtrack2(target, nums, idx + 1, int(str(curr_sum) + str(nums[idx])))
    )

def solve1():
    data = parse()
    total = 0
    for target, nums in data:
        if backtrack(target, nums, 1, nums[0]):
            total += target
    return total


def solve2():
    data = parse()
    total = 0
    for target, nums in data:
        if backtrack2(target, nums, 1, nums[0]):
            total += target
    return total
        
print("Part 1:", solve1())
print("Part 2:", solve2())