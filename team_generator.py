import random

# each list in 'lists' is a team. Add any numder of teams
teams = [[], [], []]

# each list in 'ranks' is a skill level
# enter names in appropriate list as strings separated by commas
ranks = [['top_players'], ['guys'], ['girls'], ['kids']] 

counter = 0

for rank in ranks:
    for x in range(len(rank)):
        i = random.choice(rank)
        teams[counter].append(i)
        rank.remove(i)
        if counter == len(teams)-1:
            counter = 0
        else:
            counter += 1

print(teams)









# class players:
#     def __init__(self, top_players, guys, girls, kids):
#         self.top_players = []
#         self.guys = []
#         self.girls = []
#         self.kids = []

#     def get_top_players(self, top_players):
#         return top_players
 
    

# class top_players:
#     def __init__(self, players):
#         self.players = []

#     def get_top_players(self):
#         return players    



















