class Password():
    def __init__(self, nPass, nEnd):
        self.nPass = nPass
        self.nEnd = nEnd

    def next(self):
        self.nPass += 1
        while not self.met_criteria() :
            self.nPass += 1
            if(self.nPass > self.nEnd):
                return False
        if(self.nPass > self.nEnd):
            return False
        return True

    def met_criteria(self):
        lPass = [int(char) for char in str(self.nPass)]
        last_digit = -1
        num_adjacent = 1
        adjacency_ok = False
        for digit in lPass:
            if digit < last_digit:
                return False
            if digit == last_digit:
                num_adjacent += 1
            else:
                if num_adjacent == 2:
                    adjacency_ok = True
                num_adjacent = 1
            last_digit = digit
        if num_adjacent == 2:
            adjacency_ok = True
        return adjacency_ok


def count_possible_passwords(nBegin, nEnd):
    password = Password(nBegin, nEnd)
    counter = 0
    while password.next():
        counter +=1
    return counter

num_passwords = count_possible_passwords(264793, 803935) # puzzle input
print("Number of possible passwords is %d"%num_passwords)


        
