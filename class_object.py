# this is class
class student:

    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Adding new student data in Database..")

# This is an object
s1 = student("Danish",97)
print(s1.name, s1.marks)

s2 = student("Bilal",100)
print(s2.name, s2.marks)