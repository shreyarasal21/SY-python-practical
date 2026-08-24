marks=[]

while True:
    print("\n---Student Marks Management System---")
    print("1. Insert Marks")
    print("2. Display Marks")
    print("3. Update Marks")
    print("4. Delete Marks")
    print("5. Exit")

    choice = int(input("Enter your choice:"))

    #Insertion
    if choice == 1:
        mark = int(input("Enter student mark:"))
        marks.append(mark)
        print("Marks inserted succesfully.")


    #Traversal
    elif choice == 2:
        if len(marks) == 0:
            print("No marks available.")


        else:
            print("Student Marks:")
            for i in range (len(marks)):
                print("Student",i+1, ":", marks[i])


    #Updating

    elif choice == 3:
        student = int(input("Enter student number to update:"))
        if i <= student <= len(marks):
            new_mark = int(input("Enter new marks:"))
            marks[student-1] = new_mark
            print("Marks updated succesfully.")

        else:
            print("Invalid student number.")


    #Deletion 
    elif choice == 4:
        student = int(input("Enter student number to delete:"))
        if 1<=student <= len(marks):
            marks.pop(student-1)
            print("Marks deleted succesfully.")

        else:
            print("Invalid student number.")

    #exit           

    elif choice == 5:
        print("program ended.") 
        break

    else:
        print("Invalid choice.")