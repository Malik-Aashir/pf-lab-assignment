num_of_teams =int(input("Enter Number Of Teams: "))
total_teams_dict={}
for team in range(num_of_teams):
    team_name = input("Enter Team name: ")
    team_score =[]
    wins = int(input("Enter Win: "))
    losses = int(input("Enter Losses: "))
    team_score.extend((wins,losses))
    total_teams_dict.update({team_name:team_score})

print(total_teams_dict)