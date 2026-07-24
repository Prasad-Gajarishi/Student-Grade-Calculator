while True:

    print("="*51)
    print("          Welcome to the Grade Calculator")
    print("="*51)
    name=input("Enter your name: ")
    print("Welcome",name)
    print("Please enter your marks for the following subjects out of 100:")

    while True:
            subject1=input("Enter your marks for Maths:")
            if  0<= int(subject1) <= 100:
                break
            else:
                print("Invalid input. Please enter a number between 0 and 100.")

    while True:
        subject2=input("Enter your marks for Science:")
        if  0<= int(subject2) <= 100:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 100.")

    while True:
        subject3=input("Enter your marks for English:")
        if  0<= int(subject3) <= 100:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 100.")

    while True:
        subject4=input("Enter your marks for History:")
        if  0<= int(subject4) <= 100:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 100.")

    while True:
        subject5=input("Enter your marks for Geography:")
        if  0<= int(subject5) <= 100:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 100.")
    Total_marks= int(subject1)+int(subject2)+int(subject3)+int(subject4)+int(subject5)
    Average_marks= Total_marks/5
    print("Total Marks obtain by ",name,"in all subjects is:",Total_marks)
    Percentage= (Total_marks/500)*100
    print("Percentage of marks obtained by ",name,"is:",Percentage,"%")
    Highest_marks= max(int(subject1),int(subject2),int(subject3),int(subject4),int(subject5))
    if Highest_marks == int(subject1):
        Highest_subject = "Maths"
    elif Highest_marks == int(subject2):
        Highest_subject = "Science"
    elif Highest_marks == int(subject3):
        Highest_subject = "English"
    elif Highest_marks == int(subject4):
        Highest_subject = "History"
    else:
        Highest_subject = "Geography"
    print("Highest marks obtained by ",name,"is:",Highest_marks,"in",Highest_subject)
    Lowest_marks=min(int(subject1),int(subject2),int(subject3),int(subject4),int(subject5))
    if Lowest_marks == int(subject1):
        Lowest_subject = "Maths"
    elif Lowest_marks == int(subject2):
        Lowest_subject = "Science"
    elif Lowest_marks == int(subject3):
        Lowest_subject = "English"
    elif Lowest_marks == int(subject4):
        Lowest_subject = "History"
    else:
        Lowest_subject = "Geography"
    print("Lowest marks obtained by ",name,"is:",Lowest_marks,"in",Lowest_subject)
    if Percentage>=90:
        print("Excelent score",name,"! You have achieved an A+ grade.")
    elif Percentage>=80:
        print("Good score",name,"! You have achieved a A grade.")
    elif Percentage>=70:
        print("Average score",name,"! You have achieved a B+ grade.")
    elif Percentage>=60:
        print("Below Average score",name,"but you can score better next time " "You have achieved a B grade.")
    elif Percentage>=50:
        print("Poor score",name,"do better next time ""! You have achieved a C grade.")
    else:
        print("Fail",name,"! You have achieved a D grade. Better luck next time.")
    if Percentage >= 36:
        print("You have passed  in the exam.")
    else:
        print("You have failed in the exam. Better luck next time.")
        print("\n" + "="*50)
    print()
    print("="*50)
    print("           STUDENT REPORT CARD")
    print("="*50)

    print(f"Student Name      : {name}")

    print()

    print(f"Total Marks       : {Total_marks}/500")
    print(f"Average Marks     : {Average_marks:.2f}")
    print(f"Percentage        : {Percentage:.2f}%")

    print()

    print(f"Highest Marks     : {Highest_marks} ({Highest_subject})")
    print(f"Lowest Marks      : {Lowest_marks} ({Lowest_subject})")

    print()
    print("="*50)
    choice = input("\nDo you want to calculate another student's result? (Y/N): ")
    if choice.upper() == "N":
            print("Thank you for using the Grade Calculator!")
            break
