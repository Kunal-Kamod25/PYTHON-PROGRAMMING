class Player:
    def __init__(self, name, run, matches):
        self.name = name
        self.run = run
        self.matches = matches

    def average(self):
        # Use float division for correct average
        return self.run / self.matches if self.matches != 0 else 0


# Main program
name = input("Enter player name: ")
run = int(input("Enter player runs: "))
matches = int(input("Enter player matches: "))

p = Player(name, run, matches)

avg = p.average()
print("Avg =", avg)
