score=float(input("Enter your scores :"))
backlogs=int(input("Enter your backlogs :"))

if score >= 70 and backlogs == 0:
    print("The candidate is eligible for placement ")
else:
    print("The candidate is not eligible for placement ")