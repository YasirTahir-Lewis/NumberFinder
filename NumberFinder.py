largest = None
smallest = None

while True:

    try:
        num = raw_input("Enter a Number:")
        if num == "done": break
        num = int(num)
        #print(num)
    elif largest is None or largest < num:
        largest = num
    if smallest is None or smallest > num:
        smallest = num


    except ValueError:
        print("Invalid Input")

print("Maximum Number is", largest)
print("Minimum Number is", smallest)
