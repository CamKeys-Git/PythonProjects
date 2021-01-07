# I wrote this function to randomly distribute any number of balanced teams from one group based on skill level

import random
# enter number of teams
num_teams = 3
teams = []
# each list in 'lists' is a team
for i in range(num_teams):
    teams += []

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
