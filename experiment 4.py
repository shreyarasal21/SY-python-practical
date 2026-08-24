print("=====trafic signals rules======")

signals=input("Enter the signals colour :").lower()
if signals =="red":
    print("action:stop")
elif signals =="yellow":
    print("action:slow down")
elif signals =="green":
    print("action:go")
else:
    print("invalid signals")