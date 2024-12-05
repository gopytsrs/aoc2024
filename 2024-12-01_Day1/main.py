def parse_input():
    list1, list2 = [], []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))
            
    return list1, list2

def solve1():
    list1, list2 = parse_input()
    total_dist = 0
    for num1, num2 in zip(sorted(list1), sorted(list2)):
        total_dist = total_dist + abs(num1 - num2)
    print("Total distance:", total_dist)

from collections import Counter
def solve2():
    list1, list2 = parse_input()
    list2_count = Counter(list2)
    similarity = 0
    for num in list1:
        similarity += num * list2_count[num]
    print("Similarity:", similarity)
        

solve1()
solve2()