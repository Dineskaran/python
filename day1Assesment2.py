class Student:

    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def Display(self):
        print("Student name is  ::", self.name)
        print("Enroll number is :: ", self.rollnumber)

        print("====================*==================*====================*")

    def setAge(self, age):
        self.age = age
        return f"my Age is {self.age}"

    def setMarks(self, mar):
        self.mar = mar
        return f"my marks is {self.mar}"


student_name = input("Enter student name : ")
roll_number = input("Enter the roll num :")
print("..................")

student1 = Student(student_name, roll_number)
student1.Display()
# age=student1.setAge=25;
# marks=student1.setMarks=93;

# print("Student Age is:",age)
# print("Siudent Marks is:",marks)

age = int(input("Enter student's age: "))
marks = float(input("Enter the marks: "))
print("..................")

print(student1.setAge(age))
print(student1.setMarks(marks))
print("---------------=------------------------=-----------------------------=-----------------------------=")
