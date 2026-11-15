def ways(stairs):
    if stairs <  0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs - 1) + ways(stairs - 2)

input("ways counts every distinct path up n stairs - 1 step or 2 steps at a time.  Press Enter")
print("  ways(8) =", ways(8))
print("  ways(9) =", ways(9))
print("  ways(10) =", ways(10))