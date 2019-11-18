    
def sum_drift(offset):
    with open("2018-01-input-01") as f:
        drift = [int(line) for line in f]
        return offset + sum(drift)
    
print("After all changes in frequencies, the result is = " + str(sum_drift(0)))
        
