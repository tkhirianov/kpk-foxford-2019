class Goat:
    """ класс козы - родовой для объектов коз"""
    def __init__(self, nickname, sex, age, weight):
        # атрибуты создаются _только_ в конструкторе класса!
        self.nickname = nickname
        self.sex = sex
        self.age = age
        self.weight = weight
        

    def get_milk(self):
        """ метод извлекания молока из козы """
        if self.sex == "male":
            return 0
        elif self.sex == "female":
            return self.weight / 20
        else:
            return 0

    def show(self):
        print('козёл' if self.sex == "male" else
              'коза' if self.sex == "female" else "",
              self.nickname, 'возраста', self.age,
              'весит', self.weight)


a = Goat("Зорька", "female", 5, 40)
a.show()
print(a.get_milk())
