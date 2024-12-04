name = input("Enter the name:")
roll_number = int(input("Enter the roll number:"))
marks = int(input("Enter the marks:"))

if marks >= 90:
    print("Name:", name, "Roll Number:", roll_number, "Marks:", marks,"Grade Point:", 10, "Remark:", "OUTSTANDING")
elif marks < 90 and marks >= 80:
    print("Name:", name, "Roll Number:", roll_number, "Marks:", marks,"Grade Point:", 9, "Remark:", "VERY GOOD")
elif marks < 80 and marks >= 70:
    print("Name:", name, "Roll Number:", roll_number, "Marks:", marks,"Grade Point:", 8,  "Remark:", "GOOD")
elif marks < 70 and marks >= 60:
    print("Name:", name, "Roll Number:", roll_number, "Marks:", marks,"Grade Point:", 7,  "Remark:", "AVERAGE")
elif marks < 60 and marks >= 50:
    print("Name:", name, "Roll Number:", roll_number, "Marks:", marks,"Grade Point:", 6,  "Remark:", "PASS")
else:
    print("Name:", name, "Roll Number:", roll_number, "Marks:", marks,"Grade Point:", 0,  "Remark:", "FAIL")        