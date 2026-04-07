class mummy:

    def __init__(self, car, salary):
        self.car = car
        self.salary = salary

    def _access_my_car_mummy(self):
        return f"you can drive my car - Mummy"
    
class grandpa:

    def __init__(self, car, salary):
        self.car = car
        self.salary = salary

    def _access_my_car(self):
        return "You can drive my car - Grandpa"
    
    def __access_my_salary(self):
        return "You can't access my salary - Grandpa"
    

class papa(grandpa):

    def __init__(self, grandpa_car, papa_salary):
        self.papa_salary = papa_salary
        grandpa.__init__(self, grandpa_car, self.papa_salary*0.8)

    def _access_my_father_car(self):
        return self._access_my_car()
    
    def _access_my_father_salary(self):
        return self.__access_my_salary()
    
    def play_cricket(self):
        return "Okey son you can play cricket"
    
class son(papa, mummy):

    def __init__(self, car, salary):
        papa.__init__(self, car, salary)
        mummy.__init__(self, car, salary)

    def _access_my_father_car(self):
        return f"Okey son you can drive your grandpa car - papa"
    
    def access_my_mummy_car(self):
        return self._access_my_car_mummy()
# papaIns = papa("Swift", 100000)
# print(papaIns.access_my_father_car())
# print(papaIns.access_my_father_salary())

sonIns = son("Swift", 100000)
print(sonIns._access_my_father_car())
print(sonIns.access_my_mummy_car())
# print(sonIns._access_my_father_salary())