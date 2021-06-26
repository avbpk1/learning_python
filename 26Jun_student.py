class Student:
    #Static Attributes
    tax_pct = 10
    course_fees = {'c': 3000, 'python': 4000, 'java': 5000, 'javaee': 8000}
    course_disc = {'c': 10, 'python': 20, 'java': 10, 'javaee': 5}

    @staticmethod
    def change_fee(course, fee):
        Student.course_fees[course] = fee

    def __init__(self, name, course='python', feepaid=0):
        # Object Attributes
        self.name = name
        if not course in Student.course_fees:
            raise ValueError("Invalid course!")

        self.course = course
        self.feepaid = feepaid
        self.disc = (Student.course_disc[self.course]/100)*Student.course_fees[self.course]

    def info(self):
        print("Student Name   : ", self.name)
        print("Course Name    : ", self.course)
        print("Course Fee    : ", Student.course_fees[self.course])
        print("Discount : ", self.disc)
        print("Total fee after tax   : ", self.totalfee())
        print("Fee Paid       : ", self.feepaid)
        print("Fee Due       : ", self.getdue())

    def payment(self, amount):
        self.feepaid += amount

#Total fee is course fee - discount + tax
    def totalfee(self):
        return (Student.course_fees[self.course] - self.disc) * (1 + self.tax_pct/100)

    def getdue(self):
        return (self.totalfee() - self.feepaid)

s = Student("Scott", "c",1000)
print(s.info())