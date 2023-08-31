# osztály létrehozása
class Users:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def bemutatkozas(self):
        print(
            f"Én vagyok {self.name}, {self.age} éves vagyok, {self.location}-ről vagyok.")


#user1 = Users("Ferenc", 40)
user2 = Users("Géza", 20, "Budapest")

user2.bemutatkozas()  #én vagyok géza 20 éves vagyok
