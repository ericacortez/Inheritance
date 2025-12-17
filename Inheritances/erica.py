# 1. SINGLE INHERITANCE

class Human:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Student(Human):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course  # instance variable

    def study(self):
        print(f"{self.name} is studying {self.course}.")

print("SINGLE INHERITANCE")
student = Student("Erica Cortez", 19, "Information Systems")
student.greet()  # changed from student.breathe()
student.study()
print()



# 2. MULTIPLE INHERITANCE

class Skills:
    def __init__(self, skill):
        self.skill = skill  # instance variable

class Experience:
    def __init__(self, years):
        self.years = years  # instance variable

class Employee(Skills, Experience):
    def __init__(self, skill, years, name):
        Skills.__init__(self, skill)
        Experience.__init__(self, years)
        self.name = name  # instance variable

    def show_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Skill: {self.skill}")
        print(f"Years of Experience: {self.years}")

print("MULTIPLE INHERITANCE")
employee = Employee("Graphic design", 5, "lily")
employee.show_info()
print()

# 3. MULTILEVEL INHERITANCE

class Person:
    def __init__(self, name):
        self.name = name  # instance variable

    def identity(self):
        print(f"I am {self.name}, a person.")

class Worker(Person):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job  # instance variable

    def work(self):
        print(f"{self.name} works as a {self.job}.")

class Supervisor(Worker):
    def __init__(self, name, job, team_size):
        super().__init__(name, job)
        self.team_size = team_size  # instance variable

    def supervise(self):
        print(f"{self.name} supervises a team of {self.team_size} workers.")

print("MULTILEVEL INHERITANCE")
supervisor = Supervisor("Charlie", "Engineer", 10)
supervisor.identity()
supervisor.work()
supervisor.supervise()
print()



# 4. HIERARCHICAL INHERITANCE

class PersonBase:
    def __init__(self, name):
        self.name = name  # instance variable

    def eat(self):
        print(f"{self.name} needs food.")

class Teacher(PersonBase):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject  # instance variable

    def teach(self):
        print(f"{self.name} teaches {self.subject}.")

class Nurse(PersonBase):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department  # instance variable

    def care(self):
        print(f"{self.name} cares for patients in {self.department} department.")

print("HIERARCHICAL INHERITANCE")
teacher = Teacher("dani", "English")
nurse = Nurse("Mae ", "Pediatrics")
teacher.eat()
teacher.teach()
nurse.eat()
nurse.care()
print()



# 5. HYBRID INHERITANCE

class Individual:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Professional(Individual):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession  # instance variable

    def work(self):
        print(f"I work as a {self.profession}.")

class Artist:
    def __init__(self, art_type):
        self.art_type = art_type  # instance variable

    def create_art(self):
        print(f"I create {self.art_type} art.")

class ProfessionalArtist(Professional, Artist):
    def __init__(self, name, age, profession, art_type):
        Professional.__init__(self, name, age, profession)
        Artist.__init__(self, art_type)

    def perform(self):
        print(f"{self.name} performs {self.art_type} art professionally.")

print("HYBRID INHERITANCE")
pa = ProfessionalArtist("belle", 25, "Dancer", "Contemporary")
pa.introduce()
pa.work()
pa.create_art()
pa.perform()
