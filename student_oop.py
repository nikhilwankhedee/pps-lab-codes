
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", sum(self.marks))
        print("Average:", sum(self.marks)/len(self.marks))


students = []

n = int(input("Enter number of students: "))

for i in range(n):

    name = input("Enter student name: ")
    marks = []

    for j in range(3):
        m = int(input("Enter marks: "))
        marks.append(m)

    students.append(Student(name, marks))


for s in students:
    s.display()
