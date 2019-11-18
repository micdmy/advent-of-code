    
def read_input():
    with open("2018-01-input-01") as f:
        return [int(line) for line in f]
    return

def sum_drift(offset, drift):
        return offset + sum(drift)

drift = read_input()
if not drift :
    exit()
    
print("part 1: After all changes in frequencies, the result is = " + str(sum_drift(0, drift)))
        
