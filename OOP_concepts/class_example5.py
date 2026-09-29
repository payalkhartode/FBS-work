
class College:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def display(self):
        print("College:", self.name)
        print("City:", self.city)


c1 = College("MCP College", "Phaltan")
c1.display()

print("Old City:", c1.get_city())

c1.set_city("Pune")

print("New City:", c1.get_city())