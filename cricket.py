import random
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def play_shot(self):
        while True:
            try:
                run = int(input(f"{self.name}, play your shot (1-6): "))
                if 1 <= run <= 6:
                    return run
                else:
                    print("Choose between 1 to 6 only!")
            except ValueError:
                print("Enter a valid number!")

    def bowl_ball(self):
       
        while True:
            try:
                ball = int(input(f"{self.name}, bowl the ball (1-6): "))
                if 1 <= ball <= 6:
                    return ball
                else:
                    print("Choose between 1 to 6 only!")
            except ValueError:
                print("Enter a valid number!")

class Cricket:
    def __init__(self, player_name="Player"):
        self.player = Player(player_name)
        self.computer = Player("Computer")

    def toss(self):
        
        print("Welcome to Odd or Cricket Game!")
        choice = input("Choose Odd or Even: ").lower()

        if choice not in ["odd", "even"]:
            print("Invalid choice! Defaulting to 'odd'.")
            choice = "odd"

        player_num = int(input("Enter a number (1-6): "))
        comp_num = random.randint(1, 6)
        print(f"You chose {player_num}, Computer chose {comp_num}")

        total = player_num + comp_num
        result = "odd" if total % 2 else "even"
        print(f"Total = {total} ({result.upper()})")

        if result == choice:
            print("You won the toss")
            decision = input("Choose Batting or Bowling: ").lower()
            if decision not in ["batting", "bowling"]:
                print("Invalid choice! Defaulting to batting.")
                decision = "batting"
            return decision
        else:
            print("Computer won the toss!")
            decision = random.choice(["batting", "bowling"])
            print(f"Computer chooses {decision} first.")
            return "bowling" if decision == "batting" else "batting"

    def play_innings(self, batting_player: Player, bowling_player: Player, target=None):
        print(f"\n{batting_player.name} is Batting")
        score = 0
        while True:
            if batting_player.name == "Player":
                bat = batting_player.play_shot()
                bowl = random.randint(1, 6)
                print(f"Computer bowls {bowl}")
            else:
                bat = random.randint(1, 6)
                print(f"Computer bats {bat}")
                bowl = bowling_player.bowl_ball()

            if bat == bowl:
                print("WICKET!")
                break
            else:
                score += bat
                print(f"{batting_player.name} Score: {score}")
                if target and score > target:
                    break

        batting_player.score = score
        print(f"{batting_player.name} scored {score} runs!\n")

    def start_game(self):
        first_choice = self.toss()
        player_batting_first = (first_choice == "batting")
        if player_batting_first:
            self.play_innings(self.player, self.computer)
            print(f"Computer needs {self.player.score + 1} to win!")
            self.play_innings(self.computer, self.player, target=self.player.score)
        else:
            self.play_innings(self.computer, self.player)
            print(f"You need {self.computer.score + 1} to win!")
            self.play_innings(self.player, self.computer, target=self.computer.score)

        self.show_result()

    def show_result(self):
        
        print("\nFinal Scores")
        print(f"{self.player.name}: {self.player.score}")
        print(f"{self.computer.name}: {self.computer.score}")

        if self.player.score > self.computer.score:
            print("You Win!")
        elif self.player.score < self.computer.score:
            print("Computer Wins")
        else:
            print("Match Draw")


game = Cricket("Player")
game.start_game()