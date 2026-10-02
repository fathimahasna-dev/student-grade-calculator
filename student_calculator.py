# Student Grade Calculator 
print("======= STUDENT GRADE CALCULATOR =======\n")

# Input Student Name 
Name = input("Enter The Student Name:")

# Input Marks 
math = float(input("Mathematics"))
science  = float(input("Science"))
english = float(input("English"))
ict = float(input("Ict"))
physics = float(input("Physics"))

# Calculate Total And Average 
total = math + science + english + ict + physics
average = total / 5 

# Find Grade
if average >= 90:
    Grade = "A" 
elif average >= 80:
    Grade = "B"
elif average >= 70:
    Grade = "C"
elif average >= 60:
    Grade = "D"  
else:
    Grade = "F"  

# Result (Pass\Fail)
if average >= 60:
    Result = "Pass" 
else:
    Result = "Fail"  

# Output
print("\n=======Result=======")   
print("Student Name:",Name) 
print("Total Marks:",total)
print("Average:",average)
print("Grade:",Grade)
print("Result:",Result)









