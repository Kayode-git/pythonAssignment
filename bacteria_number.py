print(f"%s" % 'Hour', "%20s" % 'Number of Bacteria')

# for number in range(4):
number = 0
while number < 4:
    print(f"%4d" % (number * 5), "%20d" % (200 * 2 ** (number * 5)))
    number += 1
