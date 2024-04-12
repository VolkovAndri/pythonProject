import random

class Car:
    def __init__(self):
        self.coins = 0
        self.has_car = False

    def buy_car(self, human):
        if human.coins >= 150:
            print("Congratulations! You bought a car.")
            human.coins -= 150  # Car costs 150 coins
            self.has_car = True
        else:
            print("You don't have enough coins to buy a car.")

    def casino(self):
        if self.has_car:
            print("You decide to go to the casino.")
            roll = random.randint(1, 10)
            if roll > 7:
                print("Congratulations! You won 10,000 coins!")
                self.coins += 10000
            else:
                print("Unfortunately, you lost 10 coins at the casino.")
                self.coins -= 10
                print("You decide to sell your car.")
                self.has_car = False
                self.coins += 150  # Selling the car returns 150 coins

class HumanLife:
    def __init__(self):
        self.happiness = 30
        self.satiation = 50
        self.love = 5
        self.coins = 100
        self.car = Car()

    def play_game(self):
        choices = ['rock', 'paper', 'scissors']
        your_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        computer_choice = random.choice(choices)
        print(f"You chose: {your_choice}")
        print(f"Computer chose: {computer_choice}")

        if your_choice in choices:
            if your_choice == computer_choice:
                print("It's a tie!")
            elif (your_choice == 'rock' and computer_choice == 'scissors') or \
                 (your_choice == 'paper' and computer_choice == 'rock') or \
                 (your_choice == 'scissors' and computer_choice == 'paper'):
                print("You win!")
                self.happiness += 25
            else:
                print("You lose!")
                self.happiness -= 5
        else:
            print("Invalid choice.")

        self.happiness = min(self.happiness, 100)
        self.satiation = min(self.satiation + random.randint(0, 50), 100)
        self.love = min(self.love + random.randint(0, 50), 100)

    def help_stranger(self):
        choice = input("Would you like to help a passerby pick up trash? (yes/no): ").lower()
        if choice == "yes":
            print("You chose to help. You receive positive messages!")
            self.love += 20
            self.coins += 30
        elif choice == "no":
            print("You chose not to help. You receive negative messages.")
            self.love -= 20
        else:
            print("Invalid choice.")

    def eat(self):
        choice = input("Would you like to buy food? (yes/no): ").lower()
        if choice == "yes":
            if self.coins >= 10:
                print("You chose to buy food.")
                self.satiation += 10
                self.coins -= 10
            else:
                print("You don't have enough coins to buy food.")
                self.satiation -= 5
        elif choice == "no":
            print("You chose not to buy food.")
            self.satiation -= 5
        else:
            print("Invalid choice.")

    def check_status(self):
        return self.happiness >= 100 and self.satiation >= 100 and self.love >= 100

    def live(self, days):
        for day in range(1, days+1):
            print(f"Day {day}:")
            while not self.check_status():
                print(f"Happiness: {self.happiness}, Satiation: {self.satiation}, Love: {self.love}, Coins: {self.coins}")
                if self.coins >= 150 and not self.car.has_car:
                    choice = input("Would you like to buy a car? (yes/no): ").lower()
                    if choice == "yes":
                        self.car.buy_car(self)
                    elif choice == "no":
                        print("You chose not to buy a car.")
                    else:
                        print("Invalid choice.")
                if not self.car.has_car:
                    self.play_game()
                    self.help_stranger()
                    self.eat()
                else:
                    self.car.casino()
            if self.check_status():
                print("Congratulations! You've achieved maximum happiness, satiation, and love!")
                print("Moving to the next day...\n")
                self.happiness = 30
                self.satiation = 50
                self.love = 5
                self.coins = 100

human = HumanLife()
human.live(30)