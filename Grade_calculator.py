def get_valid_marks(subject_name):
    while True:
        marks = input(f"Enter your marks for {subject_name}: ").strip()
        if not marks.isdigit():
            print("Invalid input. Please enter a whole number between 0 and 100 (no symbols, decimals, or letters).")
            continue
        marks = int(marks)
        if 0 <= marks <= 100:
            return marks
        else:
            print("Invalid input. Please enter a number between 0 and 100.")


while True:

    print("="*51)
    print("          Welcome to the Grade Calculator")
    print("="*51)

    while True:
        name = input("Enter your name (First Last): ").strip()
        name_parts = name.split()
        if len(name_parts) < 2:
            print("Invalid name format. Please enter both first and last name (e.g., John Smith).")
        elif not all(part.isalpha() for part in name_parts):
            print("Invalid name. Name should contain only letters, no numbers or symbols.")
        else:
            name = " ".join(word.capitalize() for word in name_parts)
            break

    print("Welcome", name)
    print("Please enter your marks for the following subjects out of 100:")

    subject1 = get_valid_marks("Maths")
    subject2 = get_valid_marks("Science")
    subject3 = get_valid_marks("English")
    subject4 = get_valid_marks("History")
    subject5 = get_valid_marks("Geography")

    Total_marks = subject1 + subject2 + subject3 + subject4 + subject5
    Average_marks = Total_marks / 5
    print("Total Marks obtain by ",name,"in all subjects is:",Total_marks)
    Percentage = (Total_marks/500)*100
    print("Percentage of marks obtained by ",name,"is:",Percentage,"%")
    Highest_marks = max(subject1, subject2, subject3, subject4, subject5)
    if Highest_marks == subject1:
        Highest_subject = "Maths"
    elif Highest_marks == subject2:
        Highest_subject = "Science"
    elif Highest_marks == subject3:
        Highest_subject = "English"
    elif Highest_marks == subject4:
        Highest_subject = "History"
    else:
        Highest_subject = "Geography"
    print("Highest marks obtained by ",name,"is:",Highest_marks,"in",Highest_subject)
    Lowest_marks = min(subject1, subject2, subject3, subject4, subject5)
    if Lowest_marks == subject1:
        Lowest_subject = "Maths"
    elif Lowest_marks == subject2:
        Lowest_subject = "Science"
    elif Lowest_marks == subject3:
        Lowest_subject = "English"
    elif Lowest_marks == subject4:
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

    while True:
        choice = input("\nDo you want to calculate another student's result? (Y/N): ").strip().upper()
        if choice in ("Y", "N"):
            break
        else:
            print("Invalid input. Please enter only Y or N.")

    if choice == "N":
        print("Thank you for using the Grade Calculator!")
        break