import random

class HumanLife:
    def __init__(self):
        self.happiness = 30
        self.satiation = 50
        self.love = 5

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
        elif choice == "no":
            print("You chose not to help. You receive negative messages.")
            self.love -= 20
        else:
            print("Invalid choice.")

    def eat(self):
        choice = input("Would you like to eat? (yes/no): ").lower()
        if choice == "yes":
            print("You chose to eat.")
            self.satiation += 10
        elif choice == "no":
            print("You chose not to eat.")
            self.satiation -= 5
        else:
            print("Invalid choice.")

    def check_status(self):
        if self.happiness >= 100 and self.satiation >= 100 and self.love >= 100:
            print("Congratulations! You've achieved maximum happiness, satiation, and love!")
            return True
        return False

    def live(self, days):
        for day in range(1, days+1):
            print(f"Day {day}:")
            print(f"Happiness: {self.happiness}, Satiation: {self.satiation}, Love: {self.love}")
            self.play_game()
            self.help_stranger()
            self.eat()
            if self.check_status():
                print("Moving to the next day...\n")
                self.happiness = 30
                self.satiation = 50
                self.love = 5

human = HumanLife()
human.live(30)
