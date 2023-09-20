import itertools
import random

def check_for_triples(team):
    team_counts = {}
    for team1 in team_schedules[team]:
        if team1 in team_counts:
            team_counts[team1] += 1
        else:
            team_counts[team1] = 1
        
    for item, count in team_counts.items():
        if count > 2:
            return True

    return False
                


# Define the number of teams and weeks
num_teams = 10
num_weeks = 14

# Create a list of team names (you can replace these with your team names)
teams = ["Erik", "Brandon", "Andrew", "Nick", "Sam", "Gavin", "Boeke", "Jack", "Chauncey", "Noah"]

# Define week 10 matchups (customize as needed)
week_10_matchups = [("Erik", "Sam"), ("Andrew", "Nick"), ("Brandon", "Noah"), ("Boeke", "Jack"), ("Chauncey", "Gavin")]

# Initialize a list to keep track of each team's schedule
team_schedules = {team: [] for team in teams}

def generate_matchups(names, i):
    is_valid = True
    while is_valid:
        random.shuffle(names)
        pairs = [[names[i], names[i + 1]] for i in range(0, len(names), 2)]
        for pair in pairs:
            pair.sort()
        for matchup in pairs:
            team1, team2 = matchup
            if i < 10:
                if team_schedules[team1].count(team2) > 0 or team_schedules[team2].count(team1) > 0:
                    is_valid = True
                    pairs = []
                    break
                else:
                    is_valid = False
                    
            elif i > 10:
                if team_schedules[team1].count(team2) >= 2 or team_schedules[team2].count(team1) >= 2:
                    is_valid = True
                    pairs = []
                    break
                else:
                    is_valid = False
    return pairs
                

# Initialize the schedule
schedule = []

# Update team schedules with week 10 matchups


# Generate the remaining weeks
for week in range(1, num_weeks+1):
    week_schedule = []
    if week == 10:
        week_schedule = week_10_matchups
    else:
        week_schedule = generate_matchups(teams, week)
    
    for matchup in week_schedule:
        team1, team2 = matchup
        team_schedules[team1].append(team2)
        team_schedules[team2].append(team1)
        
    schedule.append(week_schedule)
    

# Print the schedule
for week, matches in enumerate(schedule, start=1):
    print(f"Week {week}:")
    for match in matches:
        print(f"{match[0]} vs. {match[1]}")
    print()
    
for team in teams:
    if check_for_triples(team):
        print("INVALID SCHEDULE")
        break
