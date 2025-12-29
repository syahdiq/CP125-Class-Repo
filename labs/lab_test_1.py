#MUHAMMAD SYAHDIQ ASYRAF BIN TIPILIL @ RAPAHIL
#C02T
#WRITE A PYTHON PROGRAM USING FUNCTION TO CHECK AND DISPLAY STUDENT MARK AND GRADE

#Ask user to enter score
score = float(input("Enter the student's mark: "))

#Using function to determine grade
def determine_grade (score):
    if score >= 80:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C" 
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"
    return grade
    
#Output displaying using function above
if score <= 100 and score >= 0:
    result = determine_grade(score)
    print(f"Mark: {score}, Grade: {result}")
else:
    print("Mark that you entered is not true")
