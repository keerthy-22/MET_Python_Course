class CricketPlayer:
    def __init__(self, player_name, team, runs):
        self.player_name = player_name
        self.team = team
        self.runs = runs

    def display_details(self):
        print("\n------ Player Details ------")
        print("Player Name :", self.player_name)
        print("Team        :", self.team)
        print("Runs Scored :", self.runs)


# Create Five Player Objects
player1 = CricketPlayer("Virat Kohli", "India", 13848)
player2 = CricketPlayer("Rohit Sharma", "India", 11274)
player3 = CricketPlayer("Babar Azam", "Pakistan", 6200)
player4 = CricketPlayer("Joe Root", "England", 6522)
player5 = CricketPlayer("Kane Williamson", "New Zealand", 7025)

# Display Details of Each Player
player1.display_details()
player2.display_details()
player3.display_details()
player4.display_details()
player5.display_details()


#User Input
class CricketPlayer:
    def __init__(self, player_name, team, runs):
        self.player_name = player_name
        self.team = team
        self.runs = runs

    def display_details(self):
        print("\n------ Player Details ------")
        print("Player Name :", self.player_name)
        print("Team        :", self.team)
        print("Runs Scored :", self.runs)


# Create an empty list
players = []

# Get input for 5 players
for i in range(5):
    print(f"\nEnter details of Player {i + 1}")
    player_name = input("Enter Player Name: ")
    team = input("Enter Team Name: ")
    runs = int(input("Enter Runs Scored: "))

    player = CricketPlayer(player_name, team, runs)
    players.append(player)

# Display all player details
print("\n===== Cricket Player Details =====")
for player in players:
    player.display_details()
