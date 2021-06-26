class students:
    name=""
    roll_number = 0
    age=0
    marks=-0

    def __init__(self, name, roll_number,age,marks):
        self.name= name
        self.roll_number = roll_number
        self.age = age
        self.marks= marks
        print("Name = ",name, "Rollnumber = ",roll_number,"Age = ", age,"Marks = ", marks)

Student= students("Amanjot", 42, 18, 600)



