    
def read_input():
    with open("2018-01-input-01") as f:
        return [int(line) for line in f]
    return

def sum_drift(offset, drift):
        return offset + sum(drift)

drift = read_input()
if not drift :
    exit()

table_step = sum_drift(0, drift)
print("part 1: After all changes in frequencies, the result is = " + str(table_step))
        
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

generated = set()
integral = integrate(0, drift)
offset = 0
counter = 0
while True:
    table = [offset + i for i in integral]
    for t in table:
        if t not in generated:
            generated.add(t)
        else:
            print("First frequency reached twice is " + str(t))
            exit()
    offset += table_step
    counter += 1
    print(str(offset) + " " + str(counter))