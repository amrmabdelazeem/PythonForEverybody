'''largest = None
print("Before ",largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print("Loop ",itervar, largest)
print("After ", largest)'''

smallest = None
print("Before ",smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("in Loop ", itervar, smallest)
print("Smallest ", smallest)
