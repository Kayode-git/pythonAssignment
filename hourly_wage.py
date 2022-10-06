import math

# earning for 5 years
o = 10
p = 3 / 100
n = 5

w1 = o * math.pow((1 + p), n)

print(f"Employee's earning after 5 year: $%.2f" % w1)

# 2 years afterwards
o = w1
p = - 3 / 100
n = 2

w2 = w1 * math.pow((1 + p), n)

print(f"Employee's earning 2 years later: $%.2f" % w2)
