name=input("Enter your name :")
age= int(input("Enter your age :"))
income=float(input("Enter your income :"))
cast=input("Enter your cast ( sc/st/mt/obc):")
if age < 25 and income < 300000 and cast in ["sc","st","nt","obc"]:
    print("congratulation! .You are qualified for education scolarship scheme. ")  
else:
    print("You are not qualified for education scolarship scheme. ")