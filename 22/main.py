class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def write_my_name(self):
        print(self.name,self.age)

uros=Person("Uros",24)
uros.write_my_name()
sara=Person("Sara",25)
sara.write_my_name()
