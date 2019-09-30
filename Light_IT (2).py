import random

class  Hero():
    """Класс игрока"""
    def __init__(self, name):
        """Initiate our Hero PC"""
        self.name = name
        self.health = 100


    def show_hero(self):
        """параметры игрока"""
        description = ("Имя игрока: " + self.name + " количество жизни " + str(self.health)).title()
        print(description)

    def health_up(self):
        """Повышение зоровья"""
        self.health += 20
        print("Здоровье пополнено")

    def low_hit(self):
        """Ударить"""
        self.health -= 20
        #print(self.name + " нанес удар")

    def set_health(self, new_health):
        """Потерять здоровье"""
        self.health = new_health

    def high_hit(self):
        """Сильный удар"""
        self.health -= 30
        #





# Main -------------------------------------

user1 = Hero("1. Человек,")
user2 = Hero("2. Компьютер,")

print("-----------------------------")

for i in range(1, 100):
    random_user = random.choice([user1, user2])

    if random_user == user1:
        print("Компьютер ударил")
        user2.low_hit()
        user1.show_hero()
        user2.show_hero()


    elif random_user == user2:
        print("Человек ударил")
        user1.low_hit()
        user1.show_hero()
        user2.show_hero()







