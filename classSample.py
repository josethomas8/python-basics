class FamilyMembers:
    year = 2020

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Year "+str(FamilyMembers.year))
        print("Name "+self.name)
        print("Age "+str(self.age))
        print("Place "+self.place)

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1

    @staticmethod
    def display_welcome():
        print("Welcome")


FamilyMembers.display_welcome()


x = FamilyMembers("Nirmala", 52, "calicut")
y = FamilyMembers("Thomas kv", 56, "kannur")


x.display()
y.display()

print("-----------------------------------------------------------------------")

FamilyMembers.year=FamilyMembers.year+1
x.add_age()
y.add_age()

x.display()
y.display()
print("----------------------------------------------------------------------")

FamilyMembers.add_year()

x.add_age()
y.add_age()

x.relocate("Delhi")
y.relocate("Mumbi")

x.display()
y.display()
