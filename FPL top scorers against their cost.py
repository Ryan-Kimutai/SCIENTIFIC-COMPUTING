import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data from the FPL API
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
response = requests.get(url)
data = response.json()

# Extract player data
players = data['elements']
players_df = pd.DataFrame(players)

# Merge with team data to get team names
teams = pd.DataFrame(data['teams'])
players_df = players_df.merge(teams, left_on='team', right_on='id', suffixes=('_player', '_team'))

# Select relevant columns
players_df = players_df[['first_name', 'second_name', 'name', 'now_cost', 'total_points']]
players_df['now_cost'] = players_df['now_cost'] / 10  # Convert cost to millions

# Get the top 10 players based on total points
top_players = players_df.sort_values(by='total_points', ascending=False).head(10)

# Scatter plot: Cost vs. Total Points
plt.figure(figsize=(10, 6))
plt.scatter(players_df['now_cost'], players_df['total_points'], alpha=0.5, label="All Players")
plt.scatter(top_players['now_cost'], top_players['total_points'], color='red', label="Top 10 Players")

# Annotate top 10 players with a smaller font size
for _, row in top_players.iterrows():
    player_name = f"{row['first_name']} {row['second_name']}"
    plt.annotate(player_name, (row['now_cost'], row['total_points']), 
                 textcoords="offset points", xytext=(0,5), ha='center', fontsize=6)  # Adjust fontsize

# Labels and title
plt.xlabel('Cost (in £m)')
plt.ylabel('Total Points')
plt.title('Premier League Players: Cost vs. Total Points')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

