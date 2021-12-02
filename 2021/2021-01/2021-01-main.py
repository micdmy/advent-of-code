
def read_input():
    with open("input.txt") as f:
        return [int(line) for line in f]
    return

depths = read_input()


def count_elements(check, array):
    cnt = 0
    for d in array:
        if check(d):
            cnt += 1
    return cnt

def increases(value):
    return value > 0

def differences(array):
    return [array[i] - array[i-1] for i in range(1, len(array))]

depths_diffs = differences(depths)
increase_cnt = sum([d > 0 for d in depths_diffs])
print("Depth increases " + str(increase_cnt) + " times.")


window_size = 3
sweep_sum = []
for i in range (0, len(depths) - window_size + 1):
    elements_to_sum = depths[i:i + window_size]
    sweep_sum.append(sum(elements_to_sum))


sweep_sum_diffs = differences(sweep_sum)
increase_cnt = sum([ssd > 0 for ssd in sweep_sum_diffs])
print("After filtering, depth increases " + str(increase_cnt) + " times.")
