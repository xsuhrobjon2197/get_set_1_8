#6-m
class Movie:
    def __init__(self, name, year):
        self.name = name
        self.__year = year

    def get_year(self):
        return self.__year

    def get_name(self, new_name):
        return self.name == new_name

m1 = Movie("<NAME>", 1989)
print(m1)

res = m1.get_year()
print(res)

m1.get_name("mujik")
print(m1)
