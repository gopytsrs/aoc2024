def parse():
    return list(map(int, open("input.txt").read().strip()))


def solve1():
    line = parse()
    spaces = []
    file_id = 0

    for i, n in enumerate(line):
        if i % 2 == 1:
            spaces.extend([-1] * n)
        else:
            spaces.extend([file_id] * n)
            file_id += 1

    left = 0
    right = len(spaces) - 1
    while left < right:
        while left < right and spaces[left] != -1:
            left += 1
        while left < right and spaces[right] == -1:
            right -= 1
        if left >= right:
            break
        spaces[left] = spaces[right]
        spaces[right] = -1
        left += 1
        right -= 1

    checksum = sum(i * file_id for i, file_id in enumerate(spaces) if file_id != -1)

    return checksum


from heapq import heappush, heappop
def solve2():
    line = parse()
    file_id = 0
    spaces = []
    idx_to_file_id = {}
    idx = 0
    files = []
    for i, n in enumerate(line):
        if i % 2 == 1:
            if n == 0:
                continue
            heappush(spaces, (idx, n)) # start_of_gap, gap_length
        else:
            files.append((idx, n)) # start_of_file, file_length
            for i in range(n):
                idx_to_file_id[idx + i] = file_id
            file_id += 1
        idx += n
    
    for start_of_file, file_length in reversed(files):
        file_id = idx_to_file_id[start_of_file]
        push_back = []
        while spaces and spaces[0][1] < file_length:
            push_back.append(heappop(spaces))
        if spaces and spaces[0][0] < start_of_file:
            start_of_gap, gap_length = heappop(spaces)
            for i in range(file_length):
                idx_to_file_id[start_of_file + i] = -1
            for i in range(file_length):
                idx_to_file_id[start_of_gap + i] = file_id
            
            if gap_length > file_length:
                heappush(spaces, (start_of_gap + file_length, gap_length - file_length))
        for item in push_back:
            heappush(spaces, item)
    
    return sum(idx * file_id for idx, file_id in idx_to_file_id.items() if file_id != -1)
    
    
            
        

        
print("Part 1:", solve1())
print("Part 2:", solve2())