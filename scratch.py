import random
class Pet:
    def __init__(self, name):
        self.name = name
        self.sad = 50
        self.WantToEat = 0
        self.alive = True

    def to_eat(self):
        print("Time to eat")
        self.WantToEat += 0.12
        self.sad -= 3


    def to_sleep(self):
        print("I will sleep")
        self.sad += 3

    def to_chill(self):
        print("Rest time")
        self.sad -= 5
        self.WantToEat -= 0.1

    def is_alive(self):
        if self.WantToEat < -0.5:
            print("Died!")
            self.alive = False
        elif self.sad <= 0:
            print("Depressionae!")
            self.alive = False
        elif self.WantToEat > 5:
            print("Love u!")
            self.alive = False

    def end_of_day(self):
        print(f"Sad = {self.sad}")
        print(f"WantToEat = {round(self.WantToEat, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:+^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

cat = Pet(name="Cat")
dog = Pet(name="Dog")
giraffe = Pet(name="Giraffe")



for day in range(365):
    if cat.alive == False:
        break
    cat.live(day)

    if dog.alive == False:
        break
    dog.live(day)

    if giraffe.alive == False:
        break
    giraffe.live(day)