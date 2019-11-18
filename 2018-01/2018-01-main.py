    
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
        
# PART TWO:

def integrate(offset, drift):
    integral = [0] * (len(drift) + 1)
    integral[0] = offset
    for i in range(0, len(drift)):
        integral[i+1] = integral[i] + drift[i]
    return integral[1:]

print("PART two")
a = [1, 2, 3]
print(str(a))
print(str(integrate(0, a)))

print(str(integrate(0,drift)))

