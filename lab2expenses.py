print("\n***** EXPENSE TRACKER *****")

food = 0.0
shopping = 0.0
travels = 0.0
other = 0.0
expenses = 0.0

while True:
    value = float(input("Enter your amount (-1 to stop): "))

    if value == -1:
        break

    category = input("Enter category (food/shopping/travels/other): ").lower()

    if category == "food":
        food += value
    elif category == "shopping":
        shopping += value
    elif category == "travels":
        travels += value
    elif category == "other":
        other += value
    else:
        print("Invalid category!")
        continue

    expenses += value

print("\n***** EXPENSE SUMMARY *****")
print("Food:", food)
print("Shopping:", shopping)
print("Travels:", travels)
print("Other:", other)
print("Total Expenses:", expenses)
