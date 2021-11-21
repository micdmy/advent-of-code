
def read_input():
    with open("input.txt") as f:
        return [int(line) for line in f]
    return

expenses = read_input()
sortedExpenses = sorted(expenses)
sumToFind = 2020

for idx1, expense1 in enumerate(sortedExpenses[:-1]):
    for idx2, expense2 in enumerate(sortedExpenses[idx1 + 1:]):
        if expense1 + expense2 == sumToFind:
            print("Two expenses that sum to {} are: {} {} . Multipied: {}".format(sumToFind, expense1, expense2, expense1 * expense2))
        if expense1 + expense2 > sumToFind:
            break
        for  expense3 in sortedExpenses[idx1 + 1 + idx2 + 1:]:
            if expense1 + expense2 + expense3 == sumToFind:
                print("Three expenses that sum to {} are: {} {} {}. Multipied: {}".format(sumToFind, expense1, expense2, expense3, expense1 * expense2 * expense3))
