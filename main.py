import random
import json
from time import sleep

class Human:
    def __init__(self, name):
        self.name = name
        self.car = None
        self.gladness = 50
        self.money = 20
    def greeting(self, human):
        print(f"Hello {human.name}, I am {self.name}")
    def drive(self):
        if self.car:
            self.car.drive()
    def work(self):
        #money +, gladness -
        self.money += random.randint(5, 10)
        self.gladness -= random.randint(2, 5)
    def rest(self):
        #money -, gladness +
        self.money -= random.randint(1, 10)
        self.gladness += random.randint(2, 5)

class Car:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
        self.owner = None
    def drive(self):
        print(f"{self.name} chux-chux")
    def buy(self, human):
        if not self.owner:
            if human.money >= self.price:
                human.car = self
                self.owner = human
                print(f"{human.name} купил {self.name}")
            else:
                print(f"{human.name} недостаточно средств купить {self.name}")
        else:
            print(f"{self.name} уже приобретена {self.owner.name}")

class Home:
    def __init__(self):
        self.humans = []
    def add(self, human):
        self.humans.append(human)
    def greetingAll(self):
        for human in self.humans:
            for some_human in self.humans:
                if human != some_human:
                    human.greeting(some_human)


home = None
autopark = None
player = None
thief = None

def game_start():
    h1 = Human("Kolya")
    h2 = Human("Olya")
    h3 = Human("Vadim")
    h4 = Human("Nastya")
    h5 = Human("Kristina")
    h6 = Human("Sergey")
    h7 = Human("Andrey")
    h8 = Human("Polina")

    home = Home()

    home.add(h1)
    home.add(h2)
    home.add(h3)
    home.add(h4)
    home.add(h5)
    home.add(h6)
    home.add(h7)
    home.add(h8)

autopark = [
    Car("BMW", 2019, 200),
    Car("Bentli", 2017, 300),
    Car("Bugatti", 2016, 100),
    Car("Toyota", 2022, 600),
]

def create_player():
    global player
    h = input("Введите рост персонажа: ")
    w = input("Введите вес персонажа: ")
    name = input("Введите имя персонажа: ")
    player = Player(name, h, w)
    player.save()

def init_player():
    global player
    with open('./save.json') as json_file:
        data = json.load(json_file)
        if not data:
            create_player()
        else:
            player = Player(data["name"], data["h"], data["w"])
    home.add(player)

game_start()
init_player()

day = 1
while True:
    print("Day: ", day)
    for human in home.humans:
        actions = [human.work, human.rest]
        random.choice(actions)()
        if random.randint(1, 100) <= 5:
            sleep(2)
            random.choice(autopark).buy(human)
    day += 1