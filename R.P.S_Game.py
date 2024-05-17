import random

class Rock_Paper_Scissors:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]

    def play(self):
        while True:
            player_choice = input("\nEnter your choice (rock, paper, scissors): ")
            if player_choice.lower() not in self.choices:
                print("\nInvalid choice! Try again.")
                continue
            computer_choice = random.choice(self.choices)
            print(f"\nComputer choice: {computer_choice}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif player_choice == "rock":
                if computer_choice == "scissors":
                    print("You win!")
                    self.player_score += 1
                else:
                    print("Computer wins!")
                    self.computer_score += 1
            elif player_choice == "paper":
                if computer_choice == "rock":
                    print("You win!")
                    self.player_score += 1
                else:
                    print("Computer wins!")
                    self.computer_score += 1
            elif player_choice == "scissors":
                if computer_choice == "paper":
                    print("You win!")
                    self.player_score += 1
                else:
                    print("Computer wins!")
                    self.computer_score += 1
            else:
                print("Invalid choice! Try again.")
                continue

            print(f"\nPlayer: {self.player_score} | Computer: {self.computer_score}")
            play_again = input("\nDo you want to play again? (yes/no): ")
            if play_again.lower() == "yes" or play_again.lower() == "y":
                continue
            elif play_again.lower() == "no" or play_again.lower() == "n":
                self.feedback()
                break
            else:
                input("Invalid input!")
                continue

    def feedback(self):
        print("\nThanks for playing!")
        print(f"Final Score -> Player: {self.player_score} | Computer: {self.computer_score}")

if __name__ == "__main__":
    print()
    print("*"*40)
    print("Welcome to Rock, Paper, Scissors Game!\n")
    print("Rules:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins")
    print("*"*40)

    game = Rock_Paper_Scissors()
    game.play()