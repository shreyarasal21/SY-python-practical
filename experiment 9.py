marks=[]

while True:
    print("\n===STUDENT MARKS MANAGEMENT SYSTEM====")
    print("1. Insert marks:")
    print("2. display marks:")
    print("3. update marks:")
    print("4. delete marks:")
    print("5.exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        mark=int(input("Enter student marks:"))
        marks.append(mark)
        print("Marks inserted successfully")
    elif choice==2:
        if len(marks)==0:
            print("No marks available")
        else:
            print("Student Marks:")
            for i in range(len(marks)):
                print("Student",i+1,":",marks[i])
    elif choice==3:
        student=int(input("Enter student number to update:"))
        if i<=student<=len(marks):
            new_mark=int(input("Enter new marks:")) 
            marks[student-1]=new_mark
            print("Marks updated successfully")
        else:
            print("Invalid student number")

    elif choice==4:
            student=int(input("Enter student number to delete:"))
            if i<=student<=len(marks): 
              marks.pop(student-1)
              print("Marks deleted successfully")
            else:
                print("Invalid student number")

    elif choice==5:
        print("Program ended")
        break
    else:
        print("Invalid choice")